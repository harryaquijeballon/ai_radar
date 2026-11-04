---
slug: 2026-chen-zhang-patching-the-protocol-pre-registration-repairs
title: "Patching the Protocol: A Taxonomy of Pre-Registration Repairs in LLM-Proposer Experiments"
status: accepted
domains: [ai_engineering, social_science]
source_type: academic
source_url: https://arxiv.org/abs/2611.04338
canonical_ids: ["arxiv:2611.04338"]
publisher_or_author: "Peter Chen, Ni Zhang, Siyuan Zhang"
published: 2026-11-03
captured: 2026-11-04
relevance:
  social_science: medium
  ai_engineering: medium
rationale: >-
  Medium on reproducibility/governance (ai_engineering lens 6) and AI applied
  to research with attention to credibility (social_science lens 6): a
  three-case taxonomy of when and how pre-registered LLM-proposer research
  protocols need auditable repairs — directly relevant to any agentic
  research pipeline, including this library's own economic-research-agent
  entries, that leans on pre-registration for credibility.
verification: verified
---

# Patching the Protocol: A Taxonomy of Pre-Registration Repairs in LLM-Proposer Experiments

## Summary

Argues that pre-registration, often proposed as a trust mechanism for
machine-learning research involving LLM-generated content, assumes a frozen
protocol can run unchanged — but in software-intensive studies the protocol
is partly implemented, and that implementation can contain defects needing
repair. The authors argue credibility depends more on whether patches are
auditable than on whether they occur at all. In a three-case study of
protocol repairs in a program where an LLM proposes executable rules and a
programmatic verifier gates them (covering production scheduling, incentive
design, and task assignment), they propose a two-axis patch taxonomy
(defect class: environmental, feasibility, or correctness; timing: pre-data
or post-data), introduce a verifiable non-impact claim for post-data
repairs, and distill a nine-item checklist. Each of the three protocols
needed exactly one defect-repair patch (three total); none changed a
numbered judgment criterion, its threshold, the scoring rule, or already-
collected data; two patches changed pre-registered design parameters before
any data were collected, each with a recorded rationale; all nine checklist
items were used by at least one patch, which the authors describe as an
observation of use rather than evidence the checklist is sufficient.

## Why it matters

A practical auditability framework for anyone running a pre-registered,
LLM-proposer-based research pipeline (directly applicable to this library's
own entries on agentic economic-research workflows): rather than treating
any mid-study protocol change as suspect, this gives a structured way to
classify and document a repair so the study's credibility rests on
transparency of the patch, not on an unrealistic assumption that the
original protocol was flawless.

## Verification notes

Read directly from the arXiv abstract (captured 2026-11-04; submitted
2026-11-03). The two-axis taxonomy, the three-case design, the nine-item
checklist, and the counts (three patches, two pre-data) trace to the
abstract text. Full paper (the checklist items themselves, per-case detail)
not read at capture.

## Updates

None yet.

## Related entries

[2026-chen-zhang-verifier-strength-discovery-quality](2026-chen-zhang-verifier-strength-discovery-quality.md) — companion paper by the same authors on whether verifier strength improves LLM-proposer discovery quality.
