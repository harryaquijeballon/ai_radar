"""Tests for scan_finish_guard.py (plan 2026-11-09-001 U7c;
docs/ops/2026-11-11-coverage-floor-incident.md)."""

import json
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.join(os.path.dirname(__file__), "..", "..")
sys.path.insert(0, os.path.join(REPO, "scripts", "validators"))
sys.path.insert(0, os.path.join(REPO, "scripts"))

import check_scan_coverage as csc  # noqa: E402
import scan_finish_guard as sfg  # noqa: E402

SCRIPT = os.path.join(REPO, "scripts", "scan_finish_guard.py")
PROFILES = os.path.join(REPO, "profiles")
SESSION = "aa312cbc-5cd4-472b-8491-4d5d3b4c5d38"
SECRET = "FETCHED-PAGE-TEXT-7733"


def source_urls(domain, count):
    """One fetchable URL for each of the first `count` fetchable sources."""
    urls = []
    for _, patterns in csc.load_watchlists(PROFILES)[domain]:
        if patterns and len(urls) < count:
            host, path = patterns[0]
            urls.append("https://%s%s" % (host, path))
    return urls


class FinishGuardCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="radar-finish-")
        self.transcript = os.path.join(self._tmp.name, "session.jsonl")
        self.log = os.path.join(self._tmp.name, "finish.txt")

    def tearDown(self):
        self._tmp.cleanup()

    def write_transcript(self, urls, extra_tool=True):
        lines = [{"type": "mode", "mode": "x"}]
        if extra_tool:
            lines.append({"type": "assistant", "message": {"content": [
                {"type": "tool_use", "id": "r0", "name": "Read",
                 "input": {"file_path": "engine/ENGINE.md"}}]}})
        for number, url in enumerate(urls):
            lines.append({"type": "assistant", "message": {"content": [
                {"type": "tool_use", "id": "f%d" % number, "name": "WebFetch",
                 "input": {"url": url, "prompt": "p"}}]}})
            lines.append({"type": "user", "message": {"content": [
                {"type": "tool_result", "tool_use_id": "f%d" % number,
                 "content": SECRET}]}})
        with open(self.transcript, "w", encoding="utf-8") as handle:
            handle.write("\n".join(json.dumps(line) for line in lines))
            handle.write("\nnot json at all\n")

    def run_hook(self, payload=None):
        if payload is None:
            payload = {"hook_event_name": "Stop", "session_id": SESSION,
                       "transcript_path": self.transcript,
                       "stop_hook_active": False}
        stdin = payload if isinstance(payload, str) else json.dumps(payload)
        return subprocess.run(
            [sys.executable, SCRIPT, "--pristine", REPO, "--log", self.log],
            input=stdin, capture_output=True, text=True)

    def log_lines(self):
        if not os.path.isfile(self.log):
            return []
        with open(self.log, encoding="utf-8") as handle:
            return handle.read().splitlines()


