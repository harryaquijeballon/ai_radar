---
slug: 2026-liu-parsebench-2-severity-policy-eval
title: "Building Toward a Perfect Document Parsing Benchmark"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://www.llamaindex.ai/blog/building-toward-a-perfect-document-parsing-benchmark
canonical_ids: []
publisher_or_author: "Jerry Liu — LlamaIndex blog"
published: 2026-11-19
captured: 2026-11-20
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation/validation) and lens 8 (document-grounding
  done rigorously): demonstrates, with a concrete counterexample, that
  standard document-parsing similarity metrics and LLM-judge scoring
  misrank errors by severity and are unstable across reruns — then supplies
  a generalizable severity-policy fix any team building a document-RAG
  pipeline could apply, discounted for vendor/product promotion per
  profiles/ai_engineering/sources.md.
---

# Building Toward a Perfect Document Parsing Benchmark

## Summary

Argues that common document-parsing metrics do not track how severe a
parsing error actually is. In the post's worked example, a truncated
dollar figure ($6,264 parsed as $6,26) scored 99.2 under the prior
benchmark (ParseBench-1) — because edit-distance-style metrics barely react
to that change — while a fully correct extraction using a different but
equivalent table markup scored only 43.6, because such metrics
over-penalize formatting differences that don't change meaning. LLM judges
have a related, separate problem: in a test of 412 SERFF insurance pages
(77 selected after judging), 11 pages reversed which output "won" when the
same comparison was rerun on identical inputs — judge instability that
hides real error-type tradeoffs. The author's fix, ParseBench-2, makes the
expected penalty for each error type an explicit target: a severity policy
sorts errors into critical/major/minor/benign categories across text,
formatting, tables, charts, and forms, with a severity cap so a serious
error (e.g., a first critical error caps an otherwise-perfect page at 90)
isn't diluted by otherwise-correct content, and deterministic metrics are
tuned against those targets using 330 controlled-perturbation types across
six test suites (4,317 page-level cases total). The scorer stays
deterministic for fixed inputs and versions.

## Why it matters

For anyone building or evaluating a document-grounded RAG or extraction
pipeline: direct, reproducible evidence that both a standard similarity
metric and an LLM-as-judge can disagree with human severity judgment — and
can disagree with themselves on a rerun — which argues against trusting
either uncritically for pipeline evaluation. The severity-policy pattern
(classify errors by consequence, cap scores on the worst error class
instead of averaging it away, validate with controlled perturbations, keep
scoring deterministic and versioned) is a directly transferable recipe for
building a defensible evaluation harness for any document-extraction
system, independent of LlamaIndex's own tooling.

## Verification notes

Blog post fetched directly (2026-11-20); author (Jerry Liu), publication
date (19 November 2026), and the core examples traced to the fetched text:
the $6,264/$6,26 ParseBench-1 scoring mismatch (99.2 vs. 43.6), the
11-of-77-pages LLM-judge reversal-on-rerun result, the severity-cap design
(a first critical error caps a page at 90), and the 330-perturbation-type/
4,317-case ParseBench-2 scale. Discounted per the ai_engineering sources
policy for framework/product promotion (LlamaParse and the "Metric Lab"
tool are promoted throughout); the entry treats the severity-policy
technique as the load-bearing, vendor-independent claim. Full post
(complete perturbation-suite breakdown, annotation-quality caveats) not
read in full detail at capture. No independent secondary corroboration
attempted (vendor blog post, no secondary coverage found this run).

## Updates

None yet.

## Related entries

None yet.
