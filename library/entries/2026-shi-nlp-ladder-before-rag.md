---
slug: 2026-shi-nlp-ladder-before-rag
title: "RAG Is Not the Whole Toolkit: The NLP Techniques Real Problems Still Need"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/rag-is-not-the-whole-toolkit-the-nlp-techniques-real-problems-still-need/
canonical_ids: []
publisher_or_author: "Kezhan Shi — Towards Data Science"
published: 2026-08-29
captured: 2026-08-30
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Gives a concrete, ordered decision ladder — exact match, spelling fix,
  keyword search, embeddings, RAG, LLM prompting, cheapest-sufficient-method
  first — for enterprise document/support systems, on lens 4 (deterministic
  guardrails around stochastic components) and lens 8 (RAG grounding done
  rigorously); each rung names the rule it fired on, directly supporting
  auditable "I don't know" responses.
---

# RAG Is Not the Whole Toolkit: The NLP Techniques Real Problems Still Need

## Summary
Shi argues that defaulting straight to RAG or LLM prompting for enterprise
document/support systems skips cheaper, more auditable techniques that solve
most requests outright. The piece lays out an ordered "ladder" of methods —
exact match (for requests with clean identifiers), spelling correction
(single-character errors against corpus vocabulary), keyword search (expert-
curated vocabularies), embeddings (wording beyond the vocabulary), RAG, and
LLM prompting, described as "the slowest way to do it, the most expensive" —
with the design rule to reach for the lowest rung that solves the case:
"Most requests are settled by one of these, in milliseconds, and each one
can name the rule it fired on." Each technique's traceability is presented
as the mechanism that makes an "I don't know" response auditable, since the
system can show which rung was tried and why it didn't fire. On tables, the
piece argues for escalating through four representation levels only as
needed rather than flattening everything into RAG chunks. One concrete,
self-contained quantified claim: for local/small models, "JSON structural
validity passes from 1B [parameters] onwards. Literal extraction without
fabrication kicks in at 7B" (unverified beyond this stated threshold — the
piece references, but does not itself detail, three linked "bonus"
benchmark posts: a 13-model comparison, a 4-PDF-parser comparison, and an
11-model local-Ollama-size comparison; those figures are not independently
confirmed here).

## Why it matters
A directly actionable architecture pattern for anyone building document- or
support-facing RAG systems for research or policy use: it reframes "add an
LLM" as the last, not first, resort, and ties each cheaper technique to an
explicit, inspectable firing rule — the kind of deterministic-first design
this radar's lens 4 and lens 8 look for in RAG-grounded products meant to be
defensible rather than demo-grade.

## Verification notes
Fetched directly from towardsdatascience.com (allowlisted). The ladder's six
named techniques, their stated order and rationale, the model-size threshold
quote (1B/7B), and the four-level table-representation claim were traced
directly to the fetched source text. The three benchmark posts it references
(13 LLM models, 4 PDF parsers, 11 local Ollama models) were not fetched or
reviewed separately, so their specific figures are not corroborated and are
not summarized above beyond the one self-contained quote.

## Updates
None yet.

## Related entries
Related RAG-engineering pieces by the same author: [2026-shi-rag-typed-generation-contract](2026-shi-rag-typed-generation-contract.md), [2026-shi-row-level-chunks-rag](2026-shi-row-level-chunks-rag.md), [2026-shi-enterprise-rag-ten-positions](2026-shi-enterprise-rag-ten-positions.md) — distinct topic (method-selection ladder rather than chunking or hallucination patterns).
