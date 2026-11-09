"""Tests for normalize_queue_appends.py (plan 2026-11-09-001 U3).

The fixtures reproduce the real failures: a field at the 240-character cap
and one at 233 that a re-encounter appended to (2026-11-05, run 42029203188),
and a 207-character field the run rephrased (2026-10-30, run 41044727227).
After normalisation, the real queue validators must pass.
"""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import check_changed_paths as ccp  # noqa: E402
import check_queue_records as cqr  # noqa: E402
import lib_queues  # noqa: E402
import normalize_queue_appends as nqa  # noqa: E402

PATH = "reviews/deferred_candidates/social_science.md"


def text_of(length, stem):
    """A deterministic action_needed value of exactly `length` characters."""
    body = (stem + " " + "x" * length)[:length]
    assert len(body) == length
    return body


AT_CAP = text_of(240, "retry the column fetch, or have a human confirm")
NEAR_CAP = text_of(233, "confirm the true publication date directly")
SHORT = text_of(207, "locate the working paper PDF and confirm the date")


def record(url, action_needed, last="2026-11-04", reason="column 403'd"):
    return ("### %s\n- title: Example\n- domain: social_science\n"
            "- first_encountered: 2026-09-25\n- last_encountered: %s\n"
            "- source_type: academic\n- reason_class: access_or_license_unclear\n"
            "- reason: %s\n- surfaced_by: watchlist:voxeu-cepr\n"
            "- action_needed: %s\n- status: pending\n"
            % (url, last, reason, action_needed))


HEADER = "# Deferred candidates - social science\n\n"
BASE = HEADER + "\n".join([
    record("https://example.org/at-cap", AT_CAP),
    record("https://example.org/near-cap", NEAR_CAP),
    record("https://example.org/short", SHORT),
])


def validate(old, new):
    """The real unattended validators that judged the failed runs."""
    return (ccp.check_queue_preservation(PATH, old, new, ccp.MODE_UNATTENDED)
            + cqr.validate_file(PATH, new))


def rules(violations):
    return sorted(v.rule_id for v in violations)


class TestNormalizeQueueAppends(unittest.TestCase):
    def test_base_fixture_is_valid(self):
        self.assertEqual(rules(validate(BASE, BASE)), [])

    def test_over_cap_appends_restored_and_bump_kept_2026_11_05(self):
        new = (BASE
               .replace(AT_CAP, AT_CAP + "; 11-05: same (403).")
               .replace(NEAR_CAP, NEAR_CAP + "; 11-05: still undated.")
               .replace("- last_encountered: 2026-11-04",
                        "- last_encountered: 2026-11-05"))
        # Before normalisation: the two violations attempt 1 produced.
        self.assertEqual(rules(validate(BASE, new)),
                         ["QUEUE_TEXT_TOO_LONG", "QUEUE_TEXT_TOO_LONG"])
        fixed, restored = nqa.normalize_text(BASE, new)
        self.assertEqual(sorted((f, r) for _, f, r in restored),
                         [("action_needed", "over_cap"),
                          ("action_needed", "over_cap")])
        self.assertEqual(rules(validate(BASE, fixed)), [])
        records, _ = lib_queues.parse_queue_file(fixed)
        self.assertEqual({r.fields["last_encountered"] for r in records},
                         {"2026-11-05"})
        self.assertEqual(records[0].fields["action_needed"], AT_CAP)

    def test_trimmed_repair_output_restored_2026_11_05(self):
        """What the repair pass produced: shortened text (a rewrite)."""
        new = BASE.replace(AT_CAP, AT_CAP[:180])
        self.assertEqual(rules(validate(BASE, new)), ["QUEUE_RECORD_REWRITTEN"])
        fixed, restored = nqa.normalize_text(BASE, new)
        self.assertEqual([r for _, _, r in restored], ["rephrased"])
        self.assertEqual(rules(validate(BASE, fixed)), [])

    def test_rephrased_field_restored_2026_10_30(self):
        new = BASE.replace(SHORT, "find the paper and check when it came out")
        self.assertEqual(rules(validate(BASE, new)), ["QUEUE_RECORD_REWRITTEN"])
        fixed, restored = nqa.normalize_text(BASE, new)
        self.assertEqual(len(restored), 1)
        self.assertEqual(rules(validate(BASE, fixed)), [])

    def test_legal_append_within_cap_is_kept(self):
        new = BASE.replace(SHORT, SHORT + "; 11-05: re-seen")
        self.assertEqual(rules(validate(BASE, new)), [])
        fixed, restored = nqa.normalize_text(BASE, new)
        self.assertEqual(restored, [])
        self.assertEqual(fixed, new)

    def test_other_grow_only_field_restored(self):
        new = BASE.replace("- reason: column 403'd\n",
                           "- reason: page was blocked\n", 1)
        fixed, restored = nqa.normalize_text(BASE, new)
        self.assertEqual([(f, r) for _, f, r in restored],
                         [("reason", "rephrased")])
        self.assertEqual(rules(validate(BASE, fixed)), [])

    def test_new_records_are_never_touched(self):
        """A new record has no history: over-cap text there stays a
        repairable finding for the model (10-30, line 290)."""
        new = BASE + "\n" + record("https://example.org/new", "y" * 300)
        fixed, restored = nqa.normalize_text(BASE, new)
        self.assertEqual(restored, [])
        self.assertEqual(fixed, new)
        self.assertEqual(rules(validate(BASE, fixed)), ["QUEUE_TEXT_TOO_LONG"])

    def test_non_grow_only_and_lifecycle_changes_left_to_validators(self):
        new = BASE.replace("- status: pending", "- status: dismissed", 1)
        fixed, restored = nqa.normalize_text(BASE, new)
        self.assertEqual(restored, [])
        self.assertEqual(rules(validate(BASE, fixed)),
                         ["QUEUE_RESOLUTION_BY_AUTOMATION"])

    def test_unparseable_input_is_left_unchanged(self):
        new = BASE.replace(AT_CAP, AT_CAP + " more") + "stray prose line\n"
        fixed, restored = nqa.normalize_text(BASE, new)
        self.assertEqual(restored, [])
        self.assertEqual(fixed, new)

    def test_workspace_run_writes_derived_report_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            workspace = os.path.join(tmp, "ws")
            pristine = os.path.join(tmp, "base")
            for root, text in ((pristine, BASE),
                               (workspace, BASE.replace(AT_CAP, AT_CAP + "; more"))):
                os.makedirs(os.path.join(root, os.path.dirname(PATH)))
                with open(os.path.join(root, PATH), "w", encoding="utf-8") as handle:
                    handle.write(text)
            # A queue file absent from the base (new file) is skipped.
            other = os.path.join(workspace, "reviews", "source_proposals")
            os.makedirs(other)
            with open(os.path.join(other, "ai_engineering.md"), "w") as handle:
                handle.write("# Source proposals\n")
            report = nqa.normalize_workspace(workspace, pristine)
            self.assertEqual(len(report), 1)
            self.assertRegex(report[0],
                             r"^RESTORED reviews/deferred_candidates/"
                             r"social_science\.md:\d+ action_needed over_cap$")
            self.assertNotIn("retry", report[0])  # never the text (R43)
            with open(os.path.join(workspace, PATH), encoding="utf-8") as handle:
                self.assertEqual(handle.read(), BASE)


if __name__ == "__main__":
    unittest.main()
