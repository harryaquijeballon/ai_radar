---
slug: 2026-zeng-how-ai-agents-waste-your-money
title: "How Do AI Agents Waste Your Money?"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07238
canonical_ids: ["arxiv:2611.07238"]
publisher_or_author: "Huimin Zeng, Yuxuan Lu, Jesse Cai, et al. (incl. Kai-Wei Chang)"
published: 2026-11-04
captured: 2026-11-06
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 5 (observability and debugging) and lens 4 (deterministic
  guardrails around stochastic components): a validated method for
  identifying and removing wasted reasoning tokens in agent trajectories
  with a large, verified removable fraction and a transferable
  judge-then-remove-and-replay validation protocol.
---

# How Do AI Agents Waste Your Money?

## Summary

The authors record and normalize full agent trajectories, use an
LLM-as-a-Judge to flag spans of reasoning that look removable, and map
flagged spans back to token counts. They validate each flagged span by
actually removing it, resuming execution, and checking whether the
outcome and later actions change. In online pruning experiments across two
agent benchmarks, this cut 41–46% of the model's reasoning tokens while
largely preserving task performance. The paper reports that waste varies
more by task and agent configuration than by the underlying model, and
that reasoning tokens and visible execution tokens show different waste
patterns from each other.

## Why it matters

Gives builders a concrete, validated (not just judge-estimated) method for
locating and removing wasted reasoning spend in agent trajectories —
directly actionable for cost/latency-sensitive deployments, including
agentic research or policy-simulation pipelines where reasoning-token
budgets scale with the number of agents and turns. The remove-and-replay
validation step (checking outcomes don't change after removal) is the
part that distinguishes this from a purely judge-estimated waste number,
making the 41–46% figure a stronger, more actionable claim than an
unvalidated LLM-judge assessment would be.

## Verification notes

Located via WebSearch (arXiv:2611.07238) after an initial arXiv-ID mix-up
with a same-week cs.MA paper; the abstract and key finding were confirmed
through the search result rather than a direct WebFetch of the abstract
page. The core quantified claim (41–46% reasoning-token reduction with
largely preserved task performance, validated by removal-and-replay) is
corroborated by the search summary's description of the paper's stated
method. Submission date (~2 days before this run, i.e. early Nov 2026) is
approximate; the full abstract page was not independently re-fetched to
confirm the exact day-level date or benchmark names.

## Updates

None yet.

## Related entries

None yet.
