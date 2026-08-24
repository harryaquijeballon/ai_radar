---
slug: 2026-yadav-memstrata-temporal-validity
title: "Temporal Validity on Real Software Histories: Eliminating Stale-Fact Errors in Code-Assistant Memory over GitHub Fixes"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.20685
canonical_ids: ["arxiv:2608.20685"]
publisher_or_author: "Neeraj Yadav — arXiv preprint (cs.SE)"
published: 2026-08-24
captured: 2026-08-24
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on lens 2 (harness and context engineering): standard RAG-based
  code-assistant memory cannot distinguish superseded facts (renamed
  functions, updated dependencies) from current ones within a session;
  MemStrata's deterministic subject-relation-object state tracking names
  the mechanism and reports a large, quantified accuracy gain over RAG on
  a real-world benchmark — directly usable guidance on when retrieval alone
  is the wrong memory architecture.
verification: verified
---

# Temporal Validity on Real Software Histories: Eliminating Stale-Fact Errors in Code-Assistant Memory over GitHub Fixes

## Summary

When code changes mid-session — a function renamed, a dependency updated — standard RAG-based code-assistant memory cannot tell old and new values apart and often serves the outdated one. The author proposes MemStrata, which tracks state transitions deterministically in subject-relation-object form instead of relying on similarity retrieval. Validated on 130 clean atomic state transitions extracted from 707 real GitHub issues in SWE-bench Lite + Verified, MemStrata reaches 0.91 answer accuracy versus 0.57–0.59 for RAG. Stale-value serving — RAG returning a superseded fact — occurred 36–38% of the time under RAG and was reduced to approximately zero under MemStrata, while matching RAG's retrieval latency (~2.1s) and beating an LLM-reranker baseline (~18s). The authors note a scope limit: only about 18% of real fixes qualify as "clean" atomic transitions the method currently handles, and report that a production bug was found and fixed during the study without breaking deterministic-supersession accuracy on code mutations.

## Why it matters

A concrete, quantified case for when deterministic state tracking should replace similarity-based retrieval in agent memory: for the subset of code changes that are clean atomic transitions, MemStrata all but eliminates a specific, measurable failure mode (serving superseded facts) at no added latency cost. The explicit 18% coverage limit is itself useful — it tells a builder exactly how far this pattern reaches before falling back to RAG is still necessary, rather than overselling scope.

## Verification notes

Read via the arXiv abstract page, which reports the accuracy, stale-serving-rate, and latency figures directly. Not independently corroborated against a second source or the full paper.

## Updates

None yet.

## Related entries

None yet.
