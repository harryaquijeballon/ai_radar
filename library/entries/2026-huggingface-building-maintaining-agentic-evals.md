---
slug: 2026-huggingface-building-maintaining-agentic-evals
title: "How to Build and Maintain an Agentic Evaluation"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://huggingface.co/blog/agentic-evals
canonical_ids: []
publisher_or_author: "Hugging Face"
published: 2026-11-23
captured: 2026-11-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  An eight-step method for building agent evaluations (define the claim,
  validate the oracle, check the grader against no-op and shortcut agents,
  report pass@k/pass^k) plus concrete maintenance and open-sourcing
  guidance — squarely lens 4 (evaluation, validation and deterministic
  guardrails): directly usable by a builder setting up an eval this quarter.
---

# How to Build and Maintain an Agentic Evaluation

## Summary

This Hugging Face post lays out an eight-step method for building agentic
evaluations: (1) define the claim narrowly and split it into checkable
skills with domain-expert input on noise and tolerances; (2) reuse an open
task and its infrastructure (e.g., the Harbor task format, a Terminal-Bench
task) rather than building from scratch; (3) run the reference solution
(oracle) first and fix the task before reading model failures into results
if the oracle itself fails; (4) adapt the task with synthetic data from
known parameters, explicit units and conventions, and grading on saved
output rather than the agent's self-report of completion; (5) check the
evaluation itself — the oracle passes, a no-op agent fails, and shortcuts
fail (the post describes a shortcut that fooled a ratio-only grader, fixed
by adding checks on the fit itself); (6) read failure traces and group them
by cause (early stopping, missing dependencies, grading errors); (7) report
scores with pass@k ("at least one success") and pass^k (consistency), with
uncertainty clustered by task plus cost and tool-use figures; (8) compare
models with pinned provider/version and investigate shared failures for
task, environment, or verifier causes. On maintenance, it recommends
inviting public review, keeping a dated error record per flaw, checking
construct validity (do the tasks actually support the claim?), refreshing
tasks to limit contamination/saturation (noting that hiding test data alone
does not prevent saturation), and retiring tasks into regression checks or
harder successors. On open-sourcing, it recommends releasing specs,
environments, harness code, verifiers, traces, and results separately,
protecting active test items via gated datasets, and pinning versions and
run configurations for reproducibility. Its central principle: "grade what
the agent produced," not what the agent claims to have done.

## Why it matters

A complete, concrete recipe — not just principles — for building an agent
eval from scratch, including the specific checks (no-op agent fails,
shortcuts fail) that catch a flawed grader before it produces misleading
results, directly applicable to anyone building or auditing agent
evaluations this quarter.

## Verification notes

Read directly from the source post (huggingface.co/blog/agentic-evals),
dated 2026-11-23 on the Hugging Face blog listing. The summarized eight-step
method, maintenance guidance, and open-sourcing recommendations are taken
directly from the fetched post text. No independent corroboration sought —
a first-party methodology post, not an empirical claim requiring external
checking.

## Updates

None yet.

## Related entries

None yet.
