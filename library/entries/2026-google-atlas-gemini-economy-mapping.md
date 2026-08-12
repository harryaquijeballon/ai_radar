---
slug: 2026-google-atlas-gemini-economy-mapping
title: "Google's AI & Economy ATLAS v1.0: Mapping Gemini Usage in the Economy"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://ai.google/static/documents/GoogleATLASv1.pdf
canonical_ids: []
publisher_or_author: "Zanna Iscenko, Scott Strand, Alex Imas, Julian Jacobs, Juan Mateos-Garcia, James Manyika and others — Google and Google DeepMind"
published: 2026-07-23
captured: 2026-07-31
relevance:
  social_science: high
  ai_engineering: n/a
verification: verified
rationale: >-
  High on digital technologies and connectivity, economic development, and
  economic growth and productivity (lenses 3, 2, 1): a 15-million-interaction
  usage dataset mapped to BLS occupations, O*NET tasks and American Time Use
  Survey activities across 150 countries and 140 languages, producing
  specific elasticities and quantified adoption structure of exactly the kind
  connectivity and digital-economy analysis can cite and build on. Retained
  with an explicit first-party caveat: Google measuring usage of Google's own
  products.
---

# Google's AI & Economy ATLAS v1.0: Mapping Gemini Usage in the Economy

## Summary

An economic research initiative built on "15 million de-identified interactions across the Gemini App, Google AI Mode, and the Gemini API," clustered and mapped onto established labour frameworks — BLS occupational codes, O*NET tasks — and, for non-work use, American Time Use Survey activities. Coverage spans "over 800 occupations, 4000 work tasks, 300 household activities, 150 countries, and 140 languages." The framing is explicitly a new Solow paradox: "AI appears to be everywhere, yet its impact remains hard to discern in many traditional measures of employment, productivity, and growth."

Ten findings are reported. The load-bearing ones:

**Breadth without depth.** Workplace adoption spans "over 68% of all occupations that collectively represent just above 88% of total US employment," yet "AI is used for only 21% of total tasks in the median occupation with any AI use." Only 3% of occupations show AI use across more than 75% of their tasks.

**Assistive, not automating.** Non-routine cognitive tasks are about 35% of professional tasks economy-wide but "almost 65% of work-related AI interactions" in the data. Within that category, "attempts to automate tasks end-to-end represent less than 10% of AI conversations." Usage centres on partial drafting, review and refinement, ideation, and information retrieval.

**Not only white-collar.** Nearly a third of heavily physical occupations show no observed use, but manual and technical trades do use AI as a "hands-on collaborator for diagnostics, troubleshooting, and real-time learning," with multimodal usage among automotive technicians and industrial mechanics running "more than 2 times higher than the overall work baseline."

**Steep income gradient.** "A 1% increase in an occupation's median earnings is associated with a more than 2.5% increase in AI usage intensity," persisting after controlling for educational attainment. Conversation-weighted median salary is around $83,000, roughly $20,000 above the employment-weighted national median. Complicating this: tasks requiring lower-to-middle expertise see relatively *higher* usage than the highest-expertise tasks, even though high-earning workers adopt at the highest rates.

**Household value invisible to national accounts.** "Over 86% of interactions with conversational AI happen outside of work." High-friction bureaucratic activities are heavily over-represented relative to time actually spent on them — government services and civic obligations "by a factor of almost twenty" — and "nearly half of all medical, legal, financial, and government AI consultations take place outside 9-to-5 business hours." The report offers a conditional valuation: *if* household time savings averaged 30 minutes per week, US unpaid productivity gains "could be worth approximately $100 billion" (a stated hypothetical, not a measurement — see Verification notes).

**Global diffusion tracks wealth, with exceptions.** "A 1% increase in GDP per capita associated with a 0.9% increase in usage." The lowest-adopting quintile of countries accounts for only 2% of conversations. However, "multiple middle-income nations across Latin America and the Middle East buck this trend, adopting AI at rates comparable to Western Europe," and the differences "are not easily explained by any single factor, such as internet access and interest in AI topics."

**Language and modality.** English is "only about a third of global conversations," and work and non-work activity show nearly identical language distributions — no sign of users switching to English for complex professional tasks. Users in non-OECD countries "generate images and videos for work at roughly twice the rate of those in advanced economies."

