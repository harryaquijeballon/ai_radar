---
slug: 2026-lazer-agentic-authorization-trust-boundaries
title: "Evaluating Authorization and Trust Boundaries in Agentic Orchestration Frameworks"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.21259
canonical_ids: ["arxiv:2611.21259"]
publisher_or_author: "Sahaya Jestus Lazer, Kshitiz Aryal, Maanak Gupta, Elisa Bertino — arXiv preprint"
published: 2026-11-16
captured: 2026-11-17
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 3 (tool use and MCP) and lens 6 (reproducibility, security and
  governance): runs twelve concrete experiments mapped to the OWASP Top 10
  for Agentic Applications across four production orchestration frameworks
  (LangChain, LangGraph, AutoGen, OpenClaw), directly actionable for anyone
  choosing or hardening a tool-permission model for an agentic system.
---

# Evaluating Authorization and Trust Boundaries in Agentic Orchestration Frameworks

## Summary
Examines security risks at the boundaries where agentic AI systems
orchestrate tools, memory, and multiple agents, evaluating four widely used
orchestration frameworks — LangChain, LangGraph, AutoGen, and OpenClaw —
with a common underlying model (gpt-4o-mini). The authors ran twelve
experiments mapped to the OWASP Top 10 for Agentic Applications, covering
prompt injection, unauthorized resource access and command execution, memory
poisoning, and inter-agent trust and identity attacks. They report that
adversarial inputs caused unauthorized tool invocation; that tool chaining,
stale filesystem validation, encoded instructions, and inter-agent
delegation exposed authorization gaps across component boundaries; and that
memory poisoning let untrusted state influence responses in a way the
authors treat as distinct from conventional access-control violations. In
protected configurations, explicit authorization, controlled capability
assignment, filesystem containment, and execution safeguards prevented
specific unauthorized operations. The paper concludes that framework
features and model-level instructions alone should not be treated as
sufficient security guarantees (unverified: the fetched page gave no
numerical success/failure rates for the twelve experiments, only qualitative
findings — full paper not read at capture).

## Why it matters
Gives a builder evaluating or hardening an agentic orchestration stack a
concrete, cross-framework test set (the OWASP Top 10 for Agentic
Applications, operationalized as twelve experiments) rather than a general
warning, and a specific finding to act on: authorization checks implemented
by the framework or encoded in model instructions are not sufficient on
their own, so capability assignment, filesystem containment, and execution
safeguards need independent enforcement regardless of which orchestration
framework is in use.

## Verification notes
arXiv abstract/page fetched directly (2026-11-17); title, authors, and
"Submitted on 16 Nov 2026" confirmed. The frameworks evaluated (LangChain,
LangGraph, AutoGen, OpenClaw), the common model (gpt-4o-mini), the
twelve-experiment design mapped to the OWASP Top 10 for Agentic
Applications, and the qualitative findings (unauthorized tool invocation,
authorization gaps at tool-chaining/filesystem-validation/delegation
boundaries, memory poisoning as a distinct risk class, and mitigations that
worked in protected configurations) all trace directly to the fetched page
text. No numerical results were visible in the fetched content, so no
load-bearing quantitative claim required independent corroboration; the
qualitative findings are the source's own reported results, not
corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
