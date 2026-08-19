---
slug: 2026-he-agent-lightning-harnessed-rl
title: "Agent Lightning v1.0: Towards Harnessed Agentic RL"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.17528
canonical_ids: ["arxiv:2608.17528"]
publisher_or_author: "Zhiyuan He, Siwei Zhang, Zhiwen Zhou, Yuqing Yang, Yu Kang, Yuge Zhang, Luna K. Qiu, Tin Yan Tsui, Jiahang Xu, Chong Luo"
published: 2026-08-18
captured: 2026-08-19
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Squarely on lens 1 (agent architecture) and lens 2 (harness engineering):
  an open-sourced framework letting a deployment-time agent harness
  participate directly in RL training, with a quantified SWE-bench
  Verified gain and released reproducible workflows.
---

# Agent Lightning v1.0: Towards Harnessed Agentic RL

## Summary

The paper addresses agent systems that operate within harnesses managing
tools and control flow. The authors present "harnessed agentic RL," where
the deployment-time harness itself participates in model training rather
than being replaced by a separate training engine. The ~3,500-line-of-code
framework supports arbitrary agent harnesses and serves as a testbed for
technical challenges including retokenization, sample merging, advantage
calculation, and loss normalization. Tested on instruction-following,
search, and coding agents, the framework improved Qwen3.5-9B's performance
on SWE-bench Verified from 41.8% to 56.4% using only 6,000 training
examples. Complete workflows and scripts were released for reproducible
research (unverified in detail — full training configuration and ablation
results not read beyond the abstract).

## Why it matters

A concrete architecture pattern for teams who want their production agent
harness (tools, control flow) to double as the RL training loop rather
than maintaining a parallel, harness-agnostic training stack — with an
open-sourced implementation and a large, quantified SWE-bench gain from a
modest training set. Directly actionable for anyone building or tuning a
coding- or tool-using-agent harness with an RL improvement loop in mind.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The headline
result (SWE-bench Verified 41.8% to 56.4% with 6,000 examples, ~3,500 LOC
framework) is traced to the abstract, including direct quotes. The full
training protocol, baseline configuration, and released code were not
independently corroborated — hence partial verification.

## Updates

- **2026-08-19** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