class TestScanFinishGuard(FinishGuardCase):
    def measured(self):
        return csc.build_record(
            csc.load_watchlists(PROFILES),
            csc.extract_fetches(sfg.load_transcript(self.transcript)))["domains"]

    def test_shallow_scan_is_sent_back_2026_11_11(self):
        """Run 43017169301 (9 of 19 and 6 of 17): social science below its
        floor of 12, AI engineering at its floor of 6. Some hosts serve
        both watchlists, so the exact counts are read from the sensor."""
        self.write_transcript(source_urls("social_science", 8)
                              + source_urls("ai_engineering", 6))
        domains = self.measured()
        ss, ae = domains["social_science"], domains["ai_engineering"]
        self.assertLess(ss["attempted"], 12)
        self.assertGreaterEqual(ae["attempted"], 6)
        result = self.run_hook()
        self.assertEqual(result.returncode, 2)
        self.assertIn("SCAN_COVERAGE_BELOW_FLOOR", result.stderr)
        self.assertIn("- social_science: %d of 19 watchlist sources attempted,"
                      " at least 12 needed. Not yet attempted: "
                      % ss["attempted"], result.stderr)
        self.assertNotIn("- ai_engineering:", result.stderr)
        self.assertEqual(len(ss["not_attempted"]), 19 - ss["attempted"])
        for name in ss["not_attempted"]:
            self.assertIn(name, result.stderr)
        self.assertEqual(self.log_lines(), [
            "BLOCKED COVERAGE %s ai_engineering=%d/17 social_science=%d/19"
            % (SESSION, ae["attempted"], ss["attempted"])])

    def test_scan_at_or_above_both_floors_may_finish(self):
        self.write_transcript(source_urls("social_science", 12)
                              + source_urls("ai_engineering", 6))
        domains = self.measured()
        result = self.run_hook()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(self.log_lines(), [
            "CHECKED %s ai_engineering=%d/17 social_science=%d/19"
            % (SESSION, domains["ai_engineering"]["attempted"],
               domains["social_science"]["attempted"])])

    def test_stop_after_reading_only_is_sent_back(self):
        """The model-bail shape: tools were used, nothing was fetched."""
        self.write_transcript([])
        result = self.run_hook()
        self.assertEqual(result.returncode, 2)
        self.assertIn("- ai_engineering: 0 of 17", result.stderr)
        self.assertIn("- social_science: 0 of 19", result.stderr)
        self.assertIn("and ", result.stderr)  # long lists are cut

    def test_gives_up_after_two_blocks_per_session(self):
        self.write_transcript(source_urls("social_science", 3))
        self.assertEqual(self.run_hook().returncode, 2)
        self.assertEqual(self.run_hook().returncode, 2)
        third = self.run_hook()
        self.assertEqual(third.returncode, 0)
        self.assertEqual(third.stderr, "")
        self.assertTrue(self.log_lines()[-1].startswith("GAVE_UP " + SESSION))
        # Another session (attempt 2) has its own budget.
        other = self.run_hook({"session_id": "other-session",
                               "transcript_path": self.transcript})
        self.assertEqual(other.returncode, 2)

    def test_fails_open(self):
        """A guard fault must never trap a run."""
        self.assertEqual(self.run_hook("not json").returncode, 0)
        self.assertEqual(self.run_hook({"session_id": SESSION}).returncode, 0)
        self.assertEqual(self.run_hook(
            {"session_id": SESSION,
             "transcript_path": self.transcript + ".absent"}).returncode, 0)
        # A transcript in which no tool call can be found is unreadable,
        # not an empty scan: never block on it.
        self.write_transcript([], extra_tool=False)
        self.assertEqual(self.run_hook().returncode, 0)
        self.assertEqual(self.log_lines(), [
            "GUARD_ERROR JSONDecodeError",
            "GUARD_ERROR TranscriptUnreadable " + SESSION,
            "GUARD_ERROR TranscriptUnreadable " + SESSION,
            "GUARD_ERROR TranscriptUnreadable " + SESSION])

    def test_log_carries_no_content_and_odd_session_id_is_replaced(self):
        self.write_transcript(source_urls("social_science", 2))
        self.run_hook({"session_id": "x y; rm -rf /",
                       "transcript_path": self.transcript})
        (line,) = self.log_lines()
        self.assertTrue(line.startswith("BLOCKED COVERAGE unknown "))
        self.assertNotIn(SECRET, line)
        self.assertNotIn("rm -rf", line)

    def test_failed_fetch_counts_as_attempted(self):
        """Same rule as the post-run gate: attempted, not succeeded."""
        urls = source_urls("social_science", 12) + source_urls("ai_engineering", 6)
        self.write_transcript(urls)
        with open(self.transcript, encoding="utf-8") as handle:
            text = handle.read().replace('"content": "%s"' % SECRET,
                                         '"content": "x", "is_error": true')
        with open(self.transcript, "w", encoding="utf-8") as handle:
            handle.write(text)
        self.assertEqual(self.run_hook().returncode, 0)

    def test_floors_are_the_post_run_gate_s(self):
        record = {"domains": {
            "social_science": {"attempted": 11, "fetchable": 19,
                               "not_attempted": ["A"]},
            "ai_engineering": {"attempted": 2, "fetchable": 3,
                               "not_attempted": ["B"]}}}
        self.assertEqual(sfg.shortfalls(record), [
            ("ai_engineering", 2, 3, 3, ["B"]),
            ("social_science", 11, 12, 19, ["A"])])
        self.assertEqual(bool(sfg.shortfalls(record)),
                         bool(csc.check_attempted_floors(record)))


if __name__ == "__main__":
    unittest.main()
