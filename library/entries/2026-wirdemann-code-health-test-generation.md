---
slug: 2026-wirdemann-code-health-test-generation
title: "Code Health in LLM-Based Test Generation: Effectiveness and Token Efficiency"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.18645
canonical_ids: ["arxiv:2608.18645"]
publisher_or_author: "Freya Wirdemann, Markus Borg, Nadim Hagatulah, Adam Tornhill — arXiv preprint (Engineering Track, IEEE SCAM 2026)"
published: 2026-08-19
captured: 2026-08-20
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On-lens for lens 7 (AI-assisted software development, measured results):
  a multi-language empirical study linking source-code maintainability to
  LLM-generated test quality and token cost, but the reported signal is
  explicitly described by the authors as weak.
---

# Code Health in LLM-Based Test Generation: Effectiveness and Token Efficiency

## Summary

An empirical study (accepted at the Engineering Track of IEEE SCAM 2026) investigating whether source-code maintainability — measured via CodeScene's CodeHealth metric — affects the quality of unit tests that LLM-based coding agents generate, across Python, Java, and C++. The study measures test effectiveness via coverage and mutation scoring, and input-token consumption across industrial tokenizers. Reported finding (quoted/paraphrased from the source): CodeHealth provides "a weak but consistent signal of LLM-generated test effectiveness," and higher CodeHealth is negatively correlated with input token count — i.e., more maintainable code produces moderately better generated tests while requiring fewer tokens to process.

## Why it matters

Teams deciding where to invest in code cleanup/refactoring ahead of adopting LLM-based test generation get a modest, evidence-based reason to prioritize maintainability: cleaner code appears both cheaper (fewer tokens) and slightly more amenable to good LLM-generated tests, across three languages. The effect is explicitly weak, so this should inform prioritization at the margin rather than justify a large standalone refactoring investment.

## Verification notes

Fetched arXiv abstract page 2608.18645 (submitted 2026-08-19, cs.SE, accepted IEEE SCAM 2026). Claims traced to the abstract/page summary: the CodeHealth metric, the three-language scope, the coverage/mutation-score effectiveness measures, and the "weak but consistent" correlation plus the token-count negative correlation. Not independently corroborated against the full paper or its results tables — no secondary source cross-checked, and exact correlation coefficients were not given in the fetched summary. Verification is partial.

## Updates

<!-- Append-only, dated, newest last. Never rewrite the Summary. -->

## Related entries

None yet.
