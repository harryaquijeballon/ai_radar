---
slug: 2026-akimitsu-llm-econ-exam-red-herring
title: "Wrong and More Confident: A Field Experiment on Language Models Taking a Graduate Economics Exam"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.23424
canonical_ids: ["arxiv:2607.23424"]
publisher_or_author: "Piyush Akimitsu — arXiv preprint"
published: 2026-07-26
captured: 2026-07-28
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  Cross-domain. Social science high: a concrete, evaluable test (60
  graduate-microeconomics problems, 38 models) of LLM reliability as a
  research/teaching instrument (lens 6), with a quantified, generalizable
  failure mode. AI engineering medium: a rigorous failure-mode finding
  (distractor-induced wrong-but-confident answers, undetectable without
  external verification) relevant to the evaluation and observability
  lenses, though it documents the problem rather than supplying a guardrail
  or fix.
---

# Wrong and More Confident: A Field Experiment on Language Models Taking a Graduate Economics Exam

## Summary

Tests how irrelevant information affects LLM reasoning on graduate-level
economics problems. The author inserts "red herrings" — extraneous,
irrelevant passages — into sixty problems drawn from the Graduate Economic
Reasoning Benchmark (GERB), then compares model performance on the clean
versus red-herring versions across 38 models. The red herring lowers the
probability of a correct answer by 12.3 percentage points, and the effect
holds across 37 of the 38 models tested, regardless of whether a model has
specialized reasoning capability or is open- or closed-weight. The more
striking finding concerns model self-assessment: when a red herring is
present, models rate the problem as *easier*, not harder, than the clean
version — even as they answer it incorrectly more often. Models produce
incorrect answers with coherent, confidently stated explanations, at
confidence levels comparable to their correct responses, making the errors
difficult to detect without independent verification of the answer itself.

## Why it matters

For the social-science audience: a concrete, quantified caution for anyone
using LLMs to grade, tutor, or reason through economics problems —
irrelevant context measurably degrades correctness while *increasing*
apparent ease and confidence, a failure mode that looks like competence.
For the AI-engineering audience: direct evidence for why confidence or
self-reported difficulty cannot substitute for independent verification in
any evaluation or guardrail design — a builder relying on a model's stated
confidence as a trust signal for downstream research or policy use should
treat this finding as a specific, measured reason not to.

## Verification notes

arXiv abstract page fetched directly (2026-07-28); title, author, "Submitted
on 26 Jul 2026" confirmed. Every claim in the Summary — the experimental
design (60 GERB problems, red-herring manipulation, 38 models), the 12.3
percentage-point effect and its near-universality (37/38 models), and the
self-rated-ease-versus-accuracy divergence — traces directly to the fetched
abstract text. Full paper text not read at capture; no independent
corroboration attempted (pre-publication preprint, single author). The
paper appeared on arXiv's econ.GN "recent" listing grouped under 2026-07-28
despite the abstract page's own "submitted" date of 2026-07-26 — a routine
announcement-lag discrepancy. Upgrade path: read the full PDF for the GERB
benchmark's provenance and the full per-model breakdown.

## Updates

None yet.

## Related entries

None yet.
