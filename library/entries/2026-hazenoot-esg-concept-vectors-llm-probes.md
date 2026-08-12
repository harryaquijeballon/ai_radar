---
slug: 2026-hazenoot-esg-concept-vectors-llm-probes
title: "Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.07208
canonical_ids: ["arxiv:2608.07208"]
publisher_or_author: "Luc Hazenoot, Zhaochun Ren, Amirhossein Zohrehvand — arXiv preprint"
published: 2026-08-07
captured: 2026-08-10
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  High on lens 5 (LLMs as research instruments — measurement, text-as-data):
  a linear probe on frozen LLM activations measures ESG concept presence
  within 0.6 percentage points of a fine-tuned classifier's accuracy without
  any fine-tuning — a directly usable, cheaper measurement instrument for
  any concept-in-text coding task. Medium on ai_engineering lens 4 as a
  transferable, framework-level technique for building lower-cost
  classifiers from frozen models rather than a production-ready guardrail.
---

# Measuring Concept Content in Text from LLM Activations: ESG Evidence from Concept Vectors and Linear Probes

## Summary

Tests whether "internal knowledge" accessed by monitoring frozen LLM
activations can substitute for task-specific fine-tuning when measuring
concept presence in text. Compares extraction methods — including the
Recursive Feature Machine algorithm and linear probing — against embedding
baselines and the model's own generated responses, on financial texts using
an annotated Environmental, Social and Governance (ESG) dataset. The best
linear probe comes within 0.6 percentage points of a fine-tuned domain
classifier's accuracy without fine-tuning, and outperforms the model's own
responses in most comparisons — evidence that LLM activations carry concept
information the model's generated text does not explicitly communicate.
19 pages, 1 figure, 7 tables.

## Why it matters

For social scientists doing text-as-data measurement: a cheaper, faster
instrument for coding a concept (ESG or otherwise) across a large corpus —
near-fine-tuned accuracy from a frozen model's internal activations,
without the cost of building and labeling a fine-tuning set. For AI
builders: a concrete, quantified data point on when a frozen-model
interpretability technique (linear probing) is a viable substitute for
fine-tuning inside a classification or guardrail pipeline.

## Verification notes

arXiv abstract page fetched directly (2026-08-10); authors, submission date
(7 Aug 2026, v1), and classification (cs.CL) confirmed. All claims in the
Summary — the methods compared, the ESG test domain, the 0.6-percentage-
point gap to the fine-tuned baseline, and the comparison against the
model's own responses — trace directly to the fetched abstract text. No
independent corroboration attempted (preprint, not yet peer reviewed). Full
paper PDF not read at capture.

## Updates

None yet.

## Related entries

None yet.
