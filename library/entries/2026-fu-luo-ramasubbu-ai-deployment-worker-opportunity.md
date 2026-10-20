---
slug: 2026-fu-luo-ramasubbu-ai-deployment-worker-opportunity
title: "When Better Opportunities Backfire: Service Worker Responses to Parallel AI Deployment in Customer Acquisition"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2610.25603
canonical_ids: ["arxiv:2610.25603"]
publisher_or_author: "Xinyu Fu, Shulong Luo, Narayan Ramasubbu, Peng Shen, Xincheng Wang, Yucheng Wang"
published: 2026-10-20
captured: 2026-10-20
relevance:
  social_science: high
  ai_engineering: n/a
verification: partial
rationale: >-
  Quantified causal evidence (regression-discontinuity-in-time design,
  500,000+ outreach records) on how parallel AI deployment changes human
  workers' effort allocation and output — a measurable, counter-intuitive
  productivity-measurement result (lens 1: economic growth and productivity).
---

# When Better Opportunities Backfire: Service Worker Responses to Parallel AI Deployment in Customer Acquisition

## Summary

The paper studies a Chinese online health-insurance brokerage where an AI
voice agent was deployed to handle low-intent sales leads, leaving high-intent
leads for human workers. Using sequential search theory, the authors
hypothesize that receiving better leads raises a worker's reservation value
and makes them less willing to persist with the lead currently in hand
(unverified mechanism — a theoretical prediction tested empirically below).
Drawing on more than 500,000 customer-outreach records spanning the AI
rollout, they use a regression-discontinuity-in-time design to track how
worker behavior changes across the workday, plus a calibrated decomposition
to weigh the channels involved.

Headline findings: the share of high-intent leads reaching human workers rose
about 23 percentage points on workers' first three calls of the day, fading
to zero later in the day. Over the same first three calls, human-worker
customer acquisition fell about 5 percentage points. Workers reallocated
(dropped or deprioritized) their earliest leads about 8 percentage points
more often and shortened those calls by about 13%. The decomposition finds
the gain from better lead ordering was modest and was outweighed by a larger
negative behavioral response. The authors frame "opportunity distribution" —
how good the next available option looks — as a service-operations state
variable distinct from workload or congestion.

## Why it matters

This is a directly usable productivity-measurement result for anyone modeling
how parallel AI deployment affects human-worker output in service settings:
it shows that an AI system which improves the *average* quality of leads
reaching humans can still reduce human output, because workers respond
behaviorally to the change in their own opportunity set, not just to the
leads themselves. That is a concrete mechanism (and a causal design for
detecting it) that applies wherever AI and humans are deployed in parallel to
share a task queue — a common pattern in real AI-adoption settings this
profile tracks under lenses 1 and 2.

## Verification notes

Read via the arXiv abstract page; the abstract itself gives method (RD-in-time
design, calibrated decomposition), sample size, and the quantified headline
effects summarized above, all of which are traceable to that text. The
underlying mechanism (reservation-value theory) is the authors' stated
hypothesis, not independently re-derived here. The full paper (data, exact
specification, robustness checks) was not fetched, so corroboration of the
load-bearing percentage-point figures against the primary results tables was
not attempted — hence `verification: partial` rather than `verified`.

## Updates

None yet.

## Related entries

None yet.
