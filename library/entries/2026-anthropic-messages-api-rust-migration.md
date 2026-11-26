---
slug: 2026-anthropic-messages-api-rust-migration
title: "Migrating our Messages API to Rust"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://www.anthropic.com/research/migrating-api-to-rust
canonical_ids: []
publisher_or_author: "Anthropic — Engineering blog"
published: 2026-11-25
captured: 2026-11-26
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A first-party, heavily quantified account of an agent-coordinated,
  large-scale production rewrite (Python to Rust) with a named
  verification architecture (shadowing production as oracle, inner/outer/
  memory loops) — directly usable patterns for lenses 1, 2, and 7.
  Vendor source: read the headline performance figures as describing
  Anthropic's own system, not a general claim about AI-assisted rewrites.
---

# Migrating our Messages API to Rust

## Summary

Anthropic's Python-based Messages API had grown into a high-traffic service
where per-request Python overhead made scaling costly. An initial partial
rewrite — a Rust component that parsed model output, called from Python —
cut CPU by only about 8–10%, because each token still crossed the
language boundary three times, so the team moved to a full rewrite. The
hardest problem was verifying parity with a moving production target:
existing tests (~700 integration tests) were coupled to the Python
implementation and incomplete, and an audit found more than 100 weakened
assertions in ported tests. The team's fix was "shadowing": running the
model once and replaying its output through the new Rust code, comparing
every step against the old implementation before and after the model call,
and — since user text couldn't be read — logging only the shape of each
difference (step, prompt piece, first differing byte, lengths), grouped by
"fingerprint." Verification ran in three loops: an inner loop where agents
worked in sandboxes with fast local checks; an outer loop where engineers
reviewed fixes before they were deployed and checked against shadowed
production traffic; and a memory loop where corrections from review became
stored rules, lint checks, and tests, including a merge check requiring
matching Rust changes for Python edits. Results: about 70% less CPU per
request, memory per request down more than 80%, median time-to-first-token
down about 20%, and the input match rate on production traffic rose from
roughly 24% in late April to 99.6% by August — while API traffic grew
roughly 1,800x from early 2024 to fall 2026. Claude wrote the first version
of the core request path in about a week; Claude agents, coordinated by a
lead agent and assigned per bug type, handled most subsequent fixes and
tests, with engineers reviewing proposed changes and steering work via
Slack. Human review stayed a required gate, since the verifiers themselves
could not judge whether a fix was good enough to ship.

## Why it matters

A concrete, quantified template for anyone considering an agent-driven
rewrite of a critical production system: the "shadowing with production as
oracle" verification architecture, and the inner/outer/memory loop
structure for routing agent-found fixes through human review, are directly
transferable harness-design patterns (lenses 1, 2) independent of the
specific language migration. The reported performance gains (70% CPU, 80%+
memory, 20% latency) and the match-rate ramp (24% to 99.6% over roughly four
months) are a rare first-party, quantified account of what "AI-assisted
large-scale migration" looked like in practice (lens 7), including where
human review remained load-bearing.

## Verification notes

Fetched the Anthropic engineering post directly
(anthropic.com/research/migrating-api-to-rust, published 2026-11-25). All
figures and the verification-architecture description above are traced to
the post's own text. As a first-party vendor account, the performance
figures describe Anthropic's own system and engineering process; no
independent corroboration was available or attempted. Per the sources
profile's standing caveat for this watchlist row, the headline numbers are
treated here as Anthropic's own reported results, not as a general claim
about AI-assisted migrations elsewhere.

## Updates

None yet.

## Related entries

None yet.
