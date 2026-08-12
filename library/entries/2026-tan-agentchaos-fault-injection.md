---
slug: 2026-tan-agentchaos-fault-injection
title: "AgentChaos: Chaos Engineering for Agent Systems via Programmatic Fault Injection"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.06790
canonical_ids: ["arxiv:2608.06790"]
publisher_or_author: "Gou Tan, Zhensu Sun, Jieke Shi, Ting Zhang, Zilong He, Qingfu Wu, Shuai Liang, Weifeng Sun, Junda He, Pengfei Chen, Chuanfu Zhang, Lwin Khin Shar, David Lo — arXiv preprint"
published: 2026-08-07
captured: 2026-08-10
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 5 (observability/failure taxonomy) and lens 6 (reliability,
  sandboxing): an HTTP-layer, non-intrusive fault-injection framework any
  team could point at their own agent stack, with a taxonomy of fault types
  and a generalizable, actionable finding — robustness depends on system
  implementation, not model capability — plus a quantified gap in current
  diagnostic tooling.
---

# AgentChaos: Chaos Engineering for Agent Systems via Programmatic Fault Injection

## Summary

Introduces a chaos-engineering framework for evaluating how AI agent systems
handle faults arising from the language-model API layer — server errors and
corrupted responses that agent systems encounter in practice but that
existing evaluation methods struggle to test without code modification or
offline replay. The framework injects faults at the HTTP layer where every
system talks to its LLM, enabling "controlled, runtime, non-intrusive"
fault injection with no source-code changes. Faults are categorized into
crash, omission, and value types affecting both content and tool calls.
Testing across multiple agent systems found pass@1 dropping by up to 50
percentage points under fault conditions, with robustness patterns
consistent across different underlying language models — the paper's
central claim is that robustness "depends on system implementation rather
than model capability." Current diagnostic methods performed poorly at
identifying what went wrong: below 53% accuracy on fault-type
identification and below 56% on fault-identification steps.

## Why it matters

A directly reusable methodology, not just a finding: any team running
production agents can adopt HTTP-layer fault injection to test their own
system's resilience to the kind of API-level failures (crashes, dropped
content, corrupted values) that are common in practice but rarely tested
deliberately. The headline finding — that robustness is a property of how
you build the system, not which model you use — is an actionable argument
for investing in agent-level fault handling rather than assuming a stronger
model will be more robust.

## Verification notes

arXiv abstract page fetched directly (2026-08-10); authors, submission date
(7 Aug 2026, v1), and category confirmed. All claims in the Summary — the
HTTP-layer, non-intrusive injection design, the crash/omission/value fault
taxonomy, the up-to-50-percentage-point pass@1 degradation, the
implementation-not-capability finding, and the sub-53%/sub-56% diagnostic
accuracy figures — trace directly to the fetched abstract text. No
independent corroboration attempted (preprint, not yet peer reviewed). Full
paper PDF not read at capture.

## Updates

None yet.

## Related entries

None yet.
