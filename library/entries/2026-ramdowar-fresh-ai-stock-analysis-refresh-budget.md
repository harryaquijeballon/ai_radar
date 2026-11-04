---
slug: 2026-ramdowar-fresh-ai-stock-analysis-refresh-budget
title: "When Is Fresh AI Stock Analysis Worth It? Allocating a Limited Research Budget Across a Portfolio"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.04348
canonical_ids: ["arxiv:2611.04348"]
publisher_or_author: "Russlan Ramdowar"
published: 2026-11-04
captured: 2026-11-04
relevance:
  social_science: medium
  ai_engineering: medium
rationale: >-
  Medium on AI applied to social-science/finance research (social_science
  lens 6) and agent architecture/orchestration (ai_engineering lens 1): a
  large, quantified empirical comparison of refresh strategies for
  long-horizon multi-agent research reports, with a concrete, horizon-
  dependent decision rule for when to reuse versus regenerate agent output.
verification: verified
---

# When Is Fresh AI Stock Analysis Worth It? Allocating a Limited Research Budget Across a Portfolio

## Summary

Studies how often a long-horizon AI-generated investment thesis needs to be
fully regenerated versus reused as prices move, analyzing 8,120 production
multi-agent research reports on 203 stocks from four iPulse AI batches.
Compares four refresh approaches — repricing existing targets, guarding them
against price shocks, mechanically resetting old forecast growth paths, and
generating fresh multi-agent reports — across ten matched configurations and
seven investment frameworks, simulating Top 10/Top 30 USD portfolios with
modeled trading costs and compute charges, and measuring token workloads to
estimate refresh costs and break-even budgets. In two short, unchanged-model
windows, guarded reuse averaged 2.25% versus 1.66% for SPY and 4.77% for
fresh reports, and beat SPY in all three short windows tested including a
model-change transition. Over a near-six-month holding period the ranking
reversed: guarded reuse returned -11.26%, fresh reports +9.12%, SPY +3.46%.
Mechanically re-anchoring old growth paths captured 98% of the
forecast-error improvement over fixed targets, yet the fresh and reset
approaches shared only 1-4 of their Top 10 stock picks. For Top 30
portfolios, guarded reuse outperformed (4.17% vs. 1.88%). The authors note
results are sensitive to horizon choice and a few exceptional winners.

## Why it matters

A concrete, quantified answer to a question that applies well beyond
finance: for a long-horizon multi-agent pipeline producing a decision
artifact that goes stale, when does cheap reuse-with-guardrails beat
full regeneration, and when does it actively hurt? The paper's proposed
split — continuous monitoring, periodic full rebuilding, and targeted
editorial checks — is a transferable architecture pattern for any agentic
pipeline balancing freshness against compute cost, with the caveat that the
specific numbers are drawn from one application (equity research) and
sensitive to the chosen horizons.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-04). The dataset size, the four compared approaches, the simulated
portfolio design, and all quantified return/overlap figures trace to the
abstract text. Full paper (the ten matched configurations, the seven
investment frameworks) not read at capture.

## Updates

None yet.

## Related entries

None yet.
