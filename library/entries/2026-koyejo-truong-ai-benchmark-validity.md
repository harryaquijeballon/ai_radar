---
slug: 2026-koyejo-truong-ai-benchmark-validity
title: "The Tests That Grade AI May Be Getting It Wrong"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://hai.stanford.edu/news/the-tests-that-grade-ai-may-be-getting-it-wrong
canonical_ids: ["arxiv:2605.17173"]
publisher_or_author: "Sanmi Koyejo & Sang Truong — Stanford HAI"
published: 2026-09-25
captured: 2026-09-26
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails):
  applies measurement-science/psychometric validity testing to 56 widely
  used AI benchmarks and a Multi-Group IRT framework to cross-lingual
  safety evals, giving builders two transferable methods for auditing
  whether a benchmark measures what it claims before trusting its score.
---

# The Tests That Grade AI May Be Getting It Wrong

## Summary

A Stanford HAI news article covering two COLM 2026 papers by Sanmi Koyejo,
Sang Truong and coauthors on benchmark validity. The first, "What AI
Benchmarks Actually Measure: Adapting Convergent and Discriminant Validity
to Interrogate Fifty-Six AI Benchmarks" (OpenReview submission, no arXiv
preprint yet), applies psychometric convergent/discriminant validity
testing to 56 widely used AI benchmarks and finds that benchmarks claiming
to measure the same property often disagree with each other, and that
benchmarks frequently fail to measure their stated target — for example,
the BBQ bias benchmark can be passed either by genuinely lacking bias or by
recognizing "trick questions," making it primarily measure reading
comprehension rather than bias. The second, "Why Do Safety Guardrails
Degrade Across Languages?" (Zhang, Patel, Truong, Koyejo — arXiv:2605.17173,
v1 2026-05-16, v2 2026-08-11), analyzes 1.9 million model responses across
61 model configurations and 10 languages using a Multi-Group Item Response
Theory (IRT) framework separating language-agnostic robustness, prompt
difficulty, language complexity, and cross-lingual safety gaps; it finds
safety operates through a shared cross-lingual mechanism rather than
language-specific pathways, that 22 of the models studied are paradoxically
more vulnerable in English than in some low-resource languages, and that
translating a "safety" prompt can itself inject construct-irrelevant
difficulty that a benchmark then mistakes for a genuine safety gap.

## Why it matters

Gives builders two concrete, transferable audit methods (lens 4) for their
own eval suites rather than a single new benchmark: psychometric
convergent/discriminant validity testing to check whether two benchmarks
that claim to measure the same property actually agree (the BBQ
"reading-comprehension-in-disguise" failure is a directly reusable
cautionary pattern for anyone building or selecting a bias/safety
benchmark), and an IRT framework to separate genuine cross-lingual model
unsafety from translation-induced difficulty artifacts before using a
multilingual safety score to justify a governance or deployment decision.
The article's own framing — "whoever holds the measuring stick steers the
ship" — is a direct statement of the stakes for benchmark-driven investment
and regulatory decisions.

## Verification notes

Fetched directly from hai.stanford.edu, dated 2026-09-25. The "56
benchmarks" figure, the BBQ example, and the article's direct quotes
("Benchmarks claiming to measure the same thing often disagree with each
other"; "Whoever holds the measuring stick steers the ship") trace directly
to the article's own text. The companion paper's quantified claims (1.9
million responses, 61 model configurations, 10 languages, safety
generalizing as a shared mechanism, 22 models more vulnerable in English)
were independently corroborated against its own arXiv abstract
(arxiv:2605.17173). The 56-benchmark validity paper itself is available
only via an OpenReview submission (forum ID 889XnQKyhM per the HAI article)
with no arXiv preprint or other stable identifier yet at capture time; its
claims here are traced only through the HAI article's summary, not the
paper's own text, and are not independently corroborated beyond that.

## Updates

None yet.

## Related entries

None yet.
