---
slug: 2026-cuadron-gupta-boba-coding-agent-chains
title: "Built on Broken Assumptions (BOBA): Why Coding Agents Cannot Be Left Alone"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.02207
canonical_ids: ["arxiv:2611.02207"]
publisher_or_author: "Alejandro Cuadron, Arpit Gupta"
published: 2026-11-01
captured: 2026-11-03
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation/deterministic guardrails (lens 4) and
  AI-assisted software development (lens 7) — the core standing lens for
  multi-step agent systems whose outputs must be validated: a new
  280-chain, 140-repository benchmark showing ten coding agents complete
  far fewer multi-request chains than isolated requests, with the cause
  (self-certified passing tests that miss errors) and a measured fix.
---

# Built on Broken Assumptions (BOBA): Why Coding Agents Cannot Be Left Alone

## Summary

Coding agents report a request complete once the agent's own tests pass,
and real usage often chains requests where each builds on the last — yet
most benchmarks test one isolated request at a time against human-written
code, checked once. The authors built BOBA-Bench: 280 chains of 20
consecutive requests drawn from 140 real open-source projects, and
evaluated ten coding agents on both isolated requests and full chains. All
ten performed far worse on chains: about 95% completion for isolated
requests versus 51% for chains. The cause is not code quality — once
checked, agent-written code is nearly as good a foundation as
human-written code — but missed mistakes: agents declare a request done
once their own tests pass even when those tests overlook an error, and the
next request in the chain then builds on the broken code and fails about
twice as often. Agents rarely catch these mistakes later, scoring only
about 53% accuracy when asked whether an implementation is correct. A
single external signal that the code is wrong, followed by one repair
round, raised chain completion from 51% to 59% and stopped the repaired
mistake from hurting later requests (as stated in the fetched abstract;
full per-agent results and chain construction method not reviewed at
capture).

## Why it matters

A foundational, quantified reliability finding for anyone running coding
agents across multi-step, dependent tasks rather than one request at a
time: near-95% isolated-task completion rates do not predict chain
performance, and the gap is driven specifically by agents trusting their
own (incomplete) tests rather than by worse code. The paper's own fix — one
external verification signal plus a repair round — is a concrete,
measured mitigation (51%→59% chain completion) directly transferable to
any agentic coding pipeline that currently relies on the agent's
self-reported "done."

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 1 Nov 2026, no revisions). The BOBA-Bench design (280 chains, 20
requests each, 140 projects), the 95%-vs-51% completion gap, the
code-quality-is-not-the-cause finding, the ~53% self-correctness-detection
accuracy, and the 51%→59% external-signal-plus-repair result all trace to
the fetched abstract text, which is the paper's own stated summary of its
results — treated as `verified` on this library's convention for
single-source arXiv preprints whose headline figures are self-reported
empirical findings. The full paper (per-agent breakdowns, chain
construction methodology) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
