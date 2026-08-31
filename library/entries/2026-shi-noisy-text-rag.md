---
slug: 2026-shi-noisy-text-rag
title: "Noisy Text in RAG: Typos, OCR, and the Gap Classical Spell-Check Leaves"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/noisy-text-in-rag-typos-ocr-and-the-gap-classical-spell-check-leaves/
canonical_ids: []
publisher_or_author: "Kezhan Shi — Towards Data Science"
published: 2026-08-30
captured: 2026-08-31
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 8 (reliable research and policy products): names three
  distinct noise sources hitting RAG retrieval (typos, transcription noise,
  OCR errors), shows why classical spell-check (Levenshtein/SymSpell) fails
  on them, and gives measured cosine-similarity thresholds plus a stated
  two-path remediation strategy a builder could apply directly.
---

# Noisy Text in RAG: Typos, OCR, and the Gap Classical Spell-Check Leaves

## Summary
Shi distinguishes three sources of RAG-retrieval text noise that share the
same symptom (unmatched tokens) but need different fixes: user typos,
transcription noise (scrambled word boundaries, dropped accents from fast
typing), and OCR errors (character substitutions like l→1 and O→0, broken
ligatures). He shows classical spell-checking (Levenshtein distance,
SymSpell) handles single-word typos but fails when a typo produces a valid
but wrong word ("coverage" vs "overage"), when word boundaries are scrambled,
or when OCR errors compound across a multi-word phrase and push edit
distance into false-positive territory. He reports embedding-based matching
tolerates this noise through holistic phrase understanding, with measured
cosine similarities: typo pairs score >0.95, and OCR-corrupted phrases score
0.86–0.97 despite 2–4 character edits; he also reports chunk granularity
matters, with line-level chunks (0.858) outperforming page-level chunks
(0.787). His recommended strategy: clean important documents once and
thoroughly (SymSpell plus LLM review), but for high-volume documents optimize
retrieval instead (embedding-primary matching with an LLM fallback for
borderline cases), building a corpus-specific keyword dictionary
incrementally rather than doing one-time cleanup.

## Why it matters
Gives builders of document-grounded research/policy RAG systems a concrete,
measured decision rule for where noisy source text (scanned reports,
transcribed interviews, OCR'd archival documents) will silently break exact
or edit-distance matching, plus specific similarity thresholds and a
two-path (clean vs. retrieve-around) strategy to apply rather than a general
"improve your OCR" recommendation — directly usable for the RAG-grounding
and deterministic-guardrail lenses this profile prioritizes.

## Verification notes
Fetched directly from towardsdatascience.com (allowlisted). The three-noise-
source taxonomy, the stated Levenshtein/SymSpell failure modes, the cosine
similarity figures (>0.95 typo pairs, 0.86–0.97 OCR pairs, 0.858 vs. 0.787
chunk-granularity comparison), and the two-path remediation strategy were
all traced directly to the article's text as the author's own stated
measurements and recommendations, not third-party citations requiring
separate corroboration.

## Updates
None yet.

## Related entries
[2026-shi-nlp-ladder-before-rag](2026-shi-nlp-ladder-before-rag.md) — same author, same "deterministic step before reaching for the LLM" theme applied to retrieval matching rather than the overall NLP pipeline.
[2026-shi-row-level-chunks-rag](2026-shi-row-level-chunks-rag.md) — same author, a related chunking-granularity RAG pattern.
