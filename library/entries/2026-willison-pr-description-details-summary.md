---
slug: 2026-willison-pr-description-details-summary
title: "Hide your slop PR descriptions behind <details><summary>"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Nov/9/details-summary/
canonical_ids: []
publisher_or_author: "Simon Willison — personal weblog"
published: 2026-11-09
captured: 2026-11-15
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  A concrete, transferable PR-review convention for agent-generated code
  review (lens 7): a named mechanism (collapsible details/summary block,
  model/effort label, human-written opener) illustrated with real examples
  from the author's own PRs, not a bare opinion.
verification: verified
---

# Hide your slop PR descriptions behind <details><summary>

## Summary
Simon Willison argues that coding agents (Claude Code, Codex, etc.) write
PR descriptions that are accurate and thorough — and that the thoroughness
itself is the problem: long agent-written explanations are tedious to
read, and a reviewer may suspect the text took more effort to read than it
did to produce.

His proposed convention: put a short, human-written opener at the top of
the PR description (optionally with a screenshot) stating what the PR is
for and why a reviewer should care, then place the full agent-generated
explanation inside a collapsible HTML `<details><summary>` block, labeling
the summary with the model name and effort level (e.g., "Claude Opus 5.5
Medium"). GitHub-flavored Markdown renders this natively, so the detail
stays available without forcing every reviewer to read it.

He illustrates the convention with five of his own recent PRs to the
datasette and llm projects (a redesigned row-detail page, a pagination
bar, deferred loading of a large JS bundle, a new plugin hook, and new CLI
commands), each shown with a one-to-two-sentence human opener.

## Why it matters
A specific, immediately adoptable team practice for reviewing
agent-generated code (lens 7): it names the exact mechanism (collapsible
block + model/effort label + human opener) rather than just asserting that
line-by-line review of agent output is tedious. Any team using coding
agents and GitHub-flavored PR descriptions can apply this directly without
tooling changes.

## Verification notes
Fetched simonwillison.net's post directly and traced every claim above —
the argument, the recommended markup, the model/effort labeling
convention, and the five illustrative PR examples — to the post's text.
No load-bearing quantified claim is made (this is a practice
recommendation, not an empirical result), so no further corroboration was
sought.

## Updates
None yet.

## Related entries
None yet.
