---
slug: 2026-sehgal-stratum-repository-memory
title: "Stratum: Repository Memory for Coding Agents Beyond the Context Window"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.36153
canonical_ids: ["arxiv:2610.36153"]
publisher_or_author: "Yuvraj Sehgal, Mahsa Panahandeh, Naser Ezzati-Jivan"
published: 2026-10-26
captured: 2026-10-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on harness and context engineering (lens 2): reframes coding-agent
  memory as a repository-scale indexing problem rather than a context-
  length problem, backed by a real-commit analysis (752 bug-fix commits)
  and a small but sharply quantified cross-session experiment (21/24 vs.
  6/24 root-cause success, p<10^-4, at 4.5x lower token cost) — a concrete,
  testable architecture, not a position paper.
---

# Stratum: Repository Memory for Coding Agents Beyond the Context Window

## Summary

Argues that coding agents' session-to-session amnesia is a memory-
architecture problem, not a context-length problem: each session re-reads
files, retries failed approaches, and forgets root causes a prior session
already found. Three measurements motivate this framing: mid-size
projects already exceed the largest production context windows; across
752 real bug-fix commits, the median fix touches two files and those
files plus their direct imports cover less than 10% of the repository, so
the bottleneck is file *selection* rather than context capacity; and even
with transitive import reachability and test links, 47% of co-edited file
pairs are structurally disconnected, so selection knowledge must come from
history, not static structure. The authors also note storing knowledge in
a model's KV cache costs 10^4–10^5 times more bytes than storing it as
indexed text.

They sketch Stratum, a tiered memory store kept alongside the repository
and accessed through "page-safe" tools that report what was returned,
what remains, and what it cost (retrieval over a million-node store takes
1.7 ms at the median). In an eight-bug, multi-session experiment, an agent
that inherited memory from a prior session — written by a *different*
model — identified the root cause in 21 of 24 trials, versus 6 of 24 for a
retrieval-only baseline (Fisher's exact p < 10^-4), at a 4.5x lower median
token cost; pooling the store across all eight investigations reached 8/8
success (all figures as stated in the fetched abstract; full paper,
replication package, and statistical methodology not reviewed at capture).

## Why it matters

A concrete, testable alternative to "just use a bigger context window" for
coding-agent memory: index repository knowledge as persistent, cross-
session, cross-model memory rather than re-deriving it every session from
scratch. The commit-level evidence (10% file coverage from imports alone,
47% of co-edited pairs structurally invisible) gives builders a reason to
distrust import-graph-only retrieval, and the cross-session experiment —
small but sharply significant — is a template other teams could replicate
on their own bug-fix history to test whether inherited memory helps.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-29; single version,
submitted 26 Oct 2026, 18:53 UTC; cross-listed cs.SE/cs.AI). The KV-cache
cost-ratio claim, the 752-commit analysis, the 47% disconnection figure,
the 1.7 ms median retrieval latency, and the 21/24 vs. 6/24 (p<10^-4) and
4.5x token-cost results all trace to the fetched abstract text. The
replication package (Zenodo DOI 10.5281/zenodo.23615180) was not fetched.
Load-bearing figures are traced to the authors' own stated summary but not
independently corroborated; the experiment's small sample (8 bugs, 24
trials per condition) limits how far the statistical result generalizes.

## Updates

None yet.

## Related entries

[2026-sehgal-context-pipeline-not-window](2026-sehgal-context-pipeline-not-window.md) — same authors, published two days earlier: that entry diagnoses information attrition from fixed-length tool-output truncation inside a single session, while this one addresses the separate problem of memory loss *between* sessions. Companion works on context/memory engineering for coding-agent harnesses.
