---
slug: 2026-giri-trustworthy-rag-poison-detection
title: "Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.21095
canonical_ids: ["arxiv:2608.21095"]
publisher_or_author: "Balkrishna Giri, Md Toufique Hasan, Jussi Rasku, Muhammad Waseem, Pekka Abrahamsson — arXiv preprint (cs.SE)"
published: 2026-08-24
captured: 2026-08-24
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails) and
  lens 8 (reliable research and policy products): a middleware Evaluation
  Agent that checks RAG outputs for factual grounding and knowledge-poisoning
  before generation, with a named Trust Index formula and quantified
  detection performance across three LLMs — exactly the "trustworthy enough
  for research/policy use" pattern the profile's standing lens targets.
verification: verified
---

# Trustworthy RAG: An Evaluation Agent for Detecting Misinformation and Knowledge Poisoning in Generative AI Systems

## Summary

The paper addresses a specific RAG failure mode: high semantic relevance between a retrieved passage and a query does not guarantee factual truth, so similarity-based retrieval alone cannot catch knowledge poisoning or misinformation injected into a knowledge base. The authors build an Evaluation Agent middleware that combines Natural Language Inference (NLI) fact-checking, a five-signal poison detector, and a combined Trust Index formula to flag untrustworthy content before it reaches generation. On the TruthfulQA benchmark with Llama 3.3 70B, the system reaches 91% accuracy and 100% precision; instruction-injection attacks are detected with 100% recall; the Trust Index achieves ROC-AUC between 0.73 and 0.81 across three different LLMs; and a secure-coding use case reaches an F1 score of 92% for blocking unsafe instruction injection. The authors note the approach struggles with subtler attacks (entity swaps, semantic weakening) and that cross-dataset generalization required domain-specific calibration. Methodology, attack generator, and experimental artifacts were released publicly (unverified — release claim not independently checked).

## Why it matters

A concrete, evaluable architecture for the exact problem this profile's standing lens exists to solve: making RAG-grounded research and policy products defensible rather than merely plausible. The Trust Index and five-signal poison detector give builders a named mechanism (not just a warning) to insert between retrieval and generation, with quantified detection rates a team could use as a comparison baseline — while the reported failure modes (entity swaps, semantic weakening, calibration needs) are an honest scope boundary rather than an unqualified claim of solved RAG trust.

## Verification notes

Read via the arXiv abstract page. Quantified results (accuracy, precision, recall, ROC-AUC, F1) and stated limitations are as reported in the abstract; not independently corroborated against a second source or the full paper.

## Updates

None yet.

## Related entries

None yet.
