---
slug: 2026-chen-zheng-zhu-self-prediction-vs-recommenders
title: "You Know What You Will Like: People Predict Their Own Ratings Better Than Recommender Systems"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2611.06696
canonical_ids: ["arxiv:2611.06696"]
publisher_or_author: "Zihan Chen, Lei Nico Zheng, Di Zhu"
published: 2026-11-04
captured: 2026-11-08
relevance:
  social_science: medium
  ai_engineering: n/a
verification: verified
rationale: >-
  Medium on lens 3 (digital technologies/platform economics): a quantified
  field comparison of self-predicted preferences against recommender-system
  predictions, with design principles for preference elicitation — on-lens
  but a specific platform-design result rather than broader AI/digital
  policy relevance.
---

# You Know What You Will Like: People Predict Their Own Ratings Better Than Recommender Systems

## Summary

Compares how accurately people predict their own future ratings against
four recommender-system benchmarks (MovieLens's own predicted rating, two
collaborative-filtering models, and a stacked model trained on other
members' outcomes), using the MovieLens Beliefs dataset (2023–2024): 551
follow-up-rated expectations from 277 members, out of 26,020 expectations
solicited (98.8% of prompts went unanswered). People predicted their own
ratings more accurately than all four benchmarks (correlation 0.69 versus
0.34 for MovieLens's own prediction and 0.54–0.59 for the trained
recommenders). Adding a person's self-expectation to machine forecasts
reduced out-of-sample mean squared error by 26%, a gain that held when
models were trained on earlier expectations and tested on later ones. A
person's expectations about other movies did not substitute for their
expectation about the movie in question. On old, heavily rated movies, the
trained recommenders matched or beat the person. The authors derive four
design principles for preference elicitation and recommender evaluation from
these results.

## Why it matters

A concrete empirical limit on how much recommender systems can learn from
behavioral data alone, and a case for when directly asking users is worth
the (high) non-response cost — relevant background for anyone evaluating
platform/recommender design or the economics of algorithmic personalization
(lens 3), though the result is specific to one domain (movie ratings) and
not AI-policy-facing.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 4 Nov 2026, no revisions). The sample sizes (551 of 26,020
expectations, 277 members, 98.8% non-response), the correlation figures
(0.69 vs. 0.34 and 0.54–0.59), and the 26% MSE reduction all trace to the
fetched abstract text — treated as `verified` per this library's standing
convention for single-source arXiv preprints whose headline claims are
self-reported. The full paper (the four design principles themselves, exact
benchmark model specifications) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
