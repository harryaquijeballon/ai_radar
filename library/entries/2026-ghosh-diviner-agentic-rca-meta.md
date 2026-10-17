---
slug: 2026-ghosh-diviner-agentic-rca-meta
title: "Diviner: Agentic Root-Cause Analysis with Human-Governed Adaptation for Large-Scale Infrastructure"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.21281
canonical_ids: ["arxiv:2610.21281"]
publisher_or_author: "Pradipta Ghosh, Gaurav Mitra, Shripad Nadgowda, Akshil Shah, Junyu Liu, Canturk Isci, Syamla Bandla, Xinyao Hu, Onkar Deshpande, Anik Dasgupta — Meta; arXiv preprint"
published: 2026-10-15
captured: 2026-10-17
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Medium on observability/debugging (lens 5) and reproducibility/governance
  (lens 6): a named production system (Meta) for agentic root-cause analysis
  with an explicit four-stage lifecycle (Encode/Execute/Evaluate/Adapt) that
  gates every knowledge update behind replay, quality checks, and
  human-owner approval. Architecturally concrete and transferable, but no
  quantified evaluation numbers available at the abstract level.
---

# Diviner: Agentic Root-Cause Analysis with Human-Governed Adaptation for Large-Scale Infrastructure

## Summary

Per the arXiv abstract page (v1 submitted 15 Oct 2026), the paper presents Diviner, an agentic root-cause-analysis (RCA) system operating at Meta, motivated by the observation that generic LLM agents with tool access struggle with RCA in large distributed systems because a single symptom can span services, data, configuration, compute, and organisational boundaries — leading agents to work from stale context, misread failed queries as absent symptoms, report unsupported system state, or overload observability services. Diviner is organised around four stages: **Encode** combines reviewed incidents and service-owner expertise into scoped, versioned skills, workflows, typed tools, and an incident knowledge graph; **Execute** uses an adaptive lead agent plus context-isolated worker agents to apply that knowledge to point-in-time evidence while maintaining evidence-linked hypotheses; **Evaluate** compares saved investigation trajectories against responder-reviewed outcomes on exact cause, useful direction, and groundedness; **Adapt** derives knowledge updates from recurring gaps and on-call feedback, admitting updates only after replay, quality checks, and owner approval. No numerical results, benchmarks, or evaluation figures are given in the abstract-level material reviewed; the abstract names the evaluation metrics (exact cause, useful direction, groundedness) without reporting values.

## Why it matters

A named, production-scale (Meta) architecture for a problem this profile tracks directly — turning an agentic debugging tool from a demo into something a human on-call team would actually trust — via a specific governance mechanism (every learned-knowledge update requires replay, automated quality checks, and human owner sign-off before it changes future behaviour) rather than continuous unsupervised self-improvement. The context-isolated-worker-under-an-adaptive-lead pattern for Execute is also a reusable orchestration shape independent of the RCA domain.

## Verification notes

Source reachable (arXiv abstract page). Claims traced to the abstract-level summary only; the full paper (which the abstract indicates contains the quantified evaluation results) was not opened, so no numerical claims are assessed here — this entry reports the architecture description only, which is fully traceable to the abstract as read.

## Updates

None yet.

## Related entries

None yet.
