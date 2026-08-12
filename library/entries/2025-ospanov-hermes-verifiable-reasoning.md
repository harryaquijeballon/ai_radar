---
slug: 2025-ospanov-hermes-verifiable-reasoning
title: "HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2511.18760
canonical_ids: ["arxiv:2511.18760", "doi:10.48550/arXiv.2511.18760"]
publisher_or_author: "Azim Ospanov, Zijin Feng, Jiacheng Sun, Haoli Bai, Xin Shen, Farzan Farnia — arXiv preprint (cs.AI, cs.FL)"
published: 2025-11-24
captured: 2026-07-22
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On the evaluation/validation lens from an interesting angle: interleaving
  informal LLM reasoning with formally verified Lean proof steps — a working
  example of deterministic verification wrapped around stochastic reasoning.
  Medium: domain-specific (formal mathematics) and early, so the pattern
  matters more than the tool for research-product builders. Note: the user's
  save-note said "agents that learn with you"; the actual paper is about
  verifiable reasoning — the memory module for proof continuity is the
  closest match to that description.
---

# HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs

## Summary

Tool-assisted agent (Nov 2025, v2 May 2026) that interleaves informal reasoning with formally verified proof steps in Lean: intermediate formal checks catch reasoning errors mid-chain, and a memory module maintains proof continuity across multi-step derivations. Self-reported results: on hard benchmarks (AIME, HARDMath2), Hermes@1 achieves up to 40% accuracy improvement while using ~80% fewer total inference FLOPs than baselines, with consistent gains across model scales and further gains under test-time scaling (all as reported by the authors — no independent replication at capture). Code publicly released.

## Why it matters

*(Radar's assessment.)* A concrete instance of the architecture principle most relevant to defensible research products: let a deterministic verifier (here, a proof assistant) gate a stochastic reasoner, instead of trusting chain-of-thought. The math domain is niche, but the check-as-you-go pattern — including the claimed efficiency gains from failing fast — transfers to any pipeline where intermediate outputs can be validated mechanically.

## Verification notes

arXiv abstract page fetched: title, authors, categories (cs.AI, cs.FL), v1 date 24 Nov 2025 and v2 29 May 2026 confirmed; Summary claims trace to the abstract. Benchmarks are the authors' self-reported numbers, marked accordingly. Full text and code not reviewed at capture; upgrade path: read the method section and check the repo if the pattern is ever adopted.

## Updates

*(none yet)*

## Related entries

[2025-dawid-agentic-workflows-economic-research](2025-dawid-agentic-workflows-economic-research.md) — verification agents in a research workflow; HERMES is the harder-guarantee version of that idea.
