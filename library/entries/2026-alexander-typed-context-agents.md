---
slug: 2026-alexander-typed-context-agents
title: "AI Agents Don't Need More Context — They Need Typed Context"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/ai-agents-dont-need-more-context-they-need-typed-context/
canonical_ids: []
publisher_or_author: "Emmimal P Alexander — Towards Data Science"
published: 2026-08-24
captured: 2026-08-25
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on harness and context engineering (lens 2): names a specific
  mechanism (a runtime context-type system with four tagged categories,
  enforced type-transition rules, and a provenance ledger) for a concrete,
  previously-unnamed failure mode — silent relabeling of tool output as
  instruction when heterogeneous context is flattened to plain strings —
  with a working implementation, a concrete before/after example, and
  explicitly stated limitations rather than overclaiming.
---

# AI Agents Don't Need More Context — They Need Typed Context

## Summary

Argues that many agent failures blamed on "not enough context" actually
stem from context losing its semantic identity when heterogeneous sources
(instructions, tool outputs, retrieved evidence, conversation memory) are
flattened into plain strings before the prompt is assembled — "content
that enters the system as tool output cannot silently become an
instruction" is exactly the failure this flattening enables. The proposed
fix is a lightweight runtime "context type system": every context item is
tagged as one of `INSTRUCTION`, `EVIDENCE`, `MEMORY`, or `TOOL_OUTPUT`,
with strict rules on which type transitions are legitimate before
serialization into a prompt, and a provenance ledger (`derived_from`
metadata) recording legitimate transformations (e.g., `TOOL_OUTPUT` →
`EVIDENCE`). A worked example shows a shipping tool returning both a
current delivery date and a prior customer request in the same string;
without typing, both lines look identical to the pipeline, but attempting
to route the tool output into the instruction channel raises a
`ContextTypeError` before the model ever sees it. The author validated
the system with eight unit tests (type registration/validation, invalid
promotion prevention, provenance preservation, memory/state separation,
failed-tool-output rejection) — "8/8 checks passed" — all without LLM
calls, and explicitly frames the layer as "a correctness and observability
layer, not a new capability for the model itself," distinct from prompt
engineering (word choice) and context engineering (information selection).
Stated limitations: single-process only, no automatic type inference, no
fix for downstream reasoning errors, no distributed-architecture support,
and it measures structural correctness rather than task-accuracy
improvement.

## Why it matters

Names and gives a concrete mechanism for a specific agent-harness failure
mode — heterogeneous context silently losing its provenance/type when
flattened to strings — that is otherwise invisible until it causes a
downstream error, and offers a deterministic, pre-model check (rejecting
an illegitimate type transition before the prompt is built) rather than
relying on the model to notice the confusion itself. Directly applicable
to any agent harness assembling prompts from multiple heterogeneous
sources; the explicit statement of what the layer does *not* do (fix
reasoning, scale to distributed systems) makes the claim easy to scope
correctly rather than overapply.

## Verification notes

Fetched directly from the published article (2026-08-25); author (Emmimal
P Alexander), publication date (24 Aug 2026), the four context types, the
provenance-ledger mechanism, the shipping-tool worked example, the "8/8
checks passed" test result, and the stated limitations all trace directly
to the fetched article text. This is a practitioner build-log/commentary
piece with a working code example rather than a peer-reviewed study;
"verified" here means the described mechanism and test result were
accurately traced to the source, not independently re-run.

## Updates

None yet.

## Related entries

None yet.
