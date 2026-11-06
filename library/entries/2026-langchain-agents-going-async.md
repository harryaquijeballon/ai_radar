---
slug: 2026-langchain-agents-going-async
title: "Agents Are Going Async"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://www.langchain.com/blog/agents-are-going-async
canonical_ids: []
publisher_or_author: "Sydney Runkle, Thushanth Bengre — LangChain blog"
published: 2026-11-05
captured: 2026-11-06
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On lens 1 (agent architecture and orchestration): names a concrete
  pattern (orchestrator agent plus background async subagents, five
  control primitives, configurable interrupt/enqueue update strategy) for
  keeping an agent responsive during long-running work; medium per the
  profile's own rule for architecture opinion pieces, since no benchmark
  or trade-off evidence is given and the vendor has an interest in
  promoting its own agent framework.
---

# Agents Are Going Async

## Summary

The post argues that a single synchronous ReAct loop cannot both stay
responsive to a user and make progress on many long-running sub-tasks at
once, because a slow tool call blocks the loop and everything queued
behind it. It proposes splitting an agent into an orchestrator that stays
with the user and background async subagents that do the long work,
started like a background job that returns immediately and reports back
later. The orchestrator manages subagents through five control
primitives: start, check, update, cancel, and list. An `update_strategy`
setting controls what happens when new instructions arrive mid-task:
"interrupt" restarts the subagent with the new instructions, "enqueue"
waits for the current run to finish first. Subagents notify the
orchestrator differently depending on whether it is busy, idle, or paused
on an approval step. The authors suggest the same asynchronous pattern
could extend to tool calls generally, citing OpenAI's async tool calling
as a parallel, and note the LangChain feature (task notifications) is in
beta with an API that may still change.

## Why it matters

Names a specific, reusable architectural vocabulary — orchestrator vs.
background subagent, the five control primitives, and the
interrupt-vs-enqueue update-strategy choice — for a problem (long-running
agent work vs. user responsiveness) that any multi-step research or
policy-simulation pipeline running many sub-tasks in parallel will hit.
Useful as a design-pattern reference even without benchmark evidence,
provided a builder independently validates throughput/responsiveness
claims for their own workload rather than taking the "capacity grows with
background workers" framing on faith.

## Verification notes

Fetched the primary post directly; the architecture description, control
primitives, and update-strategy semantics are stated in the post and
traced directly to it. The post's own framing claim — that system
capacity "grows with the number of background workers" — is explicitly
unsupported by any benchmark, throughput number, or comparison in the
post itself and is marked here as (unverified) assertion, not a measured
result. Discounted per `profiles/ai_engineering/sources.md`'s
framework-vendor-promotion policy: LangChain is describing its own
product feature.

## Updates

None yet.

## Related entries

None yet.
