---
slug: 2026-huang-reasoning-cost-code-correctness
title: "Does More Thinking Pay Off? Reasoning Cost and Correctness of LLMs in Code Generation and Bug Fixing"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.36952
canonical_ids: ["arxiv:2610.36952"]
publisher_or_author: "Andie Huang, Ying Pang, Qian Zhang, Yihang Cheng, Lin Ma"
published: 2026-10-27
captured: 2026-10-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on agent architecture and evaluation (lenses 1, 4): a controlled
  study (866 tasks, five model settings) that quantifies reasoning's
  accuracy-per-token payoff in code generation/bug-fixing and shows half
  of a stored reasoning trace can be truncated with no significant
  correctness loss — a directly actionable cost-control technique with a
  measured result, not a general observation that "models reason."
---

# Does More Thinking Pay Off? Reasoning Cost and Correctness of LLMs in Code Generation and Bug Fixing

## Summary

Many LLMs now produce an explicit reasoning trace before writing code,
but code-generation and bug-fixing benchmarks usually report only
correctness, leaving the value of that extra reasoning relative to its
token cost unclear. The authors study 866 Python tasks from HumanEval
Pro, MBPP Pro, and BugsInPy under five model settings. They measure the
accuracy gain and token overhead from reasoning, characterize what
reasoning traces actually contain (mainly implementation choice/checking
in code generation; mainly fault localization and repair planning in bug
fixing), and test whether truncated traces still yield correct solutions
by having Qwen3-32B (reasoning off) complete from a stored trace cut at
different lengths.

For Qwen3-32B, reasoning on vs. off: HumanEval Pro pass@1 rises from 71.1%
to 76.5%; BugsInPy mean tests passed rises from 3.5% to 7.9%; MBPP Pro
rises from 68.1% to 69.5%, not statistically significant. On MBPP Pro the
model uses a median of over 2,000 thinking tokens per task, and a longer
median trace does not reliably predict higher accuracy across models.
Keeping only the first half of a stored trace produces no statistically
significant drop in correctness. Two candidate stopping rules — one
triggered by repetitive traces, one that stops once solution code first
appears — rarely fire or help inconsistently across models, and neither
beats plain fixed-length truncation (all figures as stated in the fetched
abstract; full paper, task sets, and statistical tests not reviewed at
capture).

## Why it matters

A measured, directly actionable finding for anyone paying per-token for
reasoning-model inference in a coding pipeline: reasoning's accuracy
payoff is task-dependent and often small (not significant on MBPP Pro in
this study), token overhead is large (2,000+ median thinking tokens), and
simple fixed-length truncation of stored traces can cut cost with no
measured correctness loss — a concrete, cheap lever to test against more
elaborate adaptive-stopping schemes before building one.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-29; single version,
submitted 27 Oct 2026, 10:12 UTC, 957 KB). The task-set composition (866
tasks, three benchmarks, five model settings), the Qwen3-32B pass-rate
figures (71.1%→76.5%, 3.5%→7.9%, 68.1%→69.5% n.s.), the >2,000-token
median, and the truncation result (first half retained, no significant
drop) all trace to the fetched abstract text. The qualitative trace-content
analysis and the two stopping-rule comparisons are reported descriptively
in the abstract without effect sizes; full paper and statistical tests not
independently reviewed.

## Updates

None yet.

## Related entries

None yet.
