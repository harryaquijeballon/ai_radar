---
slug: 2026-phan-mine-prompt-injection-defense
title: "MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.34188
canonical_ids: ["arxiv:2611.34188"]
publisher_or_author: "Phan, Pham, Nguyen — arXiv preprint (EACL 2027, to appear)"
published: 2026-11-25
captured: 2026-11-27
relevance:
  social_science: n/a
  ai_engineering: medium
verification: unverified
rationale: >-
  A training-free, attack-agnostic defense against indirect prompt
  injection in RAG and agent tool-calling, on lens 6 (reproducibility,
  security and governance — prompt-injection defenses) — archived at
  medium/unverified because the accessible abstract gives no quantified
  accuracy or attack-success-rate figures, only qualitative superiority
  claims.
---

# MINE: A Training-Free Defense against Indirect Prompt Injection via Mutual Information and Embedding Variance

## Summary

MINE targets indirect prompt injection in retrieval-augmented generation
(RAG) and agent tool-calling by defending "by maximizing relevance, not by
detecting attacks" — it is training-free, attack-agnostic, and doubles as a
query-conditioned reranker that uses mutual information and embedding
variance (the abstract does not describe the underlying formulation beyond
this framing). The authors evaluate it on four datasets — Inj-SQuAD and
Inj-TriviaQA (short-context QA), LC-Inj-SQuAD (a new long-context QA
benchmark the authors introduce, averaging 4,032 words per context), and
InjecAgent (agent tool-call injection) — and claim MINE gives the best
accuracy-security trade-off among training-free defenses on all four, is
the only evaluated defense that stays usable against a fully adaptive
attacker, generalizes to agent tool-call injection, and has the lowest
inference latency on long contexts. (unverified: the abstract reports no
accuracy, attack-success-rate, or latency numbers to support these
comparative claims — only the benchmark's average context length. The
superiority claims above are the authors' own characterization and could
not be independently traced to a specific figure.)

## Why it matters

If the claims hold up under full-text reading, a training-free defense
that generalizes across RAG and agent tool-calling injection — without
needing retraining for new attack variants, unlike supervised detectors —
would be a practically significant addition to lens 6's toolkit for
reproducibility, security and governance in agentic systems that ingest
untrusted retrieved or tool-returned content. This entry is archived at
medium/unverified specifically because the quantified evidence behind
those claims was not accessible from the abstract alone.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.34188, v1 submitted
2026-11-25, cs.CL; EACL 2027 main-conference paper, to appear). The
methodology framing and the four evaluation datasets are traced to the
abstract's own description. The comparative superiority claims (best
trade-off, only defense robust to adaptive attackers, lowest latency) are
NOT independently verifiable from the fetched abstract text, which gave no
supporting numbers; marked unverified accordingly. No independent
corroboration was attempted.

## Updates

None yet.

## Related entries

None yet.
