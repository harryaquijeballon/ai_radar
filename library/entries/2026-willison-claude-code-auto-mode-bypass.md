---
slug: 2026-willison-claude-code-auto-mode-bypass
title: "Breaking Claude Code Opus 5 Auto Mode"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode/
canonical_ids: []
publisher_or_author: "Simon Willison, relaying research by Johann Rehberger"
published: 2026-08-27
captured: 2026-08-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A concrete, quantified (80% success rate) attack against a shipped
  agent-safety mechanism, with a named failure mode where the classifier
  itself blocks the agent's own remediation — squarely lens 6
  (reproducibility, security and governance) with an actionable mitigation
  (sandbox unattended coding agents).
---

# Breaking Claude Code Opus 5 Auto Mode

## Summary
Security researcher Johann Rehberger found an attack against Claude Code's
"Auto Mode" — the default safety system meant to protect coding agents
against prompt injection — that works roughly 80% of the time. The attack
tricks the agent into summarizing a malicious web page, which leads it to
use `curl` instead of its WebFetch tool to retrieve a page presenting itself
as an archive of notebook records, then to download and decompress a zip
archive and execute code that imports `base64`. That import inadvertently
loads a malicious local `struct.py` file extracted from the archive — Python
module shadowing, where a local file sharing a standard-library module's
name is loaded instead of the real module. In some runs, "Claude detects the
compromise, but Auto Mode blocks its cleanup command": the safety classifier
allowed the malware process to start but then blocked the command intended
to stop it. Willison quotes the finding directly: "The safety mechanism
itself can become part of the failure."

## Why it matters
A concrete, named failure mode for anyone relying on a vendor's built-in
agent-safety classifier as the sole defense against prompt injection and
tool misuse: the classifier's own action-blocking behavior can prevent
recovery once compromised. The stated mitigation — running unattended coding
agents in sandboxed environments (containers, VMs, or OS-level sandboxes)
with restricted network egress, monitoring, and isolated credentials — is a
directly applicable control for anyone building or deploying autonomous
coding agents.

## Verification notes
Fetched directly from simonwillison.net (allowlisted). Quoted passages
("Claude detects the compromise, but Auto Mode blocks its cleanup command";
"The safety mechanism itself can become part of the failure") confirmed
against the fetched source text, as was the 80% success-rate figure and the
zip/module-shadowing attack chain. The underlying finding is Johann
Rehberger's, relayed via Willison's post rather than fetched from
Rehberger's own write-up directly — labelled accordingly; Willison is
established in this profile as a high-signal, sceptical relay of exactly
this kind of research.

## Updates
None yet.

## Related entries
[2026-willison-ai-accelerated-exploit-disclosure](2026-willison-ai-accelerated-exploit-disclosure.md) — same day, same author, complementary evidence of coding-agent-driven security dynamics (a specific defense failure in this entry, offense in that one).
