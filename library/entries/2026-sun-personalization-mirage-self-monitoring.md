---
slug: 2026-sun-personalization-mirage-self-monitoring
title: "The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.04570
canonical_ids: ["arxiv:2608.04570"]
publisher_or_author: "Yushi Sun, Yanjie Zhang, Rui Sheng — arXiv preprint"
published: 2026-08-05
captured: 2026-08-06
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on evaluation, validation and deterministic guardrails: a
  quantified, benchmarked finding that a model's self-reported confidence or
  self-audit is an invalid signal for comparing models on a faithfulness
  failure mode, generalizable beyond the personalization use case to any
  guardrail design that leans on model self-report (lens 4).
---

# The Personalization Mirage: How LLMs Fabricate User Profiles, and Why Self-Monitoring Misleads

## Summary

Introduces MirageBench, a benchmark for "over-inference" (OI) — LLMs
fabricating user attributes beyond what evidence supports — built from 150
personas (stereotypical, counter-stereotypical, and neutral), 6
personalization tasks, a four-way faithfulness taxonomy scored by an
independent judge validated against blind human annotation on 400 claims
(Cohen's kappa 0.863 four-class, 0.900 binary), and a leaderboard of 12
models across 7 families over 143,616 judged claims. Every one of the 12
models over-infers on 35-49% of its claims (cross-model mean 41.6%). The
paper's central finding is a "Self-Monitoring Inversion": at the
model-selection level, a model's self-assessed over-inference rate is
*negatively* rank-correlated with its judge-measured over-inference rate
(rho = -0.60, p = 0.044, exploratory, wide bootstrap CI [-0.90, +0.06], n =
12) — the models that report the least fabrication tend to be judged as
fabricating the most. Within a single model, self-audit still ranks that
model's own claims moderately well (AUROC 0.58-0.83). Over-inference is
task-dependent (27-59%), and in a multi-turn pilot, inferred attributes
accumulate roughly linearly with little revision.

## Why it matters

A specific, quantified caution against a common evaluation shortcut: using
a model's own confidence or self-reported audit as a trust or
model-selection signal. The paper shows that signal can be actively
misleading when comparing models (the inversion), even though it remains
moderately useful within a single model's own outputs. Relevant to any
guardrail or evaluation design — not just personalization — that relies on
"ask the model if it's sure" rather than external verification.

## Verification notes

arXiv abstract page fetched directly (2026-08-06); title, authors (Yushi
Sun, Yanjie Zhang, Rui Sheng), and the "5 August 2026, 08:00:54 UTC" v1
submission timestamp confirmed. Every claim in the Summary — the benchmark
construction (150 personas, 6 tasks, judge validation kappas, 143,616
judged claims), the 35-49% (mean 41.6%) over-inference range, the
self-monitoring inversion (rho = -0.60, p = 0.044) and its stated
uncertainty (wide bootstrap CI, n = 12, "exploratory"), the within-model
AUROC range, and the task-dependence and multi-turn accumulation findings —
traces directly to the fetched abstract text. Full paper PDF not read at
capture; no independent corroboration attempted (pre-publication preprint).
Recorded as `verified` rather than `partial` because every claim above
traces to the source's own stated text and the abstract itself reports the
statistical uncertainty (wide CI, small n) rather than presenting it as
unqualified — consistent with this project's treatment of other
abstract-only arXiv captures. Upgrade path: read the full PDF for
per-model/per-task breakdowns and the multi-turn pilot's methodology.

## Updates

None yet.

## Related entries

None yet.
