---
slug: 2026-peng-write-execute-refine-skill-optimizer
title: "Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.17587
canonical_ids: ["arxiv:2608.17587"]
publisher_or_author: "Kang Peng, Zhiwei Zhang, Yichen Zhang, Zezhong Wang, Yiming Du, Geng Tu, Baojun Wang, Bin Liang, Ruifeng Xu, Kam-Fai Wong"
published: 2026-08-18
captured: 2026-08-19
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On lens 1/2 (agent architecture, harness engineering): names a specific,
  quantified failure mode of agent-authored skills versus expert-written
  ones and proposes a trained skill-optimizer to close the gap — relevant
  to any harness that lets agents write or refine their own tool-use
  skills.
---

# Write, Execute, Refine: From Skill Followers to Skill Optimizers via Reinforcement Learning from Execution Feedback

## Summary

The paper addresses a gap in agent tool use: "expert-written natural
language skills can improve tool-using agents, yet agent-authored skills
perform 8-11 points worse." The authors propose WER, a framework that
trains a dedicated skill optimizer separate from a frozen executor. The
system cycles through three stages: the optimizer proposes skills, an
agent executes them repeatedly, and a programmatic verifier scores
outcomes; pairing successful and failed execution records lets the
optimizer learn from the consequences of its own prior outputs. On
benchmark tests, WER achieves improvements of 7.80 and 3.85 points above
baseline, and a 4B-parameter optimizer reaches 76.63% performance on
BFCL v4 (unverified in detail — the benchmark suite and baseline
definitions not read beyond the abstract).

## Why it matters

Quantifies a specific reliability gap — self-authored agent skills
underperform expert-written ones by 8-11 points — and proposes a
training-based fix (a separately trained skill optimizer using
execution-feedback pairs) rather than just prompting harder. Directly
relevant to any skill-authoring or self-improvement loop in an agent
harness, including this project's own skill-based architecture.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The 8-11 point
performance gap, the three-stage WER training cycle, and the BFCL v4
figure (76.63%) are traced to the abstract, including direct quotes. The
benchmark suite, baseline definitions, and full training protocol were not
independently corroborated — hence partial verification.

## Updates

- **2026-08-19** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
