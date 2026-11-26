---
slug: 2026-goel-coding-agent-over-editing
title: "How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.34875
canonical_ids: ["arxiv:2611.34875"]
publisher_or_author: "Aakash Goel, Benjamin Steenhoek, Yu Hu — arXiv preprint"
published: 2026-11-25
captured: 2026-11-26
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A quantified, benchmark-scale method (Delta Residue Attribution) for
  telling whether a coding agent's extra edits are actually needed, tested
  on 7,660 trajectories across 18 models — a practically usable measurement
  technique for lens 7 (AI-assisted software development).
---

# How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches

## Summary

Coding-agent patches are consistently larger than human developers' patches
for the same task, which is often read as over-editing — but patch size
alone doesn't show whether the extra edits are actually needed. The authors
introduce Delta Residue Attribution (DRA): it replays an agent's trajectory,
traces each unit of the patch to the step that wrote it, reverts that unit,
and reruns the task's tests to check whether the unit was necessary. Applied
to 7,660 resolved GitHub Copilot CLI trajectories from 18 frontier models
across SWE-bench Verified (6,728) and DeepSWE (932): on SWE-bench Verified,
61% of extra edits add tests and 13% add documentation; on DeepSWE, 58% of
extra edits are code. Mean code necessity on SWE-bench Verified is actually
slightly higher for agents than developers (0.887 vs. 0.864), with 11 of 18
models leaving less unneeded code than developers; on DeepSWE it is 0.797
vs. 0.785. About 11% of agent code units on SWE-bench Verified are unneeded,
and 89% of those still change behavior. Debug steps write almost none of the
unneeded code. Code necessity varies substantially by model, and on DeepSWE
it is negatively correlated with resolve rate (Spearman -0.59, p = 0.01).
DRA-based pruning (using only tests the agent can see) removes most unneeded
code but also some needed code (67% recall, 46% precision); 89% of pruned
patches still resolve the task. Having the agent audit its own diff is more
precise (66%) but less effective (36% recall).

## Why it matters

A concrete, applicable measurement technique (and companion mitigation) for
anyone evaluating or tuning coding agents: patch-size comparisons to human
baselines are a misleading over-editing signal, and DRA gives a reusable way
to measure what's actually unneeded, rather than just what's extra. The
recommendation that benchmarks report code necessity alongside resolve rate
is directly actionable for eval design, and the pruning/self-audit results
quantify a concrete trade-off (recall vs. precision) for harness-level
patch-trimming.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.34875, v1 submitted
2026-11-25). The method description, scope (7,660 trajectories, 18 models),
and all quantified figures above are traced to the abstract's own
description. No independent corroboration was available or attempted beyond
the source text; this is the paper's own novel empirical contribution.

## Updates

None yet.

## Related entries

None yet.
