---
slug: 2026-amin-salminen-jansen-gender-sensitivity-llm-judges
title: "LLMs Cannot Be Neutral: Gender Sensitivity Across Candidates, Evaluators, and Models"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.02692
canonical_ids: ["arxiv:2611.02692"]
publisher_or_author: "Danial Amin, Joni Salminen, Bernard J. Jansen"
published: 2026-11-02
captured: 2026-11-03
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on evaluation/validation (lens 4): a large, controlled
  measurement (30,720 judgments across eight models) of gender-related
  bias in LLM-as-judge and decision-LM evaluators, with small but
  statistically significant effects and a usable comparison between judge
  types — useful calibration context rather than a technique a builder
  applies directly.
---

# LLMs Cannot Be Neutral: Gender Sensitivity Across Candidates, Evaluators, and Models

## Summary

Examines whether assigned gender for job candidates and for the evaluator
persona changes decisions made by LLM-as-a-Judge (LaJ) models versus
decision language models (DLMs). In a hypothetical city-council-vote
framing, eight models assessed 240 synthetic professional narratives (from
NVIDIA's US and French Nemotron-Personas datasets), producing 30,720
judgments. Explicitly stating a candidate's gender modestly raised the
probability of a "Yes" vote by about 1.05-1.73 percentage points versus
leaving gender unspecified; only a nonbinary evaluator assignment produced
a statistically significant increase (about 1.26 points), and matching
candidate and evaluator identities showed no significant overall
association. Yes-vote rates ranged from roughly 81% to 97% across models,
with 2.5%-3.3% of decisions reversing relative to the unspecified
baseline; when explicit gender identities were directly substituted, DLMs
reversed decisions less often than LaJ models (1.18% vs. 3.38%). The
authors conclude gender sensitivity depends jointly on candidate identity,
evaluator identity, and the specific model, and recommend examining
individual decision consistency alongside aggregate differences (as stated
in the fetched abstract; full per-model breakdowns not reviewed at
capture).

## Why it matters

Gives teams using LLMs as judges or automated decision-makers a
quantified, if modest, gender-sensitivity baseline and a concrete
methodological point: aggregate fairness metrics can look reassuring while
individual-decision reversal rates (2.5%-3.8% here) tell a different
story, and decision-LM framings reversed less often than pure LLM-as-judge
framings in this test — worth checking before assuming the two approaches
are interchangeable for evaluation pipelines sensitive to protected
attributes.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 2 Nov 2026, no revisions). The 30,720-judgment study design
(eight models, 240 synthetic narratives, city-council-vote framing), the
1.05-1.73pp candidate-gender effect, the nonbinary-evaluator significance
finding, the 81%-97% yes-vote range, the 2.5%-3.3% reversal rate, and the
1.18%-vs-3.38% DLM/LaJ reversal comparison all trace to the fetched
abstract text, which is the paper's own stated summary of its results —
treated as `verified` on this library's convention for single-source
arXiv preprints whose headline figures are self-reported. The full paper
(per-model tables, statistical tests, author affiliations) was not
reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
