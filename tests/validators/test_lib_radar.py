"""Tests for scripts/validators/lib_radar.py (plan U2).

Covers: frontmatter parsing against real v1 entries, Europe/London date
discipline across DST boundaries (R44), violation format stability, the
no-echo guarantee (R47), and fail-closed internal errors (R42).
"""

import datetime
import io
import os
import re
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts", "validators"))

import lib_radar  # noqa: E402

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures", "entries")
MARKER = "71f3c9X"  # unique suffix shared by every planted marker string


def read_fixture(name):
    with open(os.path.join(FIXTURES, name), encoding="utf-8") as handle:
        return handle.read()


class TestFrontmatterParsing(unittest.TestCase):
    def test_real_accepted_entry_parses_cleanly(self):
        parsed = lib_radar.parse_frontmatter(
            read_fixture("2023-korinek-genai-economic-research.md"))
        self.assertEqual(parsed.errors, [])
        fields = parsed.fields
        self.assertEqual(fields["slug"], "2023-korinek-genai-economic-research")
        self.assertEqual(fields["status"], "accepted")
        self.assertEqual(fields["domains"], ["social_science"])
        self.assertEqual(fields["canonical_ids"], ["doi:10.1257/jel.20231736"])
        self.assertEqual(fields["relevance"],
                         {"social_science": "high", "ai_engineering": "medium"})
        self.assertIn("Canonical reference", fields["rationale"])
        self.assertTrue(fields["title"].startswith("Generative AI"))

    def test_real_provisional_entry_parses_cleanly(self):
        parsed = lib_radar.parse_frontmatter(
            read_fixture("2026-imas-ai-productivity-paradox.md"))
        self.assertEqual(parsed.errors, [])
        self.assertEqual(parsed.fields["status"], "provisional")
        self.assertEqual(parsed.fields["canonical_ids"], [])
        self.assertEqual(parsed.fields["verification"], "partial")

    def test_body_start_points_past_delimiter(self):
        text = "---\nslug: x\n---\nBODY\n"
        parsed = lib_radar.parse_frontmatter(text)
        self.assertEqual(parsed.errors, [])
        self.assertEqual(text.split("\n")[parsed.body_start - 1], "BODY")

    def test_missing_delimiter_is_an_error_not_a_guess(self):
        parsed = lib_radar.parse_frontmatter("# Just a heading\n")
        self.assertEqual(parsed.fields, {})
        self.assertEqual(parsed.errors, [(1, "no-frontmatter-delimiter")])

    def test_unparseable_line_recorded_with_line_number(self):
        parsed = lib_radar.parse_frontmatter(read_fixture("broken_frontmatter.md"))
        self.assertIn((3, "unparseable-line"), parsed.errors)
        self.assertEqual(parsed.fields.get("status"), "accepted")

    def test_unterminated_frontmatter_fails_closed(self):
        parsed = lib_radar.parse_frontmatter("---\nslug: x\n")
        self.assertTrue(any(reason == "unterminated-frontmatter"
                            for _, reason in parsed.errors))


class TestEntryValidation(unittest.TestCase):
    def test_valid_entries_produce_no_violations(self):
        for name in ("2023-korinek-genai-economic-research.md",
                     "2026-imas-ai-productivity-paradox.md"):
            violations = lib_radar.validate_entry_frontmatter(name, read_fixture(name))
            self.assertEqual(violations, [], name)

    def test_marker_entry_flags_status_and_relevance(self):
        violations = lib_radar.validate_entry_frontmatter(
            "marker_entry.md", read_fixture("marker_entry.md"))
        rules = sorted(violation.rule_id for violation in violations)
        self.assertIn("FIELD_INVALID", rules)
        flagged_fields = [violation.message for violation in violations]
        self.assertTrue(any("status" in message for message in flagged_fields))
        self.assertTrue(any("relevance" in message for message in flagged_fields))

    def test_missing_required_field_is_flagged(self):
        text = "---\nslug: x\ntitle: \"t\"\n---\n"
        violations = lib_radar.validate_entry_frontmatter("x.md", text)
        missing = [violation.message for violation in violations
                   if violation.rule_id == "FIELD_MISSING"]
        self.assertTrue(any("status" in message for message in missing))
        self.assertTrue(any("rationale" in message for message in missing))


