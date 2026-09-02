---
slug: 2026-willison-paintnet-direct2d-vibe-coding
title: "A quote from Rick Brewster (Paint.NET's from-scratch Direct2D rewrite)"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Sep/2/rick-brewster/
canonical_ids: []
publisher_or_author: "Simon Willison, quoting Rick Brewster (Paint.NET author)"
published: 2026-09-02
captured: 2026-09-02
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  A quantified, real-world case of large-scale (180,000-line) agent-generated
  code — a clean-room reverse-engineered Direct2D reimplementation — with a
  named practical limitation (needed human supervision specifically for
  resource management and architecture decisions) directly on lens 7
  (AI-assisted software development); a single unvalidated anecdote rather
  than a study, so medium rather than high.
---

# A quote from Rick Brewster (Paint.NET's from-scratch Direct2D rewrite)

## Summary
Rick Brewster, creator of the Windows image editor Paint.NET, announced on
the Paint.NET forums that the project now has "an internal, from-scratch,
clean-room reverse-engineered rewrite of Direct2D that it uses on WINE" (the
Windows-compatibility layer for Linux), living in
`PaintDotNet.Windows.Direct2D1.Managed.dll`. Per Willison's relay, the
implementation is roughly 180,000 lines of code and was substantially "vibe
coded" by Claude — written without the thorough line-by-line review Brewster
would normally apply. Brewster reports having to intervene repeatedly to fix
COM resource-management issues and architectural decisions, while describing
Claude's reverse-engineering of Direct2D's effects-library formulas as
impressive (unverified: the specific formulas and defects are not quoted in
detail in Willison's relay).

## Why it matters
A concrete, named data point on where heavily agent-generated code holds up
and where it doesn't at real scale: a 180k-line clean-room reimplementation
of a complex graphics API is reported as achievable substantially through
agent coding, but the author-supervised failure modes were specific and
recurring — resource lifecycle management (COM reference counting) and
higher-level architecture — rather than the low-level reverse-engineering
work, which the agent reportedly handled well. For anyone weighing how much
oversight to budget for large agent-driven code-generation efforts, this is
a specific, named split (architecture/resource-management needs supervision;
algorithmic reverse-engineering may not) rather than a generic "review
everything" caution.

## Verification notes
Fetched directly from simonwillison.net (allowlisted): confirmed the
publication date/time (2026-09-02, 05:50), the quoted line ("an internal,
from-scratch, clean-room reverse-engineered rewrite of Direct2D..."), the
180,000-line figure, and the "vibe coded" characterization against the
fetched source text. The primary source — Brewster's own forum post at
forums.paint.net — is not on the egress allowlist and could not be fetched
independently this run, so the underlying claims are traced only to
Willison's quoted relay, not corroborated against Brewster's full original
post. Willison is an established high-signal relay for this project
(profiles/ai_engineering/sources.md); treated as partial verification
because the primary source is unreachable, not because the relay itself is
doubted.

## Updates
None yet.

## Related entries
None yet.
