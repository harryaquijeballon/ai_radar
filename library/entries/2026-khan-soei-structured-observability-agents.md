---
slug: 2026-khan-soei-structured-observability-agents
title: "Soei: Structured Observability of Evidence and Intent for Multi-Agent AI Software Engineering"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.39468
canonical_ids: ["arxiv:2610.39468"]
publisher_or_author: "Mohammed Nayeem Khan, K S Sarun Kumar — arXiv (cs.SE)"
published: 2026-10-29
captured: 2026-10-31
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Squarely on lens 5 (observability and debugging): a large empirical study
  of real coding-agent sessions quantifying how often "complete" work
  actually lacks verification, paired with a benchmarked provenance/ledger
  system — a concrete answer to "what was actually done, by whom, and is it
  verified" for long-running, lightly-supervised agent work.
verification: verified
---

# Soei: Structured Observability of Evidence and Intent for Multi-Agent AI Software Engineering

## Summary

AI coding agents now perform long, multi-step, multi-session work with
little supervision, leaving developers who return to it unsure what was
actually done, by whom, and whether it is complete. The authors first audit
an existing open-source local observability tool (Agenttrail) against its
own source: they confirm nine documented mechanisms, find two event
pipelines that are never unified, and identify an unauthenticated local
mutation surface in its Map service. They then run an empirical study on 45
real coding-agent sessions (~102k records, 20.6k tool executions, 2.3k
human-to-agent episodes) using a classifier with 83.3–96.7% precision: 23.4%
of code-editing episodes end without an independent check after the last
edit, and 57.8% of tasks marked complete after editing lacked proof of
verification in between. A timing heuristic for session hand-offs recovers
only 6 of 24 session pairs that content-lineage analysis independently
links. 42% of sessions exceed 24 hours, nearly half of transcript bytes fall
beyond a 2 MiB replay bound, and 16 sessions contain credential-like
strings. The authors then propose Soei: an event schema for acknowledgements,
a hash-chained local ledger, a W3C PROV-aligned provenance graph, calibrated
inference for attribution/lineage, and a verification layer separating
completion claims from proof. On the same corpus, the ledger is 20% of raw
size, stores no content or credentials, verifies at ~126k events/second,
detects tampering, and replays deterministically.

## Why it matters

Quantifies, for the first time at this scale, how often agent-marked
"complete" work actually lacks a verification trail (57.8% of editing tasks
in this corpus) — a concrete empirical basis for requiring evidence-gated
completion in any agentic SDLC workflow — alongside a working, benchmarked
system (tamper-evident, 126k events/sec, no stored credentials) that
builders can study as a reference design.

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.39468, v1 submitted
29 Oct 2026, primary cs.SE, cross-listed cs.AI/cs.MA). The Agenttrail audit
findings, the corpus size and precision figures, the 23.4%/57.8% completion-
without-verification figures, the session-hand-off/credential-leak figures,
and the Soei system's performance numbers (20% ledger size, ~126k
events/sec) are traced to the abstract text itself. No independent
corroboration of the underlying session corpus or Agenttrail source audit
was attempted.

## Updates

None yet.

## Related entries

None yet.
