---
slug: 2026-afonso-proofcoder-continuous-reasoning
title: "ProofCoder: Continuous Reasoning for Automated Software Verification"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.14106
canonical_ids: ["arxiv:2611.14106"]
publisher_or_author: "Martim Afonso, Inês Lynce, Maurizio Morisio, João F. Ferreira — arXiv preprint (cs.SE)"
published: 2026-11-10
captured: 2026-11-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on reliable research/policy products and evaluation (lens 8, with
  lens 4): a quantified improvement on formally verified proof synthesis
  — directly relevant to this profile's standing interest in techniques
  that make agent output trustworthy enough for research/policy use, since
  formal verification is the strongest available guarantee of
  correctness.
---

# ProofCoder: Continuous Reasoning for Automated Software Verification

## Summary

ProofCoder is an agentic system for synthesizing formal proofs in the Rocq
proof assistant. Rather than generating tactics inside a fixed loop
controlled by the surrounding harness, it reasons continuously during
proof search, using proof-assistant feedback to decide when to gather more
information, inspect proof states, revise proof fragments, or backtrack,
and can work at either tactic-level or whole-proof granularity. On 280
verification tasks from the AutoRocq Benchmark, ProofCoder raised proof
success from 47% to 60% over the prior state-of-the-art AutoRocq system —
a 27.7% relative improvement — at roughly half the cost in its
best-performing configurations. Without continuous reasoning, the agent
solved fewer lemmas at substantially higher cost, backtracked 4–6 times
more often, and discarded its own revisions more often. Whole-proof and
tactic-level generation reached similar success rates via different search
and repair strategies, supporting the authors' claim that continuous
reasoning and feedback-guided revision matter more than better tactic
selection alone.

## Why it matters

Formal verification is the clearest available guarantee that an AI
agent's output is actually correct, which makes a 27.7% relative
improvement in proof success at roughly half the cost a meaningful
advance for any system that needs that guarantee — including the kind of
simulation or research-pipeline harness this profile's policy-simulation
interest cares about. The architectural lesson (continuous reasoning
against assistant feedback beats tactic-selection improvements alone, and
reduces costly backtracking) is transferable beyond proof assistants to
any agent verifying its own output against a formal, feedback-giving
checker.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.14106,
2026-11-12); title, authors, submission date (10 Nov 2026), and category
(cs.SE) confirmed there. The method description and all quantified
figures (47%→60% success, 27.7% relative improvement, ~half cost,
4–6x more backtracking without continuous reasoning) trace directly to the
fetched abstract text. Full paper (AutoRocq Benchmark details, per-task
breakdowns) not read at capture — upgrade path noted.

## Updates

None yet.

## Related entries

None yet.
