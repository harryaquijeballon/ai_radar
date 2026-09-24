---
slug: 2026-kumar-agent-name-collision-a2a
title: "Agent Name Collision Attacks in Multi-Agent Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2609.27624
canonical_ids: ["arxiv:2609.27624"]
publisher_or_author: "Adithyan Arun Kumar — arXiv preprint"
published: 2026-09-23
captured: 2026-09-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance): identifies a
  concrete implementation vulnerability class in Agent-to-Agent (A2A)
  multi-agent hosts — using a remote Agent Card's human-readable name as a
  stable local routing identifier — empirically confirmed against seven
  pinned open-source revisions with a stated fix (route by origin-bound
  stable identity, keep names presentational). A named, tested failure mode
  with a concrete control, directly usable by anyone building or auditing
  multi-agent tool-routing infrastructure.
---

# Agent Name Collision Attacks in Multi-Agent Systems

## Summary

The paper examines how multi-agent hosts turn remote Agent Cards (A2A
protocol) into local agents, tools, workflow targets, and broker routes. The
A2A spec defines a card's name as human-readable metadata, not a stable
identity, and "specifies no collision semantics." The security failure
begins when a host nevertheless uses that remote name as a local routing
identifier. Testing isolated regression scenarios at seven pinned
open-source revisions, the author found that "six client-style integrations
selected an attacker-controlled peer's client or loopback endpoint for a
request addressed to a trusted peer's name," and a seventh, brokered
implementation "collapsed both peers onto one name-derived route." The
result is "wrong-peer dispatch, not universal privilege inheritance" —
synthetic credential/tool tests found no direct credential or tool transfer
in the tested client bindings, though a broker path can forward a caller
configuration object that reaches the wrong peer if usable. The author
frames this as "a recurring implementation vulnerability class, not a
universal A2A protocol exploit."

## Why it matters

For builders of multi-agent research or policy-simulation systems that use
A2A-style agent discovery, this is a directly actionable finding: treating a
remote agent's declared name as a routing identifier is unsafe by default,
and six of seven tested real-world-style integrations already do this. The
stated control — route by an origin-bound stable identity, keep names
presentational, reject ambiguous aliases — is a concrete design rule to
audit for before deploying any multi-agent system that ingests external
Agent Cards.

## Verification notes

Fetched directly from the arXiv abstract page (2609.27624; v1 submitted
2026-09-23 09:46:58 UTC). The vulnerability mechanism, the "six of seven"
and "collapsed both peers" findings, the credential/tool-transfer negative
result, and the recommended control all trace directly to the abstract's
own stated results and quoted language. This is a single-author paper with
no independent replication found; the methodology (testing seven pinned
open-source revisions) is described but the full paper (which
implementations, exact test harness) was not read at capture.

## Updates

None yet.

## Related entries

None yet.
