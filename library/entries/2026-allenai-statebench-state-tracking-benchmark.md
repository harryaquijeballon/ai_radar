---
slug: 2026-allenai-statebench-state-tracking-benchmark
title: "StateBench: Testing How Language Models Track State Changes Over Long Documents"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://huggingface.co/blog/allenai/statebench
canonical_ids: ["repo:allenai/state-bench"]
publisher_or_author: "Ai2 (Allen Institute for AI)"
published: 2026-11-03
captured: 2026-11-04
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on evaluation/validation/deterministic guardrails (lens 4): a
  released benchmark with a clean four-level difficulty ladder isolating
  exactly which kind of state-tracking (variable reassignment, running
  totals, cross-variable reference chains) breaks down in frontier models,
  with a concrete architectural lead (Gated DeltaNet) for the hardest level.
verification: verified
---

# StateBench: Testing How Language Models Track State Changes Over Long Documents

## Summary

A benchmark for how well language models track changing information about
entities across long documents (e.g., variable reassignment in code, plot
state in a story), isolating four difficulty levels that hold the number of
variables and assignment positions fixed and vary only the assignment type:
r-trivial (set once, never changes), aperiodic (reassigned; only the latest
value matters), soluble (updates build on the current value, e.g. running
totals), and general finite (one variable can take another's value, creating
dependency chains — related to the S5 permutation-tracking problem). Tested
on pretrained open models (Olmo 3, Olmo Hybrid with Gated DeltaNet layers,
and smaller 275M/2.7B variants), four frontier models (Gemini 3.8 Flash,
Claude Opus 5.5, GPT-6 Sol and Luna), and models trained from scratch on the
benchmark. Pretrained models handle r-trivial well, lose accuracy on
aperiodic as inputs grow, and stay at chance on general finite; problem
framing matters independently of content, since the same problems framed as
spreadsheet edits (versus RULER-style) dropped small hybrid/Gated-DeltaNet
models to near chance. Frontier models handle r-trivial and aperiodic well
but accuracy on soluble and general finite drops sharply with length, to 13%
or lower on the longest general-finite problems. When trained directly on
the task, Gated DeltaNet and hybrid models generalize well on the first three
levels to very long sequences; transformers degrade with length and never
learn the general-finite level; the Gated DeltaNet variant with a more
flexible memory update stays near-perfect to about 10x its training length
on the hardest level. Dataset released on Hugging Face (allenai/state-bench).

## Why it matters

A precise, released diagnostic for exactly the kind of state-tracking that
agent memory, tool-state, and long-document reasoning pipelines depend on:
"does my agent's context-management approach actually survive chained
cross-variable dependencies, or only simple reassignment?" is now a
directly testable question, and the finding that problem framing alone
(spreadsheet-style vs. RULER-style) changes small-model performance is a
concrete warning against assuming a benchmark result transfers across how a
real task happens to present the same underlying state-tracking problem.

## Verification notes

Fetched directly from the Hugging Face blog post (captured 2026-11-04;
published 2026-11-03). The four-level taxonomy, the models tested, and all
stated accuracy/generalization figures trace to the fetched text. The
underlying arXiv paper (if any) and the full Hugging Face dataset card were
not separately opened at capture.

## Updates

None yet.

## Related entries

None yet.
