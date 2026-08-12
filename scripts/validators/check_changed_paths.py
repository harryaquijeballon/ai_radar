"""Git-boundary and history validator (plan U3; enforces R22, R23, R41, R50).

Compares the model-writable workspace against a pristine base ref and aborts on:
- any change outside the autonomous-path allowlist (R22/R23) — including a
  tampered validator or delivery script, which is simply a protected-path hit;
- deletion of any existing file under library/ or reports/ (R50);
- modification of a report dated other than the Europe/London run date
  (past reports are immutable; future-dated reports are never written) (R50/R44);
- a non-append-only change to library/rejections.md (R50);
- a modified library entry whose pre-existing body text is not preserved, or
  whose frontmatter changes outside the permitted fields (status,
  verification, canonical_ids), with new content only in or after the
  Updates section (R50).

Pristine-base rule (R41): the harness executes the base commit's copy of this
script, with the diff computed against that same base ref via a harness-owned
git directory. The workspace copy of this file is data, never code.

Exit codes per the validator contract: 0 pass, 1 violations, 2 internal error.
All rules here are abort-class.
"""

from __future__ import annotations

import argparse
import datetime
import os
import subprocess
import sys
from typing import Dict, List, Optional, Tuple

import lib_queues
import lib_radar
from lib_radar import ABORT, Violation, emit, register_rule

register_rule("PATH_OUTSIDE_ALLOWLIST", ABORT,
              "changed path is outside the autonomous allowlist")
register_rule("HISTORY_DELETION", ABORT,
              "deletion of an existing file under a history-protected path")
register_rule("QUEUE_RECORD_REMOVED", ABORT,
              "an existing review-queue record was removed")
register_rule("QUEUE_RECORD_REWRITTEN", lib_radar.REPAIRABLE,
              "justification text must grow, never be rephrased ({field})")
register_rule("QUEUE_HISTORY_REWRITTEN", ABORT,
              "an existing review-queue record's history field changed ({field})")
register_rule("QUEUE_RESOLUTION_BY_AUTOMATION", ABORT,
              "queue lifecycle change requires human approval ({field})")
register_rule("QUEUE_UNVERIFIABLE", ABORT,
              "queue file could not be parsed for preservation checking")
register_rule("PAST_REPORT_MODIFIED", ABORT,
              "report dated before the run date ({run_date}) was changed")
register_rule("REPORT_NOT_RUN_DATE", ABORT,
              "report file is not dated with the run date ({run_date})")
register_rule("REPORT_NAME_INVALID", ABORT,
              "report filename is not a YYYY-MM-DD date")
register_rule("REJECTIONS_NOT_APPEND_ONLY", ABORT,
              "rejection log changed other than by appending")
register_rule("ENTRY_FRONTMATTER_FIELD_CHANGED", ABORT,
              "entry frontmatter field {field} may not change in automation")
register_rule("ENTRY_BODY_REWRITTEN", ABORT,
              "entry body text before or within existing content was altered")
register_rule("ENTRY_UNVERIFIABLE", ABORT,
              "entry could not be parsed for preservation checking")
register_rule("CHANGE_UNSUPPORTED", ABORT,
              "git reported a change type this validator does not accept ({code})")

PERMITTED_ENTRY_FIELD_CHANGES = ("status", "verification", "canonical_ids")
UPDATES_HEADING = "## Updates"
# Both placeholder spellings are removable: engine/templates/entry.md writes
# "None yet." (the form in the live library), "*(none yet)*" is the legacy
# form this validator originally shipped with (2026-08-12 alignment; see
# docs/ops/2026-08-12-validation-abort-review.md).
UPDATES_PLACEHOLDERS = ("*(none yet)*", "None yet.")
HISTORY_PROTECTED_PREFIXES = ("library/", "reports/", "reviews/")
MODE_UNATTENDED = "unattended"
MODE_MANUAL = "manual"


# --- Git access --------------------------------------------------------------

def _git(args: List[str], work_tree: str, git_dir: Optional[str]) -> bytes:
    command = ["git"]
    if git_dir:
        command += ["--git-dir", git_dir, "--work-tree", work_tree]
    command += args
    result = subprocess.run(command, cwd=work_tree, capture_output=True, check=True)
    return result.stdout


def collect_changes(base_ref: str, work_tree: str,
                    git_dir: Optional[str] = None) -> List[Tuple[str, str]]:
    """(status, path) pairs for every difference between base and workspace.
    Renames/copies decompose into delete+add. Untracked files are adds."""
    changes: List[Tuple[str, str]] = []
    raw = _git(["diff", "--name-status", "-z", "--no-renames", base_ref, "--"],
               work_tree, git_dir)
    parts = [part.decode("utf-8", "replace") for part in raw.split(b"\0") if part]
    index = 0
    while index < len(parts):
        code = parts[index]
        if code[:1] in ("A", "M", "D", "T"):
            status = "M" if code[:1] == "T" else code[:1]
            changes.append((status, parts[index + 1]))
            index += 2
        elif code[:1] in ("R", "C"):
            changes.append(("D", parts[index + 1]))
            changes.append(("A", parts[index + 2]))
            index += 3
        else:
            changes.append(("?" + code, parts[index + 1] if index + 1 < len(parts) else ""))
            index += 2
    untracked = _git(["ls-files", "--others", "--exclude-standard", "-z"],
                     work_tree, git_dir)
    for part in untracked.split(b"\0"):
        if part:
            changes.append(("A", part.decode("utf-8", "replace")))
    return changes


