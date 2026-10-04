---
slug: 2026-hardy-agent-evaluation-reliability
title: "Agent Evaluation Reliability: More Tasks Won't (Always) Fix An Agent Leaderboard"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.00651
canonical_ids: ["arxiv:2610.00651"]
publisher_or_author: "Michael Hardy, Ruhana Azam, Anka Reuel, Mykel Kochenderfer, Sanmi Koyejo — arXiv preprint"
published: 2026-09-30
captured: 2026-10-04
relevance:
  social_science: low
  ai_engineering: high
verification: verified
rationale: >-
  Lens 4 (evaluation and validation): a Bayesian variance-decomposition method
  for judging whether agent leaderboard rankings are reliable, with concrete
  budget-allocation guidance a builder can apply when evaluating agent systems.
---

# Agent Evaluation Reliability: More Tasks Won't (Always) Fix An Agent Leaderboard

## Summary

The authors argue that agent-leaderboard rankings depend on evaluation conditions beyond model performance, so reliability depends on what a score or ranking is meant to represent. They develop a Bayesian variance-decomposition framework for sparse, imbalanced agent leaderboards and apply it to 22 benchmarks from the Holistic Agent Leaderboard and Harbor Index. Reported findings (per the arXiv abstract page): fixed model–scaffold systems rank with reliability 0.935–0.994, while underlying-model reliability is 0.148–0.841; adding unlimited similar tasks improves model-ranking reliability by at most 0.097 when scaffold coverage is limited; pooling diverse benchmarks raises projected cross-task reliability from 0.44 to 0.75 at equivalent cost.

## Why it matters

For anyone building or buying agent systems for research or policy work, it shows that a leaderboard rank may reflect scaffold choice rather than the model, and that evaluation budget is better spent on the dominant source of uncertainty than on more tasks of the same kind.

## Verification notes

Source reachable (arXiv abstract page). Figures traced to the abstract as retrieved; full text was not read and results were not independently reproduced.

## Updates

None yet.

## Related entries

None yet.
