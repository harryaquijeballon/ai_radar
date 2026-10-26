"""Tests for check_scan_coverage.py (plan 2026-10-16-001 U12; R53, R59)."""

import json
import os
import re
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import check_scan_coverage as csc  # noqa: E402

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCRIPT = os.path.join(REPO, "scripts", "validators", "check_scan_coverage.py")

SOCIAL = """# Social-science curated sources

## Researchers

| who | type | why included | fetch hosts |
|-----|------|--------------|-------------|
| Daron Acemoglu (MIT) | academic | Lens 1. | `economics.mit.edu` |
| Anton Korinek (UVA) | academic | Lens 6. | — |

## Institutions

| source | type | why included | fetch hosts |
|--------|------|--------------|-------------|
| NBER working papers | academic | All lenses. | `nber.org`, `www.nber.org` |
| arXiv econ.GN (Economics) | academic | Preprints. | `arxiv.org/list/econ` |
| Towards Data Science | commentary | Methods. | `towardsdatascience.com` |

## Known coverage gaps

| not a watchlist | note |
|---|---|
| Ignored row | `ignored.example` |
"""

ENGINEERING = """# AI-engineering curated sources

| who | type | why included | fetch hosts |
|-----|------|--------------|-------------|
| Simon Willison | commentary | Practice. | `simonwillison.net` |
| arXiv cs.MA / cs.CL / cs.SE | academic | Preprints. | `arxiv.org/list/cs` |
| Towards Data Science | commentary | Builds. | `towardsdatascience.com` |
"""

SECRET = "TOOL-RESULT-CONTENT-NEVER-EMIT"


def fetch(call_id, url):
    return {"type": "tool_use", "id": call_id, "name": "WebFetch",
            "input": {"url": url, "prompt": "PROMPT-NEVER-EMIT"}}


def result(call_id, is_error=False):
    return {"type": "tool_result", "tool_use_id": call_id,
            "is_error": is_error, "content": SECRET}


def log(*calls_and_results):
    """Alternating assistant/user messages, one block each."""
    messages = []
    for block in calls_and_results:
        role = "assistant" if block["type"] == "tool_use" else "user"
        messages.append({"type": role, "message": {"content": [block]}})
    return messages


class CoverageBase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="radar-u12-")
        self.profiles = os.path.join(self._tmp.name, "profiles")
        for domain, text in (("social_science", SOCIAL),
                             ("ai_engineering", ENGINEERING)):
            os.makedirs(os.path.join(self.profiles, domain))
            with open(os.path.join(self.profiles, domain, "sources.md"), "w",
                      encoding="utf-8") as handle:
                handle.write(text)
        self.log_path = os.path.join(self._tmp.name, "execution.json")

    def tearDown(self):
        self._tmp.cleanup()

    def measure(self, messages):
        with open(self.log_path, "w", encoding="utf-8") as handle:
            json.dump(messages, handle)
        return csc.measure(self.profiles, self.log_path)


class TestParseSources(unittest.TestCase):
    def test_only_tables_with_fetch_hosts_are_watchlists(self):
        names = [name for name, _ in csc.parse_sources(SOCIAL)]
        self.assertEqual(names, ["Daron Acemoglu (MIT)", "Anton Korinek (UVA)",
                                 "NBER working papers",
                                 "arXiv econ.GN (Economics)",
                                 "Towards Data Science"])

    def test_patterns_split_host_and_path_prefix(self):
        sources = dict(csc.parse_sources(SOCIAL))
        self.assertEqual(sources["NBER working papers"],
                         [("nber.org", ""), ("www.nber.org", "")])
        self.assertEqual(sources["arXiv econ.GN (Economics)"],
                         [("arxiv.org", "/list/econ")])
        self.assertEqual(sources["Anton Korinek (UVA)"], [])

    def test_malformed_pattern_fails_closed(self):
        bad = SOCIAL.replace("`economics.mit.edu`", "`https://economics.mit.edu`")
        with self.assertRaises(ValueError):
            csc.parse_sources(bad)


