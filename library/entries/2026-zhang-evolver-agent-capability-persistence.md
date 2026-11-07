---
slug: 2026-zhang-evolver-agent-capability-persistence
title: "Evolver: Turning Agent Exploration into Evolving Capabilities"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07595
canonical_ids: ["arxiv:2611.07595"]
publisher_or_author: "Haoyang Zhang, Qumeng Sun, Xiao Zhang, Xiang Liu, Zhidong Fan, Junjie Wang"
published: 2026-11-05
captured: 2026-11-07
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on harness/context engineering (lens 2) and AI-assisted software
  development (lens 7): a named, harness-agnostic mechanism (structured
  "Gene" assets plus experience acquisition/retrieval/feedback-guided
  evolution) for persisting procedural knowledge across agent runs without
  retraining the model, tested on real harnesses (Claude Code, Codex) and
  standard benchmarks with quantified success-rate and token-cost deltas.
---

# Evolver: Turning Agent Exploration into Evolving Capabilities

## Summary

Coding agents generate useful procedural knowledge while exploring a task,
but it normally lives only in a short-lived execution trace and is lost
rather than reused on the next task. Evolver is a framework that converts
that exploration into persistent, reusable capabilities — called "Gene"
assets — without changing the underlying model's weights, and works on top
of existing agent harnesses rather than replacing them. It combines
experience acquisition, retrieval, and feedback-guided evolution of these
assets over time.

Tested with Claude Code and Codex across four benchmarks (Terminal-Bench 2.1,
SWE-bench Multilingual, SWE-rebench, GAIA): on 320 paired executions, task
success rose from 83.13% to 87.50% and measured token consumption fell by
24.24%; among the 265 pairs that succeeded under both conditions (with and
without Evolver), token use fell by 17.57%. The authors conclude persistent
procedural experience improves both effectiveness and efficiency, not just
one at the other's expense.

## Why it matters

Offers builders a harness-agnostic pattern for a problem most agent
deployments currently leave unsolved: letting an agent's own successful
problem-solving approaches compound across tasks and sessions, rather than
re-deriving them each time. The joint success-rate-and-token-cost
improvement, measured on two real production harnesses (not a research-only
scaffold), is the part other teams could try to replicate or adapt.

## Verification notes

Read directly from the arXiv abstract page (arxiv.org, allowlisted). All
claims above, including the quantified benchmark deltas, are stated in and
traced directly to the abstract; no load-bearing claim here depends on
information beyond it. The full paper (1,504 KB, 12 pages) was not
independently fetched. Single version (v1, 5 Nov 2026).

## Updates

None yet.

## Related entries

None yet.
