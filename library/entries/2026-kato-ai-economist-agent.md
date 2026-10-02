---
slug: 2026-kato-ai-economist-agent
title: "AI Economist Agent: An Agentic Framework for Evidence-Based Economic and Financial Analysis with RAG, Knowledge Graphs, and Large Language Models"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2606.20041
canonical_ids: ["arxiv:2606.20041"]
publisher_or_author: "Masahiro Kato (The University of Tokyo) — arXiv preprint"
published: 2026-06-18
captured: 2026-10-02
relevance:
  social_science: high
  ai_engineering: high
verification: partial
license: "CC BY-NC-ND 4.0"
rationale: >-
  Cross-domain, user-submitted. Social science high (lens 6): a concrete,
  evaluable agentic system for economic and financial stress-scenario
  analysis, run on a dated European application with saved records and
  candid failure reporting. AI engineering high (lenses 4, 6, 8): LLM agents
  interpret and retrieve, but only pre-registered models produce numbers,
  acceptance tests are fixed before outputs are observed, and deterministic
  programs refuse contradictory causal paths — a defensible-by-design
  pattern directly on the policy-simulation interest.
---

# AI Economist Agent: An Agentic Framework for Evidence-Based Economic and Financial Analysis with RAG, Knowledge Graphs, and Large Language Models

## Summary

Starts from the observation that "fluent narratives alone do not establish
the model-based calculations needed for economic conclusions." The
framework splits the work: LLM agents plan the analysis, retrieve evidence
(document RAG plus a knowledge graph of economic relations) and organise
economic mechanisms, while numerical outcomes come only from registered
quantitative models, and predefined tests decide whether intermediate
results may be used in the final report.

Key design choices, as described in the paper:

- **Knowledge graph of typed relations.** Each relation links source and
  destination variables with a sign and evidence fields and is tied to an
  exact source location; "Co-occurrence of two variables in one passage
  does not create a relation." An economic channel is an ordered path of
  such relations from an initiating condition to an outcome.
- **Deterministic composition.** Candidate paths are enumerated by a
  program; the restriction derivation composes directions from relation
  signs and stops when required directions conflict.
- **Registered models and tests.** Quantitative models (a quarterly VAR
  with six variables, two lags and 20,000 residual bootstrap simulations;
  bank-capital models that must meet specified validation thresholds) are
  declared in advance, and numerical statements must match stored model
  output under fixed tests.
- **Frozen, recorded execution.** Seven agents (coordination, evidence
  retrieval, model requests, execution, testing, consistency checking,
  report generation) run on the fixed snapshot `gpt-4o-2024-08-06` at
  temperature zero with strict JSON schemas; every request, response and
  identifier is retained, and a different or unavailable model stops the
  affected stage.

Application: European stress scenarios for three risks (trade
fragmentation, property market correction, market illiquidity) using only
information available by 31 December 2024, from a parsed collection of 51
files (41 PDFs, 10 spreadsheets; 2,744 page records, 4,188 text passages,
54,769 candidate numerical cells). Across seven prompt configurations, 372
LLM calls cost a recorded USD 1.9882. Every Run 7 repetition completes the
property-correction program; the market-illiquidity program stops in every
repetition because the restriction derivation refuses both recorded paths.

Limitations reported by the author: manual inspection found three
displayed relations not supported by their attached text; path ranking
uses the extractor's own confidence rather than independently measured
source support; graph conditions G3–G5 (expanded official sources,
academic studies, independent-support ranking) have no saved execution
records yet, and the numerical comparisons under the release-date rules
"will be reported after the corresponding estimation and reruns."

## Why it matters

For the social-science audience: a worked template for using agents in
scenario and stress-testing work without letting the language model invent
the numbers — evidence is source-located, mechanisms are explicit signed
paths, and conclusions rest on declared models with information-date
discipline. The honest stop on market illiquidity is the point: the system
refuses rather than narrates when its evidence contradicts itself.

For the AI-engineering audience: a compact catalogue of deterministic
guardrails around stochastic components — acceptance tests fixed before
outputs, program-owned path enumeration and composition, frozen model
snapshots, and append-only execution records — with run-level reporting of
calls, cost, completions and stops across prompt configurations. It also
shows a typical failure surface: Run 6's reports exceeded a 1,024-token
output limit and failed to parse, fixed in Run 7 by raising the limit to
2,048 with no prompt change.

## Verification notes

arXiv abstract page fetched 2026-10-02: title, sole author, v1 "Submitted
on 18 Jun 2026", v2 dated 10 Sep 2026, CC BY-NC-ND 4.0 licence confirmed.
Full text read from the arXiv HTML of v2; every figure in the Summary (51
files and parsing counts, cutoff date, model snapshot, temperature zero,
seven agents, VAR specification, 372 calls and USD 1.9882, Run 6/Run 7
token limits and completions, illiquidity refusal, three unsupported
relations, extractor-confidence ranking, G3–G5 status, deferred
comparisons) traced to the paper text by direct search. Not corroborated
independently (single-author preprint, no peer review). The paper says
replication materials (source manifests, code, configurations, saved API
records, tests) exist, but no public repository link was found in the
text; availability is unverified. Upgrade path: corroborate once the
replication materials are public or the deferred comparisons are reported.

## Updates

None yet.

## Related entries

[2026-golden-agentic-orchestration-energy-crisis](2026-golden-agentic-orchestration-energy-crisis.md) — same pattern (agents orchestrate, registered economic models originate every number), applied to energy-crisis scenarios with analyst approval rather than predefined acceptance tests.
[2026-zhu-pai-econ-claude-gated-agents](2026-zhu-pai-econ-claude-gated-agents.md) — related concern: gating agent-produced economic analysis so conclusions stay defensible.
