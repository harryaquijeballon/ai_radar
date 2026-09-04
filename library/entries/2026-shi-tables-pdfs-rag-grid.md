---
slug: 2026-shi-tables-pdfs-rag-grid
title: "Tables in PDFs for RAG: Don't Flatten the Grid"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/tables-in-pdfs-for-rag-dont-flatten-the-grid/
canonical_ids: []
publisher_or_author: "Kezhan Shi — Towards Data Science"
published: 2026-09-03
captured: 2026-09-04
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On-lens (8: document-grounding for RAG) diagnostic and operation framework
  for preserving PDF table structure rather than flattening it to text, but
  narrative/conceptual with no quantified evaluation — medium rather than
  high.
---

# Tables in PDFs for RAG: Don't Flatten the Grid

## Summary
The article addresses tables in PDFs being flattened into plain text during ingestion for RAG, which destroys the row/column relationships a table encodes. It proposes a diagnostic (`table_df_meta`) that assesses five properties of a parsed table — parse quality, size, header status, multi-page continuity, and document-level context — and five composable operations (O1–O5): structural reconstruction from cell positions, multi-page concatenation with header propagation, question-driven projection, columnar extraction, and a vision-LLM fallback for tables that resist structural parsing. A dispatcher reads the diagnostics and composes the appropriate operations per table. Three real-world examples are used to illustrate parser successes/failures: a NIST Cybersecurity Framework table, a World Bank Commodity Markets Outlook table, and an academic paper table.

## Why it matters
Table-heavy source documents (statistical releases, policy annexes, financial tables) are common in the research/policy documents this profile's lens 8 targets, and flattening them silently destroys exactly the structure a numeric query needs. A named diagnostic-plus-dispatcher pattern gives builders concrete operations to reach for instead of ad hoc table handling, even though the post stops short of measuring how much retrieval accuracy improves.

## Verification notes
Fetched and read directly from the Towards Data Science post. The diagnostic properties, the five named operations, and the three worked examples are all traceable to the article's own text. The piece is conceptual/narrative — no benchmark, accuracy figures, or comparison against a flattening baseline is given — so verification is recorded as `partial` and relevance as `medium` rather than `high`.

## Updates
None yet.

## Related entries
[2026-shi-rag-not-in-document-evidence](2026-shi-rag-not-in-document-evidence.md) — same author's TDS post on evidence-backed RAG abstention, published one day earlier.
