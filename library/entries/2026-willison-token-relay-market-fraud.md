---
slug: 2026-willison-token-relay-market-fraud
title: "An Inside Look at the Relay Market Powering Token Resellers and Fraud"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Jul/26/relay-market/
canonical_ids: []
publisher_or_author: "Simon Willison, summarizing an investigation by Matt Lenhard — simonwillison.net"
published: 2026-07-26
captured: 2026-07-27
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on the reproducibility/security/governance lens: a concrete threat
  model (open-source LLM API proxies — one-api, new-api — repurposed to
  pool stolen/abused credentials and resell discounted token access) with a
  specific, actionable control (strict, auto-terminating API key spend
  caps). Verification is partial rather than verified: Simon Willison's own
  page was fetched directly, but the underlying investigation it summarizes
  (by Matt Lenhard, apparently hosted off the egress allowlist) could not
  be independently fetched or corroborated this run.
---

# An Inside Look at the Relay Market Powering Token Resellers and Fraud

## Summary

Simon Willison covers an investigation (credited to Matt Lenhard, drawing
on a Chinese-language V2EX forum thread) into a marketplace, concentrated
in China, where LLM API tokens are resold at steep discounts by pooling
credentials. Resellers cut costs by abusing free trial periods, proxying
requests through unprotected support bots, and in some cases using stolen
payment methods or chargeback fraud. The infrastructure runs on two
legitimate open-source API-proxy projects — one-api and its more actively
developed fork new-api — designed for load-balancing across a pool of API
credentials but repurposed here for resale. Buyers are after cheap tokens,
geo-restriction bypass, and in some cases bulk data collection for model
distillation. Willison's own framing: "there's now an entire ecosystem
that can profit from finding a new unprotected endpoint to exploit," and
his stated recommendation is that "LLM vendors really need to get better
at offering strict caps for their API keys," including automated service
termination once a spend threshold is hit within a given period.

## Why it matters

A concrete reminder, with a specific recommended control, that any
publicly reachable LLM-backed endpoint is a target for automated
credential-pooling and resale infrastructure, not just prompt-injection or
jailbreak attacks. The actionable takeaway for anyone operating an API-key-
gated LLM product: enforce strict, time-windowed spend caps with automatic
key termination, rather than trusting rate limits alone.

## Verification notes

simonwillison.net fetched directly (2026-07-27); the quoted mechanisms
(free-trial abuse, unprotected support-bot proxying, stolen-payment/
chargeback fraud, the one-api/new-api tooling, and Willison's own quoted
sentences) all trace to the fetched page. `partial` rather than `verified`:
the underlying investigation's claims (attributed to Matt Lenhard, whose
original piece appears to be hosted off the project's egress allowlist,
e.g. a non-allowlisted blog) were not independently fetched or corroborated
this run — only Willison's summary and direct quotes were confirmed.
Upgrade path: locate and fetch Matt Lenhard's original investigation (once
its host is confirmed reachable or added to the allowlist) to corroborate
the load-bearing claims about the relay market's mechanics.

## Updates

None yet.

## Related entries

None yet.
