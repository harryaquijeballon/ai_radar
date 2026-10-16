---
slug: 2026-huang-81k-interviews-what-people-want-from-ai
title: "What 81,000 people want from AI"
status: accepted
domains: [social_science]
source_type: primary
source_url: https://www.anthropic.com/features/81k-interviews
canonical_ids: ["anthropic.com/research/81k-economics"]
publisher_or_author: "Saffron Huang et al. — Anthropic; economics follow-up by Maxim Massenkoff, Saffron Huang"
published: 2026
captured: 2026-10-16
relevance:
  social_science: high
  ai_engineering: low
verification: partial
rationale: >-
  Social science lens 6: AI-conducted qualitative interviewing at very large
  scale (80,508 people, 159 countries, 70 languages), a concrete and
  inspectable research instrument with clear validity caveats. Also lens 1,
  through the economics follow-up's measured link between occupational AI
  exposure and perceived job threat, and lens 8 (what people want from AI
  and what they fear). Backfilled at the user's request.
---

# What 81,000 people want from AI

## Summary

In December 2025, every Claude.ai account holder was invited to a conversational interview run by "Anthropic Interviewer", a version of Claude prompted to conduct interviews. 80,508 people in 159 countries and 70 languages took part. Claude-based classifiers coded each interview. One study, two posts:

**Main post (visions and concerns).**
- Top hopes for AI: professional excellence (18.8%), personal transformation (13.7%), life management (13.5%) and time freedom (11.1%).
- 81% said AI had already taken a step toward their vision; productivity was the largest category of experienced progress (32.0%).
- Top concerns: unreliability (26.7%), jobs and the economy (22.3%), autonomy and agency (21.9%), and cognitive atrophy (16.3%). Concern about jobs and the economy was the strongest predictor of overall sentiment.
- On average, respondents voiced 2.3 distinct concerns.
- 67% expressed net positive sentiment. A dated correction (19 March 2026) replaced the earlier wording "67% of people view AI positively".

**Economics follow-up** ("What 81,000 people told us about the economics of AI", 22 April 2026):
- Perceived job threat rises with observed occupational AI exposure: "For every 10-percentage-point increase in exposure, perceived job threat increased by 1.3 percentage points".
- Workers in the top exposure quartile mention job worry three times as often as those in the bottom quartile.
- Self-rated productivity averaged 5.1 on a 1–7 scale. Scope expansion (48%) was cited more often than speed (40%).
- 60% of early-career workers said they personally benefited, against 80% of senior professionals.

**Caveats the authors state:** participants are active, self-selected Claude users. The interview asked for positive visions before concerns, and the authors note that both factors may bias results. Occupation and career stage were inferred by Claude from context, not asked directly. Enterprise users were excluded, and findings should be confirmed with structured surveys.

## Why it matters

The method is the main contribution for social scientists. AI-run, adaptive qualitative interviews at a scale and language coverage no human team could field show what "LLMs as research instruments" looks like in practice. The study also shows the validity questions such an instrument has to answer: a self-selected sample of one product's users, Claude-coded measures, and occupation inferred rather than asked. The exposure-to-job-threat gradient is a citable descriptive result linking perceived risk to measured exposure. It should not be read as population evidence. Publisher caveat: the sample is the publisher's own user base, so attitudes describe Claude users first and the wider public only by inference.

## Verification notes

Both pages were fetched on 2026-10-16 and their raw text checked string by string with a deterministic script. Main post: 80,508, 159, "70 languages", 81%, 67% and the dated 19 March correction, 2.3, and the caveats about active users and question order; the chart values were paired with their labels from the page's chart markup. Follow-up: the "1.3 percentage points" sentence, "three times", 5.1, 48%/40% and 60%/80%. The publication date of the main post is not stated beyond the year (BibTeX `year = {2026}`); an automated summary's "18 March" could not be confirmed, so only the year is recorded. The methods appendix PDF could not be machine-read, so classifier validation (any agreement rates with human coders) was not checked. That is the main reason verification is partial. Upgrade path: read the appendix and record the classifier validation it reports.

## Updates

- None yet.

## Related entries

[2026-massenkoff-economic-index-cadences](2026-massenkoff-economic-index-cadences.md) — same economics team; links a structured survey of Claude users to their usage, complementing these open-ended interviews.
