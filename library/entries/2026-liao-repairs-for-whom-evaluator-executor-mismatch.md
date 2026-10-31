---
slug: 2026-liao-repairs-for-whom-evaluator-executor-mismatch
title: "Repairs for Whom? Evaluator-Executor Mismatch in Selecting Repairs for Failed LLM Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.38610
canonical_ids: ["arxiv:2610.38610"]
publisher_or_author: "Yijun Liao, Fanwei Liang — arXiv (cs.SE)"
published: 2026-10-28
captured: 2026-10-31
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Squarely on lens 4/5 (eval/observability for agent failure recovery): a
  controlled, quantified demonstration that the common practice of scoring
  candidate repairs with a different (often stronger) model than the one
  that will execute them systematically loses deployment value — a
  concrete, actionable correction to standard repair-evaluation practice.
verification: verified
---

# Repairs for Whom? Evaluator-Executor Mismatch in Selecting Repairs for Failed LLM Agents

## Summary

When an LLM agent fails, repair methods choose which action to replace and
what to substitute, typically scoring candidate repairs with greedy replay,
a stronger model, an environment oracle, or a judge reading the failed log.
The authors ask whether these evaluators actually choose repairs that help
the agent that will execute them. Holding failed trajectories and
single-step candidate repairs fixed, they label each candidate via
independent rollouts of the deployed policy and measure how much deployment
value each evaluator's choice loses relative to that ground truth. Greedy
replay loses 0.08–0.13 in expected net success gain on ALFWorld and
0.06–0.13 in net reward on WebShop compared with selection using the
deployed agent's own rollouts. At an equal rollout budget, choosing repairs
for Qwen2.5-7B using Qwen2.5-14B rollouts loses 0.25 on ALFWorld and 0.07 on
WebShop; twenty 14B rollouts per candidate are worth no more than two of the
7B agent's own rollouts, and the two models prefer opposite repairs on
selected disagreement cases. Between similarly-sized models from different
families, losses occur in both directions on both environments (0.07–0.17).
The scoring executor also changes which repair location gets chosen and how
repair methods rank against each other. The authors conclude repairs should
be verified with the executor that will actually run them, and repair
labels should name their executor.

## Why it matters

A direct, quantified correction to a common shortcut in agent self-repair
pipelines — evaluating candidate fixes with a stronger or different model
than the one deploying them — showing the mismatch is not a minor
approximation but can flip which repair looks best; builders of
self-correcting agents get a concrete rule ("verify with the deployment
executor") rather than an intuition.

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.38610, v1 submitted
28 Oct 2026, primary cs.SE, cross-listed cs.CL). The ALFWorld/WebShop loss
figures (0.08–0.13, 0.06–0.13, 0.25, 0.07, 0.07–0.17) and the
budget-equivalence claim (20 14B rollouts ≈ 2 of the agent's own) are traced
to the abstract text itself. No independent corroboration of the raw
rollout data was attempted.

## Updates

None yet.

## Related entries

None yet.
