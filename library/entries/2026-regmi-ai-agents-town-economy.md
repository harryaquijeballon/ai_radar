---
slug: 2026-regmi-ai-agents-town-economy
title: "But How Would AI Agents Run a Town's Economy?"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2609.11108
canonical_ids: ["arxiv:2609.11108"]
publisher_or_author: "Sajal Regmi, Siddhartha Pudasaini, Chetan Phakami Pun"
published: 2026-09-10
captured: 2026-09-13
relevance:
  social_science: high
  ai_engineering: high
verification: verified
rationale: >-
  Cross-domain (scored medium+ on both profiles per ENGINE.md's cross-domain
  rule): a concrete, quantified generative-agent simulation of a closed
  spatial economy that reproduces real macro phenomena (wage stickiness, low
  marginal propensity to consume, slow-loosening wealth concentration) —
  social_science lens 6 (AI simulating economic agents, with credibility
  markers) and ai_engineering lens 1/8 (a multi-agent simulation harness
  whose outcomes are shown to be model-dependent).
---

# But How Would AI Agents Run a Town's Economy?

## Summary

The authors place "100 memory-equipped large language model agents in charge
of a closed, money-conserving spatial economy" modeled on Pokhara Lakeside's
geography, running 91 validated simulations across 26 simulated weeks. A
12x increase in simulated tourist demand raised business revenue only 4.62x,
decomposed into a 1.50x increase in trading breadth and 3.07x in individual
business revenue. Wages barely moved (1.03x, not statistically significant),
and only 0.3% of menu items were repriced. A randomized cash transfer found
96.7% of the transferred funds went unspent, implying a marginal propensity
to consume of 3–4%. Wealth distribution appeared frozen at short horizons
(correlation of 0.964 at 2 weeks) but loosened gradually to 0.752 at 26
weeks. Swapping the underlying LLM significantly changed outcomes, while
removing agents' memory had negligible effect.

## Why it matters

For social-science researchers, this is a rare LLM-agent economic simulation
that is explicit about its own limits and reports internally consistent,
economically interpretable frictions (sticky wages, low pass-through of
demand shocks, near-zero marginal propensity to consume) rather than a
frictionless toy economy — a concrete data point on how far generative-agent
macro simulation has come, and where it still needs external validation
before being treated as evidence about real economies (lens 6). For
AI-engineering builders, the finding that swapping the backing LLM
materially changes simulation outcomes — while removing agent memory does
not — is a direct, actionable robustness/ablation lesson for anyone building
or evaluating agent-based simulation harnesses (lens 1/8): report model
sensitivity before treating simulation outputs as stable.

## Verification notes

Read the arXiv abstract directly (primary source). All quantified figures
(12x/4.62x/1.50x/3.07x demand and revenue multipliers, 1.03x wage change,
0.3% repricing, 96.7% unspent transfer / 3–4% MPC, 0.964/0.752 wealth
correlations, 91 simulations over 26 weeks) are drawn from the abstract as
stated; not independently re-run. Scored against both domain profiles per
the cross-domain rule since it clears medium-or-above on both.

## Updates

None yet.

## Related entries

None yet.
