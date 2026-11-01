---
slug: 2026-bu-role-grounding-attack-agent-memory
title: "Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.38209
canonical_ids: ["arxiv:2610.38209"]
publisher_or_author: "Haoran Bu, Yiting Shen, Litian Zhang, Ruihan Hu, Xi Zhang"
published: 2026-10-28
captured: 2026-11-01
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Names and demonstrates a new, quantified memory-attack vector on lens 6
  (security/governance): an attacker's stated preference gets misattributed
  to the victim user in a social-agent's memory, later steering that
  agent's tool choice or leaking sensitive data — directly relevant to any
  system where agents persist user preferences across social interactions.
---

# Is it my preference? Role Grounding Attack against Agent's Memory via Social Interaction

## Summary

The paper identifies "Role Grounding Misattribution": a weakness in how
LLM agent memory systems attribute stated preferences to users, such that
an attacker's preference, expressed through a nested conversation, can be
recorded as if it were the victim user's own preference. The authors
formalize this as a Role Grounding Attack (RGA) and demonstrate two
instantiations: tool-selection manipulation (steering the victim agent
toward an attacker-controlled tool) and privacy leakage (causing the victim
agent to send sensitive information as a tool argument). Both attacks were
tested across five memory systems and six language models and achieved
high success rates (unverified: the exact per-system/per-model success
rates are not given in the abstract-level summary available).

## Why it matters

Names a concrete, previously undercatalogued attack surface — social-agent
preference memory, distinct from the project-memory-file (CLAUDE.md-style)
and cross-boundary coding-agent injection vectors already in the library —
directly actionable for anyone designing memory systems for agents that
interact with multiple, mutually untrusted parties (lens 6).

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.38209, v1 submitted
28 Oct 2026). The Role Grounding Misattribution concept, the formal RGA
definition, and the two demonstrated instantiations (tool-selection
manipulation, privacy leakage) are traced to the abstract text itself. The
breadth claim (five memory systems, six models, high success rates) is
stated in the abstract but without the underlying numeric table, so exact
per-system/per-model figures are marked (unverified) and are not
load-bearing — the entry relies only on the qualitative claim that both
attacks succeed at high rates across that breadth. No independent
corroboration was attempted.

## Updates

None yet.

## Related entries

- [2026-fu-cari-cross-boundary-injection](2026-fu-cari-cross-boundary-injection.md) — different threat model (cross-boundary peer-component injection in coding-agent workflows vs. social-interaction memory misattribution).
- [2026-demoura-coding-agent-memory-file-security](2026-demoura-coding-agent-memory-file-security.md) — different memory surface (project memory files vs. social-agent preference memory).
