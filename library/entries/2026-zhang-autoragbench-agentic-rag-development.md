---
slug: 2026-zhang-autoragbench-agentic-rag-development
title: "AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.25582
canonical_ids: ["arxiv:2611.25582"]
publisher_or_author: "Hang Zhang, Yuzhi Pan, Ziyao Zhong, Chaokun Wang, Shuo Cao, Zeyu Huang, Yue Xue, Fang Niu, Bofan Xie, Guanchen Ge, Zecheng Li, Leqi Zheng, Ziyang Liu, Wei Wang, Miao Gu — arXiv preprint"
published: 2026-11-19
captured: 2026-11-21
relevance:
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 8 (reliable research and policy products) and lens 1
  (agent architecture): a measured benchmark showing LLM agents can
  autonomously build and iteratively improve RAG systems beyond a
  human-designed baseline, directly relevant to this profile's
  policy-simulation-grade RAG interest.
---

# AutoRAGBench: A Benchmark for LLM Agents Automating RAG System Development

## Summary

Asks whether LLM agents can autonomously build and iteratively improve
retrieval-augmented generation systems, given that effective RAG design
takes substantial engineering and trial-and-error and the best choices
vary by task and domain. AutoRAGBench evaluates this in an open code
space across nine RAG development tasks: agents receive no starter code
or prescribed strategy and work within a six-hour budget on a single H800
GPU, analyzing data, implementing pipelines, and refining designs from
experimental feedback. Across nine evaluated agent configurations, the
best (GPT-6.1 Sol with Codex CLI) averaged a score of 56.1 versus 44.4 for
a composite human-designed state-of-the-art baseline. Starting from that
human-designed system on seven tasks, the same agent improved scores by
16.6 points on average. The authors conclude that LLM agents can automate
effective RAG system development.

## Why it matters

For anyone building RAG-based research or policy products: a measured
upper bound on what autonomous agentic RAG-engineering can currently
achieve relative to a strong human-designed baseline, and a benchmark
other teams can use to check whether a given agent/harness combination is
actually improving RAG pipelines rather than just plausibly editing them.

## Verification notes

arXiv abstract page fetched 2026-11-21 (paraphrased summary; full abstract
text not reproduced verbatim due to tool quoting limits). Submission
history shows v1 submitted Thu, 19 Nov 2026, 06:26:28 UTC — within this
run's discovery window (2026-11-20 → 2026-11-21) and the 7-day eligibility
cap. Figures (nine tasks, six-hour/single-H800 budget, 56.1 vs 44.4
average score, +16.6-point improvement on seven tasks) were confirmed on a
second, independent fetch requesting exact quoted figures, which matched
the first pass exactly. Full per-task results and the "composite
human-designed SOTA" baseline's construction were not independently
inspected at capture. No secondary coverage found (new preprint).

## Updates

None yet.

## Related entries

None yet.
