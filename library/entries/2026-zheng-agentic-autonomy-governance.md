---
slug: 2026-zheng-agentic-autonomy-governance
title: "Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.23438
canonical_ids: ["arxiv:2607.23438"]
publisher_or_author: "Haining Zheng, Qian Dong, Rodolfo K. Depena, Jonathan D. Bhatia, Feng Xiao, Peng Xu — arXiv preprint"
published: 2026-07-26
captured: 2026-07-28
relevance:
  ai_engineering: high
  social_science: n/a
verification: verified
rationale: >-
  High on the reproducibility/security/governance lens: a concrete control
  — separating Allowed Autonomy Level from Autonomous Capability Level
  across five named autonomy tiers, with control/reversibility/
  accountability shifts specified at each tier — demonstrated on a deployed
  enterprise agent, not governance commentary.
---

# Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels

## Summary

Introduces a governance framework that separates what an agentic AI system
can technically do from what it is permitted to do. The paper distinguishes
Allowed Autonomy Levels (AAL) — the degree of autonomy an agent is
authorized to exercise — from Autonomous Capability Levels (ACL), the
agent's technical abilities, on the grounds that conflating the two leads
either to over-restricting capable systems or under-restricting risky ones.
The framework structures autonomy across five levels: reactive execution,
decision support, supervised action, goal-directed autonomy, and delegated
operational authority, and specifies how control, reversibility, and
accountability shift as autonomy increases. The authors propose a
risk-aware process for assigning permissions and demonstrate it on a
deployed enterprise data-engineering agent, showing how a technically
high-capability system can be deliberately restricted to a lower autonomy
level based on an organization's risk tolerance and operational readiness.

## Why it matters

A concrete, deployable governance control for any team operating agents
with real capability beyond what current organizational trust or process
maturity should permit — directly usable when deciding how much autonomy
to grant an agent in a research or policy-simulation pipeline, independent
of how capable the underlying model actually is. The five-level structure
and the control/reversibility/accountability mapping give a shared
vocabulary for that decision instead of an ad hoc one.

## Verification notes

arXiv abstract page fetched directly (2026-07-28); title, full author
list, "Submitted on 26 Jul 2026" confirmed. Every claim in the Summary —
the AAL/ACL distinction, the five named autonomy levels, the
control/reversibility/accountability framing, and the deployed
enterprise-agent demonstration — traces directly to the fetched abstract
text. Full paper text not read at capture; no independent corroboration
attempted (pre-publication preprint). Upgrade path: read the full paper for
the risk-aware permission-assignment process and the enterprise case
study's specifics.

## Updates

None yet.

## Related entries

None yet.
