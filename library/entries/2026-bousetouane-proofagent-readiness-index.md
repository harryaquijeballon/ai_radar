---
slug: 2026-bousetouane-proofagent-readiness-index
title: "Stop Shipping AI Agents on Faith: Capability Is Not Production Readiness"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.27677
canonical_ids: ["arxiv:2607.27677"]
publisher_or_author: "Fouad Bousetouane — arXiv preprint"
published: 2026-07-30
captured: 2026-07-31
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation and on reproducibility/security/governance:
  a concrete, structured readiness framework (not commentary) for deciding
  whether an agent is fit for production, validated across two regulated
  domains — directly usable by a team deciding whether to ship an agent.
---

# Stop Shipping AI Agents on Faith: Capability Is Not Production Readiness

## Summary
The paper argues that release decisions for production AI agents too often rely on capability signals — demos or behavioral tests — that do not establish whether an agent is ready to operate under real production constraints; "capability is therefore not production readiness." It introduces the ProofAgent Index (PAI), a governance readiness index combining four dimensions of deployment evidence: Evaluation (observed behavior), Context (the operating environment shaping that behavior), Compliance (alignment with applicable rules/controls), and Governance (whether the organization can authorize, monitor, audit, and control the agent in operation). PAI is implemented inside an open-source infrastructure the authors call ProofAgent Harness, for auditable AI agent evaluation and governance. Validation across two regulated domains, healthcare and finance, shows PAI "carries held out readiness signal and separates higher risk from lower risk configurations." The paper reports that context engineering strongly changes reliability, that capability improves behavior but does not determine readiness, and that governance evidence must remain visible rather than averaged into a single score.

## Why it matters
For any team deciding whether an agent is ready to ship, this offers a structured alternative to ad hoc "it passed our demo" judgment calls: a four-dimension index (Evaluation, Context, Compliance, Governance) that keeps governance evidence visible rather than blending it away, validated in two domains where release mistakes are costly. It is directly usable as a checklist or scoring structure for release-readiness reviews, not just an argument that readiness matters.

## Verification notes
Source is the arXiv abstract page (cs.MA/cs.AI), fetched directly; the quotes and structure above are traced to that abstract text. The full paper (the index's exact scoring methodology, the healthcare/finance validation data) was not fetched, so only the headline claims are traced; verification rests on the source's own stated results rather than independent third-party corroboration.

## Updates
None yet.

## Related entries
None yet.
