---
slug: 2026-hapuarachchi-recovery-ai-agent-harnesses-survey
title: "Exercised, Rarely Recovered: What Public Reports Say About Recovery in 50 AI Agent Harnesses and Runtimes"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.27090
canonical_ids: ["arxiv:2611.27090"]
publisher_or_author: "Kaviru Hapuarachchi — arXiv preprint (cs.MA)"
published: 2026-11-23
captured: 2026-11-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A fixed-protocol survey of public failure/recovery reports across 50 real
  agent harnesses and runtimes (persistent, coding, research) — lens 5
  (observability and debugging): quantifies how rarely checkpoint/resume and
  rollback mechanisms fully recover in practice, a transferable failure
  taxonomy a builder could use to judge recovery claims.
---

# Exercised, Rarely Recovered: What Public Reports Say About Recovery in 50 AI Agent Harnesses and Runtimes

## Summary

This paper (Kaviru Hapuarachchi) studies public evidence on whether recovery
mechanisms for AI agents — resuming from checkpoints, undoing actions,
requesting approval, reading logs — actually work in practice. It covers 50
systems: 12 persistent agent runtimes, 26 coding-agent harnesses, and 12
research runtimes. Using a protocol fixed before data collection, the
authors grade each system on eight recovery mechanisms (from "not found" to
"exercised in a real run"), via two blind coding passes followed by
adjudication and re-checking against archived sources. They find recovery
mechanisms are used often in real life but usually do not fully succeed:
11 of 12 runtimes and 25 of 26 harnesses have at least one real-use report,
but of 128 reports collected, only 19 describe a full recovery, 54 are
partial, and 45 failed. Checkpoint/resume fully recovered in only 1 of 27
reports, and rollback in only 1 of 15. Research runtimes have
benchmark-tested recovery guarantees but no reported operational use, and
none of the harnesses studied offer compensation for external
(real-world) side effects once an action is taken.

## Why it matters

A concrete, cross-system failure taxonomy for a question builders ask
constantly — "if my agent harness says it supports recovery, how often does
that actually work?" — with a quantified answer (full recovery in roughly
1 in 7 reports) directly usable when evaluating or designing recovery
mechanisms, and a sharp reminder that recovery claims validated only in
benchmarks (research runtimes) have not been shown to hold operationally.

## Verification notes

Read directly from the arXiv abstract page (arxiv.org/abs/2611.27090),
listed Mon 2026-11-23 on the cs.MA recent-submissions page. The summarized
claims (the 50-system breakdown, the 128-report count and its full/partial/
failed split, the checkpoint/resume and rollback figures) are taken directly
from the arXiv-published abstract text. No independent corroboration sought
beyond the authors' own stated methodology (fixed protocol, blind coding,
adjudication).

## Updates

None yet.

## Related entries

None yet.
