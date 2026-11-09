---
slug: 2026-althoff-ai-scientific-discovery-claude-usage
title: "AI for Scientific Discovery: How Researchers Use Claude"
status: accepted
domains: [social_science, ai_engineering]
source_type: primary
source_url: https://www.anthropic.com/research/how-researchers-use-claude
canonical_ids: []
publisher_or_author: "Lukas Althoff, Johannes Hermle, Ben Jones et al. — The Anthropic Institute"
published: 2026-11-05
captured: 2026-11-09
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  High on economic growth and productivity (lens 1): a usage-data study
  mapping real Claude sessions to a capability measure across scientific
  fields and tasks, producing quantified, if illustrative, acceleration
  scenarios for research productivity that a reader could cite directly.
  Medium on ai_engineering (lens 8): the capability-task correlation and
  the gap between task importance and current AI usage are useful context
  for where agentic research tools are and are not yet trustworthy, but
  the piece reports usage patterns rather than a transferable engineering
  technique. First-party Anthropic source — scored on its own merits per
  the vendor caveat recorded in profiles/social_science/sources.md.
---

# AI for Scientific Discovery: How Researchers Use Claude

## Summary

A technical report from the Anthropic Institute's economics team analyzing how scientists use Claude for research. The team classified 207,049 consumer-plan sessions (2 August–30 September 2026) — 128,914 from Claude (Chat and Cowork) and 78,135 from Claude Code, plus a supplemental Claude Science sample — against the SciNet taxonomy (7,262 tasks, 34 fields, 318 subfields) using a language-model classifier, reporting results only in aggregate for cells meeting a minimum account threshold.

**Field skew.** Usage concentrates in formal sciences relative to researcher headcount: computer science is 11.9% of Claude sessions and 32.7% of Claude Code sessions against roughly 4.3% of the world's researchers; AI/ML is 5.0%/15.2% of sessions against about 1.2% of researchers. Log-log correlation between a field's researcher share and its session share is 0.79 (Claude) and 0.62 (Claude Code).

**Task mismatch with importance.** Data analysis (33.7%/48.1% of sessions) and writing (32.0%/17.6%) dominate usage; data gathering (11.5%/11.9%) and ideation (4.2%/2.1%) lag well behind their share of researcher time (28.6% and 7.1% respectively) — and behind a separate survey's ranking of ideation as most important for landing an important result (35.6/100 points, versus 23.6 for data gathering).

**Usage tracks a capability measure.** Tasks in the top 20% of a theoretical AI-capability measure see 2.1x (Claude) to 3.9x (Claude Code) the usage their researcher-time share would predict; bottom-20% tasks, mostly physical, see very little. Capability correlates with RL-suitability (0.78) and cognitive work (0.69), and anti-correlates with physical work (-0.57), regulatory restriction (-0.38), and interpersonal work (-0.31).

**Claude Science differs from general Claude.** On the same biology/biomedical fields, Claude Science sessions report higher estimated researcher skill requirement (>80% doctoral-level vs. 48% on general Claude), more autonomy (73.3% vs. 23.7%, with the authors flagging user self-selection as a likely partial explanation), and more time saved per session (10.3 hours of estimated human-equivalent time vs. 4.9).

**Illustrative acceleration scenarios** (explicitly not forecasts; $30/AI-hour vs. $95/researcher-hour, 0.2 AI-hours per saved researcher-hour): at current capability, implied field-level research acceleration ranges from about 1.35x (arts) to about 2x (statistics, computer science); automating all non-physical steps pushes statistics, computer science, and several social sciences to roughly 15-16x, while biology, chemistry, materials science, and biomedical sciences cap near 3-4x because physical experimentation remains roughly 40% of researcher time.

A companion 528-scientist survey (recruited from Anthropic's AI for Science grant applicants, so likely heavier-than-typical AI users) found 38% already rate AI at top-researcher level on data analysis, rising to an expected 94% by 2030; roughly 40% expect AI to run full research projects autonomously by 2030 (64% by 2035; 16% say never).

## Why it matters

The capability-task correlation and the task/importance mismatch give a concrete, falsifiable structure to the "AI productivity paradox" debate already in this library (cf. the ATLAS and Imas entries): usage is not randomly distributed, it tracks a measurable capability score, and it is currently concentrated away from the tasks scientists themselves rate as most important (ideation, data gathering). That is a specific, citable mechanism for why realised research acceleration could lag capability-based projections even as adoption headlines rise — directly usable in growth/productivity arguments about AI and R&D (lens 1).

For ai_engineering, the finding that current agentic usage clusters in exactly the task categories the capability measure rates highest (and avoids the lowest) is a data point for where AI-assisted research tooling is being trusted today, and a caution against over-indexing coding-agent and data-analysis benchmarks as proxies for full research-automation readiness (lens 8) — relevant to anyone building agentic research or policy-simulation pipelines.

## Verification notes

Fetched directly from www.anthropic.com/research/how-researchers-use-claude and read in full; every figure and claim above is traced to the fetched text (session counts, percentages, correlations, survey results, scenario multipliers). Publication date (5 November 2026) and author list are as stated on the page/citation. Load-bearing claims — the session counts, the capability-usage correlations, and the scenario assumptions — are as reported by the source; no independent corroboration against a third-party replication was attempted (none exists yet for a first-party usage dataset of this kind).

**Vendor caveat — load-bearing.** This is Anthropic measuring usage of its own products. The survey sample is explicitly drawn from AI for Science grant applicants and flagged by the authors as likely heavier AI users than typical scientists; the usage data describes Claude's user base first, and the economy of science only by inference. The acceleration scenarios are explicitly illustrative, not forecasts, and exclude field-level constraints (shared facilities, equipment costs, idea quality).

## Updates

None yet.

## Related entries

- [2026-google-atlas-gemini-economy-mapping](2026-google-atlas-gemini-economy-mapping.md) — the closest methodological sibling: another first-party usage-to-task mapping (Gemini vs. Claude), same breadth-without-depth structure, same vendor caveat.
- [2026-imas-ai-productivity-paradox](2026-imas-ai-productivity-paradox.md) — the productivity-paradox synthesis this paper's capability-usage gap helps substantiate with a research-specific mechanism.
- [2026-smith-little-scientist-llm-agent-discovery](2026-smith-little-scientist-llm-agent-discovery.md) — an agent-driven scientific-discovery system; this paper's low current usage on ideation/data-gathering tasks is a relevant caution on how close such agents are to full autonomy in practice.
