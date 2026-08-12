---
slug: 2026-macedosantos-copom-tone-llm
title: "Reading Copom's Tone: A Weighted LLM Framework for Hawkish-Dovish Sentiment, Forward Guidance, and Uncertainty"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2608.07251
canonical_ids: ["arxiv:2608.07251"]
publisher_or_author: "Gabriel de Macedo Santos — arXiv preprint"
published: 2026-08-07
captured: 2026-08-10
relevance:
  social_science: medium
  ai_engineering: n/a
verification: verified
rationale: >-
  Medium on lens 5 (LLMs as research instruments — text-as-data) and lens 6
  (AI applied to social-science research): extends a private-sector central
  bank sentiment classifier into an auditable, three-layer scoring framework
  for Brazilian Copom communications. Medium rather than high because it is a
  single-author, non-peer-reviewed preprint whose own abstract disclaims
  forecasting validity — a usable measurement instrument, not yet a
  validated result.
---

# Reading Copom's Tone: A Weighted LLM Framework for Hawkish-Dovish Sentiment, Forward Guidance, and Uncertainty

## Summary

Documents an applied NLP framework for measuring the tone of Brazilian
Monetary Policy Committee (Copom) statements, explicitly inspired by iSent,
Itaú's central-bank sentiment classifier, particularly its sentence-level
division of communication into hawkish, dovish, neutral, and out-of-context
classes. The framework extends that idea three ways: (1) an LLM identifies
short hawkish/dovish expressions and assigns each a 0-to-1 intensity weight;
(2) a document index combines sentence counts with document-specific average
signal intensities into a bounded -1-to-1 score; (3) a separate
full-document layer measures forward-guidance direction, guidance
explicitness, uncertainty level, and change in uncertainty. The sample
covers communications from August 31, 2016 through August 5, 2026 (80
statements, 1,498 classified sentences): 33.3% of sentences are hawkish,
18.0% dovish, 42.1% neutral, 6.5% out of context. The average document score
is +0.107; the most hawkish reading is +0.570 (August 2021). The latest
statement (August 5, 2026) scores +0.232 (eight hawkish, two dovish, nine
neutral sentences), with guidance classified as directionally ambiguous but
partly explicit, and uncertainty classified as central and higher than the
prior meeting. Tone and the guidance-direction score have a contemporaneous
Pearson correlation of 0.719. The paper states explicitly these are
descriptive outputs, not a validated forecast of Selic decisions or DI
returns; its contribution is framed as methodological — a transparent,
incremental, auditable system separating rhetorical tone from policy
guidance and uncertainty.

## Why it matters

Gives economists working on central-bank communication a transparent,
replicable NLP framework extending beyond the Fed/FOMC-focused literature to
a major emerging-market central bank (Brazil's Copom), and models an
auditable design pattern — separating tone from structural guidance and
uncertainty, with an explicit intensity weight rather than a bare
sentence count — that other central-bank-tone researchers could adapt or
benchmark their own classifiers against.

## Verification notes

arXiv abstract page fetched directly (2026-08-10); author (Gabriel de Macedo
Santos), submission timestamp (7 Aug 2026, 14:08:31 UTC, v1), and categories
(econ.GN, cs.AI) confirmed. Every claim in the Summary — sample composition
and date range, sentence-class percentages, average and maximum document
scores, the latest statement's score and sentence breakdown, the tone/
guidance correlation, and the paper's own forecasting-validity disclaimer —
traces directly to the fetched abstract text. Full paper PDF not read at
capture. No independent corroboration attempted: this is a single-author,
not-yet-peer-reviewed preprint reporting the output of its own method
(self-described computational statistics), not an external fact requiring
corroboration; recorded as `verified` consistent with this project's
treatment of other abstract-traceable preprint captures.

## Updates

None yet.

## Related entries

None yet.
