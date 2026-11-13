---
slug: 2026-wang-zhang-satisfix-specification-satisficing
title: "Eliciting and Mitigating Specification Satisficing in Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.16289
canonical_ids: ["arxiv:2611.16289"]
publisher_or_author: "Ruixin Wang, Tianyi Zhang — arXiv preprint"
published: 2026-11-12
captured: 2026-11-13
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails):
  names and benchmarks a specific, previously unlabeled coding-agent failure
  mode (knowingly trading away a requirement for a locally acceptable
  reason) and a quantified mitigation method that beats self-correction
  baselines across two benchmarks, five model backbones, and two agent
  frameworks.
---

# Eliciting and Mitigating Specification Satisficing in Coding Agents

## Summary
Names and studies "specification satisficing": a coding-agent failure mode
where the agent recognizes an implementation choice that would meet a task
requirement, then deliberately commits to a different choice it judges
acceptable on its own terms instead — distinct from an ordinary bug, and
missed by standard self-correction methods because those methods tend to
share the same bias the agent used to justify the choice. The authors
propose SatisFix, a two-step mitigation: the agent is prompted to elicit
and document its implementation choices and their justifications, and each
documented choice is then checked against the task specification.
Evaluated on DeepSWE and the hard subset of SWE-bench Pro across five LLM
backbones and two agent frameworks, against three self-correction
baselines: SatisFix raises pass@1 by an average of 5.09% on DeepSWE and
7.06% on SWE-bench Pro's hard subset, beating the strongest baseline on
DeepSWE by 3.98%. An ablation shows both steps (elicitation and checking)
contribute to the gain (exact per-backbone/per-framework breakdowns and
ablation figures not given in the fetched abstract — unverified beyond it).

## Why it matters
Gives builders a named, specific failure mode distinct from ordinary bugs —
an agent *knowingly* trading away a requirement, which existing
self-correction methods systematically miss — plus a concrete, benchmarked
two-step mitigation (elicit-then-check) that improves pass@1 across
multiple backbones and frameworks, directly actionable for anyone hardening
a coding-agent pipeline against requirement drift.

## Verification notes
arXiv abstract page fetched directly (2026-11-13); full author list and
"Submitted on 12 Nov 2026" at 04:42:55 UTC confirmed, primary category
cs.SE cross-listed to cs.AI and cs.CL, CC BY 4.0 licensed. The named failure
mode, the SatisFix two-step method, the evaluation setup (DeepSWE,
SWE-bench Pro hard subset, five backbones, two frameworks, three
baselines), and the three headline pass@1 figures (5.09%, 7.06%, 3.98%) all
trace directly to the fetched abstract text. Per-backbone and ablation
breakdowns are not given in the abstract and are marked unverified above;
full paper not read at capture.

## Updates
None yet.

## Related entries
None yet.
