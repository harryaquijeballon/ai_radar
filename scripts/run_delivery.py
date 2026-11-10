"""Deterministic delivery orchestrator for the unattended harness
(plan U8; enforces R7, R25-R27, R30, R41, R42; consumes the U2-U4 validators).

Subcommands, each invoked by a workflow step and always executed from the
read-only pristine base copy (R41):

- validate   — run the complete validator suite against the model workspace
               and classify: pass | repairable | abort (with failure class).
               `--final` forbids further repair: repairable becomes abort.
- deliver    — stage, atomically commit, and fast-forward push via the
               harness-owned git dir; classify: pushed | no-change | rejected
               | push-error. Never force-pushes, merges, or rebases.
- summarize  — map recorded step outcomes to the run's outcome class and emit
               the safe job summary (delegates to make_run_summary).

Outputs are `key=value` lines appended to --github-output (and stdout).
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "validators"))
sys.path.insert(0, _HERE)

import lib_radar  # noqa: E402

DOMAINS = lib_radar.DOMAINS
QUEUE_GLOBS = ("reviews/source_proposals", "reviews/deferred_candidates")


def _emit(pairs, github_output):
    lines = ["%s=%s" % (key, value) for key, value in pairs]
    for line in lines:
        print(line)
    if github_output:
        with open(github_output, "a", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + "\n")


def _run_validator(pristine, name, args):
    script = os.path.join(pristine, "scripts", "validators", name)
    result = subprocess.run([sys.executable, script] + args,
                           capture_output=True, text=True)
    return result.returncode, result.stdout


# --- validate ----------------------------------------------------------------

def cmd_validate(args) -> int:
    run_date = args.run_date or lib_radar.london_today().isoformat()
    lines = []
    tooling = False
    internal = False

    if not args.skip_evidence:
        code, out = _run_validator(args.pristine, "check_scan_evidence.py",
                                   ["--evidence", args.evidence,
                                    "--run-date", run_date])
        lines += out.splitlines()
        if code != lib_radar.EXIT_PASS:
            tooling = True
        internal |= code == lib_radar.EXIT_INTERNAL

    checks = [
        ("check_changed_paths.py",
         ["--base", args.base, "--work-tree", args.workspace,
          "--run-date", run_date, "--mode", "unattended"]
         + (["--git-dir", args.git_dir] if args.git_dir else [])),
        ("check_library_consistency.py", ["--workspace", args.workspace]),
        ("check_report_integrity.py",
         ["--workspace", args.workspace, "--run-date", run_date]),
    ]
    queue_paths = []
    for rel in QUEUE_GLOBS:
        directory = os.path.join(args.workspace, rel)
        if os.path.isdir(directory):
            queue_paths += [os.path.join(directory, name)
                            for name in sorted(os.listdir(directory))
                            if name.endswith(".md")]
    if queue_paths:
        checks.append(("check_queue_records.py", queue_paths))

    # Plan 2026-11-09-001 U5: the repair pass may not raise verification or
    # status (an evidence judgment). Only on revalidation after a repair.
    if args.pre_repair_entries:
        checks.append(("check_repair_scope.py",
                       ["--before", args.pre_repair_entries,
                        "--workspace", args.workspace]))

    for name, check_args in checks:
        code, out = _run_validator(args.pristine, name, check_args)
        lines += out.splitlines()
        internal |= code == lib_radar.EXIT_INTERNAL

    # Plan 2026-11-09-001 U7: a scan below the agreed coverage floors is not
    # delivered (user decision 2026-11-09). Measured from the scan attempt's
    # own transcript (U2 snapshot), never self-reported; fails closed when
    # the transcript is missing. Dry runs have no model step and skip it.
    coverage_lines = []
    if not args.skip_evidence and args.scan_transcript is not None:
        code, out = _run_validator(
            args.pristine, "check_scan_coverage.py",
            ["--execution-log", args.scan_transcript, "--profiles-root",
             os.path.join(args.pristine, "profiles"), "--enforce-floors"])
        coverage_lines = out.splitlines()
        lines += coverage_lines
        internal |= code == lib_radar.EXIT_INTERNAL
    coverage_abort = any(line.startswith("ABORT COVERAGE_")
                         for line in coverage_lines)

    if args.violations_out:
        with open(args.violations_out, "w", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + ("\n" if lines else ""))

    has_abort = internal or any(line.startswith("ABORT ")
                                or line.startswith("INTERNAL ") for line in lines)
    has_repairable = any(line.startswith("REPAIRABLE ") for line in lines)

    other_abort = internal or any(
        (line.startswith("ABORT ") or line.startswith("INTERNAL "))
        and not line.startswith("ABORT COVERAGE_") for line in lines)
    if tooling or (not args.skip_evidence and internal and not lines):
        verdict, failure_class = "abort", "tooling"
    elif coverage_abort and not other_abort and not has_repairable:
        verdict, failure_class = "abort", "coverage"
    elif has_abort:
        verdict, failure_class = "abort", "validation"
    elif has_repairable:
        verdict = "abort" if args.final else "repairable"
        failure_class = "validation" if args.final else "none"
    else:
        verdict, failure_class = "pass", "none"

    # Degenerate-run signature (2026-07-28 model-bail review): the model ended
    # without producing the evidence artifact and violated nothing else. Only
    # this exact signature is retry-eligible — a missing artifact alongside any
    # other violation (protected path, history, queue rewrite) is not, and a
    # malformed artifact emits a different token, so it is not either.
    # A degenerate run also scans nothing, so its coverage lines (U7) do not
    # disqualify it from the retry.
    nonempty = [line for line in lines if line.strip()]
    signature = [line for line in nonempty
                 if not line.startswith("ABORT COVERAGE_")]
    degenerate = (not internal and len(signature) == 1
                  and signature[0].startswith("ABORT EVIDENCE_MISSING"))

    _emit([("verdict", verdict), ("failure_class", failure_class),
           ("violation_count", len(nonempty)),
           ("degenerate", "true" if degenerate else "false")],
          args.github_output)
    return 0


# --- deliver -----------------------------------------------------------------

# 2026-09-01 diagnosis (run 33087741300, 2026-08-27): a single transient push
# error threw away an otherwise complete run. Transient errors are retried;
# non-fast-forward rejections are not (attempt 2 owns the race, R27).
PUSH_RETRY_DELAYS = (5, 15)  # seconds before tries 2 and 3 (3 tries total)

_REJECTION_MARKERS = ("non-fast-forward", "[rejected]", "fetch first")


def _redact_remotes(text):
    """Git echoes the remote URL in push errors; its userinfo is the delivery
    token and must never reach a diagnostics artifact."""
    return re.sub(r"://[^/@\s]+@", "://[redacted]@", text)


def _git(git_dir, work_tree, extra, check=True):
    command = ["git", "-c", "user.name=ai-radar harness",
               "-c", "user.email=radar-harness@users.noreply.github.com",
               "--git-dir", git_dir]
    if work_tree:
        command += ["--work-tree", work_tree]
    command += extra
    return subprocess.run(command, capture_output=True, text=True, check=check)


def cmd_deliver(args) -> int:
    run_date = args.run_date or lib_radar.london_today().isoformat()
    _git(args.git_dir, args.workspace, ["add", "-A"])
    status = _git(args.git_dir, args.workspace,
                  ["status", "--porcelain"]).stdout.strip()

    if not status:
        reports_ok = True
        for domain in DOMAINS:
            probe = _git(args.git_dir, None,
                         ["cat-file", "-e", "%s:reports/%s/daily/%s.md"
                          % (args.base, domain, run_date)], check=False)
            reports_ok &= probe.returncode == 0
        outcome = "no-change" if reports_ok else "tooling"
        _emit([("outcome", outcome), ("commit", "")], args.github_output)
        return 0

    # Plan 2026-11-09-001 U8: the scan's turns, cost and duration travel
    # with the commit as trailers (numbers only), so git history holds the
    # effort record after the run logs expire. No transcript, no trailers.
    import run_metrics
    message = "radar: daily run %s" % run_date
    trailers = run_metrics.trailer_lines(
        run_metrics.scan_metrics(args.scan_transcript))
    if trailers:
        message += "\n\n" + "\n".join(trailers)
    _git(args.git_dir, args.workspace, ["commit", "-q", "-m", message])
    sha = _git(args.git_dir, None, ["rev-parse", "HEAD"]).stdout.strip()

    delays = tuple(int(part) for part in args.push_retry_delays.split(",")
                   if part.strip() != "") if args.push_retry_delays is not None \
        else PUSH_RETRY_DELAYS
    stderr_log = []
    attempt = 0
    while True:
        attempt += 1
        push = _git(args.git_dir, None,
                    ["push", args.remote, "HEAD:refs/heads/main"], check=False)
        if push.returncode == 0:
            outcome = "pushed"
            break
        stderr_log.append("--- push attempt %d of %d (exit %d) ---\n%s"
                          % (attempt, len(delays) + 1, push.returncode,
                             push.stderr))
        stderr = push.stderr.lower()
        if any(marker in stderr for marker in _REJECTION_MARKERS):
            outcome = "push-failed" if args.final else "rejected"
            break
        if attempt > len(delays):
            outcome = "push-error"
            break
        time.sleep(delays[attempt - 1])
    if stderr_log and args.diagnostics_dir:
        os.makedirs(args.diagnostics_dir, exist_ok=True)
        name = "push-stderr-deliver%s.txt" % ("2" if args.final else "1")
        with open(os.path.join(args.diagnostics_dir, name), "w",
                  encoding="utf-8") as handle:
            handle.write(_redact_remotes("\n".join(stderr_log)))
    _emit([("outcome", outcome), ("commit", sha),
           ("push_attempts", attempt)], args.github_output)
    return 0


# --- summarize ---------------------------------------------------------------

def classify_outcome(mode, authgate, model1, validate1, revalidate1, deliver1,
                     model2, deliver2_verdict, deliver2_outcome,
                     validate1_class="none", deliver2_class="none"):
    """Deterministic map from step outcomes to the run's failure taxonomy."""
    if authgate == "failure":
        return "auth", 1
    attempt2_ran = model2 in ("success", "failure") \
        or deliver2_verdict not in ("none", "")
    attempts = 2 if attempt2_ran else 1
    if attempt2_ran:
        # Attempt 2 is final and authoritative whether it was triggered by a
        # push race (deliver1 rejected) or a degenerate attempt-1 model run
        # (2026-07-28 review): its own outcome classifies the whole run.
        if model2 == "failure":
            return "auth", 2
        if deliver2_outcome == "pushed":
            return "success", 2
        if deliver2_outcome == "no-change":
            return "no-change", 2
        if deliver2_verdict == "abort":
            return (deliver2_class if deliver2_class in ("tooling", "coverage")
                    else "validation"), 2
        return "push", 2
    if "failure" in (model1, model2):
        return "auth", attempts
    verdicts = [value for value in (validate1, revalidate1) if value != "none"]
    final_verdict = verdicts[-1] if verdicts else "none"
    if final_verdict in ("abort", "repairable"):
        if final_verdict == "abort" and validate1_class in ("tooling", "coverage") \
                and deliver1 == "none":
            return validate1_class, attempts
        return "validation", attempts
    if deliver1 == "pushed":
        return "success", attempts
    if deliver1 == "no-change":
        return "no-change", attempts
    if deliver1 in ("tooling",):
        return "tooling", attempts
    if deliver1 in ("push-failed", "push-error"):
        return "push", attempts
    if mode in ("dry-run", "no-push") and final_verdict in ("pass", "none"):
        return "no-change", attempts
    return "tooling", attempts


