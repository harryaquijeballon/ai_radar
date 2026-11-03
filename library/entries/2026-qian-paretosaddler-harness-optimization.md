---
slug: 2026-qian-paretosaddler-harness-optimization
title: "ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and Cost"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.02079
canonical_ids: ["arxiv:2611.02079"]
publisher_or_author: "Xingzhi Qian, Sungho Park, Rongyuan Tan, Jianbo Yu, Jue Zhang, Lorenzo Cavallaro, Menglin Xia, Yanzhi Chen, Xinnuo Xu, Yu Kang, Xinran Zheng, Gagan Somashekar, Xuchao Zhang, Chetan Bansal, Qingwei Lin, Victor Rühle"
published: 2026-11-01
captured: 2026-11-03
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on agent architecture and orchestration (lens 1): a harness
  (not model-weight) optimization method with a stated trade-off problem
  — optimizing for deployment cost mid-search can discard candidates that
  later improve — and a fix validated with quantified quality AND cost
  gains on two separate benchmarks.
---

# ParetoSaddler: Pareto-Guided Optimization of Agent Harnesses for Quality and Cost

## Summary

Harness optimization can improve LLM agents without retraining the model,
but existing methods optimize response quality alone. Adding cost to the
objective creates a problem: applying the deployment cost preference
during intermediate search steps can discard candidates that would later
lead to further improvements. ParetoSaddler separates promoting
intermediate candidates from making the final deployment choice: each
iteration compares a candidate against its parent over repeated runs and
uses Bayesian-bootstrap Pareto support to promote candidates with credible
gains in quality or cost; promoted candidates get broader evaluation and
can themselves become parents. On the ClawMark benchmark, quality rose
from 70.86% to 81.35% while cost fell from $1.17 to $1.01 per task; on
GAIA2, quality rose from 56.22% to 62.89% while cost fell from $0.78 to
$0.45 per task. Pareto-selected harnesses also beat quality-only
optimization on the quality-cost trade-off itself; the authors attribute
the gain to not discarding candidates that deployment preference alone
would reject, filtered by bootstrap screening to exclude weakly supported
gains (as stated in the fetched abstract; full search procedure and
ablations not reviewed at capture).

## Why it matters

A concrete, measured pattern for teams tuning an agent harness (prompts,
tool configuration, control flow) under both a quality bar and a cost
budget: optimizing for the final deployment trade-off at every
intermediate step is itself a trap that discards future improvements —
separating "what to keep exploring" from "what to deploy" produced
simultaneous quality and cost gains on two independent benchmarks, not a
quality-for-cost trade.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 1 Nov 2026, no revisions). The core design (decoupling
promotion from deployment choice via Bayesian-bootstrap Pareto support),
and the ClawMark/GAIA2 quality-and-cost figures, all trace to the fetched
abstract text, which is the paper's own stated summary of its results —
treated as `verified` on this library's convention for single-source
arXiv preprints whose headline figures are self-reported. The full paper
(search algorithm details, ablations, author affiliations) was not
reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
