---
slug: 2026-willison-datasette-apps-agent-self-testing
title: "Release: datasette-apps 0.2a0"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://simonwillison.net/2026/Aug/1/datasette-apps/
canonical_ids: []
publisher_or_author: "Simon Willison — simonwillison.net (datasette-apps project)"
published: 2026-08-01
captured: 2026-08-03
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on agent architecture/tool use (lenses 1, 3): a concrete, shipped
  pattern for letting an agent test its own generated changes — an invisible
  sandboxed iframe plus a paired discovery tool — that a builder could apply
  directly to reduce validation gaps in agent-driven code generation.
---

# Release: datasette-apps 0.2a0

## Summary

Simon Willison's release note for datasette-apps 0.2a0, an extension that
lets applications run inside Datasette (his data analysis/visualization
tool). The release adds two tools for the Datasette Agent: `app_debug()`,
which renders an app in a hidden iframe (`opacity: 0`, `pointer-events:
none`) and executes JavaScript inside that sandbox so the agent can smoke-test
the app and measure elements without any visible side effect, and
`app_list()`, which lets the agent discover and list editable apps so it can
find and modify them automatically. The `app_debug()` tool builds on the
`context.browser_task()` mechanism from datasette-agent 0.4a0.

## Why it matters

A directly reusable pattern for agent tool design: give a code-generating or
app-editing agent a matched pair of tools — one to discover what it can act
on (`app_list()`), one to invisibly execute and verify its own output
(`app_debug()`) — so the agent can validate a change before reporting it
done, rather than emitting unverified code. Applicable to any harness where
an agent edits and must self-check UI-producing artifacts, not just Datasette
specifically.

## Verification notes

simonwillison.net fetched directly (2026-08-03); the release date (1 August
2026, 9:23pm), the two named tools (`app_debug()`, `app_list()`), the
sandboxing mechanism (invisible iframe, JS execution), and the dependency on
`context.browser_task()` from datasette-agent 0.4a0 all trace to the fetched
page. No load-bearing claim outside the source text.

## Updates

None yet.

## Related entries

None yet.
