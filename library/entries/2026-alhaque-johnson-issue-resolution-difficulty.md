---
slug: 2026-alhaque-johnson-issue-resolution-difficulty
title: "What Makes Software Issue Resolution Tasks Difficult for Agents?"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.18280
canonical_ids: ["arxiv:2608.18280"]
publisher_or_author: "Ebtesam Al-Haque, Brittany Johnson — arXiv preprint (to appear, ESEM 2026)"
published: 2026-08-18
captured: 2026-08-20
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Clears lens 7 (AI-assisted software development) at high: a quantified
  predictive model (AUC 0.863) for coding-agent task difficulty from static
  task features, directly actionable for pre-estimating agent success and
  building difficulty-controlled benchmarks.
---

# What Makes Software Issue Resolution Tasks Difficult for Agents?

## Summary

A large-scale empirical study using CoderForge-Preview, described as the largest open dataset of coding-agent trajectories available, that extracts features from task patches, repositories, and prompts and evaluates their predictive power for agent task difficulty using ensemble methods and SHAP attribution analysis. The study reports an AUC of 0.863 predicting task difficulty from static features alone (unverified beyond the abstract), concluding difficulty is "substantially predictable" before an agent ever attempts the task. The two dominant difficulty drivers identified are patch fragmentation and repository scale; prompt linguistic features become predictive specifically in the mid-difficulty band, which the authors describe as a "layered structure of difficulty" (unverified). The paper concludes that issue-resolution difficulty is largely inherent to task structure, enabling pre-difficulty estimation and construction of difficulty-controlled benchmarks.

## Why it matters

For teams evaluating or deploying coding agents, a validated pre-execution difficulty predictor changes how issue queues can be triaged: tasks likely to fail can be routed to human review rather than burning agent budget, and benchmark builders can control for difficulty leakage (easy tasks disguised as hard ones or vice versa) when comparing agents. It also gives a concrete, measurable definition of "hard" for coding-agent tasks (patch fragmentation, repo scale) rather than relying on intuition.

## Verification notes

Fetched arXiv abstract page 2608.18280 (submitted 2026-08-18, to appear at ESEM 2026). Claims traced to the abstract/page summary: dataset name, method (ensemble + SHAP), the AUC 0.863 figure, and the two named difficulty drivers. Not independently corroborated against the full paper text or the CoderForge-Preview dataset itself — no secondary source cross-checked. The load-bearing AUC figure is stated directly on the source page, so verification is partial rather than unverified.

## Updates

<!-- Append-only, dated, newest last. Never rewrite the Summary. -->

## Related entries

None yet.
