---
slug: 2026-wilmers-working-with-ai-enterprise-adoption
title: "Working with AI"
status: accepted
domains: [social_science, ai_engineering]
source_type: primary
source_url: https://www.anthropic.com/research/working-with-ai
canonical_ids: []
publisher_or_author: "Nathan Wilmers, Maxim Massenkoff, Peter McCrory — The Anthropic Institute"
published: 2026-11-23
captured: 2026-11-24
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  Social science lens 1 (growth/productivity) and lens 4 (labour-market
  effects): 66 structured interviews across 58 US firms quantify where AI
  adoption creates value, how hiring and contracting change, and what
  bottlenecks slow adoption. AI-engineering lens 7 (AI-assisted development)
  at medium: the review-bottleneck and "zombie automation" findings are
  useful adoption-friction context but not a specific reusable engineering
  technique. Vendor source — interviewees are all Anthropic enterprise
  customers, a non-random, non-representative sample by the authors' own
  statement; read as a qualitative field study, not a population estimate.
---

# Working with AI

## Summary

A technical report from The Anthropic Institute (Nathan Wilmers, Maxim Massenkoff, Peter McCrory) based on 66 interviews across 58 US companies — all Anthropic enterprise customers actively adopting AI, selected for variation in industry, size, and usage rather than randomly or representatively. The report maps nearly 300 AI applications discussed across the interviews and identifies three adoption strategies: top-down automation, bottom-up experimentation, and broader reorganization around AI.

Headline figures as stated in the report: interviewees described about 100-140 pieces of software built with AI (the report gives both figures in different places), of which roughly 80% automated manual work and 20% replaced existing software. Most value came from increasing output rather than cutting costs — about half of output gains from accelerating existing work, half from quality improvements or new products/services — and about one-tenth of use cases delivered value directly to employees (more enjoyable or less work). On employment: five companies described pushing out employees who would not adopt AI, but only two saw AI fully eliminate a position; ten companies reported hiring more because of AI (mainly for implementation/IT support), while roughly two-thirds reported reduced hiring, about a third of that reduction via unfilled attrition and most via forgone hires. Nine companies cut contracted staff (software development, customer service, legal, back-office), several already offshored — one finance company downsized over 100 offshore contractors — and one company expected to cut reviewer hiring by more than 90% after deploying a document-review agent. Six AI-native startups estimated needing four times as many employees without AI; one startup COO reported roughly 90% of operating budget going to AI tokens versus 10% to headcount. The most-cited bottlenecks (Figure 4) were reviewing AI output, uneven adoption across teams, slower non-coding functions failing to keep pace with faster coding, and missing context/infrastructure; customer skepticism and regulation were rarely cited.

The authors characterize top-down automation as prone to expert resistance, surveillance fears, and "zombie" systems that go stale as models improve; bottom-up experimentation as producing real but localized gains with friction from uneven adoption; and reorganization — broadening roles, redeploying staff to tasks AI can't yet do, building shared non-technical-builder infrastructure, and widening data access — as yielding the highest-value deployments.

## Why it matters

For social-science readers: a rare interview-based (not survey-elicited) look inside firms adopting AI at scale, giving qualitative but concrete evidence for the displacement-vs-reorganization debate — notably, that domestic layoffs attributable to AI automation are rare in this sample, while reduced hiring and cuts to offshore contractors are the more common channel, which the authors flag as a possible early-warning signal for the international business-services industry.

For AI-engineering readers: a field-level account of where organizational adoption of AI stalls in practice — human review capacity, uneven team-level adoption, and mismatched speeds between AI-accelerated and un-accelerated functions — useful context for anyone designing how agentic tools get rolled out inside an organization, though the report offers no specific technique or architecture of its own.

## Verification notes

Fetched and read directly (not abstract-only); figures above are as stated in the report, including author list, institutional citation (The Anthropic Institute), and publication date (23 November 2026). Not independently corroborated against a second source. **Sampling caveat (load-bearing, stated by the authors):** all 58 companies are Anthropic enterprise customers, a non-random and explicitly non-representative sample; value assessments are mostly qualitative and self-reported rather than from controlled (e.g. A/B) comparisons. The report's own internal figures are inconsistent in one place (100 vs. 140 pieces of AI-built software cited in different sections) — noted here rather than resolved, since both figures are as the source states them.

## Updates

None yet.

## Related entries

- [2026-wilmers-anthropic-employment-change](2026-wilmers-anthropic-employment-change.md) — the same lead author's earlier single-firm (Anthropic-internal) report on AI-driven hiring and workflow change; this entry extends the inquiry to a 58-firm interview sample.
- [2026-sacher-ai-expectations-gap](2026-sacher-ai-expectations-gap.md) — companion survey-based report on AI economic expectations.
