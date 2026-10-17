---
slug: 2026-heander-codehealth-agentic-review-cost
title: "CodeHealth Predicts the Token Cost of Agentic Code Review: A Pre-Registered Study of 465 Agent-Authored Pull Requests"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.21914
canonical_ids: ["arxiv:2610.21914"]
publisher_or_author: "Lo Gullstrand Heander, Markus Borg, Emma Söderberg, Christofer Rydenfält — arXiv preprint"
published: 2026-10-15
captured: 2026-10-17
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on evaluation/guardrails (lens 4) and AI-assisted software development
  (lens 7): a pre-registered observational study with a quantified, directly
  actionable finding — each point of baseline code-quality (CodeHealth) is
  associated with 3.5-6.1% lower token cost in agentic review/fix pipelines,
  independent of PR size.
---

# CodeHealth Predicts the Token Cost of Agentic Code Review: A Pre-Registered Study of 465 Agent-Authored Pull Requests

## Summary

Per the arXiv abstract page (v1 submitted 15 Oct 2026), the paper is a pre-registered observational study asking whether baseline code quality (measured by the "CodeHealth" metric) predicts the token cost of a multi-agent LLM pipeline that reviews and fixes code, over and above pull-request size. The authors analysed 465 agent-authored PRs drawn from 246 repositories in the AIDev dataset, stratified by CodeHealth and PR footprint with repository caps, run through a frozen five-agent review-and-fix pipeline using three different LLMs. Reported findings: for all three LLMs, the CodeHealth coefficient on token cost was negative with a 95% confidence interval excluding zero — "each CodeHealth point was associated with 3.5% to 6.1% lower token cost." CodeHealth was unrelated to PR footprint (size), so the authors argue size does not explain the association. Two of three pre-registered code smells predicted fix cost. Batch fixing left median CodeHealth unchanged. Exploratory analysis placed the association in the review stage specifically, where agents iterated more on unhealthy code without writing more review comments, and adjusting for the size of the scored files absorbed the association — interpreted by the authors as mediation via file size. The authors note the study is observational, so the associations do not establish causation. (32 pages, 6 figures, 16 tables; CC status not confirmed from the abstract page.)

## Why it matters

A directly budgetable relationship for anyone running agentic code review at scale: baseline code quality is not just a correctness concern but a measurable cost driver of the review pipeline itself, and the effect survives controlling for PR size — giving a concrete lever (raise baseline CodeHealth) distinct from "shrink the diff," which is the lever most context-engineering advice defaults to.

## Verification notes

Source reachable (arXiv abstract page). Claims traced to the abstract-level summary only; the full 32-page paper (methodology detail, smell definitions, mediation analysis) was not opened, and the quantified ranges were not independently corroborated beyond the abstract page's own statement of them.

## Updates

None yet.

## Related entries

None yet.
