---
slug: 2026-jarmak-engineering-reliable-coding-agents
title: "Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.13867
canonical_ids: ["arxiv:2608.13867"]
publisher_or_author: "Stephanie Jarmak — arXiv preprint (cs.SE)"
published: 2026-08-14
captured: 2026-08-17
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
license: "CC BY 4.0"
rationale: >-
  High on lens 2 (harness and context engineering) and lens 4 (evaluation and
  validation): reframes coding-agent reliability as a systems problem —
  harness, execution state, retrieval, memory, permissions, review
  interfaces, resource allocation — rather than a model-capability problem,
  backed by a 206-record synthesis and runnable evaluation protocols a
  builder could apply directly.
---

# Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model

## Summary

A single-author technical monograph (314 pages, 30 figures, CC BY 4.0) arguing that AI coding agents "are commonly evaluated as models but deployed as systems," and that "their reliability depends not only on model capability, but on the harness, execution state, retrieval, memory and state management, permissions, review interfaces, and resource allocation" (quoted from the abstract). The work synthesizes 164 scholarly sources, 100 practitioner records, 29 benchmarks, and 17 case studies into a catalog of 206 reliability records, a dependency framework spanning the agent lifecycle, evaluation and reliability protocols described as runnable, and five reusable agent skills with supporting evidence maps. A central claim is that "many apparent model failures originate elsewhere in the system" — improvements to one component (e.g., the model) frequently fail to translate into end-to-end reliability gains. The specific content of the 206 individual reliability records and the five reusable skills is described only at the level the abstract and summary sources provide; the full monograph body and its companion GitHub artifact were not read in this pass (unverified beyond the abstract-level description).

## Why it matters

Gives ai_engineering practitioners a shared vocabulary and a large, catalogued evidence base for treating coding-agent reliability as a system-design question — where to look (harness, state, permissions, retrieval) when a coding agent's failures don't trace back to the underlying model. Directly usable as a checklist or reference when auditing or designing a production coding-agent harness, which is the core concern of lenses 2 and 4.

## Verification notes

Read via the arXiv abstract page (2026-08-17). The structural claims (scope of synthesized sources, 206-record catalog, five reusable skills, 314 pages/30 figures, CC BY 4.0 licence) are quoted or closely paraphrased from the abstract and its accompanying description. The monograph's full text and companion GitHub artifact were not fetched or read in this pass, so the specific content of individual reliability records and skills is not independently verified — traceable to the abstract but not corroborated beyond it, hence partial verification.

## Updates

None yet.

## Related entries

- [2026-bousetouane-proofagent-readiness-index](2026-bousetouane-proofagent-readiness-index.md) — related: another framework arguing agent capability benchmarks alone don't establish production readiness.
- [2026-valente-ark-coding-agent-architecture](2026-valente-ark-coding-agent-architecture.md) — related: exploratory study of coding-agent architecture from the systems side.
