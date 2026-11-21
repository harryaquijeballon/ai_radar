---
slug: 2026-sreenivasa-held-while-waiting-agent-runtimes
title: "Held While Waiting: What LLM Agent Sessions Reserve on Serverless and Agent Runtimes"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.26480
canonical_ids: ["arxiv:2611.26480"]
publisher_or_author: "Mekhala Hithyshini Sreenivasa — arXiv preprint"
published: 2026-11-19
captured: 2026-11-21
relevance:
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 5 (observability and debugging — cost and latency
  monitoring): a measured, mechanism-level explanation of why agent
  runtimes run out of capacity well before they run out of compute, with a
  quantified fix (environment sharing) and a named open problem for
  platform designers.
---

# Held While Waiting: What LLM Agent Sessions Reserve on Serverless and Agent Runtimes

## Summary

Measures that LLM agents spend most of their time waiting on the model: on
Amazon Bedrock AgentCore, a median 2.7-second wait per reply against an
estimated 5-40 milliseconds of actual computation. The platform does not
charge for CPU during that wait, but it reserves a separate virtual
machine per conversation until the conversation is explicitly closed, so
the system can run out of environments long before it runs out of
processing power. Two causes compound this: environments stay reserved
after a conversation functionally ends (in a customer-service benchmark,
conversations averaged 33 seconds of activity but held their environment
about 15 minutes longer unless the client closed it), and each environment
serves only one conversation despite being mostly idle. A simulation
sharing one environment across 64 conversations needed 59x fewer
environments while delaying at most 40 milliseconds on 99 of 100 replies.
The paper also flags a measurement pitfall: three common ways of
estimating per-step compute time (a stubbed model, a timer wrapped around
the model call, running steps back-to-back) each produced plausible but
too-low estimates. Closing idle environments needs only client-side
changes; sharing them needs platform support, which among surveyed agent
runtimes only one offers, and only partially — because runtimes isolate
conversations by design, since agents run model-chosen tools and sometimes
execute code.

## Why it matters

For anyone operating LLM agents on serverless or dedicated-environment
runtimes: a reusable framing for a cost/capacity failure mode that is easy
to miss (environment-per-conversation reservation, not raw compute, is
usually the real bottleneck), a correct way to measure per-step agent
compute time, and a concrete lever (closing idle environments client-side)
that needs no platform change.

## Verification notes

arXiv abstract page fetched 2026-11-21 (paraphrased summary; full abstract
text not reproduced verbatim due to tool quoting limits). Submission
history shows v1 submitted Thu, 19 Nov 2026, 17:40:09 UTC — within this
run's discovery window (2026-11-20 → 2026-11-21) and the 7-day eligibility
cap. Category: cs.PF (Performance). Figures (2.7s median wait, 5-40ms
compute estimate, 33s/~15min conversation-vs-reservation gap, 59x
environment reduction, 99/100 within 40ms) were confirmed on a second,
independent fetch requesting exact quoted figures, which matched the first
pass exactly. Single-author arXiv preprint; no independent secondary
(non-arXiv) corroboration found this run.

## Updates

None yet.

## Related entries

None yet.
