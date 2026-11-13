---
slug: 2026-sahni-rasoi-visual-diffs-coding-agents
title: "Rasoi: Visual Diffs for Evaluating Structural Changes Made by Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.16293
canonical_ids: ["arxiv:2611.16293"]
publisher_or_author: "Riya Sahni, Aryan Kaul, Anushka Bhatnagar, Xuanming Zhang, Vivian Liu, Reya Vir, Lydia B. Chilton — arXiv preprint"
published: 2026-11-12
captured: 2026-11-13
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 5 (observability and debugging) and lens 7 (AI-assisted
  software development): a transferable, field-tested technique (visual
  architecture diffs across abstraction levels) for a named, concrete
  problem — surface-correct coding-agent edits that hide structural drift —
  validated with a week-long multi-developer deployment, not just a demo.
---

# Rasoi: Visual Diffs for Evaluating Structural Changes Made by Coding Agents

## Summary
Addresses a named failure mode in coding-agent oversight: large agent edits
can look correct at the code level while duplicating logic, touching
out-of-scope modules, removing functionality, or causing broader
architectural drift that line-level diffs don't surface. Rasoi is a design
probe that generates visual diffs of a codebase's *architecture* — which
elements and relationships were added, modified, or removed — at multiple
levels of abstraction, rather than diffing code text. The authors deployed
it for one week with 12 developers working on their own codebases across
varied technical domains (deployment methodology and data-collection
details not given in the fetched abstract — unverified beyond it). Their
conclusion: oversight tooling is most valuable when it helps developers
confidently *evaluate* an agent's changes — whether they stayed in scope,
whether unexpected restructuring occurred, how a modified part fits the
whole — rather than when it simply tries to build trust in the agent.

## Why it matters
Names a concrete, transferable technique — architecture-level visual
diffing, not code-level diffing — for a failure mode (surface-correct but
structurally drifted agent edits) that line-by-line code review misses;
directly applicable to anyone building review or oversight tooling around
coding agents, and backed by a real multi-developer field deployment rather
than a lab demo.

## Verification notes
arXiv abstract page fetched directly (2026-11-13); full author list and
"Submitted on 12 Nov 2026" at 04:47:39 UTC confirmed, primary category
cs.SE cross-listed to cs.HC. The named failure mode, the architecture-level
visual-diff approach, the one-week/12-developer deployment, and the
stated conclusion (tooling value lies in supporting developer judgment, not
building agent trust) all trace directly to the fetched abstract text. The
deployment's specific data-collection and analysis methods are not
described in the abstract and are marked unverified above; full paper not
read at capture.

## Updates
None yet.

## Related entries
None yet.
