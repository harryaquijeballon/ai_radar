---
slug: 2026-agarwal-token-spend-engineering-output
title: "The AI Era's Lines of Code? A Case Study on What an Engineer's Token Spend Measures"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.13396
canonical_ids: ["arxiv:2611.13396"]
publisher_or_author: "Shyam Agarwal, Olga Lvova, Agnia Sergeyuk, Anastasiia Serova, Timofey Bryksin, Thomas Zimmermann, Bogdan Vasilescu — arXiv preprint (cs.SE)"
published: 2026-11-10
captured: 2026-11-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on observability and debugging (lens 5): a large field study (404
  engineers, five weeks of agent token usage, 412-person survey) directly
  testing whether token spend — an increasingly common engineering metric
  — reflects engineering output, finding that it mostly does not; a
  concrete warning against over-indexing on a specific observability
  metric, with a practical recommendation (resource accounting, not
  output evaluation).
---

# The AI Era's Lines of Code? A Case Study on What an Engineer's Token Spend Measures

## Summary

Tests whether organizations' use of engineers' AI-coding-agent token spend
reflects their engineering output. The authors linked five weeks of agent
token usage to the commits of 404 JetBrains engineers and analyzed a survey
of 412 employees. Findings: spend varies mostly *between* engineers rather
than week to week, and the highest spenders stayed largely the same
engineer-to-engineer across the five weeks; spend is only weakly tied to
output — among weeks with similar commit counts, 90th-percentile spend was
39 to 240 times 10th-percentile spend; within an individual engineer,
doubling spend was associated with only about 10% more commits; available
work metrics explained just 38% of between-engineer spend variation and
13% of week-to-week variation within an engineer; and nearly nine in ten
agent evaluations by technical respondents involved non-coding tasks
(analysis, research, planning). The authors conclude token spend mainly
reflects how much engineers use agents across many kinds of work, not the
outcome or value of that work, and recommend using it at most for resource
accounting rather than as an output or productivity measure.

## Why it matters

A direct, evidence-based caution for any team instrumenting AI-agent
observability around token spend (cost dashboards, "agent productivity"
metrics, resource allocation decisions): this field study finds spend is a
weak, confounded signal of output, varying far more between engineers and
across non-coding tasks than with the amount of code produced. Teams
building observability around agentic coding tools (see also this
library's [2026-sepidband-flowplan-token-cost](2026-sepidband-flowplan-token-cost.md)
on reducing an agent's own token cost) should track task-and-outcome
evidence instead of treating token spend as a productivity proxy.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.13396,
2026-11-12); title, authors, submission date (10 Nov 2026), and category
(cs.SE) confirmed there. The study design (404 engineers, five weeks of
usage data, 412-person survey) and all quantified figures (39–240x spend
ratio, ~10% commit increase per spend doubling, 38%/13% variance
explained, ~90% non-coding evaluations) trace directly to the fetched
abstract text — the authors' own stated results, not a secondary
paraphrase. Full paper (regression specifications, survey instrument) not
read at capture — upgrade path noted for a future verification pass.

## Updates

None yet.

## Related entries

- [2026-sepidband-flowplan-token-cost](2026-sepidband-flowplan-token-cost.md) — related but distinct: this entry argues token spend is a weak proxy for engineering output; that entry is a technique for reducing an agent's own token cost without changing outcomes.
