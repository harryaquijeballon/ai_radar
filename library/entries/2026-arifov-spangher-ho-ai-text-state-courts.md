---
slug: 2026-arifov-spangher-ho-ai-text-state-courts
title: "AI Might Be Flooding State Court Houses, but Proving It Is Another Matter"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://hai.stanford.edu/news/ai-might-be-flooding-state-court-houses-but-proving-it-is-another-matter
canonical_ids: []
publisher_or_author: "Javokhir Arifov, Alexander Spangher, Jonathan Hennessy, Diya Karan, Emaan Hariri, Daniel E. Ho — Stanford HAI / RegLab"
published: 2026-11-19
captured: 2026-11-20
relevance:
  social_science: high
  ai_engineering: high
verification: verified
rationale: >-
  Cross-domain high: for social_science, lens 7 (political science —
  institutions and governance) — a quantified, multi-state empirical
  measurement of AI-generated text reaching court filings, with a
  governance recommendation (disclosure policy). For ai_engineering, lens 4
  (evaluation, validation and deterministic guardrails) — a methodological
  result on why per-document AI-text detectors are unreliable and how to
  measure prevalence credibly instead.
---

# AI Might Be Flooding State Court Houses, but Proving It Is Another Matter

## Summary

Reports that AI-assisted text is spreading into US state court filings,
with documented fake-citation cases from lawyers, prosecutors, and judges,
and argues that commercial AI detectors are unreliable for legal writing:
results can shift substantially depending on detector settings, and
detection is useful for estimating overall prevalence, not for identifying
which individual filing used AI. Methodologically, the authors build
PhantomDocket, a benchmark pairing documented AI-hallucination cases from
Damien Charlotin's incident database with matched controls, to test
detectors, and ScoreMix, a calibration method that estimates the share of
filings resembling known-hallucinated writing rather than flagging
individual documents. Using complaints from county courts in four US
states, they report signs of AI-assisted drafting rising from near zero in
2022 to over a third of examined Santa Clara complaints in 2026 (38% in
Santa Clara, 36% in San Francisco non-debt-collection cases in 2026, versus
17% in Tulsa and 16% in Oklahoma county). Self-represented litigants in
Santa Clara rose from 19% (2024) to 72% (2026); attorney-filed complaints
rose from 5% to 34%. AI-like text appeared most in the statement of facts
and causes of action. For the same set of 2026 Santa Clara complaints, one
commercial detector flagged between 10% and 98% of filings as AI-written
depending only on its settings. Existing tools (Pangram, EditLens) either
failed to detect AI automatically or needed extensive tuning. Over 1,500
US cases have documented legal hallucinations. The authors recommend
better AI-assistance disclosure policies in courts for accountability and
measurement.

## Why it matters

For social scientists tracking AI's effects on institutions and
governance: a rare multi-jurisdiction, time-trending measurement of AI
use inside a formal legal institution, with a concrete governance lever
(disclosure policy) rather than only a warning. For AI-engineering
builders of detection or evaluation systems: direct evidence that a
commercial detector's output can swing from 10% to 98% flagged on an
identical document set purely from settings changes — a sharp,
quantified warning against treating any single-document AI-detector score
as ground truth — paired with a reusable alternative (benchmark against
documented-incident ground truth, then calibrate a prevalence estimate
rather than a per-document verdict).

## Verification notes

Stanford HAI page fetched directly (2026-11-20); authors, affiliations
(Stanford HAI / RegLab), and a 19 November 2026 publication date
confirmed. All quantified figures in the Summary (prevalence percentages
by county and year, the self-represented/attorney-filed share shift, the
10%-98% detector-setting range, the 1,500+ documented-case figure) are
traceable to the fetched page text. Full paper/dataset (PhantomDocket and
ScoreMix implementation detail) not read at capture. No independent
secondary corroboration attempted beyond the page's own citation of
Damien Charlotin's public hallucination-case database.

## Updates

None yet.

## Related entries

None yet.
