---
slug: 2026-mabene-ho-discriminatory-local-laws
title: "Hidden in Plain Text: LLM-Assisted Detection of Discriminatory Municipal Laws"
status: accepted
domains: [ai_engineering, social_science]
source_type: academic
source_url: https://hai.stanford.edu/news/ai-legal-review-says-millions-live-under-discriminatory-local-laws
canonical_ids: []
publisher_or_author: "Yasmine Mabene, Daniel E. Ho, Dan Bateyko, Derek Ouyang — Stanford RegLab, ICAIL 2026"
published: 2026-09-08
captured: 2026-09-09
relevance:
  social_science: high
  ai_engineering: high
verification: verified
rationale: >-
  A concrete, human-validated application of a staged LLM pipeline to a
  large-scale legal/policy research task (ai_engineering lens 8: reliable
  research and policy products) with reported accuracy against expert
  annotators — a rare instance of an AI-for-research application evaluated
  rather than merely demonstrated (social_science lens 6).
---

# Hidden in Plain Text: LLM-Assisted Detection of Discriminatory Municipal Laws

## Summary
Stanford RegLab researchers (Yasmine Mabene, Daniel E. Ho, Dan Bateyko, Derek Ouyang) built a multi-stage LLM pipeline to scan roughly 9 million local-law sections across 9,623 U.S. jurisdictions for discriminatory provisions. The pipeline first flags statutes referencing protected categories (race, religion, sex/gender/sexual orientation, marital status, national origin, genetic information, age, disability), then classifies whether the statute imposes differential treatment on that basis, then ranks flagged statutes by review priority; human legal experts then filter the output, distinguishing genuinely discriminatory provisions from acceptable differences (e.g., accessibility accommodations). The pipeline surfaced roughly 10,000 suspect laws across jurisdictions covering about 75% of the U.S. population, including over 2,000 provisions barring non-citizens from professional licenses or occupations and more than 30,000 provisions containing offensive language; the authors estimate roughly 50 million Americans live under overtly discriminatory local laws. Measured against human annotators, the pipeline achieved over 90% accuracy in identifying differential legal treatment and 88% agreement with the provisions human reviewers separately rated "high priority." The authors note the method does not catch facially neutral laws with discriminatory effect, nor discriminatory enforcement patterns, and that human review remained essential throughout. The paper is presented at ICAIL 2026; a companion site (hidden-in-plain-text.reglabapp.com) lets users explore individual flagged provisions.

## Why it matters
For ai_engineering: a concrete, validated example of taking a document-grounded AI research/analysis pipeline from demo to defensible — staged LLM classification against a fixed taxonomy, priority-ranked for review, and checked against a human-expert agreement rate, with explicit, stated limits on what the method cannot catch (lens 8). For social_science: a concrete, evaluable case of AI applied to legal/policy research at a scale (9,623 jurisdictions, ~9 million statute sections) no manual review could match, reported with transparent validation metrics rather than as an unvalidated demo (lens 6).

## Verification notes
Traced directly to Stanford HAI's announcement page, which quotes the study's stated methodology and headline statistics (accuracy, agreement rate, statute and jurisdiction counts) directly. This is a first-party institutional account of the authors' own research; the underlying ICAIL 2026 conference paper itself was not independently located or fetched this run (no public preprint or DOI found), so treat the summarized figures as traced to this institutional source rather than independently cross-checked against the paper text itself.

## Updates
None yet.

## Related entries
None yet.
