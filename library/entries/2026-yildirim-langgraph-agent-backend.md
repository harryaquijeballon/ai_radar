---
slug: 2026-yildirim-langgraph-agent-backend
title: "Building a Proper Backend for My LangGraph AI Agent"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/building-a-proper-backend-for-my-langgraph-ai-agent/
canonical_ids: []
publisher_or_author: "Soner Yıldırım — Towards Data Science"
published: 2026-08-22
captured: 2026-08-23
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on agent architecture and harness engineering (lenses 1, 2): a
  usable protocol-based pattern for moving a demo agent's state and data
  access from in-memory objects to a swappable, persistent backend, but the
  article demonstrates the pattern's structure only — no quantified
  reliability, latency, or failure-mode data — so it stays below the
  report bar's practically-usable-with-evidence threshold.
---

# Building a Proper Backend for My LangGraph AI Agent

## Summary

Describes evolving a demo LangGraph booking agent from ephemeral in-memory
Python objects to a production-oriented backend using PostgreSQL, without
hardcoding the database dependency into the agent graph. Two components are
replaced with persistent, protocol-defined interfaces: a Checkpointer
(conversation state) and a BookingRepository (appointment data), the latter
specified as a Python Protocol with three methods (`technicians` property,
`list_bookings()`, `create_booking()`) so `PostgresBookingRepository` and
`InMemoryBookingRepository` implementations can be swapped at startup
without changing calling code. Only two graph nodes touch the repository
directly — one reading existing bookings to compute free slots, one writing
confirmed bookings — keeping the rest of the graph decoupled from storage
and only reading/updating in-memory `AgentState`. States the concrete
failure this fixes: in-memory storage loses conversation state on restart
and cannot share booking availability across sessions, allowing
double-booking.

## Why it matters

A directly copyable pattern for separating an agent's working memory from
its persistent storage via protocol-based repositories — letting the same
graph run against an in-memory implementation in tests and a real database
in production, and supporting multiple frontends (the article names
Streamlit and WhatsApp) against one shared backend. Applicable to any
multi-step agent whose demo currently uses process-local state and needs a
path to a durable, concurrency-safe backend.

## Verification notes

Article fetched and read directly (2026-08-23); the author, the 2026-08-22
publication date, the Checkpointer/BookingRepository split, the Protocol
definition and its three methods, the two graph nodes that touch the
repository, and the stated in-memory failure mode (state loss on restart,
cross-session double-booking) all trace to the fetched article text. No
load-bearing quantified claims requiring independent corroboration — the
article describes an architecture, not measured performance.

## Updates

None yet.

## Related entries

None yet.
