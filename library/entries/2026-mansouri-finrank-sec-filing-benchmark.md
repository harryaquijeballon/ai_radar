---
slug: 2026-mansouri-finrank-sec-filing-benchmark
title: "FinRank: An Evidence-Grounded Benchmark for Financial Question Answering and Retrieval over SEC Filings"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.07400
canonical_ids: ["arxiv:2608.07400"]
publisher_or_author: "Sasan Mansouri, Daniel Saad, Mark Wahrenburg, Manu Weissel, Fabian Woebbeking — arXiv preprint"
published: 2026-08-07
captured: 2026-08-10
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails): a
  provenance-sensitive retrieval benchmark that separates "right answer"
  from "right evidence," built with hand-curated hard negatives across
  entity/period/comparable-firm confusions — directly usable by anyone
  building document-grounded financial or regulatory-filing agents to test
  grounding rather than just answer correctness.
---

# FinRank: An Evidence-Grounded Benchmark for Financial Question Answering and Retrieval over SEC Filings

## Summary

Argues that financial question answering over SEC filings is usually
evaluated by answer correctness alone, but in filings a plausible and even
numerically correct answer can be grounded in the wrong evidence, because
similar facts and disclosures recur across sections of a filing, across a
firm's own reporting periods, and across comparable firms. FinRank targets
this provenance-sensitive retrieval problem by requiring systems to
identify evidence tied to the intended entity, reporting period, and
disclosure context. The benchmark contains 1,185 manually authored
question-answer records over the 10-K and 10-Q filings of 22 companies.
Each record has a reference answer, gold supporting passages, and
hand-curated hard negatives drawn from confusable passages within a single
filing, across a firm's reporting periods, and across comparable firms.
FinRank evaluates passage retrieval, reranking, and hard-negative
discrimination as three separately measured tasks.

## Why it matters

Most financial or regulatory-filing QA evals check only final-answer
correctness, which a system can pass while citing the wrong reporting
period or the wrong company's filing — a grounding failure that is easy to
miss in a spot check and costly in a research, policy, or compliance
context. FinRank supplies a ready benchmark structure, and specifically a
hard-negative-construction pattern (same entity/different period; same
period/different comparable firm; confusable in-filing passages), that is
reusable for testing any provenance-sensitive document-grounded agent, not
just SEC filings.

## Verification notes

arXiv abstract page fetched directly (2026-08-10); authors, submission date
(7 Aug 2026, v1), and cross-listed categories (cs.AI, cs.DB, econ.GN,
q-fin.GN) confirmed. All claims in the Summary — the provenance-sensitive
framing, the 1,185 records over 22 companies' 10-K/10-Q filings, the
hard-negative construction, and the three separately measured tasks — trace
directly to the fetched abstract text. No institutional affiliation is
stated on the abstract page. No independent corroboration attempted
(preprint, not yet peer reviewed). Full paper PDF not read at capture.

## Updates

None yet.

## Related entries

None yet.
