---
slug: 2026-chen-vce-skill-version-change-experience
title: "VCE-Skill: Enhancing Skill Self-Evolution with Version-Change Experience"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.16544
canonical_ids: ["arxiv:2608.16544"]
publisher_or_author: "Jianming Chen, Xuanbin Ye, Yawen Wang, Junjie Wang, Qing Wang, Fanjiang Xu"
published: 2026-08-17
captured: 2026-08-18
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On lens 2 (skill/harness engineering): a method for evolving reusable
  agent skills that combines public skill-version history with
  task-trajectory evidence, with quantified gains and cross-model transfer
  — a usable idea for teams maintaining a shared skill library.
---

# VCE-Skill: Enhancing Skill Self-Evolution with Version-Change Experience

## Summary

The paper addresses how agents improve reusable skills over time. Existing
methods revise skills based only on execution trajectories from the
immediate task; the authors argue "public skill changes provide reusable
evolution priors, whereas trajectories provide evidence grounded in the
current task." VCE-Skill converts noisy public skill version histories into
structured, reusable patterns and merges these with trajectory-based
suggestions. Reported results: 3.20-4.98 point improvements in mean scores,
with improved cross-model transfer performance for the evolved skills
(unverified in detail — benchmark suite and score metric not read beyond
the abstract).

## Why it matters

As skill libraries (in the Claude Skills / agent-skill sense) become a
shared engineering artifact across teams and model versions, treating the
*history* of how a skill has been edited as a training signal — not just
what happened in one task run — is a concrete, checkable idea for anyone
maintaining a skill library that evolves over time and across models.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The method
description (combining public version-change priors with trajectory
evidence) and the 3.20-4.98 point improvement figures are traced to the
abstract. Benchmark identity, scoring metric definition, and the
cross-model transfer protocol were not independently corroborated — hence
partial verification.

## Updates

- **2026-08-18** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
