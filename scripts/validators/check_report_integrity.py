"""Report integrity validator (plan U4; enforces R6, R17, and the report-side
of R39).

For the run-date report of each domain: every substantive item must resolve to
a library entry that exists, is `accepted`, `verified`, and rated `high` for
the reporting domain; at most 3 items; a quiet-day report (zero items) must
carry the quiet-day statement and the scan-evidence block.

Classes per plan: a report item without a resolvable entry is abort-class (the
defining failure, AE5); eligibility and count defects are repairable.

DRAFT scan-evidence block (finalized in U5), required on quiet days:

    ## Scan evidence
    - curated sources fetched: 12
    - queries executed: 5
"""

from __future__ import annotations

import argparse
import datetime
import os
import re
import sys
from typing import List, Optional, Tuple

import lib_radar
from lib_radar import ABORT, REPAIRABLE, Violation, emit, register_rule

register_rule("REPORT_ITEM_NO_ENTRY_LINK", ABORT,
              "report item has no library entry link")
register_rule("REPORT_ENTRY_MISSING", ABORT,
              "report item links an entry that does not exist")
register_rule("REPORT_ITEM_NOT_ELIGIBLE", REPAIRABLE,
              "report item entry fails the report bar ({reason})")
register_rule("REPORT_TOO_MANY_ITEMS", REPAIRABLE,
              "report has more than 3 items ({count})")
register_rule("REPORT_QUIET_DAY_STATEMENT_MISSING", REPAIRABLE,
              "zero-item report lacks the quiet-day statement")
register_rule("REPORT_SCAN_EVIDENCE_MISSING", REPAIRABLE,
              "quiet-day report lacks a well-formed scan-evidence block")

ITEMS_HEADING = "## Today's developments"
QUIET_PHRASE = "No material developments cleared the reporting bar"
ENTRY_LINK_RE = re.compile(r"\(\.\./\.\./\.\./library/entries/([A-Za-z0-9._-]+)\.md\)")
ITEM_RE = re.compile(r"^### ")
EVIDENCE_HEADING = "## Scan evidence"
EVIDENCE_LINE_RE = re.compile(r"^- (curated sources fetched|queries executed): (\d+)$")


def _split_items(text: str) -> Tuple[List[str], str]:
    """Item blocks under 'Today's developments', plus the whole text."""
    lines = text.split("\n")
    items: List[str] = []
    inside = False
    current: List[str] = []
    for line in lines:
        if line.startswith("## "):
            if inside and current:
                items.append("\n".join(current))
                current = []
            inside = line.strip() == ITEMS_HEADING
            continue
        if inside and ITEM_RE.match(line):
            if current:
                items.append("\n".join(current))
            current = [line]
        elif inside and current:
            current.append(line)
    if inside and current:
        items.append("\n".join(current))
    return items, text


def _has_evidence_block(text: str) -> bool:
    lines = text.split("\n")
    try:
        start = next(index for index, line in enumerate(lines)
                     if line.strip() == EVIDENCE_HEADING)
    except StopIteration:
        return False
    found = set()
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        match = EVIDENCE_LINE_RE.match(line.strip())
        if match:
            found.add(match.group(1))
    return found == {"curated sources fetched", "queries executed"}


def _entry_fields(workspace: str, slug: str):
    path = os.path.join(workspace, "library", "entries", slug + ".md")
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as handle:
        return lib_radar.parse_frontmatter(handle.read()).fields


def validate_report(workspace: str, domain: str, run_date: datetime.date) -> List[Violation]:
    rel = "reports/%s/daily/%s.md" % (domain, run_date.isoformat())
    full = os.path.join(workspace, rel)
    if not os.path.isfile(full):
        return []  # absence of today's report is the harness's concern, not content integrity
    with open(full, encoding="utf-8", errors="replace") as handle:
        text = handle.read()
    items, _ = _split_items(text)
    violations: List[Violation] = []

    if len(items) > 3:
        violations.append(emit("REPORT_TOO_MANY_ITEMS", rel, count=len(items)))

    for item in items:
        match = ENTRY_LINK_RE.search(item)
        if not match:
            violations.append(emit("REPORT_ITEM_NO_ENTRY_LINK", rel))
            continue
        slug = match.group(1)
        fields = _entry_fields(workspace, slug)
        if fields is None:
            violations.append(emit("REPORT_ENTRY_MISSING", rel))
            continue
        if fields.get("status") != "accepted":
            violations.append(emit("REPORT_ITEM_NOT_ELIGIBLE", rel,
                                   reason="status not accepted"))
        if fields.get("verification") != "verified":
            violations.append(emit("REPORT_ITEM_NOT_ELIGIBLE", rel,
                                   reason="not verified"))
        relevance = fields.get("relevance")
        tier = relevance.get(domain) if isinstance(relevance, dict) else None
        if tier != "high":
            violations.append(emit("REPORT_ITEM_NOT_ELIGIBLE", rel,
                                   reason="relevance not high for domain"))

    if not items:
        if QUIET_PHRASE not in text:
            violations.append(emit("REPORT_QUIET_DAY_STATEMENT_MISSING", rel))
        if not _has_evidence_block(text):
            violations.append(emit("REPORT_SCAN_EVIDENCE_MISSING", rel))
    return violations


def validate(workspace: str, run_date: datetime.date) -> List[Violation]:
    violations: List[Violation] = []
    for domain in lib_radar.DOMAINS:
        violations.extend(validate_report(workspace, domain, run_date))
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", default=".", help="repo root to inspect")
    parser.add_argument("--run-date", default=None, help="YYYY-MM-DD Europe/London")
    args = parser.parse_args()
    if args.run_date:
        run_date = lib_radar.parse_iso_date(args.run_date)
        if run_date is None:
            print("INTERNAL VALIDATOR_ERROR - BadRunDate")
            return lib_radar.EXIT_INTERNAL
    else:
        run_date = lib_radar.london_today()
    return lib_radar.report(validate(args.workspace, run_date))


if __name__ == "__main__":
    sys.exit(lib_radar.run_main(main))
