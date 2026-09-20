---
slug: 2026-shea-roche-jev-agent-judge-evals
title: "Jev-as-a-Judge for Agent Evals"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://www.langchain.com/blog/jev-agent-evals-langsmith
canonical_ids: ["repo:danielgshea/jev-as-a-judge"]
publisher_or_author: "Daniel Shea, Seán Roche — LangChain blog"
published: 2026-09-20
captured: 2026-09-20
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Clears lens 4 (evaluation, validation and deterministic guardrails): a
  quantified head-to-head benchmark of a non-autoregressive "System One"
  evaluator against three LLM judges on accuracy, cost, and variance for
  agent-output judging, giving builders a concrete alternative when
  LLM-judge cost or inconsistency is prohibitive for research/policy-grade
  agent evaluation.
---

# Jev-as-a-Judge for Agent Evals

## Summary

LangChain benchmarked Jev, a "System One" model from TypeSafe AI, as a judge
for agent-output evaluation against three autoregressive LLM judges (GPT-5.6
Luna, GPT-5.6 Terra, and Claude Sonnet 4.6). Unlike LLM judges, which generate
a text verdict token-by-token, Jev "evaluates a state and returns typed
answers and probabilities" directly.

The experiment used a Deep Agents weather agent (using Tavily for current
conditions and forecasts), captured five fixed test scenarios in a LangSmith
dataset, and had each of the four evaluators score the same five agent
outputs 100 times each — isolating evaluator variation from agent variation.
Human reviewers labeled the five scenarios against a rubric to establish
ground-truth verdicts.

Reported results: Jev matched the human-labeled ground truth on all 500
evaluator decisions (5 scenarios × 100 replays), while Claude Sonnet 4.6
matched on 80%. Jev's quality-score variance across replays was reported as
92–913x lower than the three LLM judges'. Per-evaluation cost and latency
were reported as roughly $0.00035 and 0.44 seconds for Jev, against $28.17
per call for Claude Sonnet 4.6 — a difference independently corroborated in
direction (Jev dramatically cheaper and more consistent) by a third-party
write-up of the same benchmark, though that write-up quoted a different
intermediate cost figure for Jev ($0.34) than the source article's stated
per-call cost; the precise per-call cost multiple is therefore
"(unverified)" even though the qualitative finding is corroborated.

## Why it matters

For teams building agentic research or policy products that need
evaluation cheap and consistent enough to run at scale (e.g., regression
testing on every agent change, or scoring large batches of simulated policy
runs), an LLM-judge's cost and run-to-run variance can be prohibitive. This
gives a concrete, tested alternative — a typed, non-generative judge model —
plus a replicable benchmark design (fixed scenarios, human-labeled ground
truth, many replays per evaluator) that builders can reuse to test their own
candidate judges before adopting one.

## Verification notes

Read directly via the published article. Corroborated independently: a
Langfuse blog post ("Using TypeSafe's Jev for evals") and other secondary
write-ups described the same weather-agent/LangSmith benchmark structure and
the qualitative direction of the results (Jev far cheaper and lower-variance
than the LLM judges tested), but one secondary summary cited a different
Jev per-call cost figure than the source article itself — this discrepancy
is recorded above and the exact cost multiple is marked unverified pending
clarification. The underlying "System One" model and TypeSafe AI are a
third-party product being promoted here by a framework vendor (LangChain);
per `profiles/ai_engineering/sources.md`'s framework-vendor discount, this
is treated as a vendor-adjacent case study rather than independent research,
though the head-to-head design against named competitor judges gives it more
evidentiary weight than a plain feature announcement.

## Updates

None yet.

## Related entries

None yet.
