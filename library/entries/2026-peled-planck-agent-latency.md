---
slug: 2026-peled-planck-agent-latency
title: "Why Adding More AI Agents Made Our System Slower"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/why-adding-more-ai-agents-made-our-system-slower/
canonical_ids: []
publisher_or_author: "Uri Peled — Towards Data Science"
published: 2026-07-23
captured: 2026-07-23
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on the observability/debugging lens: a concrete production
  diagnosis (CPU-bound JSON deserialization and single-event-loop
  contention, not I/O, as the real bottleneck when scaling a multi-agent
  system) that is narrowly scoped to one architecture but whose diagnostic
  pattern generalizes. Discovered in the 22-23 Jul 2026 window via Towards
  Data Science.
---

# Why Adding More AI Agents Made Our System Slower

## Summary

Practitioner write-up (Uri Peled, Towards Data Science, 23 July 2026)
describing a production multi-agent system ("Planck") that got slower, not
faster, as more agents were added, despite using asynchronous Python
throughout. The stated root cause: "asynchronous I/O only removes waiting,
it doesn't eliminate computation" — the CPU work following each I/O response
(JSON serialization/deserialization, connection-limit contention in
`aiohttp`) became the bottleneck as hundreds of concurrent responses
competed for the GIL on a single event loop. The fix described was
architectural rather than a code-level optimization: distributing work
across multiple processes/workers so the bottleneck could scale
horizontally instead of funneling through one event loop.

## Why it matters

A transferable debugging lesson for anyone scaling a multi-agent system:
async I/O concurrency does not remove CPU-bound work from the critical
path, and adding agents can make a single-process, single-event-loop system
slower rather than faster once that CPU work (not the LLM calls themselves)
becomes the constraint. Worth checking before assuming more agents or more
async concurrency will improve throughput.

## Verification notes

Article fetched and read in full; the root-cause diagnosis, the specific
bottlenecks named (JSON (de)serialization, `aiohttp` connection limits, GIL
contention), and the multi-process fix are traced directly to the source
text. Single-source practitioner account of one system; no independent
corroboration sought, as the claims are about that system's specific
architecture rather than a general empirical result.

## Updates

*(none yet)*

## Related entries

None yet.
