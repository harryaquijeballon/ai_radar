"""Structural tests for the harness (plan U7; R28, R32, R41, R45, R48, R49).

The workflow YAML is asserted textually (stdlib has no YAML parser; these are
deliberate string contracts on a file we own). The settings generator is
tested functionally.
"""

import os
import re
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts"))

import build_claude_settings as bcs  # noqa: E402

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WORKFLOW = os.path.join(REPO, ".github", "workflows", "radar-daily.yml")


def workflow_text():
    with open(WORKFLOW, encoding="utf-8") as handle:
        return handle.read()


class TestWorkflowStructure(unittest.TestCase):
    def setUp(self):
        self.text = workflow_text()

    def test_auth_boundary_r32(self):
        self.assertNotIn("anthropic_api_key:", self.text)
        self.assertIn("ANTHROPIC_API_KEY present in environment", self.text)
        self.assertIn("secrets.CLAUDE_CODE_OAUTH_TOKEN != ''", self.text)
        # The only Anthropic credential reference is the OAuth secret:
        secrets = set(re.findall(r"secrets\.([A-Z_]+)", self.text))
        self.assertEqual(secrets, {"CLAUDE_CODE_OAUTH_TOKEN"})

    def test_schedule_active_at_approved_time_only(self):
        """Exactly one schedule at the approved time, plus manual dispatch —
        nothing else. 04:37 UTC (user-approved 2026-07-27): GitHub cron is
        UTC-only, so no timezone key — the first live fires showed it ignored
        (2026-07-27 ops note)."""
        active = [line.split("#")[0].strip() for line in self.text.split("\n")
                  if not line.strip().startswith("#")]
        self.assertIn("schedule:", active)
        self.assertIn('- cron: "37 4 * * *"', active)
        self.assertNotIn("timezone:", self.text.split("workflow_dispatch")[0])
        self.assertEqual(sum(1 for line in active if line.startswith("- cron:")), 1)
        self.assertIn("workflow_dispatch:", active)

    def test_every_checkout_disables_credential_persistence_r49(self):
        checkouts = self.text.count("uses: actions/checkout@")
        self.assertEqual(checkouts, 2)  # attempt 1 + attempt 2
        self.assertEqual(self.text.count("persist-credentials: false"), 2)

    def test_concurrency_queue_dont_cancel_r28(self):
        self.assertIn("group: radar-daily", self.text)
        self.assertIn("cancel-in-progress: false", self.text)

    def test_permissions_and_delivery_credential_scope(self):
        self.assertIn("permissions:\n  contents: write\n  id-token: write",
                      self.text)
        # The push token appears only as env of delivery steps, never globally:
        self.assertNotIn("GITHUB_TOKEN:", self.text)
        self.assertEqual(self.text.count("RADAR_PUSH_TOKEN: ${{ github.token }}"), 2)

    def test_model_steps_use_pinned_settings_and_prompt_file(self):
        model_steps = self.text.count(
            "uses: anthropics/claude-code-action@374f254f5efaf968abfe15d399fd90972e8138b9")
        self.assertEqual(model_steps, 3)  # attempt 1, repair 1, attempt 2
        # U11: no floating tag may remain — it moved three times unannounced.
        self.assertNotRegex(self.text, r"claude-code-action@v\d+\s*$")
        self.assertNotIn("claude-code-action@v1\n", self.text)
        # The two scan steps share one settings file; the repair pass has
        # its own, without the scan finish guard (plan 2026-11-09-001 U7c).
        self.assertEqual(
            self.text.count("settings: ${{ runner.temp }}/claude-settings.json"),
            2)
        repair = self.text.split("id: repair1")[1].split("- name:")[0]
        self.assertIn(
            "settings: ${{ runner.temp }}/claude-settings-repair.json", repair)
        build = self.text.split("Build model settings")[1].split("- name:")[0]
        scan, repair_build = build.split("claude-settings.json", 1)
        self.assertIn('--finish-script "$RUNNER_TEMP/pristine/scripts/'
                      'scan_finish_guard.py"', scan)
        self.assertIn('--finish-log "$RUNNER_TEMP/radar-private/'
                      'finish-guard.txt"', scan)
        self.assertNotIn("--finish-script", repair_build)
        self.assertIn("--guard-script", repair_build)
        summary = self.text.split("Job summary (always")[1].split("- name:")[0]
        self.assertIn('--finish-guard-log "$RUNNER_TEMP/radar-private/'
                      'finish-guard.txt"', summary)
        self.assertIn(".github/prompts/daily-radar.md", self.text)

    def test_all_scripts_execute_from_pristine_copy_r41(self):
        for call in re.findall(r"python3 \"([^\"]+)\"", self.text):
            self.assertTrue(call.startswith("$RUNNER_TEMP/pristine/"), call)
        self.assertIn("chmod -R a-w \"$RUNNER_TEMP/pristine\"", self.text)

    def test_attempt_two_is_statically_unrolled_and_bounded(self):
        self.assertIn("attempt 2", self.text)
        self.assertNotIn("attempt 3", self.text)
        self.assertIn("Re-materialize pristine base and harness clone (attempt 2)",
                      self.text)
        self.assertIn('rm -f "$RADAR_EVIDENCE_PATH"', self.text)  # stale-reset

    def test_summary_always_teed_and_artifacts_on_failure_or_incomplete(self):
        self.assertIn("if: always()", self.text)
        self.assertIn("if: failure() || steps.summary.outputs.incomplete == 'true'",
                      self.text)
        self.assertIn("uses: actions/upload-artifact@v7", self.text)
        # Summary reaches the job summary, the plain log, and the artifact:
        self.assertIn('cat "$RADAR_DIR/diagnostics/run-summary.md" >> "$GITHUB_STEP_SUMMARY"',
                      self.text)
        self.assertEqual(
            self.text.count('cat "$RADAR_DIR/diagnostics/run-summary.md"'), 2)
        # Evidence and violations always land in the diagnostics dir first:
        self.assertIn('cp "$RADAR_EVIDENCE_PATH" "$RADAR_DIR/diagnostics/"',
                      self.text)
        self.assertIn('cp "$RADAR_DIR"/violations-*.txt "$RADAR_DIR/diagnostics/"',
                      self.text)

    def test_degenerate_retry_gates_use_step_outputs_only(self):
        """2026-07-28 model-bail review: all five attempt-2 steps must also
        fire on the degenerate attempt-1 signature (evidence-missing as the
        sole violation after a successful model step), and the new conditions
        must be step-output driven — never inputs.* (2026-07-27 incident)."""
        degenerate = "steps.validate1.outputs.degenerate == 'true'"
        model_ok = "steps.model1.outcome == 'success'"
        self.assertEqual(self.text.count(degenerate), 5)
        self.assertEqual(self.text.count(model_ok), 5)
        # Each degenerate condition is paired with the push-race one:
        self.assertEqual(
            self.text.count("steps.deliver1.outputs.outcome == 'rejected'"), 5)

    def test_model_run_facts_derived_never_raw_execution_log(self):
        """R43 + 2026-07-28 review: diagnostics carry only the derived facts
        record; the raw execution log (contains fetched content) is never
        copied or uploaded."""
        self.assertEqual(self.text.count("summarize_execution_log.py"), 3)
        self.assertIn("model-run-facts.json", self.text)
        self.assertIn("model-run-facts-attempt1.json", self.text)
        self.assertIn("--deliver2-class", self.text)
        for line in self.text.split("\n"):
            if "execution_file" in line:
                self.assertNotIn("cp ", line)
                self.assertNotIn("upload", line.lower())
        # The one transcript copy (U2 snapshot) lands in the harness-private
        # runner-temp dir, never in the evidence or diagnostics dirs:
        copies = [line.strip() for line in self.text.split("\n")
                  if "scan-transcript" in line and line.strip().startswith("cp ")]
        self.assertEqual(copies, [
            'cp "$SCAN_TRANSCRIPT" '
            '"$RUNNER_TEMP/radar-private/scan-transcript-attempt1.json"'])
        upload = self.text.split("uses: actions/upload-artifact@v7")[1]
        self.assertIn("path: /tmp/radar/diagnostics/", upload)
        self.assertNotIn("radar-private", upload.split("- name:")[0])

    def test_coverage_measured_from_scan_attempt_report_only(self):
        """Plan 2026-10-16-001 U12, fixed by plan 2026-11-09-001 U2: every
        model invocation writes the same execution_file path, so the repair
        pass overwrote the scan transcript. Coverage now reads attempt 2's
        own transcript or the attempt-1 snapshot taken before any repair,
        and nothing enforces a floor until the user sets one."""
        snapshot = self.text.index("Snapshot attempt-1 transcript (before any repair)")
        self.assertLess(self.text.index("id: model1"), snapshot)
        self.assertLess(snapshot, self.text.index("id: repair1"))
        summary = self.text.split("Job summary (always")[1].split("- name:")[0]
        self.assertIn('SCAN_LOG="${{ steps.model2.outputs.execution_file || \'\' }}"',
                      summary)
        self.assertIn('SNAPSHOT="$RUNNER_TEMP/radar-private/'
                      'scan-transcript-attempt1.json"', summary)
        self.assertIn('--execution-log "$SCAN_LOG"', summary)
        self.assertNotIn("repair1.outputs.execution_file || steps.model1"
                         ".outputs.execution_file || '' }}\" \\\n"
                         "            --coverage-out", summary)
        self.assertIn('--coverage-out "$RADAR_DIR/diagnostics/coverage.json"',
                      summary)
        self.assertNotIn("--min-ratio", self.text)
        # The attempt-2 reset reads the snapshot too (a push race can follow
        # a repaired attempt 1):
        reset = self.text.split("Preserve attempt-1 diagnostics and reset")[1] \
            .split("- name:")[0]
        self.assertIn("scan-transcript-attempt1.json", reset)
        self.assertNotIn("execution_file", reset)

    def test_runner_image_pinned(self):
        """Plan 2026-11-09-001 U4: ubuntu-latest moved to 26.04 unannounced
        (HDAI-AIRADAR-001 P-rule: pin every input that can change a run)."""
        self.assertIn("runs-on: ubuntu-26.04", self.text)
        self.assertNotIn("ubuntu-latest\n", self.text)
        self.assertNotRegex(self.text, r"runs-on: ubuntu-latest\s")

    def test_queue_normaliser_runs_before_every_validation(self):
        """Plan 2026-11-09-001 U3: the P9 deadlock is fixed by a script that
        restores grow-only queue text before each validation (attempt 1,
        revalidation after repair, attempt 2)."""
        steps = self.text.split("      - name: ")
        validating = [s for s in steps if "run_delivery.py\" validate" in s]
        self.assertEqual(len(validating), 3)
        for step in validating:
            self.assertIn("normalize_queue_appends.py", step)
            self.assertLess(step.index("normalize_queue_appends.py"),
                            step.index("run_delivery.py\" validate"))
            self.assertIn('--report-out "$RUNNER_TEMP/radar-private/'
                          'queue-restored.txt"', step)
        summary = self.text.split("Job summary (always")[1].split("- name:")[0]
        self.assertIn('--queue-restored-log "$RUNNER_TEMP/radar-private/'
                      'queue-restored.txt"', summary)

    def test_coverage_floors_gate_every_scan_validation(self):
        """Plan 2026-11-09-001 U7: every validation of a scan passes that
        scan's own transcript, so a run below the floors is not delivered."""
        steps = self.text.split("      - name: ")
        validating = [s for s in steps if "run_delivery.py\" validate" in s]
        attempt1 = [s for s in validating if "pristine.outputs.base_sha" in s]
        self.assertEqual(len(attempt1), 2)  # validate1 + revalidate1
        for step in attempt1:
            self.assertIn('--scan-transcript "$RUNNER_TEMP/radar-private/'
                          'scan-transcript-attempt1.json"', step)
        attempt2 = [s for s in validating if "pristine2.outputs.base_sha" in s]
        self.assertEqual(len(attempt2), 1)
        self.assertIn("SCAN_TRANSCRIPT_2: ${{ steps.model2.outputs.execution_file }}",
                      attempt2[0])
        self.assertIn('--scan-transcript "${SCAN_TRANSCRIPT_2:-}"', attempt2[0])

    def test_repair_scope_and_outcome_inputs_are_harness_private(self):
        """Plan 2026-11-09-001 U5/U6: the pre-repair snapshot and the
        violations the repair was given live where the model cannot edit."""
        snap = self.text.index("Snapshot entries before repair (attempt 1)")
        self.assertLess(self.text.index("id: validate1"), snap)
        self.assertLess(snap, self.text.index("id: repair1"))
        self.assertIn('cp -R "$GITHUB_WORKSPACE/library/entries" '
                      '"$RUNNER_TEMP/radar-private/pre-repair-entries"', self.text)
        revalidate = self.text.split("id: revalidate1")[1].split("- name:")[0]
        self.assertIn('--pre-repair-entries "$RUNNER_TEMP/radar-private/'
                      'pre-repair-entries"', revalidate)
        self.assertIn('cp "$RADAR_DIR/violations-1.txt" '
                      '"$RUNNER_TEMP/radar-private/violations-1.txt"', self.text)
        summary = self.text.split("Job summary (always")[1].split("- name:")[0]
        self.assertIn('--violations-before "$RUNNER_TEMP/radar-private/'
                      'violations-1.txt"', summary)
        self.assertIn('--violations-after "$RADAR_DIR/violations-1b.txt"', summary)
        repair = self.text.split("id: repair1")[1].split("- name:")[0]
        self.assertIn("Never raise an entry's verification or status", repair)
        self.assertIn("set verification: unverified and status: provisional",
                      repair)

    def test_repair_prompt_forbids_delegation_and_shortening(self):
        """Plan 2026-11-09-001 U1: the 10-30 repair pass delegated to
        background agents and ended without an edit."""
        repair = self.text.split("id: repair1")[1].split("- name:")[0]
        self.assertIn("this session ends the moment you stop", repair)
        self.assertIn("never hand work to another agent", repair)
        self.assertIn("Never shorten or rephrase text that already existed "
                      "in a queue record", repair)

    def test_delivery_gate_covers_scheduled_runs(self):
        """Regression for runs 30154883225/30198956789: `inputs.mode` is empty
        on schedule triggers, so a gate of mode == 'full' alone silently skips
        delivery on every scheduled run and discards the model's work."""
        deliver_gate = self.text.split("Deliver (attempt 1)")[1].split("run:")[0]
        self.assertIn(
            "(inputs.mode == 'full' || github.event_name == 'schedule')",
            deliver_gate)

    def test_deliver_steps_capture_push_stderr_diagnostics(self):
        """2026-09-01 diagnosis: both delivery invocations hand run_delivery a
        diagnostics dir so failed-push git stderr survives into the uploaded
        artifact (redacted by the script)."""
        self.assertEqual(
            self.text.count('--diagnostics-dir "$RADAR_DIR/diagnostics"'), 2)

    def test_outcome_gate_fails_job_on_incomplete(self):
        """Regression for run 30016278453: a non-successful classified outcome
        must fail the job in every mode, so notifications and diagnostics fire."""
        self.assertIn("Enforce run outcome (fail on incomplete)", self.text)
        gate = self.text.split("Enforce run outcome (fail on incomplete)")[1]
        self.assertIn("success|no-change)", gate)
        self.assertIn("exit 1", gate)
        self.assertIn("|| 'unknown'", gate)  # missing outputs fail closed
        # The summarize call feeds the gate its classification inputs:
        self.assertIn("--validate1-class", self.text)
        self.assertIn('--github-output "$GITHUB_OUTPUT"', self.text)


    def test_entry_write_guard_wired_from_pristine(self):
        """Plan 2026-11-09-001 U7b: the guard hook runs the pristine script
        (R41), logs to the harness-private dir, and reaches the summary."""
        build = self.text.split("Build model settings")[1].split("- name:")[0]
        self.assertIn('--guard-script "$RUNNER_TEMP/pristine/scripts/'
                      'entry_write_guard.py"', build)
        self.assertIn('--workspace "$GITHUB_WORKSPACE"', build)
        self.assertIn('--pristine "$RUNNER_TEMP/pristine"', build)
        self.assertIn('--guard-log "$RUNNER_TEMP/radar-private/'
                      'entry-guard.txt"', build)
        summary = self.text.split("Job summary (always")[1].split("- name:")[0]
        self.assertIn('--entry-guard-log "$RUNNER_TEMP/radar-private/'
                      'entry-guard.txt"', summary)


    def test_effort_alarm_is_report_only_and_trailers_wired(self):
        """Plan 2026-11-09-001 U8: the scan transcript feeds the commit
        trailers; the alarm is a warning annotation from a controlled
        value passed through env, and never blocks."""
        deliver1 = self.text.split("id: deliver1")[1].split("- name:")[0]
        self.assertIn('--scan-transcript "$RUNNER_TEMP/radar-private/'
                      'scan-transcript-attempt1.json"', deliver1)
        deliver2 = self.text.split("id: deliver2")[1].split("- name:")[0]
        self.assertEqual(deliver2.count(
            '--scan-transcript "${SCAN_TRANSCRIPT_2:-}"'), 2)
        alarm = self.text.split("Effort alarm (warning annotation")[1] \
            .split("- name:")[0]
        self.assertIn("steps.summary.outputs.alarm != 'none'", alarm)
        self.assertIn("ALARM: ${{ steps.summary.outputs.alarm }}", alarm)
        self.assertIn('echo "::warning title=Radar effort alarm::${ALARM}',
                      alarm)
        self.assertNotIn("exit 1", alarm)


