---
slug: 2026-das-legal-rag-hallucination-study
title: "How Much Do Legal RAG Systems Still Hallucinate?"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.14210
canonical_ids: ["arxiv:2608.14210"]
publisher_or_author: "Souvick Das, Sallam Abualhaija, Domenico Bianculli — arXiv preprint (cs.CL)"
published: 2026-08-14
captured: 2026-08-17
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails) and
  lens 8 (reliable research and policy products): a rigorous, multi-system,
  claim- and answer-level hallucination audit of eight legal RAG systems
  across two legal corpora, quantifying hallucination rates from under 10%
  to nearly half of responses, and validated against 142 independent
  legal-expert-authored questions — directly the kind of RAG-grounding rigor
  the policy-simulation interest needs.
---

# How Much Do Legal RAG Systems Still Hallucinate?

## Summary

The paper conducts "a fine-grained analysis of hallucination behavior in eight legal RAG systems across two legal corpora, the GDPR (in English) and a national civil law (in French)" (quoted from the abstract), using both claim-level and answer-level evaluation. It reports hallucination density and severity broken down by question category and user persona, and validates its findings on an independent set of 142 legal-expert-authored questions. Headline finding: "hallucinations remain pervasive, ranging from less than 10% of responses for the best-performing systems to nearly half in the worst case" (quoted). The study further finds that false-premise questions — those containing incorrect assumptions that must be rejected rather than answered — produce especially high hallucination rates on the manually-drafted question set. The identities of the eight specific RAG systems tested and the exact per-system breakdown are not given in the abstract itself (unverified beyond the abstract's own description).

## Why it matters

Gives builders of document-grounded research and policy products a concrete, adversarially-validated method (claim-level + answer-level evaluation, including deliberately false-premise questions) for auditing how much a RAG pipeline actually hallucinates in a high-stakes domain — directly transferable to auditing any RAG system meant to ground research or policy claims in source text, which is the central concern of lens 8 and the profile's core lens 4.

## Verification notes

Read via the arXiv abstract page (2026-08-17); the full verbatim abstract was quoted. The headline hallucination-rate range (<10% to ~50%) and the false-premise-question finding are quoted directly from the abstract. The identities of the eight tested systems, the exact per-system numbers, and the full evaluation methodology were not read in this pass, so the study's overall framing is traced to the source but not independently corroborated beyond it — hence partial verification.

## Updates

None yet.

## Related entries

- [2026-shi-rag-typed-generation-contract](2026-shi-rag-typed-generation-contract.md) — related: a typed-generation-contract approach to preventing RAG hallucination, a design-side counterpart to this paper's measurement-side audit.
- [2026-kim-metamorphic-rag-testing](2026-kim-metamorphic-rag-testing.md) — related: metamorphic testing methodology for RAG systems, another rigorous evaluation approach to the same underlying problem.
