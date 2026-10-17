---
slug: 2026-yang-skip-the-compressor-whole-file-selection
title: "Skip the Compressor: Coding Agents Fix More Issues When They Pick Whole Files"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.21073
canonical_ids: ["arxiv:2610.21073"]
publisher_or_author: "Xiaocong Yang, Rishit Chatterjee, Himanshu Udupi, Vikram Ramavarapu, ChengXiang Zhai — arXiv preprint"
published: 2026-10-15
captured: 2026-10-17
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on harness/context engineering (lens 2): a controlled, equal-budget
  comparison on 300 SWE-rebench issues showing whole-file selection
  outperforms token-compression and chunk-retrieval context strategies by
  6-13 points of issue-resolution rate across two models, with a stated
  failure mechanism (retrievers miss files; compressors break patch
  application).
---

# Skip the Compressor: Coding Agents Fix More Issues When They Pick Whole Files

## Summary

Per the arXiv abstract page (v1 submitted 15 Oct 2026), the paper argues that coding agents working on large repositories need both the right files and their exact, unmodified text to produce a working patch. Common context strategies fall short in different ways: retrievers rank code by similarity to the issue description rather than by whether the file must change, and compressors delete text to fit a token budget, which the authors argue breaks patch application. At an equal per-issue context budget, the authors' selector (CQ2-CARE), which spends the budget on showing whole files verbatim rather than pruning or chunk-retrieving, resolves more issues on 300 recent SWE-rebench issues, graded by the benchmark's own tests. Reported figures: CQ2-CARE resolves 43.7% of issues with GPT-5.6 and 46.7% with Claude Opus 5 — 6.3 points higher than the best of three compressor baselines (either model), 9.3 points higher than the best of three retriever baselines with GPT-5.6 (12.7 points with Claude Opus 5), and still ahead (by 0.7-1.7 points vs. a retriever trained specifically for issue resolution, and 2.0-7.3 points vs. a compressor trained for issue resolution). The authors attribute baseline failures to retrievers missing files that need edits and to compressors altering text so that patches no longer apply cleanly, and argue whole-file selection needs no compression model at all.

## Why it matters

A concrete, benchmarked answer to a live context-engineering question — "retrieve relevant chunks," "compress to fit budget," or "select whole files" — for exactly the case this profile's policy-simulation interest cares about: agent output that must be verifiably correct (a patch that applies and passes tests), not merely plausible. The finding that compression itself is a failure mode, not just a cost-saving trade-off, is directly actionable for harness design.

## Verification notes

Source reachable (arXiv abstract page). Claims traced to the abstract-level summary only; the full paper (baseline implementation details, statistical significance of the point differences) was not opened, and the figures were not independently corroborated beyond the abstract page's own statement of them.

## Updates

None yet.

## Related entries

None yet.
