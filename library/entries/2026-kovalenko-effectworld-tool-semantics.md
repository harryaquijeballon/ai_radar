---
slug: 2026-kovalenko-effectworld-tool-semantics
title: "Small Agents Should Know What Their Tools Do"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.35981
canonical_ids: ["arxiv:2610.35981"]
publisher_or_author: "Alexander Kovalenko, Artem Redchych"
published: 2026-10-26
captured: 2026-10-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on tool use and MCP (lens 3): a reusable tool-interface design
  (declared effects, idempotency, read/write resources) that lets a
  replay verifier check trace safety and generates training signal from
  wasteful traces, with quantified gains on small open models that
  transfer to a public benchmark (BFCL) — directly actionable, interoperable
  tool-design knowledge rather than a framework-specific trick.
---

# Small Agents Should Know What Their Tools Do

## Summary

Argues that small open-weight language models can call tools syntactically
but don't reason about tool *effects*: they delete without confirmation,
repeat writes, re-read state they already hold, and issue one call per
turn when a short program would do. The authors introduce EffectWorld, an
executable environment where each tool declares its effects, whether it
is idempotent, and which resources it reads and writes. These declarations
let a replay verifier check whether a trace is "effect-safe," let an
executor run multi-call programs in a single turn, and let an optimizer
convert wasteful traces into training signal. Low-rank adapters trained on
this data improve Qwen3-4B and other model families and transfer to the
Berkeley Function-Calling Leaderboard (BFCL). The authors separately find
that refusal templates common in public tool-use datasets teach small
models *not* to call tools, and that positive examples — not negative
ones — drive the observed learning.

Reported results for Qwen3-4B: in-distribution task success rises from
53% to 99%; on a held-out split (unseen task kinds and distractor tools),
52% to 81%; on an unseen domain, 74% to 83%; output tokens drop to about a
third of the base model's. On BFCL, live accuracy matches the base model,
multi-turn accuracy rises from 21.9 to 26.6, and non-live accuracy *drops*
from 88.0 to 31.4 when refusal-template examples are included, recovering
to 84.8 once they are filtered out (all figures as stated in the fetched
abstract; full paper, training recipe, and benchmark protocol not
reviewed at capture).

## Why it matters

A concrete, transferable fix for a specific and common small-model
failure mode (tool calls that ignore what the tool actually *does* —
unconfirmed deletes, redundant writes, one-call-per-turn inefficiency):
declare tool effects and idempotency, verify traces against those
declarations, and train on the resulting signal. The finding that
standard refusal-template training data actively teaches models not to
use tools — and that filtering it recovers most of the lost accuracy — is
an immediately checkable fact about any team's existing fine-tuning data.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-29; single version,
submitted 26 Oct 2026, 10:28 UTC, 71 KB). The EffectWorld design
(declared effects, idempotency, replay verification), the refusal-
template finding, and all quantified figures (53%→99%, 52%→81%, 74%→83%,
~1/3 token count, BFCL multi-turn 21.9→26.6, BFCL non-live 88.0→31.4→84.8)
trace to the fetched abstract text. The abstract also references a "near-
miss-decline" recipe with no numbers given for it; that claim is
unverified pending the full paper. Training recipe details and the BFCL
evaluation protocol were not independently reviewed.

## Updates

None yet.

## Related entries

None yet.
