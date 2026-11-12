---
slug: 2026-voria-acf-instruction-adherence
title: "Do They Do as They Are Told? Investigating Coding Agents' Adherence to Explicit Instructions in Context Files"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.13709
canonical_ids: ["arxiv:2611.13709"]
publisher_or_author: "Gianmario Voria, Yutaro Kashiwa, Gemma Catolino, Fabio Palomba — arXiv preprint (cs.SE)"
published: 2026-11-10
captured: 2026-11-12
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Medium on harness/context engineering (lens 2): a naturalistic
  (mined-from-the-wild) complement to this library's existing controlled
  experiment on AGENTS.md policy wording — real Agent Context File
  snapshots and their linked commits, turned into measurable compliance
  checks per instruction, rather than one inserted test policy. No
  compliance-rate figures were available from the abstract alone, so the
  finding is directional rather than quantified.
---

# Do They Do as They Are Told? Investigating Coding Agents' Adherence to Explicit Instructions in Context Files

## Summary

Studies whether coding agents actually follow the explicit instructions
written into real-world Agent Context Files (ACFs) such as AGENTS.md. The
authors collected real ACF snapshots together with the agent-generated
commits linked to them, converted the actionable instructions into
measurement scripts, and checked per-instruction compliance against those
commits. They report that most observable instructions could be made
measurable, that agents followed ACF guidance "more often than not," but
that adherence was polarized — some instructions were followed
consistently, others were essentially never respected — and that
compliance varied by both instruction category and by which coding agent
was used. (unverified: no specific compliance-rate figures or sample size
were available in the fetched abstract text.)

## Why it matters

Complements this library's existing controlled study of ACF policy wording
([2026-tsuchida-agents-md-policy-wording-compliance](2026-tsuchida-agents-md-policy-wording-compliance.md))
with naturalistic, real-world evidence: instruction files like CLAUDE.md or
AGENTS.md cannot be assumed to govern agent behavior uniformly. Teams
relying on such files — including this project's own engine and skill
instructions — should expect some instruction types to need rewriting and
some agents to need enforcement mechanisms beyond the ACF itself, since
written policy alone does not reliably produce compliant behavior across
instruction types or agents.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.13709,
2026-11-12); title, authors (Gianmario Voria, Yutaro Kashiwa, Gemma
Catolino, Fabio Palomba), submission date (10 Nov 2026), and category
(cs.SE) confirmed there. The study design (real ACF snapshots, linked
commits, per-instruction measurement scripts) and the directional findings
trace to the fetched abstract text. The abstract did not include
compliance-rate numbers or sample size; these claims are marked
unverified above and the full paper was not read at capture — upgrade
path noted for a future pass.

## Updates

None yet.

## Related entries

- [2026-tsuchida-agents-md-policy-wording-compliance](2026-tsuchida-agents-md-policy-wording-compliance.md) — same topic (ACF instruction compliance), distinct method: that entry is a controlled experiment with one inserted policy across four phrasing styles; this one mines real-world ACFs and commits.
