---
slug: 2026-anthropic-building-strong-safety-evaluations
title: "Building strong safety evaluations"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://www.anthropic.com/engineering/building-strong-safety-evaluations
canonical_ids: []
publisher_or_author: "Anthropic — Engineering blog"
published: 2026-11-13
captured: 2026-11-14
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Squarely lens 4 (evaluation, validation and deterministic guardrails) —
  the core lens for the policy-simulation interest. Names applicable
  mechanisms (construct validity over refusal-rate proxies, grader
  validation against human judgment via Cohen's kappa, preregistration,
  sample-size floors, paired comparisons) rather than general advice,
  drawn from Anthropic's own system-card evaluation practice.
---

# Building strong safety evaluations

## Summary

Anthropic's engineering blog lays out practices for building and interpreting
AI safety evaluations, framed as "safety evals measure propensity to cause
harm, not capability." Recommendations span team composition (methods +
domain experts), causal vs. observational design, construct validity
(refusal rate is often the wrong target — a model refusing everything scores
perfectly while being no safer), multi-turn simulation methodology (expert
writes a spec, a Claude model plays the user, the tested model responds, a
rubric-based grader scores the transcript), internal-validity controls
(contamination avoidance, shortcut-closing, order randomization), grader
design (atomic binary criteria, hidden metadata, cross-model grading,
position-bias checks, human-agreement validation via Cohen's kappa),
preregistration, sample-size floors (100 items for complex multi-turn evals,
1,000 for simple single-turn ones), and reporting practice (per-category
breakdowns, uncertainty intervals, full configuration documentation).

Quantified claims drawn directly from the post: single-turn harmless-response
rates of 94–98% on the API for recent models (near-saturated, now mainly a
regression check); a worked example where Opus 5 scored 98% and Opus 5.5
scored 94% on a romance-scam eval with the gap judged not statistically
significant; up to a 34-point gap in appropriate-response rate between the
raw API and claude.ai (system-prompted) for Claude Fable 5.1; and a targeted
system-prompt fix raising the claude.ai appropriate-response rate on
suicide/self-harm testing to 94% versus 60% on the API. (unverified: the
post's claim that evals are "often poorly documented" industry-wide is
asserted, not evidenced within the post itself.)

## Why it matters

Gives a builder of agentic research/policy products a concrete checklist for
making stochastic-system evaluation itself trustworthy: validate the grader
against human labels before trusting any score, report uncertainty rather
than a point estimate, and preregister what "better" means before running
the comparison. Directly transferable to any eval harness, not specific to
Anthropic's tooling (though it names its own stack — Inspect, Petri — as
examples).

## Verification notes

Fetched and read in full from the primary source (anthropic.com/engineering).
All quantitative claims above are quoted or closely paraphrased from the
post's own text; no external corroboration was sought for Anthropic's
internal eval statistics (a vendor reporting on its own practice — numbers
describe Anthropic's own evaluation pipeline, not an independently audited
benchmark). No load-bearing claim required independent corroboration beyond
the source text's own worked examples (e.g., the Opus 5 vs. 5.5 significance
test), which the post itself frames as a demonstration of correct practice
rather than a claim to be fact-checked elsewhere.

## Updates

None yet.

## Related entries

None yet.
