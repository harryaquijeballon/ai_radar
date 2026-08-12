---
slug: 2026-malenfant-moral-hazard-multiagent-llms
title: "Moral Hazard in Multi-Agent Language Models"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.23982
canonical_ids: ["arxiv:2607.23982"]
publisher_or_author: "Dane Malenfant — arXiv preprint"
published: 2026-07-27
captured: 2026-07-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on agent architecture/orchestration and evaluation (lenses 1, 4): a
  controlled diagnostic game (3,015 decisions across nine cost variations)
  showing that standard optimization methods (SFT, RLOO, GEPA) can improve
  aggregate multi-agent reward while leaving the underlying cooperative
  failure — agents not reporting hidden safety information that benefits
  others — unresolved, a concrete warning against evaluating multi-agent
  systems on aggregate success metrics alone.
---

# Moral Hazard in Multi-Agent Language Models

## Summary

Studies a cooperative failure mode in multi-agent LLM systems where
"socially valuable effort is costly, weakly observable, and mainly
benefits others." The author introduces the Dialogue Moral Hazard Game, a
controlled textual environment operationalizing this hidden-action dynamic:
an agent can keep an immediate local reward or pay a query cost to reveal
hidden safety information that benefits other agents' decisions. Testing
seven open-weight models plus one frontier API model (GPT-5.6 Sol), base
models typically either keep the local reward without achieving team
success, or pay the query cost without actually communicating the
decision-relevant information. A larger run (3,015 decisions, scripted
partners, nine cost variations) shows empirical query thresholds track
theoretical predictions closely. Applying SFT, RLOO, sequential SFT+RLOO,
and GEPA optimization as diagnostics, the paper reports heterogeneous
effects: some methods raise aggregate reward while reducing the costly
cooperative queries that were supposed to be encouraged — i.e., they
improve the score without fixing the underlying cooperative failure.

## Why it matters

A concrete, quantified caution for anyone using aggregate reward or success
rate to evaluate or tune multi-agent systems: this paper shows a system can
be optimized to look better on the aggregate metric while its
actually-intended cooperative behaviour (agents sharing costly-to-reveal
safety-relevant information) gets worse, not better. Directly applicable to
designing evaluation suites for multi-agent or agent-team systems — the
paper's own recommendation is to evaluate mechanism-level behaviour, not
just aggregate outcomes.

## Verification notes

arXiv abstract page fetched directly (2026-07-29); title, author, and
"Submitted on 27 Jul 2026 (v1); 28 Jul 2026 (v2)" confirmed. The game
design, the seven-open-weight-plus-one-frontier-model test set, the
3,015-decision/nine-cost-variation experiment, and the
optimization-improves-aggregate-but-not-mechanism finding all trace to the
fetched abstract text. Full paper (exact per-model results, GEPA
configuration) not read at capture.

## Updates

None yet.

## Related entries

[2026-guo-seal-self-verification-unreliable](2026-guo-seal-self-verification-unreliable.md) — another diagnostic finding that a system can be optimized to look better on a proxy/self-reported signal while the underlying property it's meant to track does not improve.
