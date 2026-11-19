---
slug: 2026-xu-idempotency-not-recovery-fault-injection
title: "Idempotency Is Not Recovery: A Fault-Injection Study of Language-Model Agent Tool Actions"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.23353
canonical_ids: ["arxiv:2611.23353"]
publisher_or_author: "Song Xu — arXiv preprint (cs.SE)"
published: 2026-11-17
captured: 2026-11-19
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 5/6 (observability/debugging; reproducibility, security and
  governance): a controlled fault-injection study showing that duplicate
  suppression (idempotency) and recovery from an interrupted tool call are
  distinct properties, with quantified evidence for which runtime components
  are load-bearing and at what throughput cost — directly applicable to
  anyone building agent tool-execution harnesses.
---

# Idempotency Is Not Recovery: A Fault-Injection Study of Language-Model Agent Tool Actions

## Summary

Studies what happens when a language-model agent's tool call is interrupted
after it may already have changed an external system: a naive retry can
duplicate the effect, while assuming success can silently hide an action
that never completed. The author built a controlled agent runtime combining
authorization, an action ledger, target-side idempotency, reconciliation,
and evidence sealing, then tested it against ten single-host fault classes
using a target-side oracle kept separate from the runtime's own ledger.
Across 200 crash-and-replay pairs, the full configuration recorded zero
repeated effects, while each simpler baseline configuration recorded 117.
Disabling the action ledger produced orphaned effects in every affected
trial; disabling reconciliation left all post-effect crash outcomes
ambiguous even though no duplicates occurred. A supplementary test under
response loss or delay found a similar pattern. The full, safest runtime
configuration had roughly one-seventh the fail-open throughput of the
unsafe baselines, and injected evidence-write faults left many trials
unresolved. The author concludes duplicate suppression and recovery
correctness are separate engineering properties with a measured
performance tradeoff between them, within the scope of this benchmark.

## Why it matters

For anyone building a harness that lets an LLM agent call tools with
real-world side effects (payments, file writes, API calls to external
systems): a direct, load-bearing answer to "is idempotency enough to make
agent tool calls safe to retry?" — no, and this paper shows by how much,
component by component. The ablation results (action ledger, reconciliation,
evidence sealing each isolated and fault-injected) give builders a concrete
checklist of what to implement and what each piece actually buys in
measured duplicate-prevention and recovery-certainty terms, plus an explicit
throughput cost to weigh against that safety.

## Verification notes

arXiv abstract page fetched directly (2026-11-19); title, author, "Submitted
on Tue, 17 Nov 2026, 13:49 UTC" date, and cs.SE/cs.AI subject categories
confirmed. Every quantitative claim in the Summary (200 crash-and-replay
pairs, 0 vs. 117 duplicate effects, the ledger/reconciliation ablation
results, the ~1/7 throughput figure, the evidence-write fault results)
traces to the fetched abstract text. Full paper body not read at capture;
no independent corroboration attempted (new working paper, no secondary
coverage found). Appeared in arXiv's cs.SE "recent" listing dated Thu, 19
Nov 2026, two days after its Tue, 17 Nov 2026 submission — within normal
cs.SE moderation/announcement lag (no evidence of prior circulation found),
so visibility date is today per the engine's listing-date rule; also
within the 7-day eligibility cap under either date. Upgrade path: read the
full PDF for the formal fault-injection protocol and the oracle design.

## Updates

None yet.

## Related entries

None yet.
