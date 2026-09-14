---
slug: 2026-gieng-ai-adoption-selection-effect
title: "Your AI Adoption Lift Is a Selection Effect"
status: accepted
domains: [social_science]
source_type: commentary
source_url: https://towardsdatascience.com/your-ai-adoption-lift-is-a-selection-effect/
canonical_ids: []
publisher_or_author: "William Gieng — Towards Data Science"
published: 2026-09-13
captured: 2026-09-14
relevance:
  social_science: high
  ai_engineering: n/a
verification: verified
rationale: >-
  A concrete, reusable causal-inference pattern (fuzzy regression discontinuity
  on an arbitrary rollout eligibility threshold) for the specific and common
  problem of AI feature-adoption comparisons being confounded by self-selection
  into use — directly usable applied-methods content for lens 5.
---

# Your AI Adoption Lift Is a Selection Effect

## Summary
The piece argues that comparing outcomes (e.g., retention) between adopters and
non-adopters of an opt-in AI feature overstates the feature's causal effect,
because adoption itself is correlated with organizational or customer
readiness rather than randomly assigned. Using a synthetic dataset built to
illustrate the problem, the author shows a naive adopter-vs-non-adopter gap of
+15.4 percentage points against a "true" simulated effect of +4 percentage
points. The proposed fix is a fuzzy regression-discontinuity (RD) design that
exploits an arbitrary, customer-unchosen rollout eligibility threshold (e.g. a
25-seat minimum) as an instrument: a reduced-form RD estimate of +1.8pp (95%
CI: −0.9 to +4.5) and a 2SLS estimate of +4.9pp (95% CI: −2.4 to +12.1) are
reported on the synthetic data. Python code, the synthetic data-generating
process, and diagnostic checks are provided in an accompanying notebook for
reproducibility.

## Why it matters
For researchers or analysts evaluating claims about an AI feature's effect
(on retention, productivity, or other outcomes) where adoption was not
randomized, this is a directly applicable identification strategy: look for
an eligibility threshold or rollout rule the unit did not choose, and use it
as an RD instrument rather than trying to model the selection process
directly. It is a specific, actionable answer to a measurement problem that
recurs across many "AI adoption raised X" claims — including the kind
reported elsewhere in this library's own entries on organizational AI
adoption.

## Verification notes
Source (towardsdatascience.com) fetched directly and read in full. All
summarized claims — the argument, the RD method, and the quantified synthetic
estimates — are stated explicitly in the article itself; the demonstration is
self-contained (author's own synthetic data and code, not an external
empirical claim requiring independent corroboration). No load-bearing claim
depends on an outside source.

## Updates
None yet.

## Related entries
None yet.
