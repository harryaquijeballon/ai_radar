---
slug: 2026-li-gao-misinformation-x-algorithm
title: "Why Does Misinformation Propagate Faster? An Algorithmic Perspective on X"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2609.28947
canonical_ids: ["arxiv:2609.28947"]
publisher_or_author: "Pan Li, Shuang Gao — arXiv preprint (econ.GN)"
published: 2026-09-24
captured: 2026-09-25
relevance:
  social_science: high
  ai_engineering: n/a
verification: verified
rationale: >-
  High on lens 7 (political science — AI/digital effects on political
  behavior via platform algorithms): names a specific amplification
  mechanism behind misinformation's speed advantage on X and tests a
  concrete, falsifiable fix, giving platform-regulation debates a target
  more precise than a generic "the algorithm favors misinformation" claim.
---

# Why Does Misinformation Propagate Faster? An Algorithmic Perspective on X

## Summary

The authors reverse-engineer why misinformation spreads faster than
corrections on X (formerly Twitter) by reimplementing the platform's
recommendation algorithm and testing it against the USC 2024 election
dataset. Their central finding is "engagement fungibility": the ranking
algorithm amplifies content based on predicted *instant* reactions (likes,
retweets) regardless of whether it also predicts *thoughtful* engagement
(replies, quotes) — so low-credibility content that reliably triggers quick
reactions is amplified on the same terms as content that generates
deliberation. The authors ran 46 robustness checks varying scoring
approaches and found that simply reweighting existing engagement metrics is
ineffective or counterproductive at closing the credibility-exposure gap.
They instead propose a "reflective-threshold gate" — requiring a minimum
predicted level of thoughtful engagement before a post can be amplified —
and show via reimplementation and simulation that it redirects visibility
away from low-credibility content while preserving mainstream reach and
overall engagement levels (unverified: the precise magnitude of the
credibility-gap reduction from the gate was not extracted from the fetched
abstract).

## Why it matters

Most misinformation-and-platforms commentary treats "the algorithm" as a
black box that simply favors outrage. This paper instead locates the
mechanism (fungibility between instant and thoughtful engagement signals)
and tests an intervention against it using the platform's own reimplemented
ranking logic on real election data — giving competition/regulation
analysts (lens 4) and political-science researchers (lens 7) a specific,
falsifiable lever (a thoughtful-engagement gate) to evaluate rather than a
generic transparency or demotion proposal.

## Verification notes

Fetched directly from the arXiv abstract page (2609.28947; v1 submitted
Thursday, 24 September 2026, 02:53:16 UTC — within this run's discovery
window). The engagement-fungibility mechanism, the 46-robustness-check
claim, the USC 2024 election dataset reimplementation, and the
reflective-threshold-gate proposal trace directly to the abstract's own
text. The gate's exact quantified effect on the credibility-exposure gap
was not stated in the extracted abstract text and is flagged unverified
above; full paper not read at capture.

## Updates

None yet.

## Related entries

None yet.
