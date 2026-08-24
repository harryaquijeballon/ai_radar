---
slug: 2026-angela-shi-case-file-relational-tables-rag
title: "Parse the Folder, Not Just the PDFs: The Relational Tables RAG Needs on a Case File"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/parse-the-folder-not-just-the-pdfs-the-relational-tables-rag-needs-on-a-case-file/
canonical_ids: []
publisher_or_author: "Angela Shi — Towards Data Science"
published: 2026-08-23
captured: 2026-08-24
relevance:
  social_science: n/a
  ai_engineering: medium
rationale: >-
  Medium on lens 8 (reliable research and policy products): argues case
  files (heterogeneous document bundles about one entity) need a relational,
  expected-pieces-plus-conflicts structure rather than passage retrieval,
  since "missing document" and "cross-document contradiction" are not
  answerable by ranking passages — a practical, on-lens framework, but a
  single worked example with no evaluation benchmark, continuing the
  author's existing document-intelligence series already represented in
  this library.
verification: partial
---

# Parse the Folder, Not Just the PDFs: The Relational Tables RAG Needs on a Case File

## Summary

Shi argues that case files — bundles of heterogeneous documents about a single entity, such as an insurance claim — need a different RAG architecture than either small homogeneous corpora or single long documents, because the unit of work is the whole bundle, not a passage. Two questions handlers routinely ask cannot be answered by retrieval alone: whether a required document was ever filed (a missing piece is a correct answer, not a retrieval failure), and whether values conflict across documents in the bundle. She proposes structuring the bundle as relational tables: an index of expected pieces (roles, counts, conditions), role assignments with confidence scores, typed value extraction before comparison, and citations preserved per extracted value. A worked example — a fire claim on a joinery workshop with 11 PDFs — shows a missing required "fire brigade report" and a conflicting inspection date (12 March vs. 3 March) surfaced as a CaseState object of present/missing/unmatched pieces plus conflicts, rather than ranked passages. Shi explicitly notes this is the shape with "the least prior art of the three" in her series and that it lacks a standardized evaluation benchmark, recommending a test of 50 manually reviewed cases measuring false positives and missed pieces separately.

## Why it matters

A concrete answer to a RAG-grounding failure mode this profile cares about directly (lens 8): passage retrieval structurally cannot represent "this required document is absent" or "these two documents disagree," both of which are common, high-stakes questions in case-file-style research and policy work (compliance files, evidence bundles, due-diligence packets). The relational-table-plus-CaseState pattern is a specific, adoptable design a builder could prototype against their own case-file corpus, with the author's own caveat about the missing evaluation benchmark setting appropriately modest expectations.

## Verification notes

Read via direct fetch of the article page, which gives the full argument, the worked example, and the author's own stated limitation (no standardized benchmark yet). Verification marked partial: the framework and worked example are traceable to the source, but the approach's real-world effectiveness beyond the single worked example is unvalidated, as the author herself states.

## Updates

None yet.

## Related entries

None yet.
