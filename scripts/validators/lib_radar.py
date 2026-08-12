"""Shared library for ai_radar deterministic validators.

Contract (see README.md; plan R42/R47):
- Exit codes: 0 = pass, 1 = violations found, 2 = internal error (fail closed).
- Violations are classified 'abort' or 'repairable'.
- No-echo rule (R47): violation output names file, line, and rule only.
  This module exposes no API for placing file content into a message;
  free slots are sanitized and replaced with a redaction indicator when
  they look like content rather than a short identifier.

Python 3.9+ standard library only.
"""

from __future__ import annotations

import datetime
import re
import sys
from typing import Callable, Dict, Iterator, List, Optional, Tuple
from zoneinfo import ZoneInfo

# --- Exit-code contract ------------------------------------------------------

EXIT_PASS = 0
EXIT_VIOLATIONS = 1
EXIT_INTERNAL = 2

# --- Path permission data (plan R22/R23; single source of truth) -------------

AUTONOMOUS_FILE_ALLOWLIST = (
    "library/INDEX.md",
    "library/rejections.md",
)

AUTONOMOUS_DIR_ALLOWLIST = (
    "library/entries/",
    "reports/social_science/daily/",
    "reports/ai_engineering/daily/",
    "reviews/source_proposals/",
    "reviews/deferred_candidates/",
)

DOMAINS = ("social_science", "ai_engineering")

# --- Entry schema as data (engine/schema.md, frozen v1) ----------------------

REQUIRED_ENTRY_FIELDS = (
    "slug",
    "title",
    "status",
    "domains",
    "source_type",
    "source_url",
    "canonical_ids",
    "publisher_or_author",
    "published",
    "captured",
    "relevance",
    "verification",
    "rationale",
)
OPTIONAL_ENTRY_FIELDS = ("license",)

ENTRY_STATUS_VALUES = ("accepted", "provisional")
SOURCE_TYPE_VALUES = ("primary", "academic", "commentary")
VERIFICATION_VALUES = ("verified", "partial", "unverified")
RELEVANCE_TIERS = ("high", "medium", "low", "n/a")

# --- Europe/London date discipline (plan R44) --------------------------------

LONDON = ZoneInfo("Europe/London")


def london_now(now_utc: Optional[datetime.datetime] = None) -> datetime.datetime:
    """Current time in Europe/London. `now_utc` (aware, UTC) is injectable
    for tests; naive input is rejected (fail closed)."""
    if now_utc is None:
        now_utc = datetime.datetime.now(datetime.timezone.utc)
    if now_utc.tzinfo is None:
        raise ValueError("london_now requires an aware datetime")
    return now_utc.astimezone(LONDON)


def london_today(now_utc: Optional[datetime.datetime] = None) -> datetime.date:
    """Today's date in Europe/London — the only 'today' any validator uses."""
    return london_now(now_utc).date()


ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_iso_date(value: str) -> Optional[datetime.date]:
    """YYYY-MM-DD to date, or None when not a full ISO date (e.g. '2023-12',
    'unknown' — both legal in entry frontmatter, never legal in report names)."""
    if not ISO_DATE_RE.match(value or ""):
        return None
    try:
        return datetime.date.fromisoformat(value)
    except ValueError:
        return None


# --- Violations and the no-echo formatter (plan R47) -------------------------

REDACTED = "[content redacted]"

# Slot values must look like short identifiers (field names, rule names,
# counts, slugs, domains) — never prose or file content.
_SAFE_SLOT_RE = re.compile(r"^[A-Za-z0-9 _.,:/@()\[\]'-]{1,80}$")

# Path segments are model-chosen (filenames can embed content). Segments
# outside the slug charset are replaced with a redaction marker plus a short
# digest so the human reviewer can still locate the file deterministically.
_SAFE_SEGMENT_RE = re.compile(r"^[A-Za-z0-9._-]{1,120}$")


def safe_path(path: str) -> str:
    import hashlib
    segments = []
    for segment in str(path).split("/"):
        if segment == "" or _SAFE_SEGMENT_RE.match(segment):
            segments.append(segment)
        else:
            digest = hashlib.sha256(segment.encode("utf-8", "replace")).hexdigest()[:8]
            segments.append("[redacted-%s]" % digest)
    return "/".join(segments)

