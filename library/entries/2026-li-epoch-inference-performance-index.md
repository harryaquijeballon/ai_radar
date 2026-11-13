---
slug: 2026-li-epoch-inference-performance-index
title: "Inference Performance Index: Changing the Way We Measure Inference Capacity"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://epoch.ai/publications/inference-performance-index
canonical_ids: []
publisher_or_author: "Jason Li — Epoch AI"
published: 2026-11-09
captured: 2026-11-13
relevance:
  social_science: high
  ai_engineering: high
verification: verified
rationale: >-
  High on ai_engineering lens 5 (cost and latency monitoring, transferable
  across frameworks) and high on social_science lens 3 (AI/data
  infrastructure as an economic input): a rigorously specified, externally
  validated metric for AI inference capacity per chip, directly usable for
  infrastructure cost/capacity planning and compute-economics analysis
  alike.
---

# Inference Performance Index: Changing the Way We Measure Inference Capacity

## Summary
Introduces the Inference Performance Index (IPI), a metric comparing AI
chips on inference capacity rather than raw compute (FLOP/s), on the
argument that memory bandwidth and inter-chip communication — not
arithmetic throughput — increasingly determine how many simultaneous users
or agents a chip can serve. Scores are expressed in GB300-equivalents
(GB300e; GB300 = 1): a score of 2 means a chip serves roughly twice as many
simultaneous requests as a GB300 at the same output speed, averaged across
four models (Kimi K3, GLM-5.2, Qwen3-Coder-480B, and a proxy for Microsoft's
MAI-Base-2) and output speeds from 50–400 tokens/s/request, modeled via
NVIDIA's AISimulate "speed of light" tool. Version 1 targets agentic
workloads specifically, citing that agentic API keys on OpenRouter consumed
roughly 7x as many tokens as human API keys as of late September 2026.
Headline scores: VR200 (Vera Rubin) 2.18, GB300 NVL72 1 (reference), B300
HGX 0.54, MI355X ~0.55, H200 HGX 0.12. The GB300 is estimated at ~25x the
H100's inference capacity per chip on modeled agentic workloads despite
only ~2.5x the H100's 8-bit FLOP/s; the report's own figure shows newer
chips reaching up to 72x the H100. Against independent SemiAnalysis
InferenceX measurements, GB300's predicted Kimi K3 throughput (at 50% of
modeled speed-of-light performance) tracked closely, with an average
absolute difference of about 12%.

## Why it matters
Gives anyone evaluating AI infrastructure costs — whether for a
compute-economics analysis or for planning an agentic product's unit
economics — a chip-comparison metric that corrects for the fact that
inference capacity, unlike training FLOP/s, depends heavily on memory
bandwidth and interconnect; the ~12% validation gap against independent
real-world throughput measurements gives the metric a stated, checkable
error bound rather than being purely model-based.

## Verification notes
Fetched directly from epoch.ai (allowlisted); author and 2026-11-09
publication date confirmed. The methodology (output-speed/concurrency
tradeoff, AISimulate modeling inputs, four-model scoring basket), the
headline chip scores, the GB300-vs-H100 comparison, and the SemiAnalysis
InferenceX validation figure (~12% average absolute difference) all trace
directly to the fetched report text — the latter is the one load-bearing
claim independently corroborated within the source itself (against a named
third-party measurement set), rather than solely self-reported modeling.
Full report (sensitivity-analysis appendix) not read at capture.

## Updates
None yet.

## Related entries
None yet.
