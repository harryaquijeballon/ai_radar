---
slug: 2026-selvanayagam-ghaleb-ai-to-ai-code-reviews
title: "AI-to-AI Code Reviews of GitHub Pull Requests"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.21311
canonical_ids: ["arxiv:2608.21311"]
publisher_or_author: "Niruthiha Selvanayagam, Taher A. Ghaleb — arXiv preprint (cs.SE)"
published: 2026-08-24
captured: 2026-08-24
relevance:
  social_science: n/a
  ai_engineering: medium
rationale: >-
  Medium on lens 7 (AI-assisted software development): a large-scale
  descriptive study (248,641 AI-attributed PRs) documenting an emerging
  practice — AI coding agents reviewing other AI coding agents' pull
  requests — with quantified patterns on latency and comment focus, but
  observational rather than causal and offering no prescriptive practice
  yet.
verification: verified
---

# AI-to-AI Code Reviews of GitHub Pull Requests

## Summary

The authors study AI coding agents acting in both roles of the pull-request cycle — as PR authors and as reviewers — analyzing AI-attributed PRs and review events from the CodAI dataset. They identify 248,641 unique AI-attributed PRs that received at least one AI review: 45,269 received "cross-product" review (a different AI product reviewing the PR than authored it), 208,145 received "same-product" review, and 4,773 received both. Cross-product review occurs in roughly 1.6% of identified agent-authored PRs but its volume increased by more than two orders of magnitude from 2025-Q1 to 2025-Q3. Review focus differs by tool: CodeRabbit labeled 35.0% of Claude Code-authored PR comments as refactor comments versus 10.5% for Copilot-authored PRs. Dual-role reviewers (agents that both author and review) leave 58–65% more comments per PR in same-product configurations. Median review latency is 1.2 minutes for cross-product pairs and 4.7 minutes for same-product pairs.

## Why it matters

Documents a specific, measurable emerging practice — agents reviewing other agents' code, sometimes across vendors — that teams adopting AI-assisted development workflows (lens 7) are likely to encounter without having designed for it. The tool-specific differences in comment focus and the latency gap between cross- and same-product review are concrete data points for anyone deciding how to configure or interpret automated AI code review in a mixed-vendor pipeline, even though the study is descriptive rather than causal.

## Verification notes

Read via the arXiv abstract page, which reports the dataset scale and the latency/comment-pattern figures directly. Not independently corroborated against a second source or the full paper.

## Updates

None yet.

## Related entries

None yet.
