---
slug: 2026-liang-decode-developer-edits-ai-code
title: "Learning from 53.6K Real-World Developer Edits of AI-Generated Code"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.25130
canonical_ids: ["arxiv:2607.25130"]
publisher_or_author: "Jenny T. Liang, Mihika Bairathi, Wayne Chi, Ameet Talwalkar, Nishant Subramani, Valerie Chen — arXiv preprint"
published: 2026-07-27
captured: 2026-07-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on AI-assisted software development (lens 7): a genuinely large,
  real-world dataset (53.6K in-IDE edits from 1,000+ developers, not
  synthetic or lab-collected) with a measured behavioural finding (31% of
  trajectories remove the AI completion within 15 minutes) and a
  transferable practical result — small models finetuned on real edit data
  beat frontier LLMs at predicting the edit.
---

# Learning from 53.6K Real-World Developer Edits of AI-Generated Code

## Summary

Introduces DECODE, a dataset of over 53,000 authentic in-IDE code edits
that developers made to AI-generated code, spanning Python, TypeScript, and
JavaScript and collected from more than 1,000 developers. Two findings: (1)
editing-pattern analysis shows most edits happen within the first 15
minutes after accepting an AI completion, and 31% of edit trajectories end
in the AI completion being removed entirely; (2) using DECODE to finetune
open-source 3B-parameter models for the task of predicting a developer's
edit shows those finetuned small models "perform code edit prediction
tasks significantly better than frontier LLMs" (unverified — comparison
methodology and frontier-model baselines not read at capture). The authors
argue future AI programming tools should be designed around real
developer-edit data rather than synthetic or self-reported signals.

## Why it matters

A large, real (not synthetic) behavioural dataset that quantifies how often
and how fast developers actually reject or rework AI code completions — a
concrete correction to any team relying on acceptance-rate metrics alone,
since a completion can be "accepted" and then substantially edited or
removed within minutes. The finetuning result is a transferable practice:
task-specific small models trained on real edit data can outperform
general-purpose frontier LLMs for a narrow downstream prediction task,
relevant to anyone building edit-prediction or next-action tooling into a
coding agent.

## Verification notes

arXiv abstract page fetched directly (2026-07-29); title, full author
list, and "Submitted on 27 Jul 2026" confirmed. The dataset scale (53.6K
edits, 1,000+ developers, three languages), the 15-minute/31%-removal
finding, and the finetuned-3B-beats-frontier-LLMs claim all trace to the
fetched abstract text (the latter is a direct quote). The finetuning
comparison's methodology (which frontier models, what prompting) is not
independently checked — marked unverified above. Full paper not read at
capture.

## Updates

None yet.

## Related entries

None yet.
