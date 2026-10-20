---
slug: 2026-shi-xinyu-fault-localization-agentic-repair
title: "From Finding to Fixing: How Useful is Fault Localization for Agentic Program Repair?"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.25826
canonical_ids: ["arxiv:2610.25826"]
publisher_or_author: "Xinyu Shi et al."
published: 2026-10-20
captured: 2026-10-20
relevance:
  ai_engineering: high
  social_science: n/a
verification: partial
rationale: >-
  A large-scale (16,248-trajectory) empirical study overturning the
  assumption that more accurate fault localization reliably improves
  LLM-agent program repair, with a quantified, counter-intuitive token-cost
  finding — directly actionable for anyone building or evaluating agentic
  repair/debugging pipelines (lens 4, lens 5).
---

# From Finding to Fixing: How Useful is Fault Localization for Agentic Program Repair?

## Summary

The authors run a systematic empirical study of fault localization (FL) as a
component of LLM agent-based program repair. They test six recent FL methods
on SWE-bench Verified and Defects4J, using three LLMs within a common repair
framework, and analyze 16,248 repair trajectories; they also test
ground-truth ("gold") bug locations and bug-cause descriptions as upper-bound
guidance conditions.

Headline findings: FL methods did not consistently improve repair success,
and higher localization accuracy did not reliably translate into larger
repair gains. Accurate locations could cut repair token use by up to 39.2%,
but the FL methods tested often spent more tokens than they saved in
practice. FL did help agents search more effectively early in a repair
trajectory and reach relevant code sooner. FL appeared to have the most
potential when bug reports themselves contained fewer location clues already.
Providing bug-cause descriptions (not just locations) improved repair success
further, beyond locations alone. The authors also note that a single
ground-truth reference patch does not fully capture the range of locations
that successful repairs actually used.

## Why it matters

Challenges a common assumption in agentic-repair tooling — that investing in
better fault localization straightforwardly pays off — with a large,
controlled study rather than a single case. The practical lesson for
builders of repair/debugging agents: measure whether your FL step is
actually saving tokens net of its own cost, consider pairing or replacing
location information with bug-cause description, and do not assume
localization accuracy alone predicts repair quality.

## Verification notes

Read via the arXiv abstract page. The method (six FL methods, two
benchmarks, three LLMs, 16,248 trajectories, gold-location and bug-cause
ablations) and the findings above are stated in the abstract and traceable
to it. The full paper (per-method breakdowns, exact token-saving
calculations) was not fetched, so `verification: partial`.

## Updates

None yet.

## Related entries

None yet.
