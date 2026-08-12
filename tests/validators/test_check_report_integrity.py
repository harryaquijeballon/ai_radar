"""Tests for check_report_integrity.py (plan U4; R6, R17, report-side R39)."""

import datetime
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import check_report_integrity as cri  # noqa: E402

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures", "entries")
RUN_DATE = datetime.date(2026, 7, 23)
REPORT = "reports/social_science/daily/2026-07-23.md"

ITEM_TEMPLATE = (
    "### %d. %s (academic, Author, 2026)\n\n"
    "**Why it matters:** short paragraph.\n\n"
    "**Source:** https://example.org/x . **Library entry:** "
    "[%s](../../../library/entries/%s.md)\n"
    "**Selected because:** rationale line.\n\n"
)

QUIET_BODY = (
    "# Social science radar - 2026-07-23\n\n"
    "Window searched: 2026-07-22 to 2026-07-23.\n\n"
    "## Today's developments\n\n"
    "The social science radar searched its window across curated sources and "
    "open search. No material developments cleared the reporting bar today.\n\n"
    "## Scan evidence\n\n"
    "- curated sources fetched: 12\n"
    "- queries executed: 5\n"
)


def report_with_items(slugs):
    body = ("# Social science radar - 2026-07-23\n\n"
            "Window searched: 2026-07-22 to 2026-07-23.\n\n"
            "## Today's developments\n\n")
    for number, slug in enumerate(slugs, start=1):
        body += ITEM_TEMPLATE % (number, "Title %d" % number, slug, slug)
    body += "## Also archived today\n\n- nothing else\n"
    return body


class TestReportIntegrity(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="radar-u4ri-")
        self.workspace = self._tmp.name
        entries = os.path.join(self.workspace, "library", "entries")
        os.makedirs(entries)
        os.makedirs(os.path.join(self.workspace,
                                 "reports", "social_science", "daily"))
        shutil.copy(os.path.join(
            FIXTURES, "2023-korinek-genai-economic-research.md"), entries)
        shutil.copy(os.path.join(
            FIXTURES, "2026-imas-ai-productivity-paradox.md"), entries)
        # A medium-relevance but otherwise eligible entry:
        with open(os.path.join(
                FIXTURES, "2023-korinek-genai-economic-research.md"),
                encoding="utf-8") as handle:
            text = handle.read()
        text = text.replace("slug: 2023-korinek-genai-economic-research",
                            "slug: 2026-medium-entry")
        text = text.replace("  social_science: high", "  social_science: medium")
        with open(os.path.join(entries, "2026-medium-entry.md"), "w",
                  encoding="utf-8") as handle:
            handle.write(text)

    def tearDown(self):
        self._tmp.cleanup()

    def write_report(self, text):
        with open(os.path.join(self.workspace, REPORT), "w",
                  encoding="utf-8") as handle:
            handle.write(text)

    def validate(self):
        return cri.validate_report(self.workspace, "social_science", RUN_DATE)

    def rules(self, violations):
        return sorted(violation.rule_id for violation in violations)

    def test_valid_high_relevance_item_passes(self):
        self.write_report(report_with_items(
            ["2023-korinek-genai-economic-research"]))
        self.assertEqual(self.validate(), [])

    def test_medium_relevance_item_flagged(self):
        self.write_report(report_with_items(["2026-medium-entry"]))
        violations = self.validate()
        self.assertEqual(self.rules(violations), ["REPORT_ITEM_NOT_ELIGIBLE"])
        self.assertIn("relevance", violations[0].message)

    def test_provisional_item_flagged_twice(self):
        self.write_report(report_with_items(
            ["2026-imas-ai-productivity-paradox"]))
        violations = self.validate()
        self.assertEqual(self.rules(violations),
                         ["REPORT_ITEM_NOT_ELIGIBLE"] * 2)

    def test_item_without_matching_entry_aborts(self):
        self.write_report(report_with_items(["2026-no-such-entry"]))
        violations = self.validate()
        self.assertEqual(self.rules(violations), ["REPORT_ENTRY_MISSING"])
        self.assertEqual(violations[0].klass, "abort")

    def test_item_without_entry_link_aborts(self):
        body = report_with_items([]).replace(
            "## Also archived today",
            "### 1. Linkless item (academic, Author, 2026)\n\n"
            "**Why it matters:** text.\n\n## Also archived today")
        self.write_report(body)
        self.assertEqual(self.rules(self.validate()),
                         ["REPORT_ITEM_NO_ENTRY_LINK"])

    def test_four_items_flagged(self):
        self.write_report(report_with_items(
            ["2023-korinek-genai-economic-research"] * 4))
        rules = self.rules(self.validate())
        self.assertIn("REPORT_TOO_MANY_ITEMS", rules)

    def test_quiet_day_with_evidence_passes(self):
        self.write_report(QUIET_BODY)
        self.assertEqual(self.validate(), [])

    def test_quiet_day_without_statement_flagged(self):
        self.write_report(QUIET_BODY.replace(
            "No material developments cleared the reporting bar today.",
            "Nothing found."))
        self.assertEqual(self.rules(self.validate()),
                         ["REPORT_QUIET_DAY_STATEMENT_MISSING"])

    def test_quiet_day_without_evidence_flagged(self):
        self.write_report(QUIET_BODY.replace(
            "- queries executed: 5\n", ""))
        self.assertEqual(self.rules(self.validate()),
                         ["REPORT_SCAN_EVIDENCE_MISSING"])

    def test_absent_report_is_not_a_content_violation(self):
        self.assertEqual(self.validate(), [])


if __name__ == "__main__":
    unittest.main()
