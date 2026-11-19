---
slug: 2026-mallick-kaer-security-aware-replanning
title: "Kaer: Security-Aware Replanning for Multi-Agent Systems"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.24839
canonical_ids: ["arxiv:2611.24839"]
publisher_or_author: "Tushin Mallick, Evan Rose, Matthew Laws, Alina Oprea, Cristina Nita-Rotaru — arXiv preprint (cs.MA)"
published: 2026-11-18
captured: 2026-11-19
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance): a concrete
  defense against a previously under-addressed attack surface — malicious
  agent feedback hijacking an orchestrator's replanning step — with a new
  adversarial benchmark and quantified robustness gains over an undefended
  baseline and the prior state-of-the-art defense.
---

# Kaer: Security-Aware Replanning for Multi-Agent Systems

## Summary

Many multi-agent systems use an orchestrator that creates a plan,
coordinates its execution, and revises the plan based on agent feedback
when tasks cannot be fully specified in advance. The authors argue this
replanning step is an exploitable attack surface: a malicious agent can
embed instructions in its feedback to hijack the orchestrator's next plan.
Existing defenses address per-tool access control or static policy checks
before execution, but not replanning itself. The authors propose Kaer,
which shields the planner from untrusted feedback by passing diagnostics
to it only as abstract templates, and limits plan revisions to
deterministic repair operators that must satisfy preset policies. They
also introduce Cintra, a benchmark of simulated tasks requiring replanning
paired with adversarial objectives. On Cintra, Kaer is more robust than
Magentic-One (undefended) and ControlValve (the prior state-of-the-art
defense), while keeping utility comparable to ControlValve; the abstract
templates slightly reduce utility on some tasks.

## Why it matters

For anyone building a multi-agent orchestrator that revises its plan based
on agent-reported feedback: a named, previously under-addressed attack
surface (feedback-driven replanning hijacking) plus a concrete mitigation
pattern — strip diagnostics to abstract templates, restrict repairs to
policy-checked deterministic operators — and a purpose-built adversarial
benchmark (Cintra) to measure robustness against it, with a quantified
comparison against both an undefended baseline and the prior best defense.

## Verification notes

arXiv abstract page fetched directly (2026-11-19); title, full author
list, "Submitted" 18 November 2026 date, and cs.MA (primary) / cs.LG
subject categories confirmed. Every claim in the Summary (the replanning
attack-surface argument, the Kaer mechanism, the Cintra benchmark, and the
comparison against Magentic-One and ControlValve) traces to the fetched
abstract text. Full paper body not read at capture; no independent
corroboration attempted (new working paper, no secondary coverage found;
exact robustness/utility figures not quantified in the abstract itself).
Appeared in arXiv's cs.MA "recent" listing dated Thu, 19 Nov 2026, one day
after its 18 Nov 2026 submission — normal next-day announcement lag,
within the 7-day eligibility cap. Upgrade path: read the full PDF for the
quantified robustness/utility numbers and the Cintra task set.

## Updates

None yet.

## Related entries

None yet.
