---
slug: 2026-zeng-multistep-swe-long-horizon-benchmark
title: "Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07166
canonical_ids: ["arxiv:2611.07166"]
publisher_or_author: "Xiangkai Zeng, Zheng Liu, Zihao Lin"
published: 2026-11-04
captured: 2026-11-08
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation and validation): a new long-horizon benchmark
  (chained, dependent coding tasks on one codebase rather than isolated
  single-shot tasks) showing even the strongest of nine frontier models
  solves only 18.5% of chains — directly usable evidence for anyone relying
  on agents to extend their own prior work over many steps, which is the
  structural pattern behind agentic simulation pipelines.
---

# Multi-step SWE: Can Coding Agents Keep Building on Their Own Code Over Long Horizons?

## Summary

Observes that developers routinely ask a coding agent to build a
component, then extend, upgrade, and optimize it — each time on code the
agent wrote earlier — while most benchmarks score only one isolated task.
Introduces Multi-step SWE, a long-horizon benchmark of 69 tasks, each a
chain of 5 to 15 dependent steps on a single codebase, where every step
starts from the agent's own output in earlier steps, so early design
decisions and errors carry forward. Tasks span four families of
engineering work and nine languages, covering both from-scratch builds and
existing open-source codebases, with every step grounded in a source of
truth defining both the instruction and its verifier. Across nine frontier
models, the strongest reaches a solve rate of only 18.5% on full chains,
and 38 of the 69 task chains go unsolved by every model tested. The
benchmark is publicly released.

## Why it matters

A sobering, quantified limit on exactly the capability that long-running
agentic systems — including a simulation harness that must keep extending
its own prior output over many steps — depend on: even frontier models
mostly fail to correctly build on their own earlier work once a task chain
gets long. Directly usable as an evaluation tool or a cited capability
ceiling (lens 4).

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 4 Nov 2026, no revisions). The benchmark design (69 tasks, 5–15
step chains, four task families, nine languages) and the headline 18.5%
solve-rate / 38-of-69-unsolved figures trace to the fetched abstract text —
treated as `verified` per this library's standing convention for
single-source arXiv preprints whose headline claims are self-reported. The
full paper (exact model list, per-family breakdowns) was not reviewed at
capture.

## Updates

None yet.

## Related entries

None yet.
