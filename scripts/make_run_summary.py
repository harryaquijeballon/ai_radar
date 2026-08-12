"""Safe run-summary generator (plan U4; enforces R37, summary-side R39, R47).

Emits the GitHub Actions job-summary markdown. Safe by construction: every
line is built from fixed strings, counts, controlled vocabularies (outcome
classes, reason classes), redaction-checked paths, and validated metadata
(commit sha pattern, boolean secret readiness). There is no code path that
places entry text, candidate content, deferral reasons beyond their controlled
class, token material, or any model-generated free text into the output.

Run from the pristine base copy (R41); reads the workspace read-only.
"""

from __future__ import annotations

import argparse
import datetime
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "validators"))

import check_changed_paths as ccp  # noqa: E402
import lib_queues  # noqa: E402
import lib_radar  # noqa: E402

OUTCOMES = ("success", "no-change", "auth", "tooling", "validation", "push")
_SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")
_ITEM_RE = re.compile(r"^### ", re.MULTILINE)


def _count_report_items(workspace: str, domain: str,
                        run_date: datetime.date) -> int:
    path = os.path.join(workspace, "reports", domain, "daily",
                        "%s.md" % run_date.isoformat())
    if not os.path.isfile(path):
        return 0
    with open(path, encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    import check_report_integrity as cri
    items, _ = cri._split_items(text)
    return len(items)


def _entry_change_counts(workspace: str, base_ref: str, git_dir):
    added = modified = provisional = 0
    rejections_added = 0
    for status, path in ccp.collect_changes(base_ref, workspace, git_dir):
        if path.startswith("library/entries/") and status == "A":
            added += 1
            text = ccp.workspace_content(workspace, path) or ""
            if lib_radar.parse_frontmatter(text).fields.get("status") == "provisional":
                provisional += 1
        elif path.startswith("library/entries/") and status == "M":
            modified += 1
        elif path == "library/rejections.md" and status == "M":
            old = ccp.base_content(base_ref, path, workspace, git_dir) or ""
            new = ccp.workspace_content(workspace, path) or ""
            if new.startswith(old):
                rejections_added = max(0, new.count("\n") - old.count("\n"))
    return added, modified, provisional, rejections_added


def _new_queue_records(workspace: str, base_ref: str, git_dir, queue_kind: str):
    """New records per file vs base; deferred returns reason-class counts."""
    by_class: dict = {}
    total = 0
    for status, path in ccp.collect_changes(base_ref, workspace, git_dir):
        if lib_queues.queue_type(path) != queue_kind or status not in ("A", "M"):
            continue
        new_text = ccp.workspace_content(workspace, path) or ""
        old_text = (ccp.base_content(base_ref, path, workspace, git_dir) or "") \
            if status == "M" else ""
        new_records, new_errors = lib_queues.parse_queue_file(new_text)
        old_records, old_errors = lib_queues.parse_queue_file(old_text)
        if new_errors or old_errors:
            continue  # structure violations are the validators' report, not ours
        old_urls = {record.url for record in old_records}
        for record in new_records:
            if record.url in old_urls:
                continue
            total += 1
            reason_class = record.fields.get("reason_class", "other")
            if reason_class not in lib_queues.REASON_CLASSES:
                reason_class = "other"
            by_class[reason_class] = by_class.get(reason_class, 0) + 1
    return total, by_class


def _evidence_counts(evidence_path):
    """Per-domain (queries, fetches) from the scan-evidence artifact.
    Fail closed: anything absent, malformed, or non-integer yields None for
    that domain — never a string taken from the file (no-echo, R47)."""
    counts = {domain: None for domain in lib_radar.DOMAINS}
    if not evidence_path or not os.path.isfile(evidence_path):
        return counts
    try:
        import json
        with open(evidence_path, encoding="utf-8") as handle:
            domains = json.load(handle).get("domains", {})
    except (OSError, ValueError, AttributeError):
        return counts
    for domain in lib_radar.DOMAINS:
        section = domains.get(domain) if isinstance(domains, dict) else None
        if not isinstance(section, dict):
            continue
        queries = section.get("queries_executed")
        fetches = section.get("curated_sources_fetched")
        if isinstance(queries, int) and isinstance(fetches, int) \
                and not isinstance(queries, bool) and not isinstance(fetches, bool) \
                and queries >= 0 and fetches >= 0:
            counts[domain] = (queries, fetches)
    return counts


def build_summary(workspace: str, base_ref: str, git_dir, run_date: datetime.date,
                  outcome: str, attempts: int, commit: str,
                  oauth_ready: bool, artifacts_note: bool,
                  evidence_path: str = None) -> str:
    added, modified, provisional, rejections = _entry_change_counts(
        workspace, base_ref, git_dir)
    deferred_total, deferred_by_class = _new_queue_records(
        workspace, base_ref, git_dir, lib_queues.QUEUE_DEFERRED)
    proposals_total, _ = _new_queue_records(
        workspace, base_ref, git_dir, lib_queues.QUEUE_PROPOSALS)

    complete = outcome in ("success", "no-change")
    sha = commit if commit and _SHA_RE.match(commit) else None

    lines = []
    lines.append("# Radar run summary - %s" % run_date.isoformat())
    lines.append("")
    lines.append("| field | value |")
    lines.append("|---|---|")
    lines.append("| outcome | %s |" % (outcome if outcome in OUTCOMES else "unknown"))
    lines.append("| run status | %s |"
                 % ("completed" if complete else "operationally incomplete"))
    lines.append("| attempts | %d |" % attempts)
    lines.append("| new accepted entries | %d |" % (added - provisional))
    lines.append("| new provisional entries | %d |" % provisional)
    lines.append("| updated or merged entries | %d |" % modified)
    lines.append("| rejections logged | %d |" % rejections)
    lines.append("| source proposals (pending) | %d |" % proposals_total)
    lines.append("| deferred candidates | %d |" % deferred_total)
    for reason_class in lib_queues.REASON_CLASSES:
        if reason_class in deferred_by_class:
            lines.append("| deferred: %s | %d |"
                         % (reason_class, deferred_by_class[reason_class]))
    evidence = _evidence_counts(evidence_path)
    for domain in lib_radar.DOMAINS:
        pair = evidence.get(domain)
        lines.append("| scan queries (%s) | %s |"
                     % (domain, pair[0] if pair else "unavailable"))
        lines.append("| scan fetches (%s) | %s |"
                     % (domain, pair[1] if pair else "unavailable"))
    for domain in lib_radar.DOMAINS:
        count = _count_report_items(workspace, domain, run_date)
        report_rel = "reports/%s/daily/%s.md" % (domain, run_date.isoformat())
        lines.append("| report items (%s) | %d |" % (domain, count))
        lines.append("| report file (%s) | %s |"
                     % (domain, lib_radar.safe_path(report_rel)))
    lines.append("| commit | %s |" % (sha if sha else "none"))
    lines.append("| oauth secret ready | %s |" % ("yes" if oauth_ready else "no"))
    if artifacts_note:
        lines.append("| diagnostics | preserved as workflow artifacts |")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--base", required=True)
    parser.add_argument("--git-dir", default=None)
    parser.add_argument("--run-date", default=None)
    parser.add_argument("--outcome", required=True, choices=OUTCOMES)
    parser.add_argument("--attempts", type=int, default=1)
    parser.add_argument("--commit", default="")
    parser.add_argument("--oauth-ready", choices=["true", "false"], default="false")
    parser.add_argument("--artifacts", action="store_true",
                        help="note that diagnostics were preserved as artifacts")
    args = parser.parse_args()
    run_date = (lib_radar.parse_iso_date(args.run_date)
                if args.run_date else lib_radar.london_today())
    if run_date is None:
        print("INTERNAL VALIDATOR_ERROR - BadRunDate")
        return lib_radar.EXIT_INTERNAL
    print(build_summary(args.workspace, args.base, args.git_dir, run_date,
                        args.outcome, args.attempts, args.commit,
                        args.oauth_ready == "true", args.artifacts))
    return lib_radar.EXIT_PASS


if __name__ == "__main__":
    sys.exit(lib_radar.run_main(main))
