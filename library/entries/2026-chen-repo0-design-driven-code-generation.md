---
slug: 2026-chen-repo0-design-driven-code-generation
title: "Repo0: Design-Driven Zero-to-All Code Generation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.19854
canonical_ids: ["arxiv:2608.19854"]
publisher_or_author: "Silin Chen, Haoyi Teng, Xiaodong Gu, Yuling Shi, Jiale Huang, Yongpan Wang, Hongyu Zhang, Haibing Guan"
published: 2026-08-20
captured: 2026-08-21
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  An architecture-first pattern for whole-repository code generation from
  natural-language specs, with a benchmarked comparison against baselines —
  on-lens for AI-assisted software development (lens 7).
---

# Repo0: Design-Driven Zero-to-All Code Generation

## Summary

Repo0 generates entire software repositories from natural-language specifications
while maintaining an explicit "Dual-Directed-Acyclic-Graph" model of architectural
state. It iteratively refines component boundaries against modularity metrics
until the structure stabilizes, then drives test-driven code generation from that
stabilized structure. Evaluated on six real repositories using GPT-5-mini and
DeepSeek V3.2, the authors report Repo0 outperforming baseline approaches on
functionality coverage and test pass rates (specific baseline deltas not given in
the fetched abstract — unverified beyond the directional claim).

## Why it matters

A concrete architecture-first alternative to purely incremental repo-generation
approaches, of interest to teams evaluating whether explicit structural
stabilization before code generation improves whole-repo output quality.

## Verification notes

Read directly from the arXiv abstract; the method description, evaluation setup
(six repos, GPT-5-mini and DeepSeek V3.2), and directional performance claim are
traced to the source text; exact comparative figures were not present in the
fetched abstract and are marked unverified above. No independent corroboration
was possible — newly posted preprint (submitted 20 Aug 2026). Verification is
`partial`.

## Updates

- **2026-08-21** — Entry created.

## Related entries

None yet.
