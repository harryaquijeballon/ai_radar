---
slug: 2026-wu-what-the-middleman-delivers-api-relays
title: "What the Middleman Delivers: Answer Behavior, Tool Permissions, and Billed Usage in LLM API Relays"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.07650
canonical_ids: ["arxiv:2611.07650"]
publisher_or_author: "Xiaodong Wu, Zhimin Zhao, Qi Li, Chaklam Cheong, Xiangman Li, Jianbing Ni"
published: 2026-11-05
captured: 2026-11-07
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on tool use and MCP / reproducibility and governance (lenses 3, 6):
  a direct, repeated-measurement empirical audit of 20 third-party LLM API
  relays, finding behavioral divergence from the official API, disabled
  tools still firing, and token-count discrepancies — quantified evidence a
  builder sourcing models through a relay/router needs, distinct from this
  library's existing router-cost and relay-fraud entries.
---

# What the Middleman Delivers: Answer Behavior, Tool Permissions, and Billed Usage in LLM API Relays

## Summary

The paper audits 20 third-party LLM API relays advertising access to GPT-6
Astra and Claude Opus 5. In a first round, comparing relay answers to
official-API answers on knowledge questions flagged behavioral differences in
7 of 10 low-priced relays and 2 of 10 relays priced at or above the official
rate; retesting 35 of the flagged pairs changed several of the flags
(unverified beyond the authors' own retest: the instability of the flags
across retest rounds is reported but not independently reproduced here).
Across 3,332 screened responses, no prompt injection was confirmed, but four
relays returned tool calls even when the corresponding tools had been
disabled by the caller. For identical requests, five relays reported 4,200 to
60,000 more input tokens than the official API; for the six services with
available account balances, the charges matched the (inflated) reported
usage. The authors conclude that advertised model identity and price are not
enough to judge a relay's reliability, and that evaluation needs repeated
measurement rather than a single pass.

## Why it matters

Direct, quantified evidence for anyone sourcing models through a third-party
relay or router (a increasingly common pattern for cost or availability
reasons): relays can silently ignore a disabled-tool instruction and can
over-report token usage in a way that inflates the bill, not just
occasionally misquote the model's answers. This complements, rather than
duplicates, this library's existing entries on router cost/latency overhead
and relay-market fraud — this is a controlled behavioral and billing audit,
not a cost-overhead measurement or a journalistic account.

## Verification notes

Read directly from the arXiv abstract page (arxiv.org, allowlisted); the
source enforces a 125-character verbatim-quote limit, so the summary above
paraphrases. All claims, including the quantified figures (7/10, 4 of 20
relays firing disabled tools, the token-count ranges), are traced directly to
the abstract; no load-bearing claim here depends on information beyond it.
The full paper (224 KB) and its underlying response logs were not
independently fetched. Single version (v1, 5 Nov 2026).

## Updates

None yet.

## Related entries

[2026-fu-sidel-router-injection](2026-fu-sidel-router-injection.md) — related theme (cost/behavior of third-party API routing), independent study, not the same development.
[2026-willison-token-relay-market-fraud](2026-willison-token-relay-market-fraud.md) — related theme (token relay market), independent source and method, not the same development.
