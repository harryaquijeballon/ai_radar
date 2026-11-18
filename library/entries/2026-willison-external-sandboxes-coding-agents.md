---
slug: 2026-willison-external-sandboxes-coding-agents
title: "External sandboxes for coding agents"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Nov/17/external-sandboxes-for-coding-agents/
canonical_ids: ["repo:prime-radiant-inc/external-sandbox-v86", "repo:prime-radiant-inc/external-sandbox-container", "repo:prime-radiant-inc/external-sandbox-quicksand"]
publisher_or_author: "Simon Willison, with Prime Radiant"
published: 2026-11-17
captured: 2026-11-18
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance): a concrete,
  working sandboxing pattern — code execution kept outside the agent process,
  with network allow-listing and credential replacement — shipped as three
  interoperable reference implementations a builder could adopt directly.
---

# External sandboxes for coding agents

## Summary

Simon Willison, working with Prime Radiant (the AI research lab behind
Superpowers), describes and releases an "external sandbox" pattern for
coding agents: code the agent wants to execute runs in a separate sandbox
process, while the agent itself never runs code directly on the host. The
stated goal is letting people experiment with local/open models without
risking host-machine damage from a mistake or a prompt injection. Three
sandbox server implementations are released, all exposing the same localhost
API so that Pi, Claude Code, or Codex can point at any of them:
`external-sandbox-v86` (Node.js, runs Alpine Linux in WebAssembly via the
v86 emulator), `external-sandbox-container` (Python, runs Alpine Linux in
Apple's Containers framework), and `external-sandbox-quicksand` (Python,
built on Microsoft's Quicksand library, which bundles QEMU and Alpine). Each
sandbox supports an optional HTTP/HTTPS allow-list proxy restricting which
hosts the executed code can reach, plus a credential-replacement mechanism
so authenticated API calls can be made without exposing the secret to the
agent. A web UI shows the current proxy policy and lets it be edited live.
Willison says he remains "fascinated by the challenge of safely running
untrusted code" and frames this as a way to experiment with different
sandboxing approaches side by side.

## Why it matters

Gives anyone building or hardening a coding agent a direct, working
alternative to running agent-generated code in-process or in a shared
container: three drop-in sandbox servers behind one API, each with different
isolation technology (software CPU emulation, OS-level containers, or a full
VM), so a team can pick the isolation/performance trade-off that fits without
rewriting their agent's execution interface. The allow-list proxy and
credential-replacement mechanism are directly reusable primitives for
containing prompt-injection and tool-abuse risk in any agent that executes
model-written code.

## Verification notes

Fetched simonwillison.net directly (on the egress allowlist) and read the
full post text, including its outbound links. All claims above are traced to
that text. The underlying Prime Radiant post (blog.primeradiant.com) and the
GitHub repositories are linked but were not independently fetched — github.com
is reachable but was not needed to corroborate Willison's own description,
which is first-hand (he states he worked on the release). No benchmark or
formal security analysis is claimed by the post itself, so none is reported
here as verified.

## Updates

None yet.

## Related entries

None yet.
