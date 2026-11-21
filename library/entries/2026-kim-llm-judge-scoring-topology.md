---
slug: 2026-kim-llm-judge-scoring-topology
title: "Same Judgement, Different Scores: Numerical Scoring Topology in LLM-as-a-Judge Evaluation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.26077
canonical_ids: ["arxiv:2611.26077"]
publisher_or_author: "Doyun Kim, Chanwoo Kim, Jiwoo Kum, Minsoo Song, Chanjun Park — arXiv preprint"
published: 2026-11-19
captured: 2026-11-21
relevance:
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails —
  LLM-as-judge validity): the first systematic study of how a scoring
  scheme's structure, not just its content, biases LLM-judge reliability,
  with a direct, actionable implication for anyone designing a judge rubric.
---

# Same Judgement, Different Scores: Numerical Scoring Topology in LLM-as-a-Judge Evaluation

## Summary

Defines "numerical scoring topology" — a scoring scheme's structure as
described by its scale width, granularity, offset, symmetry, and boundary
placement — and presents what the authors describe as the first
systematic study of how this topology affects zero-shot LLM-as-a-Judge
evaluation, tested across several benchmarks and judge models. Scoring
topology systematically affects judge scores, calibration, and robustness,
with the effect strongest on judgment-intensive tasks. Shifted and narrow
scoring ranges tend to cause the largest score deviations. Stronger,
larger judge models generally show higher discriminative validity and
greater robustness to topology changes, but are not immune to them. The
authors conclude that scoring topology should be treated as an integral,
controlled part of LLM-as-a-Judge evaluation design, and argue for more
standardized scoring protocols.

## Why it matters

For anyone building or relying on LLM-as-judge evaluation (a core
mechanism for this profile's eval/guardrail interest): direct evidence
that the *shape* of a scoring rubric — not just its wording — can move
judge scores and calibration, meaning two teams using differently-shaped
scales on the same rubric and model may get systematically different
verdicts. Actionable implication: fix and report scoring topology as part
of an eval's methodology, and prefer wider, less-shifted scales when
judgment is on the line.

## Verification notes

arXiv abstract page fetched 2026-11-21 (paraphrased summary; full abstract
text not reproduced verbatim due to tool quoting limits). Submission date
confirmed as 19 November 2026 (arXiv:2611.26077) — within this run's
discovery window (2026-11-20 → 2026-11-21) and the 7-day eligibility cap.
Core claims (topology affects scores/calibration/robustness; narrow/shifted
ranges worst; stronger models more robust but not immune) are traced to
the fetched summary; the specific benchmarks and judge models tested were
not individually enumerated at capture, so verification is partial. No
secondary coverage found (new preprint).

## Updates

None yet.

## Related entries

None yet.
