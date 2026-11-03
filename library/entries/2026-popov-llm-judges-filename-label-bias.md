---
slug: 2026-popov-llm-judges-filename-label-bias
title: "Same Text, Different Filename: Are LLM Judges Biased?"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.01829
canonical_ids: ["arxiv:2611.01829"]
publisher_or_author: "Sergey V. Popov"
published: 2026-11-01
captured: 2026-11-03
relevance:
  social_science: high
  ai_engineering: high
verification: verified
rationale: >-
  High cross-domain: a controlled experiment showing three frontier LLMs
  score an identical document differently depending only on the label
  attached to its filename, with a context-specific (not simply
  own-group-favoring) bias. High on ai_engineering lens 4 (LLM-as-judge
  validity, a named failure mode with a quantified test); high on
  social_science lens 5 (a credible warning about a method failure mode)
  given the abstract's own note that leading economics journals began
  using an LLM tool for technical quality assessment of submissions in
  2026.
---

# Same Text, Different Filename: Are LLM Judges Biased?

## Summary

Tests whether renaming a file changes how LLM judges rate the same
document's quality. Three frontier LLMs scored the identical document
differently depending on the filename's label. A label referring to a
person scored higher than no label at all. The study found no consistent
preference for own-group versus rival-group labels and no penalty for an
Asian name, but did find a context-specific label bias whose direction and
size vary with the document and the label itself. For LLM-written
documents, some self-preference also appears, alongside the
context-dependent label bias. The author frames whether to correct for the
bias as a question of the relative costs of evaluation errors, and notes
that leading economics journals began using an LLM tool for technical
quality assessment of submissions during 2026 (as stated in the fetched
abstract; full experimental design, model list, and effect sizes not
reviewed at capture).

## Why it matters

For ai_engineering: a concrete, named failure mode for any pipeline using
an LLM as a judge or quality gate — superficial metadata (here, a
filename) can shift scores in a document-and-label-specific, not simply
predictable, direction, so blind or metadata-stripped evaluation should be
the default wherever LLM judges gate decisions. For social_science: a
timely, credible warning precisely because the abstract states that
economics journals have begun using LLM tools for submission quality
assessment in 2026 — anyone relying on such tools for peer review or
research triage needs to know that non-substantive metadata can move the
score, sharpening the question of whether research processes built on
model outputs can be trusted.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 1 Nov 2026, no revisions). The three-LLM filename-label
experiment, the "no consistent own/rival-group preference, no
Asian-name penalty" finding, the context-specific label bias, the
self-preference note for LLM-written documents, and the note on economics
journals adopting LLM technical-assessment tools in 2026 all trace to the
fetched abstract text, which is the paper's own stated summary — treated
as `verified` on this library's convention for single-source arXiv
preprints whose headline claims are self-reported. The full paper (exact
models tested, effect sizes, document/label pairings) was not reviewed at
capture.

## Updates

None yet.

## Related entries

None yet.
