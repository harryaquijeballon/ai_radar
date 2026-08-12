---
slug: 2026-liu-liveplan-programming-agent-monitoring
title: "Online Monitoring and Corrective Steering of Programming Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.06701
canonical_ids: ["arxiv:2608.06701"]
publisher_or_author: "Shuyang Liu, Saman Dehghan, Ji Young Kim, Jatin Ganhotra, Martin Hirzel, Reyhaneh Jabbarvand — arXiv preprint"
published: 2026-08-07
captured: 2026-08-10
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 5 (observability and debugging) and lens 1 (agent
  architecture): a concrete, quantified pattern for keeping long-running
  coding agents on track — a deterministic, LLM-free monitor paired with an
  advisor LLM invoked only when needed — evaluated on a standard benchmark
  (SWE-bench) with a stated, transferable trade-off (accuracy gain for
  modest added cost).
---

# Online Monitoring and Corrective Steering of Programming Agents

## Summary

Addresses a common failure mode in automated software-issue resolution:
agents fixing GitHub issues "drift away from their intended plan, repeat
failed actions, or terminate without a working patch." The paper proposes
LivePlan, which separates monitoring from correction: a deterministic,
rule-based monitor detects behavioral inefficiencies without invoking any
language model, while a separate advisor LLM issues corrections only when
the monitor flags a problem. Built on the SWE-agent framework and evaluated
across multiple LLMs on SWE-bench, LivePlan improves issue-resolution rates
by up to 15.2% over baseline approaches, with minimal added computational
cost, and shows particular effectiveness on medium- and hard-difficulty
instances.

## Why it matters

A reusable architectural pattern for anyone running long-lived coding or
tool-use agents in production: catch drift and repeated-failure loops with
cheap, deterministic rules instead of paying for a model call on every
step, and reserve the LLM's judgment for the moments the rules actually
flag. The quantified gain on a standard benchmark, with the cost trade-off
stated explicitly, makes this a concrete, evaluable design a team could
adopt this quarter rather than a general architecture opinion.

## Verification notes

arXiv abstract page fetched directly (2026-08-10); authors, submission date
(7 Aug 2026, v1), and category confirmed. All claims in the Summary — the
drift/repeat-failure/no-patch failure mode, the monitor/advisor split
design, the SWE-agent/SWE-bench evaluation setup, the up-to-15.2%
improvement, the "minimal additional computational cost" claim, and the
medium/hard-instance effectiveness — trace directly to the fetched abstract
text. No independent corroboration attempted (preprint, not yet peer
reviewed). Full paper PDF not read at capture.

## Updates

None yet.

## Related entries

None yet.