def base_content(base_ref: str, path: str, work_tree: str,
                 git_dir: Optional[str] = None) -> Optional[str]:
    try:
        return _git(["show", "%s:%s" % (base_ref, path)],
                    work_tree, git_dir).decode("utf-8", "replace")
    except subprocess.CalledProcessError:
        return None


def workspace_content(work_tree: str, path: str) -> Optional[str]:
    full = os.path.join(work_tree, path)
    if not os.path.isfile(full):
        return None
    with open(full, encoding="utf-8", errors="replace") as handle:
        return handle.read()


# --- Pure checks -------------------------------------------------------------

def path_in_allowlist(path: str) -> bool:
    if path in lib_radar.AUTONOMOUS_FILE_ALLOWLIST:
        return True
    return any(path.startswith(prefix) for prefix in lib_radar.AUTONOMOUS_DIR_ALLOWLIST)


def _report_date(path: str) -> Optional[datetime.date]:
    return lib_radar.parse_iso_date(os.path.basename(path)[:-3])


def check_change(status: str, path: str,
                 run_date: datetime.date) -> List[Violation]:
    """Path-level rules for one change. Content-level rules are separate."""
    if status.startswith("?"):
        return [emit("CHANGE_UNSUPPORTED", path, code=status[1:])]
    violations: List[Violation] = []
    if not path_in_allowlist(path):
        return [emit("PATH_OUTSIDE_ALLOWLIST", path)]
    if status == "D" and any(path.startswith(prefix)
                             for prefix in HISTORY_PROTECTED_PREFIXES):
        violations.append(emit("HISTORY_DELETION", path))
    if path.startswith("reports/") and path.endswith(".md") and status != "D":
        date = _report_date(path)
        if date is None:
            violations.append(emit("REPORT_NAME_INVALID", path))
        elif date < run_date:
            violations.append(emit("PAST_REPORT_MODIFIED", path,
                                   run_date=run_date.isoformat()))
        elif date > run_date:
            violations.append(emit("REPORT_NOT_RUN_DATE", path,
                                   run_date=run_date.isoformat()))
    return violations


def check_rejections_append_only(path: str, old: Optional[str],
                                 new: Optional[str]) -> List[Violation]:
    if old is None or new is None:
        return [emit("REJECTIONS_NOT_APPEND_ONLY", path)]
    if not new.startswith(old):
        return [emit("REJECTIONS_NOT_APPEND_ONLY", path)]
    return []


def _is_subsequence(needle: List[str], haystack: List[str]) -> bool:
    position = 0
    for line in haystack:
        if position < len(needle) and line == needle[position]:
            position += 1
    return position == len(needle)


def check_entry_preservation(path: str, old: Optional[str],
                             new: Optional[str]) -> List[Violation]:
    """Frontmatter: only permitted fields may change. Body: everything before
    the Updates heading is byte-identical; from the heading on, existing lines
    survive in order (insertions allowed, either Updates placeholder may go)."""
    if old is None or new is None:
        return [emit("ENTRY_UNVERIFIABLE", path)]
    old_fm = lib_radar.parse_frontmatter(old)
    new_fm = lib_radar.parse_frontmatter(new)
    if old_fm.errors or new_fm.errors:
        return [emit("ENTRY_UNVERIFIABLE", path)]

    violations: List[Violation] = []
    keys = set(old_fm.fields) | set(new_fm.fields)
    for key in sorted(keys):
        if old_fm.fields.get(key) != new_fm.fields.get(key):
            if key not in PERMITTED_ENTRY_FIELD_CHANGES:
                violations.append(emit("ENTRY_FRONTMATTER_FIELD_CHANGED",
                                       path, field=key))

    old_body = old.split("\n")[old_fm.body_start - 1:]
    new_body = new.split("\n")[new_fm.body_start - 1:]
    try:
        old_heading = old_body.index(UPDATES_HEADING)
    except ValueError:
        old_heading = len(old_body)
    try:
        new_heading = new_body.index(UPDATES_HEADING)
    except ValueError:
        new_heading = len(new_body)

    if old_body[:old_heading] != new_body[:new_heading]:
        violations.append(emit("ENTRY_BODY_REWRITTEN", path))
        return violations
    old_rest = [line for line in old_body[old_heading:]
                if line.strip() not in UPDATES_PLACEHOLDERS]
    new_rest = new_body[new_heading:]
    if not _is_subsequence(old_rest, new_rest):
        violations.append(emit("ENTRY_BODY_REWRITTEN", path))
    return violations


