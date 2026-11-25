---
slug: 2026-chen-worth-the-wait-chatbot-latency-bias
title: "Worth the Wait? How Response Time and Streaming Shape Judgments of Generative AI Answers and Chatbot Engagement"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.33050
canonical_ids: ["arxiv:2611.33050"]
publisher_or_author: "Zihan Chen, Di Zhu, Lei Nico Zheng"
published: 2026-11-25
captured: 2026-11-25
relevance:
  social_science: medium
  ai_engineering: high
verification: verified
rationale: >-
  AI-engineering lens 4 (evaluation, validation and deterministic
  guardrails): a large-sample, causally identified finding that delivery
  speed and streaming — not answer content — bias blind preference votes,
  a direct validity threat to the arena-style human/LLM-preference
  leaderboards widely used to evaluate models. Social-science lens 5
  (causal inference and empirical methods): a natural-experiment design
  (congestion-induced latency variation) applied to a question about
  AI-mediated judgment, though the substantive topic is product UX rather
  than economics.
---

# Worth the Wait? How Response Time and Streaming Shape Judgments of Generative AI Answers and Chatbot Engagement

## Summary

The authors study whether the speed and manner (streamed vs. shown-at-once) of a generative-AI chatbot's reply changes how people judge it, across three natural experiments. In a French government chatbot arena, repeated prompts were answered either by a freshly streamed reply or by instantly replaying an earlier stored answer; replays were judged the losing answer far more often in blind votes, lowering an answer's chance of winning by 25.8 percentage points, and were rated less complete, more superficial, and more often incorrect even though the underlying content was identical. Across 324,029 Chatbot Arena conversations, provider congestion that slowed streamed answers produced no detectable net voting advantage for speed, but a slower first exchange made users less likely to ask a follow-up question. Across 4,378,514 WildChat ChatGPT replies, congestion-induced slowdowns similarly reduced the likelihood that users continued the conversation.

## Why it matters

For AI-engineering readers: this is direct evidence that preference-vote-based evaluation — the mechanism behind widely used arena-style leaderboards — is sensitive to how an answer is delivered (streamed vs. replayed, fast vs. slow), independent of its content. A caching strategy that replays a stored answer to save cost or latency will be penalized in blind preference votes even when the content is as good or better, and any team using human- or LLM-judge preference votes to evaluate models or features should treat delivery-speed/streaming as a confound to control for, not ignore.

For social-science readers: a methodologically strong example of using congestion-induced variation as a natural experiment to causally identify a user-judgment effect at very large scale (millions of conversations) — relevant to anyone using LLMs or chatbot logs as a measurement instrument, since it shows user "preference" signals can be contaminated by infrastructure-level factors unrelated to content quality.

## Verification notes

Fetched directly from arXiv; abstract and submission history (v1, 24 November 2026, appearing in the 25 November econ.GN and cs.CL listings) confirmed on the page. Load-bearing figures (25.8 percentage-point swing; sample sizes of 324,029 and 4,378,514 conversations) are as stated in the abstract. The three underlying datasets and the precise congestion-based identification strategy for studies 2 and 3 were not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

None yet.
