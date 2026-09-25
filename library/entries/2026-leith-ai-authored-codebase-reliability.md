---
slug: 2026-leith-ai-authored-codebase-reliability
title: "Between the Commits: Process, Error, and Claim Reliability in a Wholly AI-Authored Codebase"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2609.29744
canonical_ids: ["arxiv:2609.29744"]
publisher_or_author: "Douglas Leith — arXiv preprint"
published: 2026-09-24
captured: 2026-09-25
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 7 (AI-assisted software development): a single-codebase,
  process-level empirical trace of a substantial application written
  entirely by an AI coding agent with no human-authored code or tests,
  yielding quantified error rates a team running a similar workflow could
  use as a reliability baseline.
---

# Between the Commits: Process, Error, and Claim Reliability in a Wholly AI-Authored Codebase

## Summary

The author studies a roughly 21,000-line Python application built entirely
by Claude, with no human-authored code or tests, introducing code-provenance
tracing tools and three taxonomies covering instruction intent, commit
origin, and response dependability. The study finds that CLI-based
instructions emphasize "comprehension, planning and consultation" more than
IDE-chat interactions, and that development was predominantly proactive
(agent-initiated) rather than purely reactive to human requests. Quantified
reliability findings: "14.3% of AI code-generation events contain a real
error later caught by the AI-authored test suite," and roughly one in
four-to-five of the agent's interactive responses included at least one
factual error.

## Why it matters

Most AI-assisted-coding studies compare human-plus-AI workflows or
benchmark task completion; this instead traces process and error rates
inside a single, real, wholly-AI-authored codebase over its full
development history — giving a concrete reliability baseline (how often
generated code contains an error the AI's own tests catch, how often
interactive responses contain factual errors) that a team adopting a
similar "AI writes everything" workflow could use to calibrate how much
independent verification to budget for (lens 7, and directly relevant to
lens 4's guardrail-design concerns).

## Verification notes

Fetched directly from the arXiv abstract page (2609.29744; v1 submitted
Thursday, 24 September 2026, 12:59:20 UTC — within this run's discovery
window). The codebase scale (~21,000 lines), the taxonomy structure, the
14.3% code-generation-error rate, and the ~1-in-4-to-5 factual-error rate in
interactive responses trace directly to the abstract's own quoted text.
Full paper (the taxonomy definitions in detail, the tracing-tool
methodology) not read at capture.

## Updates

None yet.

## Related entries

None yet.
