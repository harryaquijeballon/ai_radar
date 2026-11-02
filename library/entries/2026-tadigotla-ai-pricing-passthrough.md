---
slug: 2026-tadigotla-ai-pricing-passthrough
title: "When AI Gets Cheaper, Do Prices Follow? Information Delays and Algorithmic Pricing"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2610.31693
canonical_ids: ["arxiv:2610.31693"]
publisher_or_author: "Krish Tadigotla"
published: 2026-10-20
captured: 2026-11-02
relevance:
  social_science: high
  ai_engineering: n/a
verification: verified
rationale: >-
  High on competition, regulation and public policy (lens 4): a quantified
  simulation of whether AI-driven cost reductions pass through to consumer
  prices under algorithmic pricing, directly usable in arguments about
  whether AI cost savings reach consumers or are retained as higher margins
  under algorithmic competition. First reviewed by a prior run and logged in
  rejections.md on 2026-10-26 for a submission/listing date gap; re-reviewed
  on its merits per the revised ENGINE.md P6.1 rule that a date-only
  rejection is not a dedup match, and the 2026-10-26 econ.GN listing date is
  within this run's 7-day eligibility cap.
---

# When AI Gets Cheaper, Do Prices Follow? Information Delays and Algorithmic Pricing

## Summary

Asks whether lower costs for running AI models translate into lower
consumer prices, and whether delays in observing rivals' prices or limits
on repricing frequency change the consumer-welfare outcome. Uses a
simulated market with two differentiated sellers, logit demand, and
tabular Q-learning agents, varying information delay, repricing frequency,
cost shocks, and firm asymmetry across 960 training runs (16 conditions,
60 paired seeds each). The paper reports that the interaction between
information delay and repricing frequency has no detectable effect on
consumer surplus. Under the shortest delay and repricing every period —
the condition most favorable to consumers — price cuts equal only 55.6%
and 44.0% of the underlying cost reduction for the two firms. Consumer
surplus under the learned pricing policies falls below the static
grid-Nash benchmark in all 16 conditions tested. The author is explicit
that the results do not establish real-world collusion or describe actual
AI providers' pricing (all figures and framing as stated in the fetched
abstract; full simulation code and robustness appendix not reviewed at
capture).

## Why it matters

A concrete, quantified counter to the assumption that AI's falling compute
costs automatically flow through to consumers: in this simulation, under
every tested combination of information delay and repricing frequency,
algorithmic sellers capture a majority of the cost saving as margin rather
than passing it through, and consumer surplus never reaches the
competitive (static Nash) benchmark. Directly usable by anyone arguing a
competition-policy or antitrust question about AI-era algorithmic pricing:
it gives a specific, citable pass-through range (44-56%) and a stated
null result on whether faster information or repricing closes the gap,
rather than a qualitative worry about "algorithmic collusion."

## Verification notes

Read via the arXiv abstract page (captured 2026-11-02; single version,
submitted 20 Oct 2026, no revisions). The simulation design (two sellers,
logit demand, tabular Q-learning, 960 runs across 16 conditions), the
55.6%/44.0% pass-through figures, the "no detectable effect" finding for
the delay-by-repricing interaction, and the below-Nash consumer-surplus
result in all 16 conditions all trace to the fetched abstract text, which
is the paper's own stated summary of its results — treated as `verified`
on the convention applied elsewhere in this library to single-source
arXiv preprints whose headline figures are self-reported simulation
output rather than claims requiring third-party corroboration. The full
paper (simulation code, parameter grid, robustness checks) was not
reviewed at capture.

Dedup note: this candidate first surfaced on 2026-10-26 and was logged to
`rejections.md` that day with "not a new development... late cross-post"
reasoning based on a submission-to-listing gap. `engine/ENGINE.md` P6.1
(revised 2026-10-26) states that a rejection-log line whose only reason
was the date is not a dedup match for discovery, and that the candidate
should be reviewed on its merits; the 2026-10-26 econ.GN listing date is
within this run's 7-day eligibility window (cap: 2026-10-26). The original
rejection-log line is left unedited per the append-only rule; this entry
is the merits-based review the revised rule calls for.

## Updates

None yet.

## Related entries

None yet.