class TestCoverageRecord(CoverageBase):
    def test_full_coverage(self):
        record = self.measure(log(
            fetch("a", "https://economics.mit.edu/people/acemoglu"), result("a"),
            fetch("b", "https://www.nber.org/papers?page=1"), result("b"),
            fetch("c", "https://arxiv.org/list/econ.GN/new"), result("c"),
            fetch("d", "https://towardsdatascience.com/latest"), result("d"),
            fetch("e", "https://simonwillison.net/"), result("e"),
            fetch("f", "https://arxiv.org/list/cs.SE/new"), result("f")))
        social = record["domains"]["social_science"]
        self.assertEqual((social["attempted"], social["fetchable"],
                          social["succeeded"]), (4, 4, 4))
        self.assertEqual(social["ratio"], 1.0)
        self.assertEqual(record["domains"]["ai_engineering"]["ratio"], 1.0)
        self.assertEqual(record["unmatched_fetches"], 0)

    def test_search_only_sources_are_outside_the_denominator(self):
        record = self.measure(log())
        social = record["domains"]["social_science"]
        self.assertEqual(social["fetchable"], 4)
        self.assertEqual(social["search_only"], ["Anton Korinek (UVA)"])
        self.assertEqual(social["attempted"], 0)
        self.assertEqual(len(social["not_attempted"]), 4)

    def test_path_prefix_required(self):
        """An arXiv abstract found via search is not a scan of the listing."""
        record = self.measure(log(
            fetch("a", "https://arxiv.org/abs/2610.01234"), result("a")))
        self.assertIn("arXiv econ.GN (Economics)",
                      record["domains"]["social_science"]["not_attempted"])
        self.assertEqual(record["unmatched_hosts"],
                         {"arxiv.org": {"fetches": 1, "failed": 0}})

    def test_host_match_is_exact(self):
        record = self.measure(log(
            fetch("a", "https://papers.nber.org.evil.example/x"), result("a"),
            fetch("b", "https://blog.simonwillison.net/"), result("b")))
        self.assertEqual(record["domains"]["social_science"]["attempted"], 0)
        self.assertEqual(record["domains"]["ai_engineering"]["attempted"], 0)
        self.assertEqual(record["unmatched_fetches"], 2)

    def test_errored_and_unanswered_fetches_count_as_attempted_not_succeeded(self):
        record = self.measure(log(
            fetch("a", "https://nber.org/"), result("a", is_error=True),
            fetch("b", "https://economics.mit.edu/")))  # session died
        social = record["domains"]["social_science"]
        self.assertEqual((social["attempted"], social["succeeded"]), (2, 0))
        self.assertEqual(sorted(social["attempted_all_failed"]),
                         ["Daron Acemoglu (MIT)", "NBER working papers"])

    def test_one_success_among_failures_counts_as_succeeded(self):
        record = self.measure(log(
            fetch("a", "https://nber.org/"), result("a", is_error=True),
            fetch("b", "https://www.nber.org/"), result("b")))
        social = record["domains"]["social_science"]
        self.assertEqual((social["attempted"], social["succeeded"]), (1, 1))

    def test_shared_host_counts_for_both_domains(self):
        record = self.measure(log(
            fetch("a", "https://towardsdatascience.com/"), result("a")))
        self.assertEqual(record["domains"]["social_science"]["attempted"], 1)
        self.assertEqual(record["domains"]["ai_engineering"]["attempted"], 1)

    def test_unmatched_hosts_tallied_and_sanitized(self):
        record = self.measure(log(
            fetch("a", "https://www.oecd.org/en/publications"),
            result("a", is_error=True),
            fetch("b", "https://www.oecd.org/x"), result("b", is_error=True),
            fetch("c", "not a url " + SECRET), result("c", is_error=True)))
        self.assertEqual(record["unmatched_hosts"]["www.oecd.org"],
                         {"fetches": 2, "failed": 2})
        self.assertEqual(record["unmatched_hosts"]["[other]"],
                         {"fetches": 1, "failed": 1})

    def test_other_tools_are_ignored(self):
        messages = log(fetch("a", "https://nber.org/"), result("a"))
        messages.insert(0, {"type": "assistant", "message": {"content": [
            {"type": "tool_use", "id": "s", "name": "WebSearch",
             "input": {"query": "economics.mit.edu"}}]}})
        record = self.measure(messages + ["junk", {"no": "type"}])
        self.assertEqual(record["web_fetches"], 1)

    def test_record_never_carries_urls_paths_prompts_or_results(self):
        record = self.measure(log(
            fetch("a", "https://www.nber.org/papers/w99999?q=SECRETQUERY"),
            result("a"),
            fetch("b", "https://unlisted.example/SECRETPATH"), result("b")))
        serialized = json.dumps(record)
        for marker in (SECRET, "SECRETQUERY", "SECRETPATH", "PROMPT-NEVER-EMIT",
                       "https://", "/papers"):
            self.assertNotIn(marker, serialized)


