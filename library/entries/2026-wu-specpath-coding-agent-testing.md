---
slug: 2026-wu-specpath-coding-agent-testing
title: "SpecPath: Testing Coding Agents Across Contract-Equivalent Specification Histories"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.09799
canonical_ids: ["arxiv:2608.09799"]
publisher_or_author: "Yangfan Wu, Haozhe Wang, Huanyu Yang, Jianmin Ji, Fangzhen Lin — arXiv preprint (cs.SE)"
published: 2026-08-10
captured: 2026-08-11
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation and validation): identifies and quantifies a
  distinct coding-agent failure mode — "specification-path sensitivity" —
  showing that success on a consolidated specification does not guarantee
  robustness to how that specification was reached, directly actionable for
  teams evaluating agent reliability before production use.
---

# SpecPath: Testing Coding Agents Across Contract-Equivalent Specification Histories

## Summary
The paper defines "specification-path sensitivity": the failure mode where a coding agent, given requirement histories that are logically equivalent (same final contract, different revision paths), produces different program outcomes. The authors introduce SpecPath, an evaluation framework that holds the repository, final contract, verifier, agent, and execution budget constant while varying only the revision path to the final specification, then compares paired outcomes rather than scoring each patch in isolation. Across five calibrated software tasks and fourteen coding-agent configurations, aggregate accuracy (direct vs. revision-history) barely changes — but 35 of 100 complete blocks that succeed on the direct specification fail on at least one equivalent history.

## Why it matters
A directly reusable diagnostic: teams relying on coding agents for research or policy-product engineering can adopt SpecPath's paired-history testing to check whether an agent's apparent reliability is an artifact of how requirements were presented, rather than genuine robustness — the 35% divergence rate shows aggregate accuracy alone would have hidden this failure mode entirely.

## Verification notes
Read via the arXiv abstract page. The headline 35/100 figure and the "aggregate accuracy is stable, paired outcomes are not" claim are quoted/paraphrased directly from the abstract; not independently corroborated against a second source, consistent with a same-day single-preprint read.

## Updates
None yet.

## Related entries
None yet.
