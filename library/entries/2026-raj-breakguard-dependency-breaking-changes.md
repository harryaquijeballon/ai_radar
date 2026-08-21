---
slug: 2026-raj-breakguard-dependency-breaking-changes
title: "BreakGuard: Detecting Dependency Breaking Changes"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.20167
canonical_ids: ["arxiv:2608.20167"]
publisher_or_author: "Rachna Raj, Benoit Baudry, Diego Elias Costa"
published: 2026-08-20
captured: 2026-08-21
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  A concrete, cost-quantified LLM-generated-test technique for catching
  dependency breaking changes — a deterministic-guardrail pattern (lens 4)
  directly usable in CI for AI-assisted software development (lens 7).
---

# BreakGuard: Detecting Dependency Breaking Changes

## Summary

BreakGuard statically extracts client methods that invoke a target library's
methods, then uses an LLM to generate per-focal-method tests aimed at catching
breaking changes (BCs) — tests that pass against the pre-upgrade library version
and fail against the post-upgrade version. Evaluated on 89 real breaking changes
from the BUMP dataset, using GPT-4o, Qwen3-Coder-480B, and GPT-OSS-120B across
three context levels, BreakGuard detected 30.3% of breaking changes at an average
cost of about $0.90 per detection, and was reported as more reliable at catching
crash-type breaking changes than behavioral (silent) ones.

## Why it matters

Gives teams a concrete, costed technique — and a candid detection-rate ceiling
(30.3%) — for automatically generating tests that catch dependency upgrade
breakage before it reaches production, with an explicit weak spot (behavioral,
non-crashing breaking changes) that a builder should account for rather than
assume away.

## Verification notes

Read directly from the arXiv abstract; the dataset size (89 BCs from BUMP), model
list, detection rate (30.3%), and per-detection cost (~$0.90) are traced to the
source text. No independent corroboration was possible — newly posted preprint
(submitted 20 Aug 2026), no second source yet. Verification is `partial`: traced
but not independently corroborated.

## Updates

- **2026-08-21** — Entry created.

## Related entries

None yet.
