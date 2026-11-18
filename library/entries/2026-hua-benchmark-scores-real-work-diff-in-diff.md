---
slug: 2026-hua-benchmark-scores-real-work-diff-in-diff
title: "Higher-Scoring Coding Models Did Not Get More Work Done"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.23216
canonical_ids: ["arxiv:2611.23216"]
publisher_or_author: "Yining Hua"
published: 2026-11-17
captured: 2026-11-18
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation and validation) and lens 7 (AI-assisted
  software development): a difference-in-differences natural experiment,
  using a real model-access shock, that directly tests whether coding-model
  benchmark scores predict real merged-work output — a measured, transferable
  result, not opinion.
---

# Higher-Scoring Coding Models Did Not Get More Work Done

## Summary

The paper tests whether coding models that score higher on benchmarks
(specifically SWE-Bench Pro) produce more completed real-world work. It
treats a 12 June 2026 US export-control directive — which cut off access to
Claude Fable 5 for 19 days — as a natural experiment: users who had been
using Fable 5 were forced onto other models, predominantly Opus 4.8, which
scores lower on SWE-Bench Pro. Using difference-in-differences with
developer and date fixed effects, the author compares 297 GitHub developers
who lost Fable 5 access against 8,908 developers who stayed on Opus 4.8
throughout, tracking pull-request outcomes before, during, and after the
suspension. The effect of regaining access to the higher-scoring model on
the 7-day PR merge rate was +1.4 percentage points (95% CI: -1.4 to +4.3) —
not statistically significant. A second analysis repeats the design across
five separate 2026 model upgrades (1,208 developers, 15,442 pull requests):
the weighted mean effect was -0.9 points (CI: -1.9 to +0.2), with all five
individual estimates negative and all five confidence intervals including
zero. Merged PRs per week rose a non-significant 2.4% (CI: -4.9% to +10.2%).
The author concludes that, in this setting, higher benchmark scores did not
translate into a measurable increase in merged real-world work.

## Why it matters

Gives anyone choosing a coding model for a team, or justifying a model
upgrade on benchmark grounds, a concrete causal (not merely correlational)
counter-example: a quasi-experimental design found no detectable real-work
payoff from switching to a higher-SWE-Bench-Pro-scoring model, across both a
policy-driven access shock and five separate model upgrades. It is a direct,
quantitative complement to Epoch AI's qualitative finding the same week that
benchmark rank and real-work quality can diverge ([How good are Fable 5.2
and GPT-6.2 Astra at real work?](2026-epoch-fable-gpt-astra-real-work.md)) —
together they argue that teams should validate on their own real-work
metrics (merge rate, throughput) before trusting a benchmark-driven model
switch to pay off.

## Verification notes

Fetched the arXiv abstract page directly (arxiv.org, on the egress
allowlist). All claims — the natural-experiment design, sample sizes, point
estimates, and confidence intervals — are traced to the abstract text as
summarized by the fetch. The underlying regression tables and robustness
checks in the full paper were not independently re-derived; the reported
confidence intervals (all crossing zero) are taken as stated.

## Updates

None yet.

## Related entries

- [How good are Fable 5.2 and GPT-6.2 Astra at real work?](2026-epoch-fable-gpt-astra-real-work.md) — same-week, independent evidence of a capability/real-work gap.
