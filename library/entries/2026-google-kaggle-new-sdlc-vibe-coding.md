---
slug: 2026-google-kaggle-new-sdlc-vibe-coding
title: "The New SDLC With Vibe Coding"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
canonical_ids: []
publisher_or_author: "Addy Osmani, Shubham Saboo, Sokratis Kartakis — Google / Kaggle (5-Day AI Agents Intensive, Day 1 whitepaper)"
published: 2026-06
captured: 2026-07-22
relevance:
  social_science: low
  ai_engineering: high
verification: partial
rationale: >-
  Dead-center on the AI-assisted software development and harness/context
  engineering lenses: a first-party Google framework separating vibe coding
  from agentic engineering, with verification practice as the dividing line.
  User-flagged as a strong accept; scored high for immediately transferable
  team practice. Verification partial — see notes.
---

# The New SDLC With Vibe Coding

## Summary

Google/Kaggle whitepaper (June 2026, course Day 1 material, ~51 pp.) arguing that AI restructures the software lifecycle: implementation compresses dramatically, so **specification and verification become the bottlenecks** — the hard problem is stating what is wanted and confirming what came back is correct. The core distinction is **vibe coding vs agentic engineering**: casual natural-language coding is fine for disposable prototypes but degrades production systems, while agentic engineering is formally specified and rigorously evaluated — with verification practice as the dividing line (tests for deterministic outputs, evals for reasoning trajectories). The paper treats **harness engineering as the dominant capability lever** (stated as "90% of agent capability") and context engineering as the primary cost lever. Phase-by-phase claims: requirements become collaborative prototyping; architecture stays human-driven; implementation collapses to hours; testing becomes bidirectional feedback; maintenance gains automated risky refactoring. Headline statistics as cited by the authors: 85% of professional developers regularly use AI coding agents, ~41% of new code is AI-generated, and vibe coding costs "3 to 10 times more per feature" than structured agentic approaches after a crossover point (unverified — reported as the authors state them).

## Why it matters

*(Radar's assessment.)* For a team building AI research and policy products, this is a citable first-party framework for two practices the radar's own project already embodies: treating the harness — not the model — as the main reliability lever, and drawing the production line at verification (tests + evals), not at code generation. Useful vocabulary for engineering-practice discussions with product teams; its phase-by-phase framing maps directly onto how to structure AI-assisted development workflow standards.

## Verification notes

The canonical Kaggle page is not machine-readable (JavaScript shell), so the whitepaper PDF itself was not read at capture. Content verified instead against the first-party companion post by co-author Addy Osmani ("The New Software Lifecycle", addyosmani.com, 2026-06-16), which explicitly references the whitepaper and restates its frameworks and statistics; authorship, publisher, June 2026 date, and ~51-page length corroborated across the companion post and independent coverage. All Summary claims trace to the companion post; the three headline statistics are marked unverified pending the full PDF. Upgrade path to `verified`: read the whitepaper PDF end-to-end and confirm the statistics' primary sources.

## Updates

*(none yet)*

## Related entries

[2025-korinek-ai-agents-economic-research](2025-korinek-ai-agents-economic-research.md) — applies the same vibe-coding/agentic toolchain to economic research practice.
