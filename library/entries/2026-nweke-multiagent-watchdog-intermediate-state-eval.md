---
slug: 2026-nweke-multiagent-watchdog-intermediate-state-eval
title: "Why Most Multi-Agent Systems Fail Even When Evaluation Passes"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/why-most-multi-agent-systems-fail-even-when-evaluation-passes/
canonical_ids: []
publisher_or_author: "Benjamin Nweke — Towards Data Science"
published: 2026-09-07
captured: 2026-09-08
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails): names
  a concrete "Intermediate State Eval" / watchdog architecture — checkpoint
  verifiers at agent-to-agent handoffs that reject implausible-but-well-formed
  payloads before they propagate — with runnable Pydantic/Python code and
  stated tradeoffs, directly usable for hardening multi-step agent pipelines
  used in research/policy products.
---

# Why Most Multi-Agent Systems Fail Even When Evaluation Passes

## Summary
Nweke argues that end-to-end evaluation of multi-agent pipelines is
structurally blind to a common failure mode: an intermediate agent hands off
a payload that is well-formed (valid JSON, schema-compliant) but semantically
wrong — corrupted, empty, or implausible — and this passes silently through
downstream agents because "grading only the compiled output makes you
structurally blind to intermediate states that look correct but aren't." He
proposes an "Intermediate State Eval" architecture: lightweight watchdog
checks placed at each agent-to-agent handoff boundary, using a small local
model to ask narrow plausibility questions about the payload (e.g., "does
this look like a real order confirmation?") and raising an exception to halt
the pipeline when a handoff looks implausible, rather than letting it
propagate. The article gives a working Python implementation using Pydantic
models to define expected payload shape, a grading function that calls a
small local model to judge plausibility, and orchestration logic that stops
execution on a failed check. Nweke motivates the problem with a statistic
attributed to "Datadog's 2026 State of AI Engineering report": approximately
5% of production AI requests fail, of which roughly 40% surface as loud
errors and 60% are requests that "complete and still get it wrong"
(unverified — see Verification notes). He also names three explicit costs of
the pattern: added latency from extra inference calls per handoff, false
rejections from a miscalibrated watchdog, and the judgment call of which
handoffs are worth monitoring.

## Why it matters
Gives builders of multi-step agent pipelines (including agentic research or
policy-simulation products, where a silently-corrupted intermediate result
could poison a downstream conclusion) a concrete, code-level pattern for
catching "confidently wrong" handoffs that current end-to-end evals miss —
directly actionable for the deterministic-guardrail and validation lenses
this profile prioritizes, without requiring a full redesign of the
evaluation harness.

## Verification notes
Fetched directly from towardsdatascience.com (allowlisted). The core
technical claims — the failure-mode argument, the Intermediate State Eval /
watchdog design, the Pydantic-based code pattern, and the three stated
tradeoffs — are the author's own description of his proposed architecture
and are traceable directly to the article's text. The motivating statistic
("~5% failure rate, ~40%/60% loud-vs-silent split," attributed to Datadog's
2026 State of AI Engineering report) is marked **(unverified)**: an
independent search for that report surfaced a different breakdown (~5% of
LLM call spans erroring, with the cited article there attributing roughly
60% of *those* errors to rate-limit/capacity exhaustion, not to
silently-wrong-but-complete responses). This may reflect a different section
or data cut of the same report, but it was not confirmed this run, so the
statistic is not corroborated and verification is recorded as partial rather
than verified.

## Updates
None yet.

## Related entries
None yet.
