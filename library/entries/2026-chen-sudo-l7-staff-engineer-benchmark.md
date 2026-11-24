---
slug: 2026-chen-sudo-l7-staff-engineer-benchmark
title: "sudo L7: Can Coding Agents Act Like Staff Engineers?"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.30517
canonical_ids: ["arxiv:2611.30517"]
publisher_or_author: "Edwin Chen et al."
published: 2026-11-24
captured: 2026-11-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Lens 4 (evaluation, validation and deterministic guardrails): a
  staff-engineer-authored benchmark targeting known frontier-model failure
  cases, graded by an agentic, rubric-based process validated against
  human labels at human-level agreement — a rare eval design that measures
  professional judgment (truthful reporting, hazard-flagging) rather than
  only functional correctness.
---

# sudo L7: Can Coding Agents Act Like Staff Engineers?

## Summary

Chen et al. introduce sudo L7, a benchmark of 60 software-engineering tasks written by staff-level engineers, mostly drawn from private production codebases, each centered on a place where a frontier model had previously failed. Each task pairs an underspecified request with a hidden, expert-written rubric of 1,287 atomic criteria across eight behavioral dimensions, from functional correctness to truthful reporting. An agentic grader reviews the agent's full transcript, inspects and runs its code, and treats test output as evidence rather than as the agent's self-report; an attempt passes only if it meets every criterion at the two highest severities, and more than half of those gating criteria assess things beyond functional correctness.

On the November 2026 public leaderboard (19 models, three attempts per task), Claude Fable 5.2 passes 52.2% of attempts — the highest result — while most other models pass at most 18.9%. In a human-label study, three model graders each agreed with a software engineer on 85-86% of criterion verdicts, roughly the rate at which two human engineers agreed with each other. Case studies show a single unsupported claim can fail an otherwise strong attempt, and that good engineering judgment includes both flagging hidden hazards and avoiding unnecessary work.

## Why it matters

A benchmark design directly usable as a template for evaluating "beyond functional correctness" agent behavior (truthful reporting, hazard-flagging, avoiding scope creep) using an agentic grader whose agreement with human experts is independently measured rather than assumed — relevant to anyone building evals who wants to move past pass/fail test execution toward professional-judgment criteria, with a demonstrated large performance spread (52.2% vs. ≤18.9%) showing the benchmark currently discriminates meaningfully between models.

## Verification notes

Fetched directly from arXiv; abstract and metadata confirmed (v1 submitted 23 November 2026, within the discovery window; primary category cs.SE, cross-listed cs.AI). All figures above are as stated in the abstract. The rubric-construction process and the agentic grader's internal mechanics were not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

None yet.
