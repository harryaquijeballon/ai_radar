---
slug: 2026-joos-pradel-agentbouncer-syscall-mediation
title: "AgentBouncer: Defending Software Engineering Agents via Dynamic System-Call Mediation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.30621
canonical_ids: ["arxiv:2611.30621"]
publisher_or_author: "Pascal Joos, Michael Pradel"
published: 2026-11-24
captured: 2026-11-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Lens 6 (reproducibility, security, governance): a concrete runtime
  defense mechanism (LLM-arbitrated system-call mediation) with quantified
  attack-success reduction, low task-success cost, and measured
  latency/cost overhead against a named competing defense — a directly
  comparable, practically applicable security control for agent runtimes.
---

# AgentBouncer: Defending Software Engineering Agents via Dynamic System-Call Mediation

## Summary

Joos and Pradel present AgentBouncer, a runtime enforcement system that intercepts the system calls a software-engineering agent triggers through its tools and blocks unsafe ones. Its core is an LLM arbiter that scores each system call on necessity and safety for the current task; less-necessary calls must clear a higher safety-certainty bar before being allowed. Preseeded policy rules and hierarchy-aware caching reduce how often the arbiter needs to run, controlling overhead.

Tested on 340 attacks across four attack vectors plus benign issue-resolution tasks from SWE-bench Verified: attack success fell from 99.41% for an unsupervised agent to 10.59%, 18.23 to 73.53 percentage points lower than competing defenses. Only 0.25% of benign tool calls were blocked, so task success was largely preserved. Per benign task, AgentBouncer added about 47 seconds and USD 0.0036 in LLM cost; the closest existing runtime defense added 4.5x the time and 9.6x the cost.

## Why it matters

A specific, measured design for gating an agent's system-level actions that is cheap enough to run on every call and preserves benign task success almost entirely — a directly comparable baseline for anyone building or evaluating runtime defenses against agent tool misuse, with both security (attack-success rate) and cost/latency figures reported against a named competing approach.

## Verification notes

Fetched directly from arXiv; abstract and metadata confirmed (v1 submitted 23 November 2026, within the discovery window; primary category cs.CR, cross-listed cs.MA and cs.SE). All figures above are as stated in the abstract. The arbiter's policy design and the "competing defenses" baseline were not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

None yet.
