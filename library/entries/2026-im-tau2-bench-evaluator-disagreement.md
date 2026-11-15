---
slug: 2026-im-tau2-bench-evaluator-disagreement
title: "When Evaluators of AI Agents Disagree: An Empirical Study of Native Scoring, LLM Judges, and Commit-Boundary Checks on tau2-bench"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.14581
canonical_ids: ["arxiv:2611.14581"]
publisher_or_author: "Sungbin Im — arXiv preprint (cs.SE)"
published: 2026-11-10
captured: 2026-11-15
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Directly on lens 4 (evaluation, validation and deterministic guardrails):
  a quantified, reproducible comparison showing LLM judges and a cheap
  rule-based boundary check reach different verdicts on the same agent
  episodes, with the deterministic check catching failures the judges
  systematically miss — exactly the evidence class this lens asks for.
---

# When Evaluators of AI Agents Disagree

## Summary
The paper tests whether the common ways of evaluating agentic LLM
workflows are interchangeable. Benchmarks typically compare final database
state to a gold answer; deployed services usually lack a gold answer and
instead rely on an LLM judge reading the transcript. Using 2,160 episodes
in the tau2-bench airline and retail domains (every database write
recorded), each episode was scored four ways: native gold-state scoring,
an LLM judge, that same judge given the policy document, and a rule-based
"boundary evaluator" that checks whether each write was expected under the
policy. Two human annotators independently labeled 120 episodes for task
correctness, policy compliance, and commitment correctness.

Key findings: the LLM judge was internally consistent (repeated its own
verdict 98.2% of the time) but agreed with native gold-state scoring only
56.2% of the time. Of 11 episodes where the agent executed a forbidden
database write, the judge passed 10–11 of them regardless of whether it
saw the policy or transcript, and a stronger judge still passed 6 of 11.
The rule-based boundary evaluator — no model call required — caught all
11, and no judge configuration significantly beat it against the human
labels. Forbidden writes occurred in 11.1% of episodes with no gates
active; adding verification, correction, and safe-termination gates did
not significantly reduce that rate, a result the author traces (as a
candidate explanation, not confirmed) to the gates' evidence digest
dropping order-status and authentication fields, causing valid requests to
be wrongly rejected rather than catching genuinely forbidden ones.

## Why it matters
A directly actionable warning for anyone building or buying an
LLM-as-judge evaluation pipeline for agents: the choice of evaluator can
change the conclusion about whether an agent is safe to deploy, and a
cheap deterministic boundary check can outperform an LLM judge at catching
genuinely forbidden actions. Teams building research or policy agents
that write to any external state (databases, APIs, files) have a
concrete, low-cost pattern to add — a rule-based write-boundary check
alongside or instead of judge-based scoring.

## Verification notes
Fetched the arXiv abstract page directly; the summary above traces to its
reported figures (2,160 episodes, 98.2%/56.2% agreement rates, 10–11 and
6/11 forbidden-write pass rates, 11.1% baseline rate). The full paper body
and the Zenodo replication package were not independently fetched in this
session, so the detailed experimental protocol was not corroborated beyond
the abstract — verification is partial. No contradicting source was
found.

## Updates
None yet.

## Related entries
None yet.
