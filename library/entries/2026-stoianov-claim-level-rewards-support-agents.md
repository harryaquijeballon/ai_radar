---
slug: 2026-stoianov-claim-level-rewards-support-agents
title: "Learning from Unreliable Operator References: Claim-Level Rewards for Customer Support Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.34341
canonical_ids: ["arxiv:2611.34341"]
publisher_or_author: "Dmitrii Stoianov, Olga Tsymboi, Danil Taranets, Daniil Strizhakov, Ilya Buryak, Almaz Dautov, Dmitry Fatnev, Arthur Babkin, Aleksandr Fida, Daniil Dryabin, Maksim Shilenko, Nikita Surnachev, Anatolii Potapov — arXiv preprint"
published: 2026-11-25
captured: 2026-11-27
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  A real-world-validated training signal design (claim-level, evidence-
  checked rewards instead of imitating operator text) that cuts
  hallucinations and raises deployed containment, with both an offline
  benchmark and a randomized online A/B test — lens 4 (evaluation and
  deterministic guardrails) with lens 8 relevance (reliable AI products
  grounded against evidence rather than imitated reference text).
---

# Learning from Unreliable Operator References: Claim-Level Rewards for Customer Support Agents

## Summary

Training a customer-support agent to imitate human operator replies
inherits the operators' own errors: the authors find that about a quarter
of the factual claims in operator replies lack full support in the
knowledge base and tool records available to them. Rather than treat
operator replies as answers to imitate, the authors treat them as claims to
verify: unverified claims guide revisions to the knowledge base and tools,
while verified claims become coverage targets in a claim-level GRPO reward
that scores factual precision against the evidence the agent itself
retrieved. In an offline benchmark, 8.6% of the GRPO-trained agent's text
answers were flagged for hallucinations, versus 13.6% for a supervised
fine-tuning baseline trained to imitate operator text. In a randomized
online A/B test against the existing procedural bot, the share of
conversations closed without a human operator rose from 63.3% to 80.8%.
(unverified beyond the abstract: the exact definition of "full support" in
knowledge-base/tool records and the composition of the "existing procedural
bot" baseline, which would require the full 31-page paper.)

## Why it matters

A transferable lesson for anyone training or evaluating support, research,
or policy-advice agents against human-written reference text: correct-
*sounding* human references can still be factually unsupported, so
training signals that verify claims against retrieved evidence (rather than
imitating reference text) both reduce hallucination and improve real-world
outcomes — validated here with a live randomized A/B test, not just an
offline metric.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.34341, v1 submitted
2026-11-25, cs.CL). The methodology (claim verification, claim-level GRPO
reward) and the quantified figures above (~25% unsupported operator claims;
8.6% vs. 13.6% hallucination rate; 63.3%→80.8% containment) are traced to
the abstract's own description as summarized by the fetch tool. No
independent corroboration was attempted; verification is partial pending a
full-text read.

## Updates

None yet.

## Related entries

None yet.
