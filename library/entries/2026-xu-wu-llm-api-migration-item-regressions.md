---
slug: 2026-xu-wu-llm-api-migration-item-regressions
title: "What Aggregate Scores Miss: Measuring Item-Level Regressions in Commercial LLM API Migrations"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.17719
canonical_ids: ["arxiv:2608.17719"]
publisher_or_author: "Xiaonan Xu, Wenjing Wu"
published: 2026-08-18
captured: 2026-08-19
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Squarely on lens 4 (evaluation and deterministic guardrails): a
  reproducible item-level auditing method for commercial LLM API version
  migrations, showing aggregate benchmark gains can mask a meaningful share
  of reliably regressed items — directly actionable for any team deciding
  whether to upgrade a production model.
---

# What Aggregate Scores Miss: Measuring Item-Level Regressions in Commercial LLM API Migrations

## Summary

The paper examines what aggregate benchmark scores overlook when
organizations migrate between commercial LLM API versions. The authors
analyzed three model upgrades in the GPT-5.4-to-GPT-5.6-Sol sequence,
testing 900 benchmark items fifty times each across three domains. Despite
overall aggregate gains (up to 7.3 percentage points), migrations
simultaneously contained items that reliably regressed — up to 8.3% of
items in some migrations. Items were classified as reliably improved,
reliably regressed, practically equivalent, or inconclusive. On an
instruction-following benchmark, "the gap between strict and loose scoring
widens by 3.9 percentage points on the latest migration," with a 3.9-point
decline under strict scoring shrinking to 0.04 points under loose scoring.
The authors released their response archives and per-item scoring data for
reproducibility (unverified in detail — full methodology and dataset not
read beyond the abstract).

## Why it matters

Teams that gate model upgrades on aggregate eval deltas alone can ship a
regression that aggregate scores hide entirely — this paper gives a
concrete, repeatable item-level classification method (reliably
improved/regressed/equivalent/inconclusive, run fifty times per item) for
catching that before a migration ships. Directly usable for any AI product
team's model-upgrade evaluation gate, the core lens for this radar's
policy-simulation-reliability interest.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The headline
findings (900 items x 50 runs, up to 8.3% reliably regressed items despite
aggregate gains, the 3.9pp strict-vs-loose scoring gap) are traced to the
abstract, including direct quotes. The full experimental protocol and the
released dataset itself were not independently corroborated — hence
partial verification.

## Updates

- **2026-08-19** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
