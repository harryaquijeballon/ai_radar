---
slug: 2026-liu-fairness-drift-property-assessment
title: "Fairness Drift: Assessing Algorithmic Fairness in a Moving Market"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2611.11783
canonical_ids: ["arxiv:2611.11783"]
publisher_or_author: "Meng Liu — arXiv preprint (econ.GN, q-fin.EC)"
published: 2026-11-09
captured: 2026-11-12
relevance:
  social_science: high
  ai_engineering: n/a
verification: verified
rationale: >-
  High on political science (lens 7, algorithmic government): a real-world
  difference-in-differences study of Cook County's switch to a
  gradient-boosted property-assessment model, showing that an algorithm's
  measured fairness effects depend on how long it has run since its last
  update relative to market movement — a methodological warning applicable
  to evaluating any deployed algorithmic-government system, not just this
  one.
---

# Fairness Drift: Assessing Algorithmic Fairness in a Moving Market

## Summary

Studies Cook County, Illinois's rollout of a gradient-boosted machine-learning
model (replacing older township regressions and manual adjustments) for
property tax assessment, phased in by region on a three-year cycle. Using
difference-in-differences, the author tests how the ratio of assessed value
to sale price varies with sale price and neighborhood minority share,
before and after the model's introduction. In Chicago (2021), the reform
"roughly halved the over-assessment of cheaper homes relative to pricier
ones," weakening the link between assessment accuracy and neighborhood
racial composition. In the suburbs (2022–2023), results diverged by
sub-region: in the North, prior values were already fairly accurate, so
little changed; in the South, cheaper neighborhoods had appreciated faster
while values stayed frozen between updates, which initially corrected the
distortion, but prices then stalled before reassessment, leaving the new
values too high where prices had risen — so accuracy did not improve
overall. The paper's central claim: "fairness... drifts with the market
between updates," so an algorithm's apparent fairness effect depends on when,
relative to its deployment and the market's movement, it is evaluated.

## Why it matters

Any assessment of an "algorithmic government" system — a model used for tax
assessment, benefits eligibility, risk scoring, or similar official
decisions — risks attributing to the algorithm itself a fairness
improvement or deterioration that is actually driven by how much the market
or underlying population has moved since the model's last update. This
gives policy evaluators and political scientists studying algorithmic
government a concrete methodological point: single-snapshot fairness
audits of a deployed algorithm need to account for time-since-update,
not just the model's design, before drawing conclusions — and a model that
looks fair (or unfair) in one evaluation window may not in the next.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.11783,
2026-11-12); title, sole author (Meng Liu), subject categories (econ.GN,
q-fin.EC), and submission date (9 Nov 2026) confirmed there. The summarized
findings and the quoted phrase ("Fairness thus drifts with the market
between updates") trace directly to the fetched abstract text — the
author's own stated results, not a secondary paraphrase. The PDF full text
was not machine-readable at capture (binary extraction failed), so the
detailed DiD coefficients beyond the abstract's qualitative description were
not independently checked — load-bearing claims here rest on the abstract
alone, not corroborated against a second source or the full paper body.
Upgrade path: re-attempt full-text extraction or confirm against a secondary
discussion of the paper in a future pass.

## Updates

None yet.

## Related entries

None yet.
