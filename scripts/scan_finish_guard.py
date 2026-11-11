"""Scan finish guard: a Stop hook on the scan session (plan 2026-11-09-001
U7c; docs/ops/2026-11-11-coverage-floor-incident.md).

Not a validator. The coverage floors (`check_scan_coverage.py`,
`ATTEMPTED_FLOORS`) are a gate after the run: below them the day is
discarded, and the agent never learns why. This hook gives the agent the
same measurement while it can still act. When the agent tries to end its
turn, the hook measures the session's WebFetch calls against the active
watchlists (from the pristine base) and, below a floor, blocks the stop
and returns the sources not yet attempted.

Hook contract: the event arrives as JSON on stdin with `transcript_path`
(the session transcript, one JSON message per line); exit 2 blocks the
stop and returns stderr to the model; exit 0 lets the session end.

Bounds:
- at most MAX_BLOCKS blocks per session, then the stop is allowed and the
  post-run gate decides;
- it fails OPEN: an unreadable transcript, or any error of its own, lets
  the session end. A guard fault must never trap a run.

It is registered for the scan only. The repair pass fetches nothing by
design and runs on settings without this hook.

The log holds derived lines only: `CHECKED`, `BLOCKED COVERAGE`, `GAVE_UP`
or `GUARD_ERROR`, a session id, and counts.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "validators"))

import check_scan_coverage as csc  # noqa: E402

MAX_BLOCKS = 2
MAX_NAMES = 12
_SESSION = re.compile(r"^[A-Za-z0-9-]{1,64}$")

MESSAGE = (
    "SCAN_COVERAGE_BELOW_FLOOR the scan is not finished. A run that attempts "
    "too few watchlist sources is discarded whole, with every entry and "
    "report written today.\n%(lines)s\n"
    "Before ending your turn: fetch the page of each source listed above "
    "(its address is in the `fetch hosts` column of "
    "profiles/<domain>/sources.md), review what is new there (P6, P7), then "
    "bring the entries, library/INDEX.md, the scan-evidence counts and both "
    "daily reports up to date. A source that fails to load still counts as "
    "attempted; do not retry it. Do not reply to this message: continue with "
    "the next fetch.")


def load_transcript(path):
    """Messages of a session transcript (JSON lines), or None when it is
    absent, unreadable or holds no assistant tool call at all."""
    if not path or not os.path.isfile(path):
        return None
    messages = []
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    item = json.loads(line)
                except ValueError:
                    continue
                if isinstance(item, dict):
                    messages.append(item)
    except OSError:
        return None
    for message in messages:
        payload = message.get("message")
        content = payload.get("content") if isinstance(payload, dict) else None
        if isinstance(content, list) and any(
                isinstance(block, dict) and block.get("type") == "tool_use"
                for block in content):
            return messages
    return None


def shortfalls(record, floors=None):
    """[(domain, attempted, required, fetchable, not_attempted names)] for
    each domain below its floor (capped at the watchlist size, as in
    check_attempted_floors)."""
    floors = csc.ATTEMPTED_FLOORS if floors is None else floors
    short = []
    for domain, floor in sorted(floors.items()):
        section = record["domains"].get(domain)
        if not section:
            continue
        required = min(floor, section["fetchable"])
        if section["attempted"] < required:
            short.append((domain, section["attempted"], required,
                          section["fetchable"], list(section["not_attempted"])))
    return short


def _prior_blocks(log_path, session: str) -> int:
    if not log_path or not os.path.isfile(log_path):
        return 0
    with open(log_path, encoding="utf-8") as handle:
        return sum(1 for line in handle
                   if line.startswith("BLOCKED COVERAGE %s " % session))


def evaluate(payload: dict, profiles_root: str, log_path=None,
             max_blocks: int = MAX_BLOCKS):
    """(log line, message | None). A message means: block the stop."""
    session = str(payload.get("session_id") or "")
    session = session if _SESSION.match(session) else "unknown"
    messages = load_transcript(payload.get("transcript_path"))
    if messages is None:
        return ("GUARD_ERROR TranscriptUnreadable %s" % session, None)
    record = csc.build_record(csc.load_watchlists(profiles_root),
                              csc.extract_fetches(messages))
    short = shortfalls(record)
    counts = " ".join("%s=%d/%d" % (domain, section["attempted"],
                                    section["fetchable"])
                      for domain, section in sorted(record["domains"].items()))
    if not short:
        return ("CHECKED %s %s" % (session, counts), None)
    if _prior_blocks(log_path, session) >= max_blocks:
        return ("GAVE_UP %s %s" % (session, counts), None)
    lines = []
    for domain, attempted, required, fetchable, names in short:
        shown = ", ".join(names[:MAX_NAMES])
        if len(names) > MAX_NAMES:
            shown += ", and %d more" % (len(names) - MAX_NAMES)
        lines.append("- %s: %d of %d watchlist sources attempted, at least "
                     "%d needed. Not yet attempted: %s."
                     % (domain, attempted, fetchable, required, shown))
    return ("BLOCKED COVERAGE %s %s" % (session, counts),
            MESSAGE % {"lines": "\n".join(lines)})


def _log(path, line: str) -> None:
    if not path:
        return
    try:
        with open(path, "a", encoding="utf-8") as handle:
            handle.write(line + "\n")
    except OSError:
        pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pristine", required=True)
    parser.add_argument("--log", default=None)
    args = parser.parse_args()
    try:
        line, message = evaluate(json.load(sys.stdin),
                                 os.path.join(args.pristine, "profiles"),
                                 args.log)
    except Exception as error:  # fail open; the post-run gate decides
        _log(args.log, "GUARD_ERROR %s" % type(error).__name__)
        return 0
    _log(args.log, line)
    if message is None:
        return 0
    sys.stderr.write(message + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
