---
slug: 2026-xie-judged-in-company-batch-llm-judge-bias
title: "Judged in Company: In-Context Batching Makes LLM Verdicts Depend on Other Items"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.40241
canonical_ids: ["arxiv:2610.40241"]
publisher_or_author: "Peng Xie, Amr Alanwar — arXiv (cs.CL)"
published: 2026-10-29
captured: 2026-10-31
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Squarely on lens 4 (LLM-as-judge validity): a quantified demonstration
  that batching items into one grading prompt — a common cost-saving
  practice — changes a meaningful fraction of individual verdicts depending
  on which other items share the batch, with a concrete, actionable
  mitigation.
verification: verified
---

# Judged in Company: In-Context Batching Makes LLM Verdicts Depend on Other Items

## Summary

To cut cost, practitioners often have an LLM grade many items in a single
prompt, assuming each item's verdict is independent of the other items and
their position. The authors test this across three judgment tasks
(detecting harm in social-media comments, grading short answers, predicting
review star ratings) using five open-weight models (4–9B parameters) and
four models (14–32B parameters). Reshuffling the same 2,000 items into
different random batches of 25 changed 11–22% of harm/grading decisions for
smaller models and 6–15% for larger ones — larger than the effect of simply
renaming item keys or rewording instructions — while AUROC against human
labels barely moved versus single-item grading. Decomposing the flips into
order, slot, and membership effects shows flip rates scale with the square
root of the variance that batch context adds, so small score shifts can
become large pass/fail decision changes; most inconsistency comes from
neighboring items' order and position, but a persistent effect from which
items share a prompt survives even after voting over permutations. On the
easiest task (star ratings), only 2.9–3.9% of decisions changed. The authors
recommend grading ambiguous items individually, using a cached prompt
prefix to recover most of the cost savings of batching, and reporting
agreement with single-item grading whenever items are in fact batched.

## Why it matters

A direct, quantified warning against a common LLM-as-judge cost-saving
shortcut — batching items into one grading call — showing it can flip
6–22% of individual verdicts depending on batch composition even though
aggregate accuracy (AUROC) looks unaffected; gives eval builders both the
failure mechanism and a concrete, low-cost mitigation (cached-prefix
single-item grading for ambiguous cases).

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.40241, v1 submitted
29 Oct 2026, cs.CL). The experimental setup (three tasks, nine models across
two size tiers, 2,000 items reshuffled into batches of 25), the 11–22%/6–15%
flip-rate figures, the 2.9–3.9% figure for the easiest task, and the
recommended mitigation are traced to the abstract text itself. No
independent corroboration of the raw reshuffling data was attempted.

## Updates

None yet.

## Related entries

None yet.
