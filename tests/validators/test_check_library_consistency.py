"""Tests for check_library_consistency.py (plan U4)."""

import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import check_library_consistency as clc  # noqa: E402

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures", "entries")

INDEX_OK = (
    "# Library Index\n\n"
    "| slug | title | domains | status | canonical ids / URL |\n"
    "|------|-------|---------|--------|---------------------|\n"
    "| 2023-korinek-genai-economic-research | Generative AI for Economic Research"
    " | social_science | accepted | doi:10.1257/jel.20231736 |\n"
    "| 2026-imas-ai-productivity-paradox | What is the impact of AI on productivity?"
    " | social_science | provisional | aleximas.substack.com |\n"
)


class TestLibraryConsistency(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="radar-u4lc-")
        self.workspace = self._tmp.name
        entries = os.path.join(self.workspace, "library", "entries")
        os.makedirs(entries)
        for name in ("2023-korinek-genai-economic-research.md",
                     "2026-imas-ai-productivity-paradox.md"):
            shutil.copy(os.path.join(FIXTURES, name), entries)
        self.write_index(INDEX_OK)

    def tearDown(self):
        self._tmp.cleanup()

    def write_index(self, text):
        with open(os.path.join(self.workspace, "library", "INDEX.md"),
                  "w", encoding="utf-8") as handle:
            handle.write(text)

    def rules(self, violations):
        return sorted(violation.rule_id for violation in violations)

    def test_consistent_library_passes(self):
        self.assertEqual(clc.validate(self.workspace), [])

    def test_missing_index_row(self):
        self.write_index(INDEX_OK.replace(
            "| 2026-imas-ai-productivity-paradox | What is the impact of AI on "
            "productivity? | social_science | provisional | aleximas.substack.com |\n",
            ""))
        self.assertEqual(self.rules(clc.validate(self.workspace)),
                         ["INDEX_ROW_MISSING"])

    def test_stale_index_row(self):
        self.write_index(INDEX_OK
                         + "| 2020-ghost-entry | Ghost | social_science "
                           "| accepted | none |\n")
        self.assertEqual(self.rules(clc.validate(self.workspace)),
                         ["INDEX_ROW_STALE"])

    def test_status_mismatch(self):
        self.write_index(INDEX_OK.replace("| provisional |", "| accepted |"))
        violations = clc.validate(self.workspace)
        self.assertEqual(self.rules(violations), ["INDEX_ROW_MISMATCH"])
        self.assertIn("status", violations[0].message)

    def test_slug_filename_mismatch(self):
        source = os.path.join(self.workspace, "library", "entries",
                              "2026-imas-ai-productivity-paradox.md")
        renamed = os.path.join(self.workspace, "library", "entries",
                               "2026-renamed-file.md")
        os.rename(source, renamed)
        rules = self.rules(clc.validate(self.workspace))
        self.assertIn("SLUG_FILENAME_MISMATCH", rules)
        self.assertIn("INDEX_ROW_MISSING", rules)  # renamed file has no row
        self.assertIn("INDEX_ROW_STALE", rules)    # old row now points nowhere

    def test_invalid_entry_status_flagged_via_schema(self):
        path = os.path.join(self.workspace, "library", "entries",
                            "2023-korinek-genai-economic-research.md")
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text.replace("status: accepted", "status: banana"))
        rules = self.rules(clc.validate(self.workspace))
        self.assertIn("FIELD_INVALID", rules)
        self.assertIn("INDEX_ROW_MISMATCH", rules)

    def test_missing_index_fails_visibly(self):
        os.remove(os.path.join(self.workspace, "library", "INDEX.md"))
        self.assertEqual(self.rules(clc.validate(self.workspace)),
                         ["INDEX_UNPARSEABLE"])


    def test_duplicate_identifier_aborts_2026_11_10(self):
        """Plan 2026-11-09-001 U7b: run 42819765946 wrote three duplicates
        of archived papers under new slugs; nothing flagged them."""
        entries = os.path.join(self.workspace, "library", "entries")
        with open(os.path.join(entries, "2023-korinek-genai-economic-research.md"),
                  encoding="utf-8") as handle:
            text = handle.read()
        dup = "2023-korinek-llms-for-economists"
        with open(os.path.join(entries, dup + ".md"), "w",
                  encoding="utf-8") as handle:
            handle.write(text.replace(
                "slug: 2023-korinek-genai-economic-research", "slug: " + dup))
        self.write_index(INDEX_OK + "| %s | T | social_science | accepted "
                         "| doi:10.1257/jel.20231736 |\n" % dup)
        found = [v for v in clc.validate(self.workspace)
                 if v.rule_id == "ENTRY_DUPLICATE_IDENTIFIER"]
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].klass, clc.ABORT)
        self.assertEqual(found[0].path, "library/entries/%s.md" % dup)
        self.assertIn("2023-korinek-genai-economic-research", found[0].message)


if __name__ == "__main__":
    unittest.main()
