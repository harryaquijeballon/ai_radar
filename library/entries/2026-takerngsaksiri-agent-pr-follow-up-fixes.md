---
slug: 2026-takerngsaksiri-agent-pr-follow-up-fixes
title: "Who Finishes the Job? A Study of Follow-Up Fixes and Commit Authorship on AI Coding Agent Pull Requests"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2609.26847
canonical_ids: ["arxiv:2609.26847"]
publisher_or_author: "Wannita Takerngsaksiri, Nhat Duong, Scott Barnett — arXiv preprint (cs.SE)"
published: 2026-09-22
captured: 2026-09-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 7 (AI-assisted software development): a large-scale (6,774
  merged agent PRs vs. a 5,044-PR human baseline, five agents) measured
  comparison of post-merge fix rates and who authors the fixes, verified
  against human annotation with a human-level-agreement LLM judge (Cohen's
  Kappa 0.78 vs. human-human 0.77) — exactly the "measured results or
  transferable practices" standard the lens calls for.
---

# Who Finishes the Job? A Study of Follow-Up Fixes and Commit Authorship on AI Coding Agent Pull Requests

## Summary

The authors follow 6,774 merged agent pull requests across five AI coding
agents (OpenAI Codex, GitHub Copilot, Devin, Cursor, and Claude Code) from
the AIDev-pop dataset (open-source repositories with at least 500 stars)
into their follow-up fixes, against a baseline of 5,044 contemporaneous
human PRs from the same repositories. Every candidate fix was verified by
human annotators and an LLM judge matching human-level agreement (binary
Cohen's Kappa 0.78 vs. a human-human 0.77, direct-fix precision 90%), with
fixing work attributed at the PR and commit level. Findings, quoted
directly: "(1) merged agent PRs attract verified fixes at 1.62 times the
odds of merged human PRs in the same repositories over the same period of
time; (2) 69.6% of verified fixes in agent merges come from the same agent;
and (3) 76.4% of the verified fix PRs are agent-authored throughout all
commits." The authors conclude agents "currently largely finish their own
job, but their merges still require fixing more often than human merges."

## Why it matters

Teams treating a merged agent PR as finished work should budget for a higher
follow-up-fix rate than for human-authored merges — a concrete, measured
multiplier (1.62x) rather than an anecdotal caution. The finding that most
fixes are agent-authored (not human rework) also reframes what "reviewing
agent output" should mean in practice: the near-term risk is fix latency and
verification overhead, not silent human absorption of agent debt.

## Verification notes

Fetched directly from the arXiv abstract page (2609.26847; v1 submitted
2026-09-22 07:22:44 UTC). The dataset scale, baseline, verification
methodology (human annotators plus an LLM judge, with reported Cohen's Kappa
figures), and all three headline findings trace directly to the abstract's
own quoted text. Full paper (per-agent breakdowns, fix-latency data) not
read at capture.

## Updates

None yet.

## Related entries

None yet.
