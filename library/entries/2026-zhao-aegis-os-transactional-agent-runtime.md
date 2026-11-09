---
slug: 2026-zhao-aegis-os-transactional-agent-runtime
title: "Aegis OS: A Transactional Multi-Tenant Operating System Runtime for Eliminating Authorization Fatigue in Autonomous Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.08516
canonical_ids: ["arxiv:2611.08516"]
publisher_or_author: "Hui Zhao — Heurion Research"
published: 2026-10-22
captured: 2026-11-09
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on reproducibility/security (lens 6) and agent architecture (lens 1):
  moves the authorization boundary from per-tool-call confirmation to a
  kernel-enforced transactional workspace, with quantified before/after
  evaluation across both controlled and real agent sessions — a concrete,
  measured architectural fix for a named, widely felt problem (confirmation
  fatigue vs. unrestricted credential exposure).
---

# Aegis OS: A Transactional Multi-Tenant Operating System Runtime for Eliminating Authorization Fatigue in Autonomous Coding Agents

## Summary

Autonomous coding agents (Google Antigravity, Claude Code, OpenAI Codex CLI) force a choice between per-action confirmation — which the paper reports interrupts roughly 45-57% of tool calls, causing approval fatigue — and unrestricted operation, which exposes host files, SSH/cloud credentials, and API tokens to prompt injection and hallucinated actions. Concurrent agents sharing a working tree also overwrite each other's edits, and routing large artifacts through the model's context window adds token cost.

Aegis OS is a transactional, multi-tenant agent runtime in Rust, exposed over MCP and Google's A2A protocol. Instead of authorizing individual tool calls, it places the authorization boundary around a transactional workspace: each agent runs in a kernel-enforced, deny-by-default sandbox (macOS Seatbelt or Linux Bubblewrap), works on copy-on-write shadow workspaces, and reaches external resources only through an identity-pinned egress proxy that injects secrets by method/path while applying outbound data-loss prevention. An A2A inter-process messaging bus uses content-addressable storage for cross-agent handoffs.

Evaluated across 1,500 controlled calls and 28,087 real calls from 52 coding-agent sessions: confirmation prompts fell 94.19-99.88% in controlled tests and 90.7-97.9% in real sessions; attack success fell from 100% to 0% across 80 attacks in eight categories on both macOS and Linux; cloning a 1,000-file repository into a shadow workspace took 6.3ms (APFS) / 15.6ms (btrfs); the system detected all 10 syntactic/semantic merge conflicts tested.

## Why it matters

Gives builders a concrete, measured alternative to the binary choice between constant confirmation prompts and unrestricted agent access — directly applicable to anyone running coding agents with real filesystem/credential access, including agentic research or policy-simulation pipelines that need both throughput and a defensible security boundary. The copy-on-write shadow-workspace mechanism and the identity-pinned egress proxy are specific, reusable patterns, not just a general warning about agent security.

## Verification notes

Fetched the arXiv abstract page directly; claims above (interruption-rate figures, evaluation counts, quantified reductions) are as stated in the abstract. The paper is single-author (independent research lab), with v1 submitted 2026-10-22 — load-bearing quantified claims (the 94-99% prompt reduction, 100%→0% attack success) are as reported by the source and have not been independently replicated; this is the author's own evaluation of their own system, a single-paper result not yet corroborated by a third party.

## Updates

None yet.

## Related entries

- [2026-reid-risks-controls-multiagent-boundaries](2026-reid-risks-controls-multiagent-boundaries.md) — a governance-framework treatment of the same cross-organizational-boundary agent-security problem this runtime addresses mechanically.
- [2026-tran-agent-security-networking-problem](2026-tran-agent-security-networking-problem.md) — reframes agent security as a networking problem; Aegis OS's egress proxy is one concrete instantiation of that framing.
