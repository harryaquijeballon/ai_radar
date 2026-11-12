---
slug: 2026-zhang-agent-eval-framework-comparison
title: "Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.14493
canonical_ids: ["arxiv:2611.14493"]
publisher_or_author: "Howard Zhang, Chuck Arvin, Logan Brown, Mihir Bhatia, Neelu Choudhary, Lily Miao — arXiv preprint (cs.AI/cs.SE), accepted KDD 2026"
published: 2026-11-10
captured: 2026-11-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation and observability (lenses 4, 5): a
  KDD-accepted, quantified comparison of three evaluation approaches
  (trace-based LLM judging, text-only LLM judging with red-teaming,
  deterministic heuristics) on real enterprise analytics agents, with a
  concrete, actionable recommendation (pair trace-based functional
  evaluation with adversarial red-teaming) backed by measured
  precision/recall and failure-overlap figures.
---

# Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents

## Summary

Compares three evaluation approaches for LLM-based analytics agents —
trace-based LLM judging, text-only LLM judging combined with
red-teaming, and deterministic heuristics — applied to two real analytics
agents using frozen execution traces, across three phases. Stability
(Phase 1): 97% of configurations met the stability threshold, with no
dependence on which agent was tested. Detection (Phase 2): on 72
ground-truth test cases, the trace-based framework had the best
precision-recall balance (F1 = 0.90); the text-only approach matched its
recall but produced roughly 5x more false alarms. Discovery (Phase 3): the
evaluations together surfaced 24 novel failures, with zero overlap between
functional testing and security red-teaming — the two approaches found
entirely different problems. The authors conclude that the information
available to an evaluation harness determines evaluation quality, that
functional and security evaluation are complementary rather than
redundant, and that LLM-based harnesses can catch subtle errors human
reviewers miss.

## Why it matters

A directly actionable recipe for teams building evaluation harnesses
around production agents: trace-based evaluation (giving the judge access
to execution traces, not just final text) materially reduces false alarms
versus text-only judging at matched recall, and security red-teaming finds
failures functional testing structurally cannot — the two must be paired,
not chosen between. The zero-overlap finding is itself the key design
lesson: a harness with only one of these approaches will systematically
miss an entire category of real failures.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.14493,
2026-11-12); title, authors, submission date (10 Nov 2026), and KDD 2026
acceptance confirmed there. The three-phase design and all quantified
figures (97% stability rate, F1 = 0.90, ~5x false-alarm ratio, 24 novel
failures with zero overlap) trace directly to the fetched abstract text.
Full paper (the specific heuristics used, per-agent breakdowns) not read
at capture — upgrade path noted.

## Updates

None yet.

## Related entries

None yet.
