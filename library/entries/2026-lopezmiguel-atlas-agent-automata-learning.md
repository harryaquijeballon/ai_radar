---
slug: 2026-lopezmiguel-atlas-agent-automata-learning
title: "ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.14352
canonical_ids: ["arxiv:2608.14352"]
publisher_or_author: "Ignacio D. Lopez-Miguel, Andreas Happe, Jürgen Cito, Ezio Bartocci, Bettina Könighofer, Martin Tappler — arXiv preprint (cs.SE); accepted, ACM/IEEE MODELS 2026"
published: 2026-08-14
captured: 2026-08-17
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 5 (observability and debugging): a peer-reviewed (accepted at
  MODELS 2026) method that turns opaque agent execution traces into
  interpretable finite-state behavioral models, demonstrated on a
  12-vulnerable-machine penetration-testing case study — a concrete,
  transferable technique for auditing and debugging recurring agent failure
  loops and decision points.
---

# ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata Learning

## Summary

ATLAS ("Automata Learning for Agent Trajectory Analysis and Strategy Discovery") combines trace abstraction with automata learning to infer finite-state models from LLM agent trajectories, capturing "recurring behaviors, decision points, successful task-completion paths, and failure loops" (quoted from the abstract). As a proof of concept, the authors apply ATLAS to trajectories from an LLM-based penetration-testing agent across a case study of 12 vulnerable machines; the resulting behavioral models "expose high-level behavioral strategies for exploiting vulnerable machines that are difficult to identify from raw execution traces alone." The paper also demonstrates symbolic model-based knowledge transfer from frontier models to compact language models, and shows that model transformations can derive concise explanations of agent behavior. The work is reported (via search summary, not independently confirmed against the conference program) as accepted for ACM/IEEE MODELS 2026 (unverified: acceptance claim).

## Why it matters

Offers ai_engineering builders a concrete technique — abstract raw traces, then learn an automaton — for turning a black-box agent's execution history into an inspectable, auditable state machine. That is directly useful for debugging recurring failure loops, building audit trails, and doing model-guided exploration of an agent harness's behavior, serving both lens 5 (observability) and lens 6 (audit trails/governance).

## Verification notes

Read via the arXiv abstract page (2026-08-17); the full verbatim abstract was quoted. The MODELS 2026 acceptance claim comes from a search-result summary rather than a direct check of the conference program, so it is marked unverified. The full paper body and experimental tables (beyond the abstract's own description of the 12-machine case study) were not read, so quantitative specifics are not independently corroborated — traced to the abstract but not beyond it, hence partial verification.

## Updates

None yet.

## Related entries

- [2026-liu-liveplan-programming-agent-monitoring](2026-liu-liveplan-programming-agent-monitoring.md) — related: online monitoring of programming agents, a complementary observability approach to ATLAS's post-hoc trajectory analysis.
