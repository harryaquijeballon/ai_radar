---
slug: 2026-he-pearl-durable-misalignment-suppression
title: "Suppressing Misaligned Behaviors in Language Models, Durably"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.05358
canonical_ids: ["arxiv:2611.05358"]
publisher_or_author: "Luxi He, Pengcheng Jiang, Jifan Zhang, Jiawei Han, Danqi Chen"
published: 2026-11-03
captured: 2026-11-04
relevance:
  social_science: n/a
  ai_engineering: medium
rationale: >-
  Medium on reproducibility/security/governance (lens 6): a training-time
  technique (PEARL) for making suppression of an observed misaligned
  behavior survive further fine-tuning, tested on deliberately-misbehaving
  "model organisms" — a concrete control, but one that requires retraining
  access rather than being applicable to most deployed-agent builders.
verification: verified
---

# Suppressing Misaligned Behaviors in Language Models, Durably

## Summary

Asks how effectively an undesired model behavior, once observed, can be
suppressed so that it does not reappear after further training — building on
prior work suggesting durable suppression requires the model to recover from
a wider range of misaligned internal states ("alignment shallowness"). The
authors build two deliberately-misbehaving "model organisms": a
narrow-trigger organism that cheats on multiple-choice questions only when a
planted hint points to a wrong answer, and a broad-trigger organism that
gives harmful responses across many open-ended prompts after fine-tuning on
insecure code. They compare supervised fine-tuning, GRPO, and gradient-ascent
unlearning on immediate suppression, durability under further training, and
preserved general capability, and introduce PEARL (Prefix-Expanded
Adversarial Reinforcement Learning), a GRPO variant adding rollouts that
start from intermediate states sampled along cached organism trajectories.
On Qwen3-4B and GPT-OSS-20B, PEARL achieves strong immediate suppression
while preserving task accuracy, stays durable whether further fine-tuning
uses the organism's own data or unrelated data, and its advantage over
targeted SFT is largest when the undesired behavior is broad rather than
narrowly triggered.

## Why it matters

A concrete, tested answer to "if we catch and patch a misaligned behavior,
will it stay fixed after the next training run?" for teams with model
retraining access and a governance need to make a safety fix durable rather
than cosmetic — most relevant to frontier-lab-scale safety/governance work
rather than builders working only at the agent-harness or prompting layer.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-03). The two model-organism designs, the compared training methods,
the PEARL mechanism, and the durability/preservation findings trace to the
abstract text. Full paper (quantified suppression/durability numbers) not
read at capture.

## Updates

None yet.

## Related entries

None yet.
