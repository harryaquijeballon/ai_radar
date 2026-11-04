---
slug: 2026-huang-how-agent-skills-evolve
title: "How Agent Skills Evolve: A Large-Scale Empirical Study of Skills on GitHub"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.04456
canonical_ids: ["arxiv:2611.04456"]
publisher_or_author: "Jinjun Huang, Jialun Cao, Junxiao Han, Zhonghao Jiang, Shing-Chi Cheung, Zhongxin Liu"
published: 2026-11-03
captured: 2026-11-04
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on harness/context engineering and AI-assisted software development
  (lenses 2, 7): a large-scale (84,200 skills, 750,898 commits) empirical
  study of how agent skills actually change over time in real repositories,
  yielding five concrete, named implications directly relevant to this
  project's own use of agent skills.
verification: verified
---

# How Agent Skills Evolve: A Large-Scale Empirical Study of Skills on GitHub

## Summary

Studies how "agent skills" — reusable packages of task-specific knowledge
that let LLM-based agents avoid retraining — evolve in real GitHub
repositories, arguing prior work has only examined skills statically. The
authors collected 84,200 skills and 750,898 commits, manually built
taxonomies of skill components, change patterns, and evolution motivations,
then built an automated pipeline to label changes at scale, combining
quantitative measures with qualitative assessment. Five implications are
reported: (1) reliability receives comparatively little attention in skill
composition and change, motivating execution-contract designs with
verification and recovery; (2) evolution concentrates in project-coupled
skills, calling for automated just-in-time updating; (3) changes are
dominated by incremental enrichment and refinement, motivating
pattern-guided tools that diagnose incomplete components; (4) redundancy is
a practical maintenance problem, calling for more context-efficient skill
representations; (5) security-motivated changes show limited measured risk
reduction, suggesting regression testing that objectively checks both
functionality and security.

## Why it matters

A grounded, large-N empirical basis — rather than anecdote — for how agent
skills (the mechanism this project's own `.claude/skills/` directory and
engine rely on) actually get maintained and drift over time in practice.
The five implications translate directly into engineering choices: treat
skill changes as needing verification/recovery contracts, expect
project-coupled skills to need more frequent updates, watch for redundant or
duplicated skill content as a maintenance cost, and don't assume a
security-motivated edit measurably reduced risk without checking.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-03). The dataset size, the taxonomy-plus-automated-pipeline
methodology, and all five numbered implications trace to the abstract text.
Full paper (taxonomy definitions, per-implication supporting statistics) not
read at capture.

## Updates

None yet.

## Related entries

None yet.
