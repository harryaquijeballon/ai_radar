---
slug: 2026-sehgal-context-pipeline-not-window
title: "Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.36114
canonical_ids: ["arxiv:2610.36114"]
publisher_or_author: "Yuvraj Sehgal, Mahsa Panahandeh, Naser Ezzati-Jivan"
published: 2026-10-26
captured: 2026-10-28
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on harness and context engineering (lens 2) and observability
  (lens 5): names a five-stage pipeline model of context loss distinct
  from context-window size, quantifies the cost of unsafe truncation in a
  controlled experiment, and surveys seven agent frameworks finding two
  with the same unsafe behavior — a concrete check any agent builder
  could run against their own harness.
---

# Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses

## Summary

Argues that LLM agents are usually judged only by context-window size and
answer correctness, which misses how much tool output is lost before the
model ever sees it. In a tool-using agent diagnosing injected faults from
Linux kernel traces, the largest prompt used only about 5.75% of the
context window — yet about a third of tool results were truncated before
reaching the model, and every truncated result became invalid JSON. The
harness cut results at a fixed character length, removing data near the
end of each result; one field reached the model in only 4.7% of calls
while another field in the same results reached it in 99.3% of calls.
Which field carried the fault's evidence depended on when the faulty
process started in the trace, and the agent's diagnostic accuracy followed
the same pattern.

The paper models the agent's context as a five-stage pipeline with a
measured failure at each stage, replays 864 real tool results (including
one production trace where truncation removes all 128 records of the
fault's evidence), and runs a controlled experiment: the data loss first
shows up as extra work rather than wrong answers (43% more tool calls,
roughly double the computation, yield falling from 0.61 to 0.31), with the
agent still reaching the right answer when it has another route to the
data. A survey of seven agent frameworks finds two that truncate tool
output in the same unsafe way. The authors state that whether the data
loss truly causes the accuracy drop (versus correlating with it) remains
an open question (unverified: the causal claim, by the authors' own
framing).

## Why it matters

Gives agent builders a concrete, checkable failure mode distinct from
"not enough context window": fixed-length truncation of tool output can
silently destroy exactly the evidence a task needs, in a way that context-
window-size or raw-accuracy metrics won't surface. The five-stage pipeline
framing and the cross-framework survey (2 of 7 sharing the unsafe pattern)
give a template for auditing any existing harness's tool-output handling.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-28; single version,
submitted 26 Oct 2026, 18:25 UTC). The quantified figures (5.75% context
usage, ~33% truncated results, 4.7%/99.3% per-field delivery rates, 43%
more tool calls, yield 0.61→0.31, 864 replayed results, 128-record
production trace, 2-of-7 framework survey) all trace to the fetched
abstract text. The authors' own caveat that causality is unconfirmed is
preserved rather than treated as established. Full experimental detail and
framework-survey methodology were not independently reviewed beyond the
abstract.

## Updates

None yet.

## Related entries

None yet.
