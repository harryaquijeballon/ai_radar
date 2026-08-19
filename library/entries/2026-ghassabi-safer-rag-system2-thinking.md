---
slug: 2026-ghassabi-safer-rag-system2-thinking
title: "Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.17153
canonical_ids: ["arxiv:2608.17153"]
publisher_or_author: "Mehrdad Ghassabi"
published: 2026-08-17
captured: 2026-08-19
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On lens 4/6 (evaluation/guardrails, security): a refinement of a named
  prior defense (the Cordon Principle) against document-borne
  misinformation in RAG, with a stated metric for the detection-vs-influence
  gap — early-stage, single-author, not yet independently benchmarked at
  scale.
---

# Towards Safer RAG: Only Agents Capable of System 2 Thinking may Access Untrusted Documents

## Summary

The paper addresses RAG vulnerabilities where misinformation in retrieved
documents can corrupt model outputs. It proposes that "only agents capable
of deliberative System 2 reasoning may access untrusted documents,"
refining a prior "Cordon Principle" approach. The contribution includes
novel metrics measuring the gap between an agent *detecting* false
information and being *influenced* by it. Testing reasoning models against
standard language models reportedly shows deliberative reasoning
substantially improves robustness to corrupted evidence, without the
computational overhead of strict isolation methods (unverified in detail —
the metric definitions, model list, and quantified results not read beyond
the abstract).

## Why it matters

Names a specific, measurable failure mode in RAG safety — an agent can
correctly flag a document as false yet still be swayed by it — and
proposes routing untrusted-document access by reasoning capability rather
than blanket isolation. Relevant to any RAG pipeline handling
untrusted or adversarial sources, though the paper is early-stage and its
quantified claims were not accessible beyond the abstract summary.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The core
proposal (System-2-gated document access, refining the Cordon Principle)
and the detection-vs-influence-gap framing are traced to the abstract,
including a direct quote. No quantified results, benchmark names, or model
list were available in the fetched summary — hence partial verification;
a fuller read is needed before this could be corroborated further.

## Updates

- **2026-08-19** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
