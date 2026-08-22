---
slug: 2026-angela-shi-rag-corpus-shapes
title: "Three Kinds of RAG Corpus, and What It Costs to Build for the Wrong One"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/three-kinds-of-rag-corpus-and-what-it-costs-to-build-for-the-wrong-one/
canonical_ids: []
publisher_or_author: "Angela Shi — Towards Data Science"
published: 2026-08-20
captured: 2026-08-22
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on the reliable-research-and-policy-products lens: a diagnostic
  framework for classifying a document collection's "shape" before choosing
  a RAG architecture, with a quantified worked failure case showing the
  cost of the wrong choice — directly usable by anyone standing up a
  document-grounded research or policy pipeline.
---

# Three Kinds of RAG Corpus, and What It Costs to Build for the Wrong One

## Summary

Argues that treating every document collection as a single undifferentiated
vector store wastes effort and produces avoidable retrieval failures,
because document collections come in three distinct "shapes" that need
different architectures: (1) a pile of unrelated files with no common
fields; (2) a typed corpus of homogeneous documents where business users
can name consistent fields across the set; (3) case bundles, related
documents grouped around a single entity. Proposes three diagnostic
questions to determine a corpus's shape before building: do documents
reference each other; can users name a field meaningful across all
documents; do documents arrive in expected bundles. Demonstrates the cost
of misclassification with a baseline test: a simple per-document pipeline
run over five NIST documents for the query "What is a Profile in the
Cybersecurity Framework?" found the answer in only one of the five
documents, with the other four calls — roughly 2.9 seconds each — producing
nothing usable, i.e. four out of five calls did no work.

## Why it matters

Gives builders of document-grounded research/policy agents a pre-build
diagnostic to avoid the single most common RAG-architecture mistake this
radar has seen described (flat-pile retrieval applied to a corpus that
isn't a flat pile), with a directly reusable worked example of the wasted
cost when the diagnosis is skipped. Complements the same author's earlier
archived work on dispatcher-based retrieval routing.

## Verification notes

Article fetched and read directly (2026-08-22); the author, the 2026-08-20
publication date, the three corpus shapes, the three diagnostic questions,
and the five-NIST-document baseline test (1/5 documents useful, ~2.9s per
call) all trace to the fetched article text. `partial` rather than
`verified`: the baseline test is the author's own reporting on her own
pipeline, not independently reproduced or corroborated this run.

## Updates

None yet.

## Related entries

[2026-angela-shi-loop-engineering-pdf-outline-rag](2026-angela-shi-loop-engineering-pdf-outline-rag.md) — same author and "Enterprise Document Intelligence" series.
[2026-shi-rag-dispatcher-loop-control](2026-shi-rag-dispatcher-loop-control.md) — same author and series; that entry covers retrieval-pattern dispatch and loop termination once a corpus is being queried, this one covers classifying the corpus before building the pipeline at all.
