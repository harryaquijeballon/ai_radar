---
slug: 2026-zhang-reconcile-trust-tiered-research-writer
title: "Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research"
status: accepted
domains: [ai_engineering, social_science]
source_type: academic
source_url: https://arxiv.org/abs/2608.12984
canonical_ids: ["arxiv:2608.12984"]
publisher_or_author: "Xing Zhang, Yanwei Cui, Guanghui Wang, Peiyang He — arXiv preprint"
published: 2026-08-14
captured: 2026-08-14
relevance:
  social_science: medium
  ai_engineering: high
rationale: >-
  Squarely on ai_engineering lens 8 (reliable research and policy products):
  a deterministic "librarian" plus multi-agent "writer" architecture aimed at
  eliminating temporal/factual drift in AI-generated research reports, with
  strong quantified reliability numbers, evaluated on real economic data
  sources (SEC filings, labor statistics). Medium for social_science lens 6
  (AI applied to social-science research): a generic research-report
  pipeline, not itself economic research, but directly usable infrastructure
  for building more trustworthy automated research/policy pipelines.
verification: partial
---

# Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research

## Summary

The paper addresses temporal and factual inconsistency in AI-generated
research reports by splitting the system into a deterministic "librarian"
that maintains a trust-tiered ontology (evidence cards, an authoritative
metric ledger, and a claim graph as a persistent knowledge base) and a
multi-agent "writer" that produces reports fixed to a specified knowledge
cutoff without look-ahead. Evaluated on 6,130 sources yielding 555,926
evidence cards drawn from SEC filings, labor statistics, and Wikipedia.
Reported results: 6,845 cross-sectional contradictions eliminated to zero;
trust-tiered source selection scored 22/22 correct versus 9/22 for a
baseline popularity-first selection method; model routing ran 3.7x faster
than serial processing while maintaining quality; zero look-ahead
(temporal-cutoff) violations across seven tested cutoffs; defect-injection
testing of the quality-control step achieved recall 1.0 and precision 1.0.

## Why it matters

A concretely quantified architecture pattern — separate deterministic
knowledge maintenance from generative writing — for anyone building
AI-assisted research or policy-analysis products that must stay
point-in-time-consistent and avoid hallucinated or anachronistic claims;
directly relevant to the standing "agentic simulation of policy
interventions" interest this radar tracks (ai_engineering lens 8), and
useful infrastructure for building more defensible AI-assisted
social-science research pipelines (social_science lens 6).

## Verification notes

Read via the arXiv abstract page only; full paper and evaluation data not
examined. The quantitative results above (contradiction elimination,
22/22 vs 9/22, 3.7x speedup, recall/precision 1.0) are as stated on the
fetched abstract page and have not been independently corroborated against
a second source — several of these figures (perfect precision/recall,
22/22) read as unusually clean and warrant a skeptical read of the full
methodology before relying on them.

## Updates

None yet.

## Related entries

None yet.
