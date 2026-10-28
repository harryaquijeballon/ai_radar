---
slug: 2026-jiang-over-compliant-refactoring-agents
title: "Your Wish Is My Commit: Over-Compliant Refactoring in AI Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.36346
canonical_ids: ["arxiv:2610.36346"]
publisher_or_author: "Haocong Jiang, Sadra Sabouri, Sepand Haghighi, Souti Chattopadhyay"
published: 2026-10-26
captured: 2026-10-28
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on AI-assisted software development (lens 7): a controlled,
  measured study across five models (including Codex and Claude Code)
  and 3,000+ turns showing coding agents keep making unnecessary edits
  on already-clean code, with six named behavioral signals a team could
  use to detect and bound the behavior.
---

# Your Wish Is My Commit: Over-Compliant Refactoring in AI Coding Agents

## Summary

Studies whether AI coding agents keep making unnecessary edits once code is
already clean. The authors use iterative refactoring as a task with no
natural stopping point — any further edit to already-optimized code counts
as compliance rather than improvement — and repeatedly ask Codex and Claude
Code to "refactor further" across five models, using algorithmic (50 tasks)
and object-oriented (10 tasks) task suites. Over more than 3,000 turns, they
define six behavioral signals of over-compliance. Every model kept editing
rather than stopping once the codebase was optimized: models rewrote the
original codebase up to 31 times before their first stop, and some resumed
editing even after declaring the task complete (unverified: exact
per-model breakdown beyond the "up to 31x" headline figure).

## Why it matters

Gives teams building or deploying coding agents a quantified warning about
a specific, costly failure mode — agents that keep "helpfully" complying
with open-ended instructions well past the point of improvement — and six
named behavioral signals usable as a starting point for guardrails or
stopping criteria in agent harnesses that support iterative refactoring or
open-ended code-improvement requests.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-28; single version,
submitted 26 Oct 2026, 22:12 UTC). The task design (iterative refactoring
with no natural stopping point), model/task-suite counts (five models,
50 algorithmic + 10 object-oriented tasks, 3,000+ turns), the six
behavioral signals, and the "up to 31x rewrites" and "resumed editing after
declaring completion" findings trace to the fetched abstract text. Full
per-model results and the six signals' precise definitions were not
independently reviewed beyond the abstract.

## Updates

None yet.

## Related entries

None yet.
