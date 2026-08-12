"""Tests for check_changed_paths.py (plan U3; R22/R23/R41/R50/R44)."""

import datetime
import io
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import check_changed_paths as ccp  # noqa: E402
import lib_radar  # noqa: E402

from . import repo_fixture as fix  # noqa: E402

RUN_DATE = datetime.date(2026, 7, 23)
MARKER = "71f3c9X"


class ChangedPathsBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory(prefix="radar-u3-")
        cls.origin, cls.template = fix.build_template(cls._tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def workspace(self):
        return fix.fresh_workspace(self._tmp.name, self.template)

    def validate(self, workspace):
        return ccp.validate("origin/main", workspace, None, RUN_DATE)

    def rules(self, violations):
        return sorted(violation.rule_id for violation in violations)


class TestPermittedChanges(ChangedPathsBase):
    def test_no_changes_passes(self):
        self.assertEqual(self.validate(self.workspace()), [])

    def test_new_entry_with_index_and_rejection_append_passes(self):
        workspace = self.workspace()
        fix.write(workspace, "library/entries/2026-new-development.md",
                  fix.read(workspace, fix.ACCEPTED_ENTRY)
                  .replace("2023-korinek-genai-economic-research",
                           "2026-new-development"))
        fix.write(workspace, "library/INDEX.md",
                  fix.read(workspace, "library/INDEX.md") + "| new | row |\n")
        fix.write(workspace, fix.REJECTIONS,
                  fix.read(workspace, fix.REJECTIONS)
                  + "- 2026-07-23 - example.org/three - out of scope\n")
        self.assertEqual(self.validate(workspace), [])

    def test_same_day_report_regeneration_and_creation_pass(self):
        workspace = self.workspace()
        fix.write(workspace, fix.TODAY_REPORT,
                  "# Daily report - 2026-07-23\n\nRegenerated union.\n")
        fix.write(workspace, "reports/ai_engineering/daily/2026-07-23.md",
                  "# Daily report - 2026-07-23\n\nFirst run.\n")
        self.assertEqual(self.validate(workspace), [])

    def test_legitimate_entry_update_passes(self):
        workspace = self.workspace()
        text = fix.read(workspace, fix.PROVISIONAL_ENTRY)
        text = text.replace("status: provisional", "status: accepted")
        text = text.replace("verification: partial", "verification: verified")
        text = text.replace("canonical_ids: []",
                            'canonical_ids: ["doi:10.9999/example"]')
        text = text.replace(
            "*(none yet)*",
            "- **2026-07-23** - Load-bearing micro-study range corroborated; "
            "upgraded to accepted.")
        text += ("[2026-new-development](2026-new-development.md) - "
                 "related follow-up.\n")
        fix.write(workspace, fix.PROVISIONAL_ENTRY, text)
        self.assertEqual(self.validate(workspace), [])

    def test_queue_pending_append_and_bump_pass(self):
        workspace = self.workspace()
        text = fix.read(workspace, fix.DEFERRED_FILE)
        text = text.replace("last_encountered: 2026-07-21",
                            "last_encountered: 2026-07-23")
        text = text.replace(
            "- reason: underlying public artifact not yet located",
            "- reason: underlying public artifact not yet located; "
            "re-encountered via curated scan")
        fix.write(workspace, fix.DEFERRED_FILE, text + fix.NEW_DEFERRED_RECORD)
        self.assertEqual(self.validate(workspace), [])


class TestHistoryProtection(ChangedPathsBase):
    def test_deleted_historical_entry_aborts(self):
        workspace = self.workspace()
        fix.remove(workspace, fix.ACCEPTED_ENTRY)
        violations = self.validate(workspace)
        self.assertEqual(self.rules(violations), ["HISTORY_DELETION"])
        self.assertEqual(violations[0].klass, lib_radar.ABORT)

    def test_deleted_report_aborts(self):
        workspace = self.workspace()
        fix.remove(workspace, fix.PAST_REPORT)
        self.assertIn("HISTORY_DELETION", self.rules(self.validate(workspace)))

    def test_rewritten_historical_report_aborts(self):
        workspace = self.workspace()
        fix.write(workspace, fix.PAST_REPORT,
                  "# Daily report - 2026-07-22\n\nRewritten history.\n")
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["PAST_REPORT_MODIFIED"])

    def test_future_dated_report_aborts(self):
        workspace = self.workspace()
        fix.write(workspace, "reports/social_science/daily/2026-07-24.md", "x\n")
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["REPORT_NOT_RUN_DATE"])

    def test_undated_report_filename_aborts(self):
        workspace = self.workspace()
        fix.write(workspace, "reports/social_science/daily/notes.md", "x\n")
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["REPORT_NAME_INVALID"])

    def test_rejection_log_rewrite_aborts_append_passes(self):
        workspace = self.workspace()
        fix.write(workspace, fix.REJECTIONS,
                  fix.REJECTIONS_BASE.replace("below discovery bar",
                                              "edited old reason"))
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["REJECTIONS_NOT_APPEND_ONLY"])


