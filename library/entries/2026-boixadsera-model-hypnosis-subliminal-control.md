---
slug: 2026-boixadsera-model-hypnosis-subliminal-control
title: "Model Hypnosis: Strong control of AI via additive subliminal effects"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.16834
canonical_ids: ["arxiv:2608.16834"]
publisher_or_author: "Enric Boix-Adsera, Benedict Tessler"
published: 2026-08-17
captured: 2026-08-18
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Directly on lens 6 (security, prompt-injection-adjacent defenses): a named
  failure mode where individually weak, innocuous-looking prompt cues
  combine to strongly control model behavior, transferably across model
  families — a concrete threat a builder of guarded agent systems needs to
  account for.
---

# Model Hypnosis: Strong control of AI via additive subliminal effects

## Summary

The authors demonstrate a vulnerability they term "model hypnosis": weak,
individually innocuous cues embedded in a prompt (subtle textual variations
such as paraphrases or typos) can be systematically combined to strongly
control a model's behavior, even though no single cue looks adversarial.
They report the effect appears across different model families and scales,
including advanced reasoning models, and that hypnotic prompts transfer
across models (unverified — exact experimental protocol and quantitative
success rates not read beyond the abstract).

## Why it matters

This is a distinct threat class from typical prompt injection (which relies
on overt adversarial instructions): because control is exerted through
subtle, distributed cues rather than a single detectable trigger, it
complicates both content-filtering defenses and interpretability efforts.
Builders of agentic systems that accept untrusted or lightly-reviewed text
input should treat this as a reason to distrust "looks benign" as a safety
signal for prompt content.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The core claim
(weak additive cues combining into strong behavioral control, observed
across model families and transferable) is traced to the abstract.
Quantitative results, the specific cue-construction method, and scope of
"advanced reasoning models" tested were not independently corroborated —
hence partial verification.

## Updates

- **2026-08-18** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
