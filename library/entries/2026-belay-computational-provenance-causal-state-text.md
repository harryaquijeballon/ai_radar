---
slug: 2026-belay-computational-provenance-causal-state-text
title: "Towards Computational Provenance: Carrying Causal-State Evidence in Generated Text"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.16868
canonical_ids: ["arxiv:2608.16868"]
publisher_or_author: "Benjamin Belay"
published: 2026-08-17
captured: 2026-08-18
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On lens 4/6 (provenance and verification): early-stage evidence that
  generated text can retain detectable traces of the internal computation
  that produced it, tested with controlled small-scale experiments — a
  building block for output-provenance work, not yet a usable technique,
  hence medium ("early, unvalidated" per the profile's tier guidance).
---

# Towards Computational Provenance: Carrying Causal-State Evidence in Generated Text

## Summary

The paper investigates whether generated text retains detectable
information about the internal computational states that produced it,
using two small neural architectures (a modular feed-forward network and a
transformer) trained on arithmetic tasks that pass through two discrete
intermediate states. Reported finding: "information about a verified,
causally relevant internal state can be preserved in generated text even
when the answer is unchanged," across 128 matched-pair evaluations,
reproduced across multiple independently trained models. Linear probes,
however, failed to recover naturally learned intermediate states in a
separate transformer experiment (unverified in detail — full experimental
setup not read beyond the abstract).

## Why it matters

If generated text can carry provenance signal about the process that
produced it, this could eventually support output-verification and
attribution techniques beyond today's post-hoc heuristics. The result is
early and on small controlled tasks (arithmetic, small architectures), so
it is not yet an applicable technique — but it is a concrete, testable
claim worth tracking as this line of work matures.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The core claim
(causal-state information preserved in generated text), the 128
matched-pair evaluation count, and the linear-probe negative result are
traced to the abstract. Full experimental protocol and architecture
details were not independently corroborated — hence partial verification.

## Updates

- **2026-08-18** — Entry created from arXiv abstract during the daily scan.

## Related entries

None yet.
