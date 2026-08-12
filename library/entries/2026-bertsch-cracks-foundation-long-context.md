---
slug: 2026-bertsch-cracks-foundation-long-context
title: "Cracks in the Foundation: Seemingly Minor Architectural Choices Impact Long Context Extension"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.10296
canonical_ids: ["arxiv:2608.10296"]
publisher_or_author: "Amanda Bertsch, Luca Soldaini, Matthew R. Gormley, Graham Neubig, Hannaneh Hajishirzi, Kyle Lo, Dirk Groeneveld — arXiv preprint (cs.CL); accepted to COLM 2026"
published: 2026-08-10
captured: 2026-08-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 2 (harness and context engineering): a large, controlled
  ablation (170,000+ GPU hours, 26 released 7B models) isolating which
  transformer architectural choices compound to damage long-context
  performance — undetectable by short-context loss but costing up to 47%
  downstream — a directly actionable checklist for anyone building or
  selecting a long-context model for a research/policy pipeline.
---

# Cracks in the Foundation: Seemingly Minor Architectural Choices Impact Long Context Extension

## Summary
The paper isolates four architectural decisions found across the Olmo, Llama, and Qwen model families — normalization choice, grouped query attention (GQA), pretraining context length, and sliding window attention — and shows they compound: any one alone has a minor impact on long-context performance, but combining three or more can drop downstream long-context performance by up to 47%. Critically, these differences are undetectable through short-context loss metrics, meaning standard pretraining monitoring would miss them. The authors ran an extensive controlled study (170,000+ GPU hours) holding data and tokenizers constant while varying only these architectural factors, and released OlmPool, a collection of 26 comparable 7B models, plus an analysis linking specific architectural choices to attention-sink behavior. Some tested configurations outperformed Llama 3 on long-context extensibility.

## Why it matters
A concrete, evidence-based checklist of architectural choices that silently determine whether a model will hold up in long-context use (e.g. large document grounding, extended agent trajectories) — and a warning that short-context loss is not a sufficient proxy for catching these failures during pretraining or model selection. The released model pool (OlmPool) gives builders a controlled reference set instead of confounded off-the-shelf comparisons.

## Verification notes
Read via the arXiv abstract page. The GPU-hour count, model-release count, and the up-to-47% figure are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
