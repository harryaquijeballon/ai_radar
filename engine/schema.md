# Archive Schema — entry lifecycle, dedup, index, rejections

The library is the product. One markdown file per *development* (a paper, framework, dataset, result, or policy event — not per URL) in `library/entries/`. This schema is frozen for v1; friction goes to follow-up work, not silent drift.

## Entry file

Filename: `library/entries/<slug>.md`, where `<slug>` is `YYYY-<author-or-project>-<short-topic>` in kebab-case (year of publication, or capture year if unknown).

### Frontmatter — every field required unless marked optional

```yaml
---
slug: 2023-korinek-genai-economic-research
title: "Generative AI for Economic Research"
status: accepted            # accepted | provisional
domains: [social_science]   # social_science, ai_engineering — one or both
source_type: academic       # primary | academic | commentary
source_url: https://example.org/paper
canonical_ids: ["doi:10.1257/jel.20231736"]   # DOI, arXiv ID, repo owner/name, ISBN; [] if none
publisher_or_author: "Anton Korinek — Journal of Economic Literature"
published: 2023-12          # ISO date, partial date, or unknown (only with page evidence; never inferred)
captured: 2026-07-22
relevance:                  # tier per domain, judged against profiles/<domain>/profile.md
  social_science: high      # high | medium | low | n/a
  ai_engineering: medium
verification: verified      # verified | partial | unverified
license: "CC BY 4.0"        # optional — only when the source states a reuse licence
rationale: >-
  One or two sentences: why this cleared review, in terms of the interest
  profiles. Written public-safe.
---
```

Field semantics:

- `status` — `accepted` entries are full library members. `provisional` entries are quarantined: visibly marked, **never report-eligible**, awaiting verification. Status lives here, not in directory structure, so an upgrade is an edit, not a move.
- `source_type` — `primary` (original artifact: dataset, code release, official announcement, legislation), `academic` (peer-reviewed or working paper), `commentary` (analysis, blog, opinion about primary/academic work).
- `canonical_ids` — the dedup anchors. Record every stable identifier found: DOI, arXiv ID (`arxiv:2304.xxxxx`), repository (`repo:owner/name`), working-paper number (`nber:w30957`).
- `publisher_or_author` — one convention, always: `"Author(s) — Series/Publisher"` (e.g., `"Anton Korinek — Journal of Economic Literature 61(4)"`; multi-author institutional work lists authors, then series and publisher).
- `verification` — `verified`: every summarized claim traced to the cited source, load-bearing claims corroborated. `partial`: traced but load-bearing claims not corroborated. `unverified`: source not machine-readable or claims not checkable. An entry whose claims are all unverified must be `provisional`.
- `license` — optional; record only when the source states a reuse licence (e.g., CC BY 4.0). Downstream consumer: sharing decisions — an entry summarizing openly licensed material can quote it more freely.
- `rationale` — required on every entry (accepted or provisional): the explicit selection reasoning, referencing the profile lens it cleared (or why it was retained despite a low score, e.g., deliberate user save).

### Body — sections in this order

```markdown
# <title>

## Summary
What the development is and what it claims. Every claim here must be traceable
to the cited source; claims that could not be verified are marked "(unverified)".

## Why it matters
The practical implication for the interest profiles — what a reader could do
with this. Written for sharing.

## Verification notes
What was checked and how: source reachable? claims traced? load-bearing claims
corroborated against what? What could not be verified and why.

## Updates
Append-only, newest last. Each update is dated with its own capture date.
Corrections, retractions, and follow-ups are recorded here and ONLY here:
everything above the `## Updates` heading is immutable once written — no
edits, no correction markers — and deterministic validation enforces this
byte-for-byte. Name the affected claim in the dated update line instead
(e.g., "- **2026-08-01** — Correction: the Summary's 35% figure was revised
to 28% by the authors <link>."). Replacing the placeholder line with the
first dated update is permitted.

- **YYYY-MM-DD** — what changed, with source link.

## Related entries
Links to other entries: `[<slug>](<slug>.md)` — supersedes, extends,
contradicts, same-project. "None yet." if empty.
```

## The four review dispositions and what each writes

Every candidate gets exactly one:

1. **Archive new** — create `entries/<slug>.md` (status per verification state), add a row to `INDEX.md`.
2. **Merge / link** — no new entry. Append a dated line to the existing entry's Updates (and/or Related entries), extend its `canonical_ids` with any new identifiers, update the INDEX row if title/ids changed.
3. **Retain provisional** — create the entry with `status: provisional`, `verification: unverified` or `partial`, add INDEX row. For sources that cannot be fetched (e.g., LinkedIn), a metadata-only entry: whatever provenance the user supplied, all claims marked unverified, and a note requesting the underlying public artifact.
4. **Reject** — no entry. Append one line to `rejections.md` with the reason.

Write ordering (interruption safety): disposition artifacts — entry file, INDEX row, rejection line — are written **before** any inbox line is annotated as processed.

### Provisional → accepted

`Verify Provisionals` (procedure defined in `ENGINE.md`) upgrades a provisional entry when verification later succeeds: edit `status` to `accepted`, update `verification`, record the trigger in Updates. It fires when a new candidate dedup-matches a provisional entry, and on explicit user request.

## Dedup matching — identifier first, similarity second

Checked against `INDEX.md` and `rejections.md` before any disposition:

1. **Identifier match**: same canonical URL (normalized: strip tracking params, trailing slash), or any shared `canonical_ids` value → same development.
2. **Similarity match**: no shared identifier, but title/topic clearly the same development (e.g., press coverage of an already-archived paper) → same development.
3. **Same-artifact rule**: same underlying artifact or result (preprint → published version, paper → press coverage, repo → release announcement) → merge/link into the existing entry. A new version with **materially new capability or results** → new entry, linked both ways in Related entries.
4. Previously rejected source re-surfacing in discovery → skip (no re-review, no new rejection line).

## INDEX.md — derived, regenerable

`library/INDEX.md` is a table derived from entry frontmatter. Entries are the single source of truth; when the index and entries disagree (count or paths mismatch), regenerate the index by re-reading every file in `entries/` and rewriting the table. Columns:

```markdown
| slug | title | domains | status | canonical ids / URL |
```

## rejections.md — dated log

One line per rejection, newest last:

```markdown
| date | source | reason |
```

Discovery consults this log: listed sources are skipped silently. Manual re-submission of a rejected source by the user overrides the log (their insistence is a signal — re-review it).
