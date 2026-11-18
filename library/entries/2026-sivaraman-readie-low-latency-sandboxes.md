---
slug: 2026-sivaraman-readie-low-latency-sandboxes
title: "Readie: Low-Latency Code Sandboxes for AI Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.22171
canonical_ids: ["arxiv:2611.22171"]
publisher_or_author: "Arjun Sivaraman, Zhaoheng Li, Alan Shi, Sanjay Malisetty, Eugene Wu, Yongjoo Park"
published: 2026-11-17
captured: 2026-11-18
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility and governance, via sandboxing) and lens 2
  (harness engineering): a measured systems technique with a stated,
  quantified improvement over existing sandbox approaches, directly relevant
  to anyone running agent-generated code safely at scale.
---

# Readie: Low-Latency Code Sandboxes for AI Agents

## Summary

The paper addresses slow sandbox startup for AI-agent code execution: a
single environment snapshot cannot be both compact and cover the varied
packages/datasets that different agent-generated scripts need, so systems
today trade off size against coverage. The authors formulate snapshot-set
construction as an optimization problem — choosing a small set of
fast-initializing snapshots, learned from a large training workload of
roughly 15,000 scripts drawn from public sources and LLM-generated code —
and solve it with an approximation algorithm. Their system, Readie, cuts
sandbox startup latency by 3–22x and end-to-end runtime by 1.3–3.3x compared
with existing approaches, at the same storage budget.

## Why it matters

Gives anyone running AI-agent-generated code at scale (e.g., a coding agent
that executes and checks its own output many times per task) a concrete,
measured lever for the latency cost of sandboxing — directly complementary
to the isolation-focused sandboxing pattern published the same week by Simon
Willison and Prime Radiant ([External sandboxes for coding
agents](2026-willison-external-sandboxes-coding-agents.md)): that post solves
*where* code runs safely, this paper addresses *how fast* a fresh, safe
environment can be ready.

## Verification notes

Fetched the arXiv abstract page directly (arxiv.org, on the egress
allowlist). The claim, optimization framing, data-set size, and the 3–22x /
1.3–3.3x figures are traced to the abstract text as summarized by the
fetch. The paper's own baselines and experimental setup were not
independently re-derived.

## Updates

None yet.

## Related entries

- [External sandboxes for coding agents](2026-willison-external-sandboxes-coding-agents.md) — same-week sandboxing work, addressing isolation rather than startup latency.
