---
slug: 2026-raj-trace-router-agentic-routing
title: "TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.22465
canonical_ids: ["arxiv:2607.22465", "doi:10.48550/arXiv.2607.22465"]
publisher_or_author: "Ritik Raj, Souvik Kundu, Sarbartha Banerjee, Dheemanth Joshi, Ishita Vohra, Tushar Krishna — arXiv preprint (cs.AI)"
published: 2026-07-24
captured: 2026-07-27
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on model selection/routing/cost-latency, a named standing interest
  for this radar: identifies a real mismatch (per-call routers can't
  attribute delayed, task-level outcomes to individual routing decisions in
  long-horizon agentic workflows) and proposes a task-level contextual
  bandit router pinned per task, with quantified Pareto-frontier gains on
  two agentic benchmarks (tau2-Bench, Terminal-Bench) — a usable pattern
  with stated trade-offs and evidence, not just an opinion piece.
---

# TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI

## Summary

Enterprise agentic AI increasingly routes each LLM call to a model chosen
for its cost-quality trade-off, but existing routers make independent
per-call decisions, while an agentic workflow's quality is only observable
as a delayed, task-level outcome — a mismatch that prevents per-call
routers from correctly attributing feedback to individual routing
decisions. TRACE-Router instead assigns each task to a model once at
admission using a contextual bandit, pins all subsequent LLM calls in that
task to the selected backend, and updates its policy using the task's
terminal reward (jointly accounting for accuracy and latency) — avoiding
explicit task-complexity estimation. Across three agentic benchmarks,
TRACE-Router consistently improves the accuracy-latency trade-off, reaching
non-dominated Pareto-frontier points: on tau2-Bench it outperforms
latency-matched interpolation between individual models by 7–8 accuracy
points; on Terminal-Bench it achieves 7.1 higher accuracy points than the
strongest single-model baseline with 36% lower latency.

## Why it matters

A directly deployable pattern for anyone running agentic workloads across
multiple LLM backends: pin the routing decision at the task level (not the
call level) and let the terminal task reward — not a proxy per-call
signal — drive the bandit update. The reported Pareto-frontier gains give a
concrete benchmark to compare against when evaluating any routing layer for
a research or policy agent pipeline where both cost and latency matter.

## Verification notes

arXiv abstract page fetched directly (2026-07-27); title, authors,
"Submitted on 24 Jul 2026", categories (cs.AI, cs.LG, cs.MA) confirmed.
Every claim in the Summary — the routing mismatch problem, the
task-level-bandit mechanism, and the tau2-Bench/Terminal-Bench figures —
traces directly to the abstract text, the primary source for this
pre-publication preprint. Full paper text not read at capture, so the
bandit's exact formulation and the three benchmarks' full results are
unverified beyond the abstract's summary figures. Upgrade path: read the
full PDF for the bandit formulation and the third benchmark's results.

## Updates

None yet.

## Related entries

None yet.
