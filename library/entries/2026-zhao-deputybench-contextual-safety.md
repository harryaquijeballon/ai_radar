---
slug: 2026-zhao-deputybench-contextual-safety
title: "DEPUTYBENCH: Evaluating Contextual Safety in Enterprise Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.13355
canonical_ids: ["arxiv:2611.13355"]
publisher_or_author: "Hao Zhao, Minghao Lin — arXiv preprint (cs.SE)"
published: 2026-11-09
captured: 2026-11-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation and reproducibility-governance (lenses 4,
  6, the core lens for this profile's policy-simulation interest): an
  executable, expert-verified benchmark with quantified evidence that
  enterprise agents handle missing authorization evidence very differently
  from explicit non-permission — directly actionable for anyone building
  permission-gated or policy-constrained agent systems.
---

# DEPUTYBENCH: Evaluating Contextual Safety in Enterprise Agents

## Summary

Introduces DEPUTYBENCH, an executable benchmark testing whether enterprise
agents can tell whether an ordinary request is permitted by organizational
records and policies, while still completing legitimate work when it is.
The benchmark has 79 base items and 375 instances, testing agents under
paired permission contexts and graded evidence requirements. Pooled across
12 models: 88.0% safety and 79.1% paired success (correctly refusing when
unauthorized and completing when authorized). A controlled sub-study (28
derived tasks, six models) tested authorization-fact flips, evidence
masking, and irrelevant rewrites: restricted execution occurred in only
10.3% of cases with missing evidence, versus 3.5% with explicit
non-permission (a 6.8-point gap, 95% interval 1.9–13.0) — i.e., agents
treated "I can't confirm this is allowed" much more permissively than "this
is explicitly not allowed." Masked-condition executions concentrated
heavily (61 of 100) in four privacy tasks requiring complete cumulative
counts or person-specific consent. Two security experts manually verified
task ground truth over two weeks (though stage labels were LLM-generated),
and a scorer-validation pass raised correctly scored held-out
counterexamples from 178 to 266 of 284.

## Why it matters

A concrete, quantified warning for anyone building permission-gated
enterprise or policy-constrained agents: "high safety with available
evidence does not establish reliable stopping when permission cannot be
verified," as the authors put it. Agents in this benchmark were far more
likely to proceed under ambiguous/missing authorization evidence than
under explicit denial — exactly the failure mode that matters for
agentic systems (including research/policy simulation agents) operating
under incomplete organizational or regulatory information. The benchmark
itself is a reusable evaluation tool for testing this specific failure
mode before deployment.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.13355,
2026-11-12); title, authors (Hao Zhao, Minghao Lin), submission date (9
Nov 2026), and category (cs.SE) confirmed there. The benchmark design and
all quantified figures (item/instance counts, pooled safety/success rates,
the 10.3%/3.5% evidence-gap finding and its confidence interval,
concentration and scorer-validation figures) trace directly to the
fetched abstract text. Full paper (per-task breakdowns, the two-expert
verification protocol in detail) not read at capture — upgrade path
noted.

## Updates

None yet.

## Related entries

- [2026-zheng-agentic-autonomy-governance](2026-zheng-agentic-autonomy-governance.md) — related theme (permission/governance for agentic AI), distinct contribution: that entry is a governance framework separating capability from permission; this one is an executable benchmark quantifying where permission-checking actually fails.
