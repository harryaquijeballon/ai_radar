---
slug: 2026-yang-one-recipe-many-harnesses
title: "One Recipe, Many Harnesses: What Self-Evolution Encodes Across Languages and Models"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.10178
canonical_ids: ["arxiv:2608.10178"]
publisher_or_author: "Siqi Yang, Qianlan Yang, Yu-Xiong Wang, Saurabh Pujar, Martin Hirzel — arXiv preprint (cs.SE)"
published: 2026-08-10
captured: 2026-08-12
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium-high on lens 2 (harness and context engineering): a controlled
  study of self-evolving agent harnesses across 8 programming languages
  and 3 base models, finding the evolved logic transfers as an abstract
  pattern but language-specific machinery does not — useful context for
  anyone building self-improving harnesses, though the practical
  transferability outside a coding-benchmark setting is not yet shown.
---

# One Recipe, Many Harnesses: What Self-Evolution Encodes Across Languages and Models

## Summary
Self-evolving harnesses are agent systems that refine their own prompts, tools, and memory by inspecting their own results. The paper fixes a single evolution recipe and tests it across a grid of eight programming languages (Multi-SWE-Bench) and three base models to ask what these systems actually learn. The evolution loop improves on baseline performance in most cases but shows two "null regions" where gains disappear. Evolved harnesses share an abstract playbook across languages but instantiate it with almost disjoint language-ecosystem-specific machinery — the core logic transfers between environments, but language-specific components resist generalization and require re-evolution. The authors reframe evolved harnesses as a "legible compensation layer" shaped jointly by a language's engineering demands and a model's behavioral gaps, rather than benchmark-specific overfitting.

## Why it matters
Useful conceptual grounding for teams building self-evolving or self-improving agent harnesses: expect the abstract strategy to transfer across languages/domains but expect to re-evolve the concrete, environment-specific implementation each time — a testable expectation rather than an assumption.

## Verification notes
Read via the arXiv abstract page. The eight-language/three-model grid and the "null regions" finding are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
