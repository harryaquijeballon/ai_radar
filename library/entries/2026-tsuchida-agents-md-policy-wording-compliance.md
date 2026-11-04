---
slug: 2026-tsuchida-agents-md-policy-wording-compliance
title: "Do Coding Agents Follow AGENTS.md? The Effect of Policy Wording on Instruction Compliance"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.04367
canonical_ids: ["arxiv:2611.04367"]
publisher_or_author: "Rikuto Tsuchida, Youmei Fan, Kazumasa Shimari, Raula Gaikovina Kula, Kenichi Matsumoto"
published: 2026-11-03
captured: 2026-11-04
relevance:
  social_science: n/a
  ai_engineering: medium
rationale: >-
  Medium on harness/context engineering (lens 2): a direct, controlled test
  of how phrasing style in an agent-instruction file (AGENTS.md-style)
  changes instruction compliance across harness-model combinations —
  narrow in scope (one policy, 86 tasks) but squarely on how this project's
  own CLAUDE.md/engine instructions should be worded.
verification: verified
---

# Do Coding Agents Follow AGENTS.md? The Effect of Policy Wording on Instruction Compliance

## Summary

Tests whether coding agents actually follow the policies written into their
Agent Context File (ACF), such as AGENTS.md. The authors inserted one policy
into the ACFs of 86 benchmark tasks, wrote it in four phrasing styles, and
tested across four harness-model combinations. Conditional phrasing (e.g.,
"if X, then do Y") was followed less often than the other styles.
Prescriptive and explanatory phrasing both did better than conditional, but
which of the two was stronger depended on the specific harness-model
combination.

## Why it matters

A direct, if narrow, empirical input into how to word instruction files
that this project's own engine and skills rely on (CLAUDE.md, ENGINE.md,
skill instructions): conditional "if/then" policy wording appears to be a
weaker choice than prescriptive or explanatory phrasing for getting a coding
agent to actually comply, though the best of the two non-conditional styles
is harness-and-model dependent rather than universal.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-03). The experimental design (one policy, four phrasing styles, 86
tasks, four harness-model combinations) and the headline finding
(conditional phrasing weaker; prescriptive/explanatory stronger but
harness-model-dependent) trace to the abstract text. Full paper (compliance
rates per condition) not read at capture.

## Updates

None yet.

## Related entries

None yet.
