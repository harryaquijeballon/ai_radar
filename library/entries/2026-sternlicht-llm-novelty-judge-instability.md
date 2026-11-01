---
slug: 2026-sternlicht-llm-novelty-judge-instability
title: "Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation"
status: accepted
domains: [ai_engineering, social_science]
source_type: academic
source_url: https://arxiv.org/abs/2610.02022
canonical_ids: ["arxiv:2610.02022"]
publisher_or_author: "Noy Sternlicht, Simra Shahid, Peter Jansen, Daniel S. Weld, Pao Siangliulue, Tom Hope"
published: 2026-10-01
captured: 2026-11-01
relevance:
  social_science: medium
  ai_engineering: high
verification: verified
rationale: >-
  High for ai_engineering lens 4 (LLM-as-judge validity): a sharply
  quantified demonstration that novelty judges flip verdicts under
  near-cosmetic prompt changes, and that purpose-built evaluators cost
  more while performing worse than a simple prompted baseline. Medium for
  social_science lens 6 (AI applied to social-science research): a
  credible, transferable warning about using LLMs to judge the novelty or
  quality of research contributions — directly relevant to any workflow
  that would use an LLM judge on research outputs, economics included.
---

# Old Ideas, Novel Problems: The Instability of LLM-Based Novelty Evaluation

## Summary

The paper studies whether LLMs can reliably judge whether an AI-generated
research idea is novel — a task usually validated only against
human-written papers. The authors build an evaluation set by mining
OpenReview reviewer comments that unanimously affirm or dispute a paper's
originality, assembling a high-novelty pool of 154 human ideas and a
lower-novelty pool of 145 human ideas (the "Human-Only" setting), and
pairing the 154 high-novelty ideas with ideas from a simple LLM generator
to form a "Human+Generated" setting with weak labels. Six judge models
(GPT-5.1, GPT-5.2, GPT-5.4, Claude Sonnet 4.5, Claude Opus 4.5, Claude
Opus 4.6) were tested in pointwise and pairwise formats, varying one
factor at a time: prompt wording, reasoning budget, retrieval access,
formatting, vote aggregation, and generator model.

Headline findings: on the Human+Generated pairs, GPT-5.4's accuracy fell
from 93.5% to 40.9% — a roughly 53-point drop, with more than half its
verdicts flipping — when the prompt was simplified. The same prompt change
moved accuracy by only about 7 points on Human-Only pairs, though Claude
Opus 4.6 still shifted by 21 points there. When comparing ideas from two
AI generators against each other, roughly a quarter to a third of
verdicts changed across prompt variations. More retrieval and reasoning
budget did not reliably help: an agentic GPT-5.6 "Sol" judge with arXiv
search scored 0.78 macro-F1, below Claude Opus 4.6's plain 0.89, at
roughly 10x the cost. Two purpose-built novelty evaluators also
underperformed a simple prompted baseline: a Claude Opus 4.6 prompt with
majority voting scored 0.854 macro-F1 for $2.59, versus 0.642 for $30.66
(Idea Novelty Checker) and 0.772 for $82.05 (Sakana AI Scientist's
evaluator). The blog summary describes the evaluation-set construction as
based on "ICLR 2026 peer reviews"; the arXiv abstract itself says only
"OpenReview," which hosts ICLR but also other venues — this specific
venue attribution is (unverified).

## Why it matters

For ai_engineering: a concrete, high-signal warning against trusting an
LLM-as-judge pipeline for any evaluative task resembling novelty or
quality assessment — near-cosmetic prompt changes can flip the majority
verdict, and spending 10x more on retrieval/reasoning or buying a
purpose-built evaluator does not reliably buy more accuracy. Directly
actionable for anyone building an eval harness that uses an LLM judge
(lens 4).

For social_science: a transferable, credible failure-mode finding for any
research or policy workflow considering an LLM judge to assess the
originality or quality of papers, proposals, or ideas — a caution squarely
on lens 6's "attention to credibility and validation, not novelty."

## Verification notes

Primary claims traced to the arXiv abstract page (fetched 2026-11-01,
first submitted 2026-10-01 as v1, revised to v3 on 2026-10-26) and
corroborated against the Hugging Face / Ai2 blog write-up
(huggingface.co/blog/allenai/novelty-bench, published 2026-10-27), which
supplied the specific quantified figures (93.5%→40.9%, the macro-F1/cost
comparisons) consistent with the abstract's qualitative description. The
blog's "ICLR 2026" framing of the data source is not corroborated by the
abstract itself (which says "OpenReview" only) and is marked (unverified);
it is not load-bearing for the entry's headline claims.

Eligibility note: v1 (2026-10-01) is outside this run's 7-day discovery
cap on its own; this entry is treated as new on the strength of the v3
revision (2026-10-26, within cap) and the Hugging Face blog's first public
write-up of the full six-judge/cost-comparison results (2026-10-27, also
within cap and the actual discovery trigger via the curated Hugging Face
source) — both read as presenting materially fuller results than a bare
v1 preprint would. Whether v1 already contained the same figures was not
independently checked; flagged for the user's awareness given the
judgment call involved.

## Updates

None yet.

## Related entries

None yet.
