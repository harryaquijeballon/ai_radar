---
slug: 2026-richard-frase-agentic-ai-testing-c2
title: "Testing and Evaluation of Agentic AI Systems In Military Command and Control"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.20597
canonical_ids: ["arxiv:2608.20597"]
publisher_or_author: "Ulysse Richard, Heather Frase, Sarah Cao, Di Cooke, Sebastian Kwon, Adrianna Tan — arXiv preprint (cs.SE)"
published: 2026-08-24
captured: 2026-08-24
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on lens 4 (evaluation and validation) and lens 6 (governance): a
  systematic review of 240 documented testing-and-evaluation practices
  showing which assumptions traditional software T&E relies on break down
  for agentic AI, with a named set of narrower, still-viable evaluation
  claims (bounded mission envelopes, trajectory-grounded correctness,
  executable runtime constraints, characterized run-to-run variance) — a
  framework applicable to agentic-system evaluation well beyond its
  military-domain case study.
verification: verified
---

# Testing and Evaluation of Agentic AI Systems In Military Command and Control

## Summary

The authors reviewed 240 documented testing-and-evaluation (T&E) practices spanning eight evaluation dimensions and three lifecycle stages, applied to agentic AI systems in a military command-and-control (C2) context. They identify eight assumptions traditional T&E relies on that agentic AI properties (autonomy, adaptivity, emergent multi-step behavior) undermine, clustered into four groups: specifiability, stability, composability, and supervisability. Their central claim is that passing a test suite satisfies a process requirement but does not warrant inferring that fielded behavior will match tested behavior. Rather than abandoning testing, the authors propose narrower, still-viable claims: bounded mission envelopes, trajectory-grounded correctness, executable runtime constraints, and characterized run-to-run variance. The paper derives 10 assurance claims from this framework and maps five C2 scenarios to their operational consequences.

## Why it matters

A rigorous account of exactly why "it passed our eval suite" does not imply "it will behave the same way in deployment" for agentic AI — directly on lens 4 and squarely inside the profile's standing interest in what makes agentic-system evaluation trustworthy enough for high-stakes use. The four narrower assurance claims (bounded envelopes, trajectory-grounded correctness, executable runtime constraints, variance characterization) are a transferable checklist for any team evaluating agentic systems for defensible deployment, not only in the military C2 setting the paper uses as its case study.

## Verification notes

Read via the arXiv abstract page, which describes the review scope (240 practices, eight dimensions, three lifecycle stages), the four assumption clusters, and the derived assurance-claim framework directly. Not independently corroborated against a second source or the full paper.

## Updates

None yet.

## Related entries

None yet.