class TestEntryPreservation(ChangedPathsBase):
    def test_body_rewrite_aborts(self):
        workspace = self.workspace()
        fix.write(workspace, fix.ACCEPTED_ENTRY,
                  fix.read(workspace, fix.ACCEPTED_ENTRY)
                  .replace("Korinek systematically maps",
                           "Korinek allegedly maps"))
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["ENTRY_BODY_REWRITTEN"])

    def test_deleting_existing_update_bullet_aborts(self):
        workspace = self.workspace()
        text = fix.read(workspace, fix.ACCEPTED_ENTRY)
        lines = [line for line in text.split("\n")
                 if not line.startswith("- **2026-07-22**")]
        fix.write(workspace, fix.ACCEPTED_ENTRY, "\n".join(lines))
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["ENTRY_BODY_REWRITTEN"])

    def test_non_permitted_frontmatter_change_aborts(self):
        workspace = self.workspace()
        fix.write(workspace, fix.ACCEPTED_ENTRY,
                  fix.read(workspace, fix.ACCEPTED_ENTRY)
                  .replace('published: 2023-12', 'published: 2024-01'))
        violations = self.validate(workspace)
        self.assertEqual(self.rules(violations),
                         ["ENTRY_FRONTMATTER_FIELD_CHANGED"])
        self.assertIn("published", violations[0].message)

    def test_unparseable_modified_entry_fails_closed(self):
        workspace = self.workspace()
        fix.write(workspace, fix.ACCEPTED_ENTRY, "no frontmatter at all\n")
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["ENTRY_UNVERIFIABLE"])

    def test_removing_either_updates_placeholder_passes(self):
        # engine/templates/entry.md writes "None yet."; "*(none yet)*" is the
        # legacy spelling. Replacing either with a first dated Updates line
        # must not read as a body rewrite (2026-08-01/02/05 abort class).
        base = fix.read(self.workspace(), fix.PROVISIONAL_ENTRY)
        for placeholder in ("*(none yet)*", "None yet."):
            with self.subTest(placeholder=placeholder):
                old = base.replace("*(none yet)*", placeholder)
                new = old.replace(
                    placeholder,
                    "- **2026-08-12** - First dated update line.")
                self.assertEqual(
                    ccp.check_entry_preservation("entry.md", old, new), [])


class TestProtectedPaths(ChangedPathsBase):
    def test_profiles_engine_and_skill_modifications_abort(self):
        workspace = self.workspace()
        fix.write(workspace, "profiles/social_science/profile.md", "# Edited\n")
        fix.write(workspace, "engine/ENGINE.md", "# Edited\n")
        fix.write(workspace, ".claude/skills/social-science-radar/SKILL.md",
                  "# Edited\n")
        violations = self.validate(workspace)
        self.assertEqual(self.rules(violations), ["PATH_OUTSIDE_ALLOWLIST"] * 3)
        self.assertTrue(all(violation.klass == lib_radar.ABORT
                            for violation in violations))

    def test_tampered_validator_and_delivery_script_abort(self):
        workspace = self.workspace()
        fix.write(workspace, "scripts/validators/check_changed_paths.py",
                  "# tampered - return no violations\n")
        fix.write(workspace, "scripts/run_delivery.sh", "# tampered\n")
        violations = self.validate(workspace)
        self.assertEqual(self.rules(violations), ["PATH_OUTSIDE_ALLOWLIST"] * 2)
        paths = sorted(violation.path for violation in violations)
        self.assertEqual(paths, ["scripts/run_delivery.sh",
                                 "scripts/validators/check_changed_paths.py"])

    def test_new_file_outside_allowlist_aborts(self):
        workspace = self.workspace()
        fix.write(workspace, "inbox/sneaky.md", "x\n")
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["PATH_OUTSIDE_ALLOWLIST"])


