---
slug: 2026-xu-tool-architecture-coding-agents
title: "The Devil Is in the Interface: Evaluating How Tool Architecture Shapes Coding Agent Behavior"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.11386
canonical_ids: ["arxiv:2608.11386"]
publisher_or_author: "Xiangzhe Xu, Hamidreza Saghir, Qianhui Wu, Marc-Alexandre Côté, Tong Wang, Kiran Lakkaraju, Kexin Pei, Xiangyu Zhang — arXiv preprint (cs.SE)"
published: 2026-08-11
captured: 2026-08-13
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 3 (tool use and MCP): a large, controlled comparison (six
  tool architectures, 11,700 trajectories) on repository-level issue fixing
  that quantifies how interface design choices change agent behavior —
  directly actionable numbers for anyone designing a coding agent's tool
  surface.
---

# The Devil Is in the Interface: Evaluating How Tool Architecture Shapes Coding Agent Behavior

## Summary
Controlled experiments on repository-level issue fixing compare six tool architectures for coding agents across 11,700 trajectories. Structured low-level interfaces improved consistency by up to 4.7x. Natural-language search increased relevant file access by over 11%. Python CodeAct-style interfaces achieved comparable task performance with 41.6% fewer steps and 56.3% lower token usage. Lightweight text-based cognitive-scaffolding tools showed limited behavioral impact.

## Why it matters
A direct, quantified answer to a design question every coding-agent builder faces — which tool interface style to expose — with specific trade-offs (consistency vs. token/step cost, natural-language vs. structured access) rather than intuition. The CodeAct-style efficiency numbers (41.6% fewer steps, 56.3% fewer tokens for comparable performance) are a concrete data point for cost-sensitive agent harness design.

## Verification notes
Read via the arXiv abstract page (2026-08-13). The six-architecture comparison, the 11,700-trajectory scale, and all four headline figures (4.7x consistency, 11% file-access increase, 41.6%/56.3% CodeAct efficiency gains, and the scaffolding-tool null result) are quoted/paraphrased directly from the abstract. Full paper (task selection, statistical tests) not read at capture; findings not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
