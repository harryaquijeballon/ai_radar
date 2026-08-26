---
slug: 2026-marin-hallucination-watermark-conflict
title: "Hallucinations, Watermarks, Removers, and a Squeezed Balloon"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/hallucinations-watermarks-removers-and-a-squeezed-balloon
canonical_ids: []
publisher_or_author: "Javier Marín Valenzuela — Towards Data Science"
published: 2026-08-25
captured: 2026-08-26
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  A concrete, actionable warning for the deterministic-guardrails lens
  (lens 4/6): two commonly deployed AI-safety mechanisms (watermarking,
  uncertainty-based hallucination detection) actively undermine each
  other, with cited quantified evasion rates.
---

# Hallucinations, Watermarks, Removers, and a Squeezed Balloon

## Summary

The article argues that watermarking (proving text was AI-generated, e.g.
Google's SynthID or Kirchenbauer et al.'s method) and uncertainty-based
hallucination detection (e.g. semantic entropy, SelfCheckGPT) work against
each other inside the same model. Watermarking works by biasing token
choice at high-entropy positions where several continuations are
semantically equivalent — "a watermark can only push where there is room
to push." Hallucination detectors that sample a model multiple times and
measure how much the answers vary are undermined by this: a watermark
using a fixed secret key makes resampled outputs converge, so the detector
"overestimate[s] agreement and underestimate[s] uncertainty" — i.e., a
watermarked model can look more confident, and therefore more trustworthy,
than an unwatermarked one on the very claims it is more likely to be wrong
about. The piece is a synthesis of existing research, not a new
experiment; it cites, without independently re-deriving: watermark
stealing achieving over 80% evasion for under $50 in API queries (2024),
"WASH" (2026) achieving 99% evasion by averaging outputs across multiple
models, a mathematical impossibility result that watermarks cannot survive
systematic rewriting, and a roughly 1-in-10-trillion false-positive rate
for detecting a watermark once present.

## Why it matters

For anyone deploying both a watermarking scheme and an uncertainty-based
hallucination or reliability check on the same model output — a
combination that looks like defense in depth — this is a concrete warning
that the two can cancel each other's diagnostic value rather than add up,
and a citation trail (with quantified evasion rates) for evaluating
whether a given watermarking scheme is even worth the trade-off before
adding it to a pipeline that also needs uncertainty-based validation.

## Verification notes

Fetched and read directly from towardsdatascience.com; the argument and
its own framing ("a watermark can only push where there is room to push";
"overestimate agreement and underestimate uncertainty") are traced
verbatim to the source. The cited quantified results (watermark-stealing
evasion rate, WASH's 99% evasion, the impossibility proof, the
false-positive rate) are attributed to external sources within the post
but were not independently re-verified against the original papers this
run — verification is partial on those specific figures, verified on the
article's own argument and quotes.

## Updates

None yet.

## Related entries

None yet.
