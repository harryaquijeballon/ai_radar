---
slug: 2026-dahl-american-medical-directory-panel-transcription
title: "The American Medical Directory Panel: Comparing AI-Assisted and LLM Transcription with Manual Data Entry at Scale"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.25218
canonical_ids: ["arxiv:2611.25218"]
publisher_or_author: "Christian M. Dahl, Sophie Li, Rasmus Emil Nyholm, Maja U. Pedersen, Anthony Wray — arXiv preprint"
published: 2026-11-18
captured: 2026-11-20
relevance:
  social_science: high
  ai_engineering: high
license: "CC BY-SA 4.0"
verification: verified
rationale: >-
  Cross-domain high: for social_science, lens 6 (AI applied to
  social-science research) — a concrete, validated application of
  AI-assisted and LLM data-extraction pipelines to build a large historical
  economic/biographical dataset (the American Medical Directory), evaluated
  against a manual double-entry benchmark rather than asserted. For
  ai_engineering, lens 8 (reliable research and policy products) — a
  document-extraction and validation pattern with quantified accuracy and
  cost trade-offs across five competing workflows, directly transferable to
  building defensible data-analysis pipelines from semi-structured sources.
---

# The American Medical Directory Panel: Comparing AI-Assisted and LLM Transcription with Manual Data Entry at Scale

## Summary

Digitizes the 1912 and 1921 editions of the American Medical Directory, a
US physician register with roughly 140,000 and 150,000 entries, and
compares five machine-extraction workflows against a full manual
transcription that was itself double-entered for quality control. The
paper frames its question directly, quoted: "How closely does machine
transcription agree with manual double-entry data?" Because the directory
is semi-structured (not tabular), extraction errors can come from
misreading page layout as well as text. A rule-based parser — with rules
written by coding agents — applied to commercial OCR text recovered about
97% of the manually transcribed records at similar precision, outperforming
a multimodal language-model workflow that read both page images and OCR
text. The two approaches failed on partly overlapping records, so combining
their outputs raised recall and precision to about 98%. An open-weight LLM
pipeline run on a local GPU server scored between the two single methods on
recall, and swapping the commercial OCR for an open-source alternative
lowered that pipeline's recall by only about 2 percentage points. The
authors are explicit that, because the manual transcription's own error
rate is unknown, the reported rates measure agreement with manual entry,
not ground-truth accuracy. Direct processing cost was roughly €0.03 per
page for the commercial-OCR and multimodal workflows, versus €14.70 per
page for manual transcription.

## Why it matters

For social-science researchers building historical or large-scale datasets
with AI assistance: a rare study that validates AI/LLM extraction against a
real double-entered manual benchmark rather than assuming machine output is
correct, and that reports where the methods disagree rather than only an
aggregate accuracy number — a template for building new economic or
demographic datasets credibly. For AI-engineering builders of document-
grounded research pipelines: evidence that combining a cheap rule-based
parser (over commercial OCR) with a second, differently-failing method
raises reliability more than either method alone, and a concrete
~500x cost gap (€0.03 vs €14.70/page) against which to justify a
validation-plus-automation pipeline design instead of either pure-manual or
pure-LLM extraction.

## Verification notes

arXiv abstract page fetched directly (2026-11-20) in two passes: one for a
general summary, one requesting verbatim text (quote-length-limited to 125
characters per fetch). Both passes returned consistent figures: ~97% single-
method recall, ~98% combined recall/precision, the ~2-point recall drop from
swapping OCR vendors, and the €0.03 vs €14.70 per-page cost comparison.
Submission history shows a single version (v1), submitted Wed, 18 Nov 2026,
21:44:10 UTC — within this run's discovery window (2026-11-19 → 2026-11-20)
and the 7-day eligibility cap. Categories: econ.GN (General Economics) with
cs.DB (Databases) as the citation category shown on the page. Licence
(CC BY-SA 4.0) stated on the abstract page. Full paper (the five-workflow
comparison tables and error analysis) not read at capture; no independent
secondary corroboration attempted (new working paper, no secondary coverage
found this run).

## Updates

None yet.

## Related entries

None yet.
