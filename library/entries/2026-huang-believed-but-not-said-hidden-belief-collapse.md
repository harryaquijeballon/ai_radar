---
slug: 2026-huang-believed-but-not-said-hidden-belief-collapse
title: "Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.22138
canonical_ids: ["arxiv:2610.22138"]
publisher_or_author: "Liangjie Huang, Henry Peng Zou, Wei-Chieh Huang, Wooseong Yang, Yuwei Han, Philip S. Yu — arXiv preprint"
published: 2026-10-15
captured: 2026-10-17
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on evaluation/guardrails and reproducibility-of-reasoning (lenses 4, 6):
  a controlled multi-agent experiment across six models and three datasets
  quantifying how far a single adversarial peer corrupts group belief, and
  showing that most of that influence is privately held and never surfaces
  in the visible transcript — directly relevant to the assumption, common in
  multi-agent harness design, that peer agents will catch each other's
  errors.
---

# Believed but Not Said: Measuring Hidden Belief Collapse in Multi-Agent LLM Discussions

## Summary

Per the arXiv abstract page (v1 submitted 15 Oct 2026), multi-agent LLM systems commonly assume peers will catch each other's factual errors. The authors test this with a minimal adversary: in a ten-agent factual discussion, one or three adversarial agents repeatedly assert a plausible false answer. After each round, the researchers privately probe each benign agent's actual belief (hidden from peers) and separately record its public stance. Across six models and three factual-QA datasets, groups stay accurate with no attacker, but a single adversary substantially raises the share of benign agents who end up holding the false answer: 0.6% with no adversary, 44.8% with one adversary, 60.5% with three adversaries. Much of this is invisible in the transcript — with three adversaries, benign agents privately held the false belief in 51.6% of exposed turns but only publicly endorsed it in 19.7% of those turns, and the false answer often persists even when agents are separately asked for their own independent view. Baseline task knowledge does not predict an agent's robustness to the adversary.

## Why it matters

A quantified warning against a load-bearing but rarely tested assumption in multi-agent harness design — that visible disagreement is a reliable signal of group robustness. The private/public gap (51.6% vs. 19.7%) means an observer reading only the discussion transcript would significantly underestimate how much a single bad-faith or malfunctioning peer has already corrupted the group's actual beliefs, which argues for independent, hidden-from-peers belief probes as a guardrail in production multi-agent pipelines rather than relying on the visible consensus.

## Verification notes

Source reachable (arXiv abstract page). Claims traced to the abstract-level summary only; the full 14-page paper (model list, dataset list, exact adversary prompting) was not opened, and the percentages were not independently corroborated beyond the abstract page's own statement of them.

## Updates

None yet.

## Related entries

None yet.
