---
slug: 2026-jiang-ascon-failure-attribution-multiagent
title: "ASCon: A Direction-Aware Reciprocal Agent-Step Contextualization Model for Failure Attribution in Multi-Agent Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.10646
canonical_ids: ["arxiv:2608.10646"]
publisher_or_author: "Shuyu Jiang, Yue Ran, Kaiyu Xu, Xingshu Chen, Yi Zhang, Hao Ren, Rui Tang, Tianwei Zhang — arXiv preprint (cs.MA)"
published: 2026-08-11
captured: 2026-08-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 5 (observability and debugging): a quantified improvement
  to failure attribution in LLM-based multi-agent systems — identifying
  which agent, which step, and which failure mode caused a run to fail —
  a transferable diagnostic pattern with reported gains that generalize
  out-of-domain.
---

# ASCon: A Direction-Aware Reciprocal Agent-Step Contextualization Model for Failure Attribution in Multi-Agent Systems

## Summary
ASCon addresses failure attribution in LLM-based multi-agent systems: given a failed run, identifying the faulty agent, the erroneous step, and the failure mode. It builds a unified model over system execution trajectories using direction-aware graph attention to model execution context, masked step-to-agent attention to construct behavior-aware agent representations, and agent-conditioned step contextualization. Against the paper's baselines, it improves faulty-agent detection by 5.83%+, faulty-step detection by 10.63%+, and failure-mode detection by 14.73%+ in Macro-F1, with reported gains holding up in out-of-domain scenarios.

## Why it matters
A transferable diagnostic technique for debugging multi-agent systems in production or research use — rather than manually tracing a failed multi-agent run, ASCon's approach automates attributing failure to a specific agent, step, and mode, directly on the observability/debugging lens for multi-step agent pipelines.

## Verification notes
Read via the arXiv abstract page. The Macro-F1 improvement figures and the out-of-domain generalization claim are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
