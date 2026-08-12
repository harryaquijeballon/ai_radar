---
slug: 2026-niu-reliability-contagion-multiagent
title: "Reliability-Contagion Feasibility in LLM Multi-Agent Networks"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.21912
canonical_ids: ["arxiv:2607.21912", "doi:10.48550/arXiv.2607.21912"]
publisher_or_author: "Ruiwu Niu, Xincheng Shu, Ying Zhao — arXiv preprint (cs.MA)"
published: 2026-07-24
captured: 2026-07-27
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on the observability/agent-architecture lenses: a rigorous
  epidemiological-style model (susceptible/exposed/infectious/corrected
  agents) of how erroneous claims propagate through agent communication
  networks, deriving connectivity thresholds that trade off reliability
  against error-spread risk, validated with both large-scale simulation and
  a real (grok-4.3) multi-topology experiment. Kept at medium rather than
  high because the contribution is dense theory plus a topology-selection
  heuristic rather than a directly implementable technique a builder could
  apply this quarter.
---

# Reliability-Contagion Feasibility in LLM Multi-Agent Networks

## Summary

Models how communication among LLM agents, while useful for pooling
evidence, also creates paths along which an erroneous claim can spread. The
authors formulate a correction-aware network model tracking susceptible,
exposed, infectious, and corrected agents, deriving an early-invasion
condition for heterogeneous communication networks, then couple it to an
analytic majority-vote benchmark where a reliability target imposes a
minimum connectivity requirement. They show reliability and error-control
impose opposing graph constraints, characterize when the feasible
intersection is empty versus has an intermediate connectivity range, and
identify regular graphs minimizing invasion risk within the reliable-graph
class. Under a fixed sender budget, the homogeneous first-order threshold
is independent of network density — the communication-budget convention,
not density, determines whether adding edges increases propagation risk.
Finite-network simulations (21,000 trajectories) support these directional
predictions. A controlled experiment on grok-4.3 across three six-node
topologies and 36 closed-world tasks (12 continued to full cascades) found
mean first-generation erroneous-claim offspring rising from 0.667 to 1.333
to 1.667 as node degree increased from 2 to 4 to 5, while the
adoption fraction among exposed neighbors stayed roughly constant (0.333).

## Why it matters

Gives multi-agent system designers a tractable, evidence-backed basis for
choosing communication topology under explicit reliability and
error-propagation constraints, rather than picking a graph shape by
intuition — directly relevant wherever agents deliberate collectively (a
"reality check" or verifier network) and a wrong claim from one agent could
otherwise spread unchecked to the rest.

## Verification notes

arXiv abstract page fetched directly (2026-07-27); title, authors,
"Submitted Fri, 24 Jul 2026 02:38:25 UTC", category (cs.MA) confirmed.
Every claim in the Summary — the epidemiological model, the connectivity
trade-off findings, the simulation scale, and the grok-4.3 experiment's
reported offspring/adoption figures — traces directly to the abstract
text, the primary source for this pre-publication preprint. Full paper
text not read at capture, so the formal derivations underlying the
early-invasion condition are unverified beyond the abstract's summary.
Upgrade path: read the full PDF for the formal model and the full
36-task experimental protocol.

## Updates

None yet.

## Related entries

None yet.
