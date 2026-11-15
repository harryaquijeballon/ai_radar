---
slug: 2026-raskin-ai-slop-pull-requests-foss
title: "An Empirical Study of Maintainer-Identified AI Slop Pull Requests in Free and Open Source Software Projects"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.15159
canonical_ids: ["arxiv:2611.15159"]
publisher_or_author: "Hugo Raskin, Xavier Devroey, Benoît Vanderose — arXiv preprint (cs.SE)"
published: 2026-11-11
captured: 2026-11-15
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Lens 7 (AI-assisted software development): an exploratory but quantified
  empirical study of maintainer-flagged "AI slop" pull requests across
  FOSS projects, with measured disclosure and closure-time figures —
  medium, since the authors themselves frame it as an early-stage,
  exploratory look rather than a validated intervention.
---

# An Empirical Study of Maintainer-Identified AI Slop Pull Requests in FOSS

## Summary
The study examines "AI slop" pull requests — low-quality, low-value PRs
generated with generative AI — in free and open source software projects,
focusing specifically on PRs that maintainers themselves flagged as slop.
Using mixed methods, the authors trace where these PRs come from, measure
their volume over time, describe their characteristics, and analyze why
maintainers closed or flagged them.

Reported findings: maintainer-identified AI slop PRs increased starting
mid-2025 and peaked in May 2026 (exact counts not given in the abstract).
These PRs are mostly additive, rarely merged, and typically closed within
3 days. Authors disclosed AI use in only 14% of cases, and just 1%
disclosed only after a maintainer asked. Most PRs were closed or marked as
slop with no reason given; where maintainers did give a reason, these
ranged from concrete problems (e.g., build failures) to subjective
judgments (e.g., the PR "looks AI to me"). The authors describe the work
as exploratory and an early-stage look at generative AI's effect on FOSS,
and argue the phenomenon adds pressure on maintainers and calls for
changes to current open-source practices (unverified beyond the authors'
own framing: no comparison to a pre-GenAI baseline rate of low-quality PRs
is reported in the abstract).

## Why it matters
Gives AI-engineering teams contributing to or maintaining open-source
projects concrete figures on how low AI-use disclosure is even among
maintainer-flagged slop PRs (14%, with only 1% prompted), and how fast
such PRs get closed (within 3 days) — useful context for setting
contribution norms or automated triage for agent-generated PRs, and a
data point on how disclosure norms are (or aren't) holding up in practice.

## Verification notes
Fetched the arXiv abstract page directly; the figures and claims above
(volume trend, additive/closure characteristics, 14%/1% disclosure rates,
closure-reason categories) trace to that text. The full paper's dataset
and methodology were not independently fetched or corroborated in this
session — verification is partial. No load-bearing claim here is
unverifiable in principle; none was independently corroborated.

## Updates
None yet.

## Related entries
None yet.
