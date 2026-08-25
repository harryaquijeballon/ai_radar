---
slug: 2026-bouchekir-agentguardutil-nl-policy-verification
title: "From Natural Language Policies to Executable Obligations: A Verification Harness for Dependable In-Car LLM Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.23282
canonical_ids: ["arxiv:2608.23282"]
publisher_or_author: "Radouane Bouchekir, Damir Safin, Tomas Bueno Momcilovic — arXiv preprint"
published: 2026-08-24
captured: 2026-08-25
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation and deterministic guardrails (lens 4): a
  named, concrete mechanism — a runtime policy compiler that turns
  natural-language policy text into typed, machine-checkable rules, plus a
  deterministic engine with 25 validation gates and an LLM-based reviewer —
  for exactly the problem of making a stochastic agent's behavior
  provably compliant with a written policy. Directly transferable beyond
  the in-car setting to any agent that must obey a natural-language policy.
---

# From Natural Language Policies to Executable Obligations: A Verification Harness for Dependable In-Car LLM Agents

## Summary

Introduces AgentGuardUtil, a verification harness for LLM agents that must
comply with natural-language policies (demonstrated in an in-car agent
setting). Its core idea is a "runtime policy compiler: the natural-language
policy shipped with each conversation is compiled, once per policy, into
typed machine-checkable rules." A deterministic engine then interprets
these compiled rules against real tool outputs and simulated system
states, producing specific remedial actions rather than generic guidance
when a violation is detected. The system runs a "verify-and-revise loop"
in which the LLM acts as a proposer subject to this validation layer. The
implementation includes 25 deterministic validation gates (covering
identifier verification, data-schema validation, sequential-action
requirements, and protocol confirmations) complemented by an LLM-based
reviewer, forming a tiered evaluation framework that drives iterative
refinement optimized for pass-rate metrics.

## Why it matters

A concrete architecture pattern for the recurring problem of making an LLM
agent obey a natural-language policy reliably: compile the policy once
into machine-checkable rules rather than re-interpreting it with the LLM on
every turn, then gate agent actions through a deterministic engine that
returns specific remedial actions on violation. This is directly
applicable to any research or policy-product agent that must demonstrably
follow written rules (data handling, disclosure, escalation policies) — the
"compile once, check deterministically" pattern generalizes well beyond
the in-car domain used to demonstrate it.

## Verification notes

Fetched directly from the arXiv abstract page (2026-08-25); title, authors,
and submission date (24 Aug 2026) confirmed. The runtime-policy-compiler
description, the verify-and-revise loop, the 25 deterministic validation
gates, and the tiered evaluation framework all trace directly to the
fetched abstract text — the authors' own description of their system, not
a secondary paraphrase. Full paper (gate-by-gate detail, quantified pass
rates) not read at capture; upgrade path: read the full PDF for the
evaluation results.

## Updates

None yet.

## Related entries

None yet.
