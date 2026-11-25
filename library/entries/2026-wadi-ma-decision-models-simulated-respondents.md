---
slug: 2026-wadi-ma-decision-models-simulated-respondents
title: "Training decision models for simulating human respondents"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.31613
canonical_ids: ["arxiv:2611.31613"]
publisher_or_author: "Davood Wadi, Yu Ma"
published: 2026-11-25
captured: 2026-11-25
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  Social-science lens 6 (AI applied to social-science research): directly
  on the credibility frontier of using LLMs as simulated survey
  respondents — quantified evidence that off-the-shelf models skew
  econometric results, and a trained-model fix with measured error
  reduction across four held-out studies. AI-engineering lens 4
  (evaluation/validation): a concrete training methodology (conditional
  maximum likelihood on respondent-level choice data) for improving
  synthetic-data fidelity, though narrowly scoped to survey simulation.
---

# Training decision models for simulating human respondents

## Summary

Wadi and Ma address a known problem with using LLMs as synthetic survey respondents in economics and marketing research: off-the-shelf models produce choice data that skews treatment-effect estimates, and this isn't fixed by using larger proprietary models or more reasoning effort. They train "System One" decision models on historical respondent-level choice data via conditional maximum likelihood, without using any data from the target study being simulated. Tested across three model scales and trained on two discrete-choice experiments, the approach reduced treatment-effect error by 22% to 89% on four held-out studies covering vaccines, nutrition labels, consumer rights, and AI. A small trained model outperformed a much larger off-the-shelf model on three of the four held-out studies. Training on a single study lowered overall cross-entropy but could worsen treatment-effect error specifically, and the authors frame their approach as a complement to, not a replacement for, post-inference calibration methods.

## Why it matters

For social-science readers: a direct, quantified intervention on the "homo silicus" validity problem — off-the-shelf LLM survey simulation is shown to be unreliable for treatment-effect estimation, and purpose-trained decision models measurably close much of that gap, with results that transfer to out-of-sample studies the model was never trained on.

For AI-engineering readers: a worked example of fixing a generative model's downstream statistical validity through targeted training on behavioral data rather than prompting or scaling, relevant to anyone building LLM-based synthetic-respondent or agent-simulation pipelines where calibration against real behavioral distributions matters.

## Verification notes

Fetched directly from arXiv; abstract and submission history (v1, 23 November 2026, appearing in the 25 November cs.CL and econ.GN listings — a one-day announcement lag consistent with routine processing, not evidence of prior circulation) confirmed on the page. Load-bearing figures (22%–89% error reduction; outperformance on three of four held-out studies) are as stated in the abstract; the training procedure and the four held-out studies' details were not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

None yet.
