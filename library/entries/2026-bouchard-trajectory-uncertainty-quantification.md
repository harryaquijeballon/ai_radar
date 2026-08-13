---
slug: 2026-bouchard-trajectory-uncertainty-quantification
title: "Beyond Single-Turn Confidence: Trajectory-Adapted Uncertainty Quantification for LLM Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.11552
canonical_ids: ["arxiv:2608.11552"]
publisher_or_author: "Dylan Bouchard, Mohit Singh Chauhan — arXiv preprint (cs.CL)"
published: 2026-08-12
captured: 2026-08-13
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails):
  systematically re-tests three families of uncertainty-quantification
  method on multi-turn agent trajectories (not just single-turn outputs)
  across five LLMs and four datasets, with a clear practical ranking —
  directly usable guidance for anyone building confidence scoring into an
  agent evaluation or guardrail pipeline.
---

# Beyond Single-Turn Confidence: Trajectory-Adapted Uncertainty Quantification for LLM Agents

## Summary
Examines how uncertainty-quantification (UQ) methods designed for single-turn language-model outputs perform when applied to multi-turn agent trajectories. Tests three families — white-box scorers based on action-token probabilities, black-box consistency scorers based on resampled trajectories, and reflexive scorers based on model self-assessment — across five LLMs and four datasets. Transfer to trajectory-level evaluation shows mixed results: token-probability methods are sensitive to aggregation choices across turns; reflexive scoring offers strong baseline performance at low computational cost; black-box self-consistency methods typically rank highest overall, with trajectory-equivalence and action-set-consistency variants performing best. The authors conclude UQ methods require revalidation at the trajectory level, with careful attention to consistency measurement, aggregator choice, and compute budget.

## Why it matters
A practical ranking of which uncertainty-quantification approach to reach for when scoring confidence in multi-turn agent behavior rather than single model outputs — a core building block for any deterministic guardrail layered on top of an otherwise-stochastic agent, and a caution against assuming single-turn UQ methods transfer unchanged.

## Verification notes
Read via the arXiv abstract page (2026-08-13). The three UQ method families, the five-LLM/four-dataset test design, and the comparative findings (token-probability sensitivity, reflexive-scoring cost-effectiveness, black-box self-consistency's overall lead) are quoted/paraphrased directly from the abstract. Full paper (per-dataset numbers) not read at capture; findings not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
