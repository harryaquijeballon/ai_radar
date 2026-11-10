"""Entry write guard: a PreToolUse hook on the model's Write tool
(plan 2026-11-09-001 U7b; docs/ops/2026-11-10-dedup-miss-incident.md).

Not a validator. The harness registers this script as a hook in the model's
settings (`build_claude_settings.py`), so the CLI runs it before every
Write. The model has no shell and cannot run or skip it. It applies the
mechanical part of dedup (`engine/schema.md`, "Dedup matching", rule 1) at
the moment of the write, and tells the agent what to do instead, so the
agent corrects itself in the same run:

- `ENTRY_EXISTS`: a Write whose target is an entry already in the base
  commit. Existing entries change only by Edit (append to Updates).
- `ENTRY_DUPLICATE`: a Write of a new entry whose `canonical_ids` or
  source URL already belong to another entry, in the base commit or
  written earlier in this run.

Hook contract: the tool call arrives as JSON on stdin; exit 2 blocks the
call and returns stderr to the model; exit 0 lets it through.

The guard fails OPEN: on any error of its own it lets the write through.
The validators stay the gate (`ENTRY_BODY_REWRITTEN`,
`ENTRY_DUPLICATE_IDENTIFIER`); a guard fault must never stop a scan.

The log holds derived lines only (`BLOCKED <rule> <safe path>`), never the
content of the write.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "validators"))

import lib_dedup  # noqa: E402
import lib_radar  # noqa: E402

EXISTS_MESSAGE = (
    "ENTRY_EXISTS %(rel)s is already in the library and must not be written "
    "over. This candidate is a re-encounter, not a new development: write no "
    "new entry and do not list it as new in a report. Only if the source "
    "carries materially new information, use Edit to append one dated line to "
    "that entry's Updates section (engine/schema.md, Merge / link). Then "
    "continue the scan.")
DUPLICATE_MESSAGE = (
    "ENTRY_DUPLICATE this development is already archived as "
    "library/entries/%(slug)s.md (shared identifier: %(key)s). Write no new "
    "entry and do not list it as new in a report. Only if the source carries "
    "materially new information, use Edit to append one dated line to that "
    "entry's Updates section (engine/schema.md, Merge / link). Then continue "
    "the scan.")


def evaluate(payload: dict, workspace: str, pristine: str):
    """Return None to allow, or (rule, message, safe_rel_path) to block."""
    if payload.get("tool_name") != "Write":
        return None
    tool_input = payload.get("tool_input") or {}
    file_path = tool_input.get("file_path")
    if not isinstance(file_path, str) or not file_path:
        return None
    if not os.path.isabs(file_path):
        file_path = os.path.join(payload.get("cwd") or workspace, file_path)
    target = os.path.realpath(file_path)
    entries_dir = os.path.realpath(
        os.path.join(workspace, "library", "entries"))
    if os.path.dirname(target) != entries_dir or not target.endswith(".md"):
        return None
    name = os.path.basename(target)
    slug = name[:-3]
    rel = "library/entries/" + name
    safe_rel = lib_radar.safe_path(rel)

    if os.path.isfile(os.path.join(pristine, "library", "entries", name)):
        return ("ENTRY_EXISTS", EXISTS_MESSAGE % {"rel": rel}, safe_rel)

    content = tool_input.get("content")
    if not isinstance(content, str):
        return None
    keys = lib_dedup.all_keys(lib_radar.parse_frontmatter(content).fields)
    if not keys:
        return None
    # The base commit first, then entries written earlier in this run.
    for root in (pristine, workspace):
        known = lib_dedup.library_keys(root, skip_slugs=(slug,))
        for key in sorted(keys):
            if key in known:
                shown = key[4:] if key.startswith("url:") else key
                return ("ENTRY_DUPLICATE",
                        DUPLICATE_MESSAGE % {"slug": known[key], "key": shown},
                        safe_rel)
    return None


def _log(path, line: str) -> None:
    if not path:
        return
    try:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(line + "\n")
    except OSError:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--pristine", required=True)
    parser.add_argument("--log", default=None)
    args = parser.parse_args()
    try:
        decision = evaluate(json.load(sys.stdin), args.workspace, args.pristine)
    except Exception as error:  # fail open; the validators are the gate
        _log(args.log, "GUARD_ERROR %s" % type(error).__name__)
        return 0
    if decision is None:
        return 0
    rule, message, safe_rel = decision
    _log(args.log, "BLOCKED %s %s" % (rule, safe_rel))
    sys.stderr.write(message + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
