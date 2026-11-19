---
slug: 2026-epoch-agentic-inference-capacity-growth
title: "Agentic inference capacity grew 4.6x in a year, versus 2.6x for compute capacity"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://epoch.ai/data-insights/agentic-inference-capacity-growth
canonical_ids: []
publisher_or_author: "Jason Li — Epoch AI (Data Insight)"
published: 2026-11-18
captured: 2026-11-19
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 4/5 (independent capability/compute measurement;
  cost and latency context): an independent, methodologically transparent
  estimate of how fast agent-serving inference capacity is growing relative
  to raw compute — useful background for anyone forecasting agent-serving
  cost or capacity, but a capacity trend rather than a builder-actionable
  method or pattern.
---

# Agentic inference capacity grew 4.6x in a year, versus 2.6x for compute capacity

## Summary

Epoch AI estimates that the agentic inference capacity of AI chips sold to
date grew 4.6x between Q2 2025 and Q2 2026 (90% interval 4.2-5.1x), compared
with 2.6x growth in peak 8-bit compute (90% interval 2.5-2.7x) over the same
period — inference capacity per unit of peak compute rose about 77% over
the year. Capacity is measured with Epoch's Inference Performance Index
(IPI) v1, expressing performance in GB300-equivalents on fixed agentic
workloads with long cached contexts; per-chip IPI scores are multiplied by
cumulative chips sold in each category and summed, using Epoch's AI Chip
Sales dataset, with peak compute computed the same way for comparison. Most
of the gain is attributed to the Hopper-to-Blackwell transition, with
Blackwell and Blackwell Ultra accounting for 74% of added capacity.
Quarterly capacity additions in Q2 2026 were 3.3x those of Q2 2025 (fitted
annual growth in additions: 3.2x for inference vs. 2.1x for compute over
that period; fitted rates over Q1 2024-Q2 2026: 6.8x and 2.5x per year,
doubling times of 4.3 and 9.2 months respectively), so Epoch expects total
growth to slow even as inference capacity keeps outpacing peak compute.
Modeled inference capacity per GPU rose 8x from H200 to GB300 but only 2.2x
from GB300 to Vera Rubin VR200. Epoch notes its own modeling assumptions
(a 60/40 rack/server split; H100/H200 shipments split evenly from Q4 2024)
and that software efficiency gains are not modeled, so the stated
uncertainty intervals do not cover uncertainty in the underlying
performance model itself.

## Why it matters

For anyone forecasting the cost or availability of serving agentic
workloads at scale: an independent, non-vendor estimate that the capacity
available for agentic inference specifically is growing almost twice as
fast as raw compute capacity, with a named mechanism (the Hopper-to-
Blackwell transition) and a dated inflection (next-generation per-GPU gains
shrinking from 8x to 2.2x) — useful context for budgeting or capacity
planning, with the methodology and stated assumptions transparent enough
to audit rather than take on faith.

## Verification notes

Epoch AI data-insight page fetched directly (2026-11-19); author, "November
18, 2026" publication date, methodology (Inference Performance Index v1,
AI Chip Sales dataset), and all cited figures (4.6x/2.6x growth and their
90% intervals, the 74% Blackwell/Blackwell Ultra share, the 3.3x quarterly
figure, the 6.8x/2.5x fitted annual rates and 4.3/9.2-month doubling times,
the 77% capacity-per-compute rise, the 8x/2.2x per-GPU figures, and the
stated modeling assumptions and limitations) traced directly to the fetched
page text. No independent corroboration attempted beyond the publisher's
own stated methodology and assumptions (first-party Epoch AI dataset, no
secondary coverage found); Epoch AI is treated per profile as an
independent, non-vendor source rather than requiring the vendor-perspective
caveat applied to lab-published sources. No canonical identifier (DOI/
arXiv/repo) exists for this web page; dedup checked by URL only.

## Updates

None yet.

## Related entries

None yet.
