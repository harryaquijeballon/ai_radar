---
slug: 2026-wu-buggymle-ml-engineering-difficulty
title: "BuggyMLE: Scaling Machine Learning Engineering Difficulty with Bug Injection"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.25088
canonical_ids: ["arxiv:2611.25088"]
publisher_or_author: "John Wu, Rushi Qiang, Yuchen Zhuang, Guowang Li, Girish Narayanswamy, Max Xu, Sam Schmidgall, Mark Malhotra, Shwetak Patel, Jimeng Sun, Daniel McDuff, Bo Dai, Xin Liu — arXiv preprint"
published: 2026-11-18
captured: 2026-11-21
relevance:
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails): a
  difficulty metric validated against solve rates across eight public
  coding benchmarks, plus a benchmark-construction method (controlled bug
  injection) that directly addresses benchmark saturation for ML-engineering
  agent evaluation.
---

# BuggyMLE: Scaling Machine Learning Engineering Difficulty with Bug Injection

## Summary

Motivated by the need for agents that can do machine-learning-engineering
work (multi-file repository edits, debugging training runs) rather than
single-file coding, the authors note that existing MLE benchmarks mostly
allow only single-file edits while repository-level software-engineering
benchmarks are quickly saturating. They introduce the Code Complexity
Index (CCI), a difficulty metric built from ten structural features, and
show it predicts average solve rates across eight public coding
benchmarks well, with patch size and structural complexity as the
strongest predictors. Guided by CCI, they build BuggyMLE, a framework in
which agents inject controlled bugs into working ML repositories,
producing over 6,600 bug-injected variants from 222 source repositories.
This yields BuggyMLE-Bench-Lite, a difficulty-graded, repository-level
version of MLE-Bench Lite on which the top solve rate across 14 evaluated
models falls from roughly 95% to 9% as difficulty increases. A three-level
training curriculum built from 200 additional repositories is then used to
fine-tune a Qwen3.5-9B model, which approaches frontier-model performance
on the benchmark and also improves on non-ML tasks — its SWE-bench Lite
resolve rate rising from 24% to 33%.

## Why it matters

For anyone building or selecting evaluations for coding or ML-engineering
agents: a validated, structural (not just outcome-based) difficulty metric
usable to grade existing benchmarks or construct new ones, plus evidence
that a repository-level, bug-injection benchmark can still discriminate
between models (9%-95% solve rate) where simpler benchmarks have
saturated — directly useful for anyone whose current eval suite no longer
separates strong from weak agents.

## Verification notes

arXiv abstract page fetched 2026-11-21 (paraphrased summary; full abstract
text not reproduced verbatim due to tool quoting limits). Submission
history shows v1 submitted Wed, 18 Nov 2026, 19:26:15 UTC — within this
run's discovery window (2026-11-20 → 2026-11-21) and the 7-day eligibility
cap. Category: cs.AI. Figures (8 benchmarks, 6,600+ variants/222
repositories, 95%->9% solve-rate range across 14 models, 24%->33% SWE-bench
Lite transfer) are traced to the fetched summary; full benchmark tables not
read at capture, no independent secondary corroboration attempted (new
preprint).

## Updates

None yet.

## Related entries

None yet.
