---
slug: 2026-cho-gupta-scaffold-warranted-reuse-skills
title: "SCAFFOLD: Toward Warrant-Preserving Evidence Transport for Reusable LLM-Agent Skills"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.23990
canonical_ids: ["arxiv:2611.23990"]
publisher_or_author: "Nami Cho, Shailja Gupta — arXiv preprint (cs.AI)"
published: 2026-11-18
captured: 2026-11-19
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 2/6 (harness engineering; reproducibility and governance):
  a formal problem statement and testable design obligations for deciding
  when a previously-validated agent skill may still be trusted after its
  context has changed — on-lens and well-specified, but explicitly
  unimplemented and unvalidated, so it is early framework-level context
  rather than a practically usable method yet.
---

# SCAFFOLD: Toward Warrant-Preserving Evidence Transport for Reusable LLM-Agent Skills

## Summary

Argues that an agent skill validated yesterday may not be justified for
reuse today: tests may cover only observable contract clauses, outcome
oracles may be missing, evaluations may inherit a flawed specification, and
permissions or dependencies may change between validation and use. The
authors propose the right unit of prospective trust is a "Warranted Reuse
Claim" (WRC) — a defeasible, claim-specific authorization tied to a
versioned skill, its target context, supporting evidence, assumptions, and
identified defeaters — and introduce "Warrant-Preserving Evidence
Transport" (WPET) to decide which historical evidence remains admissible
after a context change, separating evidence admissibility from the truth
of the underlying safety/effectiveness claim. The paper states a
conditional preservation result and its limits, specifies three-valued
applicability and asymmetric context-transfer judgments, and relates the
proposal to assurance cases, contracts, and skill-library maintenance. It
explicitly does not present an implemented verifier, an empirical result
showing superiority over baselines, or a proof of universal agent safety —
it outlines a falsifiable longitudinal evaluation design as future work.

## Why it matters

For anyone maintaining a library of reusable agent skills across changing
models, permissions, and dependencies: a precise vocabulary (Warranted
Reuse Claim, Warrant-Preserving Evidence Transport) for a problem most
teams currently handle informally — deciding whether an old validation
result still applies after something in the skill's context has changed.
Useful now mainly as a framework for structuring that decision and as a
pointer to the open empirical question (which the authors themselves flag
as unresolved); not yet a tool a builder can deploy.

## Verification notes

arXiv abstract page fetched directly (2026-11-19); title, authors,
"Submitted on 18 November 2026, 07:33 UTC" date, and cs.AI (primary, with
cs.MA/cs.SE cross-lists) subject categories confirmed. Every claim in the
Summary, including the explicit absence of an implemented verifier or
empirical validation, traces to the fetched abstract text. Full paper body
not read at capture; no independent corroboration attempted or needed
beyond the paper's own stated scope (new working paper, no secondary
coverage found). Appeared in arXiv's cs.MA "recent" listing dated Thu, 19
Nov 2026, one day after its 18 Nov 2026 submission — normal next-day
announcement lag, within the 7-day eligibility cap.

## Updates

None yet.

## Related entries

None yet.
