---
slug: 2026-peilivanidis-skillware-deterministic-capability
title: "Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07652
canonical_ids: ["arxiv:2611.07652"]
publisher_or_author: "Vladimiros Peilivanidis"
published: 2026-11-05
captured: 2026-11-08
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 3 (tool use) and lens 2 (harness engineering): a concrete
  proposal to replace prompted, guessed tool calls with versioned,
  typed-contract capability bundles (deterministic code, tests, instructions
  bundled together), with a large-scale evaluation (23 models, 368
  conditions) claiming small local models equipped this way beat
  unequipped frontier models. Verification held to `partial`: single-author
  paper from a named but unfamiliar organization, no independent
  corroboration of the evaluation claims attempted.
---

# Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems

## Summary

Argues that current autonomous systems are fragile because language
models must write code, guess API payloads, and remember operational rules
through prompts alone — wasting context, raising cost, and making agents
unreliable in production. Presents Skillware, an open framework and
registry that separates what an agent wants to do from how the task is
carried out: capabilities are packaged as versioned bundles containing a
typed JSON input contract, deterministic Python code, task instructions,
datasets, and unit tests, with adapters exposing them as native tool
declarations for both cloud and local models. In an evaluation across 23
models and 368 conditions, small local models equipped with Skillware
reportedly beat unequipped frontier models on multi-step workflows, with
large reductions in token use and cost and no parameter errors. The paper
outlines extending the approach from digital systems to IoT, drones, and
robotics.

## Why it matters

A concrete architectural alternative to prompting for tool use — package
the capability itself (typed contract, deterministic code, tests) rather
than hoping the model infers the right call — directly relevant to
reliability engineering for agentic tool use (lens 3), though the claim
that small models with Skillware beat unequipped frontier models is
striking enough to warrant independent scrutiny before relying on it.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 5 Nov 2026, no revisions). The architecture description and the
23-model/368-condition evaluation claim trace to the fetched abstract
text. Verification held at `partial` (not `verified`) because the headline
comparative claim (small local models beating unequipped frontier models)
is unusually strong, the author is single and the organization
(ARPA Hellenic Logical Systems) was not independently checked, and no
corroboration beyond the abstract was attempted. The full paper
(benchmark design, model list, cost accounting) was not reviewed at
capture.

## Updates

None yet.

## Related entries

None yet.
