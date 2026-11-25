---
slug: 2026-koc-shellbench-model-harness-benchmark
title: "ShellBench: What Matters More for AI Agents, Models, or Harness for Everyday Tasks"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.32946
canonical_ids: ["arxiv:2611.32946"]
publisher_or_author: "Vincent Koc, Aditya Washikar, Rishab Naveen Venkataraman, et al."
published: 2026-11-25
captured: 2026-11-25
relevance:
  ai_engineering: high
  social_science: n/a
verification: verified
rationale: >-
  Lens 1 (agent architecture and orchestration): a large, realistic
  benchmark (100 everyday tasks drawn from over 10 million user requests;
  53,100 rollouts across 12 models, 5 harnesses, 3 reasoning levels) that
  directly answers a standing question for anyone building agent products —
  whether to invest in model choice or harness choice — with a
  quantified, actionable answer and named cost/performance trade-offs
  between specific models.
---

# ShellBench: What Matters More for AI Agents, Models, or Harness for Everyday Tasks

## Summary

The authors introduce ShellBench, a benchmark of 100 everyday agent tasks drawn from over 10 million real user requests, each run in a realistic workspace with messy files and conflicting data sources and graded on both correctness and safety (20% of tasks are released publicly). They evaluated 12 models across 5 agent harnesses at 3 reasoning levels, producing 53,100 rollouts. The central finding is that model choice affects performance more than harness choice does: the three leading models differed by only 1.1 percentage points from each other, while harness choice had comparatively little effect on performance or safety (pass@1 ranged from 42.9 for Claude Code to 45.2 for OpenClaw across harnesses). Within models, GPT-6.1 Sol passed 61.4% of attempts at roughly one-sixth of GPT-6 Astra's estimated token cost per attempt, while GPT-6 Astra had the top overall score at 62.5%.

## Why it matters

A directly actionable allocation-of-effort finding for teams building agent products: given the benchmark's scale and realism (real user requests, multiple harnesses and reasoning levels tested), investment in model selection is shown to matter more than investment in harness engineering for this task distribution, and the GPT-6.1 Sol vs. GPT-6 Astra comparison gives a concrete cost/performance trade-off a team could use when choosing a model for a cost-sensitive deployment.

## Verification notes

Fetched directly from arXiv; abstract and submission history (v1, 24 November 2026, appearing in the 25 November cs.SE listing — a one-day announcement lag consistent with routine processing) confirmed on the page. Load-bearing figures (53,100 rollouts; 1.1-point spread among leading models; 61.4% vs. 62.5% pass rates; pass@1 range of 42.9–45.2 across harnesses) are as stated in the abstract. The full task taxonomy and safety-grading methodology were not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

None yet.
