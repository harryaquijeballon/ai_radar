"""Tests for make_run_summary.py (plan U4; R37, R47, summary-side R39)."""

import datetime
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import make_run_summary as mrs  # noqa: E402

from . import repo_fixture as fix  # noqa: E402

RUN_DATE = datetime.date(2026, 7, 23)
MARKER = "71f3c9X"

POISONED_ENTRY = """---
slug: 2026-poisoned-entry
title: "Sensitive title XMARKER_{marker}"
status: provisional
domains: [social_science]
source_type: commentary
source_url: https://example.org/poisoned
canonical_ids: []
publisher_or_author: "Someone - Somewhere"
published: unknown
captured: 2026-07-23
relevance:
  social_science: medium
verification: unverified
rationale: >-
  Fixture rationale containing XMARKER_{marker} which must never reach the
  run summary.
---

# Sensitive title

## Summary

Body with XMARKER_{marker}.

## Updates

*(none yet)*
""".format(marker=MARKER)


class TestRunSummary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory(prefix="radar-u4rs-")
        cls.origin, cls.template = fix.build_template(cls._tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def build_workspace(self):
        workspace = fix.fresh_workspace(self._tmp.name, self.template)
        # New accepted entry (clean) + new provisional entry (poisoned fixture):
        clean = fix.read(workspace, fix.ACCEPTED_ENTRY).replace(
            "2023-korinek-genai-economic-research", "2026-clean-new-entry")
        fix.write(workspace, "library/entries/2026-clean-new-entry.md", clean)
        fix.write(workspace, "library/entries/2026-poisoned-entry.md",
                  POISONED_ENTRY)
        # Legitimate entry update:
        fix.write(workspace, fix.PROVISIONAL_ENTRY,
                  fix.read(workspace, fix.PROVISIONAL_ENTRY).replace(
                      "*(none yet)*",
                      "- **2026-07-23** - re-encountered; no material change."))
        # Two rejection lines:
        fix.write(workspace, fix.REJECTIONS,
                  fix.read(workspace, fix.REJECTIONS)
                  + "- 2026-07-23 - example.org/five - below bar\n"
                  + "- 2026-07-23 - example.org/six - duplicate\n")
        # New deferred record with poisoned reason; new proposal record:
        poisoned_record = fix.NEW_DEFERRED_RECORD.replace(
            "- reason: domain not on the egress allowlist",
            "- reason: sensitive context XMARKER_%s" % MARKER).replace(
            "- reason_class: access_or_license_unclear",
            "- reason_class: information_boundary_unclear")
        fix.write(workspace, fix.DEFERRED_FILE,
                  fix.read(workspace, fix.DEFERRED_FILE) + poisoned_record)
        fix.write(workspace, fix.PROPOSALS_FILE,
                  fix.read(workspace, fix.PROPOSALS_FILE)
                  + "\n### https://another.example/feed\n"
                    "- source_name: Another Outlet\n"
                    "- domain: social_science\n"
                    "- first_discovered: 2026-07-23\n"
                    "- last_encountered: 2026-07-23\n"
                    "- why_useful: relevant coverage\n"
                    "- surfaced_by: open search\n"
                    "- proposed_purpose: watchlist candidate\n"
                    "- status: pending\n")
        # Poisoned filename (counts only ever appear in the summary):
        fix.write(workspace,
                  "library/entries/2026-XMARKER_%s-name.md" % MARKER,
                  clean.replace("2026-clean-new-entry",
                                "2026-XMARKER_%s-name" % MARKER))
        return workspace

    def test_summary_counts_and_safety(self):
        workspace = self.build_workspace()
        summary = mrs.build_summary(
            workspace, "origin/main", None, RUN_DATE, "success", 1,
            "abc1234def", oauth_ready=True, artifacts_note=False)
        self.assertIn("| outcome | success |", summary)
        self.assertIn("| run status | completed |", summary)
        self.assertIn("| new accepted entries | 2 |", summary)
        self.assertIn("| new provisional entries | 1 |", summary)
        self.assertIn("| updated or merged entries | 1 |", summary)
        self.assertIn("| rejections logged | 2 |", summary)
        self.assertIn("| source proposals (pending) | 1 |", summary)
        self.assertIn("| deferred candidates | 1 |", summary)
        self.assertIn("| deferred: information_boundary_unclear | 1 |", summary)
        self.assertIn("| report items (social_science) | 0 |", summary)
        self.assertIn("reports/social_science/daily/2026-07-23.md", summary)
        self.assertIn("| commit | abc1234def |", summary)
        self.assertIn("| oauth secret ready | yes |", summary)
        # R47 / boundary rule: nothing model-authored reaches the summary.
        self.assertNotIn(MARKER, summary)
        self.assertNotIn("XMARKER", summary)
        self.assertNotIn("Sensitive", summary)
        self.assertNotIn("sensitive context", summary)

    def test_invalid_sha_renders_as_none_and_failure_notes_artifacts(self):
        workspace = self.build_workspace()
        summary = mrs.build_summary(
            workspace, "origin/main", None, RUN_DATE, "validation", 2,
            "XMARKER_%s" % MARKER, oauth_ready=False, artifacts_note=True)
        self.assertIn("| outcome | validation |", summary)
        self.assertIn("| run status | operationally incomplete |", summary)
        self.assertIn("| attempts | 2 |", summary)
        self.assertIn("| commit | none |", summary)
        self.assertIn("| oauth secret ready | no |", summary)
        self.assertIn("| diagnostics | preserved as workflow artifacts |", summary)
        self.assertNotIn(MARKER, summary)

    def test_evidence_counts_per_domain(self):
        import json
        workspace = fix.fresh_workspace(self._tmp.name, self.template)
        evidence = workspace + "-ev.json"
        with open(evidence, "w", encoding="utf-8") as handle:
            json.dump({"run_date": "2026-07-23", "domains": {
                "social_science": {"curated_sources_fetched": 7,
                                   "queries_executed": 4},
                "ai_engineering": {"curated_sources_fetched": 5,
                                   "queries_executed": 3}}}, handle)
        summary = mrs.build_summary(workspace, "origin/main", None, RUN_DATE,
                                    "no-change", 1, "", True, False,
                                    evidence_path=evidence)
        self.assertIn("| scan queries (social_science) | 4 |", summary)
        self.assertIn("| scan fetches (social_science) | 7 |", summary)
        self.assertIn("| scan queries (ai_engineering) | 3 |", summary)
        self.assertIn("| scan fetches (ai_engineering) | 5 |", summary)

    def test_missing_and_malformed_evidence_fail_closed(self):
        workspace = fix.fresh_workspace(self._tmp.name, self.template)
        for evidence in (None, workspace + "-absent.json"):
            summary = mrs.build_summary(workspace, "origin/main", None,
                                        RUN_DATE, "tooling", 1, "", True, True,
                                        evidence_path=evidence)
            self.assertIn("| scan queries (social_science) | unavailable |",
                          summary)
            self.assertIn("| scan fetches (ai_engineering) | unavailable |",
                          summary)
        broken = workspace + "-broken.json"
        with open(broken, "w", encoding="utf-8") as handle:
            handle.write("model prose, not JSON")
        summary = mrs.build_summary(workspace, "origin/main", None, RUN_DATE,
                                    "tooling", 1, "", True, True,
                                    evidence_path=broken)
        self.assertEqual(summary.count("| unavailable |"), 4)

    def test_poisoned_evidence_never_reaches_summary(self):
        import json
        workspace = fix.fresh_workspace(self._tmp.name, self.template)
        evidence = workspace + "-poison.json"
        with open(evidence, "w", encoding="utf-8") as handle:
            json.dump({"run_date": "2026-07-23",
                       "query_log": ["secret query XMARKER_%s" % MARKER],
                       "domains": {
                           "social_science": {
                               "curated_sources_fetched": "XMARKER_%s" % MARKER,
                               "queries_executed": 4,
                               "note": "XMARKER_%s" % MARKER},
                           "ai_engineering": {"curated_sources_fetched": 5,
                                              "queries_executed": 3}}}, handle)
        summary = mrs.build_summary(workspace, "origin/main", None, RUN_DATE,
                                    "no-change", 1, "", True, False,
                                    evidence_path=evidence)
        self.assertNotIn(MARKER, summary)
        self.assertNotIn("XMARKER", summary)
        # Poisoned domain fails closed; clean domain still reports:
        self.assertIn("| scan queries (social_science) | unavailable |", summary)
        self.assertIn("| scan fetches (ai_engineering) | 5 |", summary)

    def test_no_change_run_reports_zero_counts(self):
        workspace = fix.fresh_workspace(self._tmp.name, self.template)
        summary = mrs.build_summary(
            workspace, "origin/main", None, RUN_DATE, "no-change", 1, "",
            oauth_ready=True, artifacts_note=False)
        self.assertIn("| outcome | no-change |", summary)
        self.assertIn("| run status | completed |", summary)
        self.assertIn("| new accepted entries | 0 |", summary)
        self.assertIn("| deferred candidates | 0 |", summary)

    def test_cli_contract(self):
        workspace = fix.fresh_workspace(self._tmp.name, self.template)
        script = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "..", "scripts",
            "make_run_summary.py"))
        result = subprocess.run(
            [sys.executable, script, "--workspace", workspace,
             "--base", "origin/main", "--run-date", "2026-07-23",
             "--outcome", "success", "--oauth-ready", "true"],
            capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("# Radar run summary - 2026-07-23", result.stdout)


if __name__ == "__main__":
    unittest.main()
