---
slug: 2026-ko-lodestar-entropy-polarizer-rag
title: "LODESTAR: Trustworthy Entropy Is Navigated, Not Merely Measured — Reinforced Polarizer Keeps a Frozen LLM from Being Confidently Misled by the Wrong Evidence"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.11922
canonical_ids: ["arxiv:2608.11922"]
publisher_or_author: "Po-Jen Ko, Che-Cheng Wu, Hung-Chun Hsu, Li-Yang Chang, Chuan-Ju Wang — arXiv preprint (cs.CL)"
published: 2026-08-13
captured: 2026-08-13
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails): a
  named, quantified failure mode in retrieval-augmented generation
  (misleading passages produce confidently wrong answers with deceptively
  low entropy) plus a lightweight, weight-preserving fix (a reinforced
  prompt "polarizer") with measured improvement — directly usable for
  hardening a RAG pipeline against confident hallucination.
---

# LODESTAR: Trustworthy Entropy Is Navigated, Not Merely Measured

## Summary
Predictive-distribution entropy is normally a strong selection rule in retrieval-augmented QA: across five QA benchmarks, keeping the candidate answer a frozen respondent LLM produces with lowest answer-token entropy lifts mean answer F1 from 0.4769 to 0.5148 over the retriever's top-ranked passage alone. But misleading passages cause confident-yet-incorrect responses, lowering entropy exactly where it looks most reliable. LODESTAR addresses this with a reinforcement-learned "polarizer" — a brief natural-language prompt addition that recalibrates uncertainty without modifying the frozen model's weights. It reaches mean F1 of 0.5339, exact match of 0.4136, and a GPT-4o judge score of 0.6435; ablations show the polarizer specifically reduces how often the respondent is misled by a misleading passage, from 30.3% to 26.0% of cases.

## Why it matters
Names and directly measures a specific, dangerous RAG failure mode — low entropy being mistaken for reliability when the underlying evidence is wrong — and offers a weight-preserving fix any team using entropy-based answer selection can apply without retraining or fine-tuning the base model. The 30.3%-to-26.0% reduction in misleading-passage-induced errors is a concrete number to benchmark a guardrail against.

## Verification notes
Read via the arXiv abstract page (2026-08-13). The entropy-selection baseline result (F1 0.4769 to 0.5148), the failure-mode description, the polarizer mechanism, and all reported metrics (F1 0.5339, EM 0.4136, judge score 0.6435, 30.3%-to-26.0% ablation) are quoted/paraphrased directly from the abstract. Full paper (benchmark list, training details) not read at capture; findings not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
