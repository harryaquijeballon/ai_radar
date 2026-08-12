---
slug: 2026-anand-archer-compliance-harness
title: "ARCHER: Agentic Rule and Compliance Harness for Executable Regulations"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.25566
canonical_ids: ["arxiv:2607.25566"]
publisher_or_author: "Chiraag Singh Anand, Xue Wen Tan, Lionel Teo, Eric Tan — arXiv preprint"
published: 2026-07-28
captured: 2026-07-30
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on reproducibility/security/governance and agent orchestration: a
  deterministic multi-agent system that generates auditable verification
  code from regulatory text, with measured accuracy gains over
  single-pass prompting and a concrete cost/accuracy result for
  open-weights self-hosted models — a transferable pattern for building
  compliance-checking agent systems.
---

# ARCHER: Agentic Rule and Compliance Harness for Executable Regulations

## Summary
ARCHER targets automated building-compliance verification, an area the authors describe as currently served by rigid, proprietary, hard-to-adapt checkers. The system generates auditable verification code directly from regulatory Codes of Practice using multi-agent orchestration in a test-driven pattern, aiming for transparent, adaptable, scalable compliance checking. The authors report ARCHER's deterministic multi-agent approach improves accuracy by 82% compared to single-pass prompting baselines. Evaluated across four different language models and multiple data-governance configurations, a further reported result is that open-weights, self-hosted models achieved 97.8% of frontier-API accuracy at roughly one-quarter the cost, which the authors argue makes "data-sovereign compliance checking practical."

## Why it matters
This is a concrete architectural pattern — deterministic multi-agent orchestration generating auditable, test-driven verification code from source regulatory text — for anyone building agent systems that must produce defensible, checkable outputs against a rule set, not just building compliance tools specifically. The reported open-weights-vs-frontier cost/accuracy trade-off (97.8% of accuracy at ~25% of cost) is a specific, usable data point for teams weighing self-hosted models for governance-sensitive or data-sovereignty-constrained agent deployments.

## Verification notes
Source is an arXiv preprint (cs.MA, surfaced via the arXiv cs.MA curated listing on 2026-07-30, submitted 2026-07-28). The abstract page was fetched directly; all summarized claims and figures above are quoted or closely paraphrased from that abstract text. The full paper (benchmark construction, per-model breakdown) was not fetched, so verification rests on the source's own stated abstract results, not independent corroboration.

## Updates
None yet.

## Related entries
None yet.
