---
slug: 2026-huang-probeagent-diagnosis-agent-failures
title: "ProbeAgent: Principled Diagnosis of Agent Failures in Verifiable Environments"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.26897
canonical_ids: ["arxiv:2611.26897"]
publisher_or_author: "Yue Huang, Yuchen Ma, Shuhang Lin, Yuyang Wu, Zixuan Weng, Zixiang Xu, Xiangqi Wang, Yuexing Hao, Yujun Zhou, Yue Zhao, Olexandr Isayev, Stefan Feuerriegel, Xiangliang Zhang — arXiv preprint (cs.CL)"
published: 2026-11-23
captured: 2026-11-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  An automated framework that isolates causes of agent failure by replaying
  cause-preserving variants of failed trajectories and clustering shared
  failure modes, validated by human annotators (90.0% acceptance of assigned
  descriptions, 83.3% rejection of similar-but-wrong ones) — lens 5
  (observability and debugging): a transferable method for turning vague
  "agent failed" outcomes into specific, checkable failure modes.
---

# ProbeAgent: Principled Diagnosis of Agent Failures in Verifiable Environments

## Summary

This paper introduces ProbeAgent, an automated framework for diagnosing why
an LLM agent fails on multi-step tasks in verifiable environments, where a
bad outcome could stem from a genuinely hard task or from a mistake the
agent repeats across tasks. The framework (1) builds executable tests from
benchmark tasks, validated with reference solutions, automated checks, and a
review of task requirements; (2) for each failed trajectory, generates an
explanation of the error and then probes it by creating new tasks that
preserve the suspected cause while varying the surrounding context, re-
running the agent to see whether the same error recurs; and (3) clusters
failures with similar causes and writes a description that distinguishes
each cluster's specific error. Across 22 agent configurations and tasks from
10 benchmarks, the authors collected 1,244 failures and produced 536
failure-mode descriptions. In human evaluation, annotators accepted 90.0% of
the failure-mode descriptions assigned to them and rejected 83.3% of
similar-but-incorrect alternatives.

## Why it matters

A concrete, validated method for converting coarse failure labels (e.g.,
"incomplete work") into specific, falsifiable failure modes (e.g., planning
without acting, stopping before delivering a file) — directly applicable to
anyone building agent evaluation or debugging pipelines who needs more than
a pass/fail signal to know what to fix.

## Verification notes

Read directly from the arXiv abstract page (arxiv.org/abs/2611.26897),
listed Mon 2026-11-23 on the cs.CL recent-submissions page. The summarized
claims (the 22-configuration/10-benchmark scale, the 1,244-failure and
536-description counts, the 90.0%/83.3% human-validation figures) are taken
directly from the arXiv-published abstract text. No independent
corroboration sought beyond the authors' own reported human evaluation.

## Updates

None yet.

## Related entries

None yet.
