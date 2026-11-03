---
slug: 2026-wang-stategraph-dependency-aware-agent-memory
title: "A State Change Is Local, Its Consequences Are Not: Dependency-Aware State Revision for Long-Term Agent Memory"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.02912
canonical_ids: ["arxiv:2611.02912"]
publisher_or_author: "Yiqi Wang, Tongyuan Zhao, Jiaqi Zhang, Yiqun Duan, Zhangkai Wu, Mingkai Zheng, Taotao Cai"
published: 2026-11-02
captured: 2026-11-03
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on harness and context engineering (lens 2): a new method
  (StateGraph) and benchmark (StateChangeBench) for cascading memory
  revision in long-lived agents, with a clear mechanism (counterfactual
  dependency verification) and quantified gains on its own benchmark,
  though only comparable to baselines on most pre-existing public
  benchmarks.
---

# A State Change Is Local, Its Consequences Are Not: Dependency-Aware State Revision for Long-Term Agent Memory

## Summary

Long-lived agents need persistent memory that stays consistent as the
world changes. Existing memory systems can correct a single contradicted
memory but leave dependent beliefs, plans, and actions in place even after
the premise supporting them is gone. The authors define dependency-aware
state revision — identifying which dependent states should no longer be
trusted after a change — and build StateGraph, which constructs an
evolving state-dependency graph from interaction histories and uses
counterfactual verification (testing whether a dependent state would
survive losing its premise) to separate true support-dependence from mere
semantic relatedness. A dependent state is invalidated only when a strict
dependency fails and no independent support path remains. On the authors'
new StateChangeBench (50 author-built cases annotated with cascade depth,
hard negatives, and action consequences), StateGraph's Impact-F1 exceeds a
reimplemented CUPMem baseline by 6.9 points at cascade depth 1 and 26.0
points at depth 3+; on public long-term-memory benchmarks, its point
estimates are comparable to or higher than baselines on most datasets (as
stated in the fetched abstract; full benchmark details and baseline list
not reviewed at capture).

## Why it matters

Names a specific, underaddressed agent-memory failure mode — a corrected
fact doesn't automatically invalidate the plans and beliefs built on it —
and gives a concrete mechanism (counterfactual dependency testing) rather
than a blanket memory-refresh policy. Relevant to anyone building
long-horizon agents whose memory needs to stay coherent after corrections,
though the authors' own framing (comparable-to-baseline results on public
benchmarks, large gains only on their own new benchmark) suggests treating
this as early, promising evidence rather than a settled technique.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 2 Nov 2026, no revisions). The dependency-aware-state-revision
problem framing, the StateGraph/counterfactual-verification method, the
StateChangeBench design (50 cases, cascade depth, hard negatives), and the
6.9/26.0-point Impact-F1 gains at depth 1/3+ all trace to the fetched
abstract text, which is the paper's own stated summary of its results —
treated as `verified` on this library's convention for single-source
arXiv preprints whose headline figures are self-reported. The full paper
(public-benchmark comparison tables, baseline implementation detail,
author affiliations) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
