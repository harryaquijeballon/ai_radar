---
slug: 2026-angela-shi-multi-document-rag-outline
title: "Multi-Document RAG: A Folder of Unrelated PDFs Is One Long Document with a Nested Outline"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/multi-document-rag-a-folder-of-unrelated-pdfs-is-one-long-document-with-a-nested-outline/
canonical_ids: []
publisher_or_author: "Angela Shi — Towards Data Science"
published: 2026-08-22
captured: 2026-08-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on the reliable-research-and-policy-products lens: a two-level
  routing architecture for RAG over heterogeneous document folders that
  lack shared metadata fields, demonstrated on a real 63-file/4,211-page
  corpus with a quantified narrowing result — directly usable by anyone
  standing up document-grounded retrieval over a mixed corpus (e.g. mixed
  policy reports, papers, and standards documents).
---

# Multi-Document RAG: A Folder of Unrelated PDFs Is One Long Document with a Nested Outline

## Summary

Proposes treating a folder of unrelated PDFs — documents sharing no common
fields, unlike a typed corpus — as a single long document with chapters and
sections, rather than forcing a traditional relational or flat-vector
index onto it. The architecture has two levels: Level 0 is one summary
sentence per file, written specifically to help a router decide which
files are relevant rather than to summarize for a human reader; Level 1 is
each file's native table of contents, or a reconstructed outline where none
exists. A query is answered by first routing across the Level 0 summary
lines to select candidate files, then descending into each survivor's
Level 1 outline to select the relevant sections. Demonstrated on 63 public
PDFs totalling 4,211 pages (NIST security-control documents, arXiv papers,
and World Bank commodity reports): for a sample query about account
management controls, the two-pass routing narrows from 63 files down to
the handful that survive file-level routing, then from those to 5 relevant
pages.

## Why it matters

Gives builders of document-grounded research or policy agents a concrete
alternative to ontology-building or schema definition when a corpus has no
shared structure — a common situation for policy/research pipelines that
mix primary reports, standards documents, and papers. The "write summaries
for the router, not the reader" principle and the two-level routing
pattern are both directly reusable, and the worked example shows the
retrieval stays bounded and auditable (each routing decision traceable to
a specific summary line or outline entry) rather than opaque.

## Verification notes

Article fetched and read directly (2026-08-23); the author, the 2026-08-22
publication date, the two-level (Level 0/Level 1) routing architecture,
the 63-file/4,211-page corpus composition, and the worked query narrowing
from 63 files to 5 pages all trace to the fetched article text. `partial`
rather than `verified`: the worked example is the author's own
demonstration on her own assembled corpus, not independently reproduced or
corroborated this run.

## Updates

None yet.

## Related entries

[2026-angela-shi-loop-engineering-pdf-outline-rag](2026-angela-shi-loop-engineering-pdf-outline-rag.md) — same author and document-intelligence series; that entry covers reconstructing a single PDF's outline from body typography, which this entry's Level 1 step reuses across a folder of files.
[2026-angela-shi-rag-corpus-shapes](2026-angela-shi-rag-corpus-shapes.md) — same author and series; that entry diagnoses a corpus's "shape" before building, this entry is the concrete architecture for the "pile of unrelated files" shape it identifies.
