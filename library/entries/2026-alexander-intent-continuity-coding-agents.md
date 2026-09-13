---
slug: 2026-alexander-intent-continuity-coding-agents
title: "Coding Agents Don't Need Longer History — They Need Intent Continuity"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/coding-agents-dont-need-longer-history-they-need-intent-continuity/
canonical_ids: []
publisher_or_author: "Emmimal P Alexander — Towards Data Science"
published: 2026-09-11
captured: 2026-09-13
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  A named, concrete mechanism (a deterministic, non-LLM extractor/verifier
  pipeline distinct from RAG) with a small quantified evaluation and an
  explicit self-correction of a rigged benchmark — on-lens for lens 2
  (context/harness engineering); a single-author, small-scale synthetic
  benchmark keeps it at medium rather than high.
---

# Coding Agents Don't Need Longer History — They Need Intent Continuity

## Summary

The author proposes a five-stage, deterministic (no embeddings, no vector
database, no LLM calls) pipeline for recovering and validating
project-history requirements for coding agents on long-running projects: an
Extractor (trigger-phrase detection for requirement-like sentences),
Candidate Retrieval (shared-component/dependency matching), Verification
(is the historical rule still valid or superseded?), a Compiler (flattens
verified records into clean context), and a Checker (grades implementation
against ground truth). The author distinguishes this from RAG: "retrieval
asks what's relevant; verification asks if it's still valid; intent
continuity asks what should influence this task, right now." In a test of
eight coding tasks against 70 synthetic interactions with 12 planted
requirements: no-history baseline passed 0/8 tasks; keyword search passed
4/8 (57% requirement recall); the intent-aware pipeline passed 8/8 (100%
recall). The author reports discovering and fixing a rigged benchmark where
per-task hints had been hand-coded into the test harness.

## Why it matters

Gives builders a concrete, cheap (deterministic, LLM-free) alternative
mechanism to try before reaching for embeddings/RAG when a coding agent
needs to keep obeying rules established many turns ago — plus a
methodological reminder (the self-caught rigged benchmark) about auditing
one's own eval harness before trusting its numbers (lens 2/4).

## Verification notes

Read the Towards Data Science post directly (allowlisted, primary source for
this commentary). Figures (0/8, 4/8 at 57% recall, 8/8 at 100% recall, 70
synthetic interactions, 12 planted requirements) are as reported by the
author; this is a small, single-author, self-constructed synthetic
benchmark, not independently reproduced or peer-reviewed.

## Updates

None yet.

## Related entries

None yet.
