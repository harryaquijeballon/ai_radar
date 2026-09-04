---
slug: 2026-corvoysier-funes-coding-agent-memory
title: "Give Your Coding Agents a Memory You Own"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://huggingface.co/blog/funes
canonical_ids: []
publisher_or_author: "David Corvoysier — Hugging Face blog"
published: 2026-09-03
captured: 2026-09-04
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Introduces a concrete, quantified pattern for persisting coding-agent
  session reasoning as retrievable memory (lens 2, harness/context
  engineering) rather than losing it to compaction or handoff notes; the
  author's own benchmark on two tasks is the only evidence available.
---

# Give Your Coding Agents a Memory You Own

## Summary
"funes" is a tool by David Corvoysier that indexes coding-agent session traces (from tools such as Claude Code and Codex) into a searchable, retrievable memory store, so an agent's past reasoning and decisions can be recalled in later sessions or on other machines instead of disappearing when a session ends. The memory works locally by default, with no external service required, and can optionally be shared via private Hugging Face datasets. The post benchmarks three ways of giving a long-running agent access to earlier context — default compaction, written handoff notes, and funes's indexed "recall" — measured as weighted tokens spent per successfully completed task, on two test tasks. Recall was 8x cheaper than written handoffs on one task and 4x cheaper on the other; compaction "arrived on one task and never arrived on the other" (the author's own phrasing for an uneven completion outcome).

## Why it matters
Agent harnesses built for long-horizon or multi-session research and policy work routinely hit context limits, and the default responses — lossy compaction or hand-written handoff notes — are exactly the failure-prone mechanisms lenses 2 and 5 of this profile flag. A working pattern for turning agent traces into indexed, queryable memory, backed by even a small quantified cost comparison against the status quo, is directly usable by anyone building long-horizon agentic pipelines.

## Verification notes
Fetched and read directly from huggingface.co/blog/funes. The tool's mechanism (session-trace indexing, local-first storage, optional Hugging Face dataset sharing) and the benchmark numbers (8x/4x cheaper recall, compaction's uneven completion) are traceable to the post's own text and chart. The benchmark is the author's own, run on two unnamed tasks with no third-party replication or corroboration — a load-bearing but self-reported claim, so verification is recorded as `partial` rather than `unverified`: the mechanism and numbers are directly stated and traceable, just not independently checked.

## Updates
None yet.

## Related entries
None yet.
