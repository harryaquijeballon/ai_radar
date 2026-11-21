---
slug: 2026-laws-decentralized-multiagent-attacks-defenses
title: "Attacks and Defenses in Decentralized Multi-Agent Systems with Hop-by-Hop Task Decomposition and Delegation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.25056
canonical_ids: ["arxiv:2611.25056"]
publisher_or_author: "Matthew D. Laws, Maria Lazou, Alina Oprea, Cristina Nita-Rotaru — arXiv preprint"
published: 2026-11-18
captured: 2026-11-21
relevance:
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance): a
  systematic, quantified study of integrity/availability/confidentiality
  attacks a single malicious agent can mount in decentralized multi-agent
  delegation, paired with a cryptographic audit-trail defense measured on
  a named benchmark.
---

# Attacks and Defenses in Decentralized Multi-Agent Systems with Hop-by-Hop Task Decomposition and Delegation

## Summary

Studies decentralized multi-agent LLM systems in which independently
operated agents (each with its own operator, model, memory, and
configuration) split tasks, execute subtasks, and delegate remaining work
to peers with no central coordinator — a design that improves scalability
and removes single points of failure but means no single party can see
the full execution or enforce correct behavior. The authors design and
test attacks on integrity, availability, and confidentiality: a single
malicious agent can cause up to 100% task failure, raise token use and
runtime by up to 7.7x and 3.2x respectively, and extract up to 94% of
relevant prior tasks from benign agents. As a defense, they present a
cryptographic protocol that records a verifiable execution trace of every
action, plus an auditor that analyzes these traces to detect and attribute
malicious behavior. On the HiddenBench benchmark, the protocol adds
negligible latency, and the auditor detects and correctly attributes 98%
of attacks, including ones designed to otherwise follow the protocol.

## Why it matters

For anyone deploying decentralized, multi-operator agent systems (the
design direction MCP/A2A-style interoperability is pushing toward): a
concrete threat model with measured worst-case damage from a single
malicious participant, and a defense (cryptographic execution traces plus
an auditor) that is measured, not just proposed, against a named benchmark
with near-zero added latency.

## Verification notes

arXiv abstract page fetched 2026-11-21 (paraphrased summary; full abstract
text not reproduced verbatim due to tool quoting limits). Submission
history shows v1 submitted Wed, 18 Nov 2026, 19:06 UTC — within this run's
discovery window (2026-11-20 → 2026-11-21) and the 7-day eligibility cap.
Figures (100% task failure, 7.7x/3.2x token/runtime increase, 94%
extraction, 98% detection/attribution, negligible latency) were confirmed
on a second, independent fetch requesting exact quoted figures, which
matched the first pass exactly. HiddenBench itself and full experimental
tables not independently inspected at capture. No secondary coverage found
(new preprint).

## Updates

None yet.

## Related entries

None yet.