ABORT = "abort"
REPAIRABLE = "repairable"
_CLASSES = (ABORT, REPAIRABLE)

# rule_id -> (klass, message template). Templates use {slot} placeholders;
# every slot is sanitized. Validators register their own rules at import.
_RULES: Dict[str, Tuple[str, str]] = {}


def register_rule(rule_id: str, klass: str, template: str) -> None:
    if klass not in _CLASSES:
        raise ValueError("unknown violation class: %r" % (klass,))
    if not re.match(r"^[A-Z0-9_]{3,40}$", rule_id):
        raise ValueError("rule ids are UPPER_SNAKE: %r" % (rule_id,))
    if rule_id in _RULES and _RULES[rule_id] != (klass, template):
        raise ValueError("rule %s already registered differently" % rule_id)
    _RULES[rule_id] = (klass, template)


def _sanitize(value: object) -> str:
    text = str(value)
    if "\n" in text or "\r" in text or not _SAFE_SLOT_RE.match(text):
        return REDACTED
    return text


class Violation:
    __slots__ = ("rule_id", "klass", "path", "line", "message")

    def __init__(self, rule_id: str, path: str, line: Optional[int], message: str):
        self.rule_id = rule_id
        self.klass = _RULES[rule_id][0]
        self.path = safe_path(path)
        self.line = line
        self.message = message

    def format(self) -> str:
        where = "%s:%d" % (self.path, self.line) if self.line else self.path
        return "%s %s %s - %s" % (self.klass.upper(), self.rule_id, where, self.message)


def emit(rule_id: str, path: str, line: Optional[int] = None, **slots: object) -> Violation:
    """Build a Violation. Unknown rule ids raise (fail closed). Slot values are
    sanitized; there is deliberately no positional free-text parameter."""
    if rule_id not in _RULES:
        raise KeyError("unregistered rule id: %r" % (rule_id,))
    template = _RULES[rule_id][1]
    safe = {key: _sanitize(value) for key, value in slots.items()}
    try:
        message = template.format(**safe)
    except (KeyError, IndexError):
        message = template
    return Violation(rule_id, path, line, message)


def report(violations: List[Violation], stream=None) -> int:
    """Print violations one per line and return the contract exit code."""
    stream = stream or sys.stdout
    for violation in violations:
        print(violation.format(), file=stream)
    return EXIT_VIOLATIONS if violations else EXIT_PASS


def run_main(main: Callable[[], int], stream=None) -> int:
    """Wrapper for validator __main__: any uncaught exception is an internal
    error -> exit 2, printing only the exception class name (no-echo)."""
    stream = stream or sys.stdout
    try:
        return main()
    except SystemExit:
        raise
    except BaseException as error:  # noqa: BLE001 - fail closed on everything
        print("INTERNAL VALIDATOR_ERROR - %s" % type(error).__name__, file=stream)
        return EXIT_INTERNAL


# --- Framework rules ---------------------------------------------------------

register_rule("FRONTMATTER_MALFORMED", REPAIRABLE,
              "frontmatter could not be parsed ({reason})")
register_rule("FIELD_MISSING", REPAIRABLE,
              "required frontmatter field {field} is missing")
register_rule("FIELD_INVALID", REPAIRABLE,
              "frontmatter field {field} has a value outside the schema")


# --- Frontmatter parsing (the exact v1 subset; fail closed beyond it) --------

class Frontmatter:
    __slots__ = ("fields", "body_start", "errors")

    def __init__(self, fields: Dict[str, object], body_start: int,
                 errors: List[Tuple[int, str]]):
        self.fields = fields
        self.body_start = body_start  # 1-based line number of first body line
        self.errors = errors          # (line, short reason-code) pairs


_SCALAR_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$")
_NESTED_RE = re.compile(r"^  ([A-Za-z_][A-Za-z0-9_]*):\s*(\S.*)$")


def _unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def _parse_inline_list(value: str) -> Optional[List[str]]:
    inner = value.strip()[1:-1].strip()
    if inner == "":
        return []
    return [_unquote(part.strip()) for part in inner.split(",")]


