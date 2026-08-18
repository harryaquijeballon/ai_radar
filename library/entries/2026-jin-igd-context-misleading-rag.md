---
slug: 2026-jin-igd-context-misleading-rag
title: "When Context Misleads: Intent-Guided Decoding for Robust Retrieval-Augmented Generation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.16515
canonical_ids: ["arxiv:2608.16515"]
publisher_or_author: "Haolin Jin, Pengyue Yang, Huaming Chen"
published: 2026-08-17
captured: 2026-08-18
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Directly on lens 8 (reliable RAG): a decoding-time method for deciding how
  much to trust retrieved context versus parametric knowledge, with a
  quantified factual-accuracy gain — a concrete, usable technique for
  document-grounded research/policy products.
---

# When Context Misleads: Intent-Guided Decoding for Robust Retrieval-Augmented Generation

## Summary

The paper addresses a core RAG reliability problem: deciding how much to
trust retrieved context versus the model's own knowledge when the two
conflict. The authors propose Intent-Guided Decoding (IGD), a framework that
balances external evidence against model knowledge based on inferred user
intent, using answer-level filtering and token-level correction to steer
generation. Evaluated across multiple benchmarks, IGD is reported to improve
factual accuracy by up to 65.4 percentage points on factual-conflict datasets
while preserving faithfulness to context when a user explicitly requests it
(unverified — exact benchmark names and full results table not read beyond
the abstract).

## Why it matters

For document-grounded research and policy products, blind trust in retrieved
context (or blind override by parametric memory) is a known failure mode.
IGD is a concrete decoding-time control point — not a retraining or
retrieval-pipeline change — that a builder could evaluate for RAG systems
where context can be stale, wrong, or deliberately adversarial versus cases
where the user wants strict grounding.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The headline claim
(up to 65.4 percentage-point gain on factual-conflict datasets) and the
method description (answer-level filtering + token-level correction guided
by intent) are traced to the abstract text. Benchmark identities, baseline
comparisons, and the intent-inference mechanism's exact definition were not
independently corroborated — hence partial verification.

## Updates

- **2026-08-18** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
