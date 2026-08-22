---
slug: 2026-bhardwaj-llm-judge-agreeing-with-itself
title: "The LLM Judge That Kept Agreeing With Itself"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/the-llm-judge-that-kept-agreeing-with-itself/
canonical_ids: []
publisher_or_author: "Priyansh Bhardwaj — Towards Data Science"
published: 2026-08-20
captured: 2026-08-22
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Squarely on lens 4 (LLM-as-judge validity, the core lens for the
  policy-simulation interest): grounds the case for not trusting an
  LLM-judge as a neutral arbiter in a real production incident, quantifies
  judge-human agreement, and gives a concrete three-step remediation
  framework — directly applicable to any pipeline that gates production
  decisions on an LLM judge.
---

# The LLM Judge That Kept Agreeing With Itself

## Summary

Argues that using an LLM to judge another LLM's outputs introduces
systematic biases that undermine the judge's reliability as a neutral
arbiter: (1) self-preference bias, where a judge rates outputs from its own
model family higher, attributed to "perplexity familiarity"; (2) verbosity
bias, where longer responses score higher independent of correctness; (3)
position bias, where the order outputs are presented in affects comparative
judgments. The argument is grounded in a production incident where an
LLM-judge approved a flawed SQL query that a human reviewer would have
caught. The author compares judge decisions against human-reviewer
assessments on held-out samples across queries from different generator
models, finding judge-human agreement in the "low-to-mid 80s" percent
range, with the weakest agreement concentrated on subtly incorrect
queries — precisely the failure mode that caused the incident. Proposes a
three-step remediation: (1) use a judge model from a different family than
the generator; (2) revise judging rubrics to explicitly penalize
unnecessary length; (3) run continuous human-calibration loops targeted at
the categories where judge-human agreement is weakest.

## Why it matters

Gives builders of any evaluation pipeline that uses an LLM-as-judge (for
research-agent outputs, policy analysis, or code review) a concrete,
falsifiable checklist for where that judge is likely to be wrong — subtly
incorrect but fluent outputs — and three specific, low-cost mitigations.
Directly actionable for anyone using LLM judges to gate automated decisions
in a research or policy product, the profile's standing reliability
interest.

## Verification notes

Article fetched and read directly (2026-08-22); the author, the 2026-08-20
publication date, the three named biases, the production SQL incident, the
"low-to-mid 80s" percent judge-human agreement figure, and the three-step
remediation framework all trace to the fetched article text. `partial`
rather than `verified`: the agreement percentage and incident are the
author's own reporting on their own production pipeline, not independently
reproduced or corroborated this run; the underlying bias claims
(self-preference, verbosity, position bias) are well-established findings
in the LLM-judge literature and are not themselves load-bearing novel
claims.

## Updates

None yet.

## Related entries

None yet.
