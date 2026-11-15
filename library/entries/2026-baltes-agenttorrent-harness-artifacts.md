---
slug: 2026-baltes-agenttorrent-harness-artifacts
title: "AgentTorrent: A Dataset of Context and Harness Engineering Artifacts on GitHub"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.15436
canonical_ids: ["arxiv:2611.15436"]
publisher_or_author: "Sebastian Baltes, Seyedmoein Mohsenimofidi, Levi Böhme, Vahram Nersesyan, Muhammad Auwal Abubakar, Jai Lal Lulla, Matthias Galster, Christoph Treude — arXiv preprint (cs.SE)"
published: 2026-11-11
captured: 2026-11-15
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Lens 2 (harness and context engineering): a large, reusable dataset and
  update pipeline linking agent context/harness artifacts (CLAUDE.md-style
  files, skills, hooks, MCP configs, specs) to the commits and repositories
  that use them — a resource a builder could study or build on, medium
  because it is a dataset release rather than a validated pattern itself.
---

# AgentTorrent: A Dataset of Context and Harness Engineering Artifacts on GitHub

## Summary
AgentTorrent is a dataset of files developers commit to GitHub to guide
and configure agentic coding tools — context files, skills, hooks, MCP
configurations, and planning documents such as specs and task files. The
authors release both the dataset and the collection pipeline, which
supports regular updates and checks vendor documentation for previously
unknown artifact types and tools.

Reported scale: six agentic coding tools covered (proprietary and
open-source), 10,944 engineered software projects on GitHub, 62,374
configuration artifacts, 27,593 agentic planning documents, more than 1.2
million commits that credit an AI tool, and 388 repositories where
configuration artifacts, planning documents, and AI-credited commits all
co-occur. Detection heuristics are grounded in tool documentation or
derived from repository inspection, with accuracy evaluated at each
collection run; open-weight models are used to classify whether a
repository hosts an engineered software project. The authors note the
dataset supports research questions such as whether a tool is credited in
commits that add instructions for that same tool, and how instruction
files import from or contradict one another (unverified beyond the
abstract: no such analysis result itself is reported here, only that the
dataset enables it).

## Why it matters
A directly reusable resource for anyone studying how teams actually
configure coding-agent harnesses in the wild (lens 2) — at a scale
(over 10,000 projects, over a million AI-credited commits) that individual
researchers could not easily assemble themselves, with an update pipeline
rather than a one-off snapshot.

## Verification notes
Fetched the arXiv abstract page directly; the scale figures and dataset
description above trace to that text. The dataset itself (on Zenodo) and
the paper's detection-accuracy evaluation were not independently fetched
or checked in this session — verification is partial.

## Updates
None yet.

## Related entries
None yet.
