---
slug: 2026-rajpurohit-finveriqa-independent-verification
title: "FinVeriQA: Financial Research Agents for Question Answering — Routing, Retrieval, MCP Tool Use, and Provenance-Aware Evidence Verification"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.25071
canonical_ids: ["arxiv:2611.25071"]
publisher_or_author: "Meenakshi Rajpurohit, Anna Phan, Ravikumar Komandur Narayanan, Gunanidhi Ramakrishnan, Nathan Howland — arXiv preprint"
published: 2026-11-18
captured: 2026-11-20
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation/validation) and lens 3/8 (MCP tool use;
  reliable research products): an open-source multi-agent architecture for
  financial QA that separates computation, retrieval, and verification by
  construction, plus a controlled finding — self-consistency/shared-evidence
  checks miss errors that checking against the original source catches —
  directly applicable to any RAG or agent-verification design in this
  profile's policy-simulation interest.
---

# FinVeriQA: Financial Research Agents for Question Answering — Routing, Retrieval, MCP Tool Use, and Provenance-Aware Evidence Verification

## Summary

Starts from the observation that LLMs produce fluent financial analysis
but "miscompute ratios, recall stale prices, and route questions to the
wrong tool with high confidence." The authors present FinVeriQA, an
open-source multi-agent prototype for answering questions over SEC filings
and live market data: a small typed-decision model routes questions and
filters out requests for investment advice, Python performs all numerical
computation, retrieval and tools gather evidence, Mistral-7B drafts a
cited answer, and a code validator checks citations and numbers; a Model
Context Protocol server exposes the pipeline. In live experiments, the
typed router outperformed Mistral-7B at routing, and a larger DeepSeek-R1
model routed better still but far more slowly. Quoted directly: "Mistral-7B
computed 29% of 100 financial calculations correctly against 100% for
Python." A case study found both agent answers passed validation despite
attributing sample data to the wrong companies — quoted: "both agent
answers passed validation while describing AMD sample data under NVIDIA's
and Alphabet's names." A controlled study on the FinRank benchmark explains
why: when shared evidence contains one corrupted figure, self-consistency
checks stay confident, while "a shared-evidence check (the kind our
validator performs) catches 35% of the errors" — far more than
self-consistency alone, though still partial. The authors conclude:
"Verification must be independent of the evidence the writer saw."

## Why it matters

For anyone building agent systems meant to produce defensible research or
policy output: a directly transferable design lesson — routing and
numerical computation should be handled by typed/deterministic components,
not left to the generation model — paired with a controlled demonstration
that self-consistency-style validation (checking an answer against the
same evidence the writer used) systematically misses errors that an
independent, source-grounded check catches. That is a concrete argument
for building verification paths that re-derive evidence independently
rather than re-checking the writer's own trail, directly relevant to this
profile's "reliable research and policy products" interest.

## Verification notes

arXiv abstract page fetched directly (2026-11-20); title, full author
list, and an 18 November 2026 submission date confirmed. Verbatim quotes
obtained for the core miscomputation claim, the 29%-vs-100% Mistral-7B/
Python figure, the AMD/NVIDIA/Alphabet misattribution case study, the 35%
shared-evidence-check catch rate, and the "verification must be
independent" conclusion. Full paper (FinRank benchmark construction,
full routing comparison, validator implementation) not read at capture.
No independent secondary corroboration attempted (new working paper, no
secondary coverage found this run).

## Updates

None yet.

## Related entries

None yet.
