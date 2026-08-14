---
slug: 2026-li-quotebench-command-path-failures
title: "QuoteBench: How Matched Scores Can Hide Command-Path Failures"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.13547
canonical_ids: ["arxiv:2608.13547"]
publisher_or_author: "Shangao Li, Yao Zhang, Volker Tresp, Yuanyuan Yang — arXiv preprint"
published: 2026-08-14
captured: 2026-08-14
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Directly on lens 4 (evaluation, validation and deterministic guardrails)
  and lens 5 (observability): shows that standard "matched execution score"
  evals for coding agents can hide large swings in real success rate caused
  by the command-generation-to-execution transport layer, with a concrete
  benchmark and a practical reporting recommendation.
verification: partial
---

# QuoteBench: How Matched Scores Can Hide Command-Path Failures

## Summary

The authors argue that LLM coding agents issue Bash commands through
interfaces that can alter model output between generation and execution, and
that a "matched execution score" (comparing generated vs. executed command)
cannot distinguish command-generation errors from failures introduced after
generation. They introduce QuoteBench, validating final task state across 56
tasks drawn from 14 incident-derived families, to measure the gap between
generation and execution transport. Findings: replaying the same model
response through an added parser lowers success by 55.4 to 73.2 percentage
points; disclosing parsing boundaries recovers 30.4–60.7 points for six
configurations but yields zero or slightly negative recovery for two others;
one model's matched-score gap of −3.6 points conceals −64.3 points of actual
damage plus +60.7 points of compensation elsewhere; model rankings shift
under deployment configuration, with one definitive ranking reversal and
four further reversals at single-task margins. The authors recommend
reporting model configuration, generation contract, execution path,
operating point, and final-state validator together, rather than treating a
matched score as an intrinsic model property.

## Why it matters

A concrete warning and a proposed reporting standard for anyone building or
reading coding-agent evaluations: a "matched" execution score can be
statistically identical while hiding enormous swings in real success and
even reversing model rankings, depending on the shell/parser transport layer
— directly actionable for teams designing or auditing agent evals (lens 4).

## Verification notes

Read via the arXiv abstract page only; full paper and benchmark tasks not
examined. The percentage-point figures above are as stated on the fetched
abstract page; not independently corroborated against a second source or the
released benchmark.

## Updates

None yet.

## Related entries

None yet.
