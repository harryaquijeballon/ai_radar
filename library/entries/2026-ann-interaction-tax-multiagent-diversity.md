---
slug: 2026-ann-interaction-tax-multiagent-diversity
title: "The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.23541
canonical_ids: ["arxiv:2608.23541"]
publisher_or_author: "Summer Eunhyung Ann, Haokun Liu, Chenhao Tan — arXiv preprint (ICML 2026)"
published: 2026-08-24
captured: 2026-08-25
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on agent architecture and orchestration (lens 1): a stated,
  evidenced trade-off directly relevant to any multi-agent design decision
  — full-solution sharing between agents converges them onto the same
  answer and erases the diversity that motivated using multiple agents in
  the first place, tested across 11 tasks with matched compute budgets,
  with an explicit recommendation (control what information agents
  exchange, not just how many there are).
---

# The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams

## Summary

Investigates whether letting LLM agents share complete solutions with each
other helps or hurts multi-agent performance. The authors name "the
interaction tax": when agents exchange full solutions, they converge
rapidly onto the same answer, eliminating the diversity that was the
original justification for using multiple models or agents. Across 11
verifier-scored optimization tasks with matched computational budgets,
they find "full-solution interaction is a weak default" — independent
proposal generation (agents working without seeing each other's outputs)
preserves diverse approaches more effectively. Agents that do read each
other's outputs tend to stay anchored to their initial solution rather
than exploring alternatives; critique-based refinement (agents pointing
out flaws rather than sharing full solutions) helps only when the flagged
issues are easily identifiable and fixable. Their overall conclusion: what
information agents exchange, and when, matters more to multi-agent
performance than how many agents are involved.

## Why it matters

A directly actionable design lesson for anyone building a multi-agent
system to increase quality through diversity (e.g., ensemble reasoning,
multiple candidate solutions, debate-style architectures): sharing full
solutions between agents is likely to backfire by making them converge
instead of diversify, and the fix is to control the granularity and
timing of what agents see from each other — not simply to add more
agents. The paper gives a specific mechanism (critique-based refinement,
limited to identifiable/fixable issues) for when communication does help.

## Verification notes

Fetched directly from the arXiv abstract page (2026-08-25); title, all
three authors, and submission date (24 Aug 2026 per the abstract page,
25 Aug 2026 per the cs.MA "recent" listing — a routine one-day
announcement-lag discrepancy) confirmed, along with ICML 2026 acceptance.
The "interaction tax" framing, the 11-task/matched-budget experimental
design, and the finding that independent proposal generation outperforms
full-solution sharing all trace directly to the fetched abstract text —
the authors' own stated results. Full paper (per-task results, the
critique-based-refinement conditions) not read at capture; upgrade path:
read the full PDF for the task-by-task breakdown.

## Updates

None yet.

## Related entries

None yet.
