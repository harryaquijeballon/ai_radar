---
slug: 2026-cekikj-persistent-knowledge-layer-rag
title: "Designing a Persistent Knowledge Layer That Refuses to Guess"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/designing-a-persistent-knowledge-layer-that-refuses-to-guess
canonical_ids: []
publisher_or_author: "Miodrag Cekikj — Towards Data Science"
published: 2026-08-16
captured: 2026-08-17
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 8 (reliable research and policy products): a concrete
  three-layer RAG architecture that stores contradictions between sources as
  first-class, owned objects instead of silently resolving them — directly
  applicable to building document-grounded research/policy agents that must
  not overwrite conflicting evidence.
---

# Designing a Persistent Knowledge Layer That Refuses to Guess

## Summary

The author proposes a three-layer architecture for RAG systems: an Evidence layer (a standard retrieval index), a Knowledge layer (structured, durable "wiki" objects — concepts, decisions, contradictions, relationships — that accumulate understanding across queries instead of reconstructing answers from scratch each time), and an Orchestrator layer (routing logic between the two). The central mechanism is treating contradictions between sources as first-class stored objects — both conflicting statements, their dates, and an accountable owner — rather than silently resolving them. Decisions carry explicit scope constraints so numbers "never travel without their qualifiers," and queries can be tagged with a date parameter so only documentation effective on that date is retrieved, preventing rules from applying retroactively. The reference implementation described uses Azure Blob Storage for originals, Azure AI Search for the evidence index, Cosmos DB for the structured knowledge objects, and FastAPI for orchestration. The author's core claim: systems that write persistent knowledge need governance controls, patch validation, and human review, "not because the technology fails, but because a wrong canonical concept page affects every answer... for as long as it stays wrong" (paraphrased from the article).

## Why it matters

Gives builders of document-grounded research and policy agents a concrete pattern for handling conflicting source evidence explicitly — surfacing contradictions with provenance and an owner, rather than letting a RAG pipeline silently pick one source over another — which is exactly the "demo to defensible" gap lens 8 is meant to track.

## Verification notes

Read via WebFetch of the full article (2026-08-17). The architecture description, the contradiction-object mechanism, scoped-rule and temporal-query behaviour, and the implementation stack are traced directly to the article text. This is the author's own design write-up of a system they report having built; there is no independent benchmark or third-party corroboration of its effectiveness, so verification is partial rather than full.

## Updates

None yet.

## Related entries

- [2026-shi-rag-typed-generation-contract](2026-shi-rag-typed-generation-contract.md) — same-project theme: RAG reliability engineering, this entry's "typed generation contract" concept complements the contradiction-object mechanism here.
- [2026-shi-rag-dispatcher-loop-control](2026-shi-rag-dispatcher-loop-control.md) — related: same author's series on RAG workflow control engineering.
- [2026-angela-shi-loop-engineering-pdf-outline-rag](2026-angela-shi-loop-engineering-pdf-outline-rag.md) — related: same "loop engineering" RAG series, document-structure recovery rather than knowledge persistence.
- [2026-kim-metamorphic-rag-testing](2026-kim-metamorphic-rag-testing.md) — related: testing methodology for RAG systems under source-content mutation, a validation counterpart to this article's contradiction-handling design.
