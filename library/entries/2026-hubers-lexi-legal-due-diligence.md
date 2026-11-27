---
slug: 2026-hubers-lexi-legal-due-diligence
title: "From Data Room to Report: End-to-End AI Support for M&A Legal Due Diligence"
status: provisional
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.34120
canonical_ids: ["arxiv:2611.34120"]
publisher_or_author: "Johannes R. Hübers, Daniel Uedelhoven, Manuela Bergau, Markus Beyer, Lars Weber, Tobias Riethmüller, Arkadiusz Rzepka, Tobias Schuh, Maximilian Glaß, Omer Faruk Aydin, Jens Henneberg, Thiago Bell Felix de Oliveira, Lars Hillebrand, Rafet Sifa — arXiv preprint (IEEE BigData 2026 workshop)"
published: 2026-11-25
captured: 2026-11-27
relevance:
  social_science: n/a
  ai_engineering: medium
verification: unverified
rationale: >-
  An end-to-end LLM pipeline (classification, extraction with provenance,
  drafting) for a document-heavy professional workflow with mandatory
  human review — on-lens for lens 8 (reliable research/policy products,
  human-in-the-loop review patterns), retained provisional because the
  system is explicitly work-in-progress with no quantified evaluation.
---

# From Data Room to Report: End-to-End AI Support for M&A Legal Due Diligence

## Summary

The authors present LEXI (Legal Extraction and Intelligence), a work-in-
progress system applying LLMs across the M&A legal due-diligence workflow:
classifying data-room documents under a configurable due-diligence
taxonomy, assigning relevant target entities, extracting predefined
information together with supporting passages and page-level provenance,
and drafting report content from the reviewed findings. Structured outputs
link each stage so model-generated results move through the pipeline in a
controlled form, and lawyers review and correct the classifications and
extractions at each step; the authors state that substantive legal
judgment — assessments, recommendations, risk ratings, and final report
wording — remains with the lawyers. Evaluation covered only the
classification and extraction components, and the authors describe their
initial results only qualitatively, as "preliminary evidence that the
approach is feasible," reporting no accuracy, precision, recall, or
time-savings figures in the accessible abstract/metadata.

## Why it matters

A concrete architectural pattern — document classification against a
configurable taxonomy, extraction with page-level provenance, and
structured handoff to human reviewers before drafting — that is directly
analogous to building a reliable AI-assisted research or policy-document
pipeline (lens 8): the taxonomy-plus-provenance-plus-human-review structure
is reusable even though this particular system's own evaluation is too
preliminary to cite as evidence that the approach works well in practice.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.34120, v1 submitted
2026-11-25, cs.CL; IEEE BigData 2026 workshop paper). The pipeline
architecture is traced to the abstract's own description. No quantified
results (accuracy, precision, recall, or time savings) were present in the
accessible text to verify or corroborate — the authors themselves
characterize their evaluation as preliminary and qualitative — so all
claims are marked unverified and the entry is retained as provisional
pending either a full-text read or a later, evaluated version of the
system.

## Updates

None yet.

## Related entries

None yet.
