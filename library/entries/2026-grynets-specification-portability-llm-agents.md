---
slug: 2026-grynets-specification-portability-llm-agents
title: "Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.21208
canonical_ids: ["arxiv:2608.21208"]
publisher_or_author: "Oleg Grynets, Oleksii Ilchuk, Dariia Zatulna, Vasyl Lyashkevych — arXiv preprint (cs.SE)"
published: 2026-08-24
captured: 2026-08-24
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on lens 3 (tool use and interoperability, extended to
  specification-driven-development artifacts): a quantified, large-scale
  demonstration that specifications produced by one LLM development agent
  are not safely portable to another — directly actionable for any team
  treating specs as agent-neutral artifacts in a multi-agent or
  multi-vendor workflow.
verification: verified
---

# Specification Portability Across LLM Development Agents: Cross-Agent Compatibility in Specification-Driven Software Migration

## Summary

Using Oracle-to-PostgreSQL database migration as a test case, the authors evaluate a specification-first migration pipeline on 1,006 PL/SQL files: 623 (62%) were successfully regenerated into specifications and 380 (38%) of the resulting scripts executed successfully in PostgreSQL 16. They then run cross-agent experiments across Amazon Kiro, Google Gemini, and GitHub Copilot on a larger set of 1,802 Oracle scripts with PostgreSQL implementations, feeding one agent's generated specification to a different agent. Cross-agent transfer degrades sharply and unevenly: the worst case (Gemini consuming a Kiro-generated specification) produces a Token F1 of 0.035, SQL syntax validity of 2.33%, and AST mean similarity of 0.015. The authors conclude that specifications in heterogeneous specification-driven-development (SDD) workflows should not be treated as agent-neutral artifacts by default — they require adaptation when moved between agents.

## Why it matters

A concrete warning, backed by a large real-code evaluation, against a natural but risky assumption in multi-agent or multi-vendor coding workflows: that a specification produced by one LLM agent will transfer cleanly to another. The magnitude of the worst-case degradation (near-zero AST similarity) makes this an actionable data point for teams designing specification-driven pipelines that mix agent vendors, or for teams considering switching agent providers mid-project.

## Verification notes

Read via the arXiv abstract page, which reports the migration and cross-agent transfer figures directly. Not independently corroborated against a second source or the full paper.

## Updates

None yet.

## Related entries

None yet.
