"""Scan-evidence artifact validator (plan U4; enforces R39).

The model step writes a machine-readable JSON artifact to a harness-designated
path OUTSIDE the repository tree. This validator checks presence and structure
on every outcome — including no-change — and its absence is a TOOLING failure.
Existence and structure are deterministic; the truthfulness of the attested
activity is the documented accepted model-judgment risk.

DRAFT artifact schema (finalized in U5):

    {
      "run_date": "2026-07-23",
      "domains": {
        "social_science":  {"curated_sources_fetched": 12, "queries_executed": 5},
        "ai_engineering":  {"curated_sources_fetched": 9,  "queries_executed": 4}
      }
    }

A domain lacking both a positive curated-fetch count and a positive query
count has no evidence of a functioning scan. All rules abort-class (mapped to
the TOOLING failure class by the harness).
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys
from typing import List

import lib_radar
from lib_radar import ABORT, Violation, emit, register_rule

register_rule("EVIDENCE_MISSING", ABORT,
              "scan-evidence artifact is absent")
register_rule("EVIDENCE_MALFORMED", ABORT,
              "scan-evidence artifact is not valid JSON of the expected shape ({reason})")
register_rule("EVIDENCE_DATE_MISMATCH", ABORT,
              "scan-evidence run_date does not match the run date ({run_date})")
register_rule("EVIDENCE_DOMAIN_MISSING", ABORT,
              "scan-evidence lacks a section for domain {domain}")
register_rule("EVIDENCE_NO_ACTIVITY", ABORT,
              "scan-evidence shows no curated fetches and no queries for {domain}")


def validate(evidence_path: str, run_date: datetime.date) -> List[Violation]:
    label = "scan-evidence"
    if not os.path.isfile(evidence_path):
        return [emit("EVIDENCE_MISSING", label)]
    try:
        with open(evidence_path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError):
        return [emit("EVIDENCE_MALFORMED", label, reason="not-json")]
    if not isinstance(data, dict):
        return [emit("EVIDENCE_MALFORMED", label, reason="not-object")]

    violations: List[Violation] = []
    if data.get("run_date") != run_date.isoformat():
        violations.append(emit("EVIDENCE_DATE_MISMATCH", label,
                               run_date=run_date.isoformat()))
    domains = data.get("domains")
    if not isinstance(domains, dict):
        violations.append(emit("EVIDENCE_MALFORMED", label, reason="no-domains"))
        return violations
    for domain in lib_radar.DOMAINS:
        section = domains.get(domain)
        if not isinstance(section, dict):
            violations.append(emit("EVIDENCE_DOMAIN_MISSING", label, domain=domain))
            continue
        fetched = section.get("curated_sources_fetched")
        queries = section.get("queries_executed")
        if not isinstance(fetched, int) or not isinstance(queries, int) \
                or isinstance(fetched, bool) or isinstance(queries, bool) \
                or fetched < 0 or queries < 0:
            violations.append(emit("EVIDENCE_MALFORMED", label,
                                   reason="bad-counts"))
        elif fetched == 0 and queries == 0:
            violations.append(emit("EVIDENCE_NO_ACTIVITY", label, domain=domain))
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", required=True,
                        help="path to the evidence artifact (outside the repo tree)")
    parser.add_argument("--run-date", default=None, help="YYYY-MM-DD Europe/London")
    args = parser.parse_args()
    if args.run_date:
        run_date = lib_radar.parse_iso_date(args.run_date)
        if run_date is None:
            print("INTERNAL VALIDATOR_ERROR - BadRunDate")
            return lib_radar.EXIT_INTERNAL
    else:
        run_date = lib_radar.london_today()
    return lib_radar.report(validate(args.evidence, run_date))


if __name__ == "__main__":
    sys.exit(lib_radar.run_main(main))
