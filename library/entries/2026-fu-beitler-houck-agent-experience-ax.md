---
slug: 2026-fu-beitler-houck-agent-experience-ax
title: "DevEx is for Humans, AX is for Agents: Measuring Context Health in Agentic Software Work"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.33480
canonical_ids: ["arxiv:2611.33480"]
publisher_or_author: "Gratiana Fu, Josh Beitler, Brian Houck — arXiv preprint"
published: 2026-11-24
captured: 2026-11-26
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Names a reusable measurement mechanism (Agent Experience / AX, scored on
  Clarity, Actionability, Fidelity, Efficiency) for diagnosing why agentic
  coding sessions fail, with quantified survey, pilot, and controlled-defect
  evidence — squarely lens 2 (harness and context engineering).
---

# DevEx is for Humans, AX is for Agents: Measuring Context Health in Agentic Software Work

## Summary

Coding agents succeed or fail based on the context humans provide, but most
evaluations only look at outputs. Drawing on developer-experience research,
the authors introduce Agent Experience (AX): an instrument that scores
session transcripts on four CAFE(S) dimensions — Clarity, Actionability,
Fidelity, and Efficiency (Security is treated as a gate, not a friction
dimension) — using a rubric-guided language-model rater that explains what
the human could have provided. Three studies: (1) in a Stack Overflow
Developer Survey analysis, respondents reporting context problems were
12–28% less likely to rate AI as very useful, across seven activities; (2)
in a pilot of 882 rated agentic sessions (from a sample of 1,000),
Actionability scored lowest (59.6% of ratings at 3 or lower, vs. 26.6% for
Fidelity) and ratings dropped in longer sessions; (3) in a controlled
experiment across 12 runs of a data-analysis task, every injected
context-defect condition increased token usage by a mean of 91% over the
clean baseline, and five evaluator models flagged 50–85% of targeted defect
dimensions but only 14–36% of non-targeted ones, with Fidelity defects
detected most consistently and Actionability defects least. The authors
describe the results as exploratory.

## Why it matters

A named, scoreable mechanism for a problem every agentic-coding team faces
but rarely measures directly: which specific kind of missing or bad context
is costing tokens and causing failures. The four-dimension rubric and the
controlled-defect protocol are both directly reusable for auditing a team's
own agent sessions or harness design, rather than only inspecting outputs or
final pass/fail outcomes — concrete mechanisms named and quantified, which
is exactly what lens 2 asks for.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.33480, v1 submitted
2026-11-24). The AX instrument description and all three studies' headline
figures above are traced to the abstract's own description. No independent
corroboration was available or attempted beyond the source text; the
authors themselves flag the findings as exploratory with imperfectly
isolated interventions, which is reflected in the summary above.

## Updates

None yet.

## Related entries

None yet.
