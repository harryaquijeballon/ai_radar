---
slug: 2026-vrdoljak-expertcrowd-swe-benchmark
title: "ExpertCrowd-SWE: Measuring Frontier Coding Agents on Expert-Authored Engineering Tasks in Unfamiliar Codebases"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.13246
canonical_ids: ["arxiv:2611.13246"]
publisher_or_author: "Josip Vrdoljak, Akash Singh, Bas Steunebrink, Alex Yarotsky, John Lorenzo, Achille Nicoletti, Sam Pigott — arXiv preprint (cs.AI, cs.SE)"
published: 2026-11-09
captured: 2026-11-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation (lens 4): a contamination-resistant
  benchmark (practitioner-authored tasks, sealed solutions, held-back
  majority) across 87 real-world multi-file codebases, with quantified,
  model-separating results across seven frontier models — directly usable
  for anyone choosing or comparing coding agents on realistic,
  unfamiliar-codebase work.
---

# ExpertCrowd-SWE: Measuring Frontier Coding Agents on Expert-Authored Engineering Tasks in Unfamiliar Codebases

## Summary

Introduces EC-SWE, a benchmark of 100 multi-file software-engineering tasks
written by practicing engineers for large codebases they did not write
themselves. Each task pairs a change request with a pinned repository
commit, a sealed reference solution, and a weighted grader giving partial
credit and enforcing merge-blocking rules. Tasks come from 87 open-source
projects across 11 languages; the median change request is 148 words and
the median reference solution changes 471 lines. The authors evaluated
seven frontier models over five runs each (3,495 scored runs total) and
released only 24 of the tasks publicly, holding back 76 to limit
contamination. Scores: Claude Opus 5.5 led at 67.3%, GPT-6 Astra followed
at 63.7% (not statistically distinguishable from the top model), Claude
Fable 5.1 at 46.5%, Gemini 3.8 Flash at 40.0%, and Qwen 3.8 Max, DeepSeek
V4.1 Flash, and Grok 4.6 clustered at 32–34% (statistically
indistinguishable from each other) — a 35-point spread overall. No task
was fully solved by every model, and on 80 of the 100 tasks no model
earned full credit across all five runs. Median steps per run ranged from
33 to 166 depending on the model, with little relationship to score.

## Why it matters

A realistic, contamination-resistant yardstick for comparing coding agents
on the kind of work builders actually assign them — unfamiliar, multi-file
codebases with partial-credit, merge-blocking grading rather than toy
single-file tasks. The 35-point model spread and the finding that step
count doesn't track score are directly usable evidence for teams deciding
which model or harness to deploy for real engineering work, and the
sealed/held-back task design is itself a transferable pattern for building
benchmarks that resist contamination.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.13246,
2026-11-12); title, authors, submission date (9 Nov 2026), and categories
(cs.AI primary, cs.SE secondary) confirmed there. The benchmark design and
all quantified figures (task counts, median sizes, run counts, per-model
scores, spread, step-count range) trace directly to the fetched abstract
text — the authors' own stated results. Full paper (per-task breakdowns,
statistical test details) not read at capture — upgrade path noted.

## Updates

None yet.

## Related entries

None yet.
