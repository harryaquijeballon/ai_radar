---
slug: 2026-krishnamoorthy-reasoning-effort-shopping-agents
title: "Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort Increases the Confidence but Not the Correctness of LLM Shopping Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.22033
canonical_ids: ["arxiv:2611.22033"]
publisher_or_author: "Adi Krishnamoorthy, X.Y. Han"
published: 2026-11-17
captured: 2026-11-18
relevance:
  social_science: low
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails): a
  controlled, multi-model study showing reasoning effort inflates stated
  confidence without improving decision quality or calibration — directly
  actionable for anyone using model self-reported confidence as a guardrail.
---

# Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort Increases the Confidence but Not the Correctness of LLM Shopping Agents

## Summary

The authors benchmark ten frontier models, acting as product-choice shopping
agents, on three benchmarks built from WebShop, Amazon's SQID, and
Wayfair's WANDS, using multimodal (image plus text) product listings. They
vary each model's reasoning effort and measure decision quality, stated
confidence, calibration (how well stated confidence tracks actual accuracy),
and error correlation across models. Increased reasoning effort did not
produce a statistically meaningful improvement in decision quality, but it
did significantly raise stated confidence; most models were poorly
calibrated at every effort level; and errors were strongly correlated across
models — when one model erred on a task, others often erred too, frequently
converging on the same wrong product.

## Why it matters

Gives anyone building agents that report their own confidence (shopping
agents or otherwise) a concrete warning against treating "more reasoning
effort" or higher stated confidence as a reliability signal: here it tracked
effort, not correctness. Also relevant to any pipeline that uses
model-reported confidence as a deterministic guardrail or escalation
trigger — this result suggests calibration needs independent measurement
rather than being inferred from reasoning budget.

## Verification notes

Fetched the arXiv abstract page directly (arxiv.org, on the egress
allowlist). Methodology, benchmark composition, and the four main findings
are traced to the abstract text as summarized by the fetch. Exact effect
sizes and significance thresholds beyond "not statistically significant" /
"significantly" were not given in the abstract and are not claimed here.

## Updates

None yet.

## Related entries

None yet.
