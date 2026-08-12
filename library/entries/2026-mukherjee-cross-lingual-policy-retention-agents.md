---
slug: 2026-mukherjee-cross-lingual-policy-retention-agents
title: "Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.11110
canonical_ids: ["arxiv:2608.11110"]
publisher_or_author: "Sourabrata Mukherjee, Kalika Bali, Sunayana Sitaram — arXiv preprint (cs.CL); accepted to COLM 2026"
published: 2026-08-11
captured: 2026-08-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 3 (tool use and MCP) and lens 4 (evaluation): a
  large-scale (8 models, 6 benchmarks, 41 languages, 2.38M rollouts)
  action-level evaluation of tool-using agents that both quantifies a real
  reliability gap (cross-lingual action-policy retention) and identifies
  measurement artifacts that can distort eval results by up to 26x —
  directly actionable for anyone designing agent evaluation harnesses.
---

# Actions Speak Louder than Words: Measuring Cross-Lingual Policy Retention in Tool-Using Agents

## Summary
Rather than evaluating only final answers, the paper measures whether multilingual tool-using agents take consistent action sequences across languages — the actual steps/tool calls, not just outcomes. Across 8 models, 6 benchmarks, and 41 languages (2.38M rollouts), the authors identify five confounding factors that distort naive measurement and, after correcting for them, find frontier models retain only about 71-73% of their action policy across languages. Models frequently route non-English tasks through English intermediates, a pattern confirmed as causally significant, and performance deteriorates sharply below roughly 10B parameters. Separately, the authors show common measurement artifacts (e.g. regex-based trace extraction) can inflate or deflate reported performance by up to 26-fold.

## Why it matters
Two directly usable findings for building or evaluating multilingual/tool-using agents: (1) action-level consistency, not just final-answer accuracy, should be part of any evaluation harness for tool-using agents, since "actions are the product" for cost, latency, and auditability; and (2) naive trace-extraction methods can produce eval numbers that are off by an order of magnitude, a concrete pitfall to check for in any agent-eval pipeline.

## Verification notes
Read via the arXiv abstract page. The scale figures (8 models, 6 benchmarks, 41 languages, 2.38M rollouts), the 71-73% retention figure, the ~10B-parameter threshold, and the 26x measurement-artifact figure are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
