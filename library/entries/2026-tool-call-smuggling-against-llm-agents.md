---
slug: 2026-tool-call-smuggling-against-llm-agents
title: "Oops!... I Parsed It Again: Tool-Call Smuggling Against LLM Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.30624
canonical_ids: ["arxiv:2611.30624"]
publisher_or_author: "Santos-Grueiro et al."
published: 2026-11-24
captured: 2026-11-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Lens 3 (tool use and MCP) and lens 6 (security): names and demonstrates a
  new attack class ("tool-call smuggling") arising from differential JSON
  parsing across an agent's guard/executor pipeline, with a quantified,
  reportedly complete defense — directly actionable for anyone building or
  auditing agent tool-permission systems.
---

# Oops!... I Parsed It Again: Tool-Call Smuggling Against LLM Agents

## Summary

The authors study how LLM agents execute tool calls: a model writes a call's arguments as JSON, a guard decides whether the call may run, and an executor runs it. Because the same bytes get parsed independently by several components (provider, gateways, SDKs, frameworks, guard, executor) and JSON leaves some parsing details open (e.g., which duplicate key counts), a guard can approve one call while the executor runs a different one — and the audit log records only the approved call. The authors name this "tool-call smuggling," describe six ways identical bytes can yield different calls, and build a differential-testing harness across 17 parser/validator configurations, finding most pairs disagree on some input — even two official MCP SDKs accept different inputs on the same bytes.

In tasks from τ-bench and AgentDojo, an attacker able to rewrite traffic cancels another customer's reservation and creates a file the guard would have blocked, while the audit log shows only the approved call. Ten tested models did not write disguised keys directly into tool-call arguments, but did copy such keys verbatim into JSON strings nested inside arguments, which a Python guard and a Go executor parsed differently. A malicious MCP server that copied a legitimate tool's public schema and added one extra field got the model to fill that field with user data, unseen by the guard. The proposed defense parses each call exactly once — including embedded JSON text — keeps only fields present in the approved schema, and passes the sealed result (with its call ID) to the executor. The authors report this stops all 7,412 crafted inputs and every attack they built.

## Why it matters

Names a previously unnamed, concretely demonstrated class of agent tool-permission bypass that is purely a parsing-consistency problem, not a model-alignment one — directly relevant to anyone operating an agent harness with a separate guard and executor (the standard pattern for tool permissioning), with both the attack harness (17 parser configurations) and a defense (single-parse, schema-filtered, sealed call) reported as measurably effective.

## Verification notes

Fetched directly from arXiv; abstract and metadata confirmed (v1 submitted 23 November 2026, within the discovery window; primary category cs.CR, cross-listed cs.AI/cs.SE). All figures above are as stated in the abstract. The differential-testing harness design and the τ-bench/AgentDojo attack demonstrations were not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

None yet.
