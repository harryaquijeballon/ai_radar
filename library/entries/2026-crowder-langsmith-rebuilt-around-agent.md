---
slug: 2026-crowder-langsmith-rebuilt-around-agent
title: "We Rebuilt LangSmith Around the Agent"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://www.langchain.com/blog/we-rebuilt-langsmith-around-the-agent
canonical_ids: []
publisher_or_author: "Sam Crowder — LangChain blog"
published: 2026-11-16
captured: 2026-11-17
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 5 (observability and debugging): names a transferable
  design principle — give every agent a single immutable identity record
  that traces, evals, deployments, and governance all attach to, rather
  than a flat per-project trace hierarchy — but discounted per
  profiles/ai_engineering/sources.md for framework-vendor promotion
  (LangSmith-specific implementation).
---

# We Rebuilt LangSmith Around the Agent

## Summary
Describes a redesign of LangSmith so that the agent, not the project, is the
core object: each agent gets a single record with an owner, a globally
unique and immutable ID, and a type, to which its environments (local, dev,
staging, production), traces, evals, Agent Server deployments, and Engine
issues all connect. Previously, traces sat in a flat project hierarchy with
no link to a specific agent, so traces from the same agent running in
different environments were not associated with each other. LangChain says
the change responds to agent adoption spreading across teams building with
different frameworks, runtimes, tools, and models, which left engineers
switching between disconnected tracing/monitoring/deployment surfaces and
some teams skipping evals altogether, and left platform teams unable to
answer "which agents exist, and who owns each one?" The redesign organizes
work around four stages (build, run, improve, govern); agents on any
platform supporting OpenTelemetry Protocol (OTLP) can be registered and
measured the same way, with cost and quality metrics rolling up to a named
owner. Roadmapped: org-level dashboards (currently workspace-level) and
registering agents in identity providers for security-team audits
(unverified: adoption-driven motivation and roadmap items are the vendor's
own framing, not independently measured).

## Why it matters
Names a concrete fix for a specific agent-observability failure mode —
traces, evals, and deployments becoming disconnected once an agent runs in
multiple environments or frameworks — by giving the agent a single
immutable identity record everything else attaches to; the underlying
principle (agent identity as the join key, not project or trace ID) is
transferable to any observability stack even where the specific
implementation (LangSmith, OTLP-based registration) is not.

## Verification notes
Fetched and read in full from the primary source (langchain.com/blog);
author (Sam Crowder), 2026-11-16 publish date, and the described redesign
(agent-centric record, OTLP-based cross-framework registration, four-stage
lifecycle, roadmap items) trace directly to the fetched post text. This is
a first-party product-design announcement with no external benchmark
claimed, so no load-bearing statistic required independent corroboration;
discounted for vendor promotion per the ai_engineering sources profile.

## Updates
None yet.

## Related entries
None yet.
