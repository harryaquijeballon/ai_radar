---
slug: 2026-anthropic-discovering-vulnerabilities-claude
title: "Discovering and Exploiting Vulnerabilities in Critical, Real-World Software with Claude"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://www.anthropic.com/research/discovering-vulnerabilities-with-claude
canonical_ids: []
publisher_or_author: "Anthropic Frontier Red Team"
published: 2026-10-27
captured: 2026-10-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on reproducibility, security and governance (lens 6): a named,
  quantified capability demonstration (62 CVEs across a full exploit
  chain in a major browser, plus OS/kernel-level chains) that comes with
  an operational lesson set (parallel scanning agents, per-scanner
  contribution measurement, automated variant analysis, PR-time scanning)
  directly transferable to building AI-assisted security tooling. Vendor
  source: Anthropic has a direct stake in Claude's perceived offensive
  capability; scored on the disclosed methodology and named limits, not
  the headline.
---

# Discovering and Exploiting Vulnerabilities in Critical, Real-World Software with Claude

## Summary

Anthropic's Frontier Red Team used an unreleased internal research model
to find and chain exploitable vulnerabilities in widely used browsers and
operating systems, reporting all findings under coordinated disclosure
(90 days to patch, 45 more before discussing details beyond public
advisories). Reported chains: a four-stage Chrome (macOS) chain —V8 heap
corruption, a V8 sandbox escape defeating ASLR, a CacheStorage race
condition, and a FedCM use-after-free — achieving code execution outside
the sandbox; a Safari data-only chain combining a JavaScriptCore
use-after-free, a Gigacage bypass, an IPC sandbox flaw, and an overwritten
flag that disabled the same-origin policy; an Android chain (source
analysis, reverse-engineered Google Play services binaries, live testing
on a Pixel 9) chaining three vulnerabilities to extract data from a
locked phone over USB; a Windows chain found via binary reverse
engineering (Claude rebuilt an annotated C reproduction of the binary
using tools like Ghidra and compared behavior); and a zero-click Linux
chain using a networking-stack race-condition use-after-free to defeat
remote KASLR and hijack control flow.

Quantified results: 62 CVEs assigned and patched in Chrome as of version
156 (all critical/high severity, including 13 sandbox escapes and 21
renderer-compromise bugs); a Windows kernel QUIC out-of-bounds read
(CVE-2026-33096) Anthropic estimates could affect "several million"
internet-facing servers (a denial-of-service, not code execution); a
Linux kernel bug (CVE-2026-98432) whose proof of concept took 48 minutes
to leak a kernel pointer and about 5 more minutes to reach command
execution; Apple acknowledged the Safari report the same day it was
submitted. Stated lessons: run many scanning agents in parallel, measure
each scanner's unique contribution, use automated variant analysis, and
scan at pull-request time.

## Why it matters

A concrete, named operational playbook for building AI-assisted security
scanning — parallel agents, per-scanner contribution tracking, variant
analysis, PR-time scanning — alongside a quantified capability baseline
(62 Chrome CVEs, multi-platform exploit chains) useful for governance and
risk-assessment conversations about what frontier models can currently
do unassisted on real, deployed software. The page's own caveats matter
as much as the headline: the Windows finding is a DoS, not RCE; the
Linux PoC is slow and race-dependent; the Android chain assumed physical
access to one locked device model; and the degree of human involvement
("after initial prompting") is not fully quantified, so the demonstrated
chains should not be read as fully autonomous end-to-end discovery.

## Verification notes

Read in full via direct fetch of the Anthropic research page (captured
2026-10-29; published 2026-10-27; contributor list, the five platform
chains, and all quantified figures — 62 Chrome CVEs, 13 sandbox escapes,
21 renderer-compromise bugs, CVE-2026-33096, CVE-2026-98432, the 48+5
minute PoC timing, same-day Apple acknowledgment — are stated directly on
the primary source page, not relayed through a third party. The page's
own stated limits (DoS vs. RCE distinction for the Windows bug, race-
dependence of the Linux PoC, single-device Android demonstration,
unquantified human involvement) are preserved here. Independent
corroboration beyond the vendor's own page was not attempted this run;
Anthropic has a direct stake in Claude's perceived offensive-security
capability.

## Updates

None yet.

## Related entries

[2026-anthropic-theorem-formal-verification-scale](2026-anthropic-theorem-formal-verification-scale.md) — same team (Anthropic Frontier Red Team), published five days apart: one applies Claude to defensive formal verification, this one to offensive vulnerability discovery.
