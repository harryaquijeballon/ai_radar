---
slug: 2026-huang-speedrunner-programmatic-skill-learning
title: "Better, Faster, Stronger: Programmatic Skill Learning Best Reduces Agent Cost"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.11338
canonical_ids: ["arxiv:2608.11338"]
publisher_or_author: "Zixi Huang, Xiheng Wang, Andrew Wang, William Jurayj, Bernal Jiménez Gutiérrez, Daniel Khashabi, Nicholas Andrews — arXiv preprint (cs.CL)"
published: 2026-08-11
captured: 2026-08-13
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Medium on lens 2 (harness and context engineering): argues and tests that
  representing learned agent skills as executable programs (rather than
  natural-language playbooks) gives deterministic execution and the best
  cost reduction; validated across three embodied-agent environments, which
  is on-lens but not yet demonstrated on the software/research-agent tasks
  this project's harness most resembles.
---

# Better, Faster, Stronger: Programmatic Skill Learning Best Reduces Agent Cost

## Summary
Investigates cost-effective approaches for adapting LLM agents to new domains through skill learning, arguing that representing skills as programs — rather than natural-language instructions — achieves the best cost reduction, because program-based agents can deterministically execute action sequences rather than relying on trial-and-error. The paper proposes SpeedRunner, a coding agent that analyzes trajectories and refactors skills for better performance on future tasks. Tested across three embodied environments, SpeedRunner achieves strong performance while maintaining robustness against distribution shifts and environmental variability; the authors argue agent trajectories contain sufficient information to guide skill development without explicit replay or validation mechanisms.

## Why it matters
A concrete argument, with supporting experiments, for a specific harness-design choice — compile learned skills into executable programs rather than accumulating natural-language playbooks — that trades some flexibility for determinism and lower cost. Relevant to any project (including this one) considering how to encode reusable agent skills, though the embodied-environment test suite means the claim about robustness on software/research-agent tasks specifically is not yet directly evidenced.

## Verification notes
Read via the arXiv abstract page (2026-08-13). The core argument (skills-as-programs beat skills-as-instructions for cost), the SpeedRunner system description, and the three-environment test claim are quoted/paraphrased directly from the abstract; no quantitative effect sizes are stated in the abstract itself. Full paper (benchmarks, numeric results) not read at capture; findings not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
