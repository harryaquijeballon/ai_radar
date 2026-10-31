---
slug: 2026-fu-cari-cross-boundary-injection
title: "CARI: Cross-Boundary Adversarial Runtime Injection in Coding-Agent Workflows"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.38799
canonical_ids: ["arxiv:2610.38799"]
publisher_or_author: "Jie Fu, Shuang Wu, Ashish Kundu, Wendy Hui Wang, Yuan Hong — arXiv (cs.CR)"
published: 2026-10-28
captured: 2026-10-31
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Squarely on lens 6 (prompt injection and tool-abuse defenses): a named,
  quantified attack class against multi-team coding-agent workflows, with
  transfer results against commercial agents and a clear statement of why
  generic defenses fail — directly actionable for anyone running agents
  across team/service boundaries.
verification: verified
---

# CARI: Cross-Boundary Adversarial Runtime Injection in Coding-Agent Workflows

## Summary

Coding agents often work on software whose components belong to different
teams or services, so a malicious or compromised peer component can feed
manipulated runtime feedback (e.g. diagnostic/debugging output) to another
team's coding agent. The authors introduce CARI, in which an attacker hides
malicious instructions in such peer-controlled diagnostic output; the victim
agent may treat these as normal debugging guidance and take unauthorized
actions in its own environment, without the attacker needing to compromise
the victim's prompt, model, tools, or local system. They build ten attacks
covering resource exhaustion, information exposure, and development-state
manipulation, and test across four programming languages and five
code-capable models: CARI succeeds in 2,845 of 3,000 trials (94.8%). The
attack also transfers to commercial coding agents, with reported success
rates of 61.3% on Codex and 58.7% on Claude Code. Generic prompt-level
warnings were ineffective as a defense; explicit policies blocked the
attacks but caused substantial over-refusal of legitimate actions.

## Why it matters

Names and quantifies a specific, realistic injection vector — peer-component
diagnostic output in cross-team/cross-service coding-agent workflows — that
sits outside the usual "untrusted document" or "malicious tool" threat
models, with a concrete finding that the obvious cheap defense (prompt-level
warnings) does not work and the working defense (explicit policy) has a
measurable over-refusal cost that must be weighed.

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.38799, v1 submitted
28 Oct 2026, primary cs.CR, cross-listed cs.SE). The ten-attack taxonomy, the
94.8% (2,845/3,000) success rate, the 61.3%/58.7% commercial-agent transfer
rates, and the stated defense results are traced to the abstract text
itself. No independent corroboration of the attack implementation or raw
trial data was attempted.

## Updates

None yet.

## Related entries

None yet.
