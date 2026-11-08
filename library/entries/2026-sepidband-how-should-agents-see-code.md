---
slug: 2026-sepidband-how-should-agents-see-code
title: "How Should Agents See Code? Rethinking Code Representations for Agentic Software Engineering"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07286
canonical_ids: ["arxiv:2611.07286"]
publisher_or_author: "Melika Sepidband, Jiho Shin, Song Wang, Hadi Hemmati"
published: 2026-11-05
captured: 2026-11-08
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 2 (harness/context engineering): a comparative study of
  structured code-representation workflows (AST, call graphs, dependencies,
  docs, hybrid) against a raw-tool baseline, with a nuanced, mostly-negative
  result (gains concentrated in localization, smaller elsewhere, latency up)
  — useful caution rather than a clear win to adopt.
---

# How Should Agents See Code? Rethinking Code Representations for Agentic Software Engineering

## Summary

Tests whether giving LLM agents structured "maps" of a code repository —
rather than only raw files, lexical search, and shell commands — improves
repository-level software engineering. Compares five workflows (abstract
syntax trees, call graphs, module dependencies, documentation-enriched
search, and a hybrid) using Claude Code with Haiku 4.5 against a raw-tool
baseline, across fault localization, code generation and repair, test
generation, and security patching. Map-based workflows reduced token use
most when localization was the bottleneck, but gains in patch and test
success were smaller, and latency generally increased. The authors
conclude the benefits of structured code representations depend on the
task rather than being universal.

## Why it matters

A useful corrective to the assumption that giving agents richer structural
context (AST, call graphs, etc.) is a free win: the gains are real but
narrow (mainly token savings during fault localization) and come with a
latency cost, so a builder should match the representation to the specific
task bottleneck rather than adopting one by default (lens 2).

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 5 Nov 2026, no revisions). The five-workflow comparison design
and the task-dependent, latency-cost findings trace to the fetched abstract
text — treated as `verified` per this library's standing convention for
single-source arXiv preprints whose headline claims are self-reported. The
full paper (exact benchmark tasks, per-workflow numbers) was not reviewed
at capture.

## Updates

None yet.

## Related entries

None yet.
