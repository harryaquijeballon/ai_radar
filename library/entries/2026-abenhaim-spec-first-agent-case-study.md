---
slug: 2026-abenhaim-spec-first-agent-case-study
title: "Specification-first convergence with an AI coding agent: a case study of dismantling a core architectural invariant across 189 files in a 717k-line codebase with no test oracle and no human code review"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.12440
canonical_ids: ["arxiv:2608.12440"]
publisher_or_author: "Joel Abenhaim — arXiv preprint"
published: 2026-08-14
captured: 2026-08-14
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Concrete, quantified single-project case study on lens 1 (agent
  architecture) and lens 2 (harness engineering): a specification-first,
  audit-loop protocol used to complete a large real-world refactor with no
  test oracle and no human code review. High practical implication despite
  being an n=1 self-reported case study, which the Verification notes flag.
verification: partial
---

# Specification-first convergence with an AI coding agent

## Summary

The author reports a single large-scale case study in which an AI coding
agent completed an architectural refactor of a 717,725-line TypeScript
production codebase (3,648 files) with no pre-existing test oracle and no
human code review. The task: eliminate a UI panel lifetime guarantee so that
streaming generations survive panel closure and can reconnect without data
loss. The protocol used: the agent writes a formal specification, runs 14
refinement cycles validating the spec against source code, performs atomic
implementation with compile/test feedback loops, then runs 17 verification
cycles auditing the implementation against the frozen specification. Reported
results: 201 defects corrected across 31 audit passes before any human
execution of the code; 189 files modified (31 newly created), 288 files
touched during extraction; 34,770 insertions and 16,422 deletions; completed
in three days at a stated cost of USD 2,430; convergence confirmed by two
consecutive verification passes with zero findings; the author reports no
observed bugs post-implementation (unverified beyond the author's own
account — no independent post-deployment audit is cited). Full specification
and 1,500+ pages of session logs were published by the author for
transparency.

## Why it matters

A rare quantified account (cost, time, defect counts, and process) of using
a spec-first/audit-loop protocol to let an AI coding agent handle a large,
high-risk refactor with no human review — directly actionable as a process
pattern for teams considering similar agent-led architectural work, and
useful as a documented data point on cost/defect-rate tradeoffs (lens 1, 2,
7).

## Verification notes

Read via the arXiv abstract page only; the full paper, the published
specification, and the 1,500+ pages of session logs were not read. This is a
single self-reported case study by one author with no independent
replication or third-party audit cited — the "no observed bugs" claim in
particular is unverified and should be read as the author's own assessment,
not an independently confirmed outcome. Flagged here explicitly given the
paper's own framing invites strong claims from a single data point.

## Updates

None yet.

## Related entries

None yet.
