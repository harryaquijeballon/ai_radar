---
slug: 2026-ibm-cuga-cross-lingual-retrieval-failure
title: "An Indic Voice Agent with CUGA"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://huggingface.co/blog/ibm-research/an-indic-voice-agent-with-cuga
canonical_ids: []
publisher_or_author: "IBM Research"
published: 2026-11-25
captured: 2026-11-25
relevance:
  ai_engineering: medium
  social_science: n/a
verification: verified
rationale: >-
  Lens 2 (harness and context engineering) and lens 3 (tool use/RAG
  grounding): a concrete, specific failure mode in a real build — an
  English-only embedding model silently produced poor retrieval vectors
  for Hindi/Tamil queries, causing the agent to wrongly conclude its
  document didn't cover the topic with no error raised — with a stated
  fix (switch to a multilingual embedding model) and a transferable
  testing practice (probe retrieval with a non-English query before
  prompt-tuning). No quantified evaluation accompanies it, so it stays
  medium rather than high.
---

# An Indic Voice Agent with CUGA

## Summary

IBM Research built a voice agent for farmers: a spoken question in an Indic language (e.g., Hindi, Tamil) is transcribed, used to search a 154-page English agricultural handbook, and answered aloud in the same language, with source pages shown for verification; off-topic questions are redirected. The agent is built on CUGA (ConfigUrable Generalist Agent), IBM's open-source (Apache 2.0) agent harness, treated as a text-in/text-out component with speech-to-text and text-to-speech layered around it, so the team could build and test with plain text first and swap speech providers independently. The authors report one specific, previously silent failure mode: CUGA's default English-only embedding model produced poor retrieval vectors for non-English queries, and the agent then wrongly concluded the handbook didn't cover the topic — with no error surfaced. Switching to a multilingual embedding model fixed this, letting a single English document serve multiple languages. They also note writing-for-speech considerations (avoiding markdown/citation tags that read badly aloud) and a cheap, low-latency guardrail pattern for off-topic detection that avoids a second LLM call.

## Why it matters

A specific, reproducible RAG/harness failure mode — silent retrieval failure from an embedding-model/query-language mismatch, misread by the agent as "topic not covered" rather than "retrieval broken" — with a named fix and a concrete testing practice (probe with a non-English query before tuning prompts) that generalizes beyond this one build to any cross-lingual or multilingual RAG system.

## Verification notes

Fetched directly; the post itself states the architecture, the failure mode, and the fix. No quantified evaluation (retrieval accuracy, latency) accompanies the claims — the evidence is a single qualitative demonstration, which is why this is scored medium rather than high.

## Updates

None yet.

## Related entries

None yet.
