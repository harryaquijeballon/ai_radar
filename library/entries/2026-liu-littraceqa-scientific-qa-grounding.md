---
slug: 2026-liu-littraceqa-scientific-qa-grounding
title: "LitTraceQA: A Benchmark for Multi-Stage Grounding and Verification in Scientific Question Answering"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.07370
canonical_ids: ["arxiv:2608.07370"]
publisher_or_author: "Xuye Liu, Yimu Wang, Peng Shi, Bo Xue, Xiangrui Ke, Songcheng Cai, Kath Choi, Di Wu, Freda Shi, Krzysztof Czarnecki — arXiv preprint"
published: 2026-08-07
captured: 2026-08-10
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 8 (reliable research products — citation verification,
  document grounding): a benchmark that requires systems to separately
  produce the source paper, the located evidence, and the answer, so
  scientific-QA systems can be scored on whether answers are actually
  traceable rather than merely plausible. Medium rather than high because
  it is a benchmark contribution (evaluation infrastructure), not yet a
  validated method or deployed pattern a builder applies directly.
---

# LitTraceQA: A Benchmark for Multi-Stage Grounding and Verification in Scientific Question Answering

## Summary

Targets a gap in how AI systems process scientific literature: a reliable
system must identify the relevant papers, locate the concrete evidence
supporting an answer, and produce a response faithful to that evidence.
LitTraceQA requires systems to deliver three linked outputs — paper
identifiers, supporting-evidence locations, and answers in multiple formats
(text, multiple-choice, structured tables) — evaluated separately for
retrieval accuracy, evidence grounding, and answer precision. The
development set has 55 examples (single- and multi-paper questions); the
broader collection covers 4,978 unique-question records over 4,859 unique
gold papers. Targeted evidence types include tables, figures, text
passages, equations/algorithms, and citation contexts.

## Why it matters

Directly on point for anyone building AI research or policy tooling that
must cite its sources defensibly: scoring retrieval, grounding, and answer
correctness as three separate axes exposes systems that get the right
answer while citing the wrong paper or evidence — the same class of
grounding failure that undermines trust in AI-assisted literature review.
A reusable evaluation structure and evidence-type taxonomy for anyone
building or testing a scientific document-QA pipeline.

## Verification notes

arXiv abstract page fetched directly (2026-08-10); authors, submission date
(7 Aug 2026, v1), and category confirmed. All claims in the Summary — the
three-output requirement (paper ID, evidence location, answer), the
separate scoring of retrieval/grounding/answer precision, the 55-example
development set, the 4,978-question/4,859-paper collection size, and the
evidence-type taxonomy — trace directly to the fetched abstract text. No
independent corroboration attempted (preprint, not yet peer reviewed).
Full paper PDF not read at capture.

## Updates

None yet.

## Related entries

None yet.
