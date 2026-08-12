---
slug: 2026-tian-gala-agentic-root-cause-analysis
title: "GALA+: Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.08968
canonical_ids: ["arxiv:2608.08968"]
publisher_or_author: "Yifang Tian, Yaming Liu, Zichun Chong, Zihang Huang, Yiran Li, Hans-Arno Jacobsen — arXiv preprint (cs.SE, cs.AI); to appear at ASE '26"
published: 2026-08-10
captured: 2026-08-11
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 5 (observability and debugging): a microservice root-cause-
  analysis agent that bounds LLM exploration with service-dependency
  graphs, evaluated with both an industry-co-developed automated score
  (SURE-Score) and independent human SRE review — a reusable pattern with
  practitioner-validated evaluation, not just a self-reported benchmark.
---

# GALA+: Graph-Augmented LLM Agents for Root Cause Analysis and Incident Response

## Summary
GALA+ combines service-dependency graphs with LLM agents for microservice root cause analysis, using the graph to bound exploration and refine diagnosis through localized, multi-modal evidence. It introduces STRIX, a scoring module built on trace and graph structure, and SURE-Score, an evaluation framework developed jointly with industry site-reliability engineers. GALA+ surpasses the best LLM-based baseline by more than 25 percentage points in AC@1 (accuracy at rank 1) and received the highest ratings from both SURE-Score and independent human SRE evaluation. Output includes ranked diagnoses, incident summaries, and actionable recommendations, extending beyond simple fault ranking. Accepted to appear at ASE '26 (IEEE/ACM International Conference on Automated Software Engineering, Munich, October 2026).

## Why it matters
A reusable architectural pattern — bound an LLM agent's exploration space with a structural graph of the system it's diagnosing, rather than letting it search unconstrained — plus a rare example of an agent-evaluation framework built with practitioner input (SURE-Score) and checked against independent human judgment, addressing the common concern about self-reported agent benchmarks.

## Verification notes
Read via the arXiv abstract page. The AC@1 gain, SURE-Score/human-evaluation claims, and the ASE '26 acceptance note are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
