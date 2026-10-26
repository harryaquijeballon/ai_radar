"""Scan-coverage sensor (plan 2026-10-16-001 U12; enforces R53, measures R59).

The scan-evidence artifact (R39) proves a receipt exists; its self-reported
`curated_sources_fetched` count did not separate a healthy run from a
collapsed one (U11 A/B: 4/4 vs 3/4, ten entries vs none). This sensor
measures the work itself: it reads the model's actual WebFetch calls from the
Claude Code execution log and matches each URL against the `fetch hosts`
column of the active watchlists in `profiles/<domain>/sources.md`.

Per domain it reports how many fetchable watchlist sources the run attempted
and how many returned without a tool error. Sources with no fetch host (the
column holds `—`) are reachable only through search and stay out of the
denominator. Both domains are scanned in one session, so a fetch of a host
shared by both watchlists counts for both.

Hosts match exactly, as the egress allowlist does; `host/prefix` patterns
also require the URL path to start with the prefix (case-insensitive).

Two modes:
- report-only (default): write the coverage record (`--report-out`) and pass.
  The record holds watchlist names, counts, and hostname-shaped strings only:
  never URLs, paths, queries, or tool results.
- enforcing (`--min-ratio domain=0.36`, repeatable): a domain below its floor,
  or a missing execution log, is an abort (TOOLING) violation.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlsplit

import lib_radar
from lib_radar import ABORT, Violation, emit, register_rule

register_rule("COVERAGE_LOG_MISSING", ABORT,
              "execution log is absent or unreadable; coverage cannot be measured")
register_rule("COVERAGE_BELOW_FLOOR", ABORT,
              "curated-source coverage for {domain} is {attempted} of {fetchable}, "
              "below the floor {floor}")

FETCH_TOOL = "WebFetch"
HOSTS_HEADER = "fetch hosts"
NO_HOSTS = ("", "—", "-")
_PATTERN_RE = re.compile(r"^[a-z0-9.-]+(/[A-Za-z0-9._/-]*)?$")
_HOST_RE = re.compile(r"^[a-z0-9.-]{1,63}$")
MAX_UNMATCHED_HOSTS = 20


def _cells(line: str) -> List[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_sources(text: str) -> List[Tuple[str, List[Tuple[str, str]]]]:
    """Active watchlist rows as (name, [(host, path_prefix)]). Only tables
    whose header's last column is `fetch hosts` are watchlists; prose
    sections and other tables are ignored. A malformed pattern raises
    ValueError (the profile is human-controlled; fail closed)."""
    sources = []
    in_table = False
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            in_table = False
            continue
        cells = _cells(line)
        if not in_table:
            in_table = cells[-1].lower() == HOSTS_HEADER
            continue
        if set(cells[0]) <= set("-: "):
            continue  # separator row
        patterns = []
        for raw in cells[-1].split(","):
            pattern = raw.strip().strip("`").strip()
            if pattern in NO_HOSTS:
                continue
            if not _PATTERN_RE.match(pattern):
                raise ValueError("malformed fetch-host pattern")
            host, _, path = pattern.partition("/")
            patterns.append((host, "/" + path.lower() if path else ""))
        sources.append((cells[0], patterns))
    return sources


def load_watchlists(profiles_root: str) -> Dict[str, list]:
    watchlists = {}
    for domain in lib_radar.DOMAINS:
        path = os.path.join(profiles_root, domain, "sources.md")
        with open(path, encoding="utf-8") as handle:
            watchlists[domain] = parse_sources(handle.read())
    return watchlists


def extract_fetches(messages) -> List[Tuple[str, str, bool]]:
    """(host, lowercased path, errored) for every WebFetch call in the log.
    A call with no recorded result (the session died) counts as errored."""
    calls = []
    errored = {}
    for message in messages:
        if not isinstance(message, dict):
            continue
        payload = message.get("message")
        content = payload.get("content") if isinstance(payload, dict) else None
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "tool_use" and block.get("name") == FETCH_TOOL:
                target = block.get("input")
                url = target.get("url") if isinstance(target, dict) else None
                if isinstance(url, str):
                    calls.append((block.get("id"), url))
            elif block.get("type") == "tool_result":
                errored[block.get("tool_use_id")] = bool(block.get("is_error"))
    fetches = []
    for call_id, url in calls:
        try:
            parts = urlsplit(url.strip())
            host = (parts.hostname or "").lower()
        except ValueError:
            host, parts = "", None
        path = parts.path.lower() if parts is not None else ""
        fetches.append((host, path, errored.get(call_id, True)))
    return fetches


def _matches(patterns, host: str, path: str) -> bool:
    return any(host == p_host and path.startswith(p_path)
               for p_host, p_path in patterns)


def build_record(watchlists: Dict[str, list], fetches) -> dict:
    record = {"web_fetches": len(fetches), "domains": {}}
    matched_any = [False] * len(fetches)
    for domain, sources in watchlists.items():
        section = {"fetchable": 0, "attempted": 0, "succeeded": 0,
                   "not_attempted": [], "attempted_all_failed": [],
                   "search_only": []}
        for name, patterns in sources:
            if not patterns:
                section["search_only"].append(name)
                continue
            section["fetchable"] += 1
            hits = [index for index, (host, path, _) in enumerate(fetches)
                    if _matches(patterns, host, path)]
            for index in hits:
                matched_any[index] = True
            if not hits:
                section["not_attempted"].append(name)
                continue
            section["attempted"] += 1
            if any(not fetches[index][2] for index in hits):
                section["succeeded"] += 1
            else:
                section["attempted_all_failed"].append(name)
        section["ratio"] = (round(section["attempted"] / section["fetchable"], 2)
                            if section["fetchable"] else None)
        record["domains"][domain] = section
    unmatched: Dict[str, List[int]] = {}
    for index, (host, _, failed) in enumerate(fetches):
        if matched_any[index]:
            continue
        key = host if _HOST_RE.match(host) else "[other]"
        tally = unmatched.setdefault(key, [0, 0])
        tally[0] += 1
        tally[1] += int(failed)
    record["unmatched_fetches"] = sum(t[0] for t in unmatched.values())
    record["unmatched_hosts"] = {
        host: {"fetches": tally[0], "failed": tally[1]}
        for host, tally in sorted(unmatched.items(),
                                  key=lambda item: (-item[1][0], item[0]))
        [:MAX_UNMATCHED_HOSTS]}
    return record


def load_execution_log(path: str) -> Optional[list]:
    """The SDK message array, or None when absent or malformed."""
    if not path or not os.path.isfile(path):
        return None
    try:
        with open(path, encoding="utf-8") as handle:
            messages = json.load(handle)
    except (OSError, ValueError):
        return None
    return messages if isinstance(messages, list) else None


def measure(profiles_root: str, execution_log: str) -> Optional[dict]:
    messages = load_execution_log(execution_log)
    if messages is None:
        return None
    return build_record(load_watchlists(profiles_root), extract_fetches(messages))


def check_floors(record: Optional[dict], floors: Dict[str, float]) -> List[Violation]:
    label = "scan-coverage"
    if record is None:
        return [emit("COVERAGE_LOG_MISSING", label)]
    violations = []
    for domain, floor in sorted(floors.items()):
        section = record["domains"][domain]
        if section["fetchable"] and section["ratio"] < floor:
            violations.append(emit("COVERAGE_BELOW_FLOOR", label, domain=domain,
                                   attempted=section["attempted"],
                                   fetchable=section["fetchable"], floor=floor))
    return violations


def parse_floor(value: str) -> Tuple[str, float]:
    domain, _, ratio = value.partition("=")
    if domain not in lib_radar.DOMAINS:
        raise argparse.ArgumentTypeError("unknown domain")
    floor = float(ratio)
    if not 0 <= floor <= 1:
        raise argparse.ArgumentTypeError("floor must be within 0..1")
    return domain, floor


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execution-log", default="")
    parser.add_argument("--profiles-root", required=True,
                        help="profiles/ directory of the pristine base copy")
    parser.add_argument("--report-out", default=None,
                        help="write the coverage record here (JSON)")
    parser.add_argument("--min-ratio", type=parse_floor, action="append",
                        default=[], help="domain=floor; enforcing mode")
    args = parser.parse_args()
    record = measure(args.profiles_root, args.execution_log)
    if args.report_out and record is not None:
        with open(args.report_out, "w", encoding="utf-8") as handle:
            json.dump(record, handle, indent=2, sort_keys=True)
            handle.write("\n")
    if not args.min_ratio:
        return lib_radar.EXIT_PASS
    return lib_radar.report(check_floors(record, dict(args.min_ratio)))


if __name__ == "__main__":
    sys.exit(lib_radar.run_main(main))
