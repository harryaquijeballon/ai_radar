---
slug: 2026-judge-inherits-prompt-directional-label-bias
title: "Your Judge Inherits Your Prompt: In-Context Label Bias in an LLM-as-Judge Is Directional, Not Symmetric"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.26881
canonical_ids: ["arxiv:2611.26881"]
publisher_or_author: "arXiv preprint (cs.CL)"
published: 2026-11-23
captured: 2026-11-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  A frozen generator-judge experiment showing that skewing an LLM-as-judge's
  few-shot examples toward acceptance inflates its acceptance rate by
  20-30 points versus human consensus, while the opposite skew produces no
  matching drop — lens 4 (evaluation, validation and deterministic
  guardrails): a concrete, actionable warning and fix (balance examples,
  average over draws) for anyone relying on LLM judges.
---

# Your Judge Inherits Your Prompt: In-Context Label Bias in an LLM-as-Judge Is Directional, Not Symmetric

## Summary

This paper (arXiv:2611.26881, cs.CL) studies in-context label bias in
LLM-as-judge pipelines. Using a frozen generator-judge pipeline for video
question answering, the authors keep the generated answers fixed and vary
only the Yes/No balance of the judge's few-shot demonstration examples
across four demonstration sets, checking each verdict against two-annotator
human consensus on 200 examples per dataset (with a separate analysis across
five draws of example sets, after results from a single draw proved
unstable). The judge's acceptance rate stays close to human consensus when
its examples are balanced or skew toward rejection. When the examples skew
toward acceptance, acceptance jumps sharply — by about 30 points on
NExT-QA and 20 points on MSVD-QA — while the opposite skew produces no
matching drop, so the bias runs in one direction only. The authors describe
this as an "inflation-only failure mode" that can make benchmark gains look
larger than they are without making losses look worse, and note that
single-draw results varied by up to 18 points — more than the differences
between prompting conditions they were testing. They recommend balancing
the judge's few-shot examples and averaging results over several draws.

## Why it matters

A specific, actionable warning for anyone using LLM-as-judge pipelines for
evaluation: an innocuous-seeming imbalance in few-shot examples can silently
inflate scores in one direction only, and single-draw judge results can be
noisier than the effect being measured — with a direct, low-cost fix
(balance examples, average over multiple draws).

## Verification notes

Read directly from the arXiv abstract page (arxiv.org/abs/2611.26881),
listed Mon 2026-11-23 on the cs.CL recent-submissions page. The summarized
claims (the directional 20-30 point inflation, the 18-point single-draw
variance, the recommended fix) are taken directly from the arXiv-published
abstract text. Marked `partial` because the full author list was not shown
on the fetched abstract page and was not independently looked up.

## Updates

None yet.

## Related entries

None yet.
