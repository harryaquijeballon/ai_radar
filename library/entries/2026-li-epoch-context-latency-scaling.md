---
slug: 2026-li-epoch-context-latency-scaling
title: "Latency Scaling Differences for GPT and Claude Models"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://epoch.ai/publications/long-context-latency-scaling-gpt-vs-claude
canonical_ids: []
publisher_or_author: "Jason Li — Epoch AI"
published: 2026-09-08
captured: 2026-09-09
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  An independent, methodologically transparent benchmark quantifying how
  time-to-first-token scales with context length across four frontier
  models — directly actionable for latency/cost design in long-context
  agent harnesses (lens 5: observability and cost/latency monitoring).
---

# Latency Scaling Differences for GPT and Claude Models

## Summary
Epoch AI measured time-to-first-token (TTFT) as a function of context length for four frontier models: GPT-5.6 Terra, GPT-5.6 Sol, Claude Sonnet 5, and Claude Opus 5. The method used shared-prefix caching (a ~2,051-2,052 token cached prefix), sequential requests spaced ~4 seconds apart, and reasoning/thinking disabled, across context lengths from roughly 50,000 to 900,000 tokens (72 requests for Terra, 30 for Sol, 112 for Sonnet, 48 for Opus). Student-t regression on TTFT found a statistically significant quadratic component for the GPT-5.6 models (quadratic coefficient γ = 8.027 for Terra, 10.416 for Sol) but not for Claude Sonnet 5 (γ = -0.206, no observable curvature) and only a small quadratic term for Claude Opus 5 (γ = 1.575). Extrapolated marginal TTFT per additional 10,000 tokens at a 10-million-token context: 1.66s (Terra) and 2.20s (Sol), versus a reported context-length-independent ~0.13s (Sonnet) and ~0.22s (Opus). Three separate estimators (Student-t regression, stochastic-frontier, and spike-plus-contention models) all confirmed quadratic curvature for the GPT models and near-linear behavior for the Claude models.

## Why it matters
Anyone designing a long-context or high-volume agent harness needs an empirical answer to "does per-token latency get worse as context grows, and by how much, for this specific model" — this report gives model-specific numbers rather than a general claim, directly informing model choice and context-budget design for latency-sensitive agent products (lens 5). It is also an independent (non-vendor) measurement, consistent with the profile's standing interest in labs like Epoch AI as a counterweight to vendor-reported benchmarks.

## Verification notes
Traced directly to Epoch AI's own report page, which states its methodology (request design, token ranges, per-model repetition counts) and reports full regression-coefficient tables and cross-checks across three separate estimators. This is a first-party, methodologically self-contained measurement (the report itself is the primary evidence for its own claims); no external corroboration was sought or is applicable here.

## Updates
None yet.

## Related entries
None yet.
