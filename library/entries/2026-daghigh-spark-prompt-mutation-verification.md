---
slug: 2026-daghigh-spark-prompt-mutation-verification
title: "SPARK: Semantic-preserving Prompt Mutation for Code Generation using Consensus-based Verification Framework"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.13401
canonical_ids: ["arxiv:2611.13401"]
publisher_or_author: "Alireza Daghigh, Chung-Yu Wang, Luca Filippelli, Hamed Taherkhani, Hadi Hemmati, Hung Viet Pham — arXiv preprint (cs.SE), accepted CASCON 2026"
published: 2026-11-10
captured: 2026-11-12
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on evaluation/validation and deterministic guardrails (lens 4):
  a usable test-free consensus-verification technique for ranking
  LLM-generated code without ground-truth tests, with a quantified (if
  modest) improvement over the prior state of the art across three
  benchmarks and three models — a real, if incremental, method for
  validating generated code when test cases aren't available.
---

# SPARK: Semantic-preserving Prompt Mutation for Code Generation using Consensus-based Verification Framework

## Summary

Addresses the problem that LLM-generated code often cannot be verified
automatically because real-world use rarely comes with test cases. SPARK
extends consensus-based verification by applying semantic-preserving
changes to the problem description itself (paraphrasing, grammatical
edits, function renaming), generating candidate solutions and tests for
each mutated description, and ranking solutions by how consistently they
pass across those mutated-description-generated tests. Evaluated on three
benchmarks (LiveCodeBench, BigCodeBench, DLBench) and three LLMs (o4-mini,
DeepSeek-R1-Basic, Gemini-2.5-Pro), the authors report it "outperforms
state-of-the-art consensus-based verification approaches by up to 4.1%."
The abstract also describes a generalization experiment but gives no
figures for it.

## Why it matters

A concrete, test-free way to gain confidence in which of several
LLM-generated code candidates is actually correct, applicable anywhere
test cases aren't available — directly useful for pipelines (including
research/policy data-analysis agents) that need some automated signal of
code correctness without hand-written tests. The improvement is modest
(up to 4.1%), so this is an incremental refinement of an existing
technique family rather than a breakthrough, but it is a real, measured
gain with a clearly described mechanism a builder could adopt.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.13401,
2026-11-12); title, authors, submission date (10 Nov 2026), category
(cs.SE), and CASCON 2026 acceptance confirmed there. The method
description and the headline "up to 4.1%" improvement figure trace
directly to the fetched abstract text. The abstract's mentioned
generalization experiment reports no figures, so no claim is made about
it above. Full paper not read at capture — upgrade path noted.

## Updates

None yet.

## Related entries

None yet.
