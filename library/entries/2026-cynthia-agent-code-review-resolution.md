---
slug: 2026-cynthia-agent-code-review-resolution
title: "\"Go Home Copilot, You're Drunk\": Understanding Developer Responses to Agent-Generated Code Review Comments"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.21997
canonical_ids: ["arxiv:2607.21997", "doi:10.48550/arXiv.2607.21997"]
publisher_or_author: "Shamse Tasnim Cynthia, Ratnadira Widyasari, Banani Roy, Ting Zhang, David Lo — arXiv preprint (cs.SE)"
published: 2026-07-24
captured: 2026-07-27
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on the AI-assisted-software-development lens: the first large-scale
  empirical study (54,791 comments, five widely used coding agents, 342
  repositories) of how developers actually resolve agent-generated code
  review comments, with a qualitative taxonomy (ten discussion patterns for
  unresolved comments) and a clear, directly actionable predictor (inline
  code suggestions strongly predict resolution; long/complex comments do
  not) — measured results a team building or tuning an AI code-review
  feature could apply immediately.
---

# "Go Home Copilot, You're Drunk": Understanding Developer Responses to Agent-Generated Code Review Comments

## Summary

Presents the first large-scale empirical study of how developers resolve
AI-agent-generated code review comments, analyzing 54,791 comments from
five widely used coding agents (Copilot, Cursor, Codex, Devin, Claude)
across 342 Python repositories on GitHub. Examines resolution rates across
agents and comment types, the role of developer experience, and what makes
a comment more likely to be acted on. Findings: resolution rate varies
considerably by agent, with Copilot accounting for the majority (72.9%) of
resolved comments; core developers resolve most agent feedback, especially
design/evolvability comments, while peripheral developers more often
resolve functional-defect comments. Through open card sorting of 470
unresolved comment discussions, the authors identify ten discussion
patterns explaining non-resolution, the most prevalent being incorrect
suggestions and intentional design decisions. The strongest predictor of
comment resolution is the presence of an inline code suggestion; lengthy,
complex comments are less likely to be acted on.

## Why it matters

Directly actionable design guidance for anyone building or tuning an
AI-generated code review feature: attach an inline, concrete code
suggestion rather than a prose explanation, and keep comments short — both
measurably predict whether a developer acts on the feedback. The ten-pattern
taxonomy of why comments go unresolved (led by incorrect suggestions and
intentional design decisions) is a ready-made checklist for triaging or
suppressing low-value automated review comments before they reach a
developer.

## Verification notes

arXiv abstract page fetched directly (2026-07-27); title, authors,
"Submitted Fri, 24 Jul 2026 05:51:48 UTC", category (cs.SE) confirmed.
Every claim in the Summary — the study scale, the per-agent resolution
rates, the developer-experience finding, the ten discussion patterns, and
the inline-suggestion predictor — traces directly to the abstract text,
the primary source for this pre-publication preprint. Full paper text not
read at capture, so the ten discussion patterns themselves and the
statistical model behind "strongest predictor" are unverified beyond the
abstract's summary. Upgrade path: read the full PDF for the card-sorting
codebook and the predictive model's specification.

## Updates

None yet.

## Related entries

[2026-mazloomzadeh-agentic-pull-requests](2026-mazloomzadeh-agentic-pull-requests.md) — same broader empirical-SE-on-coding-agents theme, at the pull-request level rather than the comment level.
