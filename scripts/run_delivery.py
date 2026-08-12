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
import os
import subprocess
import sys

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

    for name, check_args in checks:
        code, out = _run_validator(args.pristine, name, check_args)
        lines += out.splitlines()
        internal |= code == lib_radar.EXIT_INTERNAL

    if args.violations_out:
        with open(args.violations_out, "w", encoding="utf-8") as handle:
            handle.write("\n".join(lines) + ("\n" if lines else ""))

    has_abort = internal or any(line.startswith("ABORT ")
                                or line.startswith("INTERNAL ") for line in lines)
    has_repairable = any(line.startswith("REPAIRABLE ") for line in lines)

    if tooling or (not args.skip_evidence and internal and not lines):
        verdict, failure_class = "abort", "tooling"
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
    nonempty = [line for line in lines if line.strip()]
    degenerate = (not internal and len(nonempty) == 1
                  and nonempty[0].startswith("ABORT EVIDENCE_MISSING"))

    _emit([("verdict", verdict), ("failure_class", failure_class),
           ("violation_count", len(nonempty)),
           ("degenerate", "true" if degenerate else "false")],
          args.github_output)
    return 0


# --- deliver -----------------------------------------------------------------

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

    _git(args.git_dir, args.workspace,
         ["commit", "-q", "-m", "radar: daily run %s" % run_date])
    sha = _git(args.git_dir, None, ["rev-parse", "HEAD"]).stdout.strip()

    push = _git(args.git_dir, None,
                ["push", args.remote, "HEAD:refs/heads/main"], check=False)
    if push.returncode == 0:
        _emit([("outcome", "pushed"), ("commit", sha)], args.github_output)
        return 0
    stderr = push.stderr.lower()
    if "non-fast-forward" in stderr or "[rejected]" in stderr \
            or "fetch first" in stderr:
        outcome = "push-failed" if args.final else "rejected"
    else:
        outcome = "push-error"
    _emit([("outcome", outcome), ("commit", sha)], args.github_output)
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
            return ("tooling" if deliver2_class == "tooling"
                    else "validation"), 2
        return "push", 2
    if "failure" in (model1, model2):
        return "auth", attempts
    verdicts = [value for value in (validate1, revalidate1) if value != "none"]
    final_verdict = verdicts[-1] if verdicts else "none"
    if final_verdict in ("abort", "repairable"):
        if final_verdict == "abort" and validate1_class == "tooling" \
                and deliver1 == "none":
            return "tooling", attempts
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
    summary = mrs.build_summary(
        args.workspace, args.base, args.git_dir, run_date, outcome, attempts,
        commit, args.oauth_ready == "true", artifacts_note=incomplete,
        evidence_path=args.evidence)
    # stdout carries ONLY the safe summary markdown (the workflow tees it to
    # the step summary, the log, and the diagnostics artifact); machine
    # outputs go to the --github-output file so the gate and upload steps
    # can branch on them.
    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as handle:
            handle.write("outcome=%s\nattempts=%d\nincomplete=%s\n"
                         % (outcome, attempts, "true" if incomplete else "false"))
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
    p_validate.add_argument("--github-output", default=None)

    p_deliver = sub.add_parser("deliver")
    p_deliver.add_argument("--workspace", required=True)
    p_deliver.add_argument("--git-dir", required=True)
    p_deliver.add_argument("--base", required=True)
    p_deliver.add_argument("--remote", required=True)
    p_deliver.add_argument("--final", action="store_true")
    p_deliver.add_argument("--run-date", default=None)
    p_deliver.add_argument("--github-output", default=None)

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