def _violation_keys(path):
    """Multiset of (class, rule, file) per violation line: line numbers shift
    when a repair edits a file, so they are not part of the identity."""
    keys = []
    if path and os.path.isfile(path):
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                parts = line.split()
                if len(parts) >= 3 and parts[0] in ("ABORT", "REPAIRABLE", "INTERNAL"):
                    keys.append((parts[0], parts[1], parts[2].rsplit(":", 1)[0]
                                 if parts[2].rsplit(":", 1)[-1].isdigit()
                                 else parts[2]))
    return sorted(keys)


_RULE_ID = re.compile(r"^[A-Z][A-Z0-9_]{2,60}$")


def rule_counts(path):
    """Plan 2026-11-09-001 U9: [(rule id, count)] for a findings file, most
    frequent first. Rule ids are registered constants; anything else is
    dropped. The run summary carries them into the job log, which is kept
    for 90 days; the diagnostics artifact (30 days) had expired before the
    2026-09-10/11/12 failures were written up, and their rules were lost."""
    counts = {}
    for _, rule, _ in _violation_keys(path):
        if _RULE_ID.match(rule):
            counts[rule] = counts.get(rule, 0) + 1
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))


def classify_repair(revalidate_verdict, before_path, after_path):
    """Plan 2026-11-09-001 U6: what the bounded repair pass achieved, as one
    of make_run_summary.REPAIR_OUTCOMES.
    None when no repair ran. `regressed` = it created a violation that was not
    there before (08-07, 09-27, 11-05); `no_progress` = same violations (10-30)."""
    if revalidate_verdict in ("none", "", None):
        return None
    if revalidate_verdict == "pass":
        return "fixed"
    before = _violation_keys(before_path)
    after = _violation_keys(after_path)
    remaining = list(before)
    for key in after:
        if key not in remaining:
            return "regressed"
        remaining.remove(key)
    return "no_progress" if after == before else "partial"


