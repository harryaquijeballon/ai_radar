---
slug: 2026-asgari-black-box-test-selection-agents
title: "Evaluating More with Less: Black-Box Test Selection for AI Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.34617
canonical_ids: ["arxiv:2611.34617"]
publisher_or_author: "Ali Asgari, Mitchell Olsthoorn, Arie van Deursen, Annibale Panichella — arXiv preprint"
published: 2026-11-25
captured: 2026-11-27
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  The first empirical study of black-box test-case selection for agent
  benchmarks, with a quantified, practically usable cost reduction (80% at
  under 1pp estimation error on SWE-bench Verified) — squarely on lens 4
  (evaluation, validation and deterministic guardrails), directly
  applicable to any builder running repeated, expensive agent evaluations.
---

# Evaluating More with Less: Black-Box Test Selection for AI Agents

## Summary

Agent benchmarks are expensive to re-run every time the model, prompt,
scaffold, tools, or environment changes, and for proprietary agents the
internal model details needed for smarter sampling are unavailable. The
authors present what they describe as the first empirical study of
black-box test-case selection (TCS) for agentic systems, treating each
benchmark task as a test case and adapting black-box regression-testing
techniques — selecting tasks by description, metadata, code fragments, and
embeddings, and estimating task difficulty via heuristic features or an
independent LLM-as-judge — all without executing the target agent or using
its past results. They evaluate 14 selection strategies, including random
sampling and a historical-data baseline, across 10 AI agent benchmarks with
12 to 101 agents per benchmark, on two objectives: estimating overall
Success Rate and detecting failures early. "Category Partition" gives the
lowest median Success Rate estimation error on five benchmarks at a 20%
task budget; on GPT-5.2 Codex against SWE-bench Verified, it selects 100 of
500 tasks instead of all 500, cutting execution cost from $225 to $47 (an
80% reduction) at a Success Rate estimation error of only 0.8 percentage
points. For early failure detection at the same budget, LLM-as-judge
selection finds failures in 53.0% of selected tasks versus 27.4% for random
sampling — roughly double. No single strategy wins on both objectives:
adapted regression-testing strategies suit Success Rate estimation, while
LLM-as-judge selection suits early failure detection.

## Why it matters

A directly usable method for cutting the cost of agent evaluation without
giving up much accuracy — relevant to any builder or researcher running
repeated agent benchmarks (including a policy-simulation harness that must
validate agent output across many scenarios): pick a test-selection
strategy by evaluation goal (Category Partition for overall success-rate
estimates, LLM-as-judge selection for catching failures early), rather than
assuming full-benchmark runs or random sampling are the only options.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.34617, v1 submitted
2026-11-25, cs.SE). The methodology (14 strategies, 10 benchmarks) and all
quantified figures above ($225→$47 cost, 0.8pp estimation error, 53.0% vs.
27.4% failure detection) are traced to the abstract's own description as
summarized by the fetch tool. No independent corroboration was attempted;
verification is partial pending a full-text read.

## Updates

None yet.

## Related entries

None yet.
