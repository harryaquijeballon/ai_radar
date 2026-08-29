---
slug: 2026-guo-codex-subagents-pattern
title: "From One Agent to a Team: Understanding Codex Subagents"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/from-one-agent-to-a-team-understanding-codex-subagents/
canonical_ids: []
publisher_or_author: "Shuai Guo — Towards Data Science"
published: 2026-08-28
captured: 2026-08-29
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  A concrete, reproducible walkthrough of Codex CLI's subagent-delegation
  mechanism (config format, parallel execution, inspection tooling) — on
  lens 1 (agent architecture and orchestration), useful worked-example depth
  though the underlying pattern (parallel specialist subagents synthesized
  by a main agent) is not itself novel.
---

# From One Agent to a Team: Understanding Codex Subagents

## Summary
Guo walks through Codex CLI's subagent mechanism: subagents are defined in
TOML files under `.codex/agents/`, each requiring `name`, `description`, and
`developer_instructions` fields. In a worked travel-planning example, three
specialist agents (travel logistics, budget analyst, experience researcher)
each evaluate candidate destinations from their own perspective. The main
agent is instructed to "use the `travel_logistics`, `budget_analyst`, and
`experience_researcher` agents in parallel. Each agent should evaluate all
three destinations," runs up to three subagent threads concurrently
(configurable via `.codex/config.toml`), then synthesizes — "collected
individual responses and recommended Lisbon as the best balance" — rather
than merely concatenating subagent outputs. Individual subagent threads are
inspectable via the `/agent` CLI command, showing context, tool activity,
and eventual result. Guo characterizes the pattern as useful "when a task
contains several different types of work that can be completed independently
and then combined."

## Why it matters
A concrete, reproducible reference for one harness's (Codex CLI) native
subagent-delegation primitives — configuration format, concurrency limits,
and inspection tooling — useful as a comparison point for anyone evaluating
or building parallel-specialist-subagent patterns in their own harness,
even though the underlying architectural idea (decompose, delegate to
role-specialized subagents, synthesize) is already well represented in this
library.

## Verification notes
Fetched directly from towardsdatascience.com (allowlisted). The TOML
configuration fields, the concurrency limit, the delegation instruction
text, and the synthesis description were confirmed against the fetched
source text. This is a first-person walkthrough of the author's own use of
a documented product feature; no external claim requiring corroboration is
made.

## Updates
None yet.

## Related entries
None yet.
