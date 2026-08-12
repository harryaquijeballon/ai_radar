---
slug: 2026-crescitelli-verification-cost-ai-evaluation
title: "AI Evaluation Should Measure Verification Cost, Not Correctness Alone"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.08709
canonical_ids: ["arxiv:2608.08709"]
publisher_or_author: "Viviana Crescitelli, Generoso Immediato, Fabio Persia, Stefania Costantini — arXiv preprint (cs.SE)"
published: 2026-08-09
captured: 2026-08-11
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4, the profile's stated core lens for the policy-simulation
  interest — evaluation validity: argues correctness metrics alone mask a
  distinct failure mode (errors a verifier cannot catch within a realistic
  verification budget), with empirical evidence across two domains that
  high benchmark accuracy can hide large real-world verification effort.
---

# AI Evaluation Should Measure Verification Cost, Not Correctness Alone

## Summary
The paper introduces Verification-Cost Errors (VCEs): mistakes that a verifier cannot identify within the verification budget available in a given deployment context. It argues that standard correctness-based evaluation metrics overlook this operational dimension, and that plausibility or authoritative-sounding presentation can itself contribute to verification failures — a model can be wrong in ways that are specifically hard, not just possible, to catch. Empirical evidence from two domains — code generation and multi-modal document understanding — shows that high benchmark accuracy can mask significant verification effort in practice.

## Why it matters
Close to a direct statement of the case for verification-aware evaluation of research/policy AI products: correctness alone is an insufficient reliability metric if the errors that remain are specifically the ones humans (or automated verifiers) struggle to catch within realistic effort budgets. Any evaluation harness built for a research or policy product with human review in the loop should budget for this — high headline accuracy is not evidence that a review step will actually be affordable.

## Verification notes
Read via the arXiv abstract page. The VCE definition and the two-domain empirical claim are quoted/paraphrased directly from the abstract; the abstract portion fetched did not include the underlying numeric results, so the empirical claim is recorded as stated but its magnitude is not independently quantified here — flagged as a gap for a follow-up read of the full paper if this framework is cited further.

## Updates
None yet.

## Related entries
None yet.
