---
slug: 2026-ghassabi-rag-conformity-bias-poisoned-claims
title: "Language Models Show Conformity Bias in RAG: When the Majority Endorses a Poisoned Claim"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.41012
canonical_ids: ["arxiv:2610.41012"]
publisher_or_author: "Mehrdad Ghassabi, Audrina Ebrahimi, Zahra Zojaji, Amin Milani Fard"
published: 2026-10-29
captured: 2026-11-02
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation, validation and deterministic guardrails (lens 4) and
  reliable research/policy products (lens 8): a controlled, quantified
  demonstration that a RAG model's misinformation-detection rate drops
  sharply (25% to 10% for the tested model) when poisoned documents form a
  retrieved majority rather than a minority, with a reported statistically
  significant swing (McNemar p = 6.04e-7). Directly actionable for anyone
  designing retrieval-grounded research or policy products: majority-vote
  or multi-document consensus in retrieved context is not a safe
  trust signal, and detection/guardrail design must account for
  retrieval-set composition, not just per-document checks.
---

# Language Models Show Conformity Bias in RAG: When the Majority Endorses a Poisoned Claim

## Summary

Tests whether a larger number of mutually agreeing poisoned (misleading)
retrieved documents weakens a language model's ability to detect
misinformation in a retrieval-augmented generation (RAG) setting. Using
200 randomly sampled SciFact questions, the authors compare two retrieval
conditions: one poisoned document alongside six healthy (non-misleading)
documents, versus six agreeing poisoned documents alongside one healthy
document. For the tested model (Gemma-3-12b), misinformation detection
drops from 25% (50 of 200 questions) under the minority-poisoned
condition to 10% (20 of 200) under the majority-poisoned condition. Of 38
questions whose detection outcome differs between the two conditions, 34
move from detected to undetected and 4 move the other way, a difference
the authors report as statistically significant (exact McNemar test,
p = 6.04e-7). The authors characterize the pattern as a "conformity-like
response": the model becomes much less likely to flag a poisoned claim
when it dominates the retrieved evidence, rather than being independently
checked against each document (all figures and framing as stated in the
fetched abstract; full prompt design and additional models/datasets, if
any, not reviewed at capture).

## Why it matters

A concrete, quantified counter-example to treating multi-document
agreement in a retrieval set as a trust signal: here, document-count
majority is exactly what defeats the model's own misinformation detection.
For anyone building RAG-grounded research or policy products — document
synthesis, literature review, or fact-checking pipelines — this names a
specific adversarial vector (seed the retrieval set with several mutually
agreeing poisoned documents rather than one) and a specific failure mode
(conformity, not simple per-document gullibility) that guardrail and
citation-verification design needs to test for directly, rather than
assuming per-document fact-checks compose safely.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-02; single version,
submitted 29 Oct 2026, no revisions, cs.CL primary category, no
cross-lists, CC BY-NC-ND 4.0). The experimental design (SciFact, 200
questions, 1-poisoned-vs-6-healthy compared to 6-poisoned-vs-1-healthy),
the 25%-to-10% detection-rate figures for Gemma-3-12b, the 38/34/4
breakdown, and the McNemar p-value all trace to the fetched abstract text
— the paper's own stated summary of its results — treated as `verified`
on the convention applied elsewhere in this library to single-source
arXiv preprints whose headline figures are self-reported experimental
output. The full paper (prompts, any additional models tested, dataset
construction detail) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
