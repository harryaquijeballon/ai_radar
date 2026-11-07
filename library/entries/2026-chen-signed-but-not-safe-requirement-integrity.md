---
slug: 2026-chen-signed-but-not-safe-requirement-integrity
title: "Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07483
canonical_ids: ["arxiv:2611.07483"]
publisher_or_author: "Xiaobo Chen, Genliang Zhu, Ziyuan Wang, Chu Wang"
published: 2026-11-05
captured: 2026-11-07
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation and deterministic guardrails (lens 4) and
  reproducibility/security (lens 6): a preregistered, quantified test of
  signed requirement manifests as a defense when enterprise AI agents split
  and merge work across subagents, isolating exactly where the defense
  breaks (extraction, not transit) — a precise, actionable trust-boundary
  finding rather than a general security warning.
---

# Signed but Not Safe: Requirement Integrity in Multi-Agent LLM Handoffs

## Summary

When an orchestrator splits a user request across subagents and merges their
results, the user's original requirements can be lost or corrupted in the
handoff. The paper compares three handoff formats — free text, structured
JSON, and signed requirement manifests — where the signed format has the
orchestrator extract each requirement as a quote with a checkable predicate,
sign the manifest with HMAC-SHA256, and verify the merger's decision with
deterministic code rather than an LLM checker.

Across 1,440 trajectories with Qwen3-8B and five threat types, signed
manifests cut unsafe commits under attack from 69.4% to 9.0%, with no net
loss of conformant (correct) commits. Signing defeated in-transit tampering,
and the deterministic verifier beat an LLM-based checker on both detection
and false-alarm rate. The residual risk was extraction error made *before*
signing: a pre-signing injection attack raised violations across three models
tested, because the signature then authenticates an already-corrupted
manifest. The authors conclude the trust boundary is extraction, not transit,
and that this is where defenses still need to focus. The study was
preregistered.

## Why it matters

A precise, falsifiable answer to "does signing agent-to-agent handoffs
actually make multi-agent systems safer?" — yes, against tampering in
transit, but it does nothing for the step before signing happens. For anyone
building a multi-agent system with a handoff/merge step, this names exactly
where to put verification effort (the extraction step) rather than assuming
cryptographic integrity solves requirement-preservation end to end.

## Verification notes

Read directly from the arXiv abstract page (arxiv.org, allowlisted); a
125-character verbatim-quote limit prevented reproducing the abstract
verbatim, so the summary above paraphrases it. All claims, including the
quantified results (69.4%→9.0%, the five threat types, the 1,440-trajectory
count) and the stated preregistration, are traced directly to the abstract;
no load-bearing claim depends on information beyond it. The full paper and
its code/trajectories were not independently fetched. Single version (v1, 5
Nov 2026).

## Updates

None yet.

## Related entries

None yet.
