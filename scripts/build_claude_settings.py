"""Generate the model step's permission settings from the egress allowlist
(plan U7/U8; enforces R48 and the S1 Option A egress decision).

The unattended model step gets exactly:
- file Read/Edit inside the workspace checkout, minus `.git/`;
- Read/Edit on the harness-designated evidence directory (outside the repo);
- WebSearch, and WebFetch only for domains listed in
  `profiles/egress_allowlist.md` — no other network surface;
- no Bash, no PowerShell (bare-name deny removes them from the model's
  context entirely), and no access to the runner temp directory where the
  GitHub control files ($GITHUB_ENV, $GITHUB_OUTPUT, ...) live;
- no tools that defer work past the end of the turn (subagents, wake-ups,
  messaging; `DEFERRAL_TOOLS`), which a non-interactive run silently drops.

With `--guard-script`, it also registers the entry write guard
(`entry_write_guard.py`) as a PreToolUse hook on Write. The CLI runs the
hook itself, so the model cannot skip it and needs no shell for it. With
`--finish-script`, it registers the scan finish guard
(`scan_finish_guard.py`) as a Stop hook; the workflow builds the repair
pass's settings without it.

Deny rules override allows; in a non-interactive run, anything not allowed
does not execute. Run from the pristine base copy (R41).
"""

from __future__ import annotations

import argparse
import json
import re
import shlex
import sys

DOMAIN_RE = re.compile(r"^- ([a-z0-9][a-z0-9.-]*\.[a-z]{2,})$")


def read_allowlist(path: str) -> list:
    domains = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            match = DOMAIN_RE.match(line.strip())
            if match and match.group(1) not in domains:
                domains.append(match.group(1))
    if not domains:
        raise ValueError("egress allowlist contains no domains")
    return domains


# Plan 2026-11-09-001 U1: tools that hand work to something that outlives the
# agent's turn. In a non-interactive run the end of the turn is the end of
# the session, so that work is silently lost: the 2026-09-01 scan (run
# 33492847557) and the 2026-10-30 repair pass (run 41044727227,
# docs/ops/2026-10-30-repair-pass-stall-incident.md). A prompt rule did not
# stop the second one, so they are denied by bare name, which removes them
# from the model's context like Bash. `Task` is the older name of `Agent`.
DEFERRAL_TOOLS = ("Agent", "Task", "ScheduleWakeup", "ListAgents",
                  "SendMessage", "Monitor", "CronCreate", "RemoteTrigger")

MODEL_ID = re.compile(r"^claude-[a-z0-9.-]+$")
# U11 (docs/ops/2026-10-16-scan-depth-collapse-incident.md): the unpinned
# default moved to claude-sonnet-5-5 on 2026-09-29 and the scan collapsed.
# Pinned to the model that passed the same-day A/B; change only by commit.
PINNED_MODEL = "claude-sonnet-5"


def build_guard_hook(guard_script: str, workspace: str, pristine: str,
                     guard_log: str = "") -> dict:
    """Plan 2026-11-09-001 U7b: run the entry write guard before every Write.
    On 2026-11-10 (run 42819765946) the scan missed dedup on five papers and
    wrote over two existing entries; the day was lost at validation."""
    command = "python3 %s --workspace %s --pristine %s" % (
        shlex.quote(guard_script), shlex.quote(workspace),
        shlex.quote(pristine))
    if guard_log:
        command += " --log %s" % shlex.quote(guard_log)
    return {"PreToolUse": [{
        "matcher": "Write",
        "hooks": [{"type": "command", "command": command, "timeout": 30}],
    }]}


def build_finish_hook(finish_script: str, pristine: str,
                      finish_log: str = "") -> dict:
    """Plan 2026-11-09-001 U7c: when the scan tries to end its turn, measure
    coverage and send it back below the floor (run 43017169301 was discarded
    at 9 of 19 social-science sources). Scan sessions only: the repair pass
    fetches nothing by design and gets settings without this hook."""
    command = "python3 %s --pristine %s" % (shlex.quote(finish_script),
                                            shlex.quote(pristine))
    if finish_log:
        command += " --log %s" % shlex.quote(finish_log)
    return {"Stop": [{
        "hooks": [{"type": "command", "command": command, "timeout": 30}],
    }]}


def build_settings(domains: list, evidence_dir: str, runner_temp: str,
                   model: str = "", hooks: dict = None) -> dict:
    allow = [
        "Read(./**)",
        "Edit(./**)",
        "Read(//%s/**)" % evidence_dir.strip("/"),
        "Edit(//%s/**)" % evidence_dir.strip("/"),
        "WebSearch",
    ]
    allow += ["WebFetch(domain:%s)" % domain for domain in domains]
    deny = [
        "Bash",
        "PowerShell",
        "Read(.git/**)",
        "Edit(.git/**)",
        "Read(//%s/**)" % runner_temp.strip("/"),
        "Edit(//%s/**)" % runner_temp.strip("/"),
    ]
    deny += list(DEFERRAL_TOOLS)
    settings = {"permissions": {"allow": allow, "deny": deny}}
    model = model or PINNED_MODEL
    if not MODEL_ID.match(model):
        raise ValueError("model id rejected: not a claude-* identifier")
    settings["model"] = model
    if hooks:
        settings["hooks"] = hooks
    return settings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allowlist", required=True)
    parser.add_argument("--evidence-dir", required=True)
    parser.add_argument("--runner-temp", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--model", default="")
    parser.add_argument("--guard-script", default="",
                        help="entry_write_guard.py in the pristine base")
    parser.add_argument("--workspace", default="")
    parser.add_argument("--pristine", default="")
    parser.add_argument("--guard-log", default="")
    parser.add_argument("--finish-script", default="",
                        help="scan_finish_guard.py in the pristine base "
                             "(scan settings only, never the repair pass)")
    parser.add_argument("--finish-log", default="")
    args = parser.parse_args()
    hooks = None
    if args.guard_script:
        if not (args.workspace and args.pristine):
            raise ValueError("--guard-script needs --workspace and --pristine")
        hooks = build_guard_hook(args.guard_script, args.workspace,
                                 args.pristine, args.guard_log)
    if args.finish_script:
        if not args.pristine:
            raise ValueError("--finish-script needs --pristine")
        hooks = dict(hooks or {})
        hooks.update(build_finish_hook(args.finish_script, args.pristine,
                                       args.finish_log))
    settings = build_settings(read_allowlist(args.allowlist),
                              args.evidence_dir, args.runner_temp, args.model,
                              hooks)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(settings, handle, indent=2)
        handle.write("\n")
    print("settings written: %d fetch domains allowed; model: %s"
          % (sum(1 for rule in settings["permissions"]["allow"]
                 if rule.startswith("WebFetch(")),
             settings["model"]))
    print("entry_write_guard=%s scan_finish_guard=%s" % (
        "on" if hooks and "PreToolUse" in hooks else "off",
        "on" if hooks and "Stop" in hooks else "off"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
