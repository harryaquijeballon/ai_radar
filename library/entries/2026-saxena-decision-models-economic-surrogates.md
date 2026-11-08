---
slug: 2026-saxena-decision-models-economic-surrogates
title: "Decision Models as Scalable Economic Surrogates that Capture Human Variation"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.05553
canonical_ids: ["arxiv:2611.05553"]
publisher_or_author: "Maxime Saxena, Fabio Caccioli, R. Maria del Rio-Chanona"
published: 2026-11-03
captured: 2026-11-08
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  High on social_science lens 6: a concrete, validated comparison of a new AI
  model class against LLMs as stand-ins for human respondents across three
  economic settings, with attention to whether human variation (not just the
  modal response) is reproduced. Medium on ai_engineering lens 8: a
  cost/latency/fidelity comparison directly relevant to choosing a model
  class for simulation-harness-style research products.
---

# Decision Models as Scalable Economic Surrogates that Capture Human Variation

## Summary

Introduces "Decision Models" (DMs) — a class of AI models that respond
quickly and output a probability distribution over a fixed set of options —
as a possible alternative to LLMs for standing in for humans in economic
simulations and surveys. The authors compare 10 DMs against 8 LLMs across
three settings: a household consumption-spending survey, classic economic
games, and a labour-market field experiment. Frontier DMs, which score
highest on general decision-making benchmarks, reproduce human response
variation more closely than LLMs in all three settings; they match LLMs on
the modal human response in the spending survey but do less well in the
economic games. Frontier DMs are also roughly ten times faster than the
fastest LLM tested and can be more than a hundred times cheaper. The authors
conclude DMs capture human heterogeneity better than LLMs while making
large-scale economic simulation more computationally and financially
feasible.

## Why it matters

For social_science: LLMs are increasingly used as simulated economic agents
("homo silicus")-style research instruments, and a documented tendency to
underrepresent human variation is a known validity problem (lens 6) — this
paper offers a concrete, benchmarked alternative class of model specifically
evaluated on whether it reproduces variation, not just central tendencies,
across three different experimental paradigms. For ai_engineering: a
builder choosing a model class for a simulation harness or synthetic-
respondent pipeline now has quantified cost/latency/fidelity trade-offs
(roughly 10x faster, 100x+ cheaper, better variation-fidelity in two of three
settings) rather than defaulting to an LLM by convention (lens 8).

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 3 Nov 2026, no revisions). The three-setting comparison design,
the "DMs beat LLMs on variation in all three settings but only match on the
modal response in one," and the speed/cost multiples all trace to the
fetched abstract text — treated as `verified` per this library's standing
convention for single-source arXiv preprints whose headline claims are
self-reported. The full paper (which 10 DMs and 8 LLMs specifically, exact
benchmark scores, game designs) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
