"""Tests for check_scan_evidence.py (plan U4; R39)."""

import datetime
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "scripts", "validators"))

import check_scan_evidence as cse  # noqa: E402

RUN_DATE = datetime.date(2026, 7, 23)

VALID = {
    "run_date": "2026-07-23",
    "domains": {
        "social_science": {"curated_sources_fetched": 12, "queries_executed": 5},
        "ai_engineering": {"curated_sources_fetched": 9, "queries_executed": 4},
    },
}


class TestScanEvidence(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory(prefix="radar-u4se-")
        self.path = os.path.join(self._tmp.name, "scan-evidence.json")

    def tearDown(self):
        self._tmp.cleanup()

    def write(self, data):
        with open(self.path, "w", encoding="utf-8") as handle:
            if isinstance(data, str):
                handle.write(data)
            else:
                json.dump(data, handle)

    def rules(self, violations):
        return sorted(violation.rule_id for violation in violations)

    def test_valid_artifact_passes(self):
        self.write(VALID)
        self.assertEqual(cse.validate(self.path, RUN_DATE), [])

    def test_absent_artifact_aborts(self):
        violations = cse.validate(self.path, RUN_DATE)
        self.assertEqual(self.rules(violations), ["EVIDENCE_MISSING"])
        self.assertEqual(violations[0].klass, "abort")

    def test_non_json_aborts(self):
        self.write("model wrote prose here instead of JSON")
        self.assertEqual(self.rules(cse.validate(self.path, RUN_DATE)),
                         ["EVIDENCE_MALFORMED"])

    def test_date_mismatch_aborts(self):
        data = dict(VALID, run_date="2026-07-22")
        self.write(data)
        self.assertEqual(self.rules(cse.validate(self.path, RUN_DATE)),
                         ["EVIDENCE_DATE_MISMATCH"])

    def test_missing_domain_aborts(self):
        data = {"run_date": "2026-07-23",
                "domains": {"social_science": VALID["domains"]["social_science"]}}
        self.write(data)
        self.assertEqual(self.rules(cse.validate(self.path, RUN_DATE)),
                         ["EVIDENCE_DOMAIN_MISSING"])

    def test_zero_activity_aborts(self):
        data = json.loads(json.dumps(VALID))
        data["domains"]["ai_engineering"] = {"curated_sources_fetched": 0,
                                             "queries_executed": 0}
        self.write(data)
        violations = cse.validate(self.path, RUN_DATE)
        self.assertEqual(self.rules(violations), ["EVIDENCE_NO_ACTIVITY"])
        self.assertIn("ai_engineering", violations[0].message)

    def test_partial_activity_passes(self):
        data = json.loads(json.dumps(VALID))
        data["domains"]["ai_engineering"] = {"curated_sources_fetched": 3,
                                             "queries_executed": 0}
        self.write(data)
        self.assertEqual(cse.validate(self.path, RUN_DATE), [])

    def test_bad_count_types_abort(self):
        for bad in ({"curated_sources_fetched": "12", "queries_executed": 5},
                    {"curated_sources_fetched": -1, "queries_executed": 5},
                    {"curated_sources_fetched": True, "queries_executed": 5},
                    {"queries_executed": 5}):
            data = json.loads(json.dumps(VALID))
            data["domains"]["social_science"] = bad
            self.write(data)
            self.assertEqual(self.rules(cse.validate(self.path, RUN_DATE)),
                             ["EVIDENCE_MALFORMED"], repr(bad))


if __name__ == "__main__":
    unittest.main()
