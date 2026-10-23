---
slug: 2026-hashemi-llm-herding-cascades
title: "LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.30769
canonical_ids: ["arxiv:2610.30769"]
publisher_or_author: "Farnoosh Hashemi et al."
published: 2026-10-22
captured: 2026-10-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 5 (observability and debugging) and lens 6
  (reproducibility/governance): identifies a concrete failure mode — social
  herding and runaway cascades — in LLM multi-agent systems exposed to each
  other's cumulative choices, with a rigorous experimental design borrowed
  from a classic social-science paradigm. Practical implication: avoid
  exposing agents to raw cumulative-choice signals from other agents without
  dampening. Verification held at `partial` because the abstract gives no
  effect sizes.
---

# LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades

## Summary
The paper studies herding behavior and runaway cascades in LLM multi-agent
systems: because agents respond to each other's choices, feedback loops can
form that make the collective vulnerable to social influence. The authors
replicate the design of the classic Music Lab experiment, testing large
populations of LLM agents recommending unfamiliar songs under two
conditions — with and without exposure to cumulative recommendation counts
from other agents.

When agents could see cumulative counts, the populations produced runaway
cascades: their collective recommendations became extreme and
unpredictable, and increasingly diverged from each song's intrinsic appeal.
Compared with the human populations in the original Music Lab study, the
LLM populations were generally more susceptible to herding and less able to
self-correct. The abstract does not report specific effect sizes or numeric
divergence measures.

## Why it matters
This is a named, experimentally grounded failure mode for any multi-agent
system design that exposes agents to each other's aggregate or cumulative
choices (voting counts, popularity signals, prior-agent outputs surfaced as
social proof) — a pattern increasingly common in agent-orchestration and
consensus designs. The practical lesson for builders is to treat
cumulative-signal exposure between agents as a designed risk surface:
either dampen/withhold raw cumulative counts or add explicit
de-correlation mechanisms, since LLM agents appear less able than humans to
resist herding once exposed.

## Verification notes
Read directly from the arXiv abstract page (arXiv:2610.30769, v1, submitted
22 Oct 2026, 05:42:55 UTC). The paper's method (Music-Lab-style experimental
replication, with/without cumulative-count exposure) and qualitative
findings (cascades, increased herding susceptibility relative to humans,
reduced self-correction) are stated directly in the abstract and traceable
to it. Verification is `partial` rather than `verified`: no specific
quantified effect sizes are given in the abstract to independently check,
so the finding is traceable but not corroborated against numeric evidence
in this run. No load-bearing claim is unverifiable outright, so the entry
clears `accepted`.

## Updates

- None yet.

## Related entries
None yet.
