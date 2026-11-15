---
slug: 2026-willison-claude-fable-ownership-prompting
title: "Prompting Claude Fable 5.2 (on code-ownership framing)"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Nov/10/prompting-claude-fable-52/
canonical_ids: []
publisher_or_author: "Simon Willison, quoting Anthropic's Claude Fable 5.2 prompting documentation"
published: 2026-11-10
captured: 2026-11-15
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  Names a specific, quantified prompt-engineering mechanism (framing code
  ownership) with a large reported effect on a concrete coding-agent
  behavior — clears ai_engineering lens 2 (harness and context engineering)
  at high: a mechanism named, with a stated condition for when to use it.
---

# Prompting Claude Fable 5.2 (on code-ownership framing)

## Summary
Simon Willison relays an excerpt from Anthropic's own prompting
documentation for Claude Fable 5.2. The documented finding: the model's
behaviour on coding tasks depends on who the prompt says owns the
codebase. When the prompt is silent on ownership, or frames the codebase as
someone else's, the model tends to add to the existing structure even when
doing so duplicates code. When the prompt explicitly states the model is
the codebase's owner and long-term maintainer, it more often consolidates
duplicated code and sometimes makes related fixes unprompted.

The documented technique is a single suggested sentence to add to a
system/task prompt: "You are the owner and long-term maintainer of this
codebase, and its design is up to you." Anthropic's own testing on small
coding tasks reportedly found the model consolidated duplicated code in
under 10% of runs without that sentence, versus about 75% of runs with it
(unverified beyond the quoted figures: the underlying test suite, sample
size, and task definitions are not given in the material fetched).

## Why it matters
A concrete, low-cost prompt-design lever for teams running coding agents
(Claude Code or similar) on any codebase they intend the agent to steward
over multiple sessions: stating ownership/maintainer framing explicitly
appears to shift the model from narrow task completion toward
consolidation and codebase-level judgment. Directly actionable this
quarter for harness/system-prompt design (lens 2), and relevant to
AI-assisted software development practice (lens 7) wherever duplicated
code from repeated agent sessions is a known failure mode.

## Verification notes
Fetched simonwillison.net's post directly; the summary above traces to its
quoted text of Anthropic's documentation, including the exact suggested
sentence and the ~10%/~75% figures. The primary source (Anthropic's Claude
Fable 5.2 prompting documentation, on docs.claude.com or similar) is not on
`profiles/egress_allowlist.md` and could not be fetched directly to
corroborate the figures against the original document or to see the
underlying test methodology — verification is partial on that basis. No
other claim in this entry is load-bearing beyond the two reported
percentages.

## Updates
None yet.

## Related entries
None yet.
