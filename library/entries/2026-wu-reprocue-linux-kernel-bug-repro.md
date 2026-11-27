---
slug: 2026-wu-reprocue-linux-kernel-bug-repro
title: "Reproducer Synthesis for AI-Reported Bugs in the Linux Kernel"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.34142
canonical_ids: ["arxiv:2611.34142"]
publisher_or_author: "Xiao Wu, Yunbo Ni, Hao Sun, Yuanyuan Yuan, Shaohua Li — arXiv preprint"
published: 2026-11-25
captured: 2026-11-27
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  A quantified real-world finding that runnable reproducers make
  AI-generated bug reports far more actionable to human maintainers than
  text explanations alone (69.4% vs. 9.3% confirmed) — a concrete,
  transferable lesson for AI-assisted software development (lens 7) on
  what AI code-review/bug-report output needs to actually get used.
---

# Reproducer Synthesis for AI-Reported Bugs in the Linux Kernel

## Summary

AI review systems increasingly file bug reports against Linux kernel
patches, but maintainers often ignore reports that are only textual
explanations, because confirming them requires manually building a
reproduction case. The authors present ReproCue, which generates
proof-of-concept (PoC) reproducers for AI-generated kernel bug reports by
replaying historical kernel bugs to learn one reproduction finite-state
machine (FSM) per subsystem from successful runs; each FSM records the
steps a reproduction takes and the requirements observed at each step. For
a new review, ReproCue follows the matching subsystem's FSM and adjusts the
PoC and environment based on what execution reveals is missing. On 100
recent AI-generated reviews, ReproCue produced PoCs for 49 of them, versus
10 for a comparison agentic reproducer and 9 for state-of-the-art directed
fuzzing. Linux kernel maintainers confirmed 69.4% of ReproCue's generated
PoCs, against 9.3% confirmed for Sashiko, a comparison system that provides
only textual explanations. (unverified beyond the abstract: the exact
confirmation methodology and the identity/configuration of the "agentic
reproducer" and "Sashiko" baselines, which would require the full paper.)

## Why it matters

Directly actionable for anyone building or evaluating AI code-review or
bug-reporting tools: a runnable reproducer, not a textual explanation, is
what makes an AI-generated bug report actionable to a human reviewer —
textual-only reports are confirmed at roughly an order of magnitude lower
rate in this study. Teams building AI-assisted review pipelines should
prioritize automatic reproduction synthesis over explanation quality if the
goal is actually getting maintainers to act on AI findings.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.34142, v1 submitted
2026-11-25, cs.OS). The FSM-based methodology and the quantified figures
above (49/100 PoCs produced vs. 10 and 9 for the comparison systems; 69.4%
vs. 9.3% maintainer-confirmed) are traced to the abstract's own description
as summarized by the fetch tool. No independent corroboration was
attempted; verification is partial pending a full-text read.

## Updates

None yet.

## Related entries

None yet.
