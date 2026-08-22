---
slug: 2026-shi-row-level-chunks-rag
title: "Retrieve One Row from a Table, Not the Whole Table: Row-Level Chunks for RAG"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/retrieve-one-row-from-a-table-not-the-whole-table-row-level-chunks-for-rag/
canonical_ids: []
publisher_or_author: "Kezhan Shi — Towards Data Science"
published: 2026-08-21
captured: 2026-08-22
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on the reliable-research-and-policy-products lens: a concrete,
  implementable chunking method for tabular data in RAG systems, with a
  dispatcher that selects retrieval granularity by question type and
  quantified compression results — directly usable for document-grounded
  pipelines that must ground answers in tables.
---

# Retrieve One Row from a Table, Not the Whole Table: Row-Level Chunks for RAG

## Summary

Argues that RAG systems treating an entire table as a single retrieval
chunk waste context and force the generation model to filter irrelevant
rows, because most user questions target a specific row while document
structure is organized as a rectangle. Proposes a `serialize_table_rows`
function that converts a parsed markdown pipe-formatted table into a
parallel row-level index, where each body row becomes its own chunk
formatted as "column: value | column: value" with headers preserved. A
dispatcher then selects retrieval scale by question type: row-level
indexing for targeted lookups, table-wide expansion for synthesis queries
where most rows are relevant. Reports two quantified compression examples:
an insurance-guarantees lookup returning a single-row answer (122
characters) versus the full table slice (943 characters), a 7.7x
reduction; and a query against the "Attention Is All You Need" paper's
Table 1 returning a targeted 124-character answer versus 528 characters for
the whole table, a 4.3x reduction that the author reports scales with row
count. Also describes handling for multi-row table headers to avoid silent
failures on more complex table structures.

## Why it matters

A directly reusable pattern for anyone building document-grounded research
or policy pipelines that need to ground answers in tabular source data
(financial statements, statistical tables, benchmark results) without
flooding the context window with irrelevant rows — concrete code-level
guidance rather than a general RAG-chunking opinion.

## Verification notes

Article fetched and read directly (2026-08-22); the author, the 2026-08-21
publication date, the `serialize_table_rows` method, the dispatcher logic,
and both quantified compression examples (7.7x, 4.3x) trace to the fetched
article text. `partial` rather than `verified`: the compression figures are
the author's own worked examples on her own pipeline, not independently
reproduced or corroborated this run.

## Updates

None yet.

## Related entries

[2026-shi-rag-typed-generation-contract](2026-shi-rag-typed-generation-contract.md) — same author; that entry covers typed generation contracts against extracted values, this one covers chunking strategy for the retrieval step feeding such a contract.
