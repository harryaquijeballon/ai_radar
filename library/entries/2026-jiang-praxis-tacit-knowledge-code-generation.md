---
slug: 2026-jiang-praxis-tacit-knowledge-code-generation
title: "PRAXIS: Graph-Grounded Tacit Knowledge for Domain Code Generation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.19784
canonical_ids: ["arxiv:2608.19784"]
publisher_or_author: "Xue Jiang, Tianyu Zhang, Lingwei Wu, Ziyu Wang, Ge Li, Yuan Sui, Hao Zhu, Wenpin Jiao, Zhi Jin, Yihong Dong"
published: 2026-08-20
captured: 2026-08-21
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  A context-engineering pattern for extracting undocumented domain "tacit
  knowledge" from a codebase and injecting it into coding agents at task
  time — on-lens for harness/context engineering (lens 2) and AI-assisted
  software development (lens 7).
---

# PRAXIS: Graph-Grounded Tacit Knowledge for Domain Code Generation

## Summary

PRAXIS extracts undocumented "tacit knowledge" — domain business rules, interface
contracts, and operational conventions not captured in formal documentation — by
simulating developer workflows over a codebase, then organizes the extracted
knowledge via a code dependency graph and injects it into coding agents at task
time. The authors report that PRAXIS outperforms baseline approaches, integrates
across multiple agent architectures and LLMs, and improves continuously as more
experience accumulates (specific comparative figures not given in the fetched
abstract — unverified beyond the directional claim).

## Why it matters

A concrete pattern for closing the gap between what a codebase's documentation
says and the unwritten conventions developers actually follow — relevant to teams
building coding agents for large, mature codebases where undocumented domain rules
are a common source of agent error.

## Verification notes

Read directly from the arXiv abstract; the method description and directional
performance/portability claims are traced to the source text; exact comparative
figures were not present in the fetched abstract and are marked unverified above.
No independent corroboration was possible — newly posted preprint (submitted 20
Aug 2026). Verification is `partial`.

## Updates

- **2026-08-21** — Entry created.

## Related entries

None yet.
