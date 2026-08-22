---
slug: 2026-angela-shi-loop-engineering-pdf-outline-rag
title: "Building Document Structure with Loop Engineering: Recovering a PDF's Outline from Body Typography for RAG"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/building-document-structure-with-loop-engineering-recovering-a-pdfs-outline-from-body-typography-for-rag
canonical_ids: []
publisher_or_author: "Angela Shi — Towards Data Science"
published: 2026-08-05
captured: 2026-08-06
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on reliable research/policy products (rigorous document-grounding for
  RAG): a "rules propose, LLM validates" pattern for recovering a PDF's
  outline from body typography, with quantified precision/recall gains from
  a bounded LLM validation pass over a purely deterministic baseline (lens 8).
---

# Building Document Structure with Loop Engineering: Recovering a PDF's Outline from Body Typography for RAG

## Summary

Describes a method for reconstructing a table-of-contents/outline for PDFs
that lack a native outline, by scoring each line of body text on six
deterministic typography signals: font-size ratio (relative to median body
size), boldness, a numeric-prefix regex match ("1.", "1.2.3", "I.", "A."),
short line length, left alignment to the page margin, and blank space above
the line. A weighted sum of these signals produces heading candidates. A
bounded LLM validation loop (capped at 3 passes, stopping on convergence,
constrained to a fixed output schema, with an injected-callable design
limiting the model's tool access) then filters false positives in five
named categories: single digits, dot-leaders, author names, table cells,
and numeric results. Tested against six public PDFs with known structure
(the "Attention Is All You Need" paper and four NIST/FEMA standards
documents): the deterministic pass alone reached 77% macro-average recall
and 20% micro-average precision (100% level accuracy on matched rows for
decimal-numbered documents); adding one LLM validation pass raised
micro-average precision to 87% while recall held on five of the six test
documents (the Roman-numeral-structured FEMA manual showed precision 72%
but recall dropping to 22%).

## Why it matters

A concrete, quantified "rules propose, LLM validates" architecture for a
problem that directly undermines RAG citation reliability: retrieval over
PDFs with no usable structure. The reported precision jump (20% to 87%)
from adding one bounded, schema-constrained LLM pass over a cheap
deterministic baseline is a specific, reusable pattern for teams building
document-grounded agents that need traceable citations, not just any
retrieved chunk.

## Verification notes

Article fetched directly (2026-08-06); title, author, "August 5, 2026"
publication date, the six typography signals, the bounded-loop design
(3-pass cap, convergence stop, fixed schema, injected-callable restriction),
the five false-positive categories, and the reported precision/recall
figures on the six named test documents all trace directly to the fetched
article text. `partial` rather than `verified`: the precision/recall
numbers are the author's own single-run experiment on a small (n=6),
self-selected test set, not independently reproduced or corroborated this
run.

## Updates

None yet.

## Related entries

[2026-shi-rag-typed-generation-contract](2026-shi-rag-typed-generation-contract.md) — a different author (Kezhan Shi, not Angela Shi) but the same publication and adjacent lens: RAG output/extraction reliability patterns.
[2026-shi-rag-dispatcher-loop-control](2026-shi-rag-dispatcher-loop-control.md) — same author and series (Enterprise Document Intelligence); covers retrieval dispatch and loop termination.
[2026-angela-shi-rag-corpus-shapes](2026-angela-shi-rag-corpus-shapes.md) — same author and series; covers classifying a document collection's shape before building a RAG pipeline.
[2026-shi-rag-dispatcher-loop-control](2026-shi-rag-dispatcher-loop-control.md) — same author and series (Enterprise Document Intelligence); Article 13, covering retrieval dispatch and loop termination.