def parse_frontmatter(text: str) -> Frontmatter:
    """Parse the v1 entry frontmatter subset: scalars (optionally quoted),
    inline lists, one level of nested mapping, and folded scalars (>- / >).
    Anything else is recorded as an error, never guessed at."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return Frontmatter({}, 1, [(1, "no-frontmatter-delimiter")])

    fields: Dict[str, object] = {}
    errors: List[Tuple[int, str]] = []
    index = 1
    while index < len(lines):
        line = lines[index]
        if line.strip() == "---":
            return Frontmatter(fields, index + 2, errors)
        if line.strip() == "":
            index += 1
            continue
        match = _SCALAR_RE.match(line)
        if not match:
            errors.append((index + 1, "unparseable-line"))
            index += 1
            continue
        key, raw = match.group(1), match.group(2).strip()
        if raw.startswith("[") and raw.endswith("]"):
            parsed = _parse_inline_list(raw)
            if parsed is None:
                errors.append((index + 1, "bad-inline-list"))
            else:
                fields[key] = parsed
            index += 1
        elif raw in (">-", ">", "|-", "|"):
            block: List[str] = []
            index += 1
            while index < len(lines) and (lines[index].startswith("  ")
                                          or lines[index].strip() == ""):
                if lines[index].strip() == "---":
                    break
                block.append(lines[index].strip())
                index += 1
            fields[key] = " ".join(part for part in block if part)
        elif raw == "":
            nested: Dict[str, str] = {}
            index += 1
            while index < len(lines):
                sub = _NESTED_RE.match(lines[index])
                if not sub:
                    break
                nested[sub.group(1)] = _unquote(sub.group(2).strip())
                index += 1
            if nested:
                fields[key] = nested
            else:
                errors.append((index, "empty-mapping"))
        else:
            fields[key] = _unquote(raw)
            index += 1
    return Frontmatter(fields, len(lines) + 1, errors + [(len(lines), "unterminated-frontmatter")])


# --- Entry frontmatter validation (schema as data) ---------------------------

def validate_entry_frontmatter(path: str, text: str) -> List[Violation]:
    """Framework-level schema check reused by U4 validators: required fields
    present, enumerated fields within the frozen v1 vocabularies."""
    violations: List[Violation] = []
    parsed = parse_frontmatter(text)
    for line, reason in parsed.errors:
        violations.append(emit("FRONTMATTER_MALFORMED", path, line, reason=reason))
    fields = parsed.fields
    for name in REQUIRED_ENTRY_FIELDS:
        if name not in fields:
            violations.append(emit("FIELD_MISSING", path, None, field=name))
    if "status" in fields and fields["status"] not in ENTRY_STATUS_VALUES:
        violations.append(emit("FIELD_INVALID", path, None, field="status"))
    if "source_type" in fields and fields["source_type"] not in SOURCE_TYPE_VALUES:
        violations.append(emit("FIELD_INVALID", path, None, field="source_type"))
    if "verification" in fields and fields["verification"] not in VERIFICATION_VALUES:
        violations.append(emit("FIELD_INVALID", path, None, field="verification"))
    domains = fields.get("domains")
    if domains is not None:
        if not isinstance(domains, list) or not domains or any(
                domain not in DOMAINS for domain in domains):
            violations.append(emit("FIELD_INVALID", path, None, field="domains"))
    relevance = fields.get("relevance")
    if relevance is not None:
        if not isinstance(relevance, dict) or not relevance or any(
                key not in DOMAINS or value not in RELEVANCE_TIERS
                for key, value in relevance.items()):
            violations.append(emit("FIELD_INVALID", path, None, field="relevance"))
    return violations


# --- Artifact discovery ------------------------------------------------------

def iter_entry_paths(repo_root: str) -> Iterator[str]:
    import os
    entries_dir = os.path.join(repo_root, "library", "entries")
    if not os.path.isdir(entries_dir):
        return
    for name in sorted(os.listdir(entries_dir)):
        if name.endswith(".md"):
            yield os.path.join(entries_dir, name)


def iter_report_paths(repo_root: str, domain: str) -> Iterator[str]:
    import os
    reports_dir = os.path.join(repo_root, "reports", domain, "daily")
    if not os.path.isdir(reports_dir):
        return
    for name in sorted(os.listdir(reports_dir)):
        if name.endswith(".md"):
            yield os.path.join(reports_dir, name)
