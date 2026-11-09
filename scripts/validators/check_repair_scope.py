"""Repair-scope validator (plan 2026-11-09-001 U5).

The bounded repair pass (P11) fixes form. It must never make an evidence
judgment. On 2026-11-05 (run 42029203188) the repair set `verification:
partial` on 15 entries with zero web fetches, reasoning from the entries'
own notes (docs/ops/2026-11-05-queue-deadlock-recurrence-incident.md).

This check compares every entry file after the repair with its state just
before the repair (a harness snapshot of `library/entries/`) and allows only
moves that claim less:

- `verification` may stay the same or fall (verified > partial >
  unverified); a field the repair adds must be `unverified`.
- `status` may stay the same or fall to `provisional`; a field the repair
  adds must be `provisional`.

The schema already requires an all-unverified entry to be `provisional`
(engine/schema.md), so `unverified` + `provisional` is always a legal repair.
A later Verify Provisionals pass upgrades it with evidence.

Any raise is ABORT-class: it cannot be repaired again (P11).
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import List, Optional

import lib_radar
from lib_radar import ABORT, Violation, emit, register_rule

register_rule("REPAIR_RAISED_VERIFICATION", ABORT,
              "the repair pass raised verification (evidence judgment outside "
              "repair scope; only unverified may be added)")
register_rule("REPAIR_RAISED_STATUS", ABORT,
              "the repair pass raised status (only provisional may be added)")

VERIFICATION_RANK = {"unverified": 0, "partial": 1, "verified": 2}
STATUS_RANK = {"provisional": 0, "accepted": 1}
ADDED_ALLOWED = {"verification": "unverified", "status": "provisional"}


def _field(text: Optional[str], name: str) -> Optional[str]:
    if text is None:
        return None
    value = lib_radar.parse_frontmatter(text).fields.get(name)
    return value if isinstance(value, str) else None


def raised(name: str, before: Optional[str], after: Optional[str]) -> bool:
    """True when the repair's value claims more than the pre-repair value."""
    if after is None or after == before:
        return False
    rank = VERIFICATION_RANK if name == "verification" else STATUS_RANK
    if before is None or before not in rank:
        return after != ADDED_ALLOWED[name]
    if after not in rank:
        return False  # an invalid value is the schema validators' finding
    return rank[after] > rank[before]


def check_entry(rel_path: str, before: Optional[str], after: str) -> List[Violation]:
    violations = []
    if raised("verification", _field(before, "verification"),
              _field(after, "verification")):
        violations.append(emit("REPAIR_RAISED_VERIFICATION", rel_path))
    if raised("status", _field(before, "status"), _field(after, "status")):
        violations.append(emit("REPAIR_RAISED_STATUS", rel_path))
    return violations


def validate(before_dir: str, workspace: str) -> List[Violation]:
    entries = os.path.join(workspace, "library", "entries")
    violations: List[Violation] = []
    if not os.path.isdir(entries):
        return violations
    for name in sorted(os.listdir(entries)):
        if not name.endswith(".md"):
            continue
        with open(os.path.join(entries, name), encoding="utf-8") as handle:
            after = handle.read()
        before_path = os.path.join(before_dir, name)
        before = None
        if os.path.isfile(before_path):
            with open(before_path, encoding="utf-8") as handle:
                before = handle.read()
        if before == after:
            continue
        violations += check_entry("library/entries/" + name, before, after)
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", required=True,
                        help="snapshot of library/entries/ taken just before the repair")
    parser.add_argument("--workspace", required=True)
    args = parser.parse_args()
    if not os.path.isdir(args.before):
        raise FileNotFoundError("pre-repair snapshot missing")
    return lib_radar.report(validate(args.before, args.workspace))


if __name__ == "__main__":
    sys.exit(lib_radar.run_main(main))
