"""Tests for check_queue_records.py (plan U4; R12-R14, R19)."""

import io
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import check_queue_records as cqr  # noqa: E402
import lib_radar  # noqa: E402

from . import repo_fixture as fix  # noqa: E402

DEFERRED_PATH = "reviews/deferred_candidates/social_science.md"
PROPOSALS_PATH = "reviews/source_proposals/social_science.md"
MARKER = "71f3c9X"


class TestQueueStructure(unittest.TestCase):
    def rules(self, violations):
        return sorted(violation.rule_id for violation in violations)

    def test_valid_deferred_and_proposal_files_pass(self):
        self.assertEqual(cqr.validate_file(DEFERRED_PATH, fix.DEFERRED_BASE), [])
        self.assertEqual(cqr.validate_file(PROPOSALS_PATH, fix.PROPOSALS_BASE), [])

    def test_invalid_status_flagged(self):
        text = fix.DEFERRED_BASE.replace("- status: pending",
                                         "- status: maybe_later")
        violations = cqr.validate_file(DEFERRED_PATH, text)
        self.assertEqual(self.rules(violations), ["QUEUE_FIELD_INVALID"])
        self.assertIn("status", violations[0].message)

    def test_invalid_reason_class_flagged(self):
        text = fix.DEFERRED_BASE.replace(
            "- reason_class: verification_insufficient",
            "- reason_class: vibes")
        violations = cqr.validate_file(DEFERRED_PATH, text)
        self.assertEqual(self.rules(violations), ["QUEUE_FIELD_INVALID"])
        self.assertIn("reason_class", violations[0].message)

    def test_missing_required_field_flagged(self):
        text = fix.DEFERRED_BASE.replace(
            "- action_needed: locate public artifact\n", "")
        violations = cqr.validate_file(DEFERRED_PATH, text)
        self.assertEqual(self.rules(violations), ["QUEUE_FIELD_MISSING"])
        self.assertIn("action_needed", violations[0].message)

    def test_unknown_field_flagged(self):
        text = fix.DEFERRED_BASE + "- captured_text: something\n"
        violations = cqr.validate_file(DEFERRED_PATH, text)
        self.assertEqual(self.rules(violations), ["QUEUE_FIELD_UNKNOWN"])

    def test_bad_date_flagged(self):
        text = fix.DEFERRED_BASE.replace("first_encountered: 2026-07-20",
                                         "first_encountered: last week")
        self.assertEqual(self.rules(cqr.validate_file(DEFERRED_PATH, text)),
                         ["QUEUE_FIELD_INVALID"])

    def test_stray_prose_line_flagged(self):
        text = fix.DEFERRED_BASE + "\nsome captured paragraph\n"
        self.assertEqual(self.rules(cqr.validate_file(DEFERRED_PATH, text)),
                         ["QUEUE_MALFORMED"])


class TestMetadataOnly(unittest.TestCase):
    def rules(self, violations):
        return sorted(violation.rule_id for violation in violations)

    def test_fenced_block_prohibited(self):
        text = fix.DEFERRED_BASE + "\n```\nquoted candidate text\n```\n"
        rules = self.rules(cqr.validate_file(DEFERRED_PATH, text))
        self.assertIn("QUEUE_CONTENT_BLOCK", rules)

    def test_overlong_free_text_flagged(self):
        text = fix.DEFERRED_BASE.replace(
            "- reason: underlying public artifact not yet located",
            "- reason: " + "a" * 300)
        self.assertEqual(self.rules(cqr.validate_file(DEFERRED_PATH, text)),
                         ["QUEUE_TEXT_TOO_LONG"])

    def test_url_hygiene(self):
        for bad, reason in (
                ("https://example.org/x?access_token=abc123", "token"),
                ("https://example.org/x?utm_source=news", "token"),
                ("https://user:pass@example.org/x", "credentials"),
                ("ftp://example.org/x", "not-http")):
            text = fix.DEFERRED_BASE.replace(
                "### https://example.org/walled-post", "### " + bad)
            violations = cqr.validate_file(DEFERRED_PATH, text)
            self.assertIn("QUEUE_URL_UNSAFE",
                          [violation.rule_id for violation in violations], bad)

    def test_no_echo_of_poisoned_fields(self):
        text = fix.DEFERRED_BASE.replace(
            "- reason: underlying public artifact not yet located",
            "- reason: " + "leaked sensitive detail XMARKER_%s " % MARKER * 20)
        text = text.replace("### https://example.org/walled-post",
                            "### https://example.org/x?token=XMARKER_" + MARKER)
        violations = cqr.validate_file(DEFERRED_PATH, text)
        self.assertTrue(violations)
        stream = io.StringIO()
        lib_radar.report(violations, stream=stream)
        self.assertNotIn(MARKER, stream.getvalue())
        self.assertNotIn("XMARKER", stream.getvalue())


class TestDuplicates(unittest.TestCase):
    def test_duplicate_within_file(self):
        text = fix.DEFERRED_BASE + fix.DEFERRED_BASE[
            fix.DEFERRED_BASE.index("### "):]
        violations = cqr.validate_file(DEFERRED_PATH, text)
        self.assertIn("DUPLICATE_QUEUE_RECORD",
                      [violation.rule_id for violation in violations])

    def test_duplicate_across_sibling_domain_file(self):
        sibling = ("# Deferred candidates - ai_engineering\n\n"
                   + fix.DEFERRED_BASE[fix.DEFERRED_BASE.index("### "):])
        violations = cqr.validate_file(DEFERRED_PATH, fix.DEFERRED_BASE,
                                       sibling_texts=[sibling])
        self.assertEqual([violation.rule_id for violation in violations],
                         ["DUPLICATE_QUEUE_RECORD"])
        self.assertIn("sibling", violations[0].message)


if __name__ == "__main__":
    unittest.main()