def check_queue_preservation(path: str, old: Optional[str], new: Optional[str],
                             mode: str) -> List[Violation]:
    """Queue files are audit trail (user decision at U3 checkpoint): existing
    records survive; unattended runs may append pending records, bump
    last_encountered, and grow justification text — never resolve, dismiss,
    promote, reject, or rewrite. Manual mode permits lifecycle transitions
    (human-approved resolutions) but still never removals or history rewrites."""
    if old is None or new is None:
        return [emit("QUEUE_UNVERIFIABLE", path)]
    old_records, old_errors = lib_queues.parse_queue_file(old)
    new_records, new_errors = lib_queues.parse_queue_file(new)
    if old_errors or new_errors:
        return [emit("QUEUE_UNVERIFIABLE", path)]
    violations: List[Violation] = []
    new_by_url = {record.url: record for record in new_records}
    kind = lib_queues.queue_type(path)
    resolved = set(lib_queues.status_values(kind or lib_queues.QUEUE_DEFERRED)) - {"pending"}

    for old_record in old_records:
        new_record = new_by_url.get(old_record.url)
        if new_record is None:
            violations.append(emit("QUEUE_RECORD_REMOVED", path, old_record.line))
            continue
        for key in sorted(set(old_record.fields) | set(new_record.fields)):
            old_value = old_record.fields.get(key)
            new_value = new_record.fields.get(key)
            if old_value == new_value:
                continue
            if key in lib_queues.MUTABLE_UNATTENDED:
                continue
            if key in lib_queues.GROW_ONLY_UNATTENDED and old_value is not None \
                    and new_value is not None and old_value in new_value:
                continue
            lifecycle = (key == "status"
                         or key in ("resolution", "resolution_date", "linked_ref"))
            if lifecycle:
                if mode == MODE_MANUAL:
                    continue
                violations.append(emit("QUEUE_RESOLUTION_BY_AUTOMATION",
                                       path, new_record.line, field=key))
            elif key in lib_queues.GROW_ONLY_UNATTENDED:
                # A rephrased justification is a content defect the bounded
                # repair pass may fix (restore + append); revalidation still
                # enforces grow-only before anything can be committed (R42).
                violations.append(emit("QUEUE_RECORD_REWRITTEN",
                                       path, new_record.line, field=key))
            else:
                violations.append(emit("QUEUE_HISTORY_REWRITTEN",
                                       path, new_record.line, field=key))
    if mode == MODE_UNATTENDED:
        old_urls = {record.url for record in old_records}
        for new_record in new_records:
            if new_record.url not in old_urls \
                    and new_record.fields.get("status") in resolved:
                violations.append(emit("QUEUE_RESOLUTION_BY_AUTOMATION",
                                       path, new_record.line, field="status"))
    return violations


# --- Orchestration -----------------------------------------------------------

def validate(base_ref: str, work_tree: str, git_dir: Optional[str],
             run_date: datetime.date,
             mode: str = MODE_UNATTENDED) -> List[Violation]:
    violations: List[Violation] = []
    for status, path in collect_changes(base_ref, work_tree, git_dir):
        violations.extend(check_change(status, path, run_date))
        if status == "M" and path == "library/rejections.md":
            violations.extend(check_rejections_append_only(
                path, base_content(base_ref, path, work_tree, git_dir),
                workspace_content(work_tree, path)))
        if status == "M" and path.startswith("library/entries/"):
            violations.extend(check_entry_preservation(
                path, base_content(base_ref, path, work_tree, git_dir),
                workspace_content(work_tree, path)))
        if status == "M" and path.startswith("reviews/"):
            violations.extend(check_queue_preservation(
                path, base_content(base_ref, path, work_tree, git_dir),
                workspace_content(work_tree, path), mode))
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="pristine base ref (sha or origin/main)")
    parser.add_argument("--work-tree", default=".", help="model workspace to inspect")
    parser.add_argument("--git-dir", default=None,
                        help="harness-owned git directory (R41); workspace .git is never trusted in automation")
    parser.add_argument("--run-date", default=None,
                        help="YYYY-MM-DD Europe/London run date (default: today in Europe/London)")
    parser.add_argument("--mode", choices=[MODE_UNATTENDED, MODE_MANUAL],
                        default=MODE_UNATTENDED,
                        help="unattended (default) forbids queue lifecycle transitions; "
                             "manual permits human-approved resolutions")
    args = parser.parse_args()
    if args.run_date:
        run_date = lib_radar.parse_iso_date(args.run_date)
        if run_date is None:
            print("INTERNAL VALIDATOR_ERROR - BadRunDate")
            return lib_radar.EXIT_INTERNAL
    else:
        run_date = lib_radar.london_today()
    violations = validate(args.base, args.work_tree, args.git_dir, run_date,
                          mode=args.mode)
    return lib_radar.report(violations)


if __name__ == "__main__":
    sys.exit(lib_radar.run_main(main))
