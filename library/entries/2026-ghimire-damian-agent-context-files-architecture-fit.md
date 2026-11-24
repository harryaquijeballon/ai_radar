---
slug: 2026-ghimire-damian-agent-context-files-architecture-fit
title: "Does the Agent's Map Match the Territory? Architectural Claims in AI Agent Context Files and Their Fit with the Code"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.29916
canonical_ids: ["arxiv:2611.29916"]
publisher_or_author: "Bachan Ghimire, Daniela Damian"
published: 2026-11-23
captured: 2026-11-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Lens 2 (harness and context engineering): a large-scale empirical audit
  (41,090 path claims, 184 dependency rules, 3,602 context files across
  3,346 projects) quantifying whether CLAUDE.md/AGENTS.md-style context
  files accurately describe the code they claim to describe — directly
  actionable for anyone maintaining such files.
---

# Does the Agent's Map Match the Territory? Architectural Claims in AI Agent Context Files and Their Fit with the Code

## Summary

Ghimire and Damian study whether architectural claims in AI coding agents' context files (CLAUDE.md, AGENTS.md, and similar) match the actual codebase. Because agents start each session without architectural knowledge, these files are meant to fill that gap, and agents treat their claims as accurate. The authors checked two kinds of verifiable claims — path claims (named folders/files) and dependency rules (allowed imports) — across 41,090 path claims and 184 dependency rules drawn from 3,602 context files in 3,346 open-source projects, validating each against the code and its commit history (using an LLM-assisted pipeline with human review at each step).

About 5% of path claims point to paths that can't be found, but only about 2.2% appear to be genuine errors — comparable to the staleness rate of READMEs (3.5%). When code moves, 61% of claims that go stale get fixed, usually in the same commit. Dependency rules fared worse: 33 of 184 (18%) were already violated by existing code at the time they were written, and nearly all stayed violated. The authors conclude context files function as reasonably reliable maps (paths) but weaker rulebooks (dependency constraints), since the rules tend to describe intended rather than actual architecture. In an exploratory analysis of 7,480 commits, agent-assisted commits introduced new rule violations about 1.8x as often as non-agent commits (0.29% vs. 0.16%), but with only 14 total violations this difference is not statistically significant and is presented only as an early signal.

## Why it matters

A concrete, quantified answer to a question every team maintaining a CLAUDE.md/AGENTS.md file should care about: these files are decent at describing where things are, but their "rules" (e.g., layering/import constraints) are frequently aspirational rather than enforced — meaning an agent trusting a dependency rule in a context file is often trusting something already false, and teams should treat such rules as unverified unless they are also checked by a linter or CI gate.

## Verification notes

Fetched directly from arXiv; abstract and metadata confirmed (v1 submitted 23 November 2026, within the discovery window). All figures above are as stated in the abstract. The paper's full methodology (LLM-assisted mining pipeline, validation against commit history) and the agent-assisted-commit sub-analysis were not independently re-derived from the full text, only the abstract.

## Updates

None yet.

## Related entries

- [2026-chakrabarti-claude-md-catastrophic-remembering](2026-chakrabarti-claude-md-catastrophic-remembering.md) — related prior work on CLAUDE.md file maintenance problems (growth/bloat rather than accuracy).
- [2026-sun-cursorrules-files-study](2026-sun-cursorrules-files-study.md) — related prior empirical study of agent-instruction files (.cursorrules) in open-source projects.
