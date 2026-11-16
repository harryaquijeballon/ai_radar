---
slug: 2026-nandi-tradegauntlet-trading-agent-compliance
title: "TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents"
status: accepted
domains: [ai_engineering, social_science]
source_type: academic
source_url: https://arxiv.org/abs/2611.18493
canonical_ids: ["arxiv:2611.18493"]
publisher_or_author: "Sandip Nandi, Aishwarya Bose, Apurba Bose, Soovadeep Bakshi — arXiv preprint"
published: 2026-11-13
captured: 2026-11-16
relevance:
  ai_engineering: high
  social_science: medium
verification: verified
rationale: >-
  High on ai_engineering lens 4 (evaluation, validation and deterministic
  guardrails): a replayable limit-order-book simulator that separately
  measures detection, prevention, and execution cost for compliance
  controls on trading agents, with a quantified, actionable finding that
  zero compliance alerts does not demonstrate compliance (scripted and
  search-based probes found split-order schedules that evade implemented
  rules). Medium on social_science lens 4 (competition/regulation):
  concrete evidence on how hard it is to build reliable behavioural
  controls for autonomous trading agents, directly relevant to the same
  AI-agent-market-manipulation question raised in
  [2026-margolin-framing-collusion-llm-agent](2026-margolin-framing-collusion-llm-agent.md).
---

# TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents

## Summary

Studies how to build controls that stop autonomous trading agents from
placing problematic orders without making legitimate trading impractical.
The authors present TradeGauntlet, a replayable limit-order-book simulator
that measures detection, prevention, and execution cost for compliance
controls separately rather than conflating them. In 1,680 simulated
sessions using Claude Haiku 5.5 and Sonnet 5.5 as the trading agents, every
conduct alert raised was a self-match; rules rejecting self-crossing orders
removed those alerts, and an aggregate position-size gate cut Sonnet's
two-sided fills by about 15%. A conduct reminder prompt reduced Sonnet's
alert rate but also cut Haiku's fills without a clear compliance benefit —
evidence that an agent raising zero alerts does not by itself demonstrate
compliance. Scripted probes and two automated search methods found
split-order schedules that evaded the implemented rules; a learned
detection baseline caught all 2,400 searched evasion episodes but also
flagged 15% of a large market maker's legitimate sessions. Aggregate caps
reduced the evasion gain unevenly depending on market conditions, shown via
a response fitted to five Nasdaq stocks and a separate ABIDES-simulator
experiment. An adversarial prompt attempting to elicit evasion strategies
led Sonnet to refuse in all 240 rounds, producing no candidate strategies.
The authors note the experiments establish reproducible test methodology
for trading-agent controls, not legal compliance or real-market detection
accuracy. (unverified: exact session/episode counts and model-specific
percentages are as stated in the abstract; full paper not read at
capture.)

## Why it matters

For builders of agentic financial or any other high-stakes autonomous
systems: a concrete methodology for evaluating compliance/safety controls
that separates detection, prevention, and the cost those controls impose
on legitimate behaviour — and a sharp warning that an agent producing zero
alerts can mean the control is working or that an adversary (automated
search, in this case) has simply found an evasion path the control
doesn't catch. The split-order-evasion and false-positive-on-legitimate-
market-maker-sessions findings are directly transferable red-team and
evaluation techniques for anyone deploying rule-based or learned guardrails
around an autonomous agent with room to game its own prevention rules.

## Verification notes

arXiv abstract page fetched directly (2026-11-16); title, full author list,
and "Submitted on 13 Nov 2026" confirmed. Subject categories (cs.MA, cs.AI,
cs.CE) confirmed from the abstract page. Every claim in the Summary traces
to the fetched abstract text: the TradeGauntlet simulator design, the
1,680-session count with named models, the self-match/self-crossing-rule
finding, the aggregate-gate fill reduction, the conduct-reminder result,
the split-order evasion and learned-baseline false-positive finding, the
Nasdaq/ABIDES market-assumption sensitivity, and the adversarial-prompt
refusal result. Full paper text not read at capture; no independent
corroboration attempted (new working paper, no secondary coverage found).
Appeared in arXiv's cs.MA "recent" listing dated Mon, 16 Nov 2026, a 3-day
gap from its stated submission date consistent with normal cross-list
announcement lag — within this run's 7-day eligibility cap. Upgrade path:
read the full PDF for the exact evasion-search methodology and the
learned-baseline false-positive analysis.

## Updates

None yet.

## Related entries

[2026-margolin-framing-collusion-llm-agent](2026-margolin-framing-collusion-llm-agent.md) — same underlying concern (AI agents acting as economic actors in trading/market contexts can be induced into or evade controls against manipulative behaviour), from the compliance-control-evaluation side rather than the behavioural-framing side.