def cmd_summarize(args) -> int:
    import make_run_summary as mrs
    run_date = (lib_radar.parse_iso_date(args.run_date)
                if args.run_date else lib_radar.london_today())
    verdict2, _, outcome2 = (args.deliver2.partition(":")
                             if args.deliver2 else ("none", "", "none"))
    outcome, attempts = classify_outcome(
        args.mode, args.authgate, args.model1, args.validate1,
        args.revalidate1, args.deliver1, args.model2, verdict2, outcome2,
        validate1_class=args.validate1_class,
        deliver2_class=args.deliver2_class)
    incomplete = outcome not in ("success", "no-change")
    commit = args.deliver2_commit or args.deliver1_commit or ""
    # U12 coverage sensor, report-only until the user sets per-domain floors:
    # the scan's actual fetches against the pristine watchlists.
    coverage = False
    if args.execution_log is not None:
        import check_scan_coverage as csc
        coverage = csc.measure(os.path.join(args.pristine, "profiles"),
                               args.execution_log)
        if coverage is not None and args.coverage_out:
            with open(args.coverage_out, "w", encoding="utf-8") as handle:
                json.dump(coverage, handle, indent=2, sort_keys=True)
                handle.write("\n")
    # Plan 2026-11-09-001 U3: count of grow-only queue fields the harness
    # restored before validation (one derived line each; absent file = 0).
    queue_restored = None
    if args.queue_restored_log is not None:
        queue_restored = 0
        if os.path.isfile(args.queue_restored_log):
            with open(args.queue_restored_log, encoding="utf-8") as handle:
                queue_restored = sum(1 for line in handle
                                     if line.startswith("RESTORED "))
    # Plan 2026-11-09-001 U7b: duplicate entry writes the guard blocked
    # during the model step, and the guard's own faults (it fails open).
    entry_guard = None
    if args.entry_guard_log is not None:
        blocked = errors = 0
        if os.path.isfile(args.entry_guard_log):
            with open(args.entry_guard_log, encoding="utf-8") as handle:
                for line in handle:
                    blocked += line.startswith("BLOCKED ")
                    errors += line.startswith("GUARD_ERROR ")
        entry_guard = (blocked, errors)
    # Plan 2026-11-09-001 U8: scan effort against the last delivered runs
    # (trailers in the base commit's history). Report-only.
    import run_metrics
    effort = None
    if args.execution_log is not None:
        effort = run_metrics.evaluate(
            run_metrics.scan_metrics(args.execution_log),
            run_metrics.turns_history(args.git_dir, args.base))
    summary = mrs.build_summary(
        args.workspace, args.base, args.git_dir, run_date, outcome, attempts,
        commit, args.oauth_ready == "true", artifacts_note=incomplete,
        evidence_path=args.evidence, coverage=coverage,
        queue_restored=queue_restored, entry_guard=entry_guard,
        effort=effort,
        findings=[(label, rule_counts(path)) for label, path in (
            ("attempt 1", args.violations_before),
            ("after repair", args.violations_after),
            ("attempt 2", args.violations_attempt2))],
        repair_outcome=classify_repair(args.revalidate1, args.violations_before,
                                       args.violations_after))
    # stdout carries ONLY the safe summary markdown (the workflow tees it to
    # the step summary, the log, and the diagnostics artifact); machine
    # outputs go to the --github-output file so the gate and upload steps
    # can branch on them.
    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as handle:
            handle.write("outcome=%s\nattempts=%d\nincomplete=%s\n"
                         % (outcome, attempts, "true" if incomplete else "false"))
            handle.write("alarm=%s\n" % (
                ",".join(effort["alarms"]) if effort and effort["alarms"]
                else "none"))
    print(summary)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate")
    p_validate.add_argument("--workspace", required=True)
    p_validate.add_argument("--pristine", required=True)
    p_validate.add_argument("--git-dir", default=None)
    p_validate.add_argument("--base", required=True)
    p_validate.add_argument("--evidence", default="")
    p_validate.add_argument("--skip-evidence", action="store_true")
    p_validate.add_argument("--final", action="store_true")
    p_validate.add_argument("--run-date", default=None)
    p_validate.add_argument("--violations-out", default=None)
    p_validate.add_argument("--scan-transcript", default=None,
                            help="the scan attempt's transcript; enforces the "
                                 "U7 coverage floors (omit to skip)")
    p_validate.add_argument("--pre-repair-entries", default=None,
                            help="snapshot of library/entries/ before the "
                                 "repair pass; enforces U5 repair scope")
    p_validate.add_argument("--github-output", default=None)

    p_deliver = sub.add_parser("deliver")
    p_deliver.add_argument("--workspace", required=True)
    p_deliver.add_argument("--git-dir", required=True)
    p_deliver.add_argument("--base", required=True)
    p_deliver.add_argument("--scan-transcript", default=None,
                           help="the scan attempt's execution log; its turns, "
                                "cost and duration become commit trailers (U8)")
    p_deliver.add_argument("--remote", required=True)
    p_deliver.add_argument("--final", action="store_true")
    p_deliver.add_argument("--run-date", default=None)
    p_deliver.add_argument("--github-output", default=None)
    p_deliver.add_argument("--diagnostics-dir", default=None)
    p_deliver.add_argument("--push-retry-delays", default=None,
                           help="comma-separated seconds between transient-"
                                "error retries (tests pass 0,0); default %s"
                                % (PUSH_RETRY_DELAYS,))

    p_summarize = sub.add_parser("summarize")
    p_summarize.add_argument("--workspace", required=True)
    p_summarize.add_argument("--pristine", required=True)
    p_summarize.add_argument("--git-dir", default=None)
    p_summarize.add_argument("--mode", default="schedule")
    p_summarize.add_argument("--authgate", default="success")
    p_summarize.add_argument("--oauth-ready", default="false")
    p_summarize.add_argument("--model1", default="none")
    p_summarize.add_argument("--validate1", default="none")
    p_summarize.add_argument("--revalidate1", default="none")
    p_summarize.add_argument("--deliver1", default="none")
    p_summarize.add_argument("--deliver1-commit", default="")
    p_summarize.add_argument("--model2", default="none")
    p_summarize.add_argument("--deliver2", default="none:none")
    p_summarize.add_argument("--deliver2-commit", default="")
    p_summarize.add_argument("--validate1-class", default="none")
    p_summarize.add_argument("--deliver2-class", default="none")
    p_summarize.add_argument("--evidence", default="")
    p_summarize.add_argument("--execution-log", default=None,
                             help="execution log of the scan attempt (U12 "
                                  "coverage rows); omit to skip them")
    p_summarize.add_argument("--coverage-out", default=None)
    p_summarize.add_argument("--violations-before", default=None,
                             help="validator findings that sent attempt 1 to "
                                  "repair (harness-private copy; U6)")
    p_summarize.add_argument("--violations-after", default=None,
                             help="findings at revalidation after the repair")
    p_summarize.add_argument("--queue-restored-log", default=None,
                             help="normalize_queue_appends.py report (U3 "
                                  "summary row); omit to skip the row")
    p_summarize.add_argument("--violations-attempt2", default=None,
                             help="findings at attempt 2's validation (U9 "
                                  "summary row)")
    p_summarize.add_argument("--entry-guard-log", default=None,
                             help="entry_write_guard.py log (U7b summary "
                                  "rows); omit to skip the rows")
    p_summarize.add_argument("--base", required=True)
    p_summarize.add_argument("--run-date", default=None)
    p_summarize.add_argument("--github-output", default=None)

    args = parser.parse_args()
    if args.command == "validate":
        return cmd_validate(args)
    if args.command == "deliver":
        return cmd_deliver(args)
    return cmd_summarize(args)


if __name__ == "__main__":
    sys.exit(lib_radar.run_main(main))
