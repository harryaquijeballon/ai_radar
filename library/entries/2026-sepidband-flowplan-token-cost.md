---
slug: 2026-sepidband-flowplan-token-cost
title: "FlowPlan: Reducing the Token Cost of Coding Agents with Abstraction-Guided Planning and Verification"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.13241
canonical_ids: ["arxiv:2611.13241"]
publisher_or_author: "Melika Sepidband, Jiho Shin, Song Wang, Hadi Hemmati — arXiv preprint (cs.SE)"
published: 2026-11-09
captured: 2026-11-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on agent architecture/orchestration and evaluation (lenses 1, 4): a
  concrete, quantified technique — planning and verifying code repairs
  against per-function control-flow/data-flow graphs instead of repeated
  raw-code reads — that cuts coding-agent token cost substantially while
  holding resolution rate roughly unchanged, tested across multiple models
  and benchmarks.
---

# FlowPlan: Reducing the Token Cost of Coding Agents with Abstraction-Guided Planning and Verification

## Summary

Addresses the high cost of iterative interaction loops in LLM-based coding
agents (e.g., Claude Code). FlowPlan has the agent reason about a code
repair at the level of per-function control-flow/data-flow graphs rather
than repeatedly re-reading raw source: it localizes the likely fault on
this abstraction, states the intended repair as graph changes, edits the
source, rebuilds the abstraction, and checks the observed change against
the plan before a final verification step. Across Claude Haiku 4.5 and
Sonnet 5 on SWE-bench Pro, SWE-bench Verified, and SecBench, the authors
report token-use reductions of roughly 6–68% relative to a vanilla agent
baseline (largest for Haiku 4.5, smaller for Sonnet 5), "significant in
five of six" model/benchmark settings, while resolution rate stayed
roughly unchanged. The authors attribute the savings mainly to replacing
costly post-edit re-reading and re-testing with explicit verification
against a smaller per-call context.

## Why it matters

A transferable cost-reduction pattern for anyone operating coding agents
at scale: swapping repeated raw-source re-reads for a persistent,
rebuildable program-graph abstraction that the agent plans and verifies
against cuts token spend meaningfully without the usual accuracy
trade-off. Directly actionable for teams tracking agent token cost (see
also this library's [2026-agarwal-token-spend-engineering-output](2026-agarwal-token-spend-engineering-output.md)
on why token spend alone is a weak output metric) who want a concrete
lever to reduce that spend rather than merely measure it.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.13241,
2026-11-12); title, authors (Melika Sepidband, Jiho Shin, Song Wang, Hadi
Hemmati), submission date (9 Nov 2026), and category (cs.SE) confirmed
there. The method description and the per-model/per-benchmark token-cost
figures trace to the fetched abstract text; the percentage conversions
from the reported multipliers were computed independently from the raw
figures, not copied from the source. Full paper (trajectory analysis
detail, statistical tests) not read at capture — upgrade path noted.

## Updates

None yet.

## Related entries

- [2026-agarwal-token-spend-engineering-output](2026-agarwal-token-spend-engineering-output.md) — related but distinct: that entry argues token spend is a weak proxy for engineering output; this entry is a technique for reducing an agent's own token cost without changing outcomes.