The authors state the data does not support several common claims: imminent mass automation of white-collar work, AI's irrelevance to blue-collar work, automation as AI's primary use, or the framing of global AI leadership in adoption as a US-China contest.

## Why it matters

For connectivity and digital-economy analysis this is among the most directly usable datasets to appear: adoption measured by realised usage rather than survey self-report, resolved to country, language, occupation and task. The GDP-per-capita elasticity of 0.9 and the finding that the lowest-adopting quintile accounts for just 2% of conversations give a quantified handle on the AI dimension of the digital divide. The middle-income exceptions in Latin America and the Middle East — adopting at Western European rates, unexplained by internet access — is a specific, investigable anomaly rather than a general observation.

The language result cuts directly against a common assumption in digital-inclusion argument: users are *not* abandoning native languages for professional work, and non-OECD users lean harder on multimodal input. Both point to where product and policy attention would actually matter.

For productivity work, the breadth-without-depth structure is the most useful correction available to the current debate. 88% of employment touched, 21% of tasks in the median occupation, under 10% end-to-end automation attempts — that is a concrete mechanism for why aggregate productivity statistics stay flat while adoption headlines rise, and it can be set directly against the flat-TFP measurements and the task-reallocation experimental evidence already in this library.

## Verification notes

The publisher URL supplied by the user carried Google Analytics tracking parameters; the canonical URL above is the normalised form. The PDF exceeded the fetch tool's size limit (13 MB), so it was downloaded directly and its full text extracted locally (100 pages) and read. Every quoted sentence and every figure above traces verbatim to the paper's abstract and executive summary. Title, full author list, both organisations, and the stated date of 23 July 2026 are confirmed from the document's own title page.

**First-party caveat — load-bearing.** This is Google measuring usage of Google's products and drawing economy-wide inferences from it. Gemini users are not a random sample of workers, households, or countries, so every distributional result carries an unquantified selection effect: the income gradient, the country rankings, and the occupation coverage all describe *Gemini's* user base first and the economy only by inference. The paper does not report a correction for this. External review by Diane Coyle (Cambridge) and David Autor (MIT) is credited as "contributions, guidance, and review" — a meaningful credibility signal, but not peer review.

**The $100 billion figure is conditional and should not be quoted as a finding.** The paper's own construction is "if these household time-savings would average out to just 30 minutes per week" — the 30 minutes is an assumption, not a measurement. ATLAS records what people ask AI to do, not whether time was saved.

Limitations the authors state directly: ATLAS "does not capture the ultimate productive output the user is working toward or how effective their interaction was; it only captures what people are directly doing with AI." It excludes Google Workspace, Google Translate, AI Overviews, Gemini Enterprise, and agentic coding — a large share of economically relevant AI use. The authors also state that ATLAS v1.0 cannot speak to whether AI deepens the global digital divide or dampens entry-level hiring, and that their intent and expertise classifiers "leave scope for greater sophistication."

Not verified: sections 2–6 (data and methodology, and the detailed results chapters) were not read in full, so the classification methodology, the privacy-preserving procedures, and the derivation of the reported elasticities are not independently traced. All figures above are as the executive summary states them.

## Updates

None yet.

## Related entries

- [2026-borri-tsyvinski-liu-ai-premium](2026-borri-tsyvinski-liu-ai-premium.md) — the closest methodological sibling: also realised-usage data rather than surveys, but priced through stock returns via OpenRouter tokens rather than mapped to occupations. Read together for two independent usage-based measures of AI exposure.
- [2026-imas-ai-productivity-paradox](2026-imas-ai-productivity-paradox.md) — same Solow-paradox framing, and Alex Imas is a co-author of this paper; ATLAS supplies the usage-structure mechanism his synthesis argues for.
- [2026-pethokoukis-ai-capability-business-payoff](2026-pethokoukis-ai-capability-business-payoff.md) — the flat aggregate TFP that breadth-without-depth helps explain.
- [2026-marsal-perkowski-task-based-genai-central-bank](2026-marsal-perkowski-task-based-genai-central-bank.md) — task-level experimental evidence complementing ATLAS's task-level observational mapping.
- [2025-oecd-ai-global-productivity-divide](2025-oecd-ai-global-productivity-divide.md) — cross-country productivity divide against which ATLAS's GDP-per-capita adoption elasticity can be read.
