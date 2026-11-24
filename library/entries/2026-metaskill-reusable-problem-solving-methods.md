---
slug: 2026-metaskill-reusable-problem-solving-methods
title: "MetaSkill: Reusable Problem-Solving Methods for Adaptive Skill Orchestration in LLM Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.29274
canonical_ids: ["arxiv:2611.29274"]
publisher_or_author: "Wang et al."
published: 2026-11-24
captured: 2026-11-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Lens 2 (harness and context engineering): a two-layer orchestration
  framework (method selection plus execution/repair) with quantified gains
  over strong baselines and an ablation isolating the mechanism's actual
  contribution — a named, comparable pattern for designing skill-reuse
  architectures.
---

# MetaSkill: Reusable Problem-Solving Methods for Adaptive Skill Orchestration in LLM Agents

## Summary

LLM agents increasingly have reusable skills available, but still need to decide how to organize and adapt them across tasks. MetaSkill is a two-layer framework for reusing problem-solving methods: a method layer chooses one of 26 curated methods and assigns abstract roles to task objects, and an execution layer applies the chosen method by identifying intermediate goals, coordinating the agent's native skills, and handling repairs or switching to a different method when the current one fails. On 89 SkillsBench tasks and 995 ToolHop examples, MetaSkill outperforms baselines in all six tested configurations, with accuracy gains of 3.51 to 13.48 percentage points over the strongest baseline. Ablations show that explicit method-guided orchestration outperforms simply injecting method descriptions into the prompt, and that allowing the agent to reselect methods mid-task adds further gains.

## Why it matters

A named, benchmarked architecture for the increasingly common problem of orchestrating many reusable agent skills/methods rather than hard-coding a single workflow — the ablation result (explicit orchestration beats prompt-injected method text) is a specific, actionable design choice for anyone building a skill-library-backed agent system.

## Verification notes

Fetched directly from arXiv; abstract and metadata confirmed (v1 submitted 22 November 2026, within the discovery window; primary category cs.AI, cross-listed cs.SE). All figures above are as stated in the abstract. The 26-method taxonomy and the execution-layer repair mechanism were not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

None yet.
