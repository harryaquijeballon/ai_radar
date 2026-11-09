---
slug: 2026-adnan-breakpoint-debugging-repair-limits
title: "On the Limits of Execution Traces for Repairing Assertion Failures in LLM-Generated Code"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.09212
canonical_ids: ["arxiv:2611.09212"]
publisher_or_author: "Muntasir Adnan, Carlos C. N. Kuhn"
published: 2026-11-06
captured: 2026-11-09
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/deterministic guardrails (lens 4): a quantified,
  multi-benchmark comparison showing when trace-augmented repair helps
  versus when it does not — a directly actionable rule for choosing between
  resampling and trace-based repair in an automated code-fixing loop,
  rather than a one-sided case for either.
---

# On the Limits of Execution Traces for Repairing Assertion Failures in LLM-Generated Code

## Summary

In iterative repair, a failed LLM-generated program's error is fed back to the model for another attempt. The authors observe that most failures remaining after repair are assertion failures, which they argue say little about where the underlying fault is. They propose Breakpoint Debugging (BPD) — returning the failed program annotated with variables' runtime values — and compare it against simply resampling five additional generations, on tasks where iterative repair had already failed.

Results vary by benchmark: on BigCodeBench, BPD repairs 26.7% of the remaining tasks versus 22.4% for resampling, with the advantage growing with model size, and cuts unchanged-code resubmissions from 28% to 8%. On HumanEval, BPD beats resampling only slightly. On LiveCodeBench, resampling does better (6.5% vs. 4.9%) and BPD gives no gain even when tested against public tests. Using only the first failing test's trace performs better than tracing all failing tests, while using fewer tokens. The authors conclude traces help only when a test exposes a failing input and the fault is a simple implementation slip — otherwise, a repair loop should resample instead.

## Why it matters

A directly actionable, falsifiable rule for anyone building an automated code-repair or self-correcting agent loop: trace-augmented repair is not a universal upgrade over resampling, and which one wins depends on the benchmark/task character (simple implementation slips vs. deeper logic faults). This is exactly the kind of deterministic-guardrail nuance the profile's evaluation lens calls for — a method that could silently look like a universal improvement in one setting while failing in another.

## Verification notes

Fetched the arXiv abstract page directly; the three benchmark results (BigCodeBench, HumanEval, LiveCodeBench) and the trace-selection finding are as stated in the abstract. Load-bearing quantified claims are traced to the source; no independent replication exists yet.

## Updates

None yet.

## Related entries

- [2026-wu-causalrepair-llm-program-repair](2026-wu-causalrepair-llm-program-repair.md) — another program-repair technique addressing causal/fault-localization limits; useful to compare mechanisms.
- [2026-li-retrace-independent-patch-verification](2026-li-retrace-independent-patch-verification.md) — a complementary verification-side approach to the same repair pipeline this paper studies from the generation side.
