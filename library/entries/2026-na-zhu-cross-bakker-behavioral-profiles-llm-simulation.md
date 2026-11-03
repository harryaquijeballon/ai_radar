---
slug: 2026-na-zhu-cross-bakker-behavioral-profiles-llm-simulation
title: "Designing Behavioral Profiles for Language Model Simulation of Out-of-Distribution Human Behavior"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.00661
canonical_ids: ["arxiv:2611.00661"]
publisher_or_author: "Robin Na, Kehang Zhu, Logan Cross, Michiel A. Bakker"
published: 2026-10-31
captured: 2026-11-03
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  High on AI applied to social-science research (lens 6): a large-scale
  (616 public-goods games, 144 bargaining games, 1,480 money-request
  designs), concrete and evaluable test of which behavioral-profile
  features let LLMs simulate human behavior out-of-distribution — the
  credibility frontier for LLMs as simulated economic agents. Medium on
  ai_engineering (lens 8): a transferable validated-simulation-design
  pattern (profile choice as a testable design parameter), though aimed at
  behavioral-science simulation rather than general agent engineering.
---

# Designing Behavioral Profiles for Language Model Simulation of Out-of-Distribution Human Behavior

## Summary

Examines which descriptions of people ("behavioral profiles") help
language models simulate human behavior when experimental conditions
change. The authors build a framework drawing behavioral features from the
literature, create profiles from earlier human experiments, use one LLM to
assign feature values from observed actions/messages/surveys, and a
separate LLM to simulate behavior from those profiles. Forward feature
selection keeps features only while they improve prediction on training
data; selected profiles are then tested unchanged on new participants and
new experimental designs. Across 616 public-goods games, 144 multi-party
bargaining games, and 1,480 generalized 11-20 money-request designs,
one-feature profiles predicted human outcome distributions better than no
profile or general-purpose personas. Adding more features gave no clear
extra benefit, and a feature's predictive value largely held from training
to validation; reusing profiles across different game families gave uneven
results, sometimes worse than no profile at all (as stated in the fetched
abstract; full results tables and statistical tests not reviewed at
capture).

## Why it matters

Gives researchers using LLMs as simulated economic or social agents
("homo silicus") a tested, falsifiable design rule rather than intuition:
minimal (one-feature) behavioral profiles tend to outperform richer
personas, more features do not reliably help, and profiles built for one
game family should not be assumed to transfer to another without testing.
Directly actionable for anyone designing an LLM-agent simulation study —
profile choice becomes a testable part of the design, not a fixed
assumption.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 31 Oct 2026, no revisions). The three-game-family design
(616/144/1,480 instances), the forward-feature-selection method, the
one-feature-profile advantage over no-profile/personas, the lack of
benefit from additional features, and the uneven cross-family transfer
finding all trace to the fetched abstract text, which is the paper's own
stated summary — treated as `verified` on this library's convention for
single-source arXiv preprints whose headline claims are self-reported. The
full paper (exact accuracy figures, statistical tests, feature list) was
not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
