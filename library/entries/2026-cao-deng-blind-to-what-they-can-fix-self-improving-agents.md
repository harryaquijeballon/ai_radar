---
slug: 2026-cao-deng-blind-to-what-they-can-fix-self-improving-agents
title: "Blind to What They Can Fix: A Detection Gap in Self-Improving Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.29807
canonical_ids: ["arxiv:2611.29807"]
publisher_or_author: "Teng Cao, Yu Deng, Kristian Kersting"
published: 2026-11-23
captured: 2026-11-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Lens 4 (evaluation, validation and deterministic guardrails): quantifies
  a specific, named failure mode — self-written runtime checks that miss
  most environment-drift failures — and shows a simple external monitor
  closes most of the gap, arguing self-improvement evals should measure
  failure detection, not just task scores.
---

# Blind to What They Can Fix: A Detection Gap in Self-Improving Agents

## Summary

Cao, Deng, and Kersting examine whether AI agents that write and revise their own programs also produce runtime checks that can be trusted to catch future problems. Across five task domains and up to seven author models, the agents' self-written code reaches high task scores. However, when the environment changes after the fact, the runtime checks the agents wrote miss half or more of the resulting failures in four of the five domains — the checks simply don't examine the recorded relationships that would reveal the failure. A separate monitor built from records of normal runs catches most of these failures in three domains, and the agents usually repair the problem once alerted by that monitor. The authors argue that evaluations of self-improving agents should measure whether the system notices its own failures, not merely its task-completion scores.

## Why it matters

A specific, quantified counter-example to assuming that an agent capable of writing its own tests is thereby capable of catching its own future failures — the gap (checks miss ≥50% of drift-induced failures in 4/5 domains) and the fix (an external monitor using recorded run data, not the agent's own checks) are both concrete enough to apply directly when designing self-improvement or continuous-agent-maintenance systems.

## Verification notes

Fetched directly from arXiv; abstract and metadata confirmed (v1 submitted 22 November 2026, within the discovery window; primary category cs.AI, cross-listed cs.LG/cs.SE). All figures above are as stated in the abstract. The five task domains, the up-to-seven author models, and the external monitor's construction were not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

None yet.
