---
slug: 2026-gosmar-agent-status-protocol
title: "Agent Status Protocol (ASP): A Lightweight Specification for State Reporting in Multi-Agent Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.21538
canonical_ids: ["arxiv:2610.21538"]
publisher_or_author: "Diego Gosmar, Deborah A. Dahl, Emmett Coin, Csaba Bolyós, Andreas Zettl — arXiv preprint"
published: 2026-10-15
captured: 2026-10-17
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Medium on tool use/interoperability and observability (lenses 3, 5): a
  working-draft (v0.1) protocol for heterogeneous agents to report state to a
  shared status server, deliberately reusing existing vocabularies (A2A task
  states, Open Floor Protocol floor states, OpenTelemetry GenAI semantic
  conventions). Actionable as a named interoperability pattern, but
  unvalidated — no adoption or evaluation evidence yet, by the authors' own
  framing.
---

# Agent Status Protocol (ASP): A Lightweight Specification for State Reporting in Multi-Agent Systems

## Summary

Per the arXiv abstract page (v1 submitted 15 Oct 2026, CC BY 4.0), the paper proposes ASP, a lightweight mechanism for heterogeneous AI agents to report operational state to a status server: agents send small JSON events over HTTP POST, and the server exposes aggregated state to observers (e.g. dashboards) over Server-Sent Events. Because a crashed, hung, or compromised agent cannot be trusted to self-report failure, the server also infers liveness from missed heartbeats, detects agents that are running but not making progress, and accepts corroborating or overriding observations from supervisors, guardrails, operators, and peer agents. State is tracked along independent dimensions — lifecycle, health, task, floor, and governance — so an agent can, for example, be simultaneously online-and-degraded, mid-task, and waiting for the conversational floor. The spec deliberately reuses existing vocabularies rather than inventing new ones: task states from the Agent2Agent (A2A) protocol, floor states from the Open Floor Protocol, and attribute conventions from OpenTelemetry's GenAI semantic conventions. The authors present this as version 0.1, an explicit working draft for discussion rather than an approved standard, and invite alternative proposals and independent implementations. No experimental results, benchmarks, or adoption evidence are given in the abstract-level material reviewed.

## Why it matters

A concrete, composable building block for observability and failure-detection in production multi-agent systems — the explicit design choice to not trust an agent's own self-report, and to let supervisors/guardrails/peers override it, is a directly applicable pattern independent of whether this specific spec is ever adopted. Worth tracking as an early, vendor-neutral entrant in a space (agent status/health reporting) that currently has no interoperability standard, alongside MCP (tool use) and A2A (task delegation).

## Verification notes

Source reachable (arXiv abstract page). Claims traced to the abstract-level summary only; the full 30-page spec was not opened, so the exact message schemas and the claimed reuse of A2A/Open Floor Protocol/OpenTelemetry conventions were not independently checked against those underlying specs. No quantified claims are made at this level, so there is nothing load-bearing left unverified beyond the architecture description itself.

## Updates

None yet.

## Related entries

None yet.
