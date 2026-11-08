---
slug: 2026-zhan-airlock-multiagent-containment
title: "Airlock: Bounding the Multi-Agent Blast Radius via Selective Online Containment"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.06727
canonical_ids: ["arxiv:2611.06727"]
publisher_or_author: "Zhonghao Zhan, Javad Forough, Yefan Zhang, Krinos Li, Xiao Ma, Hamed Haddadi"
published: 2026-11-04
captured: 2026-11-08
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 5 (observability/debugging) and lens 6 (reproducibility,
  security, governance): a named runtime (Airlock) that contains the
  downstream effects of a faulty agent after an alert, with a provenance
  graph for forward/backward tracing and two containment tiers, evaluated
  at scale (1,832 testbed runs, 161 smart-home runs, 24,266 simulation
  records) against native A2A and LangGraph controls.
---

# Airlock: Bounding the Multi-Agent Blast Radius via Selective Online Containment

## Summary

Introduces Airlock, a runtime and guardrail for multi-agent systems that
contains the effects of a faulty agent's output once an alert fires.
Existing approaches either stop only the faulty agent (missing downstream
consumers that already acted on its output) or halt and roll back the
entire workflow (discarding healthy work). Airlock combines a
tree-structured runtime ("EdgeCitadel") that narrows permissions from
parent to child agents with an append-only provenance graph recording which
agents consumed which data. After an alert, it traces forward to isolate
tainted executions and pending actions, and backward to identify root
causes, then offers two containment tiers: a default full quarantine that
freezes affected branches, and an optimized cut that minimizes collateral
disruption under a deadline. Across 1,832 testbed runs, 161 smart-home LLM
runs, and 24,266 simulation records, Airlock blocked all post-alert faulty
actions in the main tests with no post-convergence leaks, while preserving
substantially more healthy work than native A2A and LangGraph controls.

## Why it matters

A concrete, named containment pattern for a problem every production
multi-agent deployment eventually faces — what to do with everything
downstream of an agent once it's known to be faulty — with a provenance
mechanism for both forward containment and backward root-cause tracing,
and a large-scale evaluation against two real frameworks (A2A, LangGraph)
rather than a toy baseline (lens 5, lens 6).

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 4 Nov 2026, no revisions). The EdgeCitadel/provenance-graph
design, the two containment tiers, and the evaluation scale and headline
result (all post-alert actions blocked, no post-convergence leaks, more
healthy work preserved than A2A/LangGraph controls) all trace to the
fetched abstract text — treated as `verified` per this library's standing
convention for single-source arXiv preprints whose headline claims are
self-reported. The full paper (exact A2A/LangGraph baseline configuration,
the "optimized cut" algorithm) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
