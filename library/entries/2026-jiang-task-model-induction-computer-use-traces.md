---
slug: 2026-jiang-task-model-induction-computer-use-traces
title: "Inducing Task Models from Computer-Use Traces"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.20319
canonical_ids: ["arxiv:2608.20319"]
publisher_or_author: "Yucheng Jiang, Zora Zhiruo Wang, Ruishi Chen, Diyi Yang"
published: 2026-08-20
captured: 2026-08-21
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  A research-stage method for turning passively recorded computer-use traces
  into structured, auditable, reusable task models — on-lens for agent
  architecture (lens 1) and skill-library construction, quantified but not
  yet a drop-in tool.
---

# Inducing Task Models from Computer-Use Traces

## Summary

Introduces Task Model Induction (TMI), a method that extracts structured,
auditable, reusable task models — hierarchical goals plus procedural flow — from
passively recorded screen/action traces of computer use, including traces where
multiple activities are interleaved or run concurrently. The authors report 97.4%
agreement in recovering interleaved tasks against ground truth, roughly 75%
reconstruction accuracy of individual execution steps, and a 30% improvement in
held-out task accuracy when an agent is given skills derived from the induced task
models versus a baseline without them.

## Why it matters

Offers a candidate approach for building reusable agent "skill libraries" directly
from observed usage rather than hand-authored procedures — relevant to teams
exploring how agents can bootstrap task competence from passive traces, though the
method is presented at research/benchmark stage rather than as a production tool.

## Verification notes

Read directly from the arXiv abstract; the quantified figures (97.4% agreement,
~75% step reconstruction, 30% held-out accuracy gain) are traced to the source
text. No independent corroboration was possible — newly posted preprint (submitted
20 Aug 2026), no second source yet. Verification is `partial`.

## Updates

- **2026-08-21** — Entry created.

## Related entries

None yet.
