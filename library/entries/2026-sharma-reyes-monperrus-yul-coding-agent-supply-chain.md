---
slug: 2026-sharma-reyes-monperrus-yul-coding-agent-supply-chain
title: "YUL: Bringing Software Supply Chain Security to Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.23314
canonical_ids: ["arxiv:2611.23314"]
publisher_or_author: "Aman Sharma, Frank Reyes, Martin Monperrus — arXiv preprint (cs.SE)"
published: 2026-11-13
captured: 2026-11-19
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance): a concrete,
  measured control for a specific supply-chain-security failure mode —
  coding agents declaring stale, training-data-recalled dependency
  versions — with a quantified before/after fix rate across two different
  agents and six ecosystems.
---

# YUL: Bringing Software Supply Chain Security to Coding Agents

## Summary

Coding agents choose and declare third-party dependencies themselves, and
often pin stale versions recalled from their training data — versions that
can carry known vulnerabilities later releases have fixed. The authors
present YUL, a harness-level check that validates every dependency
declaration an agent makes against the live package registry: if a
declared version is stale or doesn't exist, YUL blocks it and tells the
agent which version to use so it can retry. They evaluated YUL on 60 tasks
across six package ecosystems, using Claude Code (Claude Opus 5.5) and
OpenCode (DeepSeek V4.1 Flash). Without YUL, Opus declared a stale
dependency version in 29% of runs and DeepSeek in 39% — both agents did so
in every GitHub Actions run tested. With YUL in place, the agents ended on
the latest release in 93% of previously-stale Opus runs and 96% of
previously-stale DeepSeek runs.

## Why it matters

For anyone operating a coding-agent harness in CI or production: a direct,
implementable defense against a specific and measured failure mode —
agents introducing outdated, vulnerable dependencies because their training
data is stale — with evidence that the fix generalizes across two
differently-built agents and six ecosystems rather than being a
model-specific patch. The before/after rates (29%/39% stale → 93%/96% fixed)
give builders a concrete expectation for how much a registry-validation
gate can be expected to close this gap.

## Verification notes

arXiv abstract page fetched directly (2026-11-19); title, full author list,
"Submitted on 13 November 2026, 09:19:55 UTC" date, and cs.SE subject
category confirmed. Every quantitative claim in the Summary (60 tasks, six
ecosystems, the two agent/model pairings, the 29%/39% stale-declaration
rates, the 93%/96% post-fix rates) traces to the fetched abstract text.
Full paper body not read at capture; no independent corroboration attempted
(new working paper, no secondary coverage found). The paper's submission
date (13 Nov 2026) is six days before this run; no evidence of earlier
public circulation was found, dedup against INDEX.md, rejections.md, and
both deferred-candidate queues found no prior record, and it is within the
7-day eligibility cap, so it is treated as new. Upgrade path: read the full
PDF for the registry-validation mechanism and the per-ecosystem breakdown.

## Updates

None yet.

## Related entries

None yet.
