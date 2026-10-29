---
slug: 2026-srinivasan-continue-or-restart-agents
title: "Continue or Restart? The Limits of Early Failure Prediction in Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.35971
canonical_ids: ["arxiv:2610.35971"]
publisher_or_author: "Srinath Srinivasan, Lunxiao Li, Tim Menzies, Wesley Assunção"
published: 2026-10-26
captured: 2026-10-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation (lens 4) and observability (lens 5): a
  large-scale analysis (147,002 execution traces, four model-framework
  settings) that challenges a widely assumed compute-saving technique
  (early-stopping unpromising agent runs) with a directly actionable
  negative result — continuation usually beats restart policies at equal
  token budget — rather than proposing yet another early-stopping method.
---

# Continue or Restart? The Limits of Early Failure Prediction in Coding Agents

## Summary

Examines whether early stopping can cut compute costs for autonomous
coding agents by terminating unpromising runs before completion. The
central question is separating a task's inherent difficulty from the
progress of one specific attempt. The authors analyze 147,002 execution
traces from two public corpora across four model-framework settings,
comparing pre-execution issue context with early execution prefixes (5k–20k
tokens) using linear count models, initial-turn text embeddings,
task-conditional rankers, and a fine-tuned Qwen3-0.6B monitor.

Early prefixes modestly improve *cross-task* outcome ranking, but
discrimination *within* a task stays near chance at early token landmarks
(mean AUC ≈0.50, 95% range [0.48, 0.51], across three seeds and 32,406
attempts at 20k tokens). The authors then simulate stopping decisions
under shared token budgets, comparing score-guided restarts, matched
random restarts, and uninterrupted continuation. Under a 75k-token cap,
learned restarting improves resolution over matched random restarting by
up to 1.98 percentage points, but within-task attempt selection
contributes only -0.11 to +0.24 points of that — meaning the gain comes
almost entirely from deciding *which tasks* to stop (avoiding stops on
easy issues), not from picking better attempts within a task. In 216 of
224 tested budget-threshold configurations, uninterrupted continuation
achieves higher solve rates at lower mean token cost than both restart
policies (all figures as stated in the fetched abstract; full paper and
corpora not reviewed at capture).

## Why it matters

A directly actionable negative result for anyone building or buying an
"early-stopping" or "failure-prediction" layer to cut coding-agent
compute costs: on this large-scale analysis, within-task discrimination
is near chance, and simply letting agents run to completion beats both
learned and random restart policies in the overwhelming majority of
tested configurations. Before investing in an early-stopping classifier,
this gives a concrete bar to clear — demonstrate attempt-level
discrimination *and* net compute savings relative to plain continuation,
not just plausible-sounding cross-task ranking.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-29; single version,
submitted 26 Oct 2026, 04:50 UTC, 52 KB). The dataset scale (147,002
traces, four settings), the near-chance within-task AUC (~0.50, 95% range
[0.48, 0.51]), the 1.98-point restart gain and its -0.11/+0.24-point
decomposition, and the 216-of-224 continuation result all trace to the
fetched abstract text. The two underlying public corpora, the monitor's
training procedure, and the full statistical methodology were not
independently reviewed beyond the abstract.

## Updates

None yet.

## Related entries

None yet.
