---
slug: 2026-polasani-doulcet-parsebench-2
title: "Introducing ParseBench-2"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://www.llamaindex.ai/blog/introducing-parsebench-v2
canonical_ids: []
publisher_or_author: "Gauthami Polasani, Pierre-Loic Doulcet — LlamaIndex"
published: 2026-11-12
captured: 2026-11-13
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 4 (evaluation and validation): a methodologically
  substantive, severity-weighted document-parsing benchmark (330+ injected
  error types, large reference-table/visual-grounding/forms test sets) —
  discounted from high because it is a framework vendor's own benchmark on
  which that vendor's own product ranks first, per the framework-vendor
  discount in profiles/ai_engineering/sources.md.
---

# Introducing ParseBench-2

## Summary
LlamaIndex's successor to ParseBench-1, a document-parsing benchmark scoring
parsers across six dimensions: text, formatting, tables, charts, layout
(visual grounding), and forms. Methodology: 330+ error types were defined by
injecting perturbations into correct outputs, each classed critical/major/
minor/harmless with severity-matched penalty caps so a single serious error
cannot be masked by many trivial matches; the test corpus grew from 2.1k to
4.3k cases; charts are scored against full reference tables (36,958 values
across 1,025 charts); visual grounding is checked on 538 pages; forms are
tested on 500 pages from 244 government templates across 30 countries.
Reported results: LlamaParse Agentic Plus scored 89.8 overall across 41
default configurations, versus 85.7 for the best direct vision model and
83.9 for the best competing parser; on cost, LlamaParse Agentic scored 83.4
at $0.0125/page versus 83.2 at $0.0300/page for the strongest competing
parser (self-reported; the post itself shows an inconsistent 88.4 vs. 89.8
figure for Agentic Plus's overall score without explaining the discrepancy
— unverified).

## Why it matters
The severity-weighted scoring design — capping how much a serious error can
be masked by many trivial correct matches, and separately stress-testing
charts, visual grounding, and forms rather than a single blended score — is
a reusable evaluation pattern for anyone building a document-extraction or
RAG-ingestion pipeline, independent of which specific parser a reader ends
up choosing; the vendor's own product unsurprisingly ranks first, so the
comparative numbers should be read with that caveat.

## Verification notes
Fetched directly from llamaindex.ai (allowlisted); authors and 2026-11-12
publication date confirmed. The methodology details (error-type count,
corpus size, chart/visual-grounding/forms test-set sizes) and the headline
accuracy and cost figures all trace directly to the fetched post text. The
post's own overall-score figures for LlamaParse Agentic Plus are internally
inconsistent (89.8 vs. 88.4) and this discrepancy is flagged unverified
above rather than resolved; no independent benchmark replication attempted.

## Updates
None yet.

## Related entries
None yet.
