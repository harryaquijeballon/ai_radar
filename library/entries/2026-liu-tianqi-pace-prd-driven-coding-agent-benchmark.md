---
slug: 2026-liu-tianqi-pace-prd-driven-coding-agent-benchmark
title: "When Coding Agents Outpace Review: Evaluating PRD-Driven Development in Mature Enterprise Repositories"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.26394
canonical_ids: ["arxiv:2610.26394"]
publisher_or_author: "Tianqi Liu et al."
published: 2026-10-20
captured: 2026-10-20
relevance:
  ai_engineering: high
  social_science: n/a
verification: partial
rationale: >-
  A new benchmark (PACE) that measures whether coding agents fully deliver a
  Product Requirement Document — not just pass isolated tests — in mature
  enterprise codebases, with a quantified demonstration that revising the
  agent harness (not the model) measurably raises delivery performance:
  directly actionable for evaluation design (lens 4) and AI-assisted
  development practice (lens 7).
---

# When Coding Agents Outpace Review: Evaluating PRD-Driven Development in Mature Enterprise Repositories

## Summary

The paper introduces PACE, a benchmark for checking whether coding agents
fully deliver on a Product Requirement Document (PRD) inside mature
enterprise codebases, arguing that existing benchmarks (issue resolution,
build-from-scratch, isolated unit tests) leave incremental PRD fulfillment —
including business and integration requirements — largely unmeasured. PACE
contains 43 enterprise tasks with 750 expert-audited "Code Points." Its
method reconstructs requirements, builds evaluation criteria from them, and
gathers evidence to judge fulfillment, explicitly linking any delivery gap
back to specific agent behaviors. The authors evaluate 11 model-scaffold
configurations.

Headline findings: most configurations scored between 52.1 and 78.1 on
PACE's scale; the best-performing model (reported as "GPT-5.6-Sol") reached
the highest complete-delivery rate at only 14.0%. Incomplete implementation
and missing integration were the main bottlenecks — building individual
components correctly did not guarantee complete delivery. PACE's automated
evaluation agreed with expert consensus 95.2% of the time. Revising the agent
harness around a fixed model and task set raised mean performance from 59.4
to 63.0, showing that PACE's diagnostic feedback can guide targeted
harness-level improvements independent of the underlying model.

## Why it matters

Gives builders a concrete alternative to issue-resolution and from-scratch
benchmarks for measuring whether a coding agent actually finishes a real,
multi-part requirement in an existing large codebase — the gap PACE
measures (complete-delivery rate far below component-level correctness) is
exactly the failure mode practitioners report anecdotally but rarely
quantify. The harness-revision result is a direct, reusable lesson: measured
diagnostic feedback from a PRD-fulfillment benchmark can be used to improve
the harness itself, not just to rank models.

## Verification notes

Read via the arXiv abstract page. The benchmark design (43 tasks, 750 Code
Points, three-part evaluation method), the 11-configuration evaluation, and
the quantified findings above are stated in the abstract and traceable to
it. The full paper (task list, scaffold-revision details, scoring rubric)
was not fetched, so corroboration of the exact figures against underlying
data was not attempted; `verification: partial`.

## Updates

None yet.

## Related entries

None yet.
