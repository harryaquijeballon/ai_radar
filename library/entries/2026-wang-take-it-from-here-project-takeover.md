---
slug: 2026-wang-take-it-from-here-project-takeover
title: "Take It From Here: Evaluating Coding Agents On Project Takeover"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07307
canonical_ids: ["arxiv:2611.07307"]
publisher_or_author: "Dingxian Wang, Zhe Fu, Jiaqi Deng, Chao Yin, Ganesh Prabhu, Karthik Gomadam Rajagopal, Darwin Yi, Huan Huo, Guandong Xu, Xianzhi Wang, Andrew Rabinovich, Zhao Chen"
published: 2026-11-05
captured: 2026-11-06
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 7 (AI-assisted software development) and lens 2 (harness/
  context engineering): a new benchmark (ReqMemBench) and a stark
  quantified failure rate for the realistic, under-studied task of a
  coding agent inheriting someone else's long-running project, with a
  diagnostic (requirement atoms) that isolates where the failure happens.
---

# Take It From Here: Evaluating Coding Agents On Project Takeover

## Summary

The paper studies whether coding agents can take over a long-running
software project: recover which requirements from the interaction history
still apply, then correctly implement a new request on top of them. The
authors evaluate this with delivery tests and introduce "requirement
atoms" to diagnose specifically where an agent's recovered requirement
state goes wrong, combined into a new benchmark, ReqMemBench. With the
full interaction history supplied as context ("Full History" baseline),
the mean complete-delivery rate across six model-harness configurations
and 37 executable-validation targets was 4.95%. None of the six
configurations produced a fully correct post-request requirement state;
agents frequently dropped previously recovered constraints when updating
them. Even when the authors supplied the correct target requirement state
directly (removing the recovery step entirely), the mean complete-delivery
rate rose only to 8.11% — build passed 96.40% of the time and regression
tests passed 90.99%, but target-test success (correctly implementing the
new request itself) was only 9.01%.

## Why it matters

Project takeover — picking up someone else's half-finished, long-running
codebase and correctly continuing it — is close to the default situation
for any agent used on a real research or policy codebase over time, yet
this paper shows current agents fail at it far more severely than
headline SWE-bench-style numbers suggest. The decomposition is the
actionable part: even with the correct target state handed to the agent
(no recovery needed), implementation success is still only ~9% — meaning
the dominant failure mode is not "losing track of requirements" so much as
"failing to implement a given requirement correctly in an existing
codebase," which is a different, narrower engineering problem to solve
than better context/memory alone.

## Verification notes

Read the abstract and submission metadata directly on arXiv (v1, 5 Nov
2026, cs.SE cross-listed cs.MA). All quantified figures above (4.95%,
8.11%, 96.40%, 90.99%, 9.01%) are stated directly in the abstract and
traced to it. The specific six model-harness configurations and the 37
validation targets were not independently inspected beyond what the
abstract states.

## Updates

None yet.

## Related entries

None yet.
