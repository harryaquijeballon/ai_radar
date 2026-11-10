"""Identifier keys for entry dedup (plan 2026-11-09-001 U7b).

`engine/schema.md`, "Dedup matching", rule 1: two entries are the same
development when they share a `canonical_ids` value or the same canonical
URL. This module turns an entry's frontmatter into comparable keys, so the
write guard (`scripts/entry_write_guard.py`) and the library validator
(`check_library_consistency.py`) apply that rule identically.

Only the identifier rule is mechanical. The similarity and same-artifact
rules (schema rules 2 and 3) stay with the agent.
"""

from __future__ import annotations

import os
import re
from typing import Dict, Iterable, Optional, Set

import lib_radar

_ARXIV_ID = r"(\d{4}\.\d{4,5}|[a-z-]+(?:\.[a-z]{2})?/\d{7})"
_ARXIV_URL = re.compile(
    r"^(?:export\.)?arxiv\.org/(?:abs|pdf|html)/" + _ARXIV_ID
    + r"(?:v\d+)?(?:\.pdf)?$")
_DOI_URL = re.compile(r"^(?:dx\.)?doi\.org/(10\.\S+)$")
_VERSION = re.compile(r"v\d+$")
_TRACKING = re.compile(r"^(utm_[a-z]+|ref|source|fbclid|gclid)=", re.I)


def normalize_url(url: str) -> str:
    """Scheme, `www.`, fragment, tracking parameters and trailing slash
    removed; lower-cased. Empty string when there is nothing usable."""
    value = str(url or "").strip().lower()
    value = re.sub(r"^https?://", "", value)
    value = re.sub(r"^www\.", "", value)
    value = value.split("#", 1)[0]
    if "?" in value:
        path, query = value.split("?", 1)
        kept = [part for part in query.split("&")
                if part and not _TRACKING.match(part)]
        value = path.rstrip("/") + ("?" + "&".join(kept) if kept else "")
    return value.rstrip("/")


def normalize_id(identifier: str) -> str:
    """Lower-cased, whitespace-free; an arXiv version suffix is dropped
    (`arxiv:2611.07050v2` is the same paper as `arxiv:2611.07050`)."""
    value = re.sub(r"\s+", "", str(identifier or "")).lower()
    if value.startswith("arxiv:"):
        value = _VERSION.sub("", value)
    return value


def id_from_url(url: str) -> Optional[str]:
    """The identifier a URL itself carries (arXiv, DOI), or None."""
    normalized = normalize_url(url)
    match = _ARXIV_URL.match(normalized)
    if match:
        return "arxiv:" + match.group(1)
    match = _DOI_URL.match(normalized)
    if match:
        return "doi:" + match.group(1)
    return None


def id_keys(fields: Dict[str, object]) -> Set[str]:
    """Stable identifiers: `canonical_ids` plus any the source URL carries."""
    keys: Set[str] = set()
    canonical = fields.get("canonical_ids")
    if isinstance(canonical, list):
        keys.update(normalize_id(item) for item in canonical)
    derived = id_from_url(str(fields.get("source_url", "")))
    if derived:
        keys.add(derived)
    keys.discard("")
    return keys


def all_keys(fields: Dict[str, object]) -> Set[str]:
    """Identifier keys plus the normalized source URL (`url:` prefix)."""
    keys = id_keys(fields)
    url = normalize_url(str(fields.get("source_url", "")))
    if url:
        keys.add("url:" + url)
    return keys


def library_keys(repo_root: str,
                 skip_slugs: Iterable[str] = ()) -> Dict[str, str]:
    """key -> slug for every entry under `repo_root` (first slug wins).
    An unreadable or unparseable entry contributes nothing."""
    skipped = set(skip_slugs)
    found: Dict[str, str] = {}
    for path in lib_radar.iter_entry_paths(repo_root):
        slug = os.path.basename(path)[:-3]
        if slug in skipped:
            continue
        try:
            with open(path, encoding="utf-8", errors="replace") as handle:
                fields = lib_radar.parse_frontmatter(handle.read()).fields
        except OSError:
            continue
        for key in all_keys(fields):
            found.setdefault(key, slug)
    return found
