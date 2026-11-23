---
slug: 2026-pachocki-openai-perplexity-intelligence-governance
title: "Perplexity and Intelligence"
status: accepted
domains: [social_science, ai_engineering]
source_type: primary
source_url: https://openai.com/index/perplexity-and-intelligence/
canonical_ids: []
publisher_or_author: "Jakub Pachocki — OpenAI"
published: 2026-11-22
captured: 2026-11-23
relevance:
  social_science: medium
  ai_engineering: medium
verification: verified
rationale: >-
  OpenAI's Chief Scientist proposes publishing pretraining perplexity
  numbers and tying cross-lab "common limits" to perplexity-linked
  capability thresholds — medium for ai_engineering lens 4/6 (a governance-
  pattern proposal with transferable eval lessons, not a builder recipe) and
  medium for social_science lens 4 (a concrete but unadopted cross-lab AI
  governance proposal, vendor-authored).
---

# Perplexity and Intelligence

## Summary

Jakub Pachocki, OpenAI's Chief Scientist, argues that most of modern AI
capability comes from training a predictor on large datasets, and that
perplexity (equivalently, cross-entropy loss) is a useful shared metric for
tracking progress toward transformative capabilities. He states OpenAI is
publishing its internal pretraining perplexity numbers as a step toward
shared safety standards, and ties specific log-perplexity thresholds to past
and anticipated capability jumps — for example, chain-of-thought reasoning
emerging around GPT-4, and transformative cybersecurity and mathematics
capabilities below a perplexity-loss threshold of 0.8. He warns that
AI-assisted pretraining research could accelerate progress sharply, and
proposes that frontier labs agree on "common limits" tied to perplexity and
other measures, not to be crossed until specific monitoring milestones are
met.

## Why it matters

For AI governance and policy readers, a concrete (if unilateral and
unadopted) proposal for a measurable, cross-lab capability-gating mechanism
— a specific trigger-plus-milestone governance pattern rather than general
calls for "safety standards." For AI engineers, several transferable
evaluation lessons: track one stable held-out metric over time since
benchmarks saturate quickly; watch for biased eval-set selection (the post
notes code perplexity was a poor proxy for GPT-2/GPT-3's general ability);
remember a static metric like perplexity misses gains from inference-time
techniques such as chain-of-thought; and make cross-party comparisons
explicit about differing eval sets and data mixes.

## Verification notes

Read directly from the source post
(openai.com/index/perplexity-and-intelligence/), dated 2026-11-22 on the
OpenAI news listing. The summarized claims (the perplexity-publication
commitment, the capability-threshold examples, the "common limits"
proposal) are taken directly from the fetched post text. No independent
corroboration sought — a first-party policy proposal, not an empirical
claim requiring external checking; treated per this profile's vendor-source
caveat (OpenAI has a direct stake in how its own safety commitments are
perceived).

## Updates

None yet.

## Related entries

None yet.
