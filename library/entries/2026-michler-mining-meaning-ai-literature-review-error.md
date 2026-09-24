---
slug: 2026-michler-mining-meaning-ai-literature-review-error
title: "Mining Meaning: Measurement Error in AI-Assisted Literature Reviews"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2609.27686
canonical_ids: ["arxiv:2609.27686"]
publisher_or_author: "Jeffrey D. Michler, Kieran Douglas, Anna Josephson — arXiv preprint (econ.GN)"
published: 2026-09-23
captured: 2026-09-24
relevance:
  social_science: high
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (AI applied to social-science research): frames LLM-assisted
  literature review as a measurement-error problem and tests it directly
  (three ChatGPT implementations classifying papers using rainfall as an
  instrument), a concrete, evaluable application rather than a demo. Also
  high on ai_engineering lens 4 (evaluation and validation): the central
  finding — that standard classification-accuracy metrics do not predict
  whether downstream substantive conclusions are robust — is a directly
  actionable warning for anyone building AI-assisted research pipelines.
---

# Mining Meaning: Measurement Error in AI-Assisted Literature Reviews

## Summary

The authors treat the use of large language models to read, classify, and
synthesize academic literature as a measurement-error problem rather than a
simple accuracy question. They test three ChatGPT-based implementations on
the task of identifying economics papers that use rainfall as an
instrumental variable. The models "perform adequately on straightforward
classification tasks, [but] their accuracy declines substantially when
greater contextual judgment is required" (unverified paraphrase of the
abstract's framing). The paper's central, directly quoted-in-abstract claim
is that measurement error "affects paper-level conclusions much more
severely than broader literature-level claims" — aggregate accuracy can look
fine even when individual paper-level classifications used for a specific
downstream argument are wrong.

## Why it matters

For social-science researchers: this is a concrete test of a specific,
common AI-assisted-research workflow (LLM-driven literature classification
and synthesis), with a clear finding about where it fails — a template for
how to evaluate similar AI-assisted pipelines rather than trusting them by
default.

For AI-engineering practitioners building research or policy products: the
paper's warning generalizes past literature review. Standard performance
metrics (accuracy, F1) computed at the dataset level can mask exactly the
paper-level or claim-level errors that matter for a specific downstream use.
Anyone validating an LLM-based extraction or classification step in a
research pipeline needs to check robustness of the specific claims drawn
from it, not just aggregate accuracy — directly actionable for eval design
(lens 4).

## Verification notes

Fetched directly from the arXiv abstract page (2609.27686; v1 submitted
2026-09-23 11:05:12 UTC). Authors, task design (three ChatGPT
implementations, rainfall-as-instrument classification task), and the two
headline claims (adequate performance on straightforward classification,
substantial decline under contextual judgment; paper-level error exceeding
literature-level error) trace directly to the abstract's own stated
findings. Full paper (per-implementation accuracy figures, robustness-check
methodology) not read at capture — upgrade path noted for a future
verification pass if a deeper methodological check is needed.

## Updates

None yet.

## Related entries

None yet.
