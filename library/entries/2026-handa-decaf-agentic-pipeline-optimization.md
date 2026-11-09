---
slug: 2026-handa-decaf-agentic-pipeline-optimization
title: "Divide, Diagnose, and Compose: Optimizing Agentic Pipelines and Harnesses"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.08723
canonical_ids: ["arxiv:2611.08723"]
publisher_or_author: "Divij Handa, Christopher Tensmeyer, Jihyung Kil, Vlad I. Morariu"
published: 2026-11-05
captured: 2026-11-09
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on agent architecture and orchestration (lens 1) and harness
  engineering (lens 2): a decomposed optimizer that tunes prompts, pipeline
  structure, model choice, and tool-use rules separately rather than as one
  unit, with logged reasoning per decision and quantified gains across
  accuracy, cost, and latency together — a usable pattern, not just a
  single-metric optimizer.
---

# Divide, Diagnose, and Compose: Optimizing Agentic Pipelines and Harnesses

## Summary

Designing agentic pipelines that perform well while controlling cost and latency requires tuning several interdependent choices at once — prompts, pipeline structure, model selection, tool-use rules — and manual search over this space is slow and expensive. Existing automated optimizers tend to cover only a fixed subset of these choices, change the whole pipeline as a single unit, or give little evidence explaining their changes.

The authors propose DeCAF (Decomposed Credit-Assignment Framework), which tailors its search space to the specific benchmark and seed pipeline, optimizes each dimension separately, and records reasoning for every decision. Given a task description, example benchmark items, and a starting pipeline, DeCAF selects relevant dimensions and generates varied hypotheses for each; separate coding-agent sessions then optimize each dimension within a limited set of allowed edits, measuring accuracy, inference cost, and latency together and logging every hypothesis, edit, and result. A final synthesis session merges compatible improvements across dimensions, using a component-level evaluator that builds role-specific rubrics from each agent's own instructions to find weak components and guide revisions spanning multiple dimensions.

On a range of agentic benchmarks, DeCAF raises average task performance by 2.58 percentage points, cuts inference cost by 4.30%, and reduces end-to-end latency by 42.45%, relative to the strongest overall baseline.

## Why it matters

A concrete harness-optimization pattern — decompose the search space by dimension, optimize each with evidence logged, then synthesize — directly applicable to anyone tuning a multi-component agentic pipeline for a research or policy product where cost, latency, and accuracy all matter simultaneously, rather than accuracy alone. The per-decision reasoning log and role-specific component rubric are reusable mechanisms for making an otherwise opaque optimization process auditable.

## Verification notes

Fetched the arXiv abstract page directly; the method description and the three quantified gains (2.58pp accuracy, -4.30% cost, -42.45% latency) are as stated in the abstract. Load-bearing quantified claims are traced to the source and have not been independently replicated by a third party; the specific "range of agentic benchmarks" evaluated is not itemized in the abstract.

## Updates

None yet.

## Related entries

- [2026-luo-autodesign-meta-harness-optimization](2026-luo-autodesign-meta-harness-optimization.md) — a closely related meta-harness optimization approach for long-horizon agentic design; useful to read alongside DeCAF's dimension-decomposed search.
- [2026-dong-capo-constraint-aware-prompt-optimization](2026-dong-capo-constraint-aware-prompt-optimization.md) — narrower in scope (prompt optimization only), complementary to DeCAF's multi-dimensional search.
