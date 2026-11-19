---
slug: 2026-zhao-reliability-user-specific-llms
title: "Reliability is a user-specific property of large language models"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.23732
canonical_ids: ["arxiv:2611.23732"]
publisher_or_author: "Xingyu Zhao — arXiv preprint (cs.SE)"
published: 2026-11-18
captured: 2026-11-19
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 4 (evaluation and validation): a position/roadmap paper
  arguing capability benchmarks aren't reliability claims, drawing a
  useful distinction (testing for fault discovery vs. testing for
  reliability assessment) and naming ten modelling considerations and six
  research workstreams, but its own integrated validation is explicitly
  still an open task — framework-level context, not yet a usable method.
---

# Reliability is a user-specific property of large language models

## Summary

Argues that public capability benchmarks rank LLMs in the aggregate, but
the same model can behave very differently for different users and
conditions of use, so a capability score alone is not a reliability claim.
Drawing on traditional software reliability engineering, the author
separates testing for fault discovery from testing for reliability
assessment, and proposes that reliability claims should be specific,
versioned, operational statements — whose requirements are covered, under
what conditions, with what uncertainty — rather than a single number. The
paper identifies ten modelling considerations for such claims and lays out
a six-workstream research roadmap: claim specification, dynamic
operational profiles, graded outcomes under noisy judgements, local
probabilistic robustness (addressing behavioural variation hidden when
different concrete inputs are treated as the same task), interaction
dependence, and statistical inference with reassessment. It motivates the
roadmap with published findings and an illustrative customer-support
example, states that reliability claims complement rather than replace
separate safety and security arguments, and explicitly flags that
integrated empirical validation of the roadmap is still an open research
task.

## Why it matters

For anyone deciding whether a benchmark-leading model is actually reliable
enough for their specific deployment: a disciplined vocabulary for why
"it scores well on the leaderboard" is a different and weaker claim than
"it will behave acceptably for this user, under these conditions, with
this much confidence" — and a named list of the modelling gaps (especially
treating distinct concrete inputs as one task, hiding real behavioural
variation) that make the difference concrete. Most useful today as a
checklist for what a rigorous internal reliability claim should specify,
ahead of any tool that automates it.

## Verification notes

arXiv abstract page fetched directly (2026-11-19); title, author,
"Submitted on 18 November 2026, 02:44:28 UTC" date, and cs.SE (primary) /
cs.AI subject categories confirmed. Every claim in the Summary, including
the paper's own statement that integrated validation remains an open
research task, traces to the fetched abstract text. Full paper body not
read at capture; no independent corroboration attempted (position/roadmap
paper, no secondary coverage found). Appeared in arXiv's cs.SE "recent"
listing dated Thu, 19 Nov 2026, one day after its 18 Nov 2026 submission —
normal next-day announcement lag, within the 7-day eligibility cap.

## Updates

None yet.

## Related entries

None yet.
