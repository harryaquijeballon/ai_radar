---
slug: 2026-xu-wu-stale-instruction-files
title: "Stale Instruction Files Override the Code in Coding Agents: A One-Sentence Fix"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.30571
canonical_ids: ["arxiv:2610.30571"]
publisher_or_author: "Xiaonan Xu, Wenjing Wu"
published: 2026-10-22
captured: 2026-10-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 2 (harness and context engineering): a precisely named
  mechanism (instruction-file precedence over code), a one-sentence
  mitigation, and a large, controlled, quantified before/after comparison —
  directly actionable for any project (including this one) that steers
  coding agents with a persistent instruction file.
---

# Stale Instruction Files Override the Code in Coding Agents: A One-Sentence Fix

## Summary
Coding agents follow a project's instruction file (e.g. CLAUDE.md,
AGENTS.md) even when it contradicts the existing code, and even when the
agent itself notices the contradiction — the authors' running example is an
instruction file requesting `print` where the codebase already uses
`logging`. They attribute the behavior to how the two sources reach the
model: the instruction file arrives as an instruction, while the code
arrives as tool output, which models are trained to weight lower.

The proposed fix is a single added sentence in the user-level instruction
file stating that the existing code takes precedence over the instruction
file when the two conflict. To test it, the authors built 40 Python
projects containing such conflicts and ran Claude Code and Codex CLI on a
feature task across 320 runs. Without the sentence, 90.1% of agent choices
followed the stale instruction file; Claude Code noted the conflict in 79 of
80 runs but still followed the file, and Codex CLI rewrote the existing
code to match the stale file in 20 of 80 runs, breaking the project's own
tests in 17 of those. With the sentence added, the share of choices
following the code rose from 4.2% to 91.4%, the code-rewriting behavior
stopped, and the test pass rate rose from 89.4% to 100%.

## Why it matters
This names a specific, previously-undiagnosed failure mode in persistent
agent-instruction-file setups — exactly the harness pattern this project
itself uses (CLAUDE.md, engine/skill instructions) — and gives a concrete,
nearly free mitigation with a large quantified effect. Any team steering
coding agents with a standing instruction file can test and adopt the
precedence sentence directly; the mechanism explanation (instruction vs.
tool-output weighting) also generalizes to other harness-design choices
about what agents will treat as authoritative.

## Verification notes
Read directly from the arXiv abstract page (arXiv:2610.30571, v1, submitted
22 Oct 2026, 01:00:43 UTC). All quantified figures (90.1%, 4.2% to 91.4%,
89.4% to 100%, the 320-run/40-project/two-harness design, the 79/80 and
20/80 Codex CLI figures) are stated directly in the abstract and traceable
to it; the controlled before/after design with two independent coding
harnesses supports `verified`. Full paper and independent replication not
checked this run.

## Updates

- None yet.

## Related entries
None yet.
