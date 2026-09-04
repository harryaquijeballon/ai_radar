---
slug: 2026-runkle-langchain-mcp-stateless-elicitation
title: "MCP in LangChain: Stateless Protocol, Elicitation, and More!"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://langchain.com/blog/mcp-in-langchain-stateless-protocol-elicitation-and-more
canonical_ids: []
publisher_or_author: "Sydney Runkle — LangChain blog"
published: 2026-09-03
captured: 2026-09-04
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  On-lens (3: tool use and MCP) integration update bringing MCP's July 2026
  stateless-protocol and elicitation features into LangChain's main package;
  vendor-authored and discounted accordingly per
  profiles/ai_engineering/sources.md's framework-vendor policy.
---

# MCP in LangChain: Stateless Protocol, Elicitation, and More!

## Summary
The post announces LangChain's adoption of the Model Context Protocol's July 2026 specification revision (already covered in this library as `2026-mcp-spec-2026-07-28-revision`): MCP support moves into LangChain's main package, built on FastMCP infrastructure, adding elicitation and client-side caching. Under the old session-based protocol, clients had to open a session and maintain a session ID per request; the stateless design removes this, so "a redeploy no longer kills live sessions, because there are none." Elicitation lets a tool pause mid-execution to request information without holding a connection open; LangChain surfaces this as a "LangGraph interrupt," enabling human-in-the-loop confirmation or parameter-collection workflows. Client-side caching lets servers specify how long tool catalogs stay fresh, avoiding redundant discovery calls. The post cites MCP SDK adoption figures: "pulling close to half a billion downloads a month," and "MCP tool calls from ChatGPT users are up 98x across 2026."

## Why it matters
This profile's lens 3 rates interoperable, reusable integration knowledge highly. A first-party account of how a major agent framework maps a protocol-level change (statelessness, elicitation) onto concrete developer-facing primitives (a LangGraph interrupt for human review, cache-control for tool catalogs) is directly usable by anyone building or maintaining MCP-based tool integrations, independent of whether LangChain itself is the chosen framework.

## Verification notes
Fetched and read directly from the LangChain blog post. The technical description of statelessness, elicitation, and caching, and the framing of elicitation as a LangGraph interrupt, are traceable to the post's own text and match the previously-archived MCP spec revision. The adoption figures (half a billion downloads/month, 98x growth in ChatGPT tool calls) are LangChain/Anthropic-ecosystem self-reported statistics with no independent source cited, so verification is recorded as `partial`; per the vendor-framework discount in `profiles/ai_engineering/sources.md`, relevance is `medium` rather than `high` despite being on-lens.

## Updates
None yet.

## Related entries
[2026-mcp-spec-2026-07-28-revision](2026-mcp-spec-2026-07-28-revision.md) — the underlying MCP specification revision this post integrates.
