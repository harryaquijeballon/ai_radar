---
slug: 2026-rajan-factsgo-omission-taxonomy
title: "Where Facts Go Missing: A Layerwise Taxonomy and Per-Layer Attribution of Information Omission in Air-Gapped LLM Agent Pipelines"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.22448
canonical_ids: ["arxiv:2607.22448", "doi:10.48550/arXiv.2607.22448"]
publisher_or_author: "Santhiya Rajan — arXiv preprint (cs.MA)"
published: 2026-07-24
captured: 2026-07-27
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on the observability-and-debugging lens: a nine-layer taxonomy
  (L0-L8) and attribution methodology for a specific, named failure mode —
  silent omission of decision-critical facts in agent pipelines — validated
  on a 75,476-trial sweep across five models and two engines, with the
  headline finding that most omission (68%) originates in deterministic
  middleware rather than the model itself. Transferable across
  architectures and frameworks (the harness spans sliding-window-hybrid,
  full-attention, and SSM-hybrid models), and directly actionable: it
  relocates where operators should intervene.
---

# Where Facts Go Missing: A Layerwise Taxonomy and Per-Layer Attribution of Information Omission in Air-Gapped LLM Agent Pipelines

## Summary

Focused on air-gapped and on-premises LLM agent deployments in regulated
settings (clinical FHIR services, legal review, sovereign infrastructure)
that run quantized 4–8B models locally behind tool servers. The dominant
reliability failure identified is omission: the silent absence of a
decision-critical fact, e.g., an agent reading 20 of 400 records and
reporting "no anomalies." The paper argues omission is a pipeline
phenomenon, not a model phenomenon, and contributes: (1) a nine-layer
taxonomy (L0–L8) locating every omission mechanism from ingestion through
the agent loop; (2) an attribution methodology separating deterministic
layers (L0–L3) from behavioral layers (L4–L8) via controlled ablation and
logit decomposition, quantified with an "omission waterfall"; (3) an open
cross-architecture harness comparing sliding-window-hybrid, full-attention,
and SSM-hybrid models across engines and frameworks; (4) a
runtime-detection framework for air-gapped settings where the operator
controls the logits. Across a 75,476-trial sweep spanning five models and
two engines, the pooled omission rate was 0.62, with 68% originating in
deterministic middleware (L0–L3) rather than model behavior — relocating
where operators should intervene. Server-side profile factors (weight
quantization, KV-cache type, RoPE scaling) were held fixed and left for
future work.

## Why it matters

A directly usable diagnostic framework for anyone running local/air-gapped
agent pipelines in regulated contexts (exactly the kind of defensible
research/policy product this radar cares about): the taxonomy gives a
vocabulary for locating where an agent silently drops information, and the
"68% is deterministic middleware, not the model" finding tells operators
where to look first — logging and validation in ingestion/retrieval layers
before reaching for a bigger or better-aligned model.

## Verification notes

arXiv abstract page fetched directly (2026-07-27); title, authors,
"Submitted Fri, 24 Jul 2026 16:10:21 UTC" (single-author submission),
category (cs.MA) confirmed. Every claim in the Summary — the deployment
context, the omission definition, the four contributions, and the
75,476-trial pooled-rate and layer-attribution figures — traces directly
to the abstract text, the primary source for this pre-publication
preprint. Full paper text not read at capture, so the nine-layer taxonomy's
individual layer definitions and the omission-waterfall method are
unverified beyond the abstract's summary. Upgrade path: read the full PDF
for the L0–L8 taxonomy definitions and the runtime-detection framework.

## Updates

None yet.

## Related entries

None yet.
