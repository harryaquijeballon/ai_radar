---
slug: 2026-naveed-raglog-rag-fault-localization
title: "From Logs to Faults: Reference-Free Fault Localization for Retrieval-Augmented Generation Pipelines"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.03725
canonical_ids: ["arxiv:2611.03725"]
publisher_or_author: "Hira Naveed, Scott Barnett, Stefanus Kurniawan, John Grundy, Chetan Arora, Hourieh Khalajzadeh, Omar Haggag"
published: 2026-11-01
captured: 2026-11-04
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on evaluation/validation/deterministic guardrails and the reliable
  research/policy products lens (lenses 4, 8): a released, open-source
  reference-free fault localizer for RAG pipelines that outperforms
  agent-baseline debugging at a fraction of the cost and latency, with a
  released fault-injection dataset for benchmarking.
verification: verified
---

# From Logs to Faults: Reference-Free Fault Localization for Retrieval-Augmented Generation Pipelines

## Summary

Addresses the manual, slow process of locating faults in Retrieval-Augmented
Generation (RAG) pipelines, where faults can propagate silently across
interdependent stages or go unnoticed even when the final answer looks
correct, and where existing evaluation methods often examine single stages
and depend on reference answers or code instrumentation. RAGLog detects and
localizes faults using only execution logs — no reference answers or code
instrumentation — by converting heterogeneous API logs into a common RAG
schema and combining rule-based, embedding-based, and LLM-based checks to
identify the faulty stage. The authors also release a live fault injector and
RAGLog Faults, a dataset of 3,134 runs across five RAG pipelines with
stage-level fault labels. With Claude Haiku 5.5 as the checking model, RAGLog
reaches a pooled F1 of 0.73 on naturally-occurring faults, versus 0.58 for
Claude Code and 0.52 for Codex used as debugging agents; on injected faults
all three are comparable (0.84 vs. 0.80 vs. 0.82). RAGLog analyzes each run
in about five seconds at roughly $0.005, cheaper and faster than the agent
baselines, and is released as open-source software.

## Why it matters

A directly usable, open-source tool and benchmark for debugging RAG
pipelines in production without needing reference answers or source-code
instrumentation — relevant to this library's many existing RAG-reliability
entries and to any research or policy product built on retrieval-grounded
generation that needs a cheap, fast way to tell which pipeline stage broke.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-01). The log-only, reference-free method, the RAGLog Faults dataset
size, and all quantified F1/cost/latency figures trace to the abstract text.
Full paper (schema design, the five pipelines tested) not read at capture.

## Updates

None yet.

## Related entries

None yet.
