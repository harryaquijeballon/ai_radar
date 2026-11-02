---
slug: 2026-kitsios-cbdl-constrained-decoding-valid-imports
title: "No More Import Errors: Constrained Decoding for Guaranteed Valid Imports in LLM-Generated Tests"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.41878
canonical_ids: ["arxiv:2610.41878"]
publisher_or_author: "Konstantinos Kitsios, Matteo Biagiola, Guido Salvaneschi, Alberto Bacchelli"
published: 2026-10-30
captured: 2026-11-02
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation, validation and deterministic guardrails (lens 4): a
  named, implemented deterministic technique (Constrained Beam Decoding
  with Lookup) that guarantees a specific class of LLM output error
  (invalid imports) cannot occur, with quantified before/after numbers
  against both static and agentic-repair baselines across two languages —
  a pattern a builder could apply this quarter to any LLM code-generation
  pipeline with a similarly well-defined, grammar-checkable error class.
---

# No More Import Errors: Constrained Decoding for Guaranteed Valid Imports in LLM-Generated Tests

## Summary

Addresses import errors as a common cause of LLM-generated test failures.
Grammar-constrained decoding can guarantee syntactically/semantically
valid imports, but the authors report it can produce "import streaks" —
repetitive, technically-valid import statements that consume the model's
token budget before it writes the actual test body. They propose
Constrained Beam Decoding with Lookup (CBDL), implemented for both Python
and Java, which guarantees import validity while avoiding these streaks.
In their evaluation, CBDL-generated tests have 100% valid imports, versus
baselines that leave import errors unresolved in 45% (a static/RAG
baseline), 10% (LIBRO), and 43% (an agentic-repair baseline) of cases.
CBDL converts roughly 14% of initial import errors into functionally
correct tests outright, improving overall test correctness by 1-4
percentage points, and frees agentic-repair budget for the remaining
errors — adding a further 2-7 points for Python and 1-6 points for Java
when combined with agentic repair. A hybrid pipeline, where a small local
model handles imports via CBDL and GPT-5.2 writes the test body, beats
GPT-5.2 alone by 1-3 points. Reported overhead is 16-21 seconds per test
(all figures as stated in the fetched abstract; full implementation
details and benchmark construction not reviewed at capture).

## Why it matters

A concrete template for converting a well-defined LLM output-error class
into a deterministic guarantee rather than a post-hoc check: grammar
constraints alone are not sufficient (they can trade one failure, invalid
syntax, for another, wasted token budget), but a decoding-level technique
that accounts for that trade-off removes the error class entirely while
*improving* downstream correctness and leaving more repair budget for
errors that cannot be constrained away. Directly transferable to any LLM
code-generation or agentic pipeline with an analogous grammar-checkable
failure mode (e.g., malformed tool calls, invalid API signatures) where
teams currently rely on retries or agentic repair alone.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-02; single version,
submitted 30 Oct 2026, no revisions; primary category cs.SE, ACM class
D.2.5, CC BY 4.0, 12 pages/5 figures/6 tables per the page's own
comments). The CBDL mechanism, the 100%-valid-imports result, the
45%/10%/43% baseline comparison, the 14% conversion figure, the
1-4/2-7/1-6-point correctness improvements, the hybrid-pipeline result,
and the 16-21-second overhead all trace to the fetched abstract text —
the paper's own stated summary of its evaluation — treated as `verified`
on the convention applied elsewhere in this library to single-source
arXiv preprints whose headline figures are self-reported evaluation
output. The full implementation, benchmark suite, and statistical
analysis were not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
