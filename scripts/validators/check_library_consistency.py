"""Library consistency validator (plan U4; enforces schema conformance and
origin priority 4 — INDEX.md agrees with the entries it derives from).

Checks every entry's frontmatter against the frozen v1 schema (via
lib_radar.validate_entry_frontmatter), slug/filename agreement, and the
derived index: a row per entry, no stale rows, status cells matching entry
frontmatter. All rules repairable-class — the index is regenerable by design.
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Dict, List

import lib_radar
from lib_radar import REPAIRABLE, Violation, emit, register_rule

register_rule("SLUG_FILENAME_MISMATCH", REPAIRABLE,
              "entry slug does not match its filename")
register_rule("INDEX_ROW_MISSING", REPAIRABLE,
              "entry has no row in INDEX.md")
register_rule("INDEX_ROW_STALE", REPAIRABLE,
              "INDEX.md row has no matching entry file")
register_rule("INDEX_ROW_MISMATCH", REPAIRABLE,
              "INDEX.md row disagrees with entry frontmatter ({field})")
register_rule("INDEX_UNPARSEABLE", REPAIRABLE,
              "INDEX.md table could not be parsed ({reason})")


def parse_index(text: str) -> Dict[str, Dict[str, str]]:
    """slug -> {title, domains, status} from the INDEX table."""
    rows: Dict[str, Dict[str, str]] = {}
    for line in text.split("\n"):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 4 or cells[0] in ("slug", "") or set(cells[0]) <= {"-"}:
            continue
        rows[cells[0]] = {"title": cells[1], "domains": cells[2],
                          "status": cells[3]}
    return rows


def validate(workspace: str) -> List[Violation]:
    violations: List[Violation] = []
    entries: Dict[str, Dict[str, object]] = {}

    for full_path in lib_radar.iter_entry_paths(workspace):
        rel = os.path.relpath(full_path, workspace)
        with open(full_path, encoding="utf-8", errors="replace") as handle:
            text = handle.read()
        violations.extend(lib_radar.validate_entry_frontmatter(rel, text))
        fields = lib_radar.parse_frontmatter(text).fields
        slug = os.path.basename(rel)[:-3]
        if fields.get("slug") and fields["slug"] != slug:
            violations.append(emit("SLUG_FILENAME_MISMATCH", rel))
        entries[slug] = fields

    index_path = os.path.join(workspace, "library", "INDEX.md")
    if not os.path.isfile(index_path):
        violations.append(emit("INDEX_UNPARSEABLE", "library/INDEX.md",
                               reason="missing"))
        return violations
    with open(index_path, encoding="utf-8", errors="replace") as handle:
        rows = parse_index(handle.read())

    for slug, fields in sorted(entries.items()):
        row = rows.get(slug)
        if row is None:
            violations.append(emit("INDEX_ROW_MISSING",
                                   "library/entries/%s.md" % slug))
            continue
        if fields.get("status") and row["status"] != fields["status"]:
            violations.append(emit("INDEX_ROW_MISMATCH", "library/INDEX.md",
                                   field="status"))
        domains = fields.get("domains")
        if isinstance(domains, list) and row["domains"].replace(" ", "") \
                != ",".join(domains):
            violations.append(emit("INDEX_ROW_MISMATCH", "library/INDEX.md",
                                   field="domains"))
    for slug in sorted(set(rows) - set(entries)):
        violations.append(emit("INDEX_ROW_STALE", "library/INDEX.md"))
    return violations


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", default=".", help="repo root to inspect")
    args = parser.parse_args()
    return lib_radar.report(validate(args.workspace))


if __name__ == "__main__":
    sys.exit(lib_radar.run_main(main))
