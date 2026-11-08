---
slug: 2026-yang-reconmem-repository-dual-memory
title: "ReConMem: A Graph-Based Dual Memory System for Repository-Oriented Conversations"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07759
canonical_ids: ["arxiv:2611.07759"]
publisher_or_author: "Zhishuo Yang, Li Zhang, Yang Liu, Donghao Yang, Fang Liu"
published: 2026-11-05
captured: 2026-11-08
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 2 (harness and context engineering): a concrete memory
  architecture for multi-turn, repository-scale coding-agent conversations,
  with quantified gains over the strongest baseline on two benchmarks
  (LoCoEval, CodeAssistBench) rather than a single-benchmark demo.
---

# ReConMem: A Graph-Based Dual Memory System for Repository-Oriented Conversations

## Summary

Presents ReConMem, a graph-based memory system for LLM code assistants
working on software repositories across many conversational turns. It
stores distilled conversation memories and the code entities they
reference in linked semantic and structural graphs, keeping the
connections between them current as the conversation proceeds. Retrieval
combines natural-language and code-based search, expands results across
graph relations, and compresses code according to its structure. On
LoCoEval, it improves Pass@1 over the strongest baseline by about 7.9
points on single-hop and 7.3 points on multi-hop subsets, with similar
compression ratios. On CodeAssistBench, it reaches 27.61% Correct and
44.03% Partially Correct, beating a full-conversation-history baseline by
4.10 and 7.09 points respectively. The authors conclude that aligning
conversational memory with repository structure improves context
management for long-running coding-agent conversations.

## Why it matters

A concrete, quantified context/memory-engineering pattern for the common
production problem of a coding agent losing track of a long-running,
repository-scoped conversation — tested against the strongest available
baseline on two separate benchmarks rather than one convenient case (lens
2).

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 5 Nov 2026, no revisions). The architecture description and the
LoCoEval/CodeAssistBench figures all trace to the fetched abstract text —
treated as `verified` per this library's standing convention for
single-source arXiv preprints whose headline claims are self-reported. The
full paper (retrieval algorithm details, baseline configurations) was not
reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
