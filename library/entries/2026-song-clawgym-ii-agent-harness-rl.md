---
slug: 2026-song-clawgym-ii-agent-harness-rl
title: "ClawGym II: Exploring Black-Box RL on Agent Harness"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.16798
canonical_ids: ["arxiv:2608.16798"]
publisher_or_author: "Huatong Song, Fei Bai, Ming Yang, Renyuan Li, Jia Deng, Jujie He, Zhange Zhang, Daixuan Cheng, Yan Xing, Qi Yun, Xuxing Chen, Danyang Li, Feng Chang, Chuan Hao, Ran Tao, Jian Yang, Bryan Dai, Wayne Xin Zhao, Mingjie Tang, Ji-Rong Wen"
published: 2026-08-17
captured: 2026-08-18
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On lens 1 (agent architecture/orchestration): a training-infrastructure
  framework decoupling policy optimization from harness execution, enabling
  multi-harness agent training with quantified gains — practically relevant
  to teams training rather than only prompting agents, hence medium (more
  training-infrastructure than product-reliability pattern).
---

# ClawGym II: Exploring Black-Box RL on Agent Harness

## Summary

The paper presents a unified black-box reinforcement-learning framework for
stable, scalable optimization of general agents operating through complex
harnesses. It uses sandbox-based execution infrastructure isolating task
environments and harnesses for concurrent rollouts at scale, decouples
policy optimization from harness execution via a serving proxy, organizes
captured calls into prefix trees, and adapts PPO and GRPO for
tree-structured optimization. The framework supports multi-harness
training — a single model learning from heterogeneous systems. Reported
results: roughly 10-15 percentage-point improvement on ClawGym-Bench,
stable across 200-400 optimization steps, with consistent gains on
additional benchmarks (unverified in detail — full benchmark suite and
ablations not read beyond the abstract).

## Why it matters

Most agent-reliability engineering discourse focuses on prompting and
harness design at inference time; this addresses the training side —
how to RL-train an agent policy against arbitrary, black-box harnesses
without harness-specific engineering per training run. The
decoupling-via-serving-proxy pattern is a transferable infrastructure idea
for teams building or fine-tuning agent policies against their own
harnesses.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The architecture
description (sandboxed rollouts, serving-proxy decoupling, prefix-tree
organization, PPO/GRPO adaptation) and the headline 10-15 percentage-point
gain are traced to the abstract. Full benchmark identities, ablation
results, and the 200-400 step stability claim's protocol were not
independently corroborated — hence partial verification.

## Updates

- **2026-08-18** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
