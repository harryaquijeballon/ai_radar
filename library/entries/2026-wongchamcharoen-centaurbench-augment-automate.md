---
slug: 2026-wongchamcharoen-centaurbench-augment-automate
title: "CentaurBench: Benchmarking LLM Capabilities on Augmenting vs. Automating Real-World Work Tasks"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.18554
canonical_ids: ["arxiv:2608.18554"]
publisher_or_author: "Pattaraphon Kenny Wongchamcharoen, Kris Gulati, Min Min Fong, Abhishek Nagaraj"
published: 2026-08-19
captured: 2026-08-20
relevance:
  social_science: high
  ai_engineering: high
verification: partial
rationale: >-
  Squarely on lens 1 (AI's effects on growth and labour productivity: a
  quantified, task-based test of automation vs. augmentation, the framework
  anchoring this profile's growth lens) and on ai_engineering lens 4
  (evaluation/validation: a concrete, quantified study of LLM-as-judge
  reliability and benchmark-ranking instability). Cross-domain: high on both
  profiles.
---

# CentaurBench: Benchmarking LLM Capabilities on Augmenting vs. Automating Real-World Work Tasks

## Summary

The paper introduces CentaurBench, a framework that separately evaluates
frontier LLMs in two roles: autonomously completing work ("automation") and
assisting a weaker worker agent ("augmentation"). It tests 10 frontier
models across seven economically grounded, professional tasks (counseling,
market analysis, meal planning, operations research, tax preparation, travel
planning, tutoring), using blind pairwise comparisons by LLM judges against
task-specific rubrics, replicated across 10 independent runs (6,265 total
comparisons).

Headline finding: automation and augmentation rankings are only modestly
correlated (Spearman ρ = 0.48, p = 0.187), with wide task-level variation
(ρ ranging from -0.04 for travel planning to 0.85 for tax preparation); in 5
of 7 tasks the best automation model differs from the best augmentation
model. On the augmentation side, an unaided GPT-3.5-Turbo baseline worker
outranks every assisted condition on three of the seven tasks, and only
GPT-5-Mini's guidance beats the unaided baseline on average — the paper
states that guidance which is "overly complex, poorly matched to the
worker, or miscalibrated" can make outcomes worse than no assistance at
all. On evaluation reliability: inter-judge agreement across the 6,265
comparisons was 71.0% (74.5% in automation mode, 67.8% in augmentation
mode), and rubric-selected responses matched judge choices in 99.7% of
cases. The authors' core claim: "automation ability is an incomplete proxy
for assistance quality" — leaderboard rankings built from automation-mode
tasks do not reliably predict which model is best suited to an
assistive/co-pilot role.

## Why it matters

For social-science and economics readers: a rare, directly quantified test
of the automation-vs-augmentation distinction that anchors task-based
frameworks for AI and labour markets (the Acemoglu/Autor tradition) —
useful as an empirical anchor for arguments about which occupations or
tasks AI displaces versus assists, and a caution against inferring
labour-market impact from automation-only benchmarks.

For AI-engineering readers: a concrete, numeric caution against selecting
or evaluating models for co-pilot/assistive deployments using
automation-mode leaderboards — rankings do not transfer, and the paper's
own eval methodology (71% inter-judge agreement, task-specific rubrics,
10-run replication) is itself a usable template for benchmarking
assistance quality rather than raw task completion.

## Verification notes

Source fetched as full HTML paper text (arxiv.org/html/2608.18554), not
just the abstract. All headline figures in the Summary — the model count,
task list, correlation coefficients, inter-judge agreement rates, and the
direct quotes — are traced to that text. No independent second source
exists yet for this newly posted preprint (submitted 2026-08-19), so
load-bearing claims could not be externally corroborated — hence `partial`
verification per schema.md, not `verified`. No claim was found to be false
or unsupported by the source text.

## Updates

<!-- Append-only, dated, newest last. Never rewrite the Summary. -->

## Related entries

None yet.
