---
slug: 2026-chetty-fogel-katz-digital-twins-workforce-training
title: "Experimentally Validated Digital Twins: Evaluating Workforce Training Programs in the Age of Big Data"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2611.03938
canonical_ids: ["arxiv:2611.03938"]
publisher_or_author: "Raj Chetty, Jamie Fogel, Lawrence F. Katz, Kadeem Noray, Sonya Porter, James Reisinger"
published: 2026-11-02
captured: 2026-11-04
relevance:
  social_science: high
  ai_engineering: n/a
verification: verified
rationale: >-
  High on causal inference and empirical methods (lens 5): machine-learning
  counterfactual-earnings estimators built on near-universal U.S. tax records,
  validated directly against 37 randomized controlled trials rather than
  merely asserted to be unbiased — a usable, quantified method for program
  evaluation without requiring a new RCT for every program.
---

# Experimentally Validated Digital Twins: Evaluating Workforce Training Programs in the Age of Big Data

## Summary

Proposes using machine-learning models, trained on anonymized U.S. income-tax
records covering nearly all American adults from 1999-2025, to predict each
workforce-training participant's counterfactual earnings from prior work
history, demographics, and location — a "digital twin" standing in for the
untreated outcome a randomized control group would have shown. Rather than
assuming the resulting observational estimates are unbiased, the authors
estimate the distribution of that bias directly against 37 real RCTs. The
machine-learning estimates track the RCT estimates about as closely as the
RCTs track each other, and the method cuts root-mean-squared error by roughly
60% relative to prior parametric observational estimators. Applied outside
the experimental sample, estimated treatment effects vary substantially by
location and over time even for the same program, and programs that place
more participants into target-sector jobs show the largest, most persistent
earnings gains.

## Why it matters

A validated, scalable alternative to running a new RCT for every workforce
program and every site: once a bias distribution is estimated against a
sufficient set of real experiments, the same ML counterfactual approach can
be applied to the much larger population of programs that were never
randomized, with a stated error bound rather than an unexamined assumption of
unbiasedness. Directly usable by researchers and evaluators who need
site- or time-varying treatment-effect estimates (not just an average) from
large administrative data, and a concrete rebuttal to the view that
small-sample survey-based bias findings generalize to richer administrative
data.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-02). The dataset description, the "digital twin" ML-counterfactual
method, the validation design against 37 RCTs, the ~60% RMSE reduction
relative to parametric estimators, and the claims about effect heterogeneity
and target-sector placement all trace to the abstract text. The full paper
(exact RCT list, estimator specification, robustness checks) was not read at
capture; no figure in the abstract is flagged unverified because none is
stated with a precision beyond what the abstract itself supports.

## Updates

None yet.

## Related entries

None yet.
