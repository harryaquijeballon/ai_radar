---
slug: 2026-anthropic-components-of-agent-memory
title: "The Components of Agent Memory"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://www.anthropic.com/research/components-of-agent-memory
canonical_ids: []
publisher_or_author: "Anthropic Engineering"
published: 2026-11-06
captured: 2026-11-07
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on harness/context engineering (lens 2): names a concrete four-layer
  memory architecture (transcripts, memory notes, memory representations,
  injected context) plus an offline "dreaming" consolidation process, and
  states when each mechanism helps or hurts — with mixed-quality evidence
  from Anthropic's own internal benchmarks and single-run anecdotes, which
  the rationale and entry both flag rather than treat as conclusive.
---

# The Components of Agent Memory

## Summary

Anthropic Engineering describes a four-layer agent-memory hierarchy spanning
sessions: (1) transcripts — a searchable event log; (2) memory notes —
salient observations Claude writes during a session; (3) memory
representations — structures such as wikis with linked pages; (4) injected
context — material loaded into every new session. "Dreaming" is an offline
process, analogized (unverified beyond the analogy itself: this is explicitly
a loose neuroscience comparison, not a mechanistic claim) to hippocampal
replay/neocortical consolidation, that reads lower layers and reorganizes
upper ones — correcting notes, creating new notes/representations, and
choosing what gets preloaded. The post explicitly excludes weight changes,
in-context learning, and compaction from its definition of "agent memory."

Reported evidence is mixed in rigor. Measured results include: on CL-Bench, a
memory learning loop raised database-task performance across models (e.g.,
Opus 5.5 0.655→0.838, Sonnet 5.5 0.644→0.833), though from one benchmark, one
task, with no variance reported; fixed "record only failures" rules hurt
stronger models (e.g., Opus 5 −0.234); explicit steering helped weaker models
most (Sonnet 4.6 rose 0.364→0.641); wiki-based dreaming raised QA accuracy
from 13% to 48% over 128 sessions on one 350k-file internal corpus (25
questions, one model); wiki+search beat search alone by 61% vs 53% on the
same questions while saving roughly 20k tokens per question. Several other
claims (selective vs. indiscriminate memory, wasteful "state-based" facts,
dreaming correcting a wrong note) rest on single anecdotal runs, mostly from
internal Pokémon-playing agent trials, and are presented as illustrative, not
as general proof.

## Why it matters

Gives builders a named vocabulary and a set of concrete, if unevenly
evidenced, design rules for agent memory: keep injected context small because
extra tokens cost budget and long instructions reduce adherence; match
guidance specificity to model strength (frontier models need less
prescriptive rules); separate fast capture (notes) from offline consolidation
(dreaming) rather than doing both in-session; and watch for representations
(e.g., wikis) that grow larger than their source material and stop helping.
Useful as a structured starting checklist for anyone designing a memory
system, with the caveat that most of the headline numbers come from one
vendor's internal benchmarks and single-run anecdotes, not independent or
large-sample evaluation.

## Verification notes

Fetched and read directly (anthropic.com, on the egress allowlist). Every
claim above, including the CL-Bench and internal-corpus figures, is traced
directly to the source text; no load-bearing claim here depends on
information beyond it. This is a first-party vendor source with a direct
stake in Claude's perceived memory capability; per
`profiles/ai_engineering/sources.md`'s vendor-source caveat, claims are
reported here with their actual evidence class (measured/benchmarked vs.
anecdotal/single-run) stated explicitly rather than treated as uniformly
authoritative, and no independent third-party corroboration of Anthropic's
own reported numbers was sought.

## Updates

None yet.

## Related entries

None yet.
