"""Tests for run_metrics.py (plan 2026-11-09-001 U8)."""

import json
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.join(os.path.dirname(__file__), "..", "..")
sys.path.insert(0, os.path.join(REPO, "scripts"))

import run_metrics as rm  # noqa: E402

# Scan turns of the scheduled runs 2026-10-18 -> 2026-11-10 (run logs).
REAL_TURNS = [75, 85, 105, 91, 108, 105, 88, 80, 93, 97, 112, 125, 112, 137,
              122, 112, 118, 143, 112, 118, 142, 173, 127, 147]


def transcript(directory, turns=127, cost=3.3772014, duration_ms=898275,
               name="log.json"):
    path = os.path.join(directory, name)
    with open(path, "w", encoding="utf-8") as handle:
        json.dump([{"type": "system", "subtype": "init"},
                   {"type": "assistant", "message": {"content": [
                       {"type": "text", "text": "SECRET-MODEL-TEXT"}]}},
                   {"type": "result", "subtype": "success", "num_turns": turns,
                    "total_cost_usd": cost, "duration_ms": duration_ms}],
                  handle)
    return path


class TestScanMetrics(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="radar-metrics-")
        self.tmp = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def test_metrics_from_result_block(self):
        self.assertEqual(rm.scan_metrics(transcript(self.tmp)),
                         {"turns": 127, "cost_usd": 3.38, "duration_s": 898})

    def test_missing_or_malformed_transcript_gives_none(self):
        self.assertIsNone(rm.scan_metrics(None))
        self.assertIsNone(rm.scan_metrics(os.path.join(self.tmp, "absent")))
        bad = os.path.join(self.tmp, "bad.json")
        with open(bad, "w", encoding="utf-8") as handle:
            handle.write("{not json")
        self.assertIsNone(rm.scan_metrics(bad))
        self.assertIsNone(rm.scan_metrics(
            transcript(self.tmp, turns="many", name="t.json")))

    def test_trailers_are_numbers_only(self):
        lines = rm.trailer_lines(rm.scan_metrics(transcript(self.tmp)))
        self.assertEqual(lines, ["Radar-Scan-Turns: 127",
                                 "Radar-Scan-Cost-USD: 3.38",
                                 "Radar-Scan-Duration-S: 898"])
        self.assertEqual(rm.trailer_lines(None), [])
        odd = rm.trailer_lines(rm.scan_metrics(
            transcript(self.tmp, cost="x; rm -rf", name="o.json")))
        self.assertEqual(odd, ["Radar-Scan-Turns: 127",
                               "Radar-Scan-Duration-S: 898"])

    def test_history_read_from_commit_trailers_newest_first(self):
        repo = os.path.join(self.tmp, "repo")
        os.makedirs(repo)

        def git(*args):
            subprocess.run(["git", "-C", repo, "-c", "user.name=t",
                            "-c", "user.email=t@example.org"] + list(args),
                           check=True, capture_output=True)
        git("init", "-q")
        for number, turns in enumerate([80, None, 90, 100, 110, 120, 130,
                                        140, 150]):
            body = "radar: daily run 2026-11-%02d" % (number + 1)
            if turns is not None:
                body += "\n\nRadar-Scan-Turns: %d\nRadar-Scan-Cost-USD: 3.10" % turns
            git("commit", "-q", "--allow-empty", "-m", body)
        history = rm.turns_history(os.path.join(repo, ".git"), "HEAD")
        self.assertEqual(history, [150, 140, 130, 120, 110, 100, 90])
        self.assertEqual(rm.turns_history(os.path.join(repo, ".git"),
                                          "no-such-ref"), [])


class TestAlarm(unittest.TestCase):
    def test_baseline_until_enough_history(self):
        record = rm.evaluate({"turns": 100, "cost_usd": 3.0}, [120, 130])
        self.assertEqual(record["reference_source"], "baseline")
        self.assertEqual(record["reference_turns"], rm.BASELINE_TURNS)
        self.assertEqual(record["alarms"], [])

    def test_collapsed_scan_raises_low_turns_2026_09_29(self):
        """The 2026-09-29 -> 10-16 scans ran about 22 turns against ~85."""
        record = rm.evaluate({"turns": 22, "cost_usd": 0.6},
                             [85, 82, 91, 75, 88, 80, 84])
        self.assertEqual(record["reference_source"], "rolling")
        self.assertEqual(record["alarms"], ["low_turns"])
        self.assertEqual(rm.evaluate({"turns": 22}, [])["alarms"],
                         ["low_turns"])

    def test_high_cost(self):
        self.assertEqual(rm.evaluate({"turns": 150, "cost_usd": 8.01},
                                     [])["alarms"], ["high_cost"])
        self.assertEqual(rm.evaluate({"turns": 150, "cost_usd": 6.09},
                                     [])["alarms"], [])

    def test_no_metrics_no_record(self):
        self.assertIsNone(rm.evaluate(None, [100] * 7))

    def test_replay_real_runs_raise_no_alarm(self):
        """Every scheduled scan 2026-10-18 -> 11-10 against the rolling
        median of the seven before it: no low_turns alarm."""
        for index, turns in enumerate(REAL_TURNS):
            history = list(reversed(REAL_TURNS[max(0, index - 7):index]))
            self.assertEqual(rm.evaluate({"turns": turns}, history)["alarms"],
                             [], (index, turns, history))


if __name__ == "__main__":
    unittest.main()
