"""Tests for check_clean_base.py (plan U3; R24/R29)."""

import io
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import check_clean_base as ccb  # noqa: E402
import lib_radar  # noqa: E402

from . import repo_fixture as fix  # noqa: E402

MARKER = "71f3c9X"


class CleanBaseBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory(prefix="radar-u3cb-")
        cls.origin, cls.template = fix.build_template(cls._tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def workspace(self):
        return fix.fresh_workspace(self._tmp.name, self.template)

    def rules(self, violations):
        return sorted(violation.rule_id for violation in violations)


class TestCleanBase(CleanBaseBase):
    def test_clean_synced_repo_passes(self):
        self.assertEqual(ccb.validate(self.workspace()), [])

    def test_dirty_tree_aborts_and_lists_files(self):
        workspace = self.workspace()
        fix.write(workspace, "notes-in-progress.md", "uncommitted human work\n")
        violations = ccb.validate(workspace)
        self.assertEqual(self.rules(violations), ["DIRTY_TREE"])
        self.assertEqual(violations[0].klass, lib_radar.ABORT)
        self.assertIn("notes-in-progress.md", violations[0].path)

    def test_dirty_tracked_file_aborts(self):
        workspace = self.workspace()
        fix.write(workspace, "engine/ENGINE.md", "# local edit\n")
        self.assertEqual(self.rules(ccb.validate(workspace)), ["DIRTY_TREE"])

    def test_content_shaped_dirty_filename_is_redacted(self):
        workspace = self.workspace()
        fix.write(workspace, "XMARKER dirty note %s.md" % MARKER, "x\n")
        violations = ccb.validate(workspace)
        self.assertEqual(self.rules(violations), ["DIRTY_TREE"])
        stream = io.StringIO()
        lib_radar.report(violations, stream=stream)
        output = stream.getvalue()
        self.assertNotIn(MARKER, output)
        self.assertIn("[redacted-", output)

    def test_ahead_only_passes(self):
        workspace = self.workspace()
        fix.write(workspace, "library/INDEX.md", "# Library Index\n\n| a | b |\n")
        fix.commit_all(workspace, "local work")
        self.assertEqual(ccb.validate(workspace), [])

    def test_behind_only_passes(self):
        workspace = self.workspace()
        fix.write(self.origin, "library/rejections.md",
                  fix.REJECTIONS_BASE + "- 2026-07-23 - example.org/four - x\n")
        fix.commit_all(self.origin, "remote advance")
        fix.fetch(workspace)
        self.assertEqual(ccb.validate(workspace), [])

    def test_diverged_history_aborts(self):
        workspace = self.workspace()
        fix.write(workspace, "library/INDEX.md", "# Library Index\n\n| c | d |\n")
        fix.commit_all(workspace, "local commit")
        fix.write(self.origin, "reviews/source_proposals/social_science.md",
                  "# Source proposals - social_science\n\n- new proposal\n")
        fix.commit_all(self.origin, "remote commit")
        fix.fetch(workspace)
        violations = ccb.validate(workspace)
        self.assertEqual(self.rules(violations), ["NOT_FAST_FORWARD"])
        self.assertIn("ahead", violations[0].message)

    def test_missing_upstream_aborts(self):
        standalone = os.path.join(self._tmp.name, "standalone")
        os.makedirs(standalone)
        subprocess.run(["git", "init", "-q", standalone],
                       check=True, capture_output=True)
        fix.write(standalone, "file.md", "x\n")
        fix.commit_all(standalone, "only commit")
        self.assertEqual(self.rules(ccb.validate(standalone)),
                         ["UPSTREAM_MISSING"])

    def test_cli_exit_codes(self):
        script = os.path.abspath(os.path.join(
            os.path.dirname(__file__), "..", "..",
            "scripts", "validators", "check_clean_base.py"))
        clean = subprocess.run([sys.executable, script, "--repo",
                                self.workspace()], capture_output=True, text=True)
        self.assertEqual(clean.returncode, lib_radar.EXIT_PASS)
        workspace = self.workspace()
        fix.write(workspace, "dirty.md", "x\n")
        dirty = subprocess.run([sys.executable, script, "--repo", workspace],
                               capture_output=True, text=True)
        self.assertEqual(dirty.returncode, lib_radar.EXIT_VIOLATIONS)
        self.assertIn("ABORT DIRTY_TREE", dirty.stdout)
        broken = subprocess.run([sys.executable, script, "--repo",
                                 self._tmp.name], capture_output=True, text=True)
        self.assertEqual(broken.returncode, lib_radar.EXIT_INTERNAL)


if __name__ == "__main__":
    unittest.main()
