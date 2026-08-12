"""Queue-record model shared by the U4 validators (plan R12-R15, R19-R21).

DRAFT record format — finalized by the U5 engine revision; validators and
fixtures are built against this shape and U5 must either adopt it or update
both together:

    ### <canonical public URL>            <- one H3 heading per record; the
    - title: Public title if visible         URL is the record's stable id
    - domain: social_science
    - first_encountered: 2026-07-23
    - last_encountered: 2026-07-23
    - reason_class: verification_insufficient
    - reason: short controlled note
    - surfaced_by: watchlist:VoxEU
    - action_needed: locate public artifact
    - status: pending

Outside records, only blank lines, `#`-heading lines, and HTML comment lines
are legal — anything else is a parse error (fail closed, never guessed at).
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple

QUEUE_DEFERRED = "deferred_candidates"
QUEUE_PROPOSALS = "source_proposals"

DEFERRED_STATUS = ("pending", "archived", "provisional", "rejected",
                   "dismissed", "duplicate")
PROPOSAL_STATUS = ("pending", "promoted", "rejected", "already_covered")

REASON_CLASSES = (
    "information_boundary_unclear",
    "access_or_license_unclear",
    "source_identity_unclear",
    "verification_insufficient",
    "relevance_requires_judgment",
    "possible_duplicate_requires_review",
    "other",
)

DEFERRED_REQUIRED = ("domain", "first_encountered", "last_encountered",
                     "reason_class", "reason", "surfaced_by", "action_needed",
                     "status")
DEFERRED_OPTIONAL = ("title", "source_type", "resolution_date", "resolution",
                     "linked_ref")
PROPOSAL_REQUIRED = ("source_name", "domain", "first_discovered",
                     "last_encountered", "why_useful", "surfaced_by",
                     "proposed_purpose", "status")
PROPOSAL_OPTIONAL = ("source_type", "review_note")

# Fields an unattended run may touch on an EXISTING pending record (R15/R20):
MUTABLE_UNATTENDED = ("last_encountered",)
# Free-text justification fields may only grow (old text must survive):
GROW_ONLY_UNATTENDED = ("reason", "why_useful", "action_needed", "review_note")

FREE_TEXT_FIELDS = ("title", "reason", "action_needed", "why_useful",
                    "review_note", "proposed_purpose", "surfaced_by",
                    "source_name", "resolution", "linked_ref")
MAX_FREE_TEXT = 240

_TOKEN_PARAM_RE = re.compile(
    r"[?&](token|key|apikey|api_key|auth|secret|access_token|sig|signature"
    r"|utm_[a-z]+)=", re.IGNORECASE)
_CREDENTIAL_RE = re.compile(r"^[a-z+]+://[^/]*:[^/]*@", re.IGNORECASE)

_RECORD_RE = re.compile(r"^### (\S+)\s*$")
_FIELD_RE = re.compile(r"^- ([a-z_]+):\s?(.*)$")


class QueueRecord:
    __slots__ = ("url", "fields", "line")

    def __init__(self, url: str, line: int):
        self.url = url
        self.fields: Dict[str, str] = {}
        self.line = line


def queue_type(path: str) -> Optional[str]:
    if "/%s/" % QUEUE_DEFERRED in "/" + path or QUEUE_DEFERRED + "/" in path:
        return QUEUE_DEFERRED
    if "/%s/" % QUEUE_PROPOSALS in "/" + path or QUEUE_PROPOSALS + "/" in path:
        return QUEUE_PROPOSALS
    return None


def parse_queue_file(text: str) -> Tuple[List[QueueRecord], List[Tuple[int, str]]]:
    records: List[QueueRecord] = []
    errors: List[Tuple[int, str]] = []
    current: Optional[QueueRecord] = None
    in_comment = False
    for number, line in enumerate(text.split("\n"), start=1):
        stripped = line.strip()
        if in_comment:
            if stripped.endswith("-->"):
                in_comment = False
            continue
        if stripped.startswith("<!--") and not stripped.endswith("-->"):
            in_comment = True
            continue
        record_match = _RECORD_RE.match(line)
        if record_match:
            current = QueueRecord(record_match.group(1), number)
            records.append(current)
            continue
        field_match = _FIELD_RE.match(line)
        if field_match and current is not None:
            key = field_match.group(1)
            if key in current.fields:
                errors.append((number, "duplicate-field"))
            current.fields[key] = field_match.group(2).strip()
            continue
        if stripped == "" or stripped.startswith("#") or stripped.startswith(">") \
                or stripped.startswith("<!--") or stripped.endswith("-->"):
            continue
        errors.append((number, "unparseable-line"))
    return records, errors


def url_unsafe_reason(url: str) -> Optional[str]:
    if not (url.startswith("http://") or url.startswith("https://")):
        return "not-http-url"
    if _CREDENTIAL_RE.match(url):
        return "credentials-in-url"
    if _TOKEN_PARAM_RE.search(url):
        return "token-or-tracking-param"
    return None


def required_fields(kind: str) -> Tuple[str, ...]:
    return DEFERRED_REQUIRED if kind == QUEUE_DEFERRED else PROPOSAL_REQUIRED


def known_fields(kind: str) -> Tuple[str, ...]:
    if kind == QUEUE_DEFERRED:
        return DEFERRED_REQUIRED + DEFERRED_OPTIONAL
    return PROPOSAL_REQUIRED + PROPOSAL_OPTIONAL


def status_values(kind: str) -> Tuple[str, ...]:
    return DEFERRED_STATUS if kind == QUEUE_DEFERRED else PROPOSAL_STATUS
