---
slug: 2026-daxerer-coding-agents-debugger-necessity
title: "Do Coding Agents Still Need a Debugger? Frontier-Model-Based Fault Localization at the Accuracy Ceiling"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.36015
canonical_ids: ["arxiv:2610.36015"]
publisher_or_author: "Christoph Daxerer, Johann Glock, Christian Macho, Rudolf Ramler, Martin Pinzger, Josef Pichler"
published: 2026-10-26
captured: 2026-10-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on agent architecture and observability (lenses 1, 5): a controlled
  fault-injection study (610 faults, 144 programs, five behavior-preserving
  code transformations, three models x three tool conditions) giving a
  quantified, directly actionable answer to a concrete harness-design
  question — is interactive debugger access worth its token cost for fault
  localization — rather than an opinion about agent tooling.
---

# Do Coding Agents Still Need a Debugger? Frontier-Model-Based Fault Localization at the Accuracy Ceiling

## Summary

Asks whether coding agents need interactive debugger access to localize
faults, or can do it from source code alone. The authors seeded 610
single-line faults into 144 LeetCodeDataset solutions and rewrote each
program with five behavior-preserving transformation recipes (e.g.
restructuring loops and conditionals) to test robustness beyond
memorized solutions. They ran agents built on three models (Sol 6.1, Luna
6, Qwen 3.8) under three conditions: no tools, optional debugger access,
and encouraged debugger use, and tracked how often agents actually used
the debugger versus just running the program.

Without any tools, agents localized 98.2–99.9% of faults in original
programs and 96.7–99.9% in transformed ones — accuracy dropped mainly
where transformations restructured loops and conditions. Encouraging
debugger use removed 63% of Luna 6's remaining transformed-program errors
(+2.1 points) and 61% of Qwen 3.8's (+1.3 points), but at 14.7–27.0 times
the token use; Sol 6.1 stayed at 99.9% regardless. With debugger access
merely optional (not encouraged), agents used it in only 0.2–6.2% of runs,
yet still gained accuracy (Luna 6 +1.5, Qwen 3.8 +1.3 points). The authors
note agents ran the program far more often than they stepped through it
(all figures as stated in the fetched abstract; full paper, transformation
recipes, and statistical tests not reviewed at capture).

## Why it matters

A direct, quantified answer to a harness-design question builders
actually face: is it worth wiring up interactive debugger access for a
coding agent's fault-localization step? On this benchmark, source-code-only
localization is already near-ceiling (96.7–99.9%) for well-specified, short
programs, and forcing debugger use to close the remaining gap costs
14–27x the tokens for a 1–2 point gain — evidence that debugger tooling is
a high-cost, low-marginal-value investment for this task class, worth
checking against before building it into a harness by default.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-29; single version,
submitted 26 Oct 2026, 17:20 UTC). The experimental design (610 faults,
144 programs, five transformation recipes, three models x three
conditions) and all quantified figures (98.2–99.9%, 96.7–99.9%, 63%/61%
error removal, 14.7–27.0x token cost, 0.2–6.2% optional-use rate, +1.5/+1.3
point gains) trace to the fetched abstract text. The transformation
recipes' exact definitions and the full statistical analysis were not
independently reviewed; results are specific to short, well-specified
competitive-programming-style solutions and may not generalize to larger,
less-specified codebases.

## Updates

None yet.

## Related entries

None yet.
