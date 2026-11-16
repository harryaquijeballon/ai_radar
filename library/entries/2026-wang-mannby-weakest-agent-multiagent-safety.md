---
slug: 2026-wang-mannby-weakest-agent-multiagent-safety
title: "Only as Safe as the Weakest Agent: A Break That Appears Only When the System Is Multi-Agent"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.17520
canonical_ids: ["arxiv:2611.17520"]
publisher_or_author: "Keegan Wang, Anantika Mannby — arXiv preprint"
published: 2026-11-12
captured: 2026-11-16
relevance:
  ai_engineering: high
  social_science: n/a
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance) and lens 1
  (agent architecture/orchestration, subagent isolation): a quantified
  demonstration, run against real production harnesses (Claude Code,
  Codex), that attacks failing against a frontier model used alone can
  succeed once that same model delegates to cheaper sub-agents — a
  concrete, named failure mode (safety set by the weakest agent, not the
  orchestrator) directly actionable for anyone designing multi-agent or
  subagent-delegation systems.
---

# Only as Safe as the Weakest Agent: A Break That Appears Only When the System Is Multi-Agent

## Summary

Shows that attacks which fail against frontier models used alone can break
multi-agent systems — including production coding harnesses Claude Code
and Codex, plus a reference multi-agent harness — through those systems'
own sub-agent delegation mechanisms. In a test where agents searched files
for an answer and one file contained a planted forged record, strong
orchestrator models rarely produced harmful output across over 1,000
trials when acting alone. When those same orchestrators delegated the
search to cheaper sub-agents, failure rates rose sharply, reaching 553 of
900 trials in the largest tested setting. Simulations spanning 18 models
found that aggregator agents frequently repeated a corrupted sub-agent's
error rather than catching it. The authors conclude that a multi-agent
system's safety is determined by its weakest participating agent, not by
the strength of its orchestrator. (unverified: the exact experimental
design beyond the planted-forged-record search task, and the per-model
breakdown across the 18-model simulation — abstract read only, full paper
not retrieved at capture.)

## Why it matters

For anyone building or operating multi-agent or subagent-delegation
systems (including Claude Code- and Codex-style harnesses): a concrete,
reproducible demonstration that delegating a task to a cheaper or weaker
sub-agent can reopen an attack surface that is closed when a strong model
works alone — and that aggregators tend to trust and repeat a corrupted
sub-agent's output rather than catching it. The practical implication is
direct: security and reliability evaluation of a multi-agent system must
target its weakest delegated agent and the aggregation step, not just the
orchestrator, since testing the orchestrator alone would have missed this
failure mode entirely.

## Verification notes

arXiv abstract page fetched directly (2026-11-16); title, both authors,
and "Submitted on 12 Nov 2026" confirmed. Subject categories (cs.MA, cs.AI)
confirmed from the abstract page. Every claim in the Summary traces to the
fetched abstract text: the named harnesses tested (Claude Code, Codex, a
reference harness), the planted-forged-record search task, the >1,000-
trial orchestrator-alone result, the 553-of-900 delegated-failure result,
the 18-model aggregation simulation, and the "weakest agent" conclusion
(quoted directly from the abstract). Full paper text not read at capture;
no independent corroboration attempted (new working paper, no secondary
coverage found). Appeared in arXiv's cs.MA "recent" listing dated Mon, 16
Nov 2026, a 4-day gap from its stated submission date consistent with
normal cross-list announcement lag — within this run's 7-day eligibility
cap. Upgrade path: read the full PDF for the full experimental design and
per-model breakdown.

## Updates

None yet.

## Related entries

None yet.
