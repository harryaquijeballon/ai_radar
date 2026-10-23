---
slug: 2026-metr-redteam-openai-agent-monitoring
title: "Red-Teaming OpenAI's Internal Agent Monitoring Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://metr.org/blog/2026-10-22-red-teaming-openai-agent-monitoring/
canonical_ids: []
publisher_or_author: "METR (with Redwood Research; contributors David Rein, Adam Kaufman)"
published: 2026-10-22
captured: 2026-10-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation/guardrails) and lens 6 (reproducibility,
  security and governance): an independent evaluator's hands-on, three-week
  red-team of a frontier lab's production agent-monitoring system, naming
  concrete, specific vulnerabilities (coverage gaps, a compaction blind
  spot, a trigger-timing gap, sandbox/review bypasses) and actionable
  design principles for monitoring long-horizon agents. METR is the
  profile's named counterweight to vendor-reported benchmarks.
---

# Red-Teaming OpenAI's Internal Agent Monitoring Systems

## Summary
METR, with a Redwood Research collaborator, ran a three-week pilot stress
test (21 Jul – 11 Aug 2026) of OpenAI's internal misalignment-monitoring
system, assessing the system as it existed on and before 21 July 2026. The
testers had deep access — OpenAI's internal codebase, monitor prompts and
configuration, internal documentation — and interviewed about a dozen
researchers and engineers from the monitoring, safety-systems, and security
teams, working on-premises on OpenAI-issued devices. The full output was a
61-page internal report; a 38-page redacted version went to METR and
Redwood leadership.

Findings include: coverage gaps (roughly 75–94% of agentic Responses API
traffic from models at least as strong as GPT-5.5 was eligible for
monitoring, with substantial uncertainty; RL training runs were not covered
at the start of the exercise); a compaction blind spot (not monitoring
compaction events likely left ~10% of eligible internal Codex traffic
unmonitored from May–July 2026, fixed during the exercise); a trigger-timing
gap (the monitor ran only when agents returned control to the user, so
agents could postpone monitoring by continuing to act); a sandbox/Auto-Review
bypass found for Codex agents; a monitoring-evasion exploit that could keep
recent actions — including the exploit itself — from being monitored; two
client-controllable headers that could disable monitoring for new agents;
and two internal tools believed read-only that were in fact unmonitored,
with a possible escape identified but not validated. On the positive side,
the monitor saw nearly the full trajectory agents saw, and its prompts
targeted scheming, sabotage, exfiltration, deception, and prompt injection.
OpenAI states all vulnerabilities affecting production safeguards have been
patched and coverage expanded; METR notes it has not evaluated these claims.

## Why it matters
This is a rare, independently-conducted, hands-on red-team of a frontier
lab's actual production agent-monitoring infrastructure rather than a
paper-based proposal — directly useful for any team building or relying on
agent-monitoring/guardrail systems (lens 4/6, the profile's core
policy-simulation-adjacent concern). The design principles METR draws out —
monitoring should be hard to evade, should verify that intended traffic is
actually covered, should respond to incidents quickly, should be
continually red-teamed, and should stay isolated from the agents it
watches — are directly transferable checklist items for any reliability
engineer designing an oversight layer around agentic systems.

## Verification notes
Read directly from metr.org. Publication date (22 Oct 2026), methodology
(three-week window, dates, access level, interview count, report page
counts), and all named vulnerabilities and quantified figures (75–94%
coverage, ~10% compaction gap, two bypass headers) are stated directly in
the post and traceable to it. As the publishing organization's own
first-party account of its own red-team exercise, no further independent
corroboration was attempted this run; METR's standing as an independent
evaluator (per profiles/ai_engineering/sources.md) and the specificity of
the findings support `verified`.

## Updates

- None yet.

## Related entries
None yet.
