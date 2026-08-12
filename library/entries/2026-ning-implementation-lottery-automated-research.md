---
slug: 2026-ning-implementation-lottery-automated-research
title: "One Run Is Not an Idea: The Implementation Lottery in Automated Research"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.26587
canonical_ids: ["arxiv:2607.26587"]
publisher_or_author: "Jingjie Ning, Shanshan Zhong, Xiaochuan Li, Ji Zeng, Chenyan Xiong — arXiv preprint"
published: 2026-07-29
captured: 2026-07-30
relevance:
  social_science: high
  ai_engineering: high
verification: verified
rationale: >-
  High on both domains: a quantified, credible warning about a method
  failure mode in any automated/agentic research pipeline — single
  implementation runs are unreliable evidence for idea-level conclusions —
  directly usable for evaluating automated empirical pipelines
  (social_science lens 5/6) and for evaluation/validation practice in
  agentic research systems generally (ai_engineering lens 4, and the
  policy-simulation-validation interest).
---

# One Run Is Not an Idea: The Implementation Lottery in Automated Research

## Summary
The paper identifies and names the "implementation lottery": in automated research systems, a single experimental run scores one specific implementation of an idea, but conclusions about the underlying idea or mechanism are often drawn as if that run represented the idea itself. The authors introduce the "Idea Reliability Audit" to measure how consistently an idea's evaluated performance holds across different implementations of the same idea. Testing across 312 assignments spanning tabular-data tasks and coding-agent tasks, they find "implementation variance was more than five and ten times same-artifact rerun variance" in the respective settings. A central quantified finding: in roughly 25.6%–43.6% of decisions, the winning approach identified under one implementation changed when tested under an alternative implementation of the same idea. The authors conclude that "before a score guides idea-level branching, transfer, or research memory, evidence should cover multiple implementations."

## Why it matters
For any agentic or automated research system — including agentic economic-research pipelines and policy-simulation harnesses this radar already tracks (e.g. Korinek's AI-for-economic-research line, agentic workflow papers) — this is a specific, quantified caution against trusting single-run evaluation to decide which idea "won." The reported decision-flip rate (up to ~44%) is a concrete number a team can use to justify multi-implementation evaluation before using an automated system's output to guide research branching, method transfer, or a persistent "research memory."

## Verification notes
Source is an arXiv preprint (cs.MA, surfaced via the arXiv cs.MA curated listing on 2026-07-30, submitted 2026-07-29). The abstract page was fetched directly; all summarized claims and figures above are quoted or closely paraphrased from that abstract text. The full paper (task-level breakdown, audit methodology detail) was not fetched, so verification rests on the source's own stated abstract results, not independent corroboration.

## Updates
None yet.

## Related entries
None yet.
