---
slug: 2026-khan-agarwal-indic-pretraining-pipeline
title: "Scaling Indic Pretraining: 2.8 Trillion Tokens and an Open Data Generation Pipeline"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://huggingface.co/blog/nvidia/scaling-indic-pretraining
canonical_ids: []
publisher_or_author: "Mohammed Safi Ur Rahman Khan, Mitesh Khapra, Anoop Kunchukuttan (AI4Bharat/IIT Madras); Niket Agarwal, Raviraj Joshi, Anusha Kamath, Markus Kliegl, Yev Meyer, Sriharsha Niverty, Kiran Praveen, Utkarsh Vaidya (NVIDIA)"
published: 2026-10-16
captured: 2026-10-17
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Medium on reproducibility/versioning (lens 6): a described data-generation
  pipeline (translate -> MQM-style score -> feedback-guided repair ->
  rescore, with provenance IDs kept throughout) and explicit reproducibility
  recommendations (pin dataset revisions, record synthetic/native shares,
  group held-out splits by source). Quantified at scale (2.8T tokens, 22
  languages) but the engineering lesson is pretraining-data-pipeline
  specific rather than agent/harness-specific.
---

# Scaling Indic Pretraining: 2.8 Trillion Tokens and an Open Data Generation Pipeline

## Summary

A joint AI4Bharat (IIT Madras) / NVIDIA Hugging Face blog post, dated 16 October 2026, describing a synthetic pretraining-data pipeline for 22 Indian languages covering, per the post, "about 97% of Indians" (1.2 billion people, 2011 Census). The pipeline: Gemma-4-31B-it translates English source documents, then judges each output against the source on an MQM-inspired rubric; outputs scoring below 75/100 go through feedback-guided repair and rescoring. Romanized-script text is produced by converting already-accepted native-script translations rather than translating directly from English, which the authors state produced fewer hallucinations. Generation and acceptance are kept separate — the pipeline returns candidates and scores, and a separate filtering policy decides what enters the corpus — and source identifiers are kept throughout for provenance, with source-ID checks removing processing duplicates (explicitly not semantic deduplication). The authors recommend pinning dataset revisions, recording the natural/synthetic and native/romanized token shares, and grouping held-out evaluation splits by shared source across languages. Reported figures: about 2.8 trillion tokens across 22 languages (2,601.0B native-script, 224.6B romanized, by the Gemma-4 tokenizer) drawn from 15 Nemotron-CC-v2 source subsets across 34 language-script configurations; repair recovered 438.4B tokens; continued pretraining of Nemotron 3.5 Super VL used 10B Indic tokens from a 100B-token budget, yielding benchmark gains of 4.98 to 9.82 percentage points on five Indic benchmarks (stated as reflecting the combined synthetic-plus-natural stage, not the synthetic data alone). The authors note quality checks are mostly automated, and that in the twelve-language workflow the translator model also serves as its own judge, with the ten-language workflow needing broader native-speaker validation.

## Why it matters

A concrete reproducibility checklist for anyone building a synthetic-data generation pipeline at scale — separating generation from acceptance, keeping document-level provenance through every transformation, and pinning/recording data-mix composition for every release — that generalises beyond this specific Indic-language application to any pipeline producing training or evaluation data via LLM-in-the-loop generation and LLM-as-judge scoring.

## Verification notes

Source reachable (Hugging Face blog post, fetched directly). Figures and the pipeline description are as stated on the page; not independently corroborated against a second source, and the authors' own caveats (translator-as-judge in the twelve-language workflow, limited native-speaker validation in the ten-language workflow) are carried through above rather than omitted. The benchmark-gain figures are explicitly stated by the authors to reflect the combined pretraining stage, not an isolated measurement of the synthetic corpus's contribution.

## Updates

None yet.

## Related entries

None yet.
