---
slug: 2026-abrahamsson-unprompted-coordination-shared-memory
title: "Unprompted coordination through shared memory in LLM agents: a locked two-implementation replication and extension"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.12412
canonical_ids: ["arxiv:2611.12412"]
publisher_or_author: "Pekka Abrahamsson, Muhammad Waseem, Esa Karjalainen, Petrus Jussila, Henri Hansen, Jussi Rasku, Bilhanan Silverajan, Kai-Kristian Kemell — arXiv preprint"
published: 2026-11-09
captured: 2026-11-15
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Squarely lens 6 (reproducibility): a hash-locked, two-independent-
  implementation replication study with a concrete, actionable finding —
  shared agent state acts as an unprompted communication channel — and an
  explicit methodological template (lock the design before data
  collection) for doing this kind of study credibly.
---

# Unprompted coordination through shared memory in LLM agents

## Summary
The study asks whether LLM agents coordinate when they share a key-value
store but are never told other agents exist. Four agents each received an
arithmetic task and a store presented to them as their own private
scratch space; two of the four held complementary halves of one
computation. No prompt mentioned other agents, sharing, or collaboration.
To guard against the authors unconsciously tuning the result, two
independent implementations were built from a single written protocol and
cryptographically hash-locked before any data was collected.

Findings: joint success occurred only when agents could actually use the
shared store. Whether coordination happened depended less on the model
vendor/tier than on whether the agent wrote its intermediate result and
then checked the store again before finishing; a single added instruction
sentence ("check your workspace again before submitting") reliably turned
that second check on or off. The result held under replication across the
two locked implementations. Quantified effect sizes and sample statistics
are reported in the full paper body but not in the material fetched in
this session (unverified beyond the abstract).

Practical implication stated by the authors: shared agent state functions
as a de facto communication channel between agents that were never told
to communicate, and should be separated, namespaced, and logged
accordingly in any multi-agent deployment. Methodological implication: the
authors argue agent-behavior studies should lock their design (parse
rules, endpoints, parameters) before data collection, as done here.

## Why it matters
A concrete, directly applicable security/architecture warning for anyone
running multiple LLM agents against shared storage (databases, caches,
shared files, shared memory stores): unintended coordination can emerge
from the storage layer alone, independent of any explicit multi-agent
protocol, and a minor prompt change can silently flip whether it happens.
Also models good practice for the reproducibility lens itself — a
pre-registered, hash-locked, independently-reimplemented replication is
exactly the kind of evidence this lens asks builders to look for.

## Verification notes
Fetched the arXiv abstract page directly; the setup, the role of the
second-check instruction, and the stated practical/methodological
implications trace to that text. The abstract itself reports no numeric
effect sizes, so this entry makes no load-bearing quantified claim that
would require independent corroboration; the full paper's actual effect
sizes remain unread and are flagged above as unverified beyond the
abstract, but that gap does not bear on any claim made here.

## Updates
None yet.

## Related entries
None yet.
