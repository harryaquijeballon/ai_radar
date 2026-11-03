---
slug: 2026-decclesiis-castellacci-ahmadi-validating-llm-synthetic-surveys
title: "Validating LLM-Generated Synthetic Survey Samples: A Use-Dependent Multi-Dimensional Framework for Social-Science Applications"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.00256
canonical_ids: ["arxiv:2611.00256"]
publisher_or_author: "Enrico Angelo Raffaele D'Ecclesiis, Fulvio Castellacci, Arash Ahmadi"
published: 2026-10-30
captured: 2026-11-03
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  High on causal inference and empirical methods (lens 5) and AI applied to
  social-science research (lens 6): proposes and empirically applies a
  use-dependent validity framework for LLM-generated synthetic survey
  respondents, rather than a single accuracy score, on real Eurobarometer
  AI-attitude data. Medium on ai_engineering (lens 8): a transferable
  validation pattern for data-analysis/simulation agents, but aimed at
  research methodology rather than a builder's immediate tooling choice.
---

# Validating LLM-Generated Synthetic Survey Samples: A Use-Dependent Multi-Dimensional Framework for Social-Science Applications

## Summary

Argues that no single accuracy measure can judge whether LLM-generated
synthetic survey respondents are useful: a synthetic sample may match
individual respondents poorly while still preserving the distributional or
substantive patterns a given analysis needs. The authors propose a
use-dependent framework with three validity dimensions — predictive,
distributional, and substantive — and apply it to Eurobarometer data on
public attitudes toward artificial intelligence. Four off-the-shelf LLMs
generate synthetic responses from observed respondent profiles, with
supervised machine learning as a predictive benchmark. Results differ by
dimension: some LLM-generated samples preserve meaningful marginal
heterogeneity, demographic ordering, cross-country variation, and
predictor structure despite imperfect respondent-level correspondence;
performance varies by model and outcome, but the authors describe the
overall conclusion as cautiously positive (figures and framing as stated in
the fetched abstract; full paper, including per-model/per-dimension
results, not reviewed at capture).

## Why it matters

Gives social scientists considering LLM-generated synthetic respondents (an
increasingly common but validity-contested practice, lens 6) a concrete
framework to apply rather than a single pass/fail accuracy check: ask which
of predictive, distributional, or substantive validity the intended
analysis actually needs, since a sample can fail one while serving another.
Directly reusable by any researcher evaluating synthetic survey data on a
specific AI-attitudes or other topic, and by AI-engineering teams building
data-analysis or simulation agents that need a validation step appropriate
to the downstream use rather than a generic benchmark score.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 30 Oct 2026, no revisions). The three-dimension framework, the
Eurobarometer AI-attitudes application, the four-LLM/supervised-ML design,
and the "cautiously positive" overall finding all trace to the fetched
abstract text, which is the paper's own stated summary of its design and
results — treated as `verified` on the convention applied elsewhere in
this library to single-source arXiv preprints whose headline claims are
self-reported. The full paper (per-dimension, per-model results; data and
code) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
