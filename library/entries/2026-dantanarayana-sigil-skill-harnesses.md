---
slug: 2026-dantanarayana-sigil-skill-harnesses
title: "SIGIL: Compiling Agent Skills into Typed Harnesses"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.27309
canonical_ids: ["arxiv:2607.27309"]
publisher_or_author: "Jayanaka Dantanarayana, Savini Kashmira, Lingjia Tang, Jason Mars — arXiv preprint"
published: 2026-07-29
captured: 2026-07-31
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on harness and context engineering and on tool use: a measured,
  practically usable technique for a mechanism this project's own operating
  model relies on — prose "agent skills" loaded into context and run by a
  tool-calling loop — with a concrete, quantified alternative (compiling
  skills into typed harnesses) and stated before/after numbers.
---

# SIGIL: Compiling Agent Skills into Typed Harnesses

## Summary
The paper starts from the observation that AI agents increasingly acquire capability from "skills": prose procedure files loaded into a model's context and executed by a tool-calling loop. It reports that such prose-based skills achieve only 56% step completion across 30 test cases. The authors introduce SIGIL, which compiles prose skills into executable harnesses via AG-IR, "a typed agentic intermediate representation separating model-owned cognition from code-owned mechanism." Compiled harnesses achieve 86% step completion, "complete the full procedure 2.3x as often, and require 0.58x the tokens," with the improvement holding consistently across different model generations.

## Why it matters
This bears directly on any system — including this project's own two radar skills — that relies on prose skill files run by a model-driven tool-calling loop rather than compiled code: it gives a quantified account of where prose-only skill execution fails (44% incomplete steps) and a concrete, measured alternative (a typed intermediate representation separating what the model reasons about from what code mechanically executes) that a builder could evaluate adopting for higher-stakes or higher-volume agent skills.

## Verification notes
Source is the arXiv abstract page (cs.SE), fetched directly; the figures and quotes above (56% vs. 86% step completion, 2.3x completion rate, 0.58x token cost) are traced to that abstract text. The full paper (AG-IR's formal structure, per-task breakdown) was not fetched, so only the headline figures are traced; verification rests on the source's own stated results rather than independent third-party corroboration, consistent with this library's treatment of single-source fresh preprints. The paper's own submission date (29 July 2026) precedes this run's nominal window start, but it was not surfaced by the 2026-07-30 report, so it is treated as newly discovered today.

## Updates
None yet.

## Related entries
None yet.
