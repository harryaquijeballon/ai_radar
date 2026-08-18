---
slug: 2026-zhang-d2-scaleagent-long-document-rag
title: "D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.16417
canonical_ids: ["arxiv:2608.16417"]
publisher_or_author: "Hao Zhang, Longrong Yang, Lunhao Duan, Ziyang Wang, Qing-Guo Chen, Shanshan Zhao"
published: 2026-08-17
captured: 2026-08-18
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On lens 8 (document-grounded reliability): an adaptive
  retrieval/reasoning-scaling agent for long, visually complex documents,
  benchmarked on named long-document datasets — a usable pattern for
  document-heavy RAG products, though multi-modal-RAG-specific rather than
  general-purpose.
---

# D2-ScaleAgent: Dual-Dimensional Scaling for Long Document Understanding

## Summary

The paper addresses limitations in multi-modal RAG systems working over
long, visually complex documents. D2-ScaleAgent introduces a
"dual-dimensional scaling paradigm" for retrieval and reasoning: a Verifier
agent manages a dynamic evidence bank and adapts computation to query
difficulty — expanding retrieval (query decomposition, parallel page search
with pruning) when more information is needed, or engaging sub-agents of
varying sophistication for deeper analysis when required. The authors
report effectiveness on MMLongBench-Doc and LongDocURL (unverified in
detail — quantitative results tables not read beyond the abstract).

## Why it matters

Document-grounded research and policy products often involve long,
layout-heavy source documents (reports, filings, PDFs) where fixed
retrieval depth either wastes compute or misses evidence. The
adapt-to-difficulty pattern (cheap path for easy queries, deeper
decomposition and sub-agent analysis for hard ones) is a concrete design
lever for RAG systems handling that kind of source material.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The architecture
description (Verifier agent, dynamic evidence bank, query decomposition,
sub-agent tiering) and the named benchmarks are traced to the abstract.
Quantitative results and comparison to baselines were not independently
corroborated — hence partial verification.

## Updates

- **2026-08-18** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
