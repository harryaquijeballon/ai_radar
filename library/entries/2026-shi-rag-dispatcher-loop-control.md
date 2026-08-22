---
slug: 2026-shi-rag-dispatcher-loop-control
title: "RAG Workflow and Loop Engineering: The Dispatcher That Decides When to Loop and When to Stop"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/rag-workflow-and-loop-engineering-the-dispatcher-that-decides-when-to-loop-and-when-to-stop/
canonical_ids: []
publisher_or_author: "Angela Shi — Towards Data Science"
published: 2026-08-14
captured: 2026-08-15
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on deterministic guardrails and reliable research/policy products
  (lenses 4, 8): a concrete dispatcher pattern that keeps retrieval-strategy
  selection and loop-termination logic in deterministic code rather than
  delegated to an autonomous agent, with worked examples and cost figures —
  directly usable for anyone building document-grounded research pipelines.
---

# RAG Workflow and Loop Engineering: The Dispatcher That Decides When to Loop and When to Stop

## Summary

Article 13 in Angela Shi's "Enterprise Document Intelligence" series (Part
III closer), following the already-archived Article on recovering PDF
outlines from typography. Describes a dispatcher-based orchestration
pattern for RAG systems: rather than letting an LLM autonomously choose
retrieval strategies, deterministic Python code (1) parses the user's
question into a typed structure, (2) profiles the target document to
identify its characteristics, (3) dispatches the applicable retrieval
patterns — table-of-contents retrieval, keyword search, two-hop reference
following, listing aggregation — and (4) runs a bounded feedback loop with
explicit stopping criteria. The author's framing: "the dispatcher picks
which patterns fire... control staying in code" rather than an autonomous
agent. A worked example analyzes a question about regularization
techniques in the "Attention Is All You Need" paper, showing four patterns
firing simultaneously and iterating via the `pdf_qa_loop` orchestrator
function. Reported cost: typical 5-9 second execution on a 15-page PDF,
LLM calls dominating runtime. Termination is enforced by three mechanisms:
a maximum-iteration cap, candidate-stability checks, and confidence-drop
detection.

## Why it matters

A concrete, code-level alternative to letting an agent freely decide when
to keep retrieving: routing and stopping logic live in auditable,
deterministic code, with the LLM confined to well-scoped sub-tasks inside
each dispatched pattern. Directly reusable for teams building document-
grounded research or policy pipelines that need bounded cost and
reproducible stopping behavior, not just plausible-looking answers — the
standing "reliable research/policy product" interest this radar tracks.

## Verification notes

Article fetched directly (2026-08-15); the author, "August 14, 2026"
publication date, the series position (Article 13, closing Part III), the
four dispatched retrieval patterns, the `pdf_qa_loop` worked example, the
5-9 second cost figure, and the three termination mechanisms all trace
directly to the fetched article text. `partial` rather than `verified`:
the cost and behavior figures are the author's own reporting on her own
pipeline, not independently reproduced or corroborated this run.

## Updates

None yet.

## Related entries

[2026-angela-shi-loop-engineering-pdf-outline-rag](2026-angela-shi-loop-engineering-pdf-outline-rag.md) — same author and series (Enterprise Document Intelligence); the earlier article covers PDF outline recovery, this one covers retrieval dispatch and loop termination.
[2026-angela-shi-rag-corpus-shapes](2026-angela-shi-rag-corpus-shapes.md) — same author and series; covers classifying a document collection's shape before building a pipeline, upstream of this entry's dispatch/loop logic.
