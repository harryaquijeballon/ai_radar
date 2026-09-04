---
slug: 2026-shi-rag-not-in-document-evidence
title: "A RAG That Says \"Not in This Document\" Has to Show Four Kinds of Evidence"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/a-rag-that-says-not-in-this-document-has-to-show-four-kinds-of-evidence/
canonical_ids: []
publisher_or_author: "Kezhan Shi — Towards Data Science"
published: 2026-09-02
captured: 2026-09-04
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  A concrete abstention framework for RAG systems (lens 4/8): a bare "not in
  this document" answer is treated as no more trustworthy than a confident
  wrong answer unless it is backed by a structured evidence chain, directly
  relevant to building defensible research/policy retrieval products.
verification: partial
---

# A RAG That Says "Not in This Document" Has to Show Four Kinds of Evidence

## Summary
The article argues that an unjustified "no answer" from a RAG system is nearly as untrustworthy as a confident wrong answer, and proposes a four-part evidence chain a system should produce before claiming a document doesn't contain an answer: (1) a parsing brick, aggregating document-coverage data (pages parsed, images OCR'd, unresolved cross-references); (2) a question-parsing brick, using expert-validated keyword sets with algorithmic clustering as a safety net for vocabulary coverage; (3) a retrieval brick, doing full-corpus sweeps rather than top-k ranking so it can show exactly where each concept variant does or doesn't appear; and (4) a generation brick, producing structured output listing the concepts searched, hit counts, the closest non-answers found and why they don't qualify, and optional suggestions. The framework is demonstrated on a case study — searching the World Bank's Commodity Markets Outlook for mentions of AI's electricity consumption — with Python code and sample structured output, but no quantified accuracy or user-study metrics.

## Why it matters
This profile's lens 8 (reliable research and policy products) explicitly calls for RAG and document-grounding "done rigorously" and citation verification that moves a product "from demo to defensible." A structured, inspectable evidence chain for abstention answers is exactly the kind of guardrail that lets a research or policy RAG system's "I don't know" be checked and trusted rather than taken on faith — directly transferable to any document-grounded agent used for policy analysis.

## Verification notes
Fetched and read directly from the Towards Data Science post. The four-brick framework and the World Bank case-study walkthrough (including the specific document, search concepts, and sample output shown) are traceable to the article's own text and code. There is no quantified accuracy, precision/recall, or user-study evidence — the claims are about the framework's design and are illustrated, not benchmarked, so verification is recorded as `partial`.

## Updates
None yet.

## Related entries
[2026-shi-tables-pdfs-rag-grid](2026-shi-tables-pdfs-rag-grid.md) — same author's TDS post on RAG table structure preservation, published one day later.
