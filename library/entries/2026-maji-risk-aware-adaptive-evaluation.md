---
slug: 2026-maji-risk-aware-adaptive-evaluation
title: "Risk-Aware Adaptive Evaluation: Finding High-Impact Failures Under Limited Budgets"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2609.38914
canonical_ids: ["arxiv:2609.38914"]
publisher_or_author: "Priyanath Maji, Spandan Ghose Chowdhury — arXiv preprint"
published: 2026-09-30
captured: 2026-10-02
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
license: unknown
rationale: >-
  Lens 4 (evaluation design): allocates a limited agent-evaluation budget
  toward high-impact failures instead of uniform sampling, a method a builder
  can apply to eval suites for research and policy agents.
---

# Risk-Aware Adaptive Evaluation: Finding High-Impact Failures Under Limited Budgets

## Summary

The abstract frames evaluation of interactive agents under a constrained trial budget as a sequential allocation problem. Instead of spreading trials uniformly across scenarios, a risk-aware contextual Thompson Sampling policy uses scenario context, impact scores and observed failures to decide which scenarios to retest. Reported results: with 50 trials (6% of the available data) it recovered 86% of impact-weighted failures versus 25% for uniform allocation; it found 3.5x more impact-weighted failures at equal budget, 5x the discovery efficiency per dollar, and cut budget wasted on never-failing scenarios from 34% to 2.8%. The advantage shrinks as the budget approaches the corpus size. Accepted to the NeurIPS 2026 Workshop on Evaluation of Interactive Agents.

## Why it matters

Agent evals are expensive and failures are unevenly consequential. For policy-simulation agents, this offers a concrete way to spend a fixed run budget on the scenarios most likely to produce costly errors, while noting that the gain is largest when the budget is small relative to the scenario set.

## Verification notes

Read the arXiv abstract page (submitted 2026-09-30). Claims are traced to the abstract only; the full paper, datasets, impact-score definitions and code were not read, and the numbers are the authors' own, not independently reproduced. Licence not stated on the page. Preprint and workshop paper, not full peer review.

## Updates

- **2026-10-02** — Captured by the unattended daily scan.

## Related entries

None yet.
