---
slug: 2025-dawid-agentic-workflows-economic-research
title: "Agentic Workflows for Economic Research: Design and Implementation"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2504.09736
canonical_ids: ["arxiv:2504.09736", "doi:10.48550/arXiv.2504.09736"]
publisher_or_author: "Herbert Dawid, Philipp Harting, Hankui Wang, Zhongli Wang, Jiachen Yi — arXiv preprint (econ.GN)"
published: 2025-04
captured: 2026-07-22
relevance:
  social_science: medium
  ai_engineering: high
verification: partial
license: "CC BY 4.0"
rationale: >-
  Cross-domain. AI engineering high: a concrete, implementable multi-agent
  architecture (named agent roles, structured communication, error escalation,
  HITL checkpoints, reproducibility agents, AutoGen implementation) squarely on
  the agent-orchestration and reliable-research-products lenses — and directly
  on the standing policy-simulation interest. Social science medium: a usable
  workflow blueprint for economics research on the AI-applied-to-research
  lens, but presented as design rather than validated empirical results.
---

# Agentic Workflows for Economic Research: Design and Implementation

## Summary

A methodology paper proposing agentic workflows that cover the full economic
research lifecycle — ideation, literature review, economic modeling, data
processing, empirical analysis, and result interpretation — with strategic
human oversight. The architecture defines dozens of specialized agents with
named roles per phase (e.g., ideation: TrendSurfer, ScholarSearcher, Ideator,
Refiner; literature: PaperDecomposer, GapFinder, CiteKeeper; data:
DataCleaner, ValidationSuite, ReproducibilityAgent; implementation: Coder,
Debugger, TestSuite, VersionManager), structured inter-agent communication
("structured Chain-of-Thought that mirrors the economic research workflow"),
and systematic error escalation — each agent resolves problems internally or
escalates (e.g., DataCleaner escalating structural breaks; a Proofreader
alerting humans on major deviations).

Human-in-the-loop checkpoints are integrated at defined stages: initial idea
review via a dashboard, iterative feedback with real-time annotation, quality
control, ethical oversight (privacy, bias, distributional implications), and
final approval. Hallucination risk is addressed with "specialized supervision
agents with conservative parameters" verifying citations and theoretical
interpretations, with human economists as final validators. Reproducibility
is a first-class concern: versioned preprocessing pipelines, complete
replication pathways from raw inputs to final datasets, reproducible model
packages. Implementation uses Microsoft's AutoGen framework, with four worked
examples (ideation team, automated literature review, model specification and
calibration, data processing); the paper motivates the gap with a survey
finding economics accounts for only 4 of 19 domain studies among 421 agentic
workflow papers reviewed. No quantitative performance results were identified
in the portions read (unverified — full case-study results sections could not
be completely retrieved).

## Why it matters

For the AI-engineering audience: one of the most complete public blueprints
for exactly the kind of system the radar's standing interest describes — a
multi-step agent pipeline for research whose outputs must be validated,
reproducible, and defensible. The named-role decomposition, escalation
pathways, verification-agent layer, and placed HITL checkpoints are
directly reusable design patterns for building research/policy agent
products, whatever the framework. For the social-science audience: a
citable framework for structuring AI-assisted economics research with
credibility controls — complementary to Korinek's hands-on guide, but
architecture-first rather than tool-first.

## Verification notes

Source reachable (arXiv abstract page and v1 HTML full text, fetched
2026-07-22). Bibliographic identity corroborated across both pages: arXiv
2504.09736, v1 2025-04-13, econ.GN, CC BY 4.0, five authors. Architecture,
agent roles, communication, escalation, HITL, and reproducibility claims all
traced to the paper's text. `partial` because the HTML retrieval truncated
before the four case-study results sections, so whether the examples carry
quantitative evaluation could not be confirmed — the "no quantitative
results" characterization is marked unverified above. Upgrade path: read the
full PDF's example sections and corroborate any reported results.

## Updates

None yet.

## Related entries

[2025-korinek-ai-agents-economic-research](2025-korinek-ai-agents-economic-research.md) — same space (agentic workflows for economics); Korinek is the practitioner on-ramp, this is the systematic architecture treatment.
