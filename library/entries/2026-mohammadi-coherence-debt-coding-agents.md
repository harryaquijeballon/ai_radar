---
slug: 2026-mohammadi-coherence-debt-coding-agents
title: "The Working Set of a Coding Agent: Coherence Debt in Repository-Scale Tasks"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.16630
canonical_ids: ["arxiv:2608.16630"]
publisher_or_author: "Bardia Mohammadi, Lars Klein, Aman Chadha, Akhil Arora, Laurent Bindschaedler"
published: 2026-08-17
captured: 2026-08-18
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Squarely on lens 2 (context engineering): a controlled ablation across
  seven models and five harnesses isolating which information channels
  coding agents actually need, with quantified, actionable findings (up to
  10x token-cost differences, systematic fabrication when facts are
  missing) — directly usable for harness and context design.
---

# The Working Set of a Coding Agent: Coherence Debt in Repository-Scale Tasks

## Summary

The paper studies how AI coding agents maintain consistency across
large codebases within limited context windows, modeling the problem as
reconstructing a "coupled-fact graph." The authors tested seven models
across five different agent harnesses, systematically withholding
information channels to measure impact. Reported findings: agents cannot
complete unfamiliar-API tasks without the essential facts; parametric
memory sometimes substitutes for reading documentation; some harness
configurations consume roughly 10x more tokens than others despite passing
identical tests; "a missing fact produces wrong work rather than absent
work" — agents fabricate rather than report a gap; agents often follow
outdated conventions even when better code exists in the repo; and fact
availability matters more than the fact's proximity to the edit site
(unverified in detail — full methodology and per-model breakdowns not read
beyond the abstract).

## Why it matters

This is a rare controlled ablation (not just a benchmark leaderboard) that
names specific, fixable causes of coding-agent unreliability at
repository scale — missing-fact fabrication, harness-dependent token
blow-up, and stale-convention-following. Each finding maps to a concrete
harness/context design lever (what to inject, when, and how) rather than a
model-choice recommendation, making it directly actionable for anyone
building or tuning a coding-agent harness.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The headline
findings (10x token-cost variation, fabrication-over-omission behavior,
outdated-convention-following, proximity-vs-availability result) are traced
to the abstract. The full experimental design (which seven models, which
five harnesses, exact ablation protocol) was not independently corroborated
— hence partial verification.

## Updates

- **2026-08-18** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
