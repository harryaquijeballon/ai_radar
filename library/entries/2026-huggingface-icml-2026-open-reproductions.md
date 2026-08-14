---
slug: 2026-huggingface-icml-2026-open-reproductions
title: "What We Learned by Reproducing 2,200 Papers from ICML"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://huggingface.co/blog/icml-2026-open-reproductions
canonical_ids: ["repo:ICML-2026-agent-repro/challenge"]
publisher_or_author: "Hugging Face — community hackathon report"
published: 2026-08-13
captured: 2026-08-14
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
license: not stated on the fetched page
rationale: >-
  Directly on lens 4 (evaluation/validation) and lens 8 (reliable research
  products): the largest reported field study to date of AI coding agents
  used specifically to reproduce published research claims, at real scale,
  with quantified verified/falsified/contested rates and an explicit lesson
  about where human oversight remains necessary — practically usable by
  anyone designing an AI-assisted research-reproduction or claim-verification
  pipeline. Headline figures independently corroborated against secondary
  coverage (howaiworks.ai, Toksick Magazine) and the underlying public
  HF dataset/collection, clearing the report bar's verification requirement.
---

# What We Learned by Reproducing 2,200 Papers from ICML

## Summary

Hugging Face organized a community hackathon (15 July – 2 August 2026, with
$4,000 in GPU credits for the strongest results) in which 1,221 participants
used AI coding agents of their choice (including Claude Code, Codex, and
OpenResearch's orx) to reproduce claims from ICML 2026 papers, publishing
their work as auditable "Trackio logbooks." An automated judge model
(GLM-5.2) classified each individual claim as verified, falsified,
toy-scale, or inconclusive. Scale: 6,816 reproduction logbooks published,
covering 2,226 papers (about 34% of the conference's roughly 6,350 accepted
papers), evaluating 35,908 individual claims via 2,962 cloud compute jobs.
Results: 51% of examined papers (1,103) had at least one claim independently
verified; 266 papers were fully reproduced with all claims verified; 23% of
papers had at least one falsified or contested claim; 49 papers had all
claims falsified; 242 papers showed contradictory verdicts across
independently-working teams attempting the same paper. The write-up's
central lesson: human oversight remained essential throughout — participants
were needed to question assumptions, recognize scale-dependent behavior, and
make perceptual judgments the automated pipeline could not make alone;
human-directed, agent-executed collaboration produced the most reliable
outcomes.

## Why it matters

The largest quantified field test yet of AI agents doing reproduction work
against real published claims at scale, with a concrete taxonomy of outcomes
(verified/falsified/toy-scale/inconclusive/contested) and a clear, evidenced
conclusion that fully autonomous agent reproduction is not yet reliable
without human direction — directly usable as a design reference for anyone
building an AI-assisted claim-verification or research-reproduction pipeline
(the standing "agentic simulation/validation" interest this radar tracks),
and as calibration data for how much to trust agent-only reproduction
efforts.

## Verification notes

Fetched and read the Hugging Face blog post directly (not abstract-only).
Load-bearing figures (1,221 participants, 6,816 logbooks, 2,226 papers, 51%
papers with a verified claim, 266 fully reproduced, 23% with a
falsified/contested claim) were independently corroborated via a second
open-web search turning up secondary coverage (howaiworks.ai,
"AI Agents Take On a Challenge to Reproduce ICML 2026 Papers"; Toksick
Magazine, "Insights Gained From Reproducing 2,200 ICML Papers") that report
the same headline numbers, plus the public Hugging Face
`ICML-2026-agent-repro` dataset/collection as underlying primary evidence.
Not independently re-derived from the raw Trackio logbooks or dataset
itself. Note on window: published 2026-08-13, the same calendar date as the
prior daily report; that report's own scan note for ai_engineering lists
what it found from Hugging Face that day and does not mention this post,
indicating it was published after that run executed — included today as a
genuinely unseen development rather than silently dropped on a date
technicality.

## Updates

None yet.

## Related entries

None yet.
