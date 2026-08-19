---
slug: 2026-badshah-judge-retrieve-abstain
title: "Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.17994
canonical_ids: ["arxiv:2608.17994"]
publisher_or_author: "Sher Badshah, Ali Emami, Hassan Sajjad"
published: 2026-08-18
captured: 2026-08-19
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Squarely on lens 4 (LLM-as-judge validity, deterministic guardrails
  around a stochastic component): a risk-controlled framework with a
  finite-sample statistical guarantee on false-discovery rate for
  LLM-judged verdicts — exactly the kind of method that could make agent
  output trustworthy enough for research/policy use.
---

# Judge, Retrieve, or Abstain: Uncertainty-Guarded LLM Judging with Provable Risk Guarantees

## Summary

The paper addresses reliability problems when using LLMs as judges of
factual correctness. It proposes a risk-controlled framework that
"calibrates uncertainty thresholds on a held-out set so that the false
discovery rate among accepted verdicts remains below a user-specified
level." When the judge model's confidence is insufficient, the system
routes the instance to a retrieval-augmented stage that gathers external
evidence before re-evaluation, rather than either forcing a verdict or
discarding the case. The approach maintains a stated "finite-sample
guarantee" across both the direct-judging and retrieval-augmented modes,
and reportedly improves open-domain QA benchmark performance while
controlling error rates more effectively than single-mode alternatives
(unverified in detail — the calibration procedure and benchmark results
not read beyond the abstract).

## Why it matters

Most LLM-as-judge deployments have no statistical guarantee on how often
an accepted verdict is simply wrong. This gives judges a formal knob —
a user-specified false-discovery-rate ceiling, with an explicit abstain-or-
retrieve fallback rather than a forced binary call — directly applicable
to any evaluation or guardrail pipeline that currently uses an
LLM-as-judge without a calibrated error bound, the core lens for this
radar's policy-simulation-reliability interest.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The core
mechanism (calibrated uncertainty threshold, finite-sample FDR guarantee,
judge/retrieve/abstain routing) is traced to the abstract, including
direct quotes. The calibration procedure, benchmark selection, and
reported performance numbers were not independently corroborated — hence
partial verification.

## Updates

- **2026-08-19** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
