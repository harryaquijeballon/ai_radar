---
slug: 2026-destefanis-authoring-agent-skills
title: "Authoring Agent Skills: A Software-Engineering Approach"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.25032
canonical_ids: ["arxiv:2607.25032"]
publisher_or_author: "Giuseppe Destefanis — arXiv preprint"
published: 2026-07-27
captured: 2026-07-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on harness and context engineering (lens 2): treats agent skills as
  software artifacts and names concrete engineering principles (single
  responsibility, interface/implementation separation, low coupling, token
  budget) plus authoring patterns, common implementation faults, and
  security considerations — exactly the "names mechanisms and when to use
  them" standard the lens sets for a high score.
---

# Authoring Agent Skills: A Software-Engineering Approach

## Summary

Argues that Agent Skills — reusable procedural knowledge that extends LLM
agents — should be authored under established software-engineering
principles: single responsibility, separation of interface from
implementation, and low coupling, all constrained by token-budget limits
specific to LLM contexts. The paper covers skill structure, staged content
loading, and selection mechanisms; compares skills against alternative
behavioural mechanisms (project memory, slash commands, subagents) with
guidance on choosing between them; and addresses authoring patterns, common
implementation faults, and third-party skill security considerations, with
UML-style diagrams of loading models and skill anatomy.

## Why it matters

A direct, named engineering vocabulary for a design decision most agent
builders currently make by convention rather than principle: when to use a
skill versus project memory, a slash command, or a subagent, and how to
structure a skill so it stays maintainable under token-budget pressure.
Immediately usable by anyone authoring or reviewing skills for a
production agent harness.

## Verification notes

arXiv abstract page fetched directly (2026-07-29); title, author, and
"Submitted on 27 Jul 2026" confirmed. The named engineering principles, the
skill-vs-alternative-mechanisms comparison, and the coverage of authoring
patterns/faults/security all trace to the fetched abstract text. Full paper
(the UML-style diagrams and specific fault catalogue) not read at capture.

## Updates

None yet.

## Related entries

None yet.
