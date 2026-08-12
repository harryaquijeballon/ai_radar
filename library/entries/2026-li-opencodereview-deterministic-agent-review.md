---
slug: 2026-li-opencodereview-deterministic-agent-review
title: "OpenCodeReview: Determinism over Non-Determinism for Cost-Effective Agent-Based Code Review"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.09290
canonical_ids: ["arxiv:2608.09290"]
publisher_or_author: "Zhengfeng Li, Lei Zhang, Xianwei Wu, Zhengqi Zhuang, Yingjie Xu, Boge Wang, Shaofei Zhu, Chuan Wang, Guoping Rong — arXiv preprint (cs.SE)"
published: 2026-08-10
captured: 2026-08-11
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lenses 4/5 (deterministic guardrails around a stochastic
  component; observability/cost): injects determinism at three specific
  pipeline points in an LLM code-review agent (rule-guided dispatch,
  grounded tool use, independent reflection to filter hallucinated
  comments), with large quantified precision and cost gains over
  unconstrained agent baselines, and is open-sourced.
---

# OpenCodeReview: Determinism over Non-Determinism for Cost-Effective Agent-Based Code Review

## Summary
OpenCodeReview addresses unreliability in LLM-based code-review agents by constraining, rather than expanding, agent autonomy at three points: Rule-Guided Dispatch (deterministic file selection), Grounded File Review (a curated, bounded toolset), and Independent Reflection (a second pass that filters hallucinated review comments). Evaluated on AACR-Bench — 200 real-world pull requests across 10 programming languages with 1,505 expert-verified comments — the system achieves up to 2.17x higher SEM-F1 (25.10% vs. 11.57%) against mainstream coding-agent baselines, while consuming 5-15x fewer tokens. The system is open-sourced via a GitHub repository associated with Alibaba.

## Why it matters
A concrete, quantified instance of the "deterministic guardrails around stochastic components" pattern applied to a common workflow (code review): constraining an agent's degrees of freedom, rather than trusting an unconstrained agent loop, produced both a large precision gain and a large cost reduction — directly transferable engineering guidance for anyone building agent-based review or similar bounded-judgment pipelines.

## Verification notes
Read via the arXiv abstract page. The SEM-F1 and token-efficiency figures, benchmark composition (200 PRs, 10 languages, 1,505 comments), and open-source claim are quoted/paraphrased directly from the abstract; not independently corroborated against a second source (the benchmark or repository itself were not separately fetched).

## Updates
None yet.

## Related entries
None yet.
