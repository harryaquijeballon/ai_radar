---
slug: 2026-vuminh-webwright-code-writing-web-agents
title: "Webwright: Why AI Web Agents Should Write Code, Not Click"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/webwright-why-ai-web-agents-should-write-code-not-click/
canonical_ids: []
publisher_or_author: "Chien Vu Minh — Towards Data Science"
published: 2026-08-17
captured: 2026-08-18
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Squarely on lens 1 (agent architecture) and lens 3 (tool use): a
  code-writing alternative to click-by-click web-agent action loops, with
  quantified benchmark gains and a small, concretely described
  implementation — a usable architectural pattern with stated trade-offs
  and evidence, per the profile's high-tier bar for lens 1.
---

# Webwright: Why AI Web Agents Should Write Code, Not Click

## Summary

The article covers Webwright, a browser-automation framework from Microsoft
Research and the University of Hong Kong that has the model write and run
executable code (Playwright plus bash) instead of predicting one UI action
at a time. The stated problem with the click-loop approach: vision agents
struggle with layout shifts and spend tokens on screenshots, DOM-based
agents accumulate stale-context bloat, and fixed action APIs (click, type,
scroll) cannot express loops, retries, or leave behind a reusable artifact.
Reported results: a 26.6-point improvement on long-horizon tasks (33.5% to
60.1% success with GPT-5.4) on the "Odysseys" benchmark, plus scores of
86.7% (GPT-5.4) and 84.7% (Claude Opus) on Online-Mind2Web; per-task cost of
about $2.37 (GPT-5.4) and $6.09 (Claude Opus); and a core implementation of
roughly 1,000 lines across three components (Runner, Model Endpoint,
Environment). Three worked examples are described: 1,000 books scraped
across 50 pages in 37 seconds with a reusable CLI produced as a byproduct;
100 JavaScript-rendered quotes fetched in 8.9 seconds; and an infinite-scroll
page handled via scroll-until-stable logic with the agent verifying data
completeness itself (unverified — figures are as reported in the article,
sourced to the underlying Microsoft Research/HKU work, not independently
re-run).

## Why it matters

For anyone building browser-using agents, this names a concrete
architectural alternative to the dominant observe-predict-act loop, with
stated trade-offs (higher up-front code-generation cost per task, offset by
a reusable artifact and much higher long-horizon success) and benchmark
evidence rather than just an opinion. The "workspace persistence over
browser-session persistence" framing is directly applicable to teams
deciding how to structure a web-automation agent.

## Verification notes

Full article read (not abstract-only). Benchmark figures, cost figures, and
the three worked-example results are traced to the article text, which
attributes the underlying research to Microsoft Research and the University
of Hong Kong. The original paper/report was not independently located or
cross-checked, so the headline load-bearing benchmark numbers are traced
but not independently corroborated — hence partial verification.

## Updates

- **2026-08-18** — Entry created from the daily scan.

## Related entries

None yet.
