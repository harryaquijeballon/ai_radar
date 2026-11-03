---
slug: 2026-mehboob-shafique-quantization-coding-agents
title: "Beyond Accuracy: How Quantization Affects Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.02368
canonical_ids: ["arxiv:2611.02368"]
publisher_or_author: "Areej Mehboob, Muhammad Ali Shafique, Muhammad Usman Qadeer, Hamza Farooq"
published: 2026-11-02
captured: 2026-11-03
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on agent architecture/orchestration (lens 1) and AI-assisted
  software development (lens 7): a controlled comparison showing
  quantization leaves final accuracy unchanged for coding agents while
  substantially changing solution trajectories, tool use, and failure
  modes — a stated trade-off with quantified evidence, directly relevant
  to deployment choices for cost-constrained agentic coding.
---

# Beyond Accuracy: How Quantization Affects Coding Agents

## Summary

Compares BF16 against 4-bit AWQ and GPTQ quantized versions of
Qwen2.5-Coder-Instruct (7B, 14B, 32B) and Devstral-Small-2507 (24B) on
OJBench coding problems across three seeds, specifically as coding
*agents* that execute and revise code rather than as static
code-generation models. No statistically significant accuracy loss
appears for any agent under quantization. But final accuracy hides large
behavioral changes: AWQ cuts Qwen-7B's one-shot solves from 17 to 0 while
raising its loop-based (iterative) solves from 10 to 25; all of
Qwen-32B's successes involve tool use, while Devstral rarely makes a valid
executor call at all. Failure patterns also diverge: Qwen-32B produces
many more compilation errors, rising slightly under quantization, while
Devstral's failures shift from runtime errors toward wrong answers and
timeouts. The authors conclude that quantization robustness in coding
agents should be judged by solution trajectories, tool use, and failure
modes — not final accuracy alone (as stated in the fetched abstract; full
per-model/per-quantization results not reviewed at capture).

## Why it matters

Directly actionable for teams choosing a quantized model to cut inference
cost in an agentic coding pipeline: matching final-accuracy numbers
between BF16 and quantized variants is not sufficient evidence that
behavior is unchanged — the same accuracy can hide a shift from one-shot
to iterative problem-solving, changed tool-use reliance, or a different
failure-mode mix that matters operationally (e.g., for latency, cost per
task, or how failures should be triaged). Evaluation protocols for
quantized coding agents should report trajectory and failure-mode
breakdowns, not just pass/fail accuracy.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 2 Nov 2026, no revisions). The model/quantization comparison
design (Qwen2.5-Coder-Instruct 7B/14B/32B, Devstral-Small-2507 24B; BF16
vs. AWQ/GPTQ; OJBench, three seeds), the "no significant accuracy loss"
finding, the Qwen-7B one-shot-vs-loop shift (17→0, 10→25), the
Qwen-32B-vs-Devstral tool-use contrast, and the divergent failure-mode
shifts all trace to the fetched abstract text, which is the paper's own
stated summary of its results — treated as `verified` on this library's
convention for single-source arXiv preprints whose headline figures are
self-reported. The full paper (statistical tests, complete per-condition
tables, author affiliations) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
