---
slug: 2026-agyekum-iac-repair-security-degradation
title: "Does Fixing Break Security? An Empirical Study of Security Degradation in Iterative LLM-Driven Infrastructure-as-Code Repair"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.13404
canonical_ids: ["arxiv:2608.13404"]
publisher_or_author: "Benjamin Agyekum, Fabio Santos — arXiv preprint, accepted at ESEM 2026"
published: 2026-08-14
captured: 2026-08-14
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Quantified, practically actionable finding directly on lens 6
  (reproducibility, security and governance) and lens 4 (deterministic
  guardrails): iterative LLM-driven repair of Infrastructure-as-Code can
  reintroduce security regressions, with a measured regression rate and a
  recommended stopping point a builder could apply this quarter.
verification: partial
---

# Does Fixing Break Security? An Empirical Study of Security Degradation in Iterative LLM-Driven Infrastructure-as-Code Repair

## Summary

The authors study whether iterative LLM feedback loops used to fix
LLM-generated Infrastructure-as-Code (IaC) inadvertently introduce new
security vulnerabilities. Analyzing 5,968 scenarios from the IaC-Eval
benchmark across up to 5 repair iterations, tracked via CIS Benchmark
security checks, they find: under standard detection, 13.8% of scenarios
show security regression (3.3% under a stricter, more conservative
detection standard); regression transitions show 2.6x more code churn than
non-regressing iterations (Cohen's d = 0.90); resource restructuring
accounts for 79.0% of regressions, suggesting most are measurement
artifacts rather than genuine new vulnerabilities; about 36.6% of
standard-mode regressions self-correct within an average of 1.2 further
iterations. The paper recommends stopping the repair loop at iteration 3 as
an empirically-grounded cutoff. Accepted at ESEM 2026 (unverified beyond the
abstract page: peer-review status not independently confirmed).

## Why it matters

A concrete, numeric answer to a question every team running LLM-driven IaC
auto-repair loops should be asking: does "fixing" quietly reintroduce
security problems? The 13.8%/3.3% regression rates and the iteration-3
stopping recommendation are directly usable as a guardrail policy for
agentic IaC repair pipelines.

## Verification notes

Read via the arXiv abstract page only; full paper (and the IaC-Eval
benchmark it builds on) not read. The quantitative figures above are as
reported on the fetched abstract page and have not been independently
corroborated against a second source or against the underlying IaC-Eval
benchmark. ESEM 2026 acceptance is stated on the page but not verified
against the conference program.

## Updates

None yet.

## Related entries

None yet.
