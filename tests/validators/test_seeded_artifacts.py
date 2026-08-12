"""U6 guards: the real seeded queue files and egress allowlist stay valid."""

import os
import re
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import check_queue_records as cqr  # noqa: E402
import lib_queues  # noqa: E402

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

QUEUE_FILES = (
    "reviews/deferred_candidates/social_science.md",
    "reviews/deferred_candidates/ai_engineering.md",
    "reviews/source_proposals/social_science.md",
    "reviews/source_proposals/ai_engineering.md",
)

DOMAIN_RE = re.compile(r"^- ([a-z0-9.-]+\.[a-z]{2,})$")


class TestSeededQueues(unittest.TestCase):
    def test_seeded_queue_files_validate_cleanly(self):
        for rel in QUEUE_FILES:
            with open(os.path.join(REPO, rel), encoding="utf-8") as handle:
                text = handle.read()
            self.assertEqual(cqr.validate_file(rel, text), [], rel)

    EXAMPLE_URLS = ("https://example.org/some-page",
                    "https://example.org/some-tool-post",
                    "https://newoutlet.example/research",
                    "https://practitioner.example/blog")

    def test_commented_examples_never_parse_as_records(self):
        """The queues are live artifacts (real records accumulate from runs);
        the invariant is that the commented example records stay comments and
        the files always parse without errors."""
        for rel in QUEUE_FILES:
            with open(os.path.join(REPO, rel), encoding="utf-8") as handle:
                records, errors = lib_queues.parse_queue_file(handle.read())
            self.assertEqual(errors, [], rel)
            for record in records:
                self.assertNotIn(record.url, self.EXAMPLE_URLS, rel)


class TestEgressAllowlist(unittest.TestCase):
    def test_allowlist_parses_to_domains(self):
        path = os.path.join(REPO, "profiles", "egress_allowlist.md")
        domains = []
        with open(path, encoding="utf-8") as handle:
            for line in handle:
                match = DOMAIN_RE.match(line.strip())
                if match:
                    domains.append(match.group(1))
        self.assertGreater(len(domains), 20)
        self.assertIn("arxiv.org", domains)
        self.assertIn("anthropic.com", domains)
        # Exact-host matching: approved subdomains are listed individually
        # (user decision 2026-07-23; no wildcards).
        self.assertIn("nber.org", domains)
        self.assertIn("www.nber.org", domains)
        self.assertIn("cosmos-institute.org", domains)
        self.assertIn("blog.cosmos-institute.org", domains)
        self.assertFalse(any("*" in domain for domain in domains))
        self.assertEqual(len(domains), len(set(domains)), "duplicate domains")


if __name__ == "__main__":
    unittest.main()
