---
slug: 2026-panossian-llm-theory-program-renderer-format
title: "Does the Way We Write a Theory Change the Program an LLM Builds from It? A Prospective Randomized Study of Renderer Format in LLM Theory-to-Program Translation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.10314
canonical_ids: ["arxiv:2608.10314"]
publisher_or_author: "Andre Panossian — arXiv preprint (cs.SE)"
published: 2026-08-10
captured: 2026-08-12
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 2 (harness and context engineering): a preregistered,
  randomized study finding that presentation format (structured vs.
  prose) of the same theoretical content has limited, mostly
  non-significant effect on the code an LLM produces from it — a
  credible negative result that tempers assumptions about prompt-format
  sensitivity, with fully auditable data/software released.
---

# Does the Way We Write a Theory Change the Program an LLM Builds from It? A Prospective Randomized Study of Renderer Format in LLM Theory-to-Program Translation

## Summary
The paper asks whether presenting identical theoretical content in different formats (structured vs. prose-based) systematically changes the code an LLM produces from it. Using a preregistered randomized design with 32 paired renderer slots, two LLM snapshots translated five theoretical accounts into 320 programs in a sparse quadratic language. Contrary to the pre-registered prediction of a uniform, family-invariant, classifiable behavioral geometry, renderer format did not produce that pattern; same-account identifiability stayed near chance, and only one endpoint survived multiplicity correction, and even that one missed the registered effect-size threshold. The authors release fully auditable datasets and software.

## Why it matters
A disciplined negative result on prompt/theory-presentation format effects in a specific, narrow LLM-translation setting: useful as a check against over-generalizing claims that renderer/prompt formatting strongly and predictably shapes LLM code output — though the tested domain (a niche quadratic modeling language) limits how far the null result can be generalized to other LLM coding tasks.

## Verification notes
Read via the arXiv abstract page. The design details (32 slots, five accounts, 320 programs) and the null/near-null findings are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
