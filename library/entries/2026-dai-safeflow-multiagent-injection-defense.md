---
slug: 2026-dai-safeflow-multiagent-injection-defense
title: "SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.25255
canonical_ids: ["arxiv:2607.25255"]
publisher_or_author: "Haowen Dai, Zonghao Ying, Wenfeng Li, Xiangfan Wu, Yisong Xiao, Tianyuan Zhang, Jiaye Lin, Lei Wei, Guangyuan Dong, Xitong Ling, Xixun Lin, Quanchen Zou, Xiangzheng Zhang — arXiv preprint"
published: 2026-07-28
captured: 2026-07-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on reproducibility, security and governance (lens 6): a concrete
  defensive control — semantic taint tracking through a dynamic
  cross-agent graph — against a named, real failure mode (harmful goals
  split across agents to evade per-agent detection), benchmarked across
  four distinct attack types with reported attack-success-rate reductions
  and preserved benign-task performance.
---

# SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems

## Summary

Addresses a multi-agent security gap: a harmful goal can be split into
subtasks that look innocuous to each individual agent, evading per-agent
safety checks. SafeFlow treats this as a semantic information-flow control
problem — it applies structured semantic "taints" to an initial request,
tracks that taint through a collaborative workflow via a dynamic graph, and
validates actions against the accumulated taint before they execute. Tested
across four benchmarks — prompt injection, jailbreak-driven unsafe tool
deployment, risky code execution, and harmful web-agent behaviour — the
authors report SafeFlow "substantially decreases attack success rates"
(unverified — exact figures not read at capture) while preserving strong
performance on benign tasks and keeping risk context intact across
delegation chains.

## Why it matters

A concrete architectural control for exactly the class of multi-agent
security failure this radar's guardrails lens is meant to surface: instead
of relying on each agent to independently judge a subtask's safety, taint
propagation gives the system a way to reason about the *composed* goal
across a delegation chain. Directly applicable to any multi-agent design
where subtasks are farmed out to specialized or lower-trust agents.

## Verification notes

arXiv abstract page fetched directly (2026-07-29); title, full author list,
and "Submitted on 28 Jul 2026" confirmed. The taint-propagation mechanism,
the dynamic-graph tracking design, and the four-benchmark evaluation scope
trace to the fetched abstract text; the quantitative attack-success-rate
reduction is stated only qualitatively in the abstract ("substantially
decreases") and is marked unverified pending a read of the full paper's
results tables. Full paper not read at capture.

## Updates

None yet.

## Related entries

[2026-vu-skillspector-agent-skill-scanner](2026-vu-skillspector-agent-skill-scanner.md) — another concrete pre/at-runtime control against agent-facing attack surface, at the skill-file layer rather than cross-agent delegation.
