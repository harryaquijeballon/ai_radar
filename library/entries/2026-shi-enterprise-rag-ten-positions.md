---
slug: 2026-shi-enterprise-rag-ten-positions
title: "10 Positions for Enterprise RAG That Mainstream Tutorials Get Wrong"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/10-positions-for-enterprise-rag-that-mainstream-tutorials-get-wrong/
canonical_ids: []
publisher_or_author: "Kezhan Shi — Towards Data Science"
published: 2026-08-24
captured: 2026-08-25
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on reliable research and policy products (lens 8) and deterministic
  guardrails (lens 4): names ten concrete, mechanism-level departures from
  tutorial-style RAG for enterprise use — structure-first retrieval,
  deterministic dispatchers over autonomous agents in regulated settings,
  per-failure-mode evaluation, typed relational data at each pipeline
  stage, and line-level verbatim citations — each stated as a specific
  practice a builder could adopt, not a general opinion.
---

# 10 Positions for Enterprise RAG That Mainstream Tutorials Get Wrong

## Summary

A ten-point manifesto arguing that the standard RAG tutorial pattern
(chunk documents, embed, retrieve top-k by cosine similarity, generate)
"starts wobbling the day a real enterprise document hits it," and that
much of the standard advice optimizes for vendor demo simplicity over
production accuracy. The ten positions: (1) vector search should be a
fallback behind structure-first retrieval (tables of contents, expert
keywords); (2) expert-maintained synonym dictionaries beat embeddings for
known vocabulary, with embeddings reserved for unseen phrasings; (3)
cross-encoder rerankers add latency without precision gains once upstream
retrieval already returns small, scoped candidate pools; (4) different
document types need different retrieval strategies — route aggregation
questions to SQL, not RAG, rather than indexing everything into one
vector store; (5) enterprises with hundreds of document types and dozens
of domain experts are not hyperscalers, and hyperscaler-optimized patterns
don't transfer; (6) enterprise RAG should amplify existing expert
judgment, not try to automate it away with autonomous agents; (7)
readable, auditable deterministic dispatcher code outperforms autonomous
agents in regulated contexts where decisions must be inspectable; (8)
aggregate accuracy metrics hide critical failures — evaluation must be
sliced by question type and failure mode; (9) each pipeline stage should
output typed, structured data (DataFrames) rather than plain text
strings, enabling independent testing and reproducible audits; (10)
citations should carry line-level, verbatim quotes and page coordinates
so they are verifiable evidence, not decoration. The author's summary
claim: "most hallucinations are extraction errors the schema can close."

## Why it matters

A concrete, checklist-style counter-manifesto to default RAG-tutorial
advice, aimed squarely at making retrieval-grounded systems defensible
rather than merely plausible-looking: several positions translate directly
into engineering decisions for a research or policy RAG product —
preferring deterministic, auditable dispatch over autonomous agents where
decisions must be inspectable, typing intermediate pipeline outputs for
independent testing, evaluating per failure mode rather than by aggregate
accuracy, and demanding verifiable line-level citations. Useful as a
concrete checklist against which to audit an existing or planned RAG
pipeline.

## Verification notes

Fetched directly from the published article (2026-08-25); author (Kezhan
Shi), publication date (24 Aug 2026), and all ten positions and the
"hallucinations are extraction errors" claim trace directly to the fetched
article text. This is an opinion/practice piece (commentary, not an
empirical study) — its claims are the author's stated engineering
positions rather than experimentally measured results, so "verified" here
means the positions were traced accurately to the source, not that they
were independently tested. Part of a longer "Enterprise Document
Intelligence" series; other installments not read at capture.

## Updates

None yet.

## Related entries

None yet.
