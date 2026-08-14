---
slug: 2026-luo-autodesign-meta-harness-optimization
title: "AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.13560
canonical_ids: ["arxiv:2608.13560"]
publisher_or_author: "Yaxin Luo, Haobin Jiang, Jialv Zou, Xu Huang, Wenhao Yan, Haodong Li, Zhengrong Yue, Jing Li, Xiaofu Chen, Xiaohan Zhao, Jiacheng Liu, Jiacheng Cui, Zhiqiang Shen, Xiaotong Li — arXiv preprint"
published: 2026-08-14
captured: 2026-08-14
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Squarely on lens 2 (harness and context engineering): a meta-harness
  optimizer that has a code agent recursively improve its own harness based
  on rollout feedback, with quantified performance and cost figures and a
  named mechanism (learned "DesignHarness") a builder could apply.
verification: partial
---

# AutoDesign: Meta-Harness Optimization for Long-Horizon Agentic Design

## Summary

AutoDesign is a framework in which a meta-harness optimizer guides a code
agent to recursively improve its own operating harness based on feedback
from its own rollouts, aiming to align agent output with human design
priors. The authors instantiate this on paper-to-poster generation and
introduce PosterBench for evaluation. Reported results: AutoDesign scored
78.32 on PosterBench, 7.45 points above a "Claude Design" comparison system;
across seven configurations, adding the learned "DesignHarness" improved
average PosterBench score from 54.99 to 67.39 (+12.4%); the system executed
253 tool calls and 11 editing turns within 40 minutes for under $3; a
system-blind human evaluation rated AutoDesign's output as highest
preference among evaluated systems, reaching "average conference-poster
quality" fully autonomously.

## Why it matters

A concrete, cost-quantified demonstration that a code agent can improve its
own harness (not just its outputs) through rollout feedback, with a named,
reusable mechanism ("DesignHarness") and a measured before/after gain
(+12.4%) — directly actionable for teams building agent harnesses that need
to improve over repeated use (lens 2).

## Verification notes

Read via the arXiv abstract page only (cross-listed from cs.CV); full paper,
PosterBench task set, and the "Claude Design" comparison system's exact
configuration were not examined. Figures above as stated on the fetched
abstract page; not independently corroborated against a second source.

## Updates

None yet.

## Related entries

None yet.
