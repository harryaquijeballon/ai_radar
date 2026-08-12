---
slug: 2026-aguiar-tabular-foundation-models-economic-behaviour
title: "Tabular Foundation Models and the Unity of Economic Behaviour"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2608.06842
canonical_ids: ["arxiv:2608.06842"]
publisher_or_author: "Victor H. Aguiar — arXiv preprint"
published: 2026-08-07
captured: 2026-08-10
relevance:
  social_science: high
  ai_engineering: low
verification: verified
rationale: >-
  High on lens 6 (AI applied to social-science research): a concrete,
  evaluable test of whether a frozen tabular foundation model captures a
  single underlying "economic behaviour" space that transfers across risk,
  time, loss, valuation, and social-preference domains, with a placebo
  control (random reassignment) and a structural decomposition a researcher
  could reuse to audit their own model's predictions of economic behavior.
---

# Tabular Foundation Models and the Unity of Economic Behaviour

## Summary

Tests whether a unified framework can explain economic decision-making
across domains. The author ran a choice experiment in which participants
made decisions involving risk, time preferences, losses, valuation, and
social preferences, then used a frozen tabular foundation model to predict
each participant's hidden choices in one domain from their visible choices
in the other domains plus labeled data from other participants. The
foundation model "improves on the training-sample median," and this gain
disappears when choices are randomly reassigned (a placebo control ruling
out spurious fit). A single random-utility model estimated on the model's
learned representation retains most of the predictive improvement across
all domains. The paper decomposes the result into three components: a
learned common choice domain, one systematic utility function on that
domain, and one random component generating stochastic choice. 56 pages,
4 figures, 19 tables including appendix.

## Why it matters

Gives economists a tested methodology — not just an assumption — for
whether foundation-model representations of choice behavior are
economically meaningful and transferable across domains, plus a reusable
placebo-test template (random reassignment) for distinguishing genuine
cross-domain transfer from overfitting or leakage. Directly applicable to
anyone auditing a foundation-model-based prediction of economic behavior
before relying on it in applied work.

## Verification notes

arXiv abstract page fetched directly (2026-08-10); author (Victor H.
Aguiar), submission date (7 Aug 2026, 06:01:20 UTC, v1), and category
(econ.GN) confirmed. All claims in the Summary — the experimental design
(five preference domains), the training-sample-median improvement and its
disappearance under randomized placebo, the random-utility-model result,
and the three-component decomposition — trace directly to the fetched
abstract text. Author identity and research programme independently
corroborated via web search: Victor H. Aguiar is economics faculty with an
existing publication record on this exact research thread, including a
companion preprint from May 2026 ("Auditing and Fixing Economic Validity in
Tabular Foundation Models for Discrete Choice", arXiv:2605.26559, not in
this library), which confirms this is an active, credible line of work
rather than an isolated claim. Full paper PDF not read at capture.

## Updates

None yet.

## Related entries

None yet.
