---
slug: 2026-collinear-cwe-bench-v2-security-benchmark
title: "CWE-bench v2: More Coverage, Quality, and Transparency"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://huggingface.co/blog/cwe-bench
canonical_ids: ["repo:collinear-ai/cwe-bench"]
publisher_or_author: "Collinear AI — Hugging Face blog"
published: 2026-11-03
captured: 2026-11-07
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation and deterministic guardrails (lens 4) and
  reproducibility/governance (lens 6): a public, deterministically and
  reproducibly scored benchmark testing whether coding agents can find and
  fix real security weaknesses without breaking existing functionality,
  with quantified multi-model results and an explicit held-out set to guard
  against memorization.
---

# CWE-bench v2: More Coverage, Quality, and Transparency

## Summary

CWE-bench v2 is a public benchmark from Collinear AI testing whether AI
coding agents can find and fix a security weakness in a real open-source
repository checkout without breaking existing behavior, aiming at broad
understanding of attack surfaces rather than recognition of memorized
patterns. It covers 100 public tasks across 91 distinct CWE (Common Weakness
Enumeration) types and eight programming languages. Scoring is fully
programmatic and deterministic, so results are reproducible at no extra
evaluation cost; LLM-judge panels were used only to help shape task
difficulty/fairness criteria during construction, not to score runs. Each
task was checked against criteria including realistic instructions,
behavior-testing (not single-fix-structure-testing) verifiers, and failure on
memorized upstream patches, and was also reviewed by hand. A held-out set
tracks progress on tasks no model has seen, with access gated by request.

Across 11 evaluated models, Gemini 4 Argon scored highest (67.8% pass@1, 81.0%
pass@4), followed by Claude Opus 5.5 (67.3% pass@1, 78.0% pass@4). 95 of the
100 tasks were solved by at least one model, but the leading model still
fails 19% of tasks on every attempt. On cost, DeepSeek V4.1 Flash reached
57.0% pass@1 at roughly $0.04 per rollout, versus roughly $1.83 for Opus
(about ten points higher) and $3.92 for Gemini. Tasks are packaged as
Dockerized environments for the Harbor framework, runnable directly from the
gated Hugging Face dataset, and are tagged for use as reinforcement-learning
environments.

## Why it matters

A concrete, reproducible yardstick for a question most agent-security claims
leave unquantified: how often can a coding agent actually find and correctly
fix a real security weakness, as opposed to pattern-matching a known CVE
patch. The deterministic, behavior-based scoring (not LLM-judge scoring) and
the held-out anti-memorization set make this usable as an independent check
on vendor security-capability claims, and the per-model cost-vs-accuracy
figures give builders a concrete basis for choosing a model for automated
security patching work.

## Verification notes

Fetched and read directly (huggingface.co, on the egress allowlist). All
claims, including the reported model scores and costs, are traced directly
to the blog post; no load-bearing claim here depends on information beyond
it. The underlying dataset is gated (access by request), so the task set and
scoring harness were not independently fetched or re-run. Collinear AI is the
benchmark's publisher and has a commercial interest in security-evaluation
tooling, though the benchmark itself (not a Collinear product) is what is
scored here.

## Updates

None yet.

## Related entries

None yet.
