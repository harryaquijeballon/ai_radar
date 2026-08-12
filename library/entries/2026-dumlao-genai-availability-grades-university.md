---
slug: 2026-dumlao-genai-availability-grades-university
title: "Generative AI Availability, Grades, and Student Satisfaction at a Large University"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2607.21534
canonical_ids: ["arxiv:2607.21534", "doi:10.48550/arXiv.2607.21534"]
publisher_or_author: "James M. Zumel Dumlao, Meng Wang, Zhonghan Xie, Junyao Hu, Ivan Bar, George Chaney III, Henry Gold, Misha Teplitskiy — arXiv preprint (cs.CY)"
published: 2026-07-23
captured: 2026-07-27
relevance:
  social_science: medium
  ai_engineering: n/a
verification: verified
rationale: >-
  Medium on the causal-inference/empirical-methods lens: a large-sample
  (156,135 students; 87,936 course offerings), decade-spanning
  difference-in-differences test of the "GenAI substitution hypothesis"
  (that AI availability inflates grades via offloaded cognitive effort),
  finding no significant effect — useful evidence, but single-institution
  scope and a standard (not methodologically novel) DiD design keep it
  below high. The human-validated LLM pipeline used to classify course
  assessment types from syllabi is a minor secondary point on the
  AI-applied-to-research lens.
---

# Generative AI Availability, Grades, and Student Satisfaction at a Large University

## Summary

Tests the "GenAI substitution hypothesis" — that students offload cognitive
effort to generative AI, inflating grades in AI-susceptible courses (those
relying on take-home problem sets and essays rather than in-class exams)
without genuine learning. Uses syllabus and administrative data from a
large U.S. university spanning 2015–2025 (156,135 students; 87,936 course
offerings). Courses' GenAI susceptibility is measured with a
human-validated LLM pipeline that extracts assessment types from syllabi.
The core design is a difference-in-differences comparison of outcomes
before and after ChatGPT's release, modeling COVID-19 pandemic effects as
either persistent or transient (a robustness check on a known confound).
Findings: no significant differential effect of GenAI availability on
grades overall or among previously lower-performing students;
self-reported understanding effects are likewise insignificant; effects on
self-reported interest are significant only under the transient-pandemic
assumption. The authors conclude the evidence tempers concerns that GenAI
inflates grades or reduces student satisfaction.

## Why it matters

A large-sample counterpoint, using a defensible causal design, to
widespread "AI is inflating grades" narratives — useful as a citable null
result when the substitution-hypothesis claim comes up in policy or
institutional discussions about generative AI in education. The syllabus
classification pipeline (LLM extraction validated against human coding) is
also a small but concrete example of an AI-assisted empirical-pipeline
component for social-science research.

## Verification notes

arXiv abstract page fetched directly (2026-07-27); title, authors,
"Submitted on 23 Jul 2026", categories (cs.CY, econ.GN) confirmed. Every
claim in the Summary — sample size, time span, methodology, and each
reported (null and non-null) finding — traces directly to the abstract
text, the primary source for this pre-publication preprint. Full paper
text not read at capture, so robustness-check details and the LLM
pipeline's validation procedure are unverified beyond the abstract's
framing. Upgrade path: read the full PDF to confirm the DiD specification
and the human-validation procedure for the LLM syllabus-classification
pipeline.

## Updates

None yet.

## Related entries

None yet.
