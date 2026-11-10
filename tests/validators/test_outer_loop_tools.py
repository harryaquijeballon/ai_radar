"""Tests for make_queue_triage.py, make_weekly_digest.py and the reminder
workflow (plan 2026-11-09-001 U10, U11)."""

import datetime
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.join(os.path.dirname(__file__), "..", "..")
sys.path.insert(0, os.path.join(REPO, "scripts", "validators"))
sys.path.insert(0, os.path.join(REPO, "scripts"))

import make_queue_triage as mqt  # noqa: E402
import make_weekly_digest as mwd  # noqa: E402

TODAY = datetime.date(2026, 11, 17)


def record(url, status="pending", action="locate public artifact",
           first="2026-10-01"):
    return ("### %s\n- title: T | with pipe\n- domain: social_science\n"
            "- first_encountered: %s\n- last_encountered: 2026-11-09\n"
            "- reason_class: verification_insufficient\n- reason: short\n"
            "- surfaced_by: watchlist:x\n- action_needed: %s\n- status: %s\n\n"
            % (url, first, action, status))


class OuterLoopCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="radar-outer-")
        self.ws = self._tmp.name
        self.write("reviews/deferred_candidates/social_science.md",
                   "# Deferred\n\n"
                   + record("https://example.org/roomy")
                   + record("https://example.org/at-cap", action="x" * 240,
                            first="2026-09-01")
                   + record("https://example.org/near", action="x" * 230)
                   + record("https://example.org/done", status="rejected",
                            action="x" * 240))

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, rel, text):
        path = os.path.join(self.ws, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)

    def git(self, *args):
        subprocess.run(["git", "-C", self.ws, "-c", "user.name=t",
                        "-c", "user.email=t@example.org"] + list(args),
                       check=True, capture_output=True)


class TestQueueTriage(OuterLoopCase):
    def test_pending_only_ordered_by_headroom(self):
        rows = mqt.pending_records(self.ws)
        self.assertEqual(len(rows), 3)
        sheet = mqt.build_sheet(self.ws, TODAY)
        self.assertIn("**3 pending records**; **2 within 15 characters", sheet)
        order = [sheet.index(name) for name in
                 ("example.org/at-cap", "example.org/near", "example.org/roomy")]
        self.assertEqual(order, sorted(order))
        self.assertIn("| 1 | 0 **at cap** | 77 |", sheet)
        self.assertNotIn("example.org/done", sheet)
        self.assertIn("T \\| with pipe", sheet)

    def test_real_queue_files_parse(self):
        sheet = mqt.build_sheet(REPO, TODAY)
        self.assertIn("# Review-queue triage sheet - 2026-11-17", sheet)


class TestWeeklyDigest(OuterLoopCase):
    def setUp(self):
        super().setUp()
        self.git("init", "-q")
        for day, trailers in (("2026-11-10", ""),
                              ("2026-11-12", "\n\nRadar-Scan-Turns: 120\n"
                                             "Radar-Scan-Cost-USD: 3.50"),
                              ("2026-11-13", "\n\nRadar-Scan-Turns: 140\n"
                                             "Radar-Scan-Cost-USD: 4.25")):
            self.git("commit", "-q", "--allow-empty", "-m",
                     "radar: daily run %s%s" % (day, trailers))
        self.write("docs/ops/2026-11-11-some-incident.md", "x")
        self.write("docs/ops/2026-11-14-queue-triage-sheet.md", "x")
        self.write("docs/hdai/2026-11-09_handover_003_delta.md", "x")
        self.write("docs/hdai/README.md", "x")

    def test_digest_and_due(self):
        digest, due = mwd.build_digest(self.ws, TODAY)
        self.assertTrue(due)
        self.assertIn("`docs/hdai/2026-11-09_handover_003_delta.md`, "
                      "8 days old", digest)
        self.assertIn("| days delivered | 3 of 7 |", digest)
        self.assertIn("| days without a delivered run | 2026-11-11, "
                      "2026-11-14, 2026-11-15, 2026-11-16 |", digest)
        self.assertIn("| scan turns (median) | 130 over 2 runs |", digest)
        self.assertIn("| scan cost (total, USD) | 7.75 over 2 runs |", digest)
        self.assertIn("| review queue, pending | 3 |", digest)
        self.assertIn("(handover 004)", digest)
        self.assertIn("- [x] 2026-11-11 had no delivered run: write-up "
                      "`docs/ops/2026-11-11-some-incident.md`", digest)
        # A dated document that is not an incident record is no write-up.
        self.assertIn("- [ ] 2026-11-14 had no delivered run: no write-up",
                      digest)

    def test_not_due_within_a_week(self):
        self.write("docs/hdai/2026-11-14_handover_004_delta.md", "x")
        digest, due = mwd.build_digest(self.ws, TODAY)
        self.assertFalse(due)
        self.assertIn("| handover due | no |", digest)
        self.assertNotIn("Write the weekly HDAI delta handover", digest)

    def test_cli_writes_due_output(self):
        out = os.path.join(self.ws, "out.txt")
        result = subprocess.run(
            [sys.executable, os.path.join(REPO, "scripts",
                                          "make_weekly_digest.py"),
             "--workspace", self.ws, "--today", "2026-11-17",
             "--github-output", out], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        with open(out, encoding="utf-8") as handle:
            self.assertEqual(handle.read(), "due=true\n")


class TestReminderWorkflow(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(REPO, ".github", "workflows",
                               "handover-reminder.yml"),
                  encoding="utf-8") as handle:
            self.text = handle.read()

    def test_least_privilege_no_model_no_secrets(self):
        self.assertIn("permissions:\n  contents: read\n  issues: write\n",
                      self.text)
        self.assertNotIn("contents: write", self.text)
        self.assertNotIn("secrets.", self.text)
        self.assertNotIn("claude-code-action", self.text)
        self.assertIn("persist-credentials: false", self.text)
        self.assertIn("runs-on: ubuntu-26.04", self.text)

    def test_posts_only_when_due_and_reuses_open_issue(self):
        post = self.text.split("Post the reminder")[1]
        self.assertIn("if: steps.digest.outputs.due == 'true'", post)
        self.assertIn("gh issue comment", post)
        self.assertIn('--assignee "$GITHUB_REPOSITORY_OWNER"', post)


if __name__ == "__main__":
    unittest.main()
