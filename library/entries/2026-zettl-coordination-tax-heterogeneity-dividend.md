---
slug: 2026-zettl-coordination-tax-heterogeneity-dividend
title: "The Coordination Tax and the Heterogeneity Dividend: Break-Even Conditions for Multi-Agent LLM Pipelines"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.37700
canonical_ids: ["arxiv:2610.37700"]
publisher_or_author: "Andreas Zettl, Diego Gosmar — arXiv (cs.MA)"
published: 2026-10-25
captured: 2026-10-31
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Squarely on lens 1 (agent architecture trade-offs with stated evidence):
  a closed-form cost model and empirical break-even test for when
  multi-agent decomposition actually pays off versus a single strong-model
  call — directly actionable for anyone deciding whether to decompose a
  pipeline into roles.
verification: verified
---

# The Coordination Tax and the Heterogeneity Dividend: Break-Even Conditions for Multi-Agent LLM Pipelines

## Summary

Multi-agent LLM pipelines built on protocols such as Open Floor Protocol
(OFP) or A2A are usually justified by capability, with runtime cost
unmeasured; because each role can run a different model, comparing a
pipeline against a single-model call is hard to do fairly. The authors
propose a closed-form model weighing coordination costs (decomposition
overhead plus per-handoff protocol cost) against savings from routing work
to a cheaper model, deriving a break-even threshold and a feasibility bound.
Testing on 135 HumanEval/ClassEval tasks across six architectures (2,430
runs total) with Claude Opus 5.5 and Haiku 5.5 over OFP, each protocol
handoff adds about 7.2ms (roughly 0.11% of pipeline wall time) — protocol
overhead itself is negligible. Decomposition does not pay off in this
setting: a planner-coder-reviewer pipeline costs 3.22x a single strong call,
runs 3.24x slower, and solves no more tasks. Moving the planner and reviewer
to the cheaper model lowers cost to 0.39x but reduces pass@1 by 6.7 points,
and the authors' own break-even forecast misses the observed result by 19%.
The authors conclude the real savings come from choosing a model per task
rather than per role: an oracle that picks between the two single-model
calls solves 94.3% of runs at half the strong call's cost per solved task.

## Why it matters

A rare quantified, falsifiable test of when multi-agent decomposition is
worth its coordination overhead, with a direct and somewhat
counterintuitive finding — on this benchmark, per-task model routing beats
role decomposition — giving builders a concrete alternative to reach for
before adding planner/coder/reviewer-style agent splits.

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.37700, v1 submitted
25 Oct 2026, primary cs.MA, cross-listed cs.AI). The experimental setup (135
tasks, six architectures, 2,430 runs, Opus 5.5/Haiku 5.5 over OFP), the
7.2ms/0.11% handoff-overhead figure, the 3.22x/3.24x decomposition-cost
figures, the 6.7-point pass@1 drop, the 19% break-even forecast miss, and
the 94.3%-at-half-cost oracle result are all traced to the abstract text
itself. No independent corroboration of the raw run data was attempted.

## Updates

None yet.

## Related entries

None yet.
