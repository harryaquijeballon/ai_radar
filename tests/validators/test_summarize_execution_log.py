"""Tests for scripts/summarize_execution_log.py (2026-07-28 model-bail
review): the derived diagnostic must answer why a model run ended without
ever exposing tool results, fetched content, URLs, or raw local paths."""

import json
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts"))

import summarize_execution_log as sel  # noqa: E402

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCRIPT = os.path.join(REPO_ROOT, "scripts", "summarize_execution_log.py")
EVIDENCE_PATH = "/tmp/radar/scan-evidence.json"

SAMPLE = [
    {"type": "system", "subtype": "init", "model": "claude-sonnet-5"},
    {"type": "assistant", "message": {"content": [
        {"type": "text", "text": "Reading the engine spec."},
        {"type": "tool_use", "name": "Read",
         "input": {"file_path": "/home/runner/work/ai_radar/engine/ENGINE.md"}},
    ]}},
    {"type": "user", "message": {"content": [
        {"type": "tool_result", "content": "FETCHED-PAGE-CONTENT-NEVER-EMIT"},
    ]}},
    {"type": "assistant", "message": {"content": [
        {"type": "tool_use", "name": "WebSearch",
         "input": {"query": "SECRET-QUERY-NEVER-EMIT"}},
        {"type": "tool_use", "name": "Write",
         "input": {"file_path": EVIDENCE_PATH, "content": "{}"}},
        {"type": "tool_use", "name": "Write",
         "input": {"file_path": "/home/runner/work/ai_radar/ai_radar/"
                                "reports/social_science/daily/2026-07-28.md",
                   "content": "report body"}},
    ]}},
    {"type": "assistant", "message": {"content": [
        {"type": "text", "text": "Now I'll run the scans."},
    ]}},
    {"type": "result", "subtype": "success", "is_error": False,
     "num_turns": 33, "duration_ms": 109004, "total_cost_usd": 0.7,
     "permission_denials_count": 0},
]


class TestBuildRecord(unittest.TestCase):
    def setUp(self):
        self.record = sel.build_record(SAMPLE, EVIDENCE_PATH)

    def test_termination_facts(self):
        self.assertEqual(self.record["result"]["subtype"], "success")
        self.assertEqual(self.record["result"]["num_turns"], 33)
        self.assertEqual(self.record["result"]["permission_denials_count"], 0)

    def test_tool_counts_and_discovery_signal(self):
        self.assertEqual(self.record["tool_calls"],
                         {"Read": 1, "WebSearch": 1, "Write": 2})
        self.assertEqual(self.record["web_searches"], 1)
        self.assertEqual(self.record["web_fetches"], 0)

    def test_artifact_and_report_detection(self):
        self.assertTrue(self.record["evidence_artifact_written"])
        self.assertEqual(self.record["report_files_written"],
                         ["reports/social_science/daily/2026-07-28.md"])

    def test_final_message_is_last_assistant_text(self):
        self.assertEqual(self.record["final_message"], "Now I'll run the scans.")
        self.assertFalse(self.record["final_message_truncated"])

    def test_final_message_truncation(self):
        long_run = SAMPLE + [{"type": "assistant", "message": {"content": [
            {"type": "text", "text": "x" * 5000}]}}]
        record = sel.build_record(long_run, EVIDENCE_PATH)
        self.assertEqual(len(record["final_message"]),
                         sel.FINAL_MESSAGE_LIMIT)
        self.assertTrue(record["final_message_truncated"])

    def test_never_emits_tool_results_queries_or_local_paths(self):
        serialized = json.dumps(self.record)
        self.assertNotIn("FETCHED-PAGE-CONTENT-NEVER-EMIT", serialized)
        self.assertNotIn("SECRET-QUERY-NEVER-EMIT", serialized)
        self.assertNotIn("/home/runner", serialized)

    def test_malformed_messages_are_skipped_not_fatal(self):
        record = sel.build_record(
            ["junk", {"type": "assistant", "message": {"content": "text"}},
             {"no": "type"}], EVIDENCE_PATH)
        self.assertEqual(record["tool_calls"], {})
        self.assertIsNone(record["final_message"])


class TestCli(unittest.TestCase):
    def run_cli(self, log_arg, output):
        return subprocess.run(
            [sys.executable, SCRIPT, "--execution-log", log_arg,
             "--evidence-path", EVIDENCE_PATH, "--output", output],
            capture_output=True, text=True)

    def test_missing_log_writes_nothing_and_exits_zero(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = os.path.join(tmp, "facts.json")
            result = self.run_cli(os.path.join(tmp, "absent.json"), output)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse(os.path.exists(output))
            self.assertEqual(self.run_cli("", output).returncode, 0)

    def test_malformed_log_writes_parse_error_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = os.path.join(tmp, "bad.json")
            with open(log, "w", encoding="utf-8") as handle:
                handle.write("{not json")
            output = os.path.join(tmp, "facts.json")
            result = self.run_cli(log, output)
            self.assertEqual(result.returncode, 0, result.stderr)
            with open(output, encoding="utf-8") as handle:
                self.assertIn("parse_error", json.load(handle))

    def test_valid_log_end_to_end(self):
        with tempfile.TemporaryDirectory() as tmp:
            log = os.path.join(tmp, "log.json")
            with open(log, "w", encoding="utf-8") as handle:
                json.dump(SAMPLE, handle)
            output = os.path.join(tmp, "facts.json")
            result = self.run_cli(log, output)
            self.assertEqual(result.returncode, 0, result.stderr)
            with open(output, encoding="utf-8") as handle:
                record = json.load(handle)
            self.assertTrue(record["evidence_artifact_written"])
