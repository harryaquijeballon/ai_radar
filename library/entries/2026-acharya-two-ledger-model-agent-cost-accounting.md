---
slug: 2026-acharya-two-ledger-model-agent-cost-accounting
title: "The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.06989
canonical_ids: ["arxiv:2611.06989"]
publisher_or_author: "Vivek Acharya"
published: 2026-11-04
captured: 2026-11-07
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on observability and cost/latency monitoring (lens 5) and
  reproducibility/governance (lens 6): a concrete two-ledger mechanism
  (settlement ledger + per-invocation attribution ledger, layered
  trace/business-key/probabilistic correlation) for attributing multi-agent
  AI spend to specific business transactions, tested in a ground-truth
  simulation with quantified coverage, reconciliation, and cost-gating
  results.
---

# The Two-Ledger Model: Transaction-Grain Cost Accounting for Multi-Agent AI Systems Across Clouds, Models, and Systems of Record

## Summary

Enterprises running business transactions (an order, an insurance claim, a
case) through multi-agent AI systems spanning cloud providers, LLMs,
orchestration tools, and systems of record cannot currently see what AI cost
a specific transaction — billing data is visible only at the settlement
level (product SKU, billing period), and providers never see enterprise
transaction boundaries. The FinOps Open Cost and Usage Specification (FOCUS)
standardizes billing schemas, including added AI token/requester attribution,
but still operates at settlement grain, not transaction grain.

The paper proposes the Two-Ledger Model: a settlement ledger (FOCUS-conformant
billing data) and an attribution ledger (per-invocation usage records built on
OpenTelemetry GenAI telemetry), linked by a layered correlation method (trace
context, agent/tool protocol metadata, business-key matching, probabilistic
matching — each link recording its method and confidence). A versioned rate
card prices usage near real-time; period reconciliation ties both ledgers to
the invoice, with unexplained residuals flagged as possible shadow AI use.

In a simulation with known ground truth: cost coverage stayed above 99% even
when trace propagation dropped to zero; the reconciliation residual recovered
planted unmetered spending within 0.24 percentage points and flagged provider
billing errors; mid-flight cost gating reduced p99 transaction cost by up to
61%, with a 2–4% false-pause rate. The author proposes the attribution ledger
as a candidate invocation-grain FOCUS profile extension (unverified: this is
a proposal, not an adopted standard).

## Why it matters

Gives builders of multi-agent systems a named, testable mechanism for a
problem most teams currently solve ad hoc or not at all: knowing what a
specific business outcome cost in AI spend, across heterogeneous
clouds/models/orchestration layers, and catching unmetered ("shadow AI")
usage. The quantified robustness-to-missing-telemetry result (99% coverage at
zero trace propagation) is the most directly reusable finding for anyone
designing cost observability into an agentic system.

## Verification notes

Read directly from the arXiv abstract page (arxiv.org, allowlisted). All
claims above, including the quantitative results (99% coverage, 0.24pp
residual, 61% p99 reduction), are stated in and traced directly to the
abstract; no load-bearing claim here depends on information beyond it. The
full paper (66 KB) was not independently fetched. Noted as context, not a
verification gap: single-author paper, simulation-based (not a production
deployment), one version (v1, 4 Nov 2026).

## Updates

None yet.

## Related entries

None yet.
