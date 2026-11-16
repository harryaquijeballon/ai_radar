---
slug: 2026-he-soteria-verified-planning-runtime-enforcement
title: "Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.17880
canonical_ids: ["arxiv:2611.17880"]
publisher_or_author: "Mike He, Ankush Desai, Sharad Malik, Aarti Gupta — arXiv preprint (NeurIPS'26 Oral)"
published: 2026-11-13
captured: 2026-11-16
relevance:
  ai_engineering: high
  social_science: n/a
verification: verified
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails) —
  the core lens for the policy-simulation interest: combines formally
  verified hierarchical planning with runtime specification enforcement so
  that an agent blocked from an unsafe action has a principled way to
  recover rather than getting stuck, reporting a quantified task-success
  improvement with zero policy violations across tool-use benchmarks — a
  concrete deterministic-guardrail pattern a builder could apply directly.
---

# Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents

## Summary

Addresses a conflict in LLM agents that carry out multi-step tool calls:
they must both complete the user's task and follow domain policies and
correctness rules, but naively blocking an unsafe action can leave the
agent stuck with no clear way to recover. Soteria resolves this by
combining verified hierarchical planning with runtime enforcement of
specifications. Before any tool is invoked, the agent produces a
structured plan that is formally checked against the given specifications;
during execution, that verified plan keeps the agent on compliant paths
and provides guidance for recovery when a specific action is blocked,
rather than leaving the agent without a path forward. Across several
tool-use benchmarks, the authors report a 1.7x higher average task success
rate than the best baselines, with no policy violations recorded. The
paper was accepted as a NeurIPS 2026 Oral. (unverified: the specific
benchmark suite, baseline identities, and the exact specification language
used — abstract read only, full paper not retrieved at capture.)

## Why it matters

For builders needing agent output trustworthy enough for research or
policy use: a concrete deterministic-guardrail pattern that avoids the
usual trade-off between safety and task completion — rather than simply
blocking unsafe actions and stalling the agent, the verified plan itself
supplies a compliant recovery path. The reported result (higher task
success *and* zero policy violations, not one traded for the other) is
the kind of evidence this profile's lens 4 asks for: a method that could
move an agent from "blocked or unsafe" to "both compliant and effective"
in a real deployment, with formal verification giving the guarantee a
purely learned or prompted guardrail cannot.

## Verification notes

arXiv abstract page fetched directly (2026-11-16); title, full author list
(Mike He, Ankush Desai, Sharad Malik, Aarti Gupta), "Submitted on 13 Nov
2026," subject categories (cs.AI, cs.SE), and the NeurIPS'26 Oral
acceptance note all confirmed from the fetched page. Every claim in the
Summary traces to the fetched abstract text: the verified-planning-plus-
runtime-enforcement architecture, the pre-execution plan-checking step, the
in-execution compliant-path guidance, and the 1.7x task-success figure with
zero policy violations. Full paper text not read at capture; no
independent corroboration attempted beyond the stated NeurIPS acceptance
(new working paper, no secondary coverage found). Appeared in arXiv's
cs.SE "recent" listing dated Mon, 16 Nov 2026, a 3-day gap from its stated
submission date consistent with normal cross-list announcement lag —
within this run's 7-day eligibility cap. Upgrade path: read the full PDF
for the benchmark suite, baseline identities, and specification language.

## Updates

None yet.

## Related entries

None yet.
