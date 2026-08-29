---
slug: 2026-metwalli-working-with-ai-coding-agents
title: "How to Work with AI Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/how-to-work-with-ai-coding-agents/
canonical_ids: []
publisher_or_author: "Sara A. Metwalli — Towards Data Science"
published: 2026-08-27
captured: 2026-08-29
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  A structured, five-element prompt framework and workflow sequence for
  directing coding agents — on lens 7 (AI-assisted software development),
  practically usable though it systematizes practice rather than presenting
  new evidence.
---

# How to Work with AI Coding Agents

## Summary
Metwalli prescribes a workflow sequence for directing coding agents: "Ask →
Inspect → Plan → Implement → Test → Review," instructing agents to first
examine a repository without modifications rather than requesting immediate
changes. She recommends replacing vague requests ("Build authentication")
with constrained ones ("Add email/password authentication. First inspect
the existing user and authentication code. Do not modify the database
yet.") and identifies five elements every agent instruction should specify:
goal, context (which files to examine), constraints (e.g., "Do not change
the public API"), acceptance criteria, and validation (testing commands).
She advises decomposing large tasks into testable increments rather than
requesting a full rewrite, and gives a decision rule for when to use an
agent versus a simpler assistant: agents for multi-step exploration tasks
with feedback loops, simple assistants for isolated questions.

## Why it matters
A concrete, adoptable prompt-structure checklist (five required elements,
an explicit workflow ordering) for anyone directing coding agents day to
day — complements this library's existing evidence-based findings on coding
agent reliability and harness design with a practitioner-level operating
procedure.

## Verification notes
Fetched directly from towardsdatascience.com (allowlisted). The workflow
sequence, the five-element framework, and the example prompts were
confirmed against the fetched source text. This is prescriptive practitioner
guidance rather than an empirical claim; no corroboration was required or
attempted beyond confirming the text matches the source.

## Updates
None yet.

## Related entries
None yet.
