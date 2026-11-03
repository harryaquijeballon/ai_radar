---
slug: 2026-roth-dependable-agents-hard-fuzzy-rules
title: "Dependable Agents Need Hard and Fuzzy Rules"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.01043
canonical_ids: ["arxiv:2611.01043"]
publisher_or_author: "Frederick Roth"
published: 2026-10-31
captured: 2026-11-03
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation/deterministic guardrails (lens 4) and
  reproducibility/security/governance (lens 6): a tested two-layer control
  pattern (an exact-limit hard guard plus a small taught "fuzzy rule"
  model) that blocks unauthorized agent actions a hard guard alone misses,
  with quantified results against 1,340 episodes.
---

# Dependable Agents Need Hard and Fuzzy Rules

## Summary

Argues dependable AI agents need two kinds of rules: hard rules (exact
limits written as code) and fuzzy rules (learned judgments for cases that
can't be stated precisely). The author tests hard rules in purchasing,
delegation-of-authority, and data-access scenarios using 1,340 episodes
written by outside authors: models left to decide alone took unauthorized
actions in many episodes, and the strongest model tested breached limits
in every condition, while a hard guard placed between the model's proposed
action and its execution blocked all unauthorized actions (confirmed by an
exhaustive search of proposals). The paper then tests "Concept
Programming" — teaching a small model a named judgment rule and measuring
its errors on unseen wording. Placed in front of the hard guard, the small
taught model caught most rule-breaking requests the guard alone missed,
while the guard continued to enforce every exact limit; a prompted
frontier model performed about as well, so the claim is that a small
taught rule suffices, not that it beats other approaches (as stated in the
fetched abstract; full episode set and model list not reviewed at
capture).

## Why it matters

A concrete, layered deterministic-guardrail pattern directly usable in
agent systems with hard operational limits (spending caps, authorization
boundaries, data-access rules): enforce the exact limits with a
non-learned guard (verified to block all violations in-domain), and catch
the harder-to-specify violations with a small, purpose-taught judgment
model in front of it — rather than relying on a single frontier model's
judgment or a single guard layer alone. Directly relevant to the
standing interest in validated, defensible agentic systems for research and
policy use.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 31 Oct 2026, no revisions). The 1,340-episode hard-rule test, the
"breached in every condition" finding for the strongest unguarded model,
the hard guard's full blocking of unauthorized actions, the Concept
Programming method, and its catching "most" guard-missed violations while
performing comparably to a prompted frontier model all trace to the
fetched abstract text, which is the paper's own stated summary of its
results — treated as `verified` on this library's convention for
single-source arXiv preprints whose headline figures are self-reported.
The full paper (exact violation rates, episode construction, author
affiliation) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
