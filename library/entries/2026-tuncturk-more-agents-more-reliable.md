---
slug: 2026-tuncturk-more-agents-more-reliable
title: "More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07140
canonical_ids: ["arxiv:2611.07140"]
publisher_or_author: "Burkay Tunçtürk, Koorosh Aslansefat, Yiannis Papadopoulos, Bao Nguyen"
published: 2026-11-04
captured: 2026-11-06
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Directly on lens 4 (evaluation/validation) and lens 1 (orchestration):
  a named method (HIP-LLM extended with a Bayesian failure network) for
  bounding multi-agent system reliability under uncertain input mix, with
  a concrete case-study finding that challenges the common assumption that
  adding agents/voting improves reliability — practically usable for
  anyone designing or evaluating multi-agent reliability claims.
---

# More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty

## Summary

The paper challenges the assumption that adding LLM agents to a system
automatically improves its reliability, arguing that average benchmark
accuracy ignores both the real mix of inputs a deployed system will see
and the rule used to combine agents' answers. The authors extend HIP-LLM
(a hierarchical imprecise-probability method for assessing a single LLM's
reliability) with a Bayesian network modeling a multi-agent system's
failure logic, including the possibility that the combining/voting rule
itself fails. Failure-probability intervals from individual agents
propagate through this network to produce a "reliability envelope" —
a bound showing which evidence actually constrains the system-level
reliability claim, rather than a single point estimate. In a case study
extracting regulated chemical-hazard statements, majority voting across
three models was protected against the weakest model's failure rate but
did not clearly outperform using the single best model; the paper notes a
voter failing on 5% of demands would largely erase whatever advantage it
had over the middle-performing model. Submitted to IEEE Software Magazine;
published under CC BY 4.0.

## Why it matters

A direct, usable warning for anyone building or evaluating multi-agent
systems for research or policy use: ensemble/voting architectures are
often adopted on the implicit assumption that more agents means more
reliability, and this paper gives both a formal reason that assumption can
fail (the combining rule is itself a failure point, and benchmark averages
hide operational-profile mismatch) and a concrete worked example where it
did fail. The HIP-LLM-plus-Bayesian-network method is a transferable
pattern for stating a reliability claim's actual evidentiary bounds
instead of a single accuracy number — directly serviceable for the
policy-simulation interest in validated, defensible agent-system outputs.

## Verification notes

Read the abstract and submission metadata directly on arXiv (v1, 4 Nov
2026, cs.MA cross-listed cs.AI). The method description and the
chemical-hazard case-study finding (majority voting not clearly beating
the best single model; the 5%-failure sensitivity point) are both stated
directly in the abstract and traced to it. The full paper's additional
experimental detail and metrics were not independently fetched; no
load-bearing claim here depends on information beyond the abstract.

## Updates

None yet.

## Related entries

None yet.