class TestQueueProtection(ChangedPathsBase):
    """User decision at the U3 checkpoint: reviews/ is audit trail."""

    def test_deleted_review_file_aborts(self):
        workspace = self.workspace()
        fix.remove(workspace, fix.DEFERRED_FILE)
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["HISTORY_DELETION"])

    def test_removed_existing_record_aborts(self):
        workspace = self.workspace()
        fix.write(workspace, fix.DEFERRED_FILE,
                  "# Deferred candidates - social_science\n"
                  + fix.NEW_DEFERRED_RECORD)
        self.assertIn("QUEUE_RECORD_REMOVED",
                      self.rules(self.validate(workspace)))

    def test_unattended_resolution_aborts_manual_passes(self):
        workspace = self.workspace()
        text = fix.read(workspace, fix.DEFERRED_FILE)
        text = text.replace("- status: pending",
                            "- status: archived\n"
                            "- resolution_date: 2026-07-23\n"
                            "- resolution: archived as accepted entry\n"
                            "- linked_ref: library/entries/2026-x.md")
        fix.write(workspace, fix.DEFERRED_FILE, text)
        unattended = self.validate(workspace)
        self.assertTrue(unattended)
        self.assertEqual(set(self.rules(unattended)),
                         {"QUEUE_RESOLUTION_BY_AUTOMATION"})
        self.assertTrue(all(v.klass == lib_radar.ABORT for v in unattended))
        manual = ccp.validate("origin/main", workspace, None, RUN_DATE,
                              mode=ccp.MODE_MANUAL)
        self.assertEqual(manual, [])

    def test_rewritten_history_field_aborts_in_both_modes(self):
        workspace = self.workspace()
        text = fix.read(workspace, fix.DEFERRED_FILE)
        fix.write(workspace, fix.DEFERRED_FILE,
                  text.replace("first_encountered: 2026-07-20",
                               "first_encountered: 2026-07-23"))
        for mode in (ccp.MODE_UNATTENDED, ccp.MODE_MANUAL):
            violations = ccp.validate("origin/main", workspace, None,
                                      RUN_DATE, mode=mode)
            self.assertEqual(self.rules(violations),
                             ["QUEUE_HISTORY_REWRITTEN"], mode)
            self.assertEqual(violations[0].klass, lib_radar.ABORT)

    def test_rephrased_justification_is_repairable(self):
        """Regression for drill-A run 30020895058: a paraphrased pending-record
        reason is a content defect (repairable), not history falsification —
        the grow-only rule still blocks it from ever being committed."""
        workspace = self.workspace()
        text = fix.read(workspace, fix.DEFERRED_FILE)
        fix.write(workspace, fix.DEFERRED_FILE,
                  text.replace(
                      "- reason: underlying public artifact not yet located",
                      "- reason: could not locate the public artifact"))
        violations = ccp.validate("origin/main", workspace, None, RUN_DATE)
        self.assertEqual(self.rules(violations), ["QUEUE_RECORD_REWRITTEN"])
        self.assertEqual(violations[0].klass, "repairable")

    def test_new_record_born_resolved_aborts_unattended(self):
        workspace = self.workspace()
        record = fix.NEW_DEFERRED_RECORD.replace("- status: pending",
                                                 "- status: dismissed")
        fix.write(workspace, fix.DEFERRED_FILE,
                  fix.read(workspace, fix.DEFERRED_FILE) + record)
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["QUEUE_RESOLUTION_BY_AUTOMATION"])

    def test_unparseable_queue_change_fails_closed(self):
        workspace = self.workspace()
        fix.write(workspace, fix.DEFERRED_FILE,
                  fix.read(workspace, fix.DEFERRED_FILE)
                  + "\nfree prose that is not a record\n")
        self.assertEqual(self.rules(self.validate(workspace)),
                         ["QUEUE_UNVERIFIABLE"])


class TestNoEchoPaths(ChangedPathsBase):
    def test_content_shaped_filename_is_redacted(self):
        workspace = self.workspace()
        bad_name = "profiles/XMARKER secret leak %s!.md" % MARKER
        fix.write(workspace, bad_name, "content\n")
        violations = self.validate(workspace)
        self.assertEqual(self.rules(violations), ["PATH_OUTSIDE_ALLOWLIST"])
        stream = io.StringIO()
        lib_radar.report(violations, stream=stream)
        output = stream.getvalue()
        self.assertNotIn(MARKER, output)
        self.assertNotIn("XMARKER", output)
        self.assertIn("profiles/[redacted-", output)


class TestCliContract(ChangedPathsBase):
    SCRIPT = os.path.join(os.path.dirname(__file__), "..", "..",
                          "scripts", "validators", "check_changed_paths.py")

    def run_cli(self, workspace, *extra):
        return subprocess.run(
            [sys.executable, os.path.abspath(self.SCRIPT),
             "--base", "origin/main", "--work-tree", workspace,
             "--run-date", "2026-07-23"] + list(extra),
            capture_output=True, text=True)

    def test_exit_zero_on_clean_workspace(self):
        self.assertEqual(self.run_cli(self.workspace()).returncode,
                         lib_radar.EXIT_PASS)

    def test_exit_one_on_violation(self):
        workspace = self.workspace()
        fix.write(workspace, "engine/ENGINE.md", "# Edited\n")
        result = self.run_cli(workspace)
        self.assertEqual(result.returncode, lib_radar.EXIT_VIOLATIONS)
        self.assertIn("ABORT PATH_OUTSIDE_ALLOWLIST engine/ENGINE.md", result.stdout)

    def test_exit_two_on_bad_base_ref(self):
        result = subprocess.run(
            [sys.executable, os.path.abspath(self.SCRIPT),
             "--base", "no-such-ref", "--work-tree", self.workspace(),
             "--run-date", "2026-07-23"],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, lib_radar.EXIT_INTERNAL)
        self.assertIn("INTERNAL VALIDATOR_ERROR", result.stdout)

    def test_exit_two_on_bad_run_date(self):
        result = self.run_cli(self.workspace())
        self.assertEqual(result.returncode, lib_radar.EXIT_PASS)
        bad = subprocess.run(
            [sys.executable, os.path.abspath(self.SCRIPT),
             "--base", "origin/main", "--work-tree", self.workspace(),
             "--run-date", "not-a-date"],
            capture_output=True, text=True)
        self.assertEqual(bad.returncode, lib_radar.EXIT_INTERNAL)


if __name__ == "__main__":
    unittest.main()
