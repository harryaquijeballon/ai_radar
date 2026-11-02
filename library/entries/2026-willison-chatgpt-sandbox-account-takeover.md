---
slug: 2026-willison-chatgpt-sandbox-account-takeover
title: "How We Took Over ChatGPT Accounts (Parameter Labs sandbox-escape writeup)"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Oct/31/how-we-took-over-chatgpt-accounts/
canonical_ids: []
publisher_or_author: "Simon Willison, relaying Parameter Labs — simonwillison.net"
published: 2026-10-31
captured: 2026-11-02
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on reproducibility, security and governance (lens 6): a concrete,
  disclosed cross-frame sandbox-escape chain against a production sandboxed
  code-execution feature (ChatGPT's HTML-preview iframe), with a specific,
  checkable root cause (an unrestricted postMessage handler using innerHTML,
  plus a CSP allowlist entry reflecting attacker JS) and a named fix. A
  transferable, concrete lesson for anyone building sandboxed tool-use or
  code-execution features for agents, not a general warning about
  sandboxing.
---

# How We Took Over ChatGPT Accounts (Parameter Labs sandbox-escape writeup)

## Summary

Simon Willison's link-blog post (31 Oct 2026, found via Hacker News)
relays a Parameter Labs writeup, "We found a gap at OpenAI" (parameter.ai/labs), 
describing an exploit chain against ChatGPT's sandboxed HTML-preview
("Canvas") feature, where user-authored HTML apps run inside a sandboxed
iframe. ChatGPT uses the MathLive JavaScript library for graph rendering;
MathLive's virtual keyboard can be triggered via `postMessage()` from a
sandboxed iframe, and nothing restricted which sandboxed frames —
including the untrusted HTML-preview frame — could send that message. The
keyboard's message handler used `innerHTML`, letting untrusted code inject
HTML into the parent page, including an iframe without sandbox
restrictions. The injected code could not directly execute scripts via
`innerHTML`, but ChatGPT's Content Security Policy allowed script loading
from a short list of domains that included YouTube, and the YouTube
oEmbed endpoint could be made to reflect attacker JavaScript in a way that
executed. Once running with page-level JavaScript access, the attacker
could fetch private user data from ChatGPT's own APIs and exfiltrate it
via an image reference; a malicious shared ChatGPT conversation URL could
expose another signed-in visitor's data or let the attacker act under
their account. OpenAI fixed the issue and paid a $5,000 bug bounty, which
Willison characterizes as low for a vulnerability of this severity (all
details as stated in Willison's post; the primary Parameter Labs writeup
was not independently fetched at capture).

## Why it matters

A specific, named failure mode for anyone building sandboxed code-execution
or tool-use features into an AI product: sandbox isolation (the iframe
`sandbox` attribute) was not the weak point — a shared, loosely-restricted
cross-frame messaging channel (an unrelated UI library's `postMessage`
handler) and an overly broad CSP allowlist entry (a third-party domain
that can be made to reflect arbitrary script) combined to defeat it. The
lesson generalizes directly to agent harnesses that embed sandboxed
browser or code-execution surfaces: audit every `postMessage` receiver
reachable from an untrusted frame, and treat every CSP-allowlisted
third-party domain as a potential script-execution vector, not just a
content source.

## Verification notes

Willison's post fetched directly (captured 2026-11-02; published 31 Oct
2026). The MathLive/postMessage/innerHTML mechanism, the CSP-plus-YouTube-
oEmbed bypass, the private-data exfiltration path via shared-URL visits,
and the $5,000 bounty figure all trace to the fetched post, which itself
summarizes the primary Parameter Labs writeup (parameter.ai/labs,
"We found a gap at OpenAI") — not independently fetched at capture, since
parameter.ai is not on `profiles/egress_allowlist.md`. `partial` rather
than `verified`: the headline technical claims are traced to Willison's
summary of the primary source but not corroborated against the primary
writeup itself. Upgrade path: fetch parameter.ai/labs directly once
allowlisted, or have a human confirm the exploit chain against the
primary writeup.

## Updates

None yet.

## Related entries

None yet.
