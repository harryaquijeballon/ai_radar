"""Review-queue structure validator (plan U4; enforces R12-R14, R19).

Validates the state of a queue file (deferred candidates or source proposals):
record shape, required fields, controlled vocabularies, ISO dates, URL hygiene
(no credentials, no token or tracking parameters), metadata-only heuristics
(no fenced blocks, bounded single-line free text), and duplicate detection —
within the file and against the sibling domain's file (cross-domain deferrals
hold one record; plan Key Decisions).

All rules repairable-class (content defects; R42) — path-level protection of
these files lives in check_changed_paths.py.
"""

from __future__ import annotations

import argparse
import glob
import os
import sys
from typing import List, Optional

import lib_queues
import lib_radar
from lib_radar import REPAIRABLE, Violation, emit, register_rule

register_rule("QUEUE_MALFORMED", REPAIRABLE,
              "queue file line is not a record heading, field, or comment ({reason})")
register_rule("QUEUE_FIELD_MISSING", REPAIRABLE,
              "queue record is missing required field {field}")
register_rule("QUEUE_FIELD_INVALID", REPAIRABLE,
              "queue record field {field} is outside the controlled vocabulary")
register_rule("QUEUE_FIELD_UNKNOWN", REPAIRABLE,
              "queue record field {field} is not part of the record schema")
register_rule("QUEUE_URL_UNSAFE", REPAIRABLE,
              "record URL failed hygiene checks ({reason})")
register_rule("QUEUE_TEXT_TOO_LONG", REPAIRABLE,
              "free-text field {field} exceeds the metadata-only length bound")
register_rule("QUEUE_CONTENT_BLOCK", REPAIRABLE,
              "queue file contains a fenced block - captured content is prohibited")
register_rule("DUPLICATE_QUEUE_RECORD", REPAIRABLE,
              "record URL duplicates another record ({where})")

_DATE_FIELDS = ("first_encountered", "last_encountered", "first_discovered",
                "resolution_date")


def _sibling_paths(path: str) -> List[str]:
    directory = os.path.dirname(os.path.abspath(path))
    return [candidate for candidate in sorted(glob.glob(os.path.join(directory, "*.md")))
            if os.path.abspath(candidate) != os.path.abspath(path)]


def validate_file(path: str, text: str,
                  sibling_texts: Optional[List[str]] = None) -> List[Violation]:
    kind = lib_queues.queue_type(path)
    if kind is None:
        return [emit("QUEUE_MALFORMED", path, None, reason="unknown-queue-type")]
    violations: List[Violation] = []

    for number, line in enumerate(text.split("\n"), start=1):
        if line.strip().startswith("```"):
            violations.append(emit("QUEUE_CONTENT_BLOCK", path, number))

    records, errors = lib_queues.parse_queue_file(text)
    for line, reason in errors:
        violations.append(emit("QUEUE_MALFORMED", path, line, reason=reason))

    seen: dict = {}
    for record in records:
        reason = lib_queues.url_unsafe_reason(record.url)
        if reason:
            violations.append(emit("QUEUE_URL_UNSAFE", path, record.line,
                                   reason=reason))
        if record.url in seen:
            violations.append(emit("DUPLICATE_QUEUE_RECORD", path, record.line,
                                   where="same file"))
        seen[record.url] = record

        for field in lib_queues.required_fields(kind):
            if not record.fields.get(field):
                violations.append(emit("QUEUE_FIELD_MISSING", path, record.line,
                                       field=field))
        for field in record.fields:
            if field not in lib_queues.known_fields(kind):
                violations.append(emit("QUEUE_FIELD_UNKNOWN", path, record.line,
                                       field=field))
        status = record.fields.get("status")
        if status and status not in lib_queues.status_values(kind):
            violations.append(emit("QUEUE_FIELD_INVALID", path, record.line,
                                   field="status"))
        if kind == lib_queues.QUEUE_DEFERRED:
            reason_class = record.fields.get("reason_class")
            if reason_class and reason_class not in lib_queues.REASON_CLASSES:
                violations.append(emit("QUEUE_FIELD_INVALID", path, record.line,
                                       field="reason_class"))
        domain = record.fields.get("domain")
        if domain and not all(part.strip() in lib_radar.DOMAINS
                              for part in domain.split(",")):
            violations.append(emit("QUEUE_FIELD_INVALID", path, record.line,
                                   field="domain"))
        for field in _DATE_FIELDS:
            value = record.fields.get(field)
            if value and lib_radar.parse_iso_date(value) is None:
                violations.append(emit("QUEUE_FIELD_INVALID", path, record.line,
                                       field=field))
        for field in lib_queues.FREE_TEXT_FIELDS:
            value = record.fields.get(field)
            if value and len(value) > lib_queues.MAX_FREE_TEXT:
                violations.append(emit("QUEUE_TEXT_TOO_LONG", path, record.line,
                                       field=field))

    for sibling in (sibling_texts or []):
        sibling_records, sibling_errors = lib_queues.parse_queue_file(sibling)
        if sibling_errors:
            continue
        for record in sibling_records:
            if record.url in seen:
                violations.append(emit("DUPLICATE_QUEUE_RECORD", path,
                                       seen[record.url].line,
                                       where="sibling domain file"))
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="queue files to validate")
    args = parser.parse_args()
    violations: List[Violation] = []
    for path in args.paths:
        with open(path, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
        siblings = []
        for sibling_path in _sibling_paths(path):
            with open(sibling_path, encoding="utf-8", errors="replace") as handle:
                siblings.append(handle.read())
        rel = os.path.relpath(path)
        violations.extend(validate_file(rel, text, siblings))
    return lib_radar.report(violations)


if __name__ == "__main__":
    sys.exit(lib_radar.run_main(main))