class TestRuntimePrompt(unittest.TestCase):
    """Completion contract of the unattended prompt (2026-07-28 model-bail
    review): two scheduled runs died because the model ended its turn after
    the reading phase; the prompt must pin the terminal state explicitly."""

    def setUp(self):
        with open(os.path.join(REPO, ".github", "prompts", "daily-radar.md"),
                  encoding="utf-8") as handle:
            self.text = handle.read()

    def test_no_user_and_turn_end_prohibition(self):
        self.assertIn("no user is present and nobody will ever reply",
                      self.text)
        self.assertIn("Never end your turn to report progress", self.text)

    def test_explicit_success_conditions_and_final_check(self):
        self.assertIn("$RADAR_EVIDENCE_PATH", self.text)
        self.assertIn("Both daily reports exist for today", self.text)
        self.assertIn(
            "Before ending your turn, verify all three; if any is missing, "
            "keep working.", self.text)

    def test_begins_scan_immediately_after_reading(self):
        self.assertIn("Then begin the social-science scan immediately",
                      self.text)
        # CLAUDE.md is auto-loaded project context; the prompt must not
        # re-mandate reading it (wasted turns before discovery):
        self.assertIn("do not\n   re-read", self.text)

    def test_no_delegation_to_background_agents(self):
        """2026-09-01 failure (run 33492847557): the model delegated the scan
        to a background agent and ended its turn; the agent died with the
        session and the day's work was lost. The prompt must forbid
        delegation outright."""
        self.assertIn("to a subagent", self.text)
        self.assertIn("still running in the background when your turn ends",
                      self.text)

    def test_evidence_artifact_written_before_reports(self):
        """2026-09-01 hardening: a run that dies midway must leave evidence,
        never orphan reports — the artifact write precedes both report
        writes."""
        self.assertIn("no report file may exist before", self.text)
        self.assertIn("Evidence-before-reports is a hard rule", self.text)

    def test_safety_rules_preserved(self):
        for fragment in ("profiles/egress_allowlist.md", "defer",
                         "Never run git", "`.github/`", "quiet-day"):
            self.assertIn(fragment, self.text)

    def test_window_never_decides_eligibility(self):
        """Plan 2026-10-16-001 U13/U14: 243 candidates were rejected for
        their submission date. The prompt points at P6.1 and keeps the
        date-rejection ban and the arXiv listing-date rule in view."""
        text = " ".join(self.text.split())
        self.assertIn("the window decides only where you look", text)
        self.assertIn("Never reject a candidate for its date while it is "
                      "inside the 7-day cap", text)
        self.assertIn("listing date, not its submission date", text)
        self.assertNotIn("Lookback per P6.1", text)
        with open(os.path.join(REPO, "engine", "ENGINE.md"),
                  encoding="utf-8") as handle:
            engine = handle.read()
        for fragment in ("**Search window**", "**Eligibility**",
                         "**Visibility date**", "**No date-only rejections.**"):
            self.assertIn(fragment, engine)


    def test_prompt_names_the_entry_guard(self):
        """Plan 2026-11-09-001 U7b (run 42819765946)."""
        self.assertIn("search `library/INDEX.md` for the candidate's", self.text)
        self.assertIn("Never retry under another slug", self.text)

    def test_prompt_states_the_coverage_minimum(self):
        """Plan 2026-11-09-001 U7c (run 43017169301): the agent was never
        told the floors that discard its run."""
        self.assertIn("fewer than 12 social-science or 6 AI-engineering "
                      "watchlist sources is", self.text.replace("\n   ", " "))
        self.assertIn("sends you back with the sources still to fetch",
                      self.text)


