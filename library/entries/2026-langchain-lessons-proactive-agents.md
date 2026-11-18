---
slug: 2026-langchain-lessons-proactive-agents
title: "What We've Learned Building Proactive Agents"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://www.langchain.com/blog/what-weve-learned-building-proactive-agents
canonical_ids: []
publisher_or_author: "LangChain"
published: 2026-11-17
captured: 2026-11-18
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Medium on lens 1 (agent architecture) and lens 2 (harness/context
  engineering): concrete, named patterns for proactive-agent memory and
  check-in design, but the evidence is anecdotal, drawn only from
  LangChain's own two internal agents, with no controlled comparison —
  discounted per the profile's framework-vendor note.
---

# What We've Learned Building Proactive Agents

## Summary

LangChain describes lessons from building two internal proactive agents
(a "GTM Agent" and "Robin"). Proactive agents act on three trigger types:
real-world events, developer-set schedules, and schedules the agent sets
for itself — the post states that over 70% of runs on its Managed Deep
Agents product now come from schedules (unverified beyond the post's own
claim). Memory is framed as built from seed data (past), feedback (present),
and outcomes (future), with three recurring maintenance problems: deciding
what's worth saving (salience), removing stale information (expiry), and
merging rather than duplicating facts — the post suggests a scheduled
"dreaming" job that reviews recent traces and updates memory accordingly.
Because check-ins cost human attention, the post frames agent proactivity as
an action-matrix problem (acting on what matters and staying quiet on what
doesn't, against the errors of noise and missed opportunities), and argues
that review needs to be fast to feed corrections back into memory — citing a
custom review UI built for GTM Agent after Slack-based draft review proved
slow, and Robin's one-line-summary-plus-claim-button review requests.

## Why it matters

Gives a builder designing a proactive (schedule- or event-triggered) agent a
named decomposition of the memory-maintenance problem (salience, expiry,
merging) and a concrete framing for the check-in tradeoff (noise vs. missed
opportunity) worth testing against their own system, even though the
evidence here is anecdotal and vendor-reported rather than independently
measured.

## Verification notes

Fetched the LangChain blog post directly (langchain.com, on the egress
allowlist) and read it in full. Claims above are traced to the post's text.
The evidence is explicitly anecdotal — drawn from LangChain's own two
products, with one unverified quantitative figure (70% schedule-driven runs)
and no controlled comparison or baseline — so verification is marked
`partial` rather than `verified`, and the post's self-reported figure is
flagged as unverified rather than corroborated.

## Updates

None yet.

## Related entries

None yet.
