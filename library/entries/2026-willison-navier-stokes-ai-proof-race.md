---
slug: 2026-willison-navier-stokes-ai-proof-race
title: "On the Navier–Stokes Millennium Prize Problem"
status: accepted
domains: [ai_engineering, social_science]
source_type: commentary
source_url: https://simonwillison.net/2026/Sep/8/on-navier-stokes/
canonical_ids: []
publisher_or_author: "Simon Willison, relaying OpenAI, Levent Alpöge and Tristan Buckmaster"
published: 2026-09-08
captured: 2026-09-09
relevance:
  social_science: high
  ai_engineering: high
verification: partial
rationale: >-
  A high-profile, contested episode combining formal (Lean) verification of
  an AI-agent-generated mathematical proof (ai_engineering lens 4/6) with
  live questions of epistemic trust in AI-generated knowledge and research
  ethics/priority (social_science lens 8) — archived despite the primary
  source being unreachable this run, per the library's standing practice
  for well-sourced Willison relays of unfetchable primary posts.
---

# On the Navier–Stokes Millennium Prize Problem

## Summary
OpenAI announced that an unreleased model, deployed as roughly 10,000 autonomous agents, produced a solution to a three-dimensional case of the Navier–Stokes existence-and-smoothness problem — one of the seven Millennium Prize Problems, each carrying a $1 million prize. OpenAI states the effort began 2026-09-01, that the agents completed the resolution by 2026-09-05 (about 88 hours later), and that the proof was checked in the Lean formal-proof assistant by 2026-09-06, using "2.7 million messages and approximately 130 billion output tokens." Separately and concurrently, Anthropic-affiliated mathematician Levent Alpöge and NYU professor Tristan Buckmaster had spent close to a year working on related fluid-equation problems using Claude and Codex/GPT-5.6 Sol, reaching a breakthrough around 2026-08-15 and publishing a paper on 2026-09-07 covering a related but distinct (unforced, inviscid) case; the two teams' proofs, and the precise results each proves, differ. Buckmaster reported having heard that OpenAI began its own effort after learning of his team's work; OpenAI did not directly answer when it sent its first prompt for some time, later acknowledging (per Willison's account) that it began after "information about our work had reached OpenAI." OpenAI offered Buckmaster co-authorship on its announcement but explicitly excluded Alpöge, citing competitive concerns tied to his Anthropic affiliation, and separately stated "(unverified beyond this OpenAI statement) while unlikely, we cannot rule out that de-identified data derived from their usage of our products helped improve our models."

## Why it matters
For ai_engineering: a rare public example of formally verifying an AI-agent-generated mathematical proof (Lean verification) as a deterministic check on the output of a large, stochastic multi-agent process — a concrete instance of pairing agentic scale (10,000 agents, ~130B tokens) with a deterministic guardrail, relevant to anyone reasoning about verification methods and costs for agent-fleet outputs (lens 4). The data-provenance question it raises — one lab's model possibly having benefited from a rival's product usage data — is a live case for the governance/reproducibility lens (lens 6). For social_science: a concrete test case for the epistemology of AI-generated knowledge — what a formally verified but agent-produced proof actually establishes, and how it should be trusted absent independent human replication — together with a live instance of research-ethics and priority questions (credit allocation, competitive exclusion of a rival-affiliated researcher from co-authorship) that lens 8 exists to give readers vocabulary for (unverified: the underlying mathematical correctness of either team's proof is outside this library's ability to assess).

## Verification notes
OpenAI's own announcement (openai.com/index/navier-stokes-solution/, on the egress allowlist) returned HTTP 403 on direct fetch this run, consistent with recurring openai.com fetch failures recorded elsewhere in this library (see profiles/social_science/sources.md and prior rejections.md entries). Claims here are traced to Simon Willison's detailed relay (simonwillison.net, allowlisted), which directly quotes OpenAI's own stated timeline and data-provenance caveat as well as Buckmaster's account of the priority dispute. Search-engine snippets from Nature, Quanta Magazine, and Forbes (none on the egress allowlist, not fetched directly this run) describe the same broad narrative — dual announcements, a priority dispute, differing proof scopes — consistent with but not a substitute for a direct primary-source read. Verification is accordingly partial, not verified: the load-bearing claim (that an unreleased model actually resolved the problem, and what exactly was and wasn't independently checked) rests on a secondary account of a still-disputed episode.

## Updates
- **2026-09-09** — Mathematician Terence Tao publicly reacted to the broader dynamic of AI systems rapidly "mining" open mathematical problems, writing that "the collection of good, fruitful open problems is now being mined in a non-renewable fashion" and warning this could incentivize researchers to withhold promising directions from the community, threatening open-science norms (via Simon Willison, simonwillison.net/2026/Sep/9/terence-tao/, relaying Tao's Mastodon post — that primary post was not independently fetched, so this update is unverified beyond Willison's relay).

## Related entries
None yet.
