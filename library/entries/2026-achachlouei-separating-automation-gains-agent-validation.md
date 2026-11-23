---
slug: 2026-achachlouei-separating-automation-gains-agent-validation
title: "Separating Automation Gains from Agent Contributions in AI-Assisted Model Validation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.27094
canonical_ids: ["arxiv:2611.27094"]
publisher_or_author: "M. Ahmadi Achachlouei — arXiv preprint (cs.SE / cs.CL cross-list)"
published: 2026-11-23
captured: 2026-11-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Proposes a staged evaluation design and attribution protocol that credits
  an LLM agent only for faults a deterministic non-LLM baseline workflow
  does not already catch, and shows naive metrics can be inflated by simply
  feeding findings back into the baseline — lens 4 (evaluation, validation
  and deterministic guardrails): a directly usable method for avoiding
  overstated "the agent found this" claims.
---

# Separating Automation Gains from Agent Contributions in AI-Assisted Model Validation

## Summary

This paper (M. Ahmadi Achachlouei) addresses a measurement problem in
evaluating LLM agents for bank model validation: evaluations often credit
the agent with gains that actually come from digitized evidence and
deterministic tests already available to a non-LLM workflow. The author
proposes a staged design where a controlled, non-LLM workflow (P1) serves as
both the fallback and the baseline against which an agent's task (P2) is
compared, plus an attribution protocol that credits the agent only for
faults P1 does not already report — penalizing false alarms, unnecessary
actions, and accepting developer assertions, and counting invalid outputs
as misses. The protocol also feeds newly automatable findings back into P1
and fixes safety bounds and a cost gate in advance. Using a synthetic
credit-scorecard test harness and five scripted reference policies (no LLM
agent has yet been evaluated; the paper specifies a falsifiable pilot), the
author compares naive scoring (case accuracy, pooled detection) against the
attribution protocol, adding a regression matrix of sixteen mutant
evaluation versions to check for misleading passes. Naive metrics gave four
flawed policies the same score as one another, while the protocol separated
all five and credited only the policy that detected faults beyond P1; a
single fold-back round also inflated the naive score of a policy that
merely repeated P1's output, without the policy itself changing.

## Why it matters

A concrete design pattern — baseline-first attribution plus a fold-back
regression check — for anyone evaluating whether an agent genuinely adds
value over an existing deterministic process, directly transferable beyond
bank model validation to any "AI-assisted review" claim that needs to be
separated from automation the non-AI workflow already provides.

## Verification notes

Read directly from the arXiv abstract page (arxiv.org/abs/2611.27094),
listed Mon 2026-11-23 (cross-listed cs.SE and cs.CL). The summarized claims
(the staged P1/P2 design, the attribution protocol's penalties, the
sixteen-mutant regression matrix, the naive-vs-protocol scoring result) are
taken directly from the arXiv-published abstract text, which explicitly
notes the pilot is a proposed falsifiable design with no LLM agent yet
evaluated. No independent corroboration sought.

## Updates

None yet.

## Related entries

None yet.
