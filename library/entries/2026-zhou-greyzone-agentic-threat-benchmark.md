---
slug: 2026-zhou-greyzone-agentic-threat-benchmark
title: "GreyZone: Production-quality Agentic Application Threats"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.09161
canonical_ids: ["arxiv:2611.09161"]
publisher_or_author: "Ruoyu Zhou, Shuyao Jiang, Haifeng Ruan, Abhik Roychoudhury"
published: 2026-11-06
captured: 2026-11-09
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Medium on reproducibility/security (lens 6): a new benchmark for
  evaluating automated red-teaming services against production-style agent
  applications, filling a stated gap in existing benchmarks (e.g.,
  AgentDojo) — on-lens and well-motivated, but the abstract reports only
  two preliminary case studies rather than broad validated results, so it
  is retained as early/framework-stage rather than high.
---

# GreyZone: Production-quality Agentic Application Threats

## Summary

Agents are increasingly deployed in coding, banking, and commerce, calling tools and changing application state — which makes security testing important for reliable deployment. The authors argue existing benchmarks poorly reflect production agent environments: where AgentDojo mainly tests how a subject agent behaves under attack, GreyZone instead tests whether an automated red-teaming *service* can generate and deliver attacks that cause verified security-policy violations.

The benchmark uses independently developed, open-source agent applications with explicit security boundaries around access permissions, confidentiality, and action authorization, exposing varied attack surfaces including multi-agent interactions and multimodal inputs; outcomes are independently verified. The authors present two preliminary case studies, using Promptfoo against Letta Code and Clawith, examining attack delivery, agent behavior, and verified outcomes, and release the benchmark including its subject agents and attack surfaces.

## Why it matters

Fills a specific, named gap — evaluating red-teaming *services* rather than agent robustness directly — relevant to anyone deploying agents with real state-changing tool access (banking, commerce, coding) who needs to know whether their automated security testing actually works, not just whether their agent survives a fixed attack set. Useful as a benchmark to watch rather than a validated result to cite yet.

## Verification notes

Fetched the arXiv abstract page directly; the benchmark's framing, scope, and the two named case studies (Letta Code, Clawith via Promptfoo) are as stated in the abstract. Verification is partial: the abstract itself frames the evaluation as "preliminary," with no broad quantified results yet (attack success rates, coverage statistics) beyond the two case studies — retained at medium/partial rather than high pending a fuller evaluation.

## Updates

None yet.

## Related entries

- [2026-hossain-channelguard-multiagent-safety](2026-hossain-channelguard-multiagent-safety.md) — related multi-agent security-composition concern, different angle (safe-component composition vs. red-team benchmarking).
- [2026-spence-sre-bench-reverse-engineering](2026-spence-sre-bench-reverse-engineering.md) — another recent agentic-security benchmark in this library, different domain (reverse engineering vs. production application threats).
