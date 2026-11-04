---
slug: 2026-talavera-eirinaki-interpretable-early-termination-web-agents
title: "Interpretable Early Termination of Web Navigation Agents via Closed Sequential Pattern Mining"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.04142
canonical_ids: ["arxiv:2611.04142"]
publisher_or_author: "Sergio Talavera, Magdalini Eirinaki"
published: 2026-11-03
captured: 2026-11-04
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on observability/debugging and evaluation/deterministic guardrails
  (lenses 4, 5): a human-reviewable, interpretable failure taxonomy for
  early-terminating failing web-navigation agent runs, with a clean
  evaluation protocol that removes contamination and quantified
  precision/token-savings figures.
verification: verified
---

# Interpretable Early Termination of Web Navigation Agents via Closed Sequential Pattern Mining

## Summary

Addresses the cost of web-navigation agents built on open-weight language
models that often fail late, after most of their tokens are already spent,
arguing that existing early-termination methods make opaque decisions that
offer little support for diagnosis or human oversight. The authors apply
closed sequential pattern mining (BIDE+) to the first K steps of agent
execution traces, producing a small, human-reviewable library of failure
signatures organized into a four-category failure taxonomy with repair
recommendations. Their evaluation protocol removes contamination — zero-step
crashes and trivially separable single-step successes — so measured accuracy
reflects genuine behavioral discrimination rather than easy cases. Tested on
1,544 MiniWoB++ traces from three open-weight models: at K=3, the
best-performing (Exclude-errors) configuration reaches F1 0.717, recovers
88% of test-set failures within the first three steps, and an
early-termination policy built on this saves 26.3% of tokens at 92%
precision.

## Why it matters

A concrete, interpretable (not black-box) mechanism for cutting the token
cost of agentic web-navigation pipelines by stopping doomed runs early,
with a human-reviewable failure taxonomy that supports diagnosis and repair
rather than just a termination score — directly transferable to any
long-running agent loop where most of the cost comes from runs that were
already going to fail.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-03). The method (BIDE+ pattern mining), the contamination-removal
protocol, the dataset (1,544 MiniWoB++ traces, three models), and the F1/
recovery/token-savings figures all trace to the abstract text. Full paper
(the four failure categories' definitions) not read at capture.

## Updates

None yet.

## Related entries

None yet.
