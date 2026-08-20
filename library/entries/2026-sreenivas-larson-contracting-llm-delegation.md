---
slug: 2026-sreenivas-larson-contracting-llm-delegation
title: "Contracting for LLM Delegation: Moral Hazard in Technology and Effort Choice"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.18232
canonical_ids: ["arxiv:2608.18232"]
publisher_or_author: "Nanda Kishore Sreenivas, Kate Larson — arXiv preprint"
published: 2026-08-18
captured: 2026-08-20
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Clears lens 1/6 (agent architecture and governed delegation) at high: a
  principal-agent contract-design framework for incentivizing model and
  effort-level (token-budget) choice in agentic workflows, empirically
  calibrated on MATH/MMLUPro with bandit-learning convergence evidence.
---

# Contracting for LLM Delegation: Moral Hazard in Technology and Effort Choice

## Summary

The paper extends principal-agent (contract) theory to a setting where an "agent" chooses both which LLM/technology to use and an effort level (e.g., token budget), with output quality modeled as a concave, saturating function of these hidden, two-dimensional choices. The authors derive optimal linear contracts for a principal seeking to incentivize this delegation, and show the agent's best response exhibits threshold-based technology switching (unverified detail beyond the abstract). Using empirical calibration on the MATH and MMLUPro benchmarks with open-weight models, they report that bandit-learning algorithms converge toward the theoretically predicted equilibrium strategies, concluding that "simple linear contracts can effectively incentivize complex, technology-aware delegation in agentic workflows" (quoted from the source).

## Why it matters

Teams that route work across multiple models/effort levels (e.g., cheap vs. expensive model tiers, small vs. large token budgets) currently do this with ad hoc heuristics or learned routers. This paper offers a principled, quantitatively calibrated way to design the incentive/reward structure so that delegated choices (which model, how much effort) align with a principal's objectives — directly relevant to building governed multi-model routing and budget-allocation policies for agentic systems, an area (lens 1/6) where evidence-backed patterns are still rare.

## Verification notes

Fetched arXiv abstract page 2608.18232 (submitted 2026-08-18, cs.MA). Claims traced to the abstract: the principal-agent framing, the concave/saturating output model, the "linear contracts" result, and the MATH/MMLUPro calibration with bandit-convergence finding. Not independently corroborated against the full paper or the benchmark results tables — no secondary source cross-checked. Verification is partial; the headline claim (bandit convergence to predicted equilibrium) is stated directly in the abstract and so is traceable, but its magnitude is not quantified in the fetched text.

## Updates

<!-- Append-only, dated, newest last. Never rewrite the Summary. -->

## Related entries

None yet.
