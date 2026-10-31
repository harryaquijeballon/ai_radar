---
slug: 2026-assuncao-case-operational-context-validity
title: "When Relevant Code Is Wrong: Runtime-Aware Context for AI Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.38800
canonical_ids: ["arxiv:2610.38800"]
publisher_or_author: "Wesley K. G. Assunção, Ramesh Periyathambi — arXiv (cs.SE)"
published: 2026-10-28
captured: 2026-10-31
relevance:
  social_science: n/a
  ai_engineering: medium
rationale: >-
  On lens 2 (context engineering): names a real retrieval failure mode
  (semantically relevant but operationally stale/incompatible code) and
  proposes a validity criterion, but the evaluation is a six-task, 15-
  artifact preliminary study the authors themselves frame as a feasibility
  demonstration rather than a performance result — medium, not high.
verification: partial
---

# When Relevant Code Is Wrong: Runtime-Aware Context for AI Coding Agents

## Summary

Retrieval for AI coding agents usually prioritizes semantic similarity or
recency, but retrieved code may describe implementations that are inactive
or incompatible with the actual target deployment because of feature flags,
architectural migrations, or deployment-specific configuration. The authors
propose "operational context validity" — a criterion depending on task,
deployment, and time — for judging whether a piece of software evidence
should actually guide implementation. They present CASE, an agent-agnostic
framework that links repository artifacts to runtime configurations and
architectural history, labels evidence as valid/invalid/unknown, and
produces context packages that separate actionable guidance from historical
rationale and unresolved constraints. In a preliminary evaluation (six
tasks, 15 artifacts, three deployments), conventional retrieval presented 16
incompatible artifact occurrences as actionable; CASE excluded them while
keeping the applicable artifacts. Recency filtering alone reduced valid
recall to 0.43; removing feature-flag evidence reduced CASE's own valid
recall to 0.13. The authors present these results as evidence of
feasibility, not as a demonstrated improvement in coding-agent correctness.

## Why it matters

Names a specific, underexamined context-engineering failure mode —
retrieved code that is semantically relevant but operationally dead — and
gives it a vocabulary (operational context validity) and a mechanism
(linking artifacts to runtime configuration/history) that builders of
retrieval-augmented coding agents can watch for, even though the evidence
for CASE itself is still preliminary.

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.38800, v1 submitted
28 Oct 2026, cs.SE). The problem framing, the CASE mechanism description,
and the preliminary-evaluation numbers (6 tasks, 15 artifacts, 3
deployments, 16 incompatible occurrences, 0.43/0.13 recall figures) are
traced to the abstract text itself; the authors' own "feasibility, not
improvement" framing is carried into this entry rather than smoothed over.
Verification is marked `partial`: the claims are traced to the source, but
the load-bearing evaluation is explicitly small-scale and not independently
corroborated.

## Updates

None yet.

## Related entries

None yet.
