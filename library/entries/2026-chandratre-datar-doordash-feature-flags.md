---
slug: 2026-chandratre-datar-doordash-feature-flags
title: "Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.31351
canonical_ids: ["arxiv:2610.31351"]
publisher_or_author: "Atharv Chandratre, Jai Datar"
published: 2026-10-22
captured: 2026-10-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 1 (agent architecture and orchestration) and lens 7
  (AI-assisted software development): a production industrial deployment
  of a multi-agent LLM system with a quantified success rate, per-task cost,
  and time — a transferable pattern (MCP-based live-state queries + ticket
  processing + PR generation) for codebase-maintenance tasks beyond feature
  flags specifically.
---

# Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash

## Summary
DoorDash built an end-to-end, LLM-based multi-agent system to clean up
stale feature flags — rollout and kill-switch mechanisms that become
technical debt once a feature has fully rolled out. Their codebase spans
56,000+ flags across 623 repositories, with 1,659 flags stale as of May
2026; manual cleanup took roughly one to two hours per flag, and existing
rule-based tooling was insufficient to keep up. The system queries live
feature-flag rollout data through MCP, processes the corresponding Jira
tickets, and generates pull requests that remove the flag and its dead
code paths.

On a test set of 50 stale flags, the system produced engineer-approved
flag-removal pull requests for 45 of them (90%). Each cleanup averaged
$4.79 in LLM cost and 13.8 minutes of wall-clock time — roughly two orders
of magnitude faster than the manual baseline. The authors report lessons
learned for building similar systems, though the abstract does not detail
the internal agent architecture (how roles/subagents are split).

## Why it matters
This is a concrete, quantified case of a multi-agent LLM system reaching
production on a well-bounded, high-volume maintenance task, combining three
reusable elements: live system-state access via MCP, ticket-driven task
framing, and PR-based output with a human approval gate. Builders working
on similar codebase-hygiene problems (dead feature flags, deprecated config,
stale dependencies) have a directly comparable cost/time/success-rate
benchmark to design against, and the human-approval-gate pattern is
transferable to other agent-generated-PR workflows that need a defensible
audit trail.

## Verification notes
Read directly from the arXiv abstract page (arXiv:2610.31351, v1, submitted
22 Oct 2026, 14:32:23 UTC; listed in today's cs.SE new-submissions feed).
All quantified figures (56,000+ flags, 623 repositories, 1,659 stale flags,
50-flag test set, 90% success rate, $4.79 and 13.8 minutes per cleanup) are
stated directly in the abstract and traceable to it. Independent
corroboration of DoorDash's internal flag counts was not attempted; the
production deployment context and specific test-set results support
`verified` at the abstract level.

## Updates

- None yet.

## Related entries
None yet.
