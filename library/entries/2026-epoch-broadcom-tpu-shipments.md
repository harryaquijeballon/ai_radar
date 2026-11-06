---
slug: 2026-epoch-broadcom-tpu-shipments
title: "Broadcom TPU Compute Shipments Doubled from Q2 to Q3 2026, Reaching 2 Million H100-Equivalents"
status: accepted
domains: [social_science]
source_type: primary
source_url: https://epoch.ai/data-insights/tpu-production-doubling
canonical_ids: []
publisher_or_author: "Venkat Somala, Josh You — Epoch AI"
published: 2026-11-04
captured: 2026-11-06
relevance:
  social_science: high
  ai_engineering: n/a
verification: partial
rationale: >-
  Quantified, methodologically transparent estimate of AI compute
  infrastructure scale-up (lens 3: data/AI infrastructure as an economic
  input), with an explicit uncertainty model (90% CIs, scenario sensitivity
  on rack-vs-chip accounting) usable directly in AI-investment or
  compute-scaling analysis; no engineering-practice lesson for
  ai_engineering.
---

# Broadcom TPU Compute Shipments Doubled from Q2 to Q3 2026, Reaching 2 Million H100-Equivalents

## Summary

Epoch AI estimates Broadcom's TPU compute shipments roughly doubled from
fiscal Q2 to Q3 2026 (the quarter spanning May to early August), reaching a
median of ~1.97 million H100-equivalents (90% CI: 1.57M–2.35M), up from
961,591 H100e in Q2 — a jump outside the 2–22%-per-quarter growth seen in
the prior three quarters. Unit volume rose ~65% quarter-over-quarter to
roughly 800,000 chips; the larger compute jump reflects a mix shift to the
newer TPU v7 (2.5x the performance of TPU v6e) and the Q3 production start
of TPU v8i (2.2x TPU v7, ~11% of Q3 TPU compute). The estimate derives
chip volumes from Broadcom's reported AI semiconductor revenue ($16.7B in
Q3 FY26, of which custom accelerators were 73%/$12.2B, with a median 92% of
that attributed to TPUs, ~$11.2B) using a bill-of-materials per-chip price
model and converting compute to H100e via each chip's peak 8-bit FLOP/s.
Anthropic's share of TPU revenue is estimated at 30–50% (central ~40%),
inferred rather than disclosed, consistent with Broadcom's stated
commitment to deliver 1 GW of TPU compute to Anthropic in 2026.

## Why it matters

A transparent, uncertainty-quantified data point on how fast AI compute
infrastructure is actually scaling — useful as an input to any growth or
investment analysis that assumes a compute-supply trajectory for AI (lens
1), and as evidence for the "data/AI infrastructure as economic inputs"
lens (lens 3) on digital-technology economics. The explicit sensitivity
analysis (rack-vs-chip revenue booking could shift the estimate by
14–30%) models exactly the kind of assumption-transparency researchers
should demand before citing a compute-scaling figure.

## Verification notes

Fetched the primary Epoch AI page directly; every figure above (shipment
volumes, confidence intervals, revenue breakdown, customer-split
reasoning) is stated on the page with its own caveats, which are
preserved here: the rack-vs-chip accounting treatment is the largest
uncertainty source (Epoch assigns 25% probability to rack-value booking in
its central case); the Anthropic/Google revenue split is inferred, not
disclosed; the timing of Anthropic's within-year deliveries is unknown;
H100e is a peak-FLOP/s conversion that is most accurate for compute-bound
training workloads; and the estimate covers Broadcom's TPU shipments only
(excludes MediaTek, expected to ramp TPU production later). No
corroboration against an independent third-party estimate was attempted;
Broadcom's own earnings-call statements (cited on the page) are consistent
with the TPU v7 volume/mix story but do not independently quantify
shipments.

## Updates

None yet.

## Related entries

None yet.
