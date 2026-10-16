---
slug: 2026-massenkoff-economic-index-cadences
title: "Anthropic Economic Index report: Cadences"
status: accepted
domains: [social_science]
source_type: primary
source_url: https://www.anthropic.com/research/economic-index-june-2026-report
canonical_ids: []
publisher_or_author: "Maxim Massenkoff, Eva Lyubich, Szymon Sacher, Zoe Hitzig, Shaoyi Zhang, Ryan Heller, Peter McCrory — Anthropic Economic Index"
published: 2026-06-26
captured: 2026-10-16
relevance:
  social_science: high
  ai_engineering: low
verification: partial
rationale: >-
  Social science lenses 1 and 3: the current release of the Anthropic
  Economic Index, which maps AI usage to occupations, tasks and wages, here
  with daily telemetry and a first survey of about 9,700 users linked to
  their own usage. That gives citable adoption and expectation measures for
  digital-economy analysis, with clearly stated limitations. Backfilled at
  the user's request; this entry represents the Index series, whose earlier
  releases are not yet in the library.
---

# Anthropic Economic Index report: Cadences

## Summary

The June 2026 Economic Index report, the latest in a recurring series measuring how Claude is used across the economy. Two methodological changes: a continuous daily sample of conversations (earlier reports used seven-day samples), and the new Anthropic Economic Index Survey (launched April 2026), whose roughly 9,700 respondents in the final sample are linked to their own usage.

**Findings:**
- **Rhythm of use:** tax-related clusters were eight times as common on 14 April as on an average May day, and work tasks on nights and weekends skew toward higher-wage occupations.
- **Artifacts:** 93% of conversations produced an artifact.
- **Job-loss expectations:** 10% of respondents rated losing their own job as likely or very likely; of those, 38% attributed this to AI, which the report treats as an upper bound.
- **Reported gains:** speed (86%), scope (82%), quality (69%) and cost savings (27%).
- **Learning and skills:** 68% report learning more with AI, and 57% say AI has made their skills more valuable.

**Stated limitations:**
- The survey is not representative of the general population, and infrequent users were filtered out.
- Respondents skew toward knowledge workers in stable employment.
- Exposure answers were binned, which biases slope estimates toward zero.
- Occupation mapping is noisy, and correlations may reflect selection.

## Why it matters

The Economic Index is the most detailed public, recurring measure of where generative AI is actually used, by task and occupation. It is a primary input for adoption and exposure analysis in digital-economy and labour research. This release adds two things researchers can use: telemetry fine-grained enough for timing analysis, and a survey linked to usage that connects expectations (job loss, skill value) to observed behaviour. Every figure describes Claude's user base, and the survey is explicitly non-representative. Use it for within-user and cross-occupation comparisons, not population rates. Publisher caveat: these are first-party measures from a vendor with a stake in how AI's economic role is perceived.

## Verification notes

The page was fetched on 2026-10-16 and its raw text checked string by string with a deterministic script for 9,700, 10%, 38%, 86%, 68%, 57%, 93%, "eight times", "not representative", the author list and the stated date ("Jun 26, 2026"; the page metadata `datePublished` agrees). The 82%, 69% and 27% figures come from the same list of gains on the page. The report and appendix PDFs were not read; the summary relies on the web version. The page links no dataset. The series' public Hugging Face dataset (Anthropic/EconomicIndex) appeared in search results but was not checked against this release, so it is not recorded as a canonical id. Partial: claims trace to the source; first-party measures cannot be independently corroborated.

## Updates

- None yet.

## Related entries

[2026-huang-81k-interviews-what-people-want-from-ai](2026-huang-81k-interviews-what-people-want-from-ai.md) — earlier open-ended interview study of Claude users by the same economics team.
[2026-korinek-economic-scenarios-transformative-ai](2026-korinek-economic-scenarios-transformative-ai.md) — shares authors (Sacher, McCrory); its scenario survey is a separate instrument.
[2026-epoch-near-daily-ai-use-growth](2026-epoch-near-daily-ai-use-growth.md) — independent US adoption measure to set against this vendor-side usage data.
