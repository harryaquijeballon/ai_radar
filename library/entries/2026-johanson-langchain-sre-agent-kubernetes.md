---
slug: 2026-johanson-langchain-sre-agent-kubernetes
title: "How We Build an Autonomous SRE Agent for Kubernetes Deployments"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://langchain.com/blog/how-we-build-an-autonomous-sre-agent-for-kubernetes-deployments
canonical_ids: []
publisher_or_author: "Eric Johanson — LangChain blog"
published: 2026-08-05
captured: 2026-08-06
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Medium on agent architecture/orchestration and observability: a concrete
  production case study of subagent specialization, a hard read/write
  boundary gated by human-in-the-loop approval, and trace-driven cost
  iteration, discounted per the sources list's explicit framework-promotion
  caveat for LangChain/LlamaIndex blog posts (lenses 1, 3, 5).
---

# How We Build an Autonomous SRE Agent for Kubernetes Deployments

## Summary

LangChain describes a production multi-agent SRE system for Kubernetes. An
orchestrator (running on Claude Sonnet, "where it thinks") delegates to
specialized, parallel read-only subagents — pod-inspector, scaling-analyzer,
performance-analyzer, log-analyzer, security-auditor, reliability-auditor —
running on Claude Haiku ("for scale"), reflecting a stated strategy to "pay
for intelligence only where it's needed." Read and write tools live in
separate modules; every write (scaling a deployment, restarting a rollout,
patching an HPA) is confined to a single change-executor subagent gated by a
human-in-the-loop interrupt requiring Slack approval before execution. A
lightweight scheduled health check was redesigned to use a single Haiku call
over plain-Python-collected state instead of roughly 20 model calls,
reported as a 95-99% cost cut per check. LangSmith traces capture all
operations, used for cost analysis, pattern detection, and turning labeled
human HITL decisions into a regression test dataset.

## Why it matters

A concrete architectural pattern for anyone building agent systems that can
take real, consequential actions: narrow, parallel, cheap-model subagents
for read-only analysis; a single, expensive-model orchestrator for
synthesis; and a structurally enforced (not just prompted) separation
between anything that reads and the one narrow path that writes, gated by
human approval. The trace-driven iteration loop — using observed cost and
failure patterns, plus labeled HITL decisions, to build a regression test
set — is a transferable practice for hardening an agentic system over time.

## Verification notes

Blog post fetched directly (2026-08-06); title, author, "August 5, 2026"
publication date, the orchestrator/subagent model split, the read/write
module separation, the change-executor HITL gate, the "95 to 99% cost cut
per check" figure, and the LangSmith-tracing account all trace directly to
the fetched article text. `partial` rather than `verified`: the cost and
architecture figures are LangChain's own self-reported account of an
internal (or customer) system, not independently corroborated, consistent
with this project's existing discount for LangChain/LlamaIndex
framework-promotion content (`profiles/ai_engineering/sources.md`) and
matching the verification level recorded for the same source's earlier
"Agent-First Data Stack" post.

## Updates

None yet.

## Related entries

[2026-hawkins-langchain-agent-data-stack](2026-hawkins-langchain-agent-data-stack.md) — same source and pattern of self-reported, partially-verified LangChain practitioner case study.
