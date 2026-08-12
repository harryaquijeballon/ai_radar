---
slug: 2026-mcp-spec-2026-07-28-revision
title: "Model Context Protocol specification, 2026-07-28 revision: statelessness, MRTR, and the Tasks extension"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://modelcontextprotocol.io/specification/2026-07-28/changelog
canonical_ids: ["mcp-spec:2026-07-28"]
publisher_or_author: "Model Context Protocol maintainers — official specification"
published: 2026-07-28
captured: 2026-07-30
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on tool use and MCP: this is the primary specification's own
  changelog for a major revision — removing protocol-level sessions,
  making the protocol stateless, replacing server-initiated requests with
  the Multi Round-Trip Requests pattern, and moving Tasks into an
  extension — directly actionable for anyone building or maintaining an
  MCP server or client.
---

# Model Context Protocol specification, 2026-07-28 revision: statelessness, MRTR, and the Tasks extension

## Summary
The Model Context Protocol's official specification changelog documents the changes made in the `2026-07-28` revision relative to the prior `2025-11-25` revision. The major changes: (1) protocol-level sessions and the `Mcp-Session-Id` header are removed from Streamable HTTP — servers needing cross-call state must use explicit, server-minted handles passed as ordinary tool arguments; (2) the protocol becomes stateless — the `initialize`/`notifications/initialized` handshake is removed, and every request instead carries its protocol version and client capabilities in `_meta`, with a new `server/discover` RPC for version/capability advertisement; (3) the HTTP GET endpoint and `resources/subscribe`/`unsubscribe` are replaced by a single long-lived `subscriptions/listen` stream with opt-in notification types; (4) `ping`, `logging/setLevel`, and `notifications/roots/list_changed` are removed, with log level now set per-request; (5) experimental Tasks move out of the core protocol into an official `io.modelcontextprotocol/tasks` extension, replacing blocking `tasks/result` with polling (`tasks/get`) plus `tasks/update`; (6) a new Multi Round-Trip Requests (MRTR) pattern replaces prior server-initiated requests (`roots/list`, `sampling/createMessage`, `elicitation/create`) — servers return an `InputRequiredResult` and clients retry the original request with `inputResponses`; (7) SSE stream resumability (`Last-Event-ID`) is removed — a broken stream requires the client to re-issue the request with a new ID. The changelog also lists minor changes (OpenTelemetry trace-context conventions in `_meta`, required cache-control fields (`ttlMs`, `cacheScope`) on list/read results, deterministic tool ordering for prompt-cache hit rates, authorization/RFC 9207 issuer validation) and deprecations (Roots, Sampling, and Logging features; the HTTP+SSE transport; OAuth Dynamic Client Registration in favor of Client ID Metadata Documents).

## Why it matters
Any team building or maintaining an MCP server or client needs to know this revision removes session state, the initialize handshake, and several methods (`ping`, subscribe/unsubscribe, `roots/list_changed`) that existing integrations may depend on — these are breaking changes with a stated migration path (server-minted handles, `subscriptions/listen`, per-request `_meta` fields). The new MRTR pattern and the Tasks extension redesign are directly relevant to anyone building long-running or interactive tool calls. The stated deprecation of Roots, Sampling, and Logging (12-month window per the new feature-lifecycle policy) is a concrete signal for what to stop building against.

## Verification notes
Source is the official MCP specification changelog page on `modelcontextprotocol.io`, the allowlisted primary domain; fetched directly and all claims above are quoted or closely paraphrased from that changelog text, each change linked to its own SEP/PR number in the source. The specification's own version label dates this revision `2026-07-28`; the announcement blog post lives on `blog.modelcontextprotocol.io`, a subdomain not itself on the egress allowlist (only the bare `modelcontextprotocol.io` domain is listed), so the blog announcement was not fetched and the exact calendar date of public announcement (versus the spec's internal version-date label) is not independently confirmed — this did not surface in this radar's 2026-07-29 run, so it is treated as newly discovered today. No independent third-party corroboration was attempted; the claims describe the specification's own documented changes.

## Updates
None yet.

## Related entries
None yet.
