"""Tests for check_repair_scope.py (plan 2026-11-09-001 U5).

Reproduces 2026-11-05 (run 42029203188): the repair pass added
`verification: partial` to entries that had none, with zero fetches.
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import check_repair_scope as crs  # noqa: E402

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SCRIPT = os.path.join(REPO, "scripts", "validators", "check_repair_scope.py")


def entry(status="accepted", verification="verified"):
    lines = ["---", "slug: 2026-example", 'title: "Example"']
    if status is not None:
        lines.append("status: %s" % status)
    if verification is not None:
        lines.append("verification: %s" % verification)
    lines += ["---", "", "# Example", ""]
    return "\n".join(lines)


def rules(violations):
    return sorted(v.rule_id for v in violations)


class TestRaised(unittest.TestCase):
    def check(self, before, after):
        return rules(crs.check_entry("library/entries/x.md", before, after))

    def test_added_partial_is_out_of_scope_2026_11_05(self):
        self.assertEqual(self.check(entry(verification=None),
                                    entry(verification="partial")),
                         ["REPAIR_RAISED_VERIFICATION"])

    def test_added_unverified_and_provisional_is_the_legal_repair(self):
        self.assertEqual(self.check(entry(verification=None),
                                    entry(status="provisional",
                                          verification="unverified")), [])

    def test_raising_verification_aborts(self):
        self.assertEqual(self.check(entry(verification="partial"),
                                    entry(verification="verified")),
                         ["REPAIR_RAISED_VERIFICATION"])

    def test_lowering_is_allowed(self):
        self.assertEqual(self.check(entry(verification="verified"),
                                    entry(status="provisional",
                                          verification="unverified")), [])

    def test_raising_status_aborts(self):
        self.assertEqual(self.check(entry(status="provisional"),
                                    entry(status="accepted")),
                         ["REPAIR_RAISED_STATUS"])
        self.assertEqual(self.check(entry(status=None), entry(status="accepted")),
                         ["REPAIR_RAISED_STATUS"])

    def test_entry_created_by_repair_must_claim_nothing(self):
        self.assertEqual(self.check(None, entry()),
                         ["REPAIR_RAISED_STATUS", "REPAIR_RAISED_VERIFICATION"])
        self.assertEqual(self.check(None, entry("provisional", "unverified")), [])

    def test_invalid_value_left_to_schema_validators(self):
        self.assertEqual(self.check(entry(verification="partial"),
                                    entry(verification="bogus")), [])


class TestCli(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.before = os.path.join(self._tmp.name, "before")
        self.workspace = os.path.join(self._tmp.name, "ws")
        self.entries = os.path.join(self.workspace, "library", "entries")
        os.makedirs(self.before)
        os.makedirs(self.entries)

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, root, name, text):
        with open(os.path.join(root, name), "w", encoding="utf-8") as handle:
            handle.write(text)

    def run_cli(self, before=None):
        return subprocess.run([sys.executable, SCRIPT, "--before",
                               before or self.before,
                               "--workspace", self.workspace],
                              capture_output=True, text=True)

    def test_unchanged_and_lowered_entries_pass(self):
        self.write(self.before, "a.md", entry())
        self.write(self.entries, "a.md", entry())
        self.write(self.before, "b.md", entry(verification=None))
        self.write(self.entries, "b.md", entry("provisional", "unverified"))
        completed = self.run_cli()
        self.assertEqual(completed.returncode, 0, completed.stdout)

    def test_raise_exits_one_without_echoing_content(self):
        self.write(self.before, "a.md", entry(verification=None))
        self.write(self.entries, "a.md", entry(verification="partial"))
        completed = self.run_cli()
        self.assertEqual(completed.returncode, 1)
        self.assertEqual(completed.stdout.strip().split(" - ")[0],
                         "ABORT REPAIR_RAISED_VERIFICATION library/entries/a.md")
        self.assertNotIn("Example", completed.stdout)

    def test_missing_snapshot_fails_closed(self):
        completed = self.run_cli(os.path.join(self._tmp.name, "absent"))
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(completed.stdout.strip(),
                         "INTERNAL VALIDATOR_ERROR - FileNotFoundError")


if __name__ == "__main__":
    unittest.main()
