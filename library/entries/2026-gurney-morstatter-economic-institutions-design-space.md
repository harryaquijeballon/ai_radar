---
slug: 2026-gurney-morstatter-economic-institutions-design-space
title: "Beyond Named Mechanisms: Economic Institutions as a Design Space for Artificial Agents"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.15017
canonical_ids: ["arxiv:2611.15017"]
publisher_or_author: "Nikolos Gurney, Fred Morstatter — arXiv preprint (cs.MA, cross-listed cs.AI, cs.GT, econ.GN)"
published: 2026-11-11
captured: 2026-11-15
relevance:
  social_science: medium
  ai_engineering: medium
verification: verified
rationale: >-
  Cross-domain conceptual framework: argues multiagent systems have borrowed
  economic institutions (auctions, markets, matching) designed for humans,
  and proposes describing institutions as typed structures independent of
  the agents that run them — relevant to social_science lens 4 (market/
  institutional design as a policy-analysis object) and ai_engineering
  lens 1 (agent architecture, naming a design space for multi-agent
  coordination mechanisms). Medium on both: a think-piece/taxonomy with a
  small illustrative demonstration rather than a validated method or
  empirical result.
---

# Beyond Named Mechanisms: Economic Institutions as a Design Space for Artificial Agents

## Summary
The paper argues that multiagent-systems research has largely borrowed its
economic institutions — auctions, markets, prices, bargaining, matching —
from human societies. Those institutions bundle together identity,
competence, execution, ownership, commitment, and settlement in ways suited
to human participants. Engineered agents do not share those constraints, so
the authors argue the familiar, named institutions are likely only a small
sample of a much larger design space (unverified: the size/shape of this
space is asserted, not measured).

The authors propose a provisional "chart" describing institutions as typed
structures across dimensions such as positions, rights and duties,
allocation, information, time, state, process, value, and external
recognition — separating the institution's structure from the agents that
operate it. In this framing, named institutions (e.g., "an auction") become
overlapping regions on the chart, and the gaps between them are candidate
areas for new institutional designs.

As a small illustrative demonstration, the authors describe a simulation
that institutionalizes one technical act — copying an agent's competence —
in three different ways: as a new independent supplier, as licensed
capacity that creates no new participant, and as a split of one economic
position into successors that inherit some but not all obligations. In a
paired task, all three configurations produce an identical technical trace,
even though they differ in who exists, who owns the copy, who is obligated,
and who gets paid. The abstract and fetched material report no quantified
results (effect sizes, sample sizes) beyond this qualitative finding
(unverified beyond the abstract: the full paper body was not machine-
readable to this session — see Verification notes).

## Why it matters
For social-science readers: frames "which economic institution governs an
AI agent's actions" as a design choice with real distributional
consequences (who owns a copy, who is liable, who gets paid) rather than a
fixed fact — directly bears on lens 4 (competition, regulation, public
policy) questions about how to regulate or analyze markets populated by
artificial agents.

For AI-engineering readers: offers a vocabulary for describing multi-agent
coordination mechanisms (lens 1, agent architecture and orchestration) that
is decoupled from borrowed human-market metaphors — useful when designing
how autonomous agents in a system should be identified, held accountable,
and compensated, distinct from how they technically execute.

## Verification notes
Fetched the arXiv abstract page (arxiv.org/abs/2611.15017) directly; every
claim above is traced to that text, and none is a load-bearing quantified
result requiring independent corroboration (the abstract itself states no
numeric effect sizes). A PDF fetch of the full paper returned a compressed
binary stream that could not be parsed in this session, so the
simulation's full setup and any numeric results in the paper body beyond
the abstract remain unchecked (flagged above as unverified beyond the
abstract); that limitation does not affect the claims this entry makes.

## Updates
None yet.

## Related entries
None yet.
