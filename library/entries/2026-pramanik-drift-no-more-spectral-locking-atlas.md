---
slug: 2026-pramanik-drift-no-more-spectral-locking-atlas
title: "Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.04315
canonical_ids: ["arxiv:2611.04315"]
publisher_or_author: "Vishal Pramanik, Maisha Maliha, Susmit Jha, Sumit Kumar Jha"
published: 2026-11-03
captured: 2026-11-04
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on harness/context engineering (lens 2): names a shared representational
  cause (hidden-state drift away from task/role/state anchor directions)
  behind three coupled long-horizon multi-agent failures, and proposes a
  training-free representation-level fix (ATLAS) with large, quantified gains
  over prompting/retrieval/memory/activation-steering baselines, transferring
  to a 72B backbone.
verification: verified
---

# Drift No More: Spectral Locking for Long-Horizon Open-Weight Multi-Agent AI

## Summary

Argues that long-horizon multi-agent systems suffer from three coupled
failures — task drift, role drift, and state staleness — that share a
single representational cause: agent hidden states drift away from the
directions encoding the active task, assigned role, and current shared
state. In a pilot study of 14,832 annotated turns, drifted turns collapsed
across all three anchor subspaces (pairwise r = 0.72-0.78). The authors
propose ATLAS, a training-free intervention that builds a positive
semidefinite anchor kernel over the task/role/state subspaces and steers
hidden states toward their shared high-coherence eigendirections before each
token is generated, using a low-rank Gram decomposition to keep computation
tractable — a representation-level controller for open-weight models,
complementing message-level methods for black-box agents. ATLAS outperforms
prompting, retrieval, memory, and activation-steering baselines across
memory, state-maintenance, tool-use, least-privilege-coordination, and
embodied stress tests: up to 5.7 points of memory macro-accuracy gain and
24.8-31.7% fewer read/write failures versus A-MEM; up to 4.8 points versus
MemoryArena-Agent; 10.7-12.1 points under perturbation; 93.5% role
consistency; and transfer to a 72B backbone (61.0 vs. 56.2 macro-average).
Ablating the joint task-role-state span costs 7.2 points versus 0.8 for a
random span of matched rank, and supplying the same information via prompt
or retrieval recovers 4.3 points less than the representation-level
intervention.

## Why it matters

For teams with access to open-weight model internals, a concrete,
training-free mechanism to correct the specific drift failures (task, role,
state) that degrade long-running multi-agent pipelines, with an ablation
showing the fix targets a functionally real, not incidental, representation
— and evidence that prompting or retrieval alone cannot fully substitute for
intervening at the representation level.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-03). The three-failure framing, the pilot-study correlation figures,
the ATLAS mechanism, and all quantified comparison figures trace to the
abstract text. Full paper (benchmark task definitions, full ablation table)
not read at capture.

## Updates

None yet.

## Related entries

[2026-maliha-atc-agent-trajectory-control-role-contracts](2026-maliha-atc-agent-trajectory-control-role-contracts.md) — a related message-level, black-box-compatible approach to the same class of long-horizon multi-agent drift problem.
