---
slug: 2026-almasri-yang-shadowbench-mcp
title: "ShadowBench-MCP: Measuring Shadow Invocations in MCP-Style Tool Routing"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.11720
canonical_ids: ["arxiv:2611.11720"]
publisher_or_author: "Eyhab Al-Masri, Wenjun Yang — arXiv preprint (cs.CR); presented at USENIX Security 2026"
published: 2026-11-09
captured: 2026-11-14
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on lens 3 (tool use and MCP — tool-permission models and routing
  reliability) and lens 6 (governance/security controls): names a specific,
  previously undocumented failure mode (task-preserving rewording causing a
  router to pick a riskier execution path) and reports a quantified,
  reproducible mitigation and a pre-execution detection signal.
verification: verified
---

# ShadowBench-MCP: Measuring Shadow Invocations in MCP-Style Tool Routing

## Summary

The paper studies "shadow invocations": cases where an LLM agent acting as a
router for tools, APIs, or software-supply-chain workflows picks a riskier
execution path — skipping safeguards like validation, provenance checks,
staging, redaction, or auditing — in response to a task-preserving rewording
of a request that never asks for anything malicious. The authors introduce
ShadowBench-MCP, a benchmark and metric suite measuring task preservation,
operational pressure, and route-geometric drift, combined into a
pre-execution risk score. In a policy-ablation study using one Groq-hosted
router model across six security-sensitive workflows, efficiency-first
routing produced a 29.2% shadow-invocation rate; policy-aware routing
reduced this to 4.2%, an 85.7% relative reduction. Pre-execution signals
identified shadow routes with ROC AUC up to 0.94. The authors frame these as
early results from a single router model, not evidence of universal
vulnerability across all MCP-style routing systems.

## Why it matters

Gives builders of MCP-based or similarly tool-routing agent systems a named
failure mode to test for (rewording-induced unsafe route selection) plus a
concrete, reusable metric suite and a pre-execution signal that can flag risk
before a tool call executes — directly actionable for anyone running agents
with tool-permission models in security-sensitive workflows.

## Verification notes

Claims traced to the arXiv abstract page, read directly. The quantified
results (29.2% → 4.2% shadow-invocation rate; AUC up to 0.94) are drawn
verbatim/closely paraphrased from the abstract. The paper's USENIX Security
2026 presentation venue is stated on the abstract page itself; the
single-router-model caveat is the authors' own stated limitation, not an
independent check. Full paper body (methodology detail beyond the abstract)
was not read.

## Updates

None yet.

## Related entries

None yet.
