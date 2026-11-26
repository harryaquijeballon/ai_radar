---
slug: 2026-khaleti-reasoning-models-auction-bidding
title: "Budget, Readout or Reasoning? Where Small Reasoning Models Lose Value in Auction Bidding"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.34068
canonical_ids: ["arxiv:2611.34068"]
publisher_or_author: "Mahbod Khaleti, Seyed Reza Tavakoli, Baran Hoseini, Alireza Noori, Amir Amini, Koorosh Aslansefat, Marjan Alirezaie, Ali Habibnia — arXiv preprint"
published: 2026-11-25
captured: 2026-11-26
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A mechanism-specific audit pattern (consistency-check against an exact
  calculator, plus token-cap and answer-timing fixes) that recovers most of
  a small reasoning model's lost decision-making value — a concrete,
  quantified deterministic-guardrail technique for lens 4.
---

# Budget, Readout or Reasoning? Where Small Reasoning Models Lose Value in Auction Bidding

## Summary

Ad platforms and marketplaces show bidders a "bid landscape" — estimated win
chances at each candidate bid — and some let reasoning-model agents choose
bids directly. The authors test six open reasoning models (4B–14B
parameters) against win curves from eBay closing prices and a simulated
advertising market (AuctionNet), scoring model bids on held-out auctions
against an exact calculator. Small reasoning models lose bidding value
mainly through their own choice errors (often skipping the option their own
reasoning ranks first, with wrong answers biased toward the highest bid on
the menu by size rather than position) rather than arithmetic mistakes —
costing 7–17% of the calculator's surplus under pay-your-bid pricing at 768
forced tokens on eBay. Two further losses are attributable to deployment
choices: token caps that cut reasoning short (letting models stop on their
own within 4,096 tokens recovers 91–100% of the calculator's advantage for
five of six models), and requesting the answer before the reasoning block
closes (closing the block first raises the weakest model from 42% to 84% on
eBay and 24% to 81% on AuctionNet). A consistency audit that flags bids
inconsistent with the trace's own numbers and replaces them with the
calculator's bid raises recovered advantage on eBay from 42–85% to 84–100%
under nested cross-validation, with the same settings transferring to
AuctionNet.

## Why it matters

A directly transferable deterministic-guardrail pattern for any agent
deployment that lets a small reasoning model make a scored decision: don't
truncate reasoning with a hard token cap, don't force the answer before
reasoning closes, and run a cheap consistency audit against an
independently computable ground truth before accepting the model's output.
The quantified recovery rates (reasoning-truncation and answer-timing fixes
alone recovering most of the lost value; the audit recovering nearly all of
it) make this a concrete, measurable deterministic check around a stochastic
component — squarely lens 4.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.34068, v1 submitted
2026-11-25). The setup, failure attribution, and all quantified recovery
rates above are traced to the abstract's own description. No independent
corroboration was available or attempted beyond the source text; this is
the paper's own novel benchmark and audit-method contribution.

## Updates

None yet.

## Related entries

None yet.
