"""Tests for entry_write_guard.py and lib_dedup.py (plan 2026-11-09-001 U7b;
docs/ops/2026-11-10-dedup-miss-incident.md)."""

import json
import os
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.join(os.path.dirname(__file__), "..", "..")
sys.path.insert(0, os.path.join(REPO, "scripts", "validators"))
sys.path.insert(0, os.path.join(REPO, "scripts"))

import entry_write_guard as ewg  # noqa: E402
import lib_dedup  # noqa: E402

SCRIPT = os.path.join(REPO, "scripts", "entry_write_guard.py")
EXISTING = "2026-donno-agent2agent-authorization-propagation"
SECRET = "UNIQUE-BODY-MARKER-9141"


def entry(slug, url="https://arxiv.org/abs/2611.07050",
          ids='["arxiv:2611.07050"]'):
    return ("---\nslug: %s\ntitle: \"A title\"\nstatus: accepted\n"
            "domains: [ai_engineering]\nsource_type: academic\n"
            "source_url: %s\ncanonical_ids: %s\n"
            "publisher_or_author: \"A. Author\"\npublished: 2026-11-04\n"
            "captured: 2026-11-06\nrelevance:\n  social_science: n/a\n"
            "  ai_engineering: high\nverification: verified\n"
            "rationale: >-\n  Reason.\n---\n\n# A title\n\n## Summary\n%s\n"
            % (slug, url, ids, SECRET))


class GuardCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="radar-guard-")
        self.pristine = os.path.join(self._tmp.name, "pristine")
        self.workspace = os.path.join(self._tmp.name, "workspace")
        for root in (self.pristine, self.workspace):
            os.makedirs(os.path.join(root, "library", "entries"))
            self.put(root, EXISTING, entry(EXISTING))
        self.log = os.path.join(self._tmp.name, "guard.txt")

    def tearDown(self):
        self._tmp.cleanup()

    def put(self, root, slug, text):
        with open(os.path.join(root, "library", "entries", slug + ".md"),
                  "w", encoding="utf-8") as handle:
            handle.write(text)

    def path(self, slug):
        return os.path.join(self.workspace, "library", "entries", slug + ".md")

    def write_call(self, file_path, content, tool="Write"):
        return {"tool_name": tool, "cwd": self.workspace,
                "tool_input": {"file_path": file_path, "content": content}}

    def run_hook(self, payload):
        stdin = payload if isinstance(payload, str) else json.dumps(payload)
        return subprocess.run(
            [sys.executable, SCRIPT, "--workspace", self.workspace,
             "--pristine", self.pristine, "--log", self.log],
            input=stdin, capture_output=True, text=True)

    def log_text(self):
        if not os.path.isfile(self.log):
            return ""
        with open(self.log, encoding="utf-8") as handle:
            return handle.read()


