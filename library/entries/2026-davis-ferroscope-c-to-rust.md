---
slug: 2026-davis-ferroscope-c-to-rust
title: "Cross-Layer Characterization and AI-Assisted Diagnosis of C-to-Rust Performance"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.33490
canonical_ids: ["arxiv:2611.33490"]
publisher_or_author: "Dalton Davis, Kunal Pai, Tapti Palit — arXiv preprint"
published: 2026-11-24
captured: 2026-11-27
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  An AI-assisted performance-diagnosis tool (FerroScope) that explains and
  helps fix C-to-Rust performance gaps with quantified before/after
  results — a concrete, transferable complement to lens 7 (AI-assisted
  software development), topically adjacent to this library's existing
  coverage of large-scale Rust migration.
---

# Cross-Layer Characterization and AI-Assisted Diagnosis of C-to-Rust Performance

## Summary

Teams migrating code from C to Rust for memory safety often find Rust
implementations slower, with the cause unclear across compiler, runtime,
and hardware layers. The authors conduct a systematic cross-layer study of
12 benchmarks, each with a C implementation and a Rust counterpart, and
build FerroScope, an AI-assisted performance debugger combining source-
level analysis, compiler optimization remarks, dynamic instruction traces,
and hardware performance counters to explain C-vs-Rust performance gaps.
Guided by FerroScope's diagnoses, they write an LLVM compiler pass that
hoists redundant bounds checks via guarded loop versioning while preserving
Rust's panic behavior. In 8 of the 12 benchmarks, at least one Rust
implementation already performs within 10% of its C counterpart or
outperforms it; after the pass, Selection Sort's overhead drops from 2.95x
to 1.00x relative to C, and Merge Sort improves from 1.43x to 0.91x
relative to C. The authors report FerroScope reproduces their own manual
diagnostic findings and sometimes gives more precise explanations, such as
identifying compiler optimizations (loop unrolling, conditional-move
conversion) blocked by redundant bounds checks. Their central claim:
runtime safety checks do not necessarily dominate Rust's performance
overhead, because compiler and microarchitectural optimizations often
mitigate their cost — the actual blocker is often which optimizations the
checks prevent, not the checks' direct runtime cost.

## Why it matters

A concrete diagnostic pattern for any team running or evaluating a large-
scale C-to-Rust (or similar language) migration, including AI-agent-driven
ones: don't assume safety-check overhead explains a performance gap without
layer-by-layer diagnosis, since the real cost is often blocked compiler
optimizations rather than the checks themselves — and an AI-assisted
diagnostic tool can reproduce and sometimes sharpen expert-level manual
analysis of exactly this kind of gap. It also topically complements this
library's existing entry on Anthropic's production Python-to-Rust
migration (verified via shadowing live traffic): that entry covers
correctness verification, while FerroScope addresses the complementary
question of diagnosing *why* a migrated Rust implementation underperforms
once correctness is established.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.33490, v1 submitted
2026-11-24, cs.PF with cross-lists to cs.PL/cs.SE). The methodology
(FerroScope's four diagnostic signals, the bounds-check-hoisting pass) and
the quantified figures above (8/12 benchmarks within 10% of C, Selection
Sort 2.95x→1.00x, Merge Sort 1.43x→0.91x) are traced to the abstract's own
description as summarized by the fetch tool. No independent corroboration
was attempted; verification is partial pending a full-text read.

## Updates

None yet.

## Related entries

[2026-anthropic-messages-api-rust-migration](2026-anthropic-messages-api-rust-migration.md) — same-week library entry on a production-scale C/Python-to-Rust migration; this entry addresses post-migration performance diagnosis rather than correctness verification.