class TestFloors(CoverageBase):
    def test_below_floor_aborts(self):
        record = self.measure(log(fetch("a", "https://nber.org/"), result("a")))
        violations = csc.check_floors(record, {"social_science": 0.5,
                                               "ai_engineering": 0.0})
        self.assertEqual([v.rule_id for v in violations], ["COVERAGE_BELOW_FLOOR"])
        self.assertEqual(violations[0].klass, "abort")
        self.assertIn("1 of 4", violations[0].format())

    def test_at_floor_passes(self):
        record = self.measure(log(
            fetch("a", "https://nber.org/"), result("a"),
            fetch("b", "https://economics.mit.edu/"), result("b")))
        self.assertEqual(csc.check_floors(record, {"social_science": 0.5}), [])

    def test_missing_log_aborts_when_enforcing(self):
        violations = csc.check_floors(None, {"social_science": 0.36})
        self.assertEqual([v.rule_id for v in violations], ["COVERAGE_LOG_MISSING"])


class TestCli(CoverageBase):
    def run_cli(self, *extra):
        return subprocess.run(
            [sys.executable, SCRIPT, "--profiles-root", self.profiles,
             "--execution-log", self.log_path] + list(extra),
            capture_output=True, text=True)

    def write_log(self, messages):
        with open(self.log_path, "w", encoding="utf-8") as handle:
            json.dump(messages, handle)

    def test_report_only_writes_record_and_passes(self):
        self.write_log(log(fetch("a", "https://nber.org/"), result("a")))
        out = os.path.join(self._tmp.name, "coverage.json")
        completed = self.run_cli("--report-out", out)
        self.assertEqual(completed.returncode, 0, completed.stdout)
        with open(out, encoding="utf-8") as handle:
            self.assertEqual(
                json.load(handle)["domains"]["social_science"]["attempted"], 1)

    def test_missing_log_report_only_passes_without_record(self):
        out = os.path.join(self._tmp.name, "coverage.json")
        self.assertEqual(self.run_cli("--report-out", out).returncode, 0)
        self.assertFalse(os.path.exists(out))

    def test_enforcing_below_floor_exits_one(self):
        self.write_log(log())
        completed = self.run_cli("--min-ratio", "social_science=0.36")
        self.assertEqual(completed.returncode, 1)
        self.assertTrue(completed.stdout.startswith(
            "ABORT COVERAGE_BELOW_FLOOR scan-coverage"))

    def test_bad_floor_is_rejected(self):
        self.write_log(log())
        self.assertNotEqual(self.run_cli("--min-ratio", "economics=0.5").returncode, 0)
        self.assertNotEqual(self.run_cli("--min-ratio", "social_science=7").returncode, 0)

    def test_malformed_profile_is_internal_error(self):
        with open(os.path.join(self.profiles, "social_science", "sources.md"),
                  "a", encoding="utf-8") as handle:
            handle.write("\n| who | type | why | fetch hosts |\n|---|---|---|---|\n"
                         "| X | academic | y | `bad host!` |\n")
        self.write_log(log())
        completed = self.run_cli()
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(completed.stdout.strip(),
                         "INTERNAL VALIDATOR_ERROR - ValueError")


class TestRealWatchlists(unittest.TestCase):
    """The committed profiles stay machine-readable and consistent with the
    egress allowlist: a host the run may not fetch can never be covered."""

    def setUp(self):
        self.watchlists = csc.load_watchlists(os.path.join(REPO, "profiles"))
        with open(os.path.join(REPO, "profiles", "egress_allowlist.md"),
                  encoding="utf-8") as handle:
            self.allowlist = {line[2:].strip() for line in handle
                              if line.startswith("- ")}

    def test_every_table_in_sources_is_a_watchlist(self):
        """A new table without the fetch-hosts column would silently drop
        out of the coverage denominator."""
        for domain in self.watchlists:
            with open(os.path.join(REPO, "profiles", domain, "sources.md"),
                      encoding="utf-8") as handle:
                text = handle.read()
            headers = re.findall(r"^\|[^\n]*\|\n\|[-| :]+\|$", text, re.MULTILINE)
            self.assertTrue(headers)
            for header in headers:
                self.assertTrue(header.split("\n")[0].rstrip(" |")
                                .endswith(csc.HOSTS_HEADER), (domain, header))

    def test_every_pattern_host_is_allowlisted(self):
        for domain, sources in self.watchlists.items():
            for name, patterns in sources:
                for host, _ in patterns:
                    self.assertIn(host, self.allowlist, (domain, name))

    def test_each_domain_has_fetchable_sources(self):
        for sources in self.watchlists.values():
            self.assertGreater(sum(1 for _, patterns in sources if patterns), 10)


if __name__ == "__main__":
    unittest.main()
