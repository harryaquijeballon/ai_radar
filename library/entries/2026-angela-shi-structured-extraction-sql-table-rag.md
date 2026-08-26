---
slug: 2026-angela-shi-structured-extraction-sql-table-rag
title: "One Document Type, a Million Files: Structured Extraction into the SQL Table RAG Queries"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/one-document-type-a-million-files-structured-extraction-into-the-sql-table-rag-queries
canonical_ids: []
publisher_or_author: "Angela Shi, Kezhan Shi — Towards Data Science"
published: 2026-08-25
captured: 2026-08-26
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  A concrete, low-tech-first RAG-corpus-preparation technique (lens 8:
  reliable research/policy products) for the specific, common case of a
  large collection of a single document type — continues this author
  pair's evidenced series on RAG corpus design.
verification: verified
---

# One Document Type, a Million Files: Structured Extraction into the SQL Table RAG Queries

## Summary

The authors argue that when an organization holds a large collection of a
single, repeated document type (their example: thousands of insurance
policies), the right retrieval approach is structured extraction into a
SQL table, not discovery-oriented RAG — because "the schema already exists
in the practice of the people who handle the documents" and can be
elicited through conversation rather than inferred from the documents
themselves. The method: a one-hour structured interview with two document
handlers (not their managers), using four sequential questions to surface
candidate columns, validated by two signals — fields the handlers name
instantly, and consistent naming across the two handlers independently.
Three field types are named as likely to fail this process: fields with
ambiguous meaning, fields empty on more than half of documents, and fields
that are judgments rather than facts. Their worked example yields six
business fields (policy number, client name, product type, effective and
renewal dates, premium amount). On cost, they estimate the preparation
investment pays off once question volume (their example: roughly 50
questions/day from claims handlers, ~12,000/year per person) approaches
the size of the document corpus, typically within months for a
several-thousand-document corpus (unverified as a general rule beyond
their example).

## Why it matters

For anyone building document-grounded research or policy tools, this is a
concrete alternative to defaulting to embedding-based RAG for corpora that
are actually structured data in disguise: a cheap, verifiable
elicitation method (two independent interviews, cross-checked) to decide
whether extraction-to-SQL beats retrieval, plus explicit failure criteria
for which fields not to extract. It is a specific, actionable addition to
this outlet's ongoing RAG-corpus-design series already represented in the
library.

## Verification notes

Fetched and read directly from towardsdatascience.com. The interview
method, validation signals, failure-mode criteria, and cost example are
all traced to the post's own worked case study; the cost/ROI claim is the
authors' own estimate from one example, not independently corroborated
across other organizations, and is noted as unverified beyond that
example.

## Updates

None yet.

## Related entries

[2026-angela-shi-rag-corpus-shapes](2026-angela-shi-rag-corpus-shapes.md),
[2026-angela-shi-case-file-relational-tables-rag](2026-angela-shi-case-file-relational-tables-rag.md),
[2026-angela-shi-multi-document-rag-outline](2026-angela-shi-multi-document-rag-outline.md),
[2026-angela-shi-loop-engineering-pdf-outline-rag](2026-angela-shi-loop-engineering-pdf-outline-rag.md),
[2026-shi-row-level-chunks-rag](2026-shi-row-level-chunks-rag.md) — same
author pair's ongoing RAG-corpus-design series.
