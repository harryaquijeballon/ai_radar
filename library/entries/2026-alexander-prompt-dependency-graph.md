---
slug: 2026-alexander-prompt-dependency-graph
title: "Changing One Prompt Can Affect 50 Others — I Built a Prompt Dependency Graph to Find What Needs Retesting"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/changing-one-prompt-can-affect-50-others-i-built-a-prompt-dependency-graph-to-find-what-needs-retesting/
canonical_ids: []
publisher_or_author: "Emmimal P Alexander — Towards Data Science"
published: 2026-09-03
captured: 2026-09-04
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  A concrete, quantified technique for the harness/context-engineering lens
  (2): a dependency graph over shared prompt components that narrows which
  downstream prompts need re-evaluation after an edit, with reproducible
  numbers from the author's own test system.
---

# Changing One Prompt Can Affect 50 Others

## Summary
In systems built from composable prompts (shared sections reused across many prompts), editing one shared component can silently affect many downstream prompts, and it is often unclear which ones need re-testing. The author built a Python prompt-dependency graph at section-level granularity (prompts are broken into named sections rather than treated as monolithic blocks) and computes two metrics after an edit: "reachable" (every node structurally connected to the changed component) and "candidate" (nodes that actually depend on the changed section, plus their downstream dependents). On a deterministic 55-node synthetic test system, the candidate set was 47% smaller than the reachable set when editing a narrowly-shared component (24 of 45 reachable nodes needed evaluation), and 0% smaller when editing a universally-shared component (a `tone` section touched by all 55 nodes) — narrowing shrinks predictably as a component's sharing increases. Reported runtime: graph construction averaged 0.229ms, impact calculation 0.0375ms.

## Why it matters
Regression-testing all downstream prompts after every shared-component edit does not scale, and re-testing nothing risks silent breakage — a concrete instance of this profile's evaluation/guardrails lens (4) as much as harness engineering (lens 2). A dependency-graph technique that quantifiably narrows the retest set, with reported numbers showing the narrowing effect depends predictably on component sharing, is a pattern a builder of prompt-heavy research or policy pipelines could apply directly to reduce eval cost without reducing coverage.

## Verification notes
Fetched and read directly from the Towards Data Science post. The method (section-level graph construction, reachable vs. candidate metrics, breadth-first traversal) and all cited numbers (47% and 0% narrowing examples, 0.229ms/0.0375ms runtimes) are traceable to the article's own description and reported test results. The test system is a synthetic 55-node graph built by the author for demonstration, not a production system or third-party dataset, so the numbers are reproducible in principle from the stated method but not independently corroborated — recorded as `partial` verification.

## Updates
None yet.

## Related entries
None yet.
