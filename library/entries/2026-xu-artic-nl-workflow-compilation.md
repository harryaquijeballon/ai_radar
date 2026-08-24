---
slug: 2026-xu-artic-nl-workflow-compilation
title: "Natural-Language Workflows Are Not Software Yet: Artifact-Driven Compilation for Reliable Agent Execution"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.21341
canonical_ids: ["arxiv:2608.21341"]
publisher_or_author: "Xiangzhe Xu, Hanxi Guo, Guangyu Shen, Siyuan Cheng, Xiangyu Zhang — arXiv preprint (cs.SE)"
published: 2026-08-24
captured: 2026-08-24
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on lens 2 (harness and context engineering): names the specific
  reliability failure of natural-language agent workflows (implicit data
  dependencies) and proposes a compiler, Artic, that makes dependencies,
  constraints, and control transfers explicit before execution, with
  quantified gains in task resolution and cross-model/cross-run consistency
  on a sizeable real-world evaluation.
verification: verified
---

# Natural-Language Workflows Are Not Software Yet: Artifact-Driven Compilation for Reliable Agent Execution

## Summary

Natural-language workflow descriptions typically leave data dependencies between steps implicit, which the authors argue is a root cause of unreliable multi-step agent execution. They propose Artic, a compiler that transforms a natural-language workflow into an "artifact-driven" one: data declarations, constraints, and control transfers between steps become explicit rather than inferred, and the transformation is validated through decomposed checking and scenario-based testing. Evaluated on 488 problem instances drawn from 11 real-world domain workflows, Artic-compiled workflows improve task resolution rate by 28 percentage points over the original text workflows, increase consistency across different models by 32 percentage points, and increase consistency across repeated executions of the same workflow by 56 percentage points.

## Why it matters

A named, evaluable pattern for a problem every harness builder runs into: prompt-only workflow descriptions under-specify data flow, and agents fill the gaps inconsistently. Compiling to an artifact-driven representation before execution — rather than relying on ever-more-detailed prompting — is a concrete design choice with quantified payoff on both correctness and consistency, the latter being the harder-to-fix property in practice (a workflow that works today but not tomorrow, or on one model but not another, is difficult to debug from prompts alone).

## Verification notes

Read via the arXiv abstract page, which reports the evaluation scale (488 instances, 11 domains) and the three headline percentage-point gains directly. Not independently corroborated against a second source or the full paper.

## Updates

None yet.

## Related entries

None yet.
