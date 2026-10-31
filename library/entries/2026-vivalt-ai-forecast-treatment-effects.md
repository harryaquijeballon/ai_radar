---
slug: 2026-vivalt-ai-forecast-treatment-effects
title: "Can Artificial Intelligence Forecast Treatment Effects in Economics?"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2610.38883
canonical_ids: ["arxiv:2610.38883"]
publisher_or_author: "Eva Vivalt — arXiv (econ.GN)"
published: 2026-10-28
captured: 2026-10-31
relevance:
  social_science: high
  ai_engineering: n/a
verification: verified
rationale: >-
  Squarely on lens 5 (LLMs as research instruments, including validity
  problems) and lens 6 (AI applied to social-science research): a large,
  quantified test of LLM forecasting against real, previously-unreleased
  treatment effects, with the method and error metrics stated plainly enough
  to be cited or reused.
---

# Can Artificial Intelligence Forecast Treatment Effects in Economics?

## Summary

Eva Vivalt uses large language models to forecast the treatment effects of
studies pre-registered on the AEA RCT Registry and the Open Science
Framework, restricted to results first released in 2026 — after the models'
training-data cutoffs. The models first extract forecasting questions from
each pre-registration or pre-analysis plan; only questions that resolve in
the eventual published paper are used to score accuracy. Forecasts were
elicited for 889 treatment effects from 39 papers (673 effects from 33 papers
after screening), restricted to effects that could be standardized in
standard-deviation units. For the best-performing model, the median absolute
forecast error is 0.054 SD, the mean absolute error is 0.093 SD, and the MSE
is 0.0218. These forecasts substantially outperform naive benchmarks that
predict a zero effect or the mean effect of other papers from the same
period. The author concludes the forecasts could meaningfully inform policy
and research prioritization.

## Why it matters

Gives researchers a concrete, quantified benchmark for how well current LLMs
can forecast real experimental results sight-unseen — directly usable
evidence for lens 5's question of when LLM-generated forecasts are credible
enough to inform research triage, pre-analysis review, or policy
prioritization, rather than an aspirational claim about "AI for research."

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.38883, v1 submitted
28 Oct 2026). The headline numbers (889/673 effects, 39/33 papers, 0.054 SD
median error, 0.093 SD mean error, 0.0218 MSE) are traced to the abstract
text itself. No independent corroboration was attempted beyond the source
document; full-text methodology (model identity, question-extraction
procedure) was not independently re-derived.

## Updates

None yet.

## Related entries

None yet.
