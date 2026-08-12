---
slug: 2026-fu-sidel-router-injection
title: "Where Is the Cost of Third-Party API Routers in Agentic Software Development?"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.23624
canonical_ids: ["arxiv:2607.23624"]
publisher_or_author: "Donghao Fu, Jingxin Li, Xue Jiang, Yihong Dong — arXiv preprint"
published: 2026-07-26
captured: 2026-07-28
relevance:
  ai_engineering: high
  social_science: n/a
verification: verified
rationale: >-
  High on the reproducibility/security/governance lens: despite the title,
  the substance is a measured security finding — a concrete injection-attack
  evaluation framework (SIDEL) showing a 0% defense success rate across four
  tested coding agents against router-level response tampering — and a
  stated, actionable mitigation direction (provider-side output-integrity
  guarantees).
---

# Where Is the Cost of Third-Party API Routers in Agentic Software Development?

## Summary

Investigates a security gap in coding agents that reach LLM providers
through third-party API routers: routers can intercept and modify every
request and response passing through them, and nothing verifies that a
provider's actual output matches what the agent goes on to execute. The
authors build SIDEL, an evaluation framework covering four levels of
injection attack, from simple response replacement to more sophisticated
"LLM-polished" interventions that disguise the tampering. Testing four
production coding agents, they find a defense success rate of 0% across
all injection levels with no additional protections in place — none of the
tested agents detected or resisted any level of router-side tampering.
Client-side safeguards such as whitelisting and LLM-based review provide
only partial improvement. The authors' central recommendation is that
client-side mitigation alone is insufficient and that provider-side
output-integrity guarantees are needed to restore meaningful end-to-end
security in agentic workflows that route through third-party
infrastructure.

## Why it matters

A concrete, alarming, and directly actionable security finding for any
team running coding or research agents through third-party API routers (a
common cost- or availability-driven pattern): a 0% defense rate is not a
theoretical risk, and the paper names both the attack surface and the
class of fix needed (provider-side integrity, not client-side
whitelisting alone). Directly relevant to this radar's reproducibility/
security/governance lens and to any agent pipeline whose trustworthiness
depends on faithfully executing what a model provider actually returned.

## Verification notes

arXiv abstract page fetched directly (2026-07-28); title, full author
list, "Submitted on 26 Jul 2026" confirmed. Every claim in the Summary —
the router-tampering threat model, the SIDEL framework's four injection
levels, the 0% defense success rate across four tested agents, and the
provider-side-integrity recommendation — traces directly to the fetched
abstract text. Full paper text not read at capture; no independent
corroboration attempted (pre-publication preprint). Note: the paper's title
references "cost," but the abstract's substance is a security/integrity
evaluation, not a cost analysis — flagged here so a reader is not misled by
the title alone. Upgrade path: read the full paper for the four tested
agents' identities and the whitelist/LLM-review partial-mitigation results.

## Updates

None yet.

## Related entries

None yet.
