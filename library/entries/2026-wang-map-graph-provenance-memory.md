---
slug: 2026-wang-map-graph-provenance-memory
title: "MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.10509
canonical_ids: ["arxiv:2608.10509"]
publisher_or_author: "Yiqi Wang, Zihao Yan, Jiaqi Zhang, Zhangkai Wu, Mingkai Zheng, Zequn Sun, Yanming Zhu, Taotao Cai — arXiv preprint (cs.AI, cs.MA)"
published: 2026-08-11
captured: 2026-08-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance) and lens 2
  (harness/context engineering): addresses a concrete reliability gap in
  agent shared memory — summaries obscuring private, poisoned, untrusted,
  or revoked sources — with a typed provenance graph, permission-aware
  filtering, and quantified task-success/audit results.
---

# MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Workflows

## Summary
Shared memory lets LLM agents reuse information across long workflows, but relevant evidence may not be admissible for a particular agent or action — summaries can silently mix in private, poisoned, untrusted, or revoked sources. MAP-Graph represents agents, sources, memories, claims, and actions in a typed execution graph that traces ancestry and excludes permission-ineligible records, reranks eligible memories by semantic similarity and multiplicative path trust, and applies risk-sensitive gating before action execution while preserving lineage for audit. On 2,700 synthetic tasks across three domains, it reaches 94.96% overall task success, 72.70% exact decision accuracy, and 90.22% accuracy in clean settings requiring correct authorization decisions rather than just safe interventions.

## Why it matters
A concrete architectural pattern for making agent shared-memory systems auditable and permission-aware rather than treating stored context as uniformly trustworthy — directly relevant to any multi-agent research or policy pipeline where memory could otherwise leak private, stale, or compromised information across agents.

## Verification notes
Read via the arXiv abstract page. The task-success, decision-accuracy, and clean-setting accuracy figures are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
