---
slug: 2026-maliha-atc-agent-trajectory-control-role-contracts
title: "ATC: Agent Trajectory Control for Role-Contract Enforcement in Black-Box Multi-Agent Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.04321
canonical_ids: ["arxiv:2611.04321"]
publisher_or_author: "Maisha Maliha, Vishal Pramanik, Sumit Kumar Jha — accepted at EMNLP 2026"
published: 2026-11-03
captured: 2026-11-04
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on agent architecture/orchestration and reproducibility/governance
  (lenses 1, 6): a message-level role-contract enforcement mechanism that
  works on black-box agents (no model internals needed), with measured gains
  in task performance and role consistency over prompting/memory/workflow
  baselines.
verification: verified
---

# ATC: Agent Trajectory Control for Role-Contract Enforcement in Black-Box Multi-Agent Systems

## Summary

Names and addresses "role drift": multi-agent LLM systems assign each agent
a role (e.g., verifier, retriever), but over many turns an agent can breach
that role's contract — a verifier starts planning, a retriever asserts
unsupported conclusions. Agent Trajectory Control (ATC) writes each role's
authority as an explicit contract and enforces it at the point a proposed
message would enter the shared conversation: it scores the message for
out-of-role behavior, leakage into other roles' functions, impermissible
speech acts, and logical contract breaches, computes a leakage-regularized
target to guide regeneration, and re-checks the revised message before
admission. Because it acts on messages rather than internal representations,
it works with black-box agents. Across homogeneous and heterogeneous teams,
ATC improves task performance and role consistency and lowers "role-drift
energy" compared with prompting, memory, workflow-control, and
activation-editing baselines, with the largest gains under explicit
role-confusion stress tests and in larger, more diverse teams. Accepted at
EMNLP 2026.

## Why it matters

A practical enforcement layer for anyone running multi-agent pipelines with
specialized roles (planner/executor/reviewer-style architectures, already
common in this library's prior entries) who cannot access or modify the
underlying model's internals — directly deployable as a message-level gate
rather than requiring retraining, fine-tuning, or activation-level access.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-03). The role-drift framing, the contract-enforcement mechanism, the
black-box applicability, the comparison baselines, and the EMNLP 2026
acceptance all trace to the abstract text. Full paper (quantified
performance/consistency numbers) not read at capture.

## Updates

None yet.

## Related entries

[2026-pramanik-drift-no-more-spectral-locking-atlas](2026-pramanik-drift-no-more-spectral-locking-atlas.md) — a related but representation-level approach to the same class of long-horizon multi-agent drift problem, for open-weight models.
