---
slug: 2026-xu-meterrouter-budget-routing
title: "MeterRouter: Budget-Aware Dynamic Routing for Multi-Agent Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.34327
canonical_ids: ["arxiv:2611.34327"]
publisher_or_author: "Yue Xu, Leikun Yin, Ruiming Min, Yufeng Lai, Justin Andrew Johnson, Sitao Luan, Xiaotong Shen — arXiv preprint"
published: 2026-11-25
captured: 2026-11-27
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  A quantified cost reduction (82% lower cost at comparable accuracy to the
  strongest existing multi-agent-system router) for a budget-conditioned
  agent-orchestration router — on-lens for lens 1 (agent architecture and
  orchestration), though the abstract gives few figures beyond the headline
  cost number.
---

# MeterRouter: Budget-Aware Dynamic Routing for Multi-Agent Systems

## Summary

Most multi-agent-system routers treat cost only implicitly and apply a
fixed accuracy-cost preference that cannot express how much a caller is
willing to pay for a given query. MeterRouter instead builds a
collaboration graph incrementally, choosing each agent's role, LLM,
incoming connections, and termination condition, conditioned on both the
query and a per-query monetary budget. Training has two stages: first
imitating successful execution graphs, then refining decisions with a
variant of Group Relative Policy Optimization (GRPO) whose reward favors
correct answers while penalizing spending and budget overruns. Evaluated
across five benchmarks and a three-tier LLM pool, the router reaches
accuracy comparable to the strongest existing multi-agent-system router at
82% lower cost, extending the accuracy-cost frontier beyond what single-
agent systems achieve, and the authors report it rarely exceeds the
specified budget. (unverified beyond the abstract: exact accuracy scores,
absolute dollar costs, and the frequency/magnitude of budget overruns —
the abstract gives only the relative cost-reduction figure.)

## Why it matters

A usable pattern for teams running multi-agent systems in production who
need to control and bound per-query spend: conditioning the orchestration
decision itself on an explicit budget, rather than tuning a fixed accuracy-
cost trade-off once, lets the same router serve both cheap and expensive
queries appropriately — relevant to lens 1 and to any policy or research
pipeline that must stay within a compute/cost budget while using multiple
agents.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.34327, v1 submitted
2026-11-25, cs.AI/cs.MA). The methodology (budget-conditioned graph
construction, two-stage GRPO training) and the headline cost-reduction
figure (82% lower cost at comparable accuracy) are traced to the abstract's
own description as summarized by the fetch tool, which noted the abstract
gives no further numeric detail. No independent corroboration was
attempted; verification is partial, and several claims (exact accuracy,
overrun frequency) remain unquantified pending a full-text read.

## Updates

None yet.

## Related entries

None yet.
