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
                 skip_evidence=False, extra_args=None):
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
        argv += extra_args or []
        result = subprocess.run(argv, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        pairs = dict(line.split("=", 1)
                     for line in result.stdout.splitlines() if "=" in line)
        return pairs

    def deliver(self, workspace, final=False, remote=None, extra_args=None):
        out = workspace + "-deliver-out"
        argv = [sys.executable, SCRIPT, "deliver",
                "--workspace", workspace,
                "--git-dir", os.path.join(workspace, ".git"),
                "--base", "origin/main", "--run-date", RUN_DATE,
                "--remote", remote or self.origin,
                "--github-output", out]
        if final:
            argv.append("--final")
        if extra_args:
            argv += extra_args
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
        # A different development: its own identifier (U7b duplicate rule).
        new_entry = new_entry.replace("10.1257/jel.20231736", "10.9999/other")
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

    def private_remote(self, workspace):
        """A bare copy of the origin, so a push here cannot make the other
        tests' pushes to the shared origin non-fast-forward."""
        remote = workspace + "-remote.git"
        subprocess.run(["git", "clone", "-q", "--bare", self.origin, remote],
                       check=True, capture_output=True)
        return remote

    def test_commit_carries_scan_effort_trailers(self):
        """Plan 2026-11-09-001 U8: turns, cost and duration of the scan
        travel with the commit; the subject line is unchanged."""
        workspace, _, _ = self.setup_run()
        fix.write(workspace, "library/entries/2026-trailer-entry.md",
                  fix.read(workspace, fix.ACCEPTED_ENTRY).replace(
                      "2023-korinek-genai-economic-research",
                      "2026-trailer-entry"))
        log = workspace + "-scan.json"
        with open(log, "w", encoding="utf-8") as handle:
            json.dump([{"type": "result", "num_turns": 127,
                        "total_cost_usd": 3.3772014,
                        "duration_ms": 898275}], handle)
        pairs = self.deliver(workspace, remote=self.private_remote(workspace),
                             extra_args=["--scan-transcript", log])
        self.assertEqual(pairs["outcome"], "pushed")
        body = subprocess.run(["git", "log", "-1", "--format=%B", "HEAD"],
                              cwd=workspace, capture_output=True,
                              text=True).stdout
        self.assertEqual(body.strip().split("\n"), [
            "radar: daily run 2026-07-23", "", "Radar-Scan-Turns: 127",
            "Radar-Scan-Cost-USD: 3.38", "Radar-Scan-Duration-S: 898"])

    def test_missing_scan_transcript_gives_plain_commit(self):
        workspace, _, _ = self.setup_run()
        fix.write(workspace, "library/entries/2026-plain-entry.md",
                  fix.read(workspace, fix.ACCEPTED_ENTRY).replace(
                      "2023-korinek-genai-economic-research",
                      "2026-plain-entry"))
        pairs = self.deliver(
            workspace, remote=self.private_remote(workspace),
            extra_args=["--scan-transcript", workspace + "-absent.json"])
        self.assertEqual(pairs["outcome"], "pushed")
        body = subprocess.run(["git", "log", "-1", "--format=%B", "HEAD"],
                              cwd=workspace, capture_output=True,
                              text=True).stdout
        self.assertEqual(body.strip(), "radar: daily run 2026-07-23")

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
            pairs = self.deliver(workspace)
            self.assertEqual(pairs["outcome"], "rejected")
            # A rejection is a push race, not a transient error — attempt 2
            # owns the retry, so deliver must not loop on it (2026-09-01):
            self.assertEqual(pairs["push_attempts"], "1")
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

    def test_transient_push_error_retried_and_stderr_captured(self):
        """2026-09-01 diagnosis (run 33087741300, 2026-08-27): a transient
        push error gets three tries, and the git stderr survives into the
        diagnostics directory."""
        workspace, _, _ = self.setup_run()
        fix.write(workspace, "library/entries/2026-transient-entry.md",
                  fix.read(workspace, fix.ACCEPTED_ENTRY).replace(
                      "2023-korinek-genai-economic-research",
                      "2026-transient-entry"))
        diagnostics = workspace + "-diagnostics"
        pairs = self.deliver(workspace,
                             remote=workspace + "-no-such-remote",
                             extra_args=["--push-retry-delays", "0,0",
                                         "--diagnostics-dir", diagnostics])
        self.assertEqual(pairs["outcome"], "push-error")
        self.assertEqual(pairs["push_attempts"], "3")
        with open(os.path.join(diagnostics, "push-stderr-deliver1.txt"),
                  encoding="utf-8") as handle:
            captured = handle.read()
        self.assertIn("push attempt 3 of 3", captured)
        self.assertIn("no-such-remote", captured)

    def test_push_stderr_redacts_remote_credentials(self):
        """Push stderr can echo the remote URL whose userinfo is the delivery
        token; the diagnostics copy must never contain it."""
        stderr = ("fatal: unable to access 'https://x-access-token:ghs_secret"
                  "@github.com/o/r.git/': The requested URL returned error: 503")
        redacted = rd._redact_remotes(stderr)
        self.assertNotIn("ghs_secret", redacted)
        self.assertIn("://[redacted]@github.com", redacted)


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


def transcript_with_fetches(path, hosts):
    """A minimal SDK message array with one successful WebFetch per host."""
    messages = []
    for number, host in enumerate(hosts):
        call = "c%d" % number
        messages.append({"type": "assistant", "message": {"content": [
            {"type": "tool_use", "id": call, "name": "WebFetch",
             "input": {"url": "https://%s/" % host, "prompt": "p"}}]}})
        messages.append({"type": "user", "message": {"content": [
            {"type": "tool_result", "tool_use_id": call, "content": "ok"}]}})
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(messages, handle)
    return path


def watchlist_hosts(domain):
    """First fetch host of every fetchable source on the real watchlist."""
    import check_scan_coverage as csc
    hosts = []
    for _name, patterns in csc.load_watchlists(
            os.path.join(REPO_ROOT, "profiles"))[domain]:
        if patterns:
            hosts.append(patterns[0][0])
    return hosts


class TestCoverageGate(DeliveryBase):
    """Plan 2026-11-09-001 U7: below the agreed floors the run is not
    delivered (abort, outcome class `coverage`)."""

    def setup_with_profiles(self):
        workspace, pristine, evidence = self.setup_run()
        shutil.copytree(os.path.join(REPO_ROOT, "profiles"),
                        os.path.join(pristine, "profiles"))
        return workspace, pristine, evidence

    def test_healthy_scan_passes(self):
        workspace, pristine, evidence = self.setup_with_profiles()
        hosts = watchlist_hosts("social_science") + watchlist_hosts("ai_engineering")
        log = transcript_with_fetches(workspace + "-scan.json", hosts)
        pairs = self.validate(workspace, pristine, evidence,
                              extra_args=["--scan-transcript", log])
        self.assertEqual(pairs["verdict"], "pass")

    def test_hollow_scan_aborts_as_coverage_2026_09_29(self):
        workspace, pristine, evidence = self.setup_with_profiles()
        log = transcript_with_fetches(workspace + "-scan.json",
                                      watchlist_hosts("social_science")[:2])
        pairs = self.validate(workspace, pristine, evidence,
                              extra_args=["--scan-transcript", log])
        self.assertEqual(pairs["verdict"], "abort")
        self.assertEqual(pairs["failure_class"], "coverage")
        self.assertEqual(pairs["degenerate"], "false")

    def test_missing_transcript_fails_closed(self):
        workspace, pristine, evidence = self.setup_with_profiles()
        pairs = self.validate(workspace, pristine, evidence,
                              extra_args=["--scan-transcript",
                                          workspace + "-absent.json"])
        self.assertEqual((pairs["verdict"], pairs["failure_class"]),
                         ("abort", "coverage"))

    def test_dry_run_skips_the_gate(self):
        workspace, pristine, evidence = self.setup_with_profiles()
        pairs = self.validate(workspace, pristine, evidence, skip_evidence=True,
                              extra_args=["--scan-transcript",
                                          workspace + "-absent.json"])
        self.assertEqual(pairs["verdict"], "pass")

    def test_bail_with_empty_transcript_stays_retry_eligible(self):
        """A degenerate attempt 1 scans nothing; its coverage lines must not
        cancel the attempt-2 retry (2026-07-28 review)."""
        workspace, pristine, _ = self.setup_with_profiles()
        log = transcript_with_fetches(workspace + "-scan.json", [])
        pairs = self.validate(workspace, pristine, workspace + "-missing.json",
                              extra_args=["--scan-transcript", log])
        self.assertEqual(pairs["degenerate"], "true")

    def test_coverage_with_repairable_defect_is_not_repaired(self):
        """A repair cannot add fetches: a low-coverage scan never goes to
        the repair pass, whatever else it violated."""
        workspace, pristine, evidence = self.setup_with_profiles()
        fix.write(workspace, fix.ACCEPTED_ENTRY, fix.read(
            workspace, fix.ACCEPTED_ENTRY).replace("verification: ", "verification_x: ", 1))
        log = transcript_with_fetches(workspace + "-scan.json", [])
        pairs = self.validate(workspace, pristine, evidence,
                              extra_args=["--scan-transcript", log])
        self.assertEqual(pairs["verdict"], "abort")
        self.assertEqual(pairs["failure_class"], "validation")

    def test_outcome_class_is_coverage(self):
        self.assertEqual(rd.classify_outcome(
            "schedule", "success", "success", "abort", "none", "none",
            "skipped", "none", "none", validate1_class="coverage"),
            ("coverage", 1))
        self.assertEqual(rd.classify_outcome(
            "schedule", "success", "success", "abort", "none", "none",
            "success", "abort", "none", deliver2_class="coverage"),
            ("coverage", 2))


class TestRepairOutcome(unittest.TestCase):
    """Plan 2026-11-09-001 U6."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, name, *lines):
        path = os.path.join(self._tmp.name, name)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write("".join(line + "\n" for line in lines))
        return path

    def test_classes(self):
        q155 = ("REPAIRABLE QUEUE_RECORD_REWRITTEN reviews/deferred_candidates/"
                "social_science.md:155 - justification text must grow")
        q290 = ("REPAIRABLE QUEUE_TEXT_TOO_LONG reviews/deferred_candidates/"
                "social_science.md:290 - free-text field too long")
        long143 = ("REPAIRABLE QUEUE_TEXT_TOO_LONG reviews/deferred_candidates/"
                   "ai_engineering.md:143 - too long")
        rewrite143 = ("REPAIRABLE QUEUE_RECORD_REWRITTEN reviews/"
                      "deferred_candidates/ai_engineering.md:143 - must grow")
        field = ("REPAIRABLE FIELD_MISSING library/entries/a.md - required "
                 "frontmatter field verification is missing")
        before = self.write("v1.txt", q155, q290)
        # 10-30: same findings after the repair (line numbers may shift).
        same = self.write("v1b.txt", q155.replace(":155", ":157"), q290)
        self.assertEqual(rd.classify_repair("abort", before, same), "no_progress")
        # 11-05: the repair created a rewrite that was not there before.
        before2 = self.write("v2.txt", field, long143)
        after2 = self.write("v2b.txt", rewrite143)
        self.assertEqual(rd.classify_repair("abort", before2, after2), "regressed")
        after3 = self.write("v3b.txt", q290)
        self.assertEqual(rd.classify_repair("abort", before, after3), "partial")
        self.assertEqual(rd.classify_repair("pass", before, None), "fixed")
        self.assertIsNone(rd.classify_repair("none", before, same))


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

    def test_summarize_measures_coverage_from_execution_log(self):
        """Plan 2026-10-16-001 U12: watchlists come from the pristine copy;
        the record lands in diagnostics and the rows in the summary."""
        workspace, pristine, _ = self.setup_run()
        shutil.copytree(os.path.join(REPO_ROOT, "profiles"),
                        os.path.join(pristine, "profiles"))
        log = workspace + "-execution.json"
        with open(log, "w", encoding="utf-8") as handle:
            json.dump([{"type": "assistant", "message": {"content": [
                {"type": "tool_use", "id": "a", "name": "WebFetch",
                 "input": {"url": "https://simonwillison.net/", "prompt": "p"}}]}},
                {"type": "user", "message": {"content": [
                    {"type": "tool_result", "tool_use_id": "a",
                     "content": "page"}]}}], handle)
        coverage_out = workspace + "-coverage.json"
        result = subprocess.run(
            [sys.executable, SCRIPT, "summarize",
             "--workspace", workspace, "--pristine", pristine,
             "--mode", "no-push", "--model1", "success", "--validate1", "pass",
             "--base", "origin/main", "--run-date", RUN_DATE,
             "--execution-log", log, "--coverage-out", coverage_out],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertRegex(result.stdout,
                         r"\| curated coverage \(ai_engineering\) \| "
                         r"1 of \d+ attempted, 1 succeeded \|")
        with open(coverage_out, encoding="utf-8") as handle:
            self.assertEqual(
                json.load(handle)["domains"]["ai_engineering"]["succeeded"], 1)

    def test_summarize_reports_effort_and_alarm(self):
        """Plan 2026-11-09-001 U8: effort rows from the scan transcript; a
        collapsed scan raises low_turns in the summary and the outputs."""
        workspace, pristine, _ = self.setup_run()
        shutil.copytree(os.path.join(REPO_ROOT, "profiles"),
                        os.path.join(pristine, "profiles"))
        log = workspace + "-execution.json"
        out = workspace + "-effort-out"

        def run(turns, cost):
            with open(log, "w", encoding="utf-8") as handle:
                json.dump([{"type": "result", "num_turns": turns,
                            "total_cost_usd": cost, "duration_ms": 60000,
                            "usage": {"input_tokens": 1200,
                                      "cache_creation_input_tokens": 90000,
                                      "cache_read_input_tokens": 4000000,
                                      "output_tokens": 52000},
                            "modelUsage": {
                                "claude-sonnet-5": {"costUSD": 3.1},
                                "claude-haiku-5-5": {"costUSD": 0.4},
                                "x | injected": {"costUSD": 1}}}],
                          handle)
            if os.path.exists(out):
                os.remove(out)
            result = subprocess.run(
                [sys.executable, SCRIPT, "summarize",
                 "--workspace", workspace, "--pristine", pristine,
                 "--git-dir", os.path.join(workspace, ".git"),
                 "--mode", "no-push", "--model1", "success",
                 "--validate1", "pass", "--base", "origin/main",
                 "--run-date", RUN_DATE, "--execution-log", log,
                 "--github-output", out],
                capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            with open(out, encoding="utf-8") as handle:
                return result.stdout, handle.read()

        stdout, outputs = run(120, 3.5)
        self.assertIn("| scan turns | 120 |", stdout)
        self.assertIn("| scan cost (USD) | 3.50 |", stdout)
        self.assertIn("| scan duration (s) | 60 |", stdout)
        self.assertIn("| scan tokens (input / cache write / cache read / "
                      "output) | 1200 / 90000 / 4000000 / 52000 |", stdout)
        self.assertIn("| scan cost by model (USD) | claude-haiku-5-5 0.40, "
                      "claude-sonnet-5 3.10 |", stdout)
        self.assertNotIn("injected", stdout)
        self.assertIn("| turns reference | 127 (fixed baseline) |", stdout)
        self.assertIn("| effort alarm | none |", stdout)
        self.assertIn("alarm=none\n", outputs)
        stdout, outputs = run(22, 9.25)
        self.assertIn("| effort alarm | low_turns, high_cost |", stdout)
        self.assertIn("alarm=low_turns,high_cost\n", outputs)

    def test_summarize_lists_finding_rules_2026_11_10(self):
        """Plan 2026-11-09-001 U9: the rule ids of the findings reach the job
        log through the summary (run 42819765946's real findings); paths,
        messages and anything that is not a rule id do not."""
        workspace, pristine, _ = self.setup_run()
        before = workspace + "-v1.txt"
        with open(before, "w", encoding="utf-8") as handle:
            handle.write(
                "ABORT ENTRY_FRONTMATTER_FIELD_CHANGED library/entries/a.md - m\n"
                "ABORT ENTRY_FRONTMATTER_FIELD_CHANGED library/entries/a.md - m\n"
                "ABORT ENTRY_BODY_REWRITTEN library/entries/a.md - m\n"
                "REPAIRABLE REPORT_QUIET_DAY_STATEMENT_MISSING reports/"
                "social_science/daily/2026-11-10.md - m\n"
                "ABORT not-a-rule|injected library/entries/a.md - m\n")
        result = subprocess.run(
            [sys.executable, SCRIPT, "summarize",
             "--workspace", workspace, "--pristine", pristine,
             "--mode", "no-push", "--model1", "success",
             "--validate1", "abort", "--validate1-class", "validation",
             "--base", "origin/main", "--run-date", RUN_DATE,
             "--violations-before", before,
             "--violations-attempt2", workspace + "-absent.txt"],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(
            "| validation findings (attempt 1) | "
            "ENTRY_FRONTMATTER_FIELD_CHANGED x2, ENTRY_BODY_REWRITTEN x1, "
            "REPORT_QUIET_DAY_STATEMENT_MISSING x1 |", result.stdout)
        self.assertNotIn("injected", result.stdout)
        self.assertNotIn("validation findings (attempt 2)", result.stdout)
        self.assertNotIn("validation findings (after repair)", result.stdout)

    def test_summarize_counts_queue_restorations(self):
        """Plan 2026-11-09-001 U3: the normaliser's derived report becomes a
        count row; a missing report means zero; no flag means no row."""
        workspace, pristine, _ = self.setup_run()
        report = workspace + "-restored.txt"
        base_args = [sys.executable, SCRIPT, "summarize",
                     "--workspace", workspace, "--pristine", pristine,
                     "--mode", "no-push", "--model1", "success",
                     "--validate1", "pass", "--base", "origin/main",
                     "--run-date", RUN_DATE]
        result = subprocess.run(base_args + ["--queue-restored-log", report],
                                capture_output=True, text=True)
        self.assertIn("| queue fields restored by harness | 0 |", result.stdout)
        with open(report, "w", encoding="utf-8") as handle:
            handle.write("RESTORED reviews/deferred_candidates/social_science.md:"
                         "266 action_needed over_cap\nRESTORED reviews/"
                         "deferred_candidates/ai_engineering.md:143 "
                         "action_needed over_cap\n")
        result = subprocess.run(base_args + ["--queue-restored-log", report],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("| queue fields restored by harness | 2 |", result.stdout)
        result = subprocess.run(base_args, capture_output=True, text=True)
        self.assertNotIn("queue fields restored", result.stdout)

    def test_summarize_counts_entry_guard_blocks(self):
        """Plan 2026-11-09-001 U7b: blocked duplicate writes become a count
        row; guard faults get their own row only when there are any."""
        workspace, pristine, _ = self.setup_run()
        log = workspace + "-guard.txt"
        base_args = [sys.executable, SCRIPT, "summarize",
                     "--workspace", workspace, "--pristine", pristine,
                     "--mode", "no-push", "--model1", "success",
                     "--validate1", "pass", "--base", "origin/main",
                     "--run-date", RUN_DATE]
        result = subprocess.run(base_args + ["--entry-guard-log", log],
                                capture_output=True, text=True)
        self.assertIn("| duplicate entry writes blocked by harness | 0 |",
                      result.stdout)
        self.assertNotIn("entry guard errors", result.stdout)
        with open(log, "w", encoding="utf-8") as handle:
            handle.write("BLOCKED ENTRY_EXISTS library/entries/a.md\n"
                         "BLOCKED ENTRY_DUPLICATE library/entries/b.md\n"
                         "CHECKED library/entries/c.md\n"
                         "GUARD_ERROR ValueError\n")
        result = subprocess.run(base_args + ["--entry-guard-log", log],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("| duplicate entry writes blocked by harness | 2 |",
                      result.stdout)
        self.assertIn("| entry guard errors | 1 |", result.stdout)
        self.assertIn("| entry writes checked by harness guard | 3 |",
                      result.stdout)
        result = subprocess.run(base_args, capture_output=True, text=True)
        self.assertNotIn("duplicate entry writes", result.stdout)

    def test_clean_no_push_run_emits_incomplete_false(self):
        pairs, stdout = self.summarize("pass", "none", "none")
        self.assertEqual(pairs["outcome"], "no-change")
        self.assertEqual(pairs["incomplete"], "false")
        self.assertIn("# Radar run summary", stdout)


if __name__ == "__main__":
    unittest.main()
