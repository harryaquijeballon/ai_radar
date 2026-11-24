---
slug: 2026-zhang-swe-gym-verified-reward-label-audit
title: "What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.30207
canonical_ids: ["arxiv:2611.30207"]
publisher_or_author: "Yikai Zhang et al."
published: 2026-11-24
captured: 2026-11-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Lens 4 (evaluation, validation and deterministic guardrails): a
  quantified audit showing that a widely used RL training benchmark's
  reward labels are frequently wrong, with a measured training-quality
  improvement from fixing them — a directly actionable lesson that a pass
  rate measures whether a task yields reward, not whether that reward is
  correct.
---

# What Makes Good Data for Training Coding Agents? A Systematic Study on SWE-Gym

## Summary

Reinforcement learning trains coding agents on software tasks whose hidden tests determine the reward, but task collections typically only check those tests against the reference fix — not against other correct solutions. The authors audit SWE-Gym with two LLM families, counting a suspected label error only when execution reproduces it. They find unsolved tasks are often mislabeled: 74% of tasks a 9B base model never solves have a test that rejects even correct fixes, versus 20% of tasks the model sometimes solves. Repairing or removing these mislabeled tasks yields better-trained policies — at equal size and matched difficulty, models trained on the audited tasks score 2.4 and 2.7 points higher on held-out SWE-bench Verified and SWE-bench Pro than models trained on the original tasks. Simply dropping never-solved tasks (without repairing labels) produces no such gain. The authors also find that incorrect patches that nonetheless pass the tests (false positives) make up about a quarter of passing patches, and that adding new tests to catch a quarter of these does not detectably change held-out scores. Their conclusion: a pass rate shows whether a task yields reward, not whether the reward is correct, so reward labels must be independently checked. They release SWE-Gym-Verified: 1,087 audited tasks with execution-backed verdicts, training sets, and the audit pipeline.

## Why it matters

A directly actionable warning for anyone training or fine-tuning coding agents with RL on benchmark-derived tasks: a low pass rate on a task may mean the test itself is broken rather than the model being wrong, and fixing reward labels (not just filtering out hard tasks) is what produces the measured training-quality gain — with a released, audited dataset (SWE-Gym-Verified) usable directly in place of the original.

## Verification notes

Fetched directly from arXiv; abstract and metadata confirmed (v1 submitted 23 November 2026, within the discovery window; primary category cs.CL, cross-listed cs.AI/cs.LG/cs.SE). All figures above are as stated in the abstract. The audit methodology and the matched-difficulty training comparison were not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

None yet.
