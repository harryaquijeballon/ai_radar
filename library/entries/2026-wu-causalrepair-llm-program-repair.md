---
slug: 2026-wu-causalrepair-llm-program-repair
title: "CausalRepair: Bridging the Causality Gap in Large Language Model-Based Automated Program Repair via Dual-Slicing"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.10613
canonical_ids: ["arxiv:2608.10613"]
publisher_or_author: "Linhao Wu, Yizhou Chen, Zhen Yang, Pengyu Xue, Dan Hao — arXiv preprint (cs.SE)"
published: 2026-08-11
captured: 2026-08-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 7 (AI-assisted software development) and lens 4
  (evaluation): a quantified, reproducible improvement to LLM-based
  automated program repair (313 Defects4J bugs fixed, outperforming named
  baselines, at $0.029/bug) via a concrete technique — dual static/dynamic
  slicing for causally relevant repair context — a builder could apply.
---

# CausalRepair: Bridging the Causality Gap in Large Language Model-Based Automated Program Repair via Dual-Slicing

## Summary
CausalRepair targets a specific failure mode in LLM-based automated program repair: incomplete or noisy test context and irrelevant surrounding source code that obscure the causal link between a bug and its fix. It combines context-aware static slicing with execution-trace-based dynamic slicing to generate compact, causally relevant context for iterative repair guidance. Evaluated on multiple Defects4J benchmarks using DeepSeek-V3, it fixes 313 bugs, outperforming comparable approaches (ReinFix, TSAPR), while reducing average repair cost to $0.029 per bug.

## Why it matters
A concrete technique for improving LLM program-repair pipelines' precision and cost by feeding the model causally-relevant code slices rather than raw surrounding context — directly applicable to any team building or evaluating AI code-repair tooling, with a reproducible benchmark comparison and a stated per-bug cost figure to budget against.

## Verification notes
Read via the arXiv abstract page. The bug-fix count, baseline comparisons, and per-bug cost figure are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
