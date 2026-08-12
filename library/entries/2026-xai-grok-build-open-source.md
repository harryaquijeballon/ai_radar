---
slug: 2026-xai-grok-build-open-source
title: "grok-build: open-sourced terminal AI coding agent (Rust)"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://github.com/xai-org/grok-build
canonical_ids: ["repo:xai-org/grok-build"]
publisher_or_author: "xAI — GitHub repository (Apache-2.0)"
published: 2026-07-15
captured: 2026-07-22
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on the agent-architecture and harness lenses: a full production coding
  agent released as source — TUI, agent runtime (leader/stdio/headless), tool
  implementations, sandboxing, MCP support, checkpoints. A rare readable
  reference implementation of a real harness. Discovered in the 15–22 Jul
  2026 window via the Simon Willison curated source.
---

# grok-build: open-sourced terminal AI coding agent (Rust)

## Summary

xAI's terminal-based AI coding agent, released as source on GitHub (surfaced 15 July 2026). Per the repository README, it "runs as a full-screen TUI that understands your codebase, edits files, executes shell commands, searches the web, and manages long-running tasks." The Rust codebase (multi-crate workspace) includes the TUI layer, an agent runtime with leader/stdio/headless entry points, tool implementations (terminal, file editing, search), workspace management with VCS and checkpoints, MCP support, and sandboxing utilities; licensed Apache-2.0 for first-party code, with external contributions not accepted.

## Why it matters

*(Radar's assessment.)* A working, readable harness to study rather than a blog post about one: the leader/stdio/headless runtime split, checkpointing, sandboxing, and MCP integration are exactly the harness-engineering concerns behind reliable agentic products. Useful as a concrete architecture reference when designing an agent for research/policy workflows.

## Verification notes

Repository README fetched and read: description, primary language (Rust), component layout, MCP/sandboxing presence, and Apache-2.0 licence all traced to the repo. **Provenance caveat / correction to secondary coverage:** Simon Willison's link-blog framed the release as following a privacy incident (directory-upload); the repository itself documents *no* such reason, and this entry does not assert it — the open-sourcing rationale is unconfirmed. Release date approximate (repo shows no formal release; 15 July is the surfacing date). Not run or audited; claims are about the stated contents, not verified behavior.

## Updates

*(none yet)*

## Related entries

[2026-google-kaggle-new-sdlc-vibe-coding.md](2026-google-kaggle-new-sdlc-vibe-coding.md) — the "harness is most of the capability" thesis this codebase concretely embodies.
