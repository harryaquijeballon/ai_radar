---
slug: 2026-shen-ai-code-reviewer-effort
title: "How Much Effort Does an AI Code Reviewer Need? Evidence from Claude 5.5 Models on Plausible-but-Wrong Patches"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.33639
canonical_ids: ["arxiv:2611.33639"]
publisher_or_author: "Zax Shen, Hanling Zhang, Zixu Wang — arXiv preprint"
published: 2026-11-25
captured: 2026-11-26
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A preregistered, quantified comparison of reasoning-effort settings for
  an AI code reviewer catching plausible-but-wrong patches, with explicit
  cost/accuracy trade-offs and a clear negative result (no setting is a
  strong gate) — directly usable guidance for lens 4 (evaluation and
  deterministic guardrails).
---

# How Much Effort Does an AI Code Reviewer Need? Evidence from Claude 5.5 Models on Plausible-but-Wrong Patches

## Summary

AI coding agents produce code faster than people can review it, so teams
are adding AI reviewers; reasoning models let these reviewers trade cost for
thoroughness via an effort setting. The authors ask how much effort a
reviewer needs to catch "plausible-but-wrong" patches — patches that pass a
benchmark's tests but fail stronger ones. Claude Opus 5.5 (preregistered),
Sonnet 5.5, and Haiku 5.5 (exploratory) each reviewed the same 90
agent-written Django patches from SWE-bench Verified at low, medium, and
high effort; under strengthened SWE-ABS tests, 55 of the 90 patches were
actually wrong and 35 correct. Higher effort accepted fewer wrong patches in
every model, but the difference was statistically supported only for Opus
and Haiku: false-success rates (wrong patches accepted) at low vs. high
effort were 0.67 vs. 0.45 (Opus), 0.65 vs. 0.49 (Sonnet), 0.78 vs. 0.51
(Haiku). For Opus, medium effort was non-inferior to high within a
preregistered 15-percentage-point margin (difference 0.018, 95% CI
[-0.065, 0.108]) and cost 20% less — short of the preregistered 30%
savings target. For Sonnet and Haiku, medium was cheaper (39% and 51% lower
cost respectively) but non-inferiority to high effort was not demonstrated.
No effort setting worked as a strong gate: every setting accepted at least
45% of wrong patches. For 32 of the 55 wrong patches, the failing test may
check more than the underlying issue actually requires, and without those
patches neither accuracy hypothesis held for any model.

## Why it matters

A directly usable, preregistered benchmark of the cost/effort dial on AI
code reviewers, with an explicit negative finding: no tested effort setting
is strong enough to use as an automatic merge gate on its own, and the
"turn up the effort" intuition only partially pays off and only for some
models. Anyone deploying an LLM-based review gate can use this as a
calibration baseline and as a caution against trusting high-effort review
as a sufficient safeguard against plausible-but-wrong patches.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.33639, v1 submitted
2026-11-25). The preregistered design, sample (90 patches, 55 wrong/35
correct under SWE-ABS), and all quantified figures above are traced to the
abstract's own description. No independent corroboration was available or
attempted beyond the source text; this is the paper's own novel preregistered
experimental contribution.

## Updates

None yet.

## Related entries

None yet.
