---
slug: 2026-chen-horizon-gap-long-horizon-agents-survey
title: "The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.06663
canonical_ids: ["arxiv:2608.06663"]
publisher_or_author: "Mingguang Chen, Licheng Wang, Bo Qu — arXiv preprint"
published: 2026-08-07
captured: 2026-08-10
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 1 (agent architecture) and lens 2 (harness/context
  engineering): a systematic review (1,547 papers, 2024-2026) that
  disambiguates long-horizon tasks, long-context capacity, and long-term
  memory persistence, and organizes the field across six dimensions.
  Medium rather than high because it is a literature synthesis rather than
  new evidence or a directly deployable method — a map, not yet a tool.
---

# The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents

## Summary

Names and systematically reviews "the horizon gap" — the discrepancy
between LLMs' strength at single-pass reasoning and their difficulty with
extended, multi-hour tasks — across 1,547 papers from 2024-2026. The
authors disambiguate three often-conflated concepts: long-horizon tasks,
long-context capacity, and long-term memory persistence, and organize the
literature across six dimensions (planning, memory, execution, training,
evaluation, and foundations/safety) intersected with where task continuity
occurs. A central finding is that outcome-only success signals grow
uninformative as task horizons lengthen, with the field responding through
denser step-level signals (process reward models, credit assignment,
trajectory diagnostics). Open challenges named include separating model
capability from system capability, managing correlated bias in dual-use
signals, and whether long-horizon reliability has a general predictive
theory.

## Why it matters

A vocabulary and organizing map for teams building agents meant to run for
hours rather than minutes: the tasks/context/memory disambiguation alone
resolves a common source of talking-past-each-other in agent-architecture
discussions, and the "outcome-only signals grow uninformative" finding is a
concrete argument for investing in step-level evaluation signals before
scaling task horizon further.

## Verification notes

arXiv abstract page fetched directly (2026-08-10); authors, submission date
(7 Aug 2026, v1), and category confirmed. All claims in the Summary — the
1,547-paper review scope and 2024-2026 window, the three-concept
disambiguation, the six-dimension organizing framework, the outcome-only-
signal finding and the field's step-level-signal response, and the named
open challenges — trace directly to the fetched abstract text. No
independent corroboration attempted (preprint, not yet peer reviewed). Full
paper PDF not read at capture.

## Updates

None yet.

## Related entries

None yet.
