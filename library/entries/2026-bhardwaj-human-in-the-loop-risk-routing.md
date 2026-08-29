---
slug: 2026-bhardwaj-human-in-the-loop-risk-routing
title: "Human-in-the-Loop Without Killing Throughput"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/human-in-the-loop-without-killing-throughput/
canonical_ids: []
publisher_or_author: "Priyansh Bhardwaj — Towards Data Science"
published: 2026-08-28
captured: 2026-08-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A concrete, weighted risk-routing mechanism replacing blanket
  human-approval gates on agent write actions, with a named failure mode
  (rubber-stamp fatigue from 20-40 minute approval waits) it solves —
  squarely lens 8 (human-in-the-loop review patterns) with a formula and
  criteria a builder could directly adapt.
---

# Human-in-the-Loop Without Killing Throughput

## Summary
Bhardwaj describes replacing a blanket human-approval requirement on every
AI agent write operation — which caused analysts to wait 20-40 minutes for
approval on mostly routine queries, and led reviewers to skim batches and
lose effectiveness ("rubber-stamp fatigue") — with risk-based routing that
scores each agent action and escalates only high-risk operations to a human.
The router combines four signals with a stated weighting formula:
`0.40 * blast_radius + 0.25 * table_floor + 0.20 * novelty + 0.15 *
disagreement`, where blast radius is the actual row count affected (capped
at 50,000 to avoid planner-estimate errors), table sensitivity is a static
allowlist enforcing minimum risk floors for regulatory/sensitive tables,
novelty is embedding-distance from previously approved query intents, and
disagreement is measured via multiple higher-temperature resamples to detect
genuine ambiguity. Escalations are acknowledged immediately as tickets
rather than left as hanging requests, decoupling user experience from
review latency. The author reports human reviewers proved most valuable at
catching intent-interpretation mismatches, not validating mechanically
correct queries.

## Why it matters
A directly adaptable pattern for the standing interest in human-in-the-loop
review for agentic research/policy products: instead of an all-or-nothing
approval gate that degrades under volume, a stated formula for deciding
*which* agent actions actually need a human, built from measurable signals
(row counts, a sensitivity allowlist, embedding novelty, resample
disagreement) rather than a blanket policy.

## Verification notes
Fetched directly from towardsdatascience.com (allowlisted). The weighting
formula and the four signal definitions (blast radius cap, table-sensitivity
allowlist, semantic-distance novelty, resample-disagreement) were confirmed
against the fetched source text, as was the 20-40 minute wait figure and the
"rubber-stamp fatigue" framing. No independent corroboration is possible or
required for what is a first-person account of the author's own system
design; no external benchmark claim is made that would need it.

## Updates
None yet.

## Related entries
None yet.
