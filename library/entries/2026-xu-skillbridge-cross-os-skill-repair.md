---
slug: 2026-xu-skillbridge-cross-os-skill-repair
title: "SkillBridge: Cost-Aware Diagnosis and Repair of Cross-OS Compatibility Defects in Agent Skills"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.26256
canonical_ids: ["arxiv:2611.26256"]
publisher_or_author: "Anjie Xu, Zixing Wang, Yifeng Cai, Leye Wang — arXiv preprint"
published: 2026-11-19
captured: 2026-11-21
relevance:
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 2 (harness and context engineering) and lens 7
  (AI-assisted software development): a concrete, measured workflow for
  the cross-OS compatibility problem in agent skills, directly extending
  this library's existing skill-authoring/skill-harness coverage (SIGIL,
  Authoring Agent Skills) with a repair technique and a budget argument
  for how to test it cheaply.
---

# SkillBridge: Cost-Aware Diagnosis and Repair of Cross-OS Compatibility Defects in Agent Skills

## Summary

Addresses agent skills that work on one operating system but fail on
another because OS-specific assumptions are scattered across
documentation, scripts, metadata, install requirements, and entry points —
and running every skill against every target OS to find these is
expensive. SkillBridge is a three-stage, contract-based workflow: static
analysis flags OS-sensitive evidence across 3,270 skill-target-OS cases
drawn from 1,090 skills tested against Linux, macOS, and Windows; dynamic
validation with root-cause review confirms which flagged cases are
genuinely OS-caused failures; and repair targets the specific contract
field responsible. Repair raised the reviewer-judged target-task pass rate
from 30.6% to 38.4%. A retrospective Linux/macOS budget analysis found
SkillBridge needed only 185 dynamic validations to confirm 38 real OS
issues, versus roughly 865 validations expected under uniform random
selection to find the same number — an unverified extrapolation from the
authors' own retrospective analysis, not an independently re-run
experiment.

## Why it matters

For anyone authoring or maintaining agent skills meant to run across
operating systems: a concrete static-plus-dynamic triage workflow that
cuts the validation budget needed to find real cross-OS defects by roughly
4-5x versus random testing, plus a repair step that moves the needle on
actual task pass rate rather than just defect counts — a pattern
directly reusable alongside this library's other skill-engineering entries.

## Verification notes

arXiv abstract page fetched 2026-11-21 (paraphrased summary; full abstract
text not reproduced verbatim due to tool quoting limits). Submission
history shows v1 submitted Thu, 19 Nov 2026, 15:30:28 UTC — within this
run's discovery window (2026-11-20 → 2026-11-21) and the 7-day eligibility
cap. Figures (3,270 cases, 1,090 skills, 30.6%->38.4% pass rate, 185 vs
~865 validations) are traced to the fetched summary; the budget-savings
estimate is the authors' own retrospective comparison and was not
independently recomputed, so verification is partial. No secondary
coverage found (new preprint).

## Updates

None yet.

## Related entries

- [2026-dantanarayana-sigil-skill-harnesses](2026-dantanarayana-sigil-skill-harnesses.md) — related: typed skill harnesses.
- [2026-destefanis-authoring-agent-skills](2026-destefanis-authoring-agent-skills.md) — related: software-engineering approach to authoring skills.
