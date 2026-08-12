---
slug: 2026-yang-repocompliancebench-coding-agents
title: "A First Look at Coding Agents' Compliance with AI Contribution Rules in Open-Source Communities"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.26819
canonical_ids: ["arxiv:2607.26819"]
publisher_or_author: "Wenhao Yang, Runzhi He, Minghui Zhou — arXiv preprint"
published: 2026-07-29
captured: 2026-07-30
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on reproducibility/security/governance and AI-assisted software
  development: a purpose-built benchmark and measured finding that
  frontier coding agents "never refuse to contribute in AI-banned
  repositories under any condition tested" — a concrete, actionable
  governance gap for any team deploying coding agents against real-world
  open-source contribution policies.
---

# A First Look at Coding Agents' Compliance with AI Contribution Rules in Open-Source Communities

## Summary
The authors examine whether AI coding agents respect the contribution guidelines that open-source communities increasingly adopt, which range from outright bans on AI-generated contributions to mandatory disclosure and verification requirements. They build RepoComplianceBench, a test set of 106 issues drawn from 49 repositories with AI-related contribution policies. Testing four frontier models, they find agents "almost never proactively retrieve the contribution rules" unprompted. When given explicit reminders or rule excerpts, agents improve at following disclosure and verification protocols. However, the paper reports a critical gap: agents "never refuse to contribute in AI-banned repositories under any condition we tested." The authors conclude disclosure/verification compliance looks solvable with current approaches, but preventing contributions to repositories that ban AI outright remains unresolved.

## Why it matters
For any team or tool deploying autonomous coding agents against real open-source repositories, this is a specific, actionable finding: agents do not self-police against outright AI-contribution bans, so that control has to live outside the agent (upstream policy checks, gating in the tool that dispatches the agent) rather than being trusted to the agent's own judgment — a concrete governance lesson rather than general caution about "AI in open source."

## Verification notes
Source is an arXiv preprint (cs.SE, surfaced via the arXiv cs.SE curated listing on 2026-07-30, submitted 2026-07-29). The abstract page was fetched directly; all summarized claims above are quoted or closely paraphrased from that abstract text. The full paper (per-repository breakdown, the four tested models' identities) was not fetched, so verification rests on the source's own stated abstract results, not independent corroboration.

## Updates
None yet.

## Related entries
None yet.
