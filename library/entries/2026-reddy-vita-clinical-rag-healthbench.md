---
slug: 2026-reddy-vita-clinical-rag-healthbench
title: "A corpus-specific clinical RAG system matches or outperforms newer frontier LLMs on HealthBench"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.12138
canonical_ids: ["arxiv:2608.12138"]
publisher_or_author: "Praveen Reddy, Charuta Mandke, Suvrankar Datta, Sarah Khan, Siddharth Reddy Anthireddy, Shitij Arora, Vishal Singh — arXiv preprint (cs.CL)"
published: 2026-08-12
captured: 2026-08-13
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 8 (reliable research and policy products): a rigorously
  benchmarked, corpus-specific RAG system (VITA) outperforms several named
  frontier general-purpose LLMs on a large, standard benchmark (4,023
  HealthBench questions), with a follow-up neutral-judge retest — direct
  evidence that domain-grounded retrieval can beat a bigger general model,
  a transferable lesson for any document-grounded research or policy
  product regardless of subject domain.
---

# A corpus-specific clinical RAG system matches or outperforms newer frontier LLMs on HealthBench

## Summary
General-purpose LLMs have recently matched or exceeded specialized clinical AI tools on medical benchmarks, but those comparisons rely on limited systems and high-income-setting benchmarks. This paper evaluates VITA, a retrieval-augmented generation system built for contextual knowledge retrieval in India and other low- and middle-income countries, drawing from curated disease-specific guidelines, India-specific antimicrobial-resistance data, national formulary constraints, and resource-limited care protocols. On 4,023 English-language HealthBench questions, VITA ranked first with 51.9% of rubric points, ahead of GPT-5.4 (46.1%), o4-mini (44.3%), Gemini 3.1 Pro (42.6%), and Claude Sonnet 4.6 (37.3%). A follow-up 500-question retest using current-generation models and a neutral open-weight judge found VITA and GPT-5.5 statistically indistinguishable on mean per-question score, though VITA led on weighted scores and question wins.

## Why it matters
Concrete, benchmarked evidence that a purpose-built, corpus-specific RAG system can match or beat larger general-purpose frontier models on a domain task — with the gap widest against generic models and narrowing (but not closing) against the very newest frontier model. The transferable lesson for any document-grounded research or policy product (this project's own stated interest, lens 8) is that corpus specificity and grounding, not raw model scale, may be the more cost-effective lever — and that retest methodology (neutral judge, current-generation baselines) matters for how durable such a claim is.

## Verification notes
Read via the arXiv abstract page (2026-08-13). The system description, the 4,023-question HealthBench result with all five named model scores, and the 500-question neutral-judge retest finding are quoted/paraphrased directly from the abstract. Full paper (retrieval corpus construction, methodology) not read at capture; findings not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
