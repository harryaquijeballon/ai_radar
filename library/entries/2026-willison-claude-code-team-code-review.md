---
slug: 2026-willison-claude-code-team-code-review
title: "How the Claude Code Team Does Code Review"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Oct/16/code-review/
canonical_ids: []
publisher_or_author: "Addy Osmani, Morgan Westlee Lunt, Qing Wang (quoted via Simon Willison)"
published: 2026-10-16
captured: 2026-10-17
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Medium on AI-assisted software development (lens 7): a first-party
  practice description (continuous review-while-writing rather than a
  post-hoc gate; the agent reviews/fixes most changes before a human looks)
  relayed verbatim via Willison's trusted-chronicler quoting. No
  quantification, but names a specific, transferable division-of-labor
  pattern distinct from prior code-review entries in this library.
---

# How the Claude Code Team Does Code Review

## Summary

Simon Willison's weblog quotes, on 16 October 2026, a post by Addy Osmani, Morgan Westlee Lunt, and Qing Wang titled "How the Claude Code team does code review" (claude.dev/blog/solving-code-review-at-anthropic/; not independently fetched, see Verification notes). The excerpt makes three claims: (1) "did a human read the code?" is treated as an imprecise proxy for risk — the better question the team asks is what could go wrong with a change and which check, automated or human, should catch it; (2) review now happens continuously while code is written rather than only as a gate after a pull request opens, compared in the quote to "spellcheck while you write"; (3) Claude reviews and fixes most changes at least once before a human is asked to look, catching most routine mistakes and leaving human reviewers time for higher-level questions and closer scrutiny on what remains.

## Why it matters

Names a specific, applicable division-of-labor pattern for teams designing their own AI-assisted review process — shifting review earlier (continuous, in-the-writing-loop) and reserving human attention for an agent-pre-filtered residual, rather than treating "a human looked at the diff" as the risk-reducing step itself. Complements this library's other code-review entries (e.g. 2026-rahman-plausible-is-not-enough-ai-pr-trust, archived the same day) by describing the producing team's own internal process rather than external reviewers' trust calculus.

## Verification notes

Simon Willison's page was fetched directly and the quoted text traced to it. The primary source (claude.dev) is not on `profiles/egress_allowlist.md` for this unattended run and so was not independently fetched; the claims above rely entirely on Willison's quotation, which the library treats as citable commentary in its own right (precedent: other Willison quote-post entries in this library, e.g. 2026-willison-paintnet-direct2d-vibe-coding). No quantified claims are made, so nothing load-bearing is left unverified beyond the quoted text itself. Vendor-adjacent: describes Anthropic's own team's internal practice; read as one team's account, not as validated general practice.

## Updates

None yet.

## Related entries

None yet.
