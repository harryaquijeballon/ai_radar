---
slug: 2026-quessada-vial-agentic-configuration-management
title: "Agentic Configuration Management (ACM): A Reference Configuration Model for Governed Agentic Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.11166
canonical_ids: ["arxiv:2608.11166"]
publisher_or_author: "Audrey Quessada-Vial (PwC) — arXiv preprint (cs.SE)"
published: 2026-08-11
captured: 2026-08-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance) and lens 1
  (agent architecture): a framework-independent governance model for
  agentic-system configuration (typed items, versioning, immutable
  revisions, dependency-aware impact analysis, runtime provenance) with a
  working implementation across three major agent frameworks and a
  quantified evaluation.
---

# Agentic Configuration Management (ACM): A Reference Configuration Model for Governed Agentic Systems

## Summary
Agentic systems increasingly combine heterogeneous agents, prompts, tools, models, skills, composite subsystems, policies, and execution workflows whose configurations evolve independently across frameworks and runtime environments. ACM proposes a framework-independent governance model: typed configuration items, versioning, immutable revisions, an explicit separation between configuration and runtime behavior, dependency-aware impact analysis, and runtime provenance tracking, all normalized into a canonical "Configuration Graph." A Python reference implementation supports LangGraph, CrewAI, and the OpenAI Agents SDK; the evaluation covers 27 governance scenarios and nine quantitative cases, reporting reproducible governance outcomes after projection across the three frameworks. Reference implementation and artifacts are on GitHub.

## Why it matters
A concrete, cross-framework governance model for a problem every team running multiple agent frameworks eventually hits: configuration drift, unclear provenance of why an agent behaves as it does, and no principled way to audit or roll back agentic-system changes. Directly usable as a reference pattern (with open implementation) rather than an abstract governance argument.

## Verification notes
Read via the arXiv abstract page. The scenario/case counts and the cross-framework reproducibility claim are quoted/paraphrased directly from the abstract; not independently corroborated against a second source. Single-author, PwC-affiliated preprint — treated as a substantive technical report (77 pages, formal appendices, open artifacts) rather than vendor marketing, but the affiliation is noted.

## Updates
None yet.

## Related entries
None yet.
