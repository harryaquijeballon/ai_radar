"""Restore grow-only queue text the unattended run may not change
(plan 2026-11-09-001 U3; fixes the P9 deadlock structurally).

Deferred-queue and source-proposal records carry free-text justification
fields that an unattended run may only grow (`GROW_ONLY_UNATTENDED`), and
every free-text field is capped at `MAX_FREE_TEXT` characters. When a run
re-encounters a record whose field is near the cap, a dated append overflows
it; the bounded repair pass then shortens the text, which rewrites history,
and the run aborts. That happened on 2026-08-05, 08-07, 09-27 and 11-05
(docs/ops/2026-11-05-queue-deadlock-recurrence-incident.md). A rephrased
field (10-30) is the same class of defect.

The fix is mechanical, so a script does it, not the model. For every record
that already existed at the base, a grow-only field is restored to its base
text when the new text either no longer contains the base text (rephrased)
or exceeds the cap (over_cap). The `last_encountered` bump and every other
change are left alone, so the re-encounter is still recorded, and the
validators still judge the result. New records, missing fields and removed
records are never touched: those remain validator findings.

Run by the workflow from the pristine copy before each validation. Writes one
derived line per restored field to --report-out (path, line, field, reason:
never the text, R43) and prints the count.
"""

from __future__ import annotations

import argparse
import glob
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "validators"))

import lib_queues  # noqa: E402

QUEUE_DIRS = ("reviews/deferred_candidates", "reviews/source_proposals")
REASON_OVER_CAP = "over_cap"
REASON_REPHRASED = "rephrased"


def restore_reason(old_value: str, new_value: str):
    """Why `new_value` must revert to `old_value`, or None if it may stand."""
    if new_value == old_value:
        return None
    if old_value not in new_value:
        return REASON_REPHRASED
    if len(new_value) > lib_queues.MAX_FREE_TEXT:
        return REASON_OVER_CAP
    return None


def normalize_text(old_text: str, new_text: str):
    """Return (normalized new text, [(line, field, reason)]). Fails safe: if
    either side does not parse, nothing is changed."""
    old_records, old_errors = lib_queues.parse_queue_file(old_text)
    new_records, new_errors = lib_queues.parse_queue_file(new_text)
    if old_errors or new_errors:
        return new_text, []
    old_by_url = {record.url: record for record in old_records}
    lines = new_text.split("\n")
    restored = []
    for record in new_records:
        old_record = old_by_url.get(record.url)
        if old_record is None:
            continue
        for field in lib_queues.GROW_ONLY_UNATTENDED:
            old_value = old_record.fields.get(field)
            new_value = record.fields.get(field)
            if old_value is None or new_value is None:
                continue
            reason = restore_reason(old_value, new_value)
            if reason is None:
                continue
            number = record.field_lines[field]
            lines[number - 1] = "- %s: %s" % (field, old_value)
            restored.append((number, field, reason))
    return "\n".join(lines), restored


def normalize_workspace(workspace: str, pristine: str):
    """Normalize every queue file present at the base; return report lines."""
    report = []
    for queue_dir in QUEUE_DIRS:
        for path in sorted(glob.glob(os.path.join(workspace, queue_dir, "*.md"))):
            rel = os.path.relpath(path, workspace)
            base_path = os.path.join(pristine, rel)
            if not os.path.isfile(base_path):
                continue
            with open(base_path, encoding="utf-8") as handle:
                old_text = handle.read()
            with open(path, encoding="utf-8") as handle:
                new_text = handle.read()
            fixed, restored = normalize_text(old_text, new_text)
            if not restored:
                continue
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(fixed)
            for number, field, reason in restored:
                report.append("RESTORED %s:%d %s %s" % (rel, number, field, reason))
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", required=True)
    parser.add_argument("--pristine", required=True)
    parser.add_argument("--report-out", default=None,
                        help="append one derived line per restored field")
    args = parser.parse_args()
    report = normalize_workspace(args.workspace, args.pristine)
    if args.report_out and report:
        with open(args.report_out, "a", encoding="utf-8") as handle:
            handle.write("\n".join(report) + "\n")
    print("queue_fields_restored=%d" % len(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
