---
slug: 2026-he-requirement-driven-candidate-sourcing-agent
title: "An Interactive Agent for Requirement-Driven Candidate Sourcing"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.23501
canonical_ids: ["arxiv:2608.23501"]
publisher_or_author: "Yuanpeng He, Fangjing Li, Xiangyu Ru, Kexin Sun, Kun Yang, Lijian Li, Chi-Man Pun, Qingsong Wen, Wenpin Jiao, Mingkai Guo, Yirong Feng, Daiheng Gao, Zhi Jin — arXiv preprint"
published: 2026-08-24
captured: 2026-08-25
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on harness and context engineering (lens 2): reframes an
  under-determined natural-language request as a requirements-engineering
  problem and names a reusable interaction pattern (bounded elicitation,
  workflow templates, a two-stage commit protocol, bidirectional
  termination guards) with quantified retrieval gains — a transferable
  harness pattern for any agent handling vague, under-specified user
  requests, though demonstrated in a narrow domain (people search).
---

# An Interactive Agent for Requirement-Driven Candidate Sourcing

## Summary

Reframes candidate sourcing (finding people matching a natural-language
description) as a requirements-engineering problem rather than plain
information retrieval, on the premise that most such requests are
under-determined. The authors' interactive agent handles this through
elicitation, validation, and verification steps, implemented via "bounded
elicitation, workflow templates, a two-stage commit protocol, and
bidirectional termination guards." In their evaluation, the agent achieves
"100% coverage at 2.5× the yield" of existing systems, with 90% of
identified candidates found by none of 20 LLM-plus-web baselines it was
compared against, and recall of "0.241 of the union pool, 1.9× the next
system" — the strongest sourcing engine in the comparison, with precision-
ranking language models positioned as a complementary verification layer
rather than a replacement.

## Why it matters

A concrete interaction-harness pattern for the general problem of an agent
handling a request that is genuinely under-specified rather than merely
under-articulated: bound how much clarification the agent asks for,
template the workflow instead of improvising it per request, commit to
decisions in two stages, and use explicit termination guards so the agent
doesn't loop or stop too early. Though demonstrated in a people-search/
recruiting context, the pattern generalizes to other agent tasks built
around vague or incomplete user requests, with quantified coverage/recall
gains over LLM-plus-web baselines as evidence it works.

## Verification notes

Fetched directly from the arXiv abstract page (2026-08-25); title, full
author list, and submission date (24 Aug 2026) confirmed. The four named
mechanisms (bounded elicitation, workflow templates, two-stage commit,
termination guards) and the three headline figures (100% coverage at 2.5x
yield; 90% of candidates found by none of 20 baselines; 0.241 recall,
1.9x the next system) all trace directly to the fetched abstract text —
the authors' own reported results. Full paper (baseline definitions,
per-query breakdown) not read at capture; upgrade path: read the full PDF
for the baseline comparison methodology.

## Updates

None yet.

## Related entries

None yet.
