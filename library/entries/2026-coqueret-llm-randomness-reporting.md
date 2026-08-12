---
slug: 2026-coqueret-llm-randomness-reporting
title: "Randomness in Large Language Models: What Researchers Need to Know (and Report)"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.24372
canonical_ids: ["arxiv:2607.24372"]
publisher_or_author: "Guillaume Coqueret, Joan Llull, Florian Oswald, Christophe Pérignon, Christoph Scheuch, Lars Vilhuber — arXiv preprint"
published: 2026-07-27
captured: 2026-07-28
relevance:
  social_science: high
  ai_engineering: high
verification: verified
rationale: >-
  Cross-domain. Social science high: a direct, methods-usable treatment of
  LLMs as a research instrument's core validity problem (lens 5) — output
  variability across repeated calls even with fixed prompts and temperature
  zero — with concrete reporting standards for empirical papers, replication
  packages, and data editors. AI engineering high: squarely on the
  reproducibility/governance lens — a concrete control (treat LLM outputs as
  distributional draws, not fixed measurements) for run reproducibility.
---

# Randomness in Large Language Models: What Researchers Need to Know (and Report)

## Summary

Addresses a validity problem for any research or engineering pipeline that
treats LLM outputs as measurements: outputs can vary across repeated
requests even when the prompt and apparent model settings are unchanged.
The authors identify several sources of this variability beyond deliberate
sampling — model updates, numerical rounding in floating-point computation,
and expert/load-based routing in mixture-of-experts or served
infrastructure. Setting temperature to zero removes intentional sampling
randomness but does not eliminate the others, especially when using
proprietary hosted APIs where routing and backend changes are invisible to
the caller. The paper illustrates the practical stakes with a sentiment
classification exercise on corporate documents, showing repeated-call
variation with real consequences for downstream conclusions. Its central
recommendation is a reframing: researchers, replication-package authors, and
journal data editors should treat LLM outputs "as draws from a distribution
rather than as fixed measurements," with reporting standards to match
(e.g., disclosing settings, repetition counts, and variability, not just a
single run's output).

## Why it matters

For the social-science audience: a direct answer to "can I trust a single
LLM-coded label or extracted number in my empirical pipeline?" — no, and
here is what to report instead, including practical proprietary-API
caveats. Applicable to any project using LLMs for classification,
information extraction, or text-as-data work. For the AI-engineering
audience: a transferable reproducibility control for anyone versioning or
replaying agent/LLM pipeline outputs — the reminder that "same prompt, same
temperature" is not sufficient for determinism, and a concrete alternative
framing (distributional reporting) for run-reproducibility and audit-trail
design.

## Verification notes

arXiv abstract page fetched directly (2026-07-28); title, full author list,
"Submitted on 27 Jul 2026" confirmed. Every claim in the Summary — the named
sources of variability, the temperature-zero caveat, the proprietary-API
point, the sentiment-classification illustration, and the "draws from a
distribution" recommendation — traces directly to the fetched abstract text.
Full paper text not read at capture; no independent corroboration attempted
(pre-publication preprint). The paper appeared on arXiv's econ.GN "recent"
listing grouped under 2026-07-28 despite the abstract page's own "submitted"
date of 2026-07-27 — a routine announcement-lag discrepancy, not treated as
a discrepancy in the claims themselves. Upgrade path: read the full PDF for
the complete list of variability sources and the illustrative experiment's
design.

## Updates

None yet.

## Related entries

None yet.