class TestNoEcho(unittest.TestCase):
    """R47: no substring of flagged content may reach any output surface."""

    def test_marker_fixture_output_contains_no_marker(self):
        violations = lib_radar.validate_entry_frontmatter(
            "marker_entry.md", read_fixture("marker_entry.md"))
        self.assertTrue(violations)
        stream = io.StringIO()
        lib_radar.report(violations, stream=stream)
        output = stream.getvalue()
        self.assertNotIn(MARKER, output)
        self.assertNotIn("XMARKER", output)

    def test_sanitizer_redacts_newlines_length_and_charset(self):
        self.assertEqual(lib_radar._sanitize("a\nb"), lib_radar.REDACTED)
        self.assertEqual(lib_radar._sanitize("x" * 81), lib_radar.REDACTED)
        self.assertEqual(lib_radar._sanitize("bad`backtick"), lib_radar.REDACTED)
        self.assertEqual(lib_radar._sanitize("status"), "status")

    def test_emit_has_no_free_text_channel(self):
        violation = lib_radar.emit("FIELD_INVALID", "entry.md", None,
                                   field="XMARKER_SLOT_" + MARKER + "\nline2")
        self.assertNotIn(MARKER, violation.format())

    def test_internal_error_prints_class_name_only(self):
        stream = io.StringIO()

        def boom():
            raise ValueError("secret content XMARKER_" + MARKER)

        code = lib_radar.run_main(boom, stream=stream)
        self.assertEqual(code, lib_radar.EXIT_INTERNAL)
        output = stream.getvalue()
        self.assertIn("INTERNAL VALIDATOR_ERROR - ValueError", output)
        self.assertNotIn(MARKER, output)


class TestViolationFormat(unittest.TestCase):
    LINE_RE = re.compile(r"^(ABORT|REPAIRABLE) [A-Z0-9_]{3,40} \S+ - .+$")

    def test_format_is_stable_and_parseable(self):
        with_line = lib_radar.emit("FIELD_MISSING", "library/entries/x.md", None,
                                   field="status")
        malformed = lib_radar.emit("FRONTMATTER_MALFORMED", "library/entries/x.md",
                                   3, reason="unparseable-line")
        for violation in (with_line, malformed):
            self.assertTrue(self.LINE_RE.match(violation.format()), violation.format())
        self.assertIn("library/entries/x.md:3", malformed.format())

    def test_report_exit_codes(self):
        stream = io.StringIO()
        self.assertEqual(lib_radar.report([], stream=stream), lib_radar.EXIT_PASS)
        violation = lib_radar.emit("FIELD_MISSING", "x.md", None, field="slug")
        self.assertEqual(lib_radar.report([violation], stream=stream),
                         lib_radar.EXIT_VIOLATIONS)

    def test_unregistered_rule_fails_closed(self):
        with self.assertRaises(KeyError):
            lib_radar.emit("NOT_A_RULE", "x.md")

    def test_duplicate_conflicting_registration_rejected(self):
        with self.assertRaises(ValueError):
            lib_radar.register_rule("FIELD_MISSING", lib_radar.ABORT, "different")


class TestLondonDates(unittest.TestCase):
    """R44: 'today' derives from Europe/London, never runner UTC."""

    @staticmethod
    def utc(*args):
        return datetime.datetime(*args, tzinfo=datetime.timezone.utc)

    def test_bst_evening_rolls_to_next_london_date(self):
        # 23:30 UTC on 22 July 2026 is 00:30 BST on 23 July in London.
        self.assertEqual(lib_radar.london_today(self.utc(2026, 7, 22, 23, 30)),
                         datetime.date(2026, 7, 23))

    def test_gmt_winter_evening_keeps_same_date(self):
        # 23:30 UTC on 22 January 2026 is 23:30 GMT in London — same date.
        self.assertEqual(lib_radar.london_today(self.utc(2026, 1, 22, 23, 30)),
                         datetime.date(2026, 1, 22))

    def test_spring_forward_transition_day(self):
        # DST starts 29 March 2026, 01:00 UTC. Both sides map to 29 March.
        self.assertEqual(lib_radar.london_today(self.utc(2026, 3, 29, 0, 30)),
                         datetime.date(2026, 3, 29))
        self.assertEqual(lib_radar.london_today(self.utc(2026, 3, 29, 1, 30)),
                         datetime.date(2026, 3, 29))
        # And 10:07 London on the transition day corresponds to 09:07 UTC.
        london = lib_radar.london_now(self.utc(2026, 3, 29, 9, 7))
        self.assertEqual((london.hour, london.minute), (10, 7))

    def test_fall_back_transition_day(self):
        # DST ends 25 October 2026, 01:00 UTC. 10:07 London is 10:07 UTC again.
        london = lib_radar.london_now(self.utc(2026, 10, 25, 10, 7))
        self.assertEqual((london.hour, london.minute), (10, 7))
        self.assertEqual(london.date(), datetime.date(2026, 10, 25))

    def test_naive_datetime_rejected(self):
        with self.assertRaises(ValueError):
            lib_radar.london_now(datetime.datetime(2026, 7, 22, 12, 0))

    def test_partial_and_unknown_dates_parse_to_none(self):
        self.assertIsNone(lib_radar.parse_iso_date("2023-12"))
        self.assertIsNone(lib_radar.parse_iso_date("unknown"))
        self.assertIsNone(lib_radar.parse_iso_date("2026-02-30"))
        self.assertEqual(lib_radar.parse_iso_date("2026-07-23"),
                         datetime.date(2026, 7, 23))


if __name__ == "__main__":
    unittest.main()
