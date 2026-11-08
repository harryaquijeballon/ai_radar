---
slug: 2026-wang-req2rust-cpp-migration-harness
title: "Req2Rust: A Requirements-Guided Agent Harness for Project-Level C++-to-Rust Migration"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07442
canonical_ids: ["arxiv:2611.07442"]
publisher_or_author: "Shengbo Wang, Mingwei Liu, Yuwen Chen, Yanlin Wang"
published: 2026-11-05
captured: 2026-11-08
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 7 (AI-assisted software development): a requirements-guided,
  spec-driven agent harness for a specific, hard migration task, measured
  against a strong baseline (Claude Code) with large, quantified test-pass
  gains on both general and real-world (OpenHarmony) codebases.
---

# Req2Rust: A Requirements-Guided Agent Harness for Project-Level C++-to-Rust Migration

## Summary

Presents Req2Rust, described as the first project-level LLM-based
C++-to-Rust migration harness. It first derives a Migration Requirements
Specification from evidence in the source project, capturing behaviors and
constraints that must be preserved, then produces a Rust Design
Specification and an initial Rust project. That project is treated as an
executable state to refine using compiler, semantic, and
unsafe-reduction validators. Compared with a Claude Code baseline on both
general C++ projects and real OpenHarmony modules, Req2Rust produces
buildable Rust crates in both settings; test pass rates rise from 69.5% to
91.9% on general projects and from 45.4% to 87.9% on OpenHarmony modules.

## Why it matters

A concrete pattern — derive a structured requirements/design spec before
generation, then refine against compiler/semantic/safety validators in a
loop — for a notoriously hard class of AI-assisted migration task, with a
head-to-head quantified comparison against an off-the-shelf coding-agent
baseline rather than an unaudited absolute number (lens 7).

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 5 Nov 2026, no revisions). The harness description and the
baseline-comparison test-pass-rate figures (69.5%→91.9%; 45.4%→87.9%) trace
to the fetched abstract text — treated as `verified` per this library's
standing convention for single-source arXiv preprints whose headline claims
are self-reported. The full paper (validator implementation, OpenHarmony
module selection) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
