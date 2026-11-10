"""Scan effort and cost: metrics, history and alarm (plan 2026-11-09-001 U8;
rest of plan 2026-10-16-001 U16).

From 2026-09-29 to 2026-10-16 the scan ran about 22 turns instead of about
85 and found almost nothing, while every run reported success
(docs/ops/2026-10-16-scan-depth-collapse-incident.md). The coverage floors
now catch a scan that fetches too little. This module is the second,
independent signal: how hard the scan worked and what it cost.

No state file. Each delivered daily commit carries the scan's figures as
trailers in its message, so git history is the record and outlives the
90-day run logs:

    Radar-Scan-Turns: 127
    Radar-Scan-Cost-USD: 3.38
    Radar-Scan-Duration-S: 898

Alarms (controlled vocabulary, report-only: a warning annotation and a
summary row; delivery is never blocked):

- `low_turns`: turns below LOW_TURNS_RATIO of the median of the last
  WINDOW delivered runs. With fewer than MIN_HISTORY trailers in history,
  the reference is BASELINE_TURNS.
- `high_cost`: scan cost above COST_CEILING_USD.

All figures come from the transcript's result block, which the CLI writes.
Nothing model-authored is read.
"""

from __future__ import annotations

import json
import os
import re
import statistics
import subprocess
from typing import Dict, List, Optional, Tuple

TURNS_TRAILER = "Radar-Scan-Turns"
COST_TRAILER = "Radar-Scan-Cost-USD"
DURATION_TRAILER = "Radar-Scan-Duration-S"

WINDOW = 7
MIN_HISTORY = 4
LOW_TURNS_RATIO = 0.5
# Calibrated 2026-11-10 from the scheduled runs 2026-10-17 -> 2026-11-10
# (scan turns 75-173, cost $1.58-$6.09). The median of the last seven
# delivered scans was 127 turns; the collapsed scans ran about 22.
BASELINE_TURNS = 127
COST_CEILING_USD = 8.0

ALARMS = ("low_turns", "high_cost")

_TURNS_LINE = re.compile(r"^%s: (\d{1,6})$" % TURNS_TRAILER, re.M)


def scan_metrics(execution_log) -> Optional[Dict[str, object]]:
    """{turns, cost_usd, duration_s} from the scan transcript's result
    block, or None when the transcript is missing or carries no result."""
    if not execution_log or not os.path.isfile(execution_log):
        return None
    try:
        with open(execution_log, encoding="utf-8") as handle:
            messages = json.load(handle)
    except (ValueError, OSError):
        return None
    if not isinstance(messages, list):
        return None
    result = None
    for message in messages:
        if isinstance(message, dict) and message.get("type") == "result":
            result = message
    if result is None:
        return None
    turns = result.get("num_turns")
    cost = result.get("total_cost_usd")
    duration = result.get("duration_ms")
    if isinstance(turns, bool) or not isinstance(turns, int) or turns < 0:
        return None
    metrics: Dict[str, object] = {"turns": turns}
    if isinstance(cost, (int, float)) and not isinstance(cost, bool) \
            and 0 <= cost < 10000:
        metrics["cost_usd"] = round(float(cost), 2)
    if isinstance(duration, (int, float)) and not isinstance(duration, bool) \
            and 0 <= duration < 10 ** 9:
        metrics["duration_s"] = int(round(duration / 1000.0))
    return metrics


def trailer_lines(metrics) -> List[str]:
    """Commit-message trailers for a delivered run: numbers only."""
    if not metrics:
        return []
    lines = ["%s: %d" % (TURNS_TRAILER, metrics["turns"])]
    if "cost_usd" in metrics:
        lines.append("%s: %.2f" % (COST_TRAILER, metrics["cost_usd"]))
    if "duration_s" in metrics:
        lines.append("%s: %d" % (DURATION_TRAILER, metrics["duration_s"]))
    return lines


def turns_history(git_dir, ref: str, window: int = WINDOW) -> List[int]:
    """Scan turns of the newest `window` delivered runs reachable from
    `ref`, newest first. Empty on any git failure."""
    command = ["git"]
    if git_dir:
        command += ["--git-dir", git_dir]
    command += ["log", "-n", "200", "--format=%B%x00", ref]
    try:
        done = subprocess.run(command, capture_output=True, text=True)
    except OSError:
        return []
    if done.returncode != 0:
        return []
    found: List[int] = []
    for body in done.stdout.split("\x00"):
        match = _TURNS_LINE.search(body)
        if match:
            found.append(int(match.group(1)))
            if len(found) == window:
                break
    return found


def reference_turns(history: List[int]) -> Tuple[float, str]:
    """(reference turns, "rolling" | "baseline")."""
    if len(history) >= MIN_HISTORY:
        return float(statistics.median(history)), "rolling"
    return float(BASELINE_TURNS), "baseline"


def evaluate(metrics, history: List[int]) -> Optional[Dict[str, object]]:
    """The summary record: the metrics, the reference they were compared
    with, and the alarms raised. None when there are no metrics."""
    if not metrics:
        return None
    reference, source = reference_turns(history)
    alarms = []
    if metrics["turns"] < LOW_TURNS_RATIO * reference:
        alarms.append("low_turns")
    if metrics.get("cost_usd", 0) > COST_CEILING_USD:
        alarms.append("high_cost")
    record = dict(metrics)
    record.update({"reference_turns": reference, "reference_source": source,
                   "alarms": alarms})
    return record
