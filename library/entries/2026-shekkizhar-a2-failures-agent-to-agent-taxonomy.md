---
slug: 2026-shekkizhar-a2-failures-agent-to-agent-taxonomy
title: "Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.19342
canonical_ids: ["arxiv:2610.19342"]
publisher_or_author: "Sarath Shekkizhar, Prathyusha Jwalapuram, Zixuan Ke, Shafiq Joty et al. — arXiv preprint"
published: 2026-10-14
captured: 2026-10-16
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
license: "CC BY-SA 4.0"
rationale: >-
  AI-engineering lenses 1 and 4 (and 5): an empirical failure taxonomy for
  agent-to-agent systems with a released trace dataset, plus the argument that
  outcome scores hide verification and conduct failures.
---

# Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for Agent-to-Agent Systems with Private States

## Summary

Per the arXiv abstract page (v1 submitted 2026-10-14, revised 2026-10-15), the paper studies agent-to-agent (A2A) systems in which each agent acts for a different principal and holds information the others cannot see. The authors analyse more than 2,500 recorded runs across 488 scenarios in eight families (e.g. legal, CRM, security, commerce) and derive "A²-Failures", a taxonomy of 20 failure modes in four categories: discovery and delegation, grounding and record consistency, verification, and conduct and fidelity. Reported findings: whether agents find and interact with peers depends mainly on task phrasing rather than peer availability; agents do not independently check a peer's factual claims, so a system is only as reliable as its least reliable participant unless the protocol checks; and aggregate outcome scores miss coordination, verification and conduct failures, so A2A systems should be evaluated per agent against its own principal. Run logs are released at huggingface.co/datasets/a2a-salesforce/a2-failures.

## Why it matters

A concrete checklist of failure modes for anyone building multi-agent pipelines that cross trust boundaries, and a case for adding explicit verification steps and per-agent evaluation rather than relying on end-to-end task success. The released traces allow builders to test their own evaluators against labelled failures.

## Verification notes

Source reachable (arXiv abstract page). Claims traced to the abstract-level summary only; the full text and the Hugging Face dataset were not opened, and the counts and taxonomy were not independently corroborated.

## Updates

None yet.

## Related entries

- [2026-han-multi-agent-diagnostic-contracts](2026-han-multi-agent-diagnostic-contracts.md) — related multi-agent failure diagnosis.
