---
slug: 2026-santos-vat-agent-decomposition-sizing
title: "Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.23395
canonical_ids: ["arxiv:2608.23395"]
publisher_or_author: "Pedro Santos — arXiv preprint"
published: 2026-08-24
captured: 2026-08-25
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on agent architecture and orchestration (lens 1): a controlled,
  quantified sweep of single- vs. multi-agent decomposition width (one to
  five specialized agents, 4,400 runs) with a stated, transferable
  heuristic (place partition boundaries at dependency-layer midpoints) and
  fault-injection evidence — a genuine architecture trade-off study, though
  demonstrated in one narrow application domain (cross-border VAT
  determination) and the pilot's own pre-registered success criteria were
  not met.
---

# Right-Sizing LLM-Agent Decomposition in VAT Determination: A Pilot Controlled Sweep

## Summary

A controlled pilot comparing how finely an LLM-agent system should be
decomposed, using cross-border VAT determination with reverse-charge rules
as the test domain. The author tests four orchestrated configurations —
from one broad agent to five specialized agents — across 4,400
experimental runs. Intermediate configurations achieved the highest
accuracy (0.830), though this fell short of the study's own pre-registered
success criteria; a single broad agent did not outperform all of the
decomposed variants. When token budgets were matched across
configurations, differences narrowed but still slightly favored
multi-agent setups. Under deliberate fault injection, wide-scope
(less-decomposed) systems proved more resilient, recovering baseline
performance by +0.160, while schema errors hurt the most fragmented
configurations the most. The paper's contribution is a "bounded,
preregistered pilot heuristic": place partition boundaries at
dependency-layer midpoints. All materials (oracle, dataset, harness,
traces, analysis pipeline) are released publicly.

## Why it matters

A rare controlled, quantified answer (rather than an opinion) to the
common agent-design question of how many specialized agents a workflow
should be split into: this pilot finds a middling decomposition wins on
accuracy but is more fragile under fault injection than a broader,
less-decomposed system, and offers a concrete rule of thumb (partition at
dependency-layer midpoints) plus full released materials for replication.
Framed around VAT determination, but the trade-off — accuracy vs.
fault-tolerance as a function of decomposition granularity — and the
methodology are transferable to other structured, rule-heavy agent
workflows.

## Verification notes

Fetched directly from the arXiv abstract page (2026-08-25); title, author
(Pedro Santos), and submission date (24 Aug 2026) confirmed. The four
tested configurations, the 4,400-run scale, the 0.830 peak accuracy
figure, the +0.160 fault-injection recovery figure, and the
dependency-layer-midpoint heuristic all trace directly to the fetched
abstract text — the author's own reported results, including the
explicit statement that pre-registered success criteria were not met.
Single-author preprint; no independent corroboration attempted. Full
paper (per-configuration results, fault-injection protocol) not read at
capture; upgrade path: read the full PDF and released materials.

## Updates

None yet.

## Related entries

None yet.
