"""Clean-base validator for interactive/manual runs (plan U3; enforces R24, R29).

Preconditions before any manual radar run starts:
- the working tree is clean (nothing uncommitted — the run must never touch,
  stash, or overwrite human work in progress);
- origin/main is known;
- the local branch has not diverged from origin/main (same commit, ahead-only,
  or behind-only). Behind-only passes: the caller then performs an ff-only
  sync, which is the permitted action. Diverged history aborts — resolution
  belongs to the user.

All rules abort-class: an abort here means "do not start the run".
Exit codes per the validator contract: 0 pass, 1 violations, 2 internal error.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from typing import List

import lib_radar
from lib_radar import ABORT, Violation, emit, register_rule

register_rule("DIRTY_TREE", ABORT,
              "working tree has uncommitted changes - commit, stash, or discard first")
register_rule("NOT_FAST_FORWARD", ABORT,
              "local branch and origin/main have diverged ({ahead} ahead / {behind} behind)")
register_rule("UPSTREAM_MISSING", ABORT,
              "origin/main is not known - fetch origin first")


def _git(args: List[str], repo: str) -> bytes:
    return subprocess.run(["git"] + args, cwd=repo,
                          capture_output=True, check=True).stdout


def validate(repo: str) -> List[Violation]:
    violations: List[Violation] = []
    status = _git(["status", "--porcelain", "-z"], repo)
    for part in status.split(b"\0"):
        if part:
            path = part.decode("utf-8", "replace")[3:]
            violations.append(emit("DIRTY_TREE", path))
    try:
        _git(["rev-parse", "--verify", "origin/main"], repo)
    except subprocess.CalledProcessError:
        violations.append(emit("UPSTREAM_MISSING", "origin/main"))
        return violations
    counts = _git(["rev-list", "--left-right", "--count", "HEAD...origin/main"],
                  repo).decode().split()
    ahead, behind = int(counts[0]), int(counts[1])
    if ahead and behind:
        violations.append(emit("NOT_FAST_FORWARD", "origin/main",
                               ahead=ahead, behind=behind))
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="repository to check")
    args = parser.parse_args()
    return lib_radar.report(validate(args.repo))


if __name__ == "__main__":
    sys.exit(lib_radar.run_main(main))
