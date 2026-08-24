---
slug: 2026-sun-hansen-bc-bench-erp-agentic-engineering
title: "BC-Bench: Evaluating Agentic Engineering in a Domain-Specific Language for ERP"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.20851
canonical_ids: ["arxiv:2608.20851"]
publisher_or_author: "Haoran Sun, Klaus Marius Hansen — arXiv preprint (cs.SE)"
published: 2026-08-24
captured: 2026-08-24
relevance:
  social_science: n/a
  ai_engineering: medium
rationale: >-
  Medium on lens 4 (evaluation): a real-world-derived benchmark (101 tasks
  from two Microsoft production repositories) for agentic coding in a
  narrow domain-specific language, whose headline finding — model choice
  matters more than agent-harness choice for bug-fixing in this setting,
  and general-benchmark gains don't reliably transfer — is a useful,
  actionable but narrow-scope data point.
verification: verified
---

# BC-Bench: Evaluating Agentic Engineering in a Domain-Specific Language for ERP

## Summary

BC-Bench is a benchmark for evaluating AI coding agents on real-world enterprise resource planning (ERP) development tasks written in AL, the domain-specific language for Microsoft Dynamics 365 Business Central. It comprises 101 manually curated tasks drawn from two Microsoft-owned production repositories, covering code generation, test generation, and multimodal problem statements, reflecting authentic ERP development workflows. In the bug-fixing category, the authors report that under their evaluated settings, differences in resolution rate between models are larger than differences between the two evaluated agent harnesses, and that improvements measured on general-purpose coding benchmarks do not consistently transfer to AL.

## Why it matters

A concrete caution for teams deploying coding agents on niche or enterprise domain-specific languages (lens 4): general-purpose benchmark performance is not a reliable proxy for performance in a narrow DSL, and in this ERP setting, which underlying model is used matters more than which agent harness wraps it — a useful prioritization signal when budgeting evaluation effort for a domain-specific coding-agent deployment.

## Verification notes

Read via the arXiv abstract page, which reports the dataset provenance (two Microsoft production repositories, 101 tasks) and the bug-fixing finding directly. Not independently corroborated against a second source or the full paper.

## Updates

None yet.

## Related entries

None yet.
