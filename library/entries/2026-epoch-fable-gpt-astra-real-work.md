---
slug: 2026-epoch-fable-gpt-astra-real-work
title: "How good are Fable 5.2 and GPT-6.2 Astra at real work?"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://epoch.ai/publications/how-good-are-fable-5-2-and-gpt-6-2-astra-at-real-work
canonical_ids: []
publisher_or_author: "Epoch AI"
published: 2026-11-17
captured: 2026-11-18
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails) and
  lens 6 (reproducibility): an independent, non-vendor evaluation (the
  profile's explicit counterweight to vendor benchmarks) that names specific
  agent failure modes on open-ended work and gives concrete, transferable
  guidance for evaluating agentic products.
---

# How good are Fable 5.2 and GPT-6.2 Astra at real work?

## Summary

Epoch AI evaluated six frontier models, including Fable 5.2, Opus 5.5, and
GPT-6.2 Astra, on an updated version of its Epoch Automation Reports
benchmark, built from real tasks drawn from Epoch's own work: adding an
entry to Epoch's AI Data Centers database, designing an out-of-distribution
chess-variant study, investigating hidden messages in SVG images, and
writing an open-ended "Data Insight." An Epoch analyst manually graded each
model's output against the standard expected of an Epoch employee (100% =
employee level), scoring each criterion 1–4; each model ran each task once,
and the authors flag the scores as noisy and subjective. On the data-centre
task, Fable 5.2 scored 97.5%, Opus 5.5 scored 87.5%, and GPT-6.2 Astra
scored 65% — a 17-point gap from Fable 5.2 despite the two roughly tying on
Epoch's own Capabilities Index. No model reached the employee standard on
every task. Fable 5.2 and Opus 5.5 reached contractor-level performance on
the data-centre analysis specifically (a human contractor takes ~16 hours;
Opus 5.5 took under 3). Models struggled with open-ended experiment design
(reusing well-known chess variants likely seen in training, undermining the
intended out-of-distribution test), rarely iterated on first attempts,
showed weak judgment about what mattered in their own findings, and — when
asked to compare their own output against human gold standards — usually
preferred their own work for reasons that rewarded superficial rigor (e.g.,
experiment count) over substance.

## Why it matters

Gives anyone evaluating or deploying agentic AI for open-ended, judgment-heavy
work (not just structured, tool-rich tasks) a concrete checklist drawn from
observed failure modes: don't infer real-work performance from capability
benchmarks alone (the Astra/Fable gap despite similar benchmark scores);
build in and check for genuine iteration rather than first-attempt reliance;
test explicitly for training-data contamination in "novel" task design; and
never let an agent grade its own output against a gold standard without
independent, human-anchored scoring, since self-preference was systematic
here. This is exactly the kind of independent, non-vendor evaluation evidence
the profile's policy-simulation interest depends on for deciding when agentic
output is trustworthy enough to act on.

## Verification notes

Fetched the Epoch AI publication page directly (epoch.ai, on the egress
allowlist) and read it in full. All claims above — methodology, the three
named model scores, the time comparison, and the four qualitative failure
patterns — are traced to that text. Epoch states its own scores are noisy
and subjective (single run per task, small task set); this caveat is
preserved rather than treated as a firm quantitative result.

## Updates

None yet.

## Related entries

- [Higher-Scoring Coding Models Did Not Get More Work Done](2026-hua-benchmark-scores-real-work-diff-in-diff.md) — same-week, independent causal evidence of a benchmark/real-work gap.
