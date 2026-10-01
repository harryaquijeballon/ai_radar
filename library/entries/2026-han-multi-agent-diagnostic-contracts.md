---
slug: 2026-han-multi-agent-diagnostic-contracts
title: "Where Do Multi-Agent Systems Fail? Evidence-Grounded Diagnosis of Collective Mechanisms"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2609.38761
canonical_ids: ["arxiv:2609.38761"]
publisher_or_author: "Zhengye Han — arXiv preprint"
published: 2026-09-30
captured: 2026-10-01
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
license: "CC BY 4.0"
rationale: >-
  Lenses 4 and 5 (validation, observability): shows correct final answers can
  hide broken multi-agent mechanisms, and offers diagnostic contracts tying
  violations to the execution evidence needed to establish them.
---

# Where Do Multi-Agent Systems Fail? Evidence-Grounded Diagnosis of Collective Mechanisms

## Summary

The abstract argues that a multi-agent system can break one of its collective mechanisms and still produce correct answers, so output checks alone miss failures. The paper introduces diagnostic contracts: specifications that separate a violation from the execution evidence required to establish it. Reported findings: LLM diagnosers extracted significantly more violations from internal records than from public outputs; generic prompts often claimed certainty without evidence, while contract-referencing prompts improved accuracy; diagnostic performance degraded on independently developed systems, indicating limited generalisation.

## Why it matters

For agentic simulations whose outputs must be defended, it is a reason to log and audit internal agent interactions, not only final answers, and to require cited evidence for any failure diagnosis. The generalisation result is a caution against assuming a diagnoser tuned on one system transfers.

## Verification notes

Read the arXiv abstract page (submitted 2026-09-30, CC BY 4.0). Claims are traced to the abstract only; the full paper, quantitative results and any code were not read, and no code link is given on the page. Treat the findings as preprint, not peer reviewed.

## Updates

- **2026-10-01** — Captured by the unattended daily scan.

## Related entries

None yet.