class TestSettingsBuilder(unittest.TestCase):
    def test_settings_shape(self):
        with tempfile.TemporaryDirectory() as tmp:
            allowlist = os.path.join(tmp, "allow.md")
            with open(allowlist, "w") as handle:
                handle.write("# x\n\n- arxiv.org\n- nber.org\nprose\n- arxiv.org\n")
            settings = bcs.build_settings(
                bcs.read_allowlist(allowlist), "/tmp/radar", "/home/runner/work/_temp")
        allow = settings["permissions"]["allow"]
        deny = settings["permissions"]["deny"]
        self.assertIn("WebFetch(domain:arxiv.org)", allow)
        self.assertIn("WebFetch(domain:nber.org)", allow)
        self.assertEqual(sum(1 for rule in allow if rule.startswith("WebFetch")), 2)
        self.assertIn("Edit(//tmp/radar/**)", allow)
        self.assertIn("Bash", deny)
        self.assertIn("PowerShell", deny)
        self.assertIn("Edit(.git/**)", deny)
        self.assertIn("Edit(//home/runner/work/_temp/**)", deny)
        self.assertNotIn("WebFetch", deny)  # bare deny would nullify domain allows

    def test_deferral_tools_denied(self):
        """Plan 2026-11-09-001 U1: tools that hand work past the end of the
        turn are denied by bare name (runs 33492847557 and 41044727227)."""
        deny = bcs.build_settings(["arxiv.org"], "/tmp/r", "/t")["permissions"]["deny"]
        for tool in ("Agent", "Task", "ScheduleWakeup", "ListAgents",
                     "SendMessage"):
            self.assertIn(tool, deny)
        allow = bcs.build_settings(["arxiv.org"], "/tmp/r", "/t")["permissions"]["allow"]
        self.assertFalse(set(bcs.DEFERRAL_TOOLS) & set(allow))

    def test_model_pinned_by_default_and_overridable(self):
        """U11: scheduled runs get the pinned model; a dispatch may override it."""
        default = bcs.build_settings(["arxiv.org"], "/tmp/r", "/t")
        self.assertEqual(default["model"], bcs.PINNED_MODEL)
        self.assertEqual(bcs.PINNED_MODEL, "claude-sonnet-5")
        override = bcs.build_settings(["arxiv.org"], "/tmp/r", "/t", "claude-opus-5-5")
        self.assertEqual(override["model"], "claude-opus-5-5")

    def test_model_id_rejected_unless_claude_identifier(self):
        for bad in ("gpt-5", "claude-sonnet-5; rm -rf /", "claude-$(id)", " claude-x"):
            with self.assertRaises(ValueError):
                bcs.build_settings(["arxiv.org"], "/tmp/r", "/t", bad)

    def test_model_override_passed_via_env_not_interpolated(self):
        text = workflow_text()
        self.assertIn("MODEL_OVERRIDE: ${{ inputs.model }}", text)
        self.assertIn('--model "${MODEL_OVERRIDE:-}"', text)
        self.assertNotIn('--model "${{ inputs.model }}"', text)

    def test_real_allowlist_builds(self):
        domains = bcs.read_allowlist(
            os.path.join(REPO, "profiles", "egress_allowlist.md"))
        self.assertGreater(len(domains), 20)
        settings = bcs.build_settings(domains, "/tmp/radar", "/home/runner/work/_temp")
        self.assertTrue(all(isinstance(rule, str)
                            for rule in settings["permissions"]["allow"]))

    def test_empty_allowlist_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            allowlist = os.path.join(tmp, "empty.md")
            with open(allowlist, "w") as handle:
                handle.write("# nothing here\n")
            with self.assertRaises(ValueError):
                bcs.read_allowlist(allowlist)


    def test_entry_write_guard_hook(self):
        """Plan 2026-11-09-001 U7b: a PreToolUse hook on Write only; paths
        are shell-quoted; no hook unless asked for."""
        self.assertNotIn("hooks", bcs.build_settings(["arxiv.org"], "/tmp/r", "/t"))
        hooks = bcs.build_guard_hook("/p/scripts/entry_write_guard.py",
                                     "/w s", "/p", "/t/private/guard.txt")
        settings = bcs.build_settings(["arxiv.org"], "/tmp/r", "/t", hooks=hooks)
        (group,) = settings["hooks"]["PreToolUse"]
        self.assertEqual(group["matcher"], "Write")
        (hook,) = group["hooks"]
        self.assertEqual(hook["type"], "command")
        self.assertEqual(
            hook["command"],
            "python3 /p/scripts/entry_write_guard.py --workspace '/w s' "
            "--pristine /p --log /t/private/guard.txt")
        self.assertIn("Bash", settings["permissions"]["deny"])


    def test_scan_finish_guard_hook(self):
        """Plan 2026-11-09-001 U7c: a Stop hook, added next to the entry
        write guard, only when asked for."""
        hook = bcs.build_finish_hook("/p/scripts/scan_finish_guard.py", "/p",
                                     "/t/private/finish.txt")
        (group,) = hook["Stop"]
        self.assertNotIn("matcher", group)
        self.assertEqual(
            group["hooks"][0]["command"],
            "python3 /p/scripts/scan_finish_guard.py --pristine /p "
            "--log /t/private/finish.txt")


if __name__ == "__main__":
    unittest.main()
