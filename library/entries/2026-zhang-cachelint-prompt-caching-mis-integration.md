---
slug: 2026-zhang-cachelint-prompt-caching-mis-integration
title: "Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.34817
canonical_ids: ["arxiv:2610.34817"]
publisher_or_author: "Ying Zhang, Ruoqi Guo, Yi Liu, Gelei Deng, Yuekang Li, Yepang Liu, Leo Zhang"
published: 2026-10-26
captured: 2026-10-27
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on observability/debugging and deterministic guardrails (lenses 4,
  5): a deterministic checker for a real, silent, cost/correctness failure
  mode (misconfigured prompt-caching integration), validated on real
  open-source agent codebases with upstream fixes confirmed — a
  practically adoptable detection practice, not a one-off anecdote.
---

# Silent and Costly: Characterizing and Detecting Prompt-Caching Mis-Integration in LLM Agents

## Summary

Studies how developers integrate prompt caching — a provider feature that
reduces LLM inference cost and latency — into agent systems. The authors
analyze 120 caching-related pull requests from 10 popular open-source
agent projects and identify two main error kinds: misconfigured caching
requests and incorrect counting of cache reads. Most of these errors are
reported to fail silently, producing no visible runtime failure. To detect
them, the authors built CACHELINT, which combines CodeQL-based location of
caching call sites with checks against a dated provider-capability model
and LLM-based review. CACHELINT reportedly reached 0.71 precision and 0.78
recall on the labeled cases. Applied more widely across 571 agent
projects, it flagged 32 issues at 0.86 precision; developers reportedly
confirmed 21 of the findings, and 18 were fixed upstream, including one fix
in Anthropic's official SDK (all figures as stated in the fetched
abstract; tool implementation and full 571-project sample not reviewed at
capture).

## Why it matters

Prompt caching is a cost/latency optimization widely adopted in agent
systems, and this paper gives concrete evidence that its integration fails
silently often enough to matter — with a working, adoptable detection tool
(CodeQL + a provider-capability model + LLM review) and real, confirmed
upstream fixes as validation, including in a major provider's own SDK.
Directly actionable for any team running LLM agents with caching enabled:
a specific class of invisible correctness/cost bug to check for, and a
concrete method for checking it.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-27; single version,
submitted 26 Oct 2026). The 120-PR / 10-project analysis, the two named
error kinds, CACHELINT's design (CodeQL + capability model + LLM review),
the 0.71/0.78 precision/recall figures, the 571-project / 32-issue / 0.86
precision wider-test figures, and the "21 confirmed, 18 fixed upstream,
including Anthropic's SDK" outcome all trace to the fetched abstract text.
CACHELINT's implementation details, the labeled dataset, and the full list
of 32 flagged issues were not reviewed — load-bearing figures are traced
to the source's own stated summary but not independently corroborated.

## Updates

None yet.

## Related entries

None yet.
