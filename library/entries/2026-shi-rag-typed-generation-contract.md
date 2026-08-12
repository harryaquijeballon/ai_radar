---
slug: 2026-shi-rag-typed-generation-contract
title: "Most RAG Hallucinations Are Extraction Errors: Seven Patterns for a Typed Generation Contract"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/most-rag-hallucinations-are-extraction-errors-seven-patterns-for-a-typed-generation-contract/
canonical_ids: []
publisher_or_author: "Kezhan Shi — Towards Data Science"
published: 2026-07-23
captured: 2026-07-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on the reliable-research-and-policy-products lens: reframes RAG
  "hallucinations" as upstream extraction errors and gives seven concrete,
  implementable patterns for treating generation as a typed contract rather
  than free text. Directly usable for building defensible document-grounded
  agents, the profile's standing generic interest. Discovered in the 22-23
  Jul 2026 window via Towards Data Science.
---

# Most RAG Hallucinations Are Extraction Errors: Seven Patterns for a Typed Generation Contract

## Summary

Practitioner essay (Kezhan Shi, Towards Data Science, 23 July 2026) arguing
that most errors labeled "hallucinations" in retrieval-augmented generation
systems are actually upstream extraction errors, not fabrications from the
model's internal knowledge, and proposing seven concrete patterns to reduce
them by treating generation as a typed contract: (1) return typed objects
with citations and fidelity flags instead of free text; (2) let the model
extract raw values and do arithmetic in code for an auditable trail; (3)
determine list-completeness from retrieval-time section boundaries rather
than asking the model about text it cannot see; (4) use two booleans
(`answer_found`, `complete_answer_found`) instead of one confidence float;
(5) compose prompts from named, reusable fragments for traceability; (6)
avoid reasoning models for schema-constrained extraction, since the schema
already limits the output space; (7) decompose extraction into multi-stage
calls for smaller models, while frontier models can fill compound schemas in
one call.

## Why it matters

A directly implementable checklist for exactly the failure mode this
project's own library-entry and report pipeline depends on avoiding:
claim-to-source traceability. Patterns 1-4 in particular map onto concrete
engineering choices (typed outputs with citation fields, code for
computation, explicit completeness flags) that make a document-grounded
agent's output easier to audit and harder to silently get wrong.

## Verification notes

Article fetched and read in full; all seven patterns and their stated
rationale are traced directly to the source text. This is an argued
practitioner position with worked reasoning rather than an empirical result
requiring independent corroboration; no external claims (benchmarks, cited
studies) were made that would need separate verification.

## Updates

*(none yet)*

## Related entries

None yet.
