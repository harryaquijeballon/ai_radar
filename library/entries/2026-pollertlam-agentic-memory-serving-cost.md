---
slug: 2026-pollertlam-agentic-memory-serving-cost
title: "Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.11879
canonical_ids: ["arxiv:2608.11879"]
publisher_or_author: "Natchanon Pollertlam, Witchayut Kornsuwannawit — arXiv preprint (cs.CL)"
published: 2026-08-13
captured: 2026-08-13
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 2 (harness and context engineering) and lens 5
  (observability, cost and latency monitoring): benchmarks the actual
  serving cost and accuracy of three real agentic-memory systems (Mem0,
  Hindsight, Mastra) against baselines, with a specific, actionable warning
  that cost cannot be predicted from conversation length alone — directly
  usable for anyone choosing or budgeting a memory system for a long-running
  agent.
---

# Total Recall at What Cost? Benchmarking the Serving Cost of Agentic Memory Systems

## Summary
Benchmarks the operational cost of three memory systems used by conversational agents — Mem0, Hindsight, and Mastra Observational Memory — against baseline approaches, across dialogues of up to 400 turns, measuring serving cost and accuracy on 665 LoCoMo questions. A memory system's serving cost cannot be predicted from conversation length and message size alone: a regression tracking those two reference strategies misses the actual memory systems by 18-69%. Cost-effectiveness varies dramatically by system and backbone model, with break-even points ranging from tens of turns to never occurring within 400 turns. No system wins on both axes: accuracy spans 21-54%, and backbone choice drives cost as much as the memory-system choice does.

## Why it matters
A rare head-to-head cost/accuracy benchmark of real, named agentic-memory products rather than a single proposed method — directly useful for anyone budgeting or selecting a memory system for a long-running conversational agent. The core warning (conversation length is not a reliable cost predictor; backbone model choice matters as much as memory-system choice) is an actionable pitfall to check before committing to a memory architecture.

## Verification notes
Read via the arXiv abstract page (2026-08-13). The three named systems, the 400-turn/665-question benchmark design, the 18-69% cost-prediction miss, the 21-54% accuracy range, and the backbone-cost finding are quoted/paraphrased directly from the abstract. Full paper (benchmark construction, per-system breakdown) not read at capture; findings not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
