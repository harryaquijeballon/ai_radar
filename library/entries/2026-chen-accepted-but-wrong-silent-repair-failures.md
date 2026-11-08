---
slug: 2026-chen-accepted-but-wrong-silent-repair-failures
title: "Accepted but Wrong: Silent Failures of LLM Code Repairs after API Migrations"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.08269
canonical_ids: ["arxiv:2611.08269"]
publisher_or_author: "Xiaobo Chen, Genliang Zhu, Ziyuan Wang, Chu Wang"
published: 2026-11-05
captured: 2026-11-08
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails — the
  core lens for the policy-simulation interest): a preregistered, quantified
  study across 73 real API-migration tasks showing a plausible release gate
  (checking typical-input assertions) lets 41% of wrong LLM-generated repairs
  through, and showing a specific, cheap fix (one edge-case input per
  release note) that cuts that to ~6.5%.
---

# Accepted but Wrong: Silent Failures of LLM Code Repairs after API Migrations

## Summary

Studies LLM-repaired code that runs without errors after a runtime or API
migration but returns wrong results — "runs cleanly yet returns wrong
results." A release check against typical inputs can ship such repairs
undetected. The preregistered study covers 73 tasks drawn from 60
documented changes in CPython, Node.js, and SQLite, with candidates
executed on the real runtimes against withheld contracts. A release gate
checking all assertions on typical inputs let through about 41% of wrong
repairs; adding one edge-case input written from the migration's release
note cut that to about 6.5% (6.1% on unseen clusters). Hard distractor
programs that match legacy output on typical inputs still passed some
checks, so the edge input did not eliminate the problem entirely.
Self-generated tests helped less than the targeted edge input. An AI audit
flagged 34 contracts as stricter than the stated requirements, but dropping
those disputed checks changed no verdicts. No model-written code was
executed during the study.

## Why it matters

A directly actionable, quantified finding for anyone gating LLM-generated
code repairs on tests: typical-input release checks are not enough (41%
false-accept rate in this study), but one well-chosen edge case drawn from
the migration's own release notes is a cheap, concrete fix that gets most
of the way there (~6.5%) — exactly the kind of deterministic guardrail this
library's policy-simulation interest tracks (lens 4).

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 5 Nov 2026, no revisions). The task/dataset counts (73 tasks, 60
documented changes, three runtimes), the 41%/6.5%/6.1% figures, the
distractor-program finding, and the 34-contract AI-audit result all trace
to the fetched abstract text — treated as `verified` per this library's
standing convention for single-source arXiv preprints whose headline claims
are self-reported. The full paper (exact task list, contract design) was
not reviewed at capture. Same author group as the already-archived "Signed
but Not Safe" entry.

## Updates

None yet.

## Related entries

[2026-chen-signed-but-not-safe-requirement-integrity](2026-chen-signed-but-not-safe-requirement-integrity.md) — same author group, a related study of integrity failures in agent/LLM pipelines that pass surface-level checks.
