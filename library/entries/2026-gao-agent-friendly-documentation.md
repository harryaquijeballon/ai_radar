---
slug: 2026-gao-agent-friendly-documentation
title: "From Agent Behaviour to Agent-Friendly Documentation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.20195
canonical_ids: ["arxiv:2608.20195"]
publisher_or_author: "Zhijun Gao, Jing Chen"
published: 2026-08-20
captured: 2026-08-21
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Empirical, quantified evidence on what documentation coding agents actually
  consult and when, directly usable for structuring repo-level agent
  instructions — lens 2 (harness/context engineering) and lens 7
  (AI-assisted software development).
---

# From Agent Behaviour to Agent-Friendly Documentation

## Summary

An empirical study of 557 agentic coding sessions (from the SWE-chat dataset) and
33,097 pull requests (from the AIDev dataset) analyzing how coding agents actually
interact with documentation versus code. The paper reports that agents consult
agent-facing instruction files (e.g., AGENTS.md-style files) in 60.5% of
documentation interactions, versus 10.6% for traditional docs, with a near-zero
unadjusted transition probability (0.002) from a documentation-consultation event
to a subsequent code edit. Agents self-initiate documentation search in 70.2% of
cases versus only 7.5% triggered by a failure signal, and code changes precede
documentation updates 4.7x more often than the reverse. The authors propose a
"two-lobed cycle" model of agent-documentation interaction and argue that assumed
"agent-friendly documentation" properties — actionability and verifiability — lack
behavioral support in the observed data (unverified: the interpretive framing and
the "lack of behavioral support" conclusion are the authors' own synthesis, not
independently checked here).

## Why it matters

Gives teams building or maintaining agent-facing repositories concrete, quantified
evidence about which documentation formats agents actually use and how — useful
for deciding where to invest effort (instruction files over prose docs) and for
questioning assumptions about what makes documentation "agent-friendly."

## Verification notes

Read directly from the arXiv abstract; the quantified figures (60.5%, 10.6%,
0.002, 70.2%, 7.5%, 4.7x) are traced to the source text. No independent
corroboration was possible — this is a newly posted preprint (submitted 20 Aug
2026) with no second source yet. Verification is `partial`: claims are traced,
but load-bearing statistics are not independently corroborated.

## Updates

- **2026-08-21** — Entry created.

## Related entries

None yet.
