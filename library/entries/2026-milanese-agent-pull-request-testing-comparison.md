---
slug: 2026-milanese-agent-pull-request-testing-comparison
title: "Testing with Coding Agents: A Large-Scale Comparison of Agent-Supported and Human-Authored Pull Requests"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.35297
canonical_ids: ["arxiv:2610.35297"]
publisher_or_author: "Roberto Milanese, Francesco Salzano, Hovhannes Muradyan, Jingjing Wu, Remo Pareschi, Fausto Fasano, Mattia Fazzini"
published: 2026-10-26
captured: 2026-10-27
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on AI-assisted software development (lens 7): a large-N (114,134
  pull requests, 391 repositories), statistically modelled comparison of
  how agent-supported and human-authored pull requests differ in testing
  practice — measured results a team could use to judge what to monitor
  when coding agents touch test code.
---

# Testing with Coding Agents: A Large-Scale Comparison of Agent-Supported and Human-Authored Pull Requests

## Summary

Compares pull requests developers make with coding-agent assistance
against those written entirely by humans. The authors examine 114,134
merged pull requests from 391 Java repositories, January 2025 to April
2026, across five areas: how often and how much test code changes, the
type and context of those changes, test structure, test smells, and code
coverage. Using mixed-effects models fitted within each repository, they
report that agent-supported pull requests add tests more often and modify
or delete existing tests less often than human-authored ones. Structural
differences between the two groups are reported as mostly absent, and
coverage differences appear only in test-only pull requests. The authors
conclude that agent involvement is associated with a different mix of
testing work, while its net effect on test quality remains uncertain
(figures and conclusions as stated in the fetched abstract; full
regression specifications and the repository sample were not reviewed at
capture).

## Why it matters

A large-sample, statistically controlled answer to a question teams
adopting coding agents actually face: do agent-assisted pull requests
change testing behaviour, and how? The reported pattern — more test
additions, fewer test deletions/modifications, coverage differences
confined to test-only PRs — gives a concrete, falsifiable baseline for
teams to check their own agent-assisted workflows against, rather than
anecdote.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-27; single version,
submitted 26 Oct 2026). The sample size (114,134 PRs, 391 repositories),
date range (Jan 2025–Apr 2026), the five analysis areas, the mixed-effects
modelling approach, and the stated findings (more test additions, fewer
deletions/modifications, coverage differences confined to test-only PRs)
all trace to the fetched abstract text. The full statistical specification,
repository selection criteria, and robustness checks were not reviewed —
load-bearing figures are traced to the source's own stated summary but not
independently corroborated.

## Updates

None yet.

## Related entries

None yet.
