"""Tests for scripts/run_delivery.py (plan U8; R7, R25-R27, R41, R42)."""

import datetime
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import run_delivery as rd  # noqa: E402

from . import repo_fixture as fix  # noqa: E402

RUN_DATE = "2026-07-23"
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCRIPT = os.path.join(REPO_ROOT, "scripts", "run_delivery.py")

VALID_EVIDENCE = {
    "run_date": RUN_DATE,
    "domains": {
        "social_science": {"curated_sources_fetched": 5, "queries_executed": 3},
        "ai_engineering": {"curated_sources_fetched": 4, "queries_executed": 2},
    },
}


class DeliveryBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory(prefix="radar-u8-")
        cls.origin, cls.template = fix.build_template(cls._tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def setup_run(self, tamper_workspace_scripts=False):
        """workspace clone + pristine copy (real repo's scripts) + evidence."""
        workspace = fix.fresh_workspace(self._tmp.name, self.template)
        pristine = workspace + "-pristine"
        os.makedirs(os.path.join(pristine, "scripts"))
        shutil.copytree(os.path.join(REPO_ROOT, "scripts", "validators"),
                        os.path.join(pristine, "scripts", "validators"))
        shutil.copy(os.path.join(REPO_ROOT, "scripts", "run_delivery.py"),
                    os.path.join(pristine, "scripts"))
        shutil.copy(os.path.join(REPO_ROOT, "scripts", "make_run_summary.py"),
                    os.path.join(pristine, "scripts"))
        evidence = os.path.join(workspace + "-evidence.json")
        with open(evidence, "w", encoding="utf-8") as handle:
            json.dump(VALID_EVIDENCE, handle)
        if tamper_workspace_scripts:
            fix.write(workspace, "scripts/validators/check_changed_paths.py",
                      "import sys; sys.exit(0)  # tampered: always pass\n")
            fix.write(workspace, "scripts/run_delivery.sh", "# tampered\n")
        return workspace, pristine, evidence

    def validate(self, workspace, pristine, evidence, final=False,
                 skip_evidence=False):
        out = workspace + ("-out-final" if final else "-out")
        argv = [sys.executable, SCRIPT, "validate",
                "--workspace", workspace, "--pristine", pristine,
                "--base", "origin/main", "--run-date", RUN_DATE,
                "--evidence", evidence,
                "--violations-out", workspace + "-violations.txt",
                "--github-output", out]
        if final:
            argv.append("--final")
        if skip_evidence:
            argv.append("--skip-evidence")
        result = subprocess.run(argv, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        pairs = dict(line.split("=", 1)
                     for line in result.stdout.splitlines() if "=" in line)
        return pairs

    def deliver(self, workspace, final=False):
        out = workspace + "-deliver-out"
        argv = [sys.executable, SCRIPT, "deliver",
                "--workspace", workspace,
                "--git-dir", os.path.join(workspace, ".git"),
                "--base", "origin/main", "--run-date", RUN_DATE,
                "--remote", self.origin,
                "--github-output", out]
        if final:
            argv.append("--final")
        result = subprocess.run(argv, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        return dict(line.split("=", 1)
                    for line in result.stdout.splitlines() if "=" in line)


class TestValidate(DeliveryBase):
    def test_clean_workspace_with_evidence_passes(self):
        workspace, pristine, evidence = self.setup_run()
        self.assertEqual(self.validate(workspace, pristine, evidence)["verdict"],
                         "pass")

    def test_missing_evidence_is_tooling_abort_even_with_empty_diff(self):
        workspace, pristine, _ = self.setup_run()
        pairs = self.validate(workspace, pristine, workspace + "-missing.json")
        self.assertEqual(pairs["verdict"], "abort")
        self.assertEqual(pairs["failure_class"], "tooling")

    def test_missing_evidence_alone_is_degenerate(self):
        """2026-07-28 review: the bail signature — no evidence artifact and no
        other violation — is the only retry-eligible validate outcome."""
        workspace, pristine, _ = self.setup_run()
        pairs = self.validate(workspace, pristine, workspace + "-missing.json")
        self.assertEqual(pairs["degenerate"], "true")

    def test_missing_evidence_with_other_violation_is_not_degenerate(self):
        workspace, pristine, _ = self.setup_run()
        fix.write(workspace, "engine/ENGINE.md", "# tampered\n")
        pairs = self.validate(workspace, pristine, workspace + "-missing.json")
        self.assertEqual(pairs["verdict"], "abort")
        self.assertEqual(pairs["degenerate"], "false")

    def test_passing_run_is_not_degenerate(self):
        workspace, pristine, evidence = self.setup_run()
        pairs = self.validate(workspace, pristine, evidence)
        self.assertEqual(pairs["verdict"], "pass")
        self.assertEqual(pairs["degenerate"], "false")

    def test_malformed_evidence_is_not_degenerate(self):
        """A malformed artifact means the model tried but wrote garbage —
        excluded from the retry signature (different token than MISSING)."""
        workspace, pristine, _ = self.setup_run()
        malformed = workspace + "-malformed.json"
        with open(malformed, "w", encoding="utf-8") as handle:
            handle.write("{not json")
        pairs = self.validate(workspace, pristine, malformed)
        self.assertEqual(pairs["verdict"], "abort")
        self.assertEqual(pairs["degenerate"], "false")

    def test_dry_run_skips_evidence(self):
        workspace, pristine, _ = self.setup_run()
        pairs = self.validate(workspace, pristine, "", skip_evidence=True)
        self.assertEqual(pairs["verdict"], "pass")

    def test_protected_path_edit_aborts_as_validation(self):
        workspace, pristine, evidence = self.setup_run()
        fix.write(workspace, "engine/ENGINE.md", "# tampered\n")
        pairs = self.validate(workspace, pristine, evidence)
        self.assertEqual(pairs["verdict"], "abort")
        self.assertEqual(pairs["failure_class"], "validation")

    def test_repairable_defect_and_final_escalation(self):
        workspace, pristine, evidence = self.setup_run()
        new_entry = fix.read(workspace, fix.ACCEPTED_ENTRY).replace(
            "2023-korinek-genai-economic-research", "2026-unindexed-entry")
        fix.write(workspace, "library/entries/2026-unindexed-entry.md", new_entry)
        self.assertEqual(
            self.validate(workspace, pristine, evidence)["verdict"],
            "repairable")
        self.assertEqual(
            self.validate(workspace, pristine, evidence, final=True)["verdict"],
            "abort")

    def test_tampered_workspace_scripts_are_inert_and_flagged(self):
        """R41: the tampered workspace validator would pass everything; the
        pristine copy actually runs and aborts on the tampered paths."""
        workspace, pristine, evidence = self.setup_run(
            tamper_workspace_scripts=True)
        pairs = self.validate(workspace, pristine, evidence)
        self.assertEqual(pairs["verdict"], "abort")
        with open(workspace + "-violations.txt", encoding="utf-8") as handle:
            violations = handle.read()
        self.assertIn("scripts/validators/check_changed_paths.py", violations)
        self.assertIn("scripts/run_delivery.sh", violations)


class TestDeliver(DeliveryBase):
    def test_pushed(self):
        workspace, _, _ = self.setup_run()
        entry = fix.read(workspace, fix.ACCEPTED_ENTRY).replace(
            "2023-korinek-genai-economic-research", "2026-pushed-entry")
        fix.write(workspace, "library/entries/2026-pushed-entry.md", entry)
        pairs = self.deliver(workspace)
        self.assertEqual(pairs["outcome"], "pushed")
        self.assertTrue(pairs["commit"])
        log = subprocess.run(["git", "log", "-1", "--format=%s", "main"],
                             cwd=self.origin, capture_output=True, text=True)
        self.assertIn("radar: daily run 2026-07-23", log.stdout)

    def test_no_change_when_reports_exist_at_base(self):
        workspace, _, _ = self.setup_run()
        self.assertEqual(self.deliver(workspace)["outcome"], "no-change")

    def test_rejected_on_remote_advance_and_final_push_failed(self):
        workspace, _, _ = self.setup_run()
        fix.write(self.origin, "library/rejections.md",
                  fix.read(self.origin, "library/rejections.md")
                  + "- 2026-07-23 - example.org/race - human push\n")
        fix.commit_all(self.origin, "human race commit")
        try:
            fix.write(workspace, "library/entries/2026-race-entry.md",
                      fix.read(workspace, fix.ACCEPTED_ENTRY).replace(
                          "2023-korinek-genai-economic-research",
                          "2026-race-entry"))
            self.assertEqual(self.deliver(workspace)["outcome"], "rejected")
            workspace2, _, _ = self.setup_run()
            fix.write(workspace2, "library/entries/2026-race-entry.md",
                      fix.read(workspace2, fix.ACCEPTED_ENTRY).replace(
                          "2023-korinek-genai-economic-research",
                          "2026-race-entry"))
            self.assertEqual(self.deliver(workspace2, final=True)["outcome"],
                             "push-failed")
        finally:
            subprocess.run(["git", "reset", "--hard", "HEAD~1"],
                           cwd=self.origin, capture_output=True, check=True)


class TestOutcomeClassification(unittest.TestCase):
    def classify(self, **kw):
        defaults = dict(mode="schedule", authgate="success", model1="success",
                        validate1="pass", revalidate1="none", deliver1="pushed",
                        model2="none", deliver2_verdict="none",
                        deliver2_outcome="none", validate1_class="none")
        defaults.update(kw)
        return rd.classify_outcome(**defaults)

    def test_happy_path(self):
        self.assertEqual(self.classify(), ("success", 1))

    def test_no_change(self):
        self.assertEqual(self.classify(deliver1="no-change"), ("no-change", 1))

    def test_auth_boundary_breach(self):
        self.assertEqual(self.classify(authgate="failure"), ("auth", 1))

    def test_model_failure_is_auth_class(self):
        self.assertEqual(self.classify(model1="failure", validate1="none",
                                       deliver1="none"), ("auth", 1))

    def test_tooling_on_evidence_abort_before_delivery(self):
        self.assertEqual(self.classify(validate1="abort",
                                       validate1_class="tooling",
                                       deliver1="none"), ("tooling", 1))

    def test_validation_on_content_abort_before_delivery(self):
        self.assertEqual(self.classify(validate1="abort",
                                       validate1_class="validation",
                                       deliver1="none"), ("validation", 1))

    def test_every_failure_class_is_incomplete_never_success(self):
        """Regression for stage-4a run 30016278453: an abort/tooling verdict
        must never classify as a successful outcome in any mode."""
        for mode in ("dry-run", "no-push", "full", "schedule"):
            for verdict, klass in (("abort", "tooling"), ("abort", "validation"),
                                   ("repairable", "none")):
                outcome, _ = self.classify(mode=mode, validate1=verdict,
                                           validate1_class=klass,
                                           deliver1="none")
                self.assertNotIn(outcome, ("success", "no-change"),
                                 "%s/%s/%s" % (mode, verdict, klass))

    def test_validation_after_failed_repair(self):
        self.assertEqual(self.classify(validate1="repairable",
                                       revalidate1="abort", deliver1="none"),
                         ("validation", 1))

    def test_race_then_success_is_two_attempt_success(self):
        self.assertEqual(self.classify(deliver1="rejected", model2="success",
                                       deliver2_verdict="pass",
                                       deliver2_outcome="pushed"),
                         ("success", 2))

    def test_double_race_is_push_failure(self):
        self.assertEqual(self.classify(deliver1="rejected", model2="success",
                                       deliver2_verdict="pass",
                                       deliver2_outcome="push-failed"),
                         ("push", 2))

    def test_dry_run_is_no_change(self):
        self.assertEqual(self.classify(mode="dry-run", model1="none",
                                       validate1="pass", deliver1="none"),
                         ("no-change", 1))

    def test_bail_retry_then_delivery_is_two_attempt_success(self):
        """2026-07-28 review: degenerate attempt 1 (evidence-missing abort,
        delivery skipped) recovered by a clean attempt 2 classifies success."""
        self.assertEqual(self.classify(validate1="abort",
                                       validate1_class="tooling",
                                       deliver1="none", model2="success",
                                       deliver2_verdict="pass",
                                       deliver2_outcome="pushed"),
                         ("success", 2))

    def test_bail_retry_then_no_change_is_two_attempt_no_change(self):
        self.assertEqual(self.classify(validate1="abort",
                                       validate1_class="tooling",
                                       deliver1="none", model2="success",
                                       deliver2_verdict="pass",
                                       deliver2_outcome="no-change"),
                         ("no-change", 2))

    def test_second_bail_is_tooling_failure_never_a_third_attempt(self):
        self.assertEqual(self.classify(validate1="abort",
                                       validate1_class="tooling",
                                       deliver1="none", model2="success",
                                       deliver2_verdict="abort",
                                       deliver2_class="tooling",
                                       deliver2_outcome="none"),
                         ("tooling", 2))

    def test_bail_retry_with_content_violation_is_validation(self):
        self.assertEqual(self.classify(validate1="abort",
                                       validate1_class="tooling",
                                       deliver1="none", model2="success",
                                       deliver2_verdict="abort",
                                       deliver2_class="validation",
                                       deliver2_outcome="none"),
                         ("validation", 2))

    def test_bail_retry_model_failure_is_auth(self):
        self.assertEqual(self.classify(validate1="abort",
                                       validate1_class="tooling",
                                       deliver1="none", model2="failure",
                                       deliver2_verdict="abort",
                                       deliver2_class="tooling",
                                       deliver2_outcome="none"),
                         ("auth", 2))


class TestSummarizeOutputs(DeliveryBase):
    """The summarize outputs drive the diagnostics upload and the outcome
    gate; stdout must stay pure summary markdown (no key=value pollution)."""

    def summarize(self, validate1, validate1_class, deliver1):
        workspace, pristine, _ = self.setup_run()
        out = workspace + "-sum-out"
        result = subprocess.run(
            [sys.executable, SCRIPT, "summarize",
             "--workspace", workspace, "--pristine", pristine,
             "--mode", "no-push", "--authgate", "success",
             "--oauth-ready", "true", "--model1", "success",
             "--validate1", validate1, "--validate1-class", validate1_class,
             "--deliver1", deliver1, "--base", "origin/main",
             "--run-date", RUN_DATE, "--github-output", out],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        with open(out, encoding="utf-8") as handle:
            pairs = dict(line.split("=", 1)
                         for line in handle.read().splitlines() if "=" in line)
        return pairs, result.stdout

    def test_tooling_abort_emits_incomplete_true(self):
        pairs, stdout = self.summarize("abort", "tooling", "none")
        self.assertEqual(pairs["outcome"], "tooling")
        self.assertEqual(pairs["incomplete"], "true")
        self.assertIn("| run status | operationally incomplete |", stdout)
        self.assertNotIn("incomplete=", stdout)  # outputs never pollute stdout

    def test_clean_no_push_run_emits_incomplete_false(self):
        pairs, stdout = self.summarize("pass", "none", "none")
        self.assertEqual(pairs["outcome"], "no-change")
        self.assertEqual(pairs["incomplete"], "false")
        self.assertIn("# Radar run summary", stdout)


if __name__ == "__main__":
    unittest.main()
