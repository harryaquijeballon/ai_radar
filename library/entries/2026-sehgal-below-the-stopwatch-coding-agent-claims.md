---
slug: 2026-sehgal-below-the-stopwatch-coding-agent-claims
title: "Below the Stopwatch: Checking the Performance Claims of Coding Agents in the Kernel"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.31460
canonical_ids: ["arxiv:2611.31460"]
publisher_or_author: "Yuvraj Sehgal, Sneh Patel, Mahsa Panahandeh, Naser Ezzati-Jivan"
published: 2026-11-25
captured: 2026-11-25
relevance:
  ai_engineering: high
  social_science: n/a
verification: verified
rationale: >-
  Lens 4 (evaluation, validation and deterministic guardrails): a
  concrete, reusable methodology for independently verifying coding
  agents' self-reported performance-improvement claims against kernel and
  hardware-level ground truth, rather than trusting the claim or the
  benchmark score alone — directly applicable to anyone deploying
  coding agents for performance-sensitive changes.
---

# Below the Stopwatch: Checking the Performance Claims of Coding Agents in the Kernel

## Summary

The authors present a pipeline ("Below") that checks whether coding agents' runtime-performance pull requests actually deliver speedups for the mechanism they claim, not just whether the code runs faster. From 1,343 runtime-performance PRs in the AIDev dataset, they extract each PR's claimed mechanism and map it to kernel and hardware signals that should change if the claim holds; a build agent that never sees the claim rebuilds the code before and after each PR, and the two versions are measured with timing runs, hardware performance counters, and LTTng kernel traces. Across 82 analyzed PRs: 32 ran measurably faster, 28 showed no clear change, and 22 ran slower. Most claims arrive unmeasured — 57.3% of PRs offer only reasoning or no evidence, and only 31.4% state an effect size. The expected signal of the claimed mechanism appeared in just 34 of the 82 PRs (20 of those detectable only via kernel-trace signals), and 42 PRs also changed program output. Kernel signals moved about 1.7 times as often for a faster PR's claimed mechanism as for unclaimed mechanisms, versus only about 1.15 times for instruction count alone — kernel-level evidence discriminated genuine claimed-mechanism speedups better than simpler proxies.

## Why it matters

A directly transferable verification pattern for anyone relying on coding agents for performance work: don't trust a stated speedup mechanism or even a passing benchmark — rebuild blind to the claim and check kernel/hardware signals specific to the claimed mechanism. The finding that over half of performance PRs carry no evidence at all, and that a quarter of "successful" PRs were actually slower, is a concrete argument for building this kind of independent-verification step into any agentic performance-engineering workflow.

## Verification notes

Fetched directly from arXiv; abstract and submission history (v1, 23 November 2026, appearing in the 25 November cs.SE listing — a one-day announcement lag consistent with routine processing) confirmed on the page. Accepted as a short paper at the AGENT 2027 workshop, ICSE 2027, per the page's comments field. Load-bearing figures (1,343 PRs sourced, 82 analyzed, 57.3% unmeasured claims, 32/28/22 faster/unchanged/slower split, 1.7x vs. 1.15x signal ratios) are as stated in the abstract. The full extraction and signal-mapping methodology was not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

None yet.
