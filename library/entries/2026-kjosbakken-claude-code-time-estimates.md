---
slug: 2026-kjosbakken-claude-code-time-estimates
title: "Why Claude Code Time Estimates Are Poor"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/why-claude-code-time-estimates-are-poor/
canonical_ids: []
publisher_or_author: "Eivind Kjosbakken — Towards Data Science"
published: 2026-08-28
captured: 2026-08-29
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Names a specific mechanism (training data reflects human, not
  AI-assisted, task durations) behind a common coding-agent failure mode and
  proposes two concrete mitigations — on lens 2 (harness and context
  engineering) and lens 5 (observability), practically usable for anyone
  relying on agent-generated time estimates.
---

# Why Claude Code Time Estimates Are Poor

## Summary
Kjosbakken argues Claude and similar LLMs systematically overestimate
coding-task duration — e.g., estimating "3-4 weeks of work" for a feature
that takes a single day with AI assistance — because "Claude is essentially
trained on human estimates of time": its training data (blog posts, GitHub
statistics) predates widespread AI-assisted coding and reflects
unassisted-human timelines. He proposes two mitigations: (1) maintain a
historical-data skill recording past tasks and their actual completion
times, which Claude can reference for comparable new estimates; (2) instruct
Claude to decompose work into subtasks and estimate each explicitly in terms
of LLM-assisted capability rather than human performance — useful even
without historical data, since smaller tasks are easier to estimate
accurately. He argues accurate estimates matter for team coordination
around dependent work.

## Why it matters
Names a specific, checkable cause (training-data provenance) for a
commonly observed coding-agent failure — bad time estimates — rather than
treating it as an unexplained quirk, and gives two concrete, low-effort
mitigations (a historical-task skill; LLM-calibrated subtask decomposition)
a team could adopt directly.

## Verification notes
Fetched directly from towardsdatascience.com (allowlisted). The mechanism
claim, the "3-4 weeks" vs. "single day" example, and both mitigations were
confirmed against the fetched source text. The causal claim (training data
reflects human, not AI-assisted, timelines) is the author's own inference,
not independently corroborated against Anthropic's training data or
documentation — labelled as the author's reasoning rather than a confirmed
fact.

## Updates
None yet.

## Related entries
None yet.