class TestEntryWriteGuard(GuardCase):
    def test_write_over_existing_entry_blocked_2026_11_10(self):
        """Run 42819765946: the scan regenerated two existing entries."""
        result = self.run_hook(self.write_call(self.path(EXISTING),
                                               entry(EXISTING)))
        self.assertEqual(result.returncode, 2)
        self.assertIn("ENTRY_EXISTS library/entries/%s.md" % EXISTING,
                      result.stderr)
        self.assertIn("Updates", result.stderr)
        self.assertEqual(self.log_text(), "BLOCKED ENTRY_EXISTS "
                         "library/entries/%s.md\n" % EXISTING)

    def test_new_slug_same_identifier_blocked_2026_11_10(self):
        """Run 42819765946: three duplicates under new slugs."""
        result = self.run_hook(self.write_call(
            self.path("2026-donno-a2a-delegation"),
            entry("2026-donno-a2a-delegation")))
        self.assertEqual(result.returncode, 2)
        self.assertIn("ENTRY_DUPLICATE", result.stderr)
        self.assertIn("library/entries/%s.md" % EXISTING, result.stderr)
        self.assertIn("arxiv:2611.07050", result.stderr)

    def test_version_suffix_and_url_only_identifier_blocked(self):
        for url, ids in (("https://arxiv.org/abs/2611.07050v2",
                          '["arxiv:2611.07050v2"]'),
                         ("https://arxiv.org/pdf/2611.07050v3", "[]"),
                         ("http://www.arxiv.org/abs/2611.07050/", "[]")):
            result = self.run_hook(self.write_call(
                self.path("2026-other-slug"),
                entry("2026-other-slug", url, ids)))
            self.assertEqual(result.returncode, 2, (url, result.stderr))

    def test_same_url_without_identifier_blocked(self):
        self.put(self.pristine, "2026-blog", entry(
            "2026-blog", "https://example.org/post/one/", "[]"))
        result = self.run_hook(self.write_call(
            self.path("2026-blog-again"),
            entry("2026-blog-again",
                  "https://www.example.org/post/one?utm_source=x", "[]")))
        self.assertEqual(result.returncode, 2)
        self.assertIn("library/entries/2026-blog.md", result.stderr)

    def test_new_development_allowed(self):
        result = self.run_hook(self.write_call(
            self.path("2026-new-paper"),
            entry("2026-new-paper", "https://arxiv.org/abs/2611.09999",
                  '["arxiv:2611.09999"]')))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.log_text(), "")

    def test_rewrite_of_entry_created_this_run_allowed(self):
        """A new entry may be written twice in a run (e.g. by the repair)."""
        text = entry("2026-new-paper", "https://arxiv.org/abs/2611.09999",
                     '["arxiv:2611.09999"]')
        self.put(self.workspace, "2026-new-paper", text)
        result = self.run_hook(self.write_call(self.path("2026-new-paper"),
                                               text))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_duplicate_within_the_run_blocked(self):
        self.put(self.workspace, "2026-new-paper", entry(
            "2026-new-paper", "https://arxiv.org/abs/2611.09999",
            '["arxiv:2611.09999"]'))
        result = self.run_hook(self.write_call(
            self.path("2026-new-paper-b"),
            entry("2026-new-paper-b", "https://arxiv.org/abs/2611.09999",
                  '["arxiv:2611.09999"]')))
        self.assertEqual(result.returncode, 2)
        self.assertIn("library/entries/2026-new-paper.md", result.stderr)

    def test_relative_path_resolved_against_cwd(self):
        result = self.run_hook(self.write_call(
            "library/entries/%s.md" % EXISTING, entry(EXISTING)))
        self.assertEqual(result.returncode, 2)

    def test_other_paths_and_tools_ignored(self):
        report = os.path.join(self.workspace, "reports", "ai_engineering",
                              "daily", "2026-11-10.md")
        self.assertEqual(self.run_hook(
            self.write_call(report, entry(EXISTING))).returncode, 0)
        self.assertEqual(self.run_hook(self.write_call(
            self.path(EXISTING), entry(EXISTING), tool="Edit")).returncode, 0)
        nested = os.path.join(self.workspace, "library", "entries", "sub",
                              EXISTING + ".md")
        self.assertEqual(self.run_hook(
            self.write_call(nested, entry(EXISTING))).returncode, 0)

    def test_fails_open_on_its_own_errors(self):
        """A guard fault must never stop a scan; validators are the gate."""
        result = self.run_hook("not json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(self.log_text(), "GUARD_ERROR JSONDecodeError\n")
        self.assertEqual(self.run_hook({"tool_name": "Write"}).returncode, 0)
        self.assertEqual(self.run_hook(self.write_call(
            self.path("2026-x"), "no frontmatter here")).returncode, 0)

    def test_log_never_carries_written_content(self):
        self.run_hook(self.write_call(self.path("2026 bad name!"),
                                      entry("2026-dup")))
        log = self.log_text()
        self.assertTrue(log.startswith("BLOCKED ENTRY_DUPLICATE "))
        self.assertNotIn(SECRET, log)
        self.assertNotIn("bad name", log)

    def test_evaluate_returns_rule(self):
        decision = ewg.evaluate(self.write_call(self.path(EXISTING), "x"),
                                self.workspace, self.pristine)
        self.assertEqual(decision[0], "ENTRY_EXISTS")


class TestDedupKeys(unittest.TestCase):
    def test_arxiv_and_doi_from_url(self):
        self.assertEqual(lib_dedup.id_from_url(
            "https://arxiv.org/pdf/2611.07050v2.pdf"), "arxiv:2611.07050")
        self.assertEqual(lib_dedup.id_from_url(
            "https://doi.org/10.1257/JEL.20231736"), "doi:10.1257/jel.20231736")
        self.assertIsNone(lib_dedup.id_from_url("https://arxiv.org/list/cs.AI"))
        self.assertIsNone(lib_dedup.id_from_url("https://example.org/a"))

    def test_normalize_url(self):
        self.assertEqual(lib_dedup.normalize_url(
            "HTTPS://www.Example.org/a/?utm_source=x&id=3#top"),
            "example.org/a?id=3")
        self.assertEqual(lib_dedup.normalize_url(None), "")

    def test_id_keys_ignore_plain_urls(self):
        fields = {"source_url": "https://example.org/a",
                  "canonical_ids": ["DOI:10.1/X", "arxiv:2611.07050v4"]}
        self.assertEqual(lib_dedup.id_keys(fields),
                         {"doi:10.1/x", "arxiv:2611.07050"})
        self.assertIn("url:example.org/a", lib_dedup.all_keys(fields))


if __name__ == "__main__":
    unittest.main()
