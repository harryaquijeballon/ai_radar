---
slug: 2026-chase-langchain-tasks-to-goals
title: "From Tasks to Goals"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://www.langchain.com/blog/from-tasks-to-goals
canonical_ids: []
publisher_or_author: "Harrison Chase — LangChain blog"
published: 2026-11-16
captured: 2026-11-17
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 1 (agent architecture and orchestration): an architecture
  opinion piece, not evidence-backed, but it names concrete design
  consequences of moving from task-driven to goal-driven agents (tighter
  tool-call controls, a clarification channel for unsupervised agents,
  built-in feedback signals, trigger/stop-rule controls, cross-run memory)
  — discounted per profiles/ai_engineering/sources.md for framework-vendor
  promotion.
---

# From Tasks to Goals

## Summary
Argues that agents are shifting from executing bounded, pre-specified tasks
to pursuing ongoing goals the agent itself decomposes into tasks, revising
its plan as it goes. The post lists the design consequences it says this
shift forces: because the agent chooses the work, it needs good
brainstorming and visibility into its own to-do list; because tool use
becomes less predictable with a goal than a task, agents need tighter
controls over which tools they can call; because background agents are not
always supervised in chat, they need a channel (e.g., Slack, a dedicated
inbox) to ask clarifying questions; because metrics alone can mislead,
feedback loops need built-in human correction of what "success" means;
goal-driven agents need trigger mechanisms (heartbeats, cron jobs, event
streams) paired with controls to pause or ignore triggers so they do not
become noisy; and agents need memory that carries decisions and feedback
across runs. The author's framing: delegating a goal moves the human's role
from specifying each step to setting direction, defining boundaries, and
reviewing progress (unverified: the post is argued from the author's
experience, not backed by a study or benchmark).

## Why it matters
Gives a builder deciding whether to move an agent from a fixed task list to
open-ended goal delegation a concrete checklist of what has to change
(tool-permission scope, a clarification channel, explicit feedback signals,
trigger/stop controls, cross-run memory) rather than a general argument that
"agents are getting more autonomous."

## Verification notes
Fetched and read in full from the primary source (langchain.com/blog);
author (Harrison Chase), 2026-11-16 publish date, and all six listed design
consequences trace directly to the fetched post text. No load-bearing
statistic is made — the post is an opinion/pattern piece, discounted per
the ai_engineering sources profile's framework-vendor-promotion note — so no
external corroboration was sought.

## Updates
None yet.

## Related entries
None yet.
