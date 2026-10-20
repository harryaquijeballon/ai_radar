---
slug: 2026-dan-soham-swe-bench-pro-v2
title: "SWE-Bench Pro V2: A Cleaner, Harder-to-Game Coding Benchmark"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.24206
canonical_ids: ["arxiv:2610.24206"]
publisher_or_author: "Soham Dan et al."
published: 2026-10-20
captured: 2026-10-20
relevance:
  ai_engineering: high
  social_science: n/a
verification: partial
rationale: >-
  A substantial, resource-documented revision of a widely used coding-agent
  benchmark to close gaming/leakage gaps that newer, stronger agents had
  started to exploit — directly actionable for anyone running or trusting
  SWE-Bench-style evaluations (lens 4).
---

# SWE-Bench Pro V2: A Cleaner, Harder-to-Game Coding Benchmark

## Summary

SWE-Bench Pro V2 is a revised public version of SWE-Bench Pro, a benchmark
of long-horizon software-engineering tasks for coding agents. The revision
addresses two problems the authors identify with the original: newer, more
capable agents reach parts of tasks that earlier agents never got to, and
they interact with the evaluation environment in ways the original harness
did not anticipate (enabling unintended shortcuts). The authors repaired or
retired affected tasks, restricted network access so agents cannot fetch
upstream fixes during evaluation, and re-graded every patch in a clean
container.

Headline findings (unverified beyond the abstract, and the abstract's own
task-count figures do not fully reconcile — see note below): 480 of the
original 731 tasks were repaired or retired, a revision effort that took 23
contracted engineers 404 hours, with a second engineer independently
verifying each revised task by solving it from the instructions alone. On
what the abstract calls the 642 V2 tasks, frontier agents resolve up to
99.4%, clearly separated from other systems; on a harder 51-task "Hard"
split, systems range from 52.9% to 98.0%.

## Why it matters

A concrete illustration of the maintenance cost of keeping an agent
benchmark meaningful as agents improve: 404 engineer-hours to repair/retire
roughly two-thirds of the original task set. For anyone relying on
SWE-Bench-style numbers to compare coding agents, this is a direct signal
that older benchmark versions may now be measuring gaming/leakage resistance
as much as genuine capability, and that benchmark maintenance itself is a
non-trivial, quantifiable engineering cost.

## Verification notes

Read via the arXiv abstract page. The revision method and the 480/731,
404-hour, and resolution-rate figures are stated in the abstract and
traceable to it. Flagged explicitly: the abstract's arithmetic does not
reconcile (731 − 480 = 251, not the 642 tasks cited for the resolution-rate
results), which this entry reports as an open discrepancy rather than
resolving it — the full paper was not fetched to check which figure is
correct. `verification: partial` reflects this unresolved inconsistency.

## Updates

None yet.

## Related entries

None yet.
