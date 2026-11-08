---
slug: 2026-hua-agent-harness-boundary-criteria
title: "Beyond the Agent Harness: Boundary Criteria for Software-Factory Orchestration - A Single-Operator Case Study"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.06946
canonical_ids: ["arxiv:2611.06946"]
publisher_or_author: "Lei Hua"
published: 2026-11-03
captured: 2026-11-08
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 2 (harness engineering): proposes operational boundary
  criteria separating a single agent run, a "factory" layer coordinating
  runs, and a domain layer, tested for inter-rater reliability by two coder
  models — a useful conceptual vocabulary with a modest validation (one
  operator's pipeline, kappa agreement study), not yet a broadly validated
  standard.
---

# Beyond the Agent Harness: Boundary Criteria for Software-Factory Orchestration

## Summary

Argues that as systems add a layer above coding-agent harnesses to
organize many agent runs into continuous delivery, the field lacks a rule
for deciding which layer a given mechanism or failure belongs to. Proposes
boundary criteria based on an operational definition of a "run": mechanisms
confined to one run belong to the agent harness; those that coordinate
runs, pass state between runs, or update based on run outcomes belong to a
factory harness; those that must change with the application domain belong
to a domain layer, with two further tests assigning infrastructure and
model causes. For failures, the author codes where the defect originated,
which control failed to stop it, and where it was fixed. The criteria were
developed on failures from one operator's pipeline (six projects) and 26
components from three published systems, then frozen and applied by two
same-family model coders to 46 held-out units: the coders agreed on all 26
mechanism layers and 18–19 of 20 incident fields (kappa 0.86–0.93), though
each flagged about half the units as ambiguous, mostly from missing
information. A revised rule set separating mechanism classification from
incident attribution resolved the conflicts but lowered agreement in a
sensitivity re-coding (kappa 0.78–0.93). The author notes agreement is not
the same as accuracy, human coders were not tested, and the evidence is
preliminary.

## Why it matters

A candidate shared vocabulary for a real coordination problem — as teams
build "factory" layers on top of agent harnesses to run many coding agents
at scale, knowing which layer owns a given failure matters for debugging
and design — though the author's own caveats (single operator, no human
coder test, preliminary evidence) keep this at medium rather than high
(lens 2).

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 3 Nov 2026, no revisions). The boundary-criteria definitions, the
case-study scope (one operator, six projects, 26+46 components), and the
kappa figures (0.86–0.93, then 0.78–0.93) all trace to the fetched abstract
text — treated as `verified` per this library's standing convention for
single-source arXiv preprints whose headline claims are self-reported,
and the author's own stated caveats are reflected in the medium-tier
rationale above. The full paper was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
