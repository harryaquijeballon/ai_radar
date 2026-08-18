---
slug: 2026-li-openharmonybench-coding-agent-benchmark
title: "OpenHarmony Bench: Evaluating LLMs and Coding Agents on OpenHarmony App Development"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.16022
canonical_ids: ["arxiv:2608.16022"]
publisher_or_author: "Li Li et al. (27 co-authors)"
published: 2026-08-17
captured: 2026-08-18
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On lens 4 (evaluation): a full-project (not function-level) coding-agent
  benchmark with a quantified build-success-vs-correct-functioning gap and
  a spec-driven-tasks-are-hardest finding — the platform (OpenHarmony) is
  narrow, but the evaluation-design lesson generalizes, hence medium.
---

# OpenHarmony Bench: Evaluating LLMs and Coding Agents on OpenHarmony App Development

## Summary

The paper introduces a benchmark testing LLMs and coding agents on
end-to-end app development for OpenHarmony (a mobile/IoT OS), requiring
agents to modify complete projects — UI, data storage, build configuration,
and system functions — rather than isolated functions. It covers 153
primary tasks across three categories: feature additions from natural
language, scenario-based specifications, and bug repairs. Reported
results: newer model versions outperform older ones; projects build
successfully at a high rate (94.77%-100%); but correctly *functioning*
apps remain far harder (48.36%-58.39%); and "spec-driven tasks have the
lowest Task Completion under all-checks task scoring, with no
configuration exceeding 35%" (unverified in detail — per-task and
per-model breakdowns not read beyond the abstract).

## Why it matters

The build-succeeds-but-doesn't-work gap (near-100% vs. under 60%) is a
generalizable evaluation lesson: build/compile success is a weak proxy for
functional correctness in full-project coding-agent evaluation, and
specification-driven tasks are disproportionately hard — relevant to
anyone designing an internal coding-agent eval, independent of the
OpenHarmony platform specifics.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The task-count,
build-success-rate range, functional-success-rate range, and the
spec-driven-tasks quote are traced to the abstract. Per-model and per-task
breakdowns were not independently corroborated — hence partial
verification.

## Updates

- **2026-08-18** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
