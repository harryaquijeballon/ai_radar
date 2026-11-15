---
slug: 2026-su-incentive-responsive-agents
title: "Incentive-Responsive Agents: A Principal-Agent Framework, Metric Suite, and Runtime Architecture for Long-Lived Personal AI Agents"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.15515
canonical_ids: ["arxiv:2611.15515"]
publisher_or_author: "Jipu Su — arXiv preprint (cs.AI, cross-listed cs.MA)"
published: 2026-11-11
captured: 2026-11-15
relevance:
  social_science: high
  ai_engineering: high
verification: partial
rationale: >-
  Cross-domain: a quantified principal-agent (economics) framework applied
  to long-lived AI agents, with a real-LLM experiment showing prompt-level
  incentive framing has no detectable effect while a runtime-enforced
  incentive contract does — high for social_science lens 6 (AI applied to
  social-science research, here mechanism design for agents) and
  ai_engineering lens 1/6 (agent architecture, governance) with a
  practically usable routing/allocation mechanism.
---

# Incentive-Responsive Agents

## Summary
The paper argues that long-lived personal AI agents — ones that hold
accounts, memory, and ongoing task streams — lack a genuine incentive
layer: most "alignment via incentives" work treats an incentive as text in
a prompt, which the author distinguishes from an incentive the agent's
policy must causally respond to. The proposed framework models an
incentive as a runtime contract over the agent's operating point (model
tier, compute, memory budget, tool authority, task priority, verification
level, and compensation). Stated theoretical contributions include a
"non-consumption invariance" principle separating real incentives from
prompt-level persuasion, a "persistence-as-discount" theorem linking
identity continuity to sustained effort, an incentive-capability
exchange-rate frontier yielding a per-task routing rule, and a Goodhart
bound for multi-channel verification.

Two experiments test the framework. A real-LLM experiment (240 runs, two
models, 60 verifiable tasks) found prompt-level incentive framing had no
detectable effect on outcomes (p = 0.62), while runtime resource
allocation raised success on the hardest task family from 0.60 to 1.00
(p = 0.008), at 4.8x price-weighted cost; the exchange-rate theorem
predicted a break-even baseline of 0.21 (unverified beyond the abstract:
how closely the prediction matched the observed value is not stated here).
A separate simulation (20 seeds, 3,000 tasks) found resource ROI rose from
7.09 to 16.67 and a "gaming" metric fell from 0.333 to 0.115 under the
framework's allocation rule. The author states code, simulator, and
results are released; live deployment is noted as future work.

## Why it matters
For social-science readers: a concrete empirical test of whether
principal-agent incentive theory — designed for human agents — transfers
to artificial ones, with a clear negative result for the naive case
(prompt text alone does nothing, p = 0.62) that bears on how economists
should model AI-agent "incentives" going forward (lens 6).

For AI-engineering readers: a practically usable per-task routing rule
(the incentive-capability exchange-rate frontier) and a quantified
Goodhart-resistance mechanism for allocating compute/tool authority across
long-lived agents — directly relevant to designing multi-agent systems
that must be both effective and resistant to gaming (lens 1, lens 6).

## Verification notes
Fetched the arXiv abstract page directly; the quantified results above
(240 runs, p-values, success-rate jump, ROI and gaming figures) trace to
that text. The full paper, released code, and simulator were not
independently fetched or re-run in this session, so the theoretical
claims (invariance principle, persistence-as-discount theorem, Goodhart
bound) were not checked for internal validity — verification is partial.

## Updates
None yet.

## Related entries
None yet.
