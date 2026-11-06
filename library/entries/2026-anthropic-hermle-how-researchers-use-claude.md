---
slug: 2026-anthropic-hermle-how-researchers-use-claude
title: "AI for Scientific Discovery: How Researchers Use Claude"
status: accepted
domains: [social_science, ai_engineering]
source_type: primary
source_url: https://www.anthropic.com/research/how-researchers-use-claude
canonical_ids: []
publisher_or_author: "Johannes Hermle, Ben Jones, Lukas Althoff et al. — Anthropic Economics Team / The Anthropic Institute"
published: 2026-11-05
captured: 2026-11-06
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  First-party, methodologically detailed usage study (207,049 sessions,
  SciNet task taxonomy, a 528-scientist survey, and capability-vs-use
  scenarios) directly on social_science lens 6 (AI applied to research,
  with explicit attention to adopter self-selection and other limits) and
  lens 1 (acceleration scenarios tied to stated cost assumptions); medium
  for ai_engineering as real-world evidence of how researchers actually use
  agentic tools (Claude Code vs. chat) rather than a builder-facing pattern.
---

# AI for Scientific Discovery: How Researchers Use Claude

## Summary

Anthropic's Economics team analyzed 207,049 privacy-preserving research
sessions on consumer Claude plans (128,914 Claude Chat/Cowork sessions and
78,135 Claude Code sessions) from 2 August to 30 September 2026, plus a
supplemental Claude Science sample, classifying each into the SciNet
taxonomy (34 fields, 318 subfields, 7,262 tasks) via an LLM classifier.
Computer science accounted for 11.9% of Claude sessions and 32.7% of Claude
Code sessions despite ~4.3% of researchers globally; AI/ML was 5.0% and
15.2% of sessions respectively versus 1.2% of researchers. By task, data
analysis was 33.7% of Claude sessions and 48.1% of Claude Code sessions
(vs. 27.6% of researcher time); writing was 32.0% of Claude sessions (vs.
16.0% of researcher time); data gathering and ideation were under-used on
Claude relative to researcher time (11.5% vs. 28.6%, and 4.2% vs. 7.1%
respectively).

A separate "theoretical AI capability" score (pairwise LLM comparison of
task steps, scored with a Bradley–Terry model) correlates with usage: tasks
in the top 20% of capability scored a 2.1–3.9x use ratio versus researcher
time share, bottom-20% tasks near 0.2x. A 528-scientist survey (recruited
from Anthropic grant-program applicants, mostly life/health sciences) found
38% already think AI matches top researchers on data analysis, rising to
94% expected by 2030; illustrative acceleration scenarios built on a simple
ideas-production model (assumed costs: $30/AI-agent-hour, $95/researcher
hour, 0.2 AI hours substituting a researcher hour) estimate 1.35–2.02x
acceleration under current capabilities, rising to 6–8x in computer
science, statistics, and economics if 75% of non-physical steps were
automated.

## Why it matters

Gives social-science and policy researchers a quantified, task-level map of
where AI usage already outpaces or lags researcher time allocation — e.g.,
AI is comparatively under-used for ideation/data-gathering relative to its
stated importance, which is itself informative for the "where will AI
actually bite" debate (lenses 1, 6). The acceleration scenarios, while
explicitly illustrative, give a transparent cost/substitution-rate model a
researcher could adapt. For ai_engineering, the Claude-vs-Claude-Code split
(data analysis dominates Claude Code; higher autonomy and doctoral-level
content on Claude Science) is real-world evidence on how domain-specialized
agent products are actually used, relevant to the policy-simulation
interest in validated, task-appropriate automation.

## Verification notes

Fetched the primary page directly; methodology, sample sizes, dates, and
all numeric findings above are stated on the page itself and traced
directly to it. The authors themselves flag several limits, all preserved
here: survey respondents are likely heavier AI users than typical
scientists; acceleration scenarios are "illustrative, not forecasts" and
omit facility/machinery constraints and idea quality; Claude Science
differences may partly reflect adopter self-selection; subfield estimates
are noisier for low-volume subfields; ideation may be undercounted because
it is embedded in other tasks.

**Vendor-source caveat** (per `profiles/social_science/sources.md`): this
is an Anthropic first-party report using only Anthropic product data and a
survey drawn from Anthropic's own grant-program applicants. Usage patterns
describe Claude's user base first, and the broader population of
researchers and AI tools only by inference; the report does not itself
discuss this limitation.

## Updates

None yet.

## Related entries

Related to [2026-google-atlas-gemini-economy-mapping](2026-google-atlas-gemini-economy-mapping.md)
(same genre of first-party usage-mapping report, different vendor and
population — occupations/tasks economy-wide vs. researchers specifically).
None supersede or contradict.
