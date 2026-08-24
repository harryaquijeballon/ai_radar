---
slug: 2026-lu-diagguard-trajectory-rca
title: "Beyond Fault Localization: A Trajectory-Level Study of LLM Agents for Microservice Root Cause Analysis"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.21310
canonical_ids: ["arxiv:2608.21310"]
publisher_or_author: "Qisheng Lu, Aoyang Fang, Junjielong Xu, Jin'ao Shang, Songhan Zhang, Yifan Yang, Xiaochuan Yan, Pinjia He — arXiv preprint (cs.SE)"
published: 2026-08-24
captured: 2026-08-24
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on lens 5 (observability and debugging): shows that endpoint
  correctness (did the agent name the right service) and diagnostic quality
  (did it reconstruct the actual fault-propagation path) are distinct and
  can diverge, then operationalizes the gap as a two-stage defense-in-depth
  architecture with a quantified, cross-setting validated improvement — a
  transferable lesson for any agentic verification pipeline, not just RCA.
verification: verified
---

# Beyond Fault Localization: A Trajectory-Level Study of LLM Agents for Microservice Root Cause Analysis

## Summary

Existing evaluations of LLM-agent root cause analysis (RCA) for microservices score only endpoint correctness — whether the agent names the responsible service — which does not reveal whether the agent's evidence and reasoning actually reconstruct the fault-propagation path an on-call engineer would need to trust the diagnosis. The authors instead evaluate 3,500 diagnostic trajectories against manually curated service-level fault-propagation paths on a public microservice RCA benchmark, characterizing where agents investigate and how they use retrieved telemetry. They find a disconnect: an agent can localize the correct fault source while still failing to reconstruct how it propagated. Successful investigations stay on the fault-impact surface, act on retrieved evidence, and broaden their queries as the search deepens; failures arise from omitted decisive evidence, misinterpreted evidence, or unsupported inference substituting for missing evidence. The authors operationalize this taxonomy as DiagGuard, a two-stage defense-in-depth architecture — a grounding stage that surveys available observations before localization, and a verification stage that audits the diagnosis against them. In an independent setting (different model, benchmark, and service topology), DiagGuard raises Acc@1 from 43.5% to 52.5%.

## Why it matters

The core finding — that answer correctness and diagnostic quality are separable, and that agents can be "right for the wrong reasons" — is a transferable warning for any agentic system whose output is judged only by a final answer, well beyond RCA. DiagGuard's grounding-then-verification pattern is a concrete, quantified architecture builders can adapt to make agent diagnoses auditable rather than just plausible, directly serving lens 5 and the profile's broader interest in deterministic guardrails around stochastic agent reasoning.

## Verification notes

Read via the arXiv abstract page, which gives the full methodology summary and quantified Acc@1 improvement. Not independently corroborated against a second source or the full paper.

## Updates

None yet.

## Related entries

None yet.
