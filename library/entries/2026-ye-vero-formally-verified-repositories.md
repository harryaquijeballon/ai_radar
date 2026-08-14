---
slug: 2026-ye-vero-formally-verified-repositories
title: "Vero: Can AI Agents Build Formally Verified Software Repositories?"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.13522
canonical_ids: ["arxiv:2608.13522"]
publisher_or_author: "Zhe Ye, Hantao Lou, Yuechun Sun, Peiyang Song, Zhengxu Yan, Timothe Kasriel, Qingyang Zhang, Kaiyu Yang, Soonho Kong, Jingxuan He, Dawn Song — arXiv preprint"
published: 2026-08-14
captured: 2026-08-14
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  New benchmark squarely on lens 4 (evaluation, validation and deterministic
  guardrails): measures whether AI agents can produce repository-scale code
  with machine-checked correctness proofs, with a concrete, low current
  success rate (27/43) that usefully calibrates expectations for teams
  considering formally-verified agent output.
verification: partial
---

# Vero: Can AI Agents Build Formally Verified Software Repositories?

## Summary

The authors introduce Vero, a benchmark testing whether AI agents can
generate code together with machine-checked proofs of correctness at
repository scale. It comprises 43 multi-module instances drawn from
real-world repositories spanning Python, Dafny, Verus, and Coq, covering
domains from cryptographic protocols to distributed systems, plus
multi-module Lean 4 repositories with formal specifications and reference
implementations. Vero also includes an audit mechanism letting agents prove
a specification is unsatisfiable or that reference code is incorrect. The
strongest evaluated agent configuration fully solves only 27 of 43 instances
and closes no specifications on the hardest repositories; current
frontier coding-agent setups with Lean toolchain access fall short of
repository-scale verified software synthesis. Benchmark and evaluation
infrastructure are released publicly.

## Why it matters

Gives ai-engineering builders a calibrated, quantified sense of how far
current agents are from repository-scale formally verified code generation
(27/43 on the best configuration) — directly useful for scoping how much to
trust agent-produced "verified" code today, and a reusable benchmark for
tracking progress.

## Verification notes

Read via the arXiv abstract page only; full paper, benchmark instances, and
evaluation code not examined. The 27/43 figure and domain composition are as
stated on the fetched abstract page; not independently corroborated against
the released benchmark repository.

## Updates

None yet.

## Related entries

None yet.
