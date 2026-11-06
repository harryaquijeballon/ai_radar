---
slug: 2026-donno-agent2agent-authorization-propagation
title: "Authorization Propagation in Agent2Agent Systems: An Experimental Security Evaluation of Multi-Hop Delegation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07050
canonical_ids: ["arxiv:2611.07050"]
publisher_or_author: "Gabriele Donno, Kashif Mehmood, Katina Kralevska"
published: 2026-11-04
captured: 2026-11-06
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance): a concrete,
  quantified security evaluation of delegated agent-to-agent authorization
  with a named, specific failure mode (forgeable shared-key evidence, no
  semantic authority attenuation) directly usable by anyone designing
  multi-agent permission models.
---

# Authorization Propagation in Agent2Agent Systems: An Experimental Security Evaluation of Multi-Hop Delegation

## Summary

The paper examines security risks in delegated Agent2Agent (A2A)
workflows, where the agent making a request downstream may not be the
principal that originally granted authority. The authors build and test a
layered downstream-verification design in a synthetic four-party
healthcare-reimbursement workflow, separating: the current caller's
context; transitive authorization evidence; per-hop Ed25519 request
authentication; and independent replay-protection state for requests and
authorization artifacts separately. Across 15 adversarial conditions, 14
were rejected by the design. The one that was not rejected exposes what
the authors call missing "semantic authority attenuation" — authority is
not narrowed as it passes along the delegation chain, so a downstream
agent can retain authority broader than the task actually requires. In a
separate experiment, a holder of the shared authorization-evidence HMAC
key could modify the represented authority and still produce
cryptographically valid evidence, showing a shared symmetric key is
insufficient for origin-verifiable delegation. Overhead was modest: 5.11ms
median security-processing latency and a 3.87kB serialized payload in a
fixed-depth local benchmark.

## Why it matters

Multi-agent systems that delegate tasks between agents — including
research/policy pipelines where one agent hands work to another with some
subset of the original authority — need exactly this kind of adversarial
evaluation before being trusted with real permissions. The paper gives two
directly actionable findings: (1) per-hop asymmetric signing plus
independent replay state blocks the overwhelming majority of tested
attacks cheaply; (2) shared symmetric keys for authorization evidence are
a specific, demonstrated forgery vector, and authority needs to narrow
(not just persist) across delegation hops. Both are concrete design
requirements, not general advice.

## Verification notes

Read the abstract and submission metadata directly on arXiv (v1, 4 Nov
2026, cs.MA). The 14/15 adversarial-rejection result, the HMAC-forgery
finding, and the latency/payload numbers are all stated directly in the
abstract and traced to it. The full experimental design (how representative
the synthetic healthcare workflow is of other delegation settings) was not
independently assessed beyond what the abstract states.

## Updates

None yet.

## Related entries

None yet.
