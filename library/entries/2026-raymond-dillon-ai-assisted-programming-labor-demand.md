---
slug: 2026-raymond-dillon-ai-assisted-programming-labor-demand
title: "AI-Assisted Programming and Labor Demand"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.31083
canonical_ids: ["arxiv:2611.31083"]
publisher_or_author: "Lindsey Raymond, Eleanor Wiske Dillon"
published: 2026-11-23
captured: 2026-11-24
relevance:
  social_science: high
  ai_engineering: high
verification: verified
rationale: >-
  Cross-domain. Social science lens 1 (growth/productivity) and lens 4
  (labour-market evidence): a natural-experiment causal estimate of
  AI-coding-assistant adoption's effect on technical hiring, at firm scale
  (5,414 firms, ~38% of the U.S. programming workforce). AI-engineering lens
  7 (AI-assisted software development, measured results): quantifies how
  AI-assisted coding reshapes the demand for junior vs. senior technical
  roles, directly informing claims about coding agents' labour effects.
---

# AI-Assisted Programming and Labor Demand

## Summary

Raymond and Dillon study how GitHub Copilot's AI coding assistance affects demand for programming labor, using firm-level adoption data across 5,414 multinational firms that together account for about 38% of the U.S. programming workforce. Because early adopters differed systematically (already hiring more pre-launch, with larger, more technical, and older workforces), the authors identify causal effects using a natural experiment based on firms' predetermined software-procurement review cycles, isolating adoption timing that was induced by the review schedule rather than firms' own AI-adoption decisions.

One year after adoption induced by the procurement review, Copilot reduced quarterly technical hiring by 29% among the affected firms. There was no detectable effect on separations, total technical headcount, or vacancy duration — the effect operates through reduced hiring flow, not headcount cuts or faster attrition. The hiring slowdown was concentrated in junior technical roles involving the most hands-on coding. The authors conclude that AI coding assistance shifts labor demand toward more experienced workers and toward roles combining coding with broader design responsibility, rather than toward or away from technical work overall.

## Why it matters

For social-science readers: a causally identified (not merely correlational) estimate of an AI coding tool's effect on hiring, using a procurement-cycle instrument to address adoption-timing endogeneity — a methodologically strong input to the junior-labor-market-displacement debate, with a specific, falsifiable magnitude (29% fewer quarterly technical hires) concentrated in junior roles.

For AI-engineering readers: direct, large-sample evidence that AI-assisted coding tools measurably shift hiring away from junior, code-heavy roles toward more senior, design-oriented ones — relevant to anyone arguing about coding agents' effect on team composition and the junior-developer pipeline, and a useful counterpoint/complement to this library's existing single-firm (Anthropic-internal) evidence on coding-agent adoption.

## Verification notes

Fetched directly from arXiv; abstract, submission history (v1, 23 November 2026), and subject classification (econ.GN primary; cs.AI, cs.CY cross-listed) confirmed on the page. Load-bearing figures (29% hiring reduction, no effect on separations/headcount/vacancy duration, concentration in junior roles) are as stated in the abstract; the identification strategy (procurement-cycle instrument) and full firm-level data construction were not independently re-derived from the full paper text, only the abstract and metadata.

## Updates

None yet.

## Related entries

- [2026-wilmers-working-with-ai-enterprise-adoption](2026-wilmers-working-with-ai-enterprise-adoption.md) — complementary interview-based evidence (58 firms) on AI adoption's effects on hiring and contracting, including reduced technical hiring.
- [2026-wilmers-anthropic-employment-change](2026-wilmers-anthropic-employment-change.md) — single-firm (Anthropic-internal) evidence on coding-agent adoption and hiring-mix change.
