---
slug: 2026-adeniji-auditing-behavioral-detectors
title: "What the Trace Shows and What the Label Says: Auditing Behavioral Detectors in Agent Evaluation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.30491
canonical_ids: ["arxiv:2610.30491"]
publisher_or_author: "Idunnuoluwa A. Adeniji, Shilpika, Michael E. Papka"
published: 2026-10-21
captured: 2026-10-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails):
  names a specific, quantified failure mode in automated agent-trace
  labeling ("silent tool-output override"), ties it to a controlled
  tool-corruption experiment with human-reviewed ground truth, and gives an
  actionable reporting recommendation — directly serving the profile's core
  lens for building defensible agent evaluation pipelines.
---

# What the Trace Shows and What the Label Says: Auditing Behavioral Detectors in Agent Evaluation

## Summary
The paper audits three trace-level behavioral detectors commonly used in
LLM-agent evaluation, which reduce execution traces to labels for final-
answer correctness, visible re-verification, and fault propagation. The
authors argue these labels can fail to reflect what the trace actually
shows. To test this, they built a tool-use setting on GSM8K where agents
call a calculator whose outputs are sometimes corrupted, so the true tool
output is always known; six production models were evaluated on 30
problems each, with humans reviewing 90 traces and an ablation run on
execution limits (step/token budgets) for two models.

The three automated signals can disagree systematically. The main failure
mode identified is "silent tool-output override": the model substitutes a
different, often-correct value without calling the tool again; the bad
corrupted value stops propagating, but the automated verification detector
records no re-check occurred, misclassifying the trace. Human review fully
agreed with automated labels for final correctness (67/67), fault impact
(19/19), and fault relevance (18/18); for verification, agreement was only
67/81, with all 14 disagreements falling into four recurring patterns.
Execution limits materially change reported results: one model's score
ranged from 21/30 to 27/30 correct purely as a function of budget, while
another stayed within a tighter 27/30–29/30 band. The authors recommend
that automated labels always ship with their supporting trace evidence, a
note on whether the detector's underlying question even applies to that
trace, whether an execution limit truncated the run, and any human
corrections.

## Why it matters
This is a direct, quantified warning against trusting automated
agent-evaluation labels (including LLM-as-judge-style behavioral detectors)
without the underlying trace evidence — squarely the profile's core lens
for making agent output trustworthy enough for research/policy use. The
"silent tool-output override" failure mode is a concrete thing to check for
in any pipeline that scores agent trajectories automatically, and the
execution-limit sensitivity finding is a reusable caution for anyone
comparing agent benchmark scores across runs with different budgets.

## Verification notes
Read directly from the arXiv abstract page (arXiv:2610.30491, v1, submitted
21 Oct 2026, 22:18:16 UTC). All quantified figures (67/67, 19/19, 18/18,
67/81, 14 disagreements, the 21/30–27/30 and 27/30–29/30 budget-sensitivity
ranges) are stated directly in the abstract and traceable to it; the
controlled tool-corruption design with known ground truth and independent
human review supports `verified`. Full paper and independent replication
not checked this run.

## Updates

- None yet.

## Related entries
None yet.
