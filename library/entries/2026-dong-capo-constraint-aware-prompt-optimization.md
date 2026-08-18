---
slug: 2026-dong-capo-constraint-aware-prompt-optimization
title: "CAPO: Constraint-Aware Prompt Optimization for LLM Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.16068
canonical_ids: ["arxiv:2608.16068"]
publisher_or_author: "Victor Ye Dong, Reid Pryzant, Yi Liu, Jian Jiao"
published: 2026-08-17
captured: 2026-08-18
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Squarely on lens 2 (harness and context engineering): a method for
  optimizing agent system prompts under explicit operational constraints
  (tool use, efficiency, safety), with a named mechanism and a reported
  feasibility guarantee — practically usable for hardening agent prompts.
---

# CAPO: Constraint-Aware Prompt Optimization for LLM Agents

## Summary

The paper targets a practical deployment problem: LLM agents must satisfy
operational constraints (correct tool use, efficiency, safety compliance),
not just maximize task success. CAPO is described as a primal-dual method
combining pool-based prompt rewrites with adaptive constraint weighting to
optimize system prompts under explicit constraints. An extended variant,
DCAPO, trains a dedicated rewriter module while leaving the task agent
unchanged, and is reported to reach "a feasible prompt in every evaluated
domain" (unverified beyond the abstract). The authors also report
improved performance on agentic benchmarks and evaluate assistant-style
tasks with formatting and safety constraints, plus a theoretical analysis of
how discretization errors affect the optimization procedure.

## Why it matters

Most prompt-optimization work targets raw task accuracy; CAPO targets
constraint satisfaction directly, which is closer to what a production
agent needs (it must use tools correctly and stay within safety bounds, not
just complete the task). The primal-dual formulation and the "feasible
prompt in every domain" claim are a concrete pattern a builder could adapt
when hardening system prompts for constrained, tool-using agents.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The method
description (primal-dual optimization, pool-based rewrites, adaptive
constraint weighting, DCAPO's dedicated rewriter) and the "feasible prompt
in every evaluated domain" claim are traced to the abstract. Specific
benchmark results, constraint definitions, and the theoretical analysis
were not independently corroborated — hence partial verification.

## Updates

- **2026-08-18** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
