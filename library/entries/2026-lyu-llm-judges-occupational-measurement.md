---
slug: 2026-lyu-llm-judges-occupational-measurement
title: "Right Order, Wrong Scale: Auditing LLM Judges for Occupational AI Measurement"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.02492
canonical_ids: ["arxiv:2610.02492"]
publisher_or_author: "Harry Lyu, Neil Thompson — arXiv preprint"
published: 2026-10-01
captured: 2026-10-05
relevance:
  social_science: high
  ai_engineering: high
verification: verified
rationale: >-
  Social-science lens 5/6 (LLMs as research instruments, with validity
  problems) and AI-engineering lens 4 (LLM-as-judge validity): an audit
  showing that judge ranking agreement does not imply calibrated acceptance
  rates, with a concrete validation recommendation.
---

# Right Order, Wrong Scale: Auditing LLM Judges for Occupational AI Measurement

## Summary

The authors introduce O*NET-BENCH, an evaluation suite built on 45,796 worker ratings, to test whether LLM judges accurately assess AI outputs on workplace tasks. They evaluate 33 judge configurations across six model families on 4,501 test ratings. Reported findings (per the arXiv abstract page): 25 configurations reach pair accuracy of at least 0.60, though a TF-IDF baseline nearly matches the strongest judge; judges' estimated acceptance rates range from 3.0% to 97.9%, against 61.1% for occupation-matched workers; fine-tuning improves response ordering but reduces worker agreement at task and occupation levels; calibrated scores explain at most 8.5% of individual worker-rating variance. The authors conclude that ranking agreement alone is insufficient for occupational measurement and recommend validating judges against the acceptance rates and aggregates they will be used to estimate.

## Why it matters

Researchers using LLM judges to measure AI's occupational and task-level effects, and builders using judges inside evaluation pipelines, should not treat good pairwise ordering as evidence of calibrated levels. The practical step is to validate a judge against human acceptance rates and the aggregates it will estimate before using its scores in research or policy claims.

## Verification notes

Source reachable (arXiv abstract page); figures traced to the abstract as retrieved. The abstract page gave submission date 2026-10-01. Full text was not read and results were not independently reproduced.

## Updates

None yet.

## Related entries

[2026-hardy-agent-evaluation-reliability](2026-hardy-agent-evaluation-reliability.md) — related evaluation-validity work.
