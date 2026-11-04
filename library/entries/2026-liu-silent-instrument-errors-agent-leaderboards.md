---
slug: 2026-liu-silent-instrument-errors-agent-leaderboards
title: "Silent Instrument Errors Reorder Agent Leaderboards"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.04399
canonical_ids: ["arxiv:2611.04399"]
publisher_or_author: "Yangze Liu"
published: 2026-11-03
captured: 2026-11-04
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on evaluation/validation/deterministic guardrails and observability
  (lenses 4, 5): shows that a published 13-point capability gap between a
  general-purpose agent and a specialized scaffold was actually a grading
  artifact (half the episodes silently went ungraded), finds three further
  concrete instrument errors on two public leaderboards (HAL, tau2-bench),
  gets three confirmed by the HAL maintainers, and proposes specific,
  implementable checks.
verification: verified
---

# Silent Instrument Errors Reorder Agent Leaderboards

## Summary

Argues that a general-purpose agent's apparent 13-point deficit against a
specialized scaffold on airline customer-service benchmark tasks was caused
by the evaluation infrastructure, not the agent: only about half of the
general agent's episodes were graded, because it often ended conversations in
a way that never triggered the grader, so the rest were silently recorded as
failures. Grading the ungraded episodes under the benchmark's own rules (with
no agent rerun) closes the pooled capability gap entirely. An audit of two
public leaderboards (HAL and tau2-bench), using only their published
artifacts, found three further instrument errors: a cost column that
double-counts nested model calls unevenly across rows; archived trajectories
that mislabel grader-written actions as agent actions; and a correct,
announced evaluator fix that silently reorders the leaderboard once saved
runs are re-graded. A separate mode-detection bug misread four files and
lowered their scores by 59-82 points with no error raised. HAL's maintainers
confirmed three of the issues within five weeks of being notified.

## Why it matters

A direct warning and checklist for anyone building or trusting an agent
evaluation harness: grading, logging, replay, and cost-accounting code is
part of the measurement and can fail silently in ways that look like genuine
capability differences. The paper's proposed checks are immediately
actionable — report the fraction of episodes actually graded, aggregate cost
from root spans (not per-call), tag the provenance of every recorded action,
and pin evaluator versions with a published diff on any re-grading — a
concrete, low-cost guardrail set for any team running or publishing agent
leaderboards.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-03). The 13-point gap, the half-ungraded-episodes finding, the three
audited instrument errors, the 59-82 point mode-detection bug, and the HAL
maintainers' confirmation of three issues within five weeks all trace to the
abstract text. Full paper (exact benchmark tasks, audit methodology) not read
at capture.

## Updates

None yet.

## Related entries

None yet.
