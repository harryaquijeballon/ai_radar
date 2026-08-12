---
slug: 2026-singh-illusion-secure-llm-code
title: "The Illusion of Secure LLM Code: Closing the Security Gap via Iterative Reprompting"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.23710
canonical_ids: ["arxiv:2607.23710"]
publisher_or_author: "Ishpuneet Singh, Shreyas Mahajan, Gurjot Singh, Maninder Singh — arXiv preprint"
published: 2026-07-26
captured: 2026-07-28
relevance:
  ai_engineering: high
  social_science: n/a
verification: verified
rationale: >-
  High on the AI-assisted software development and security/governance
  lenses: a measured evaluation (five models, four prompting approaches,
  static analysis plus penetration testing mapped to NIST guidelines) of a
  concrete, generalizable failure — AI-generated authentication code omits
  standard protections by default — with a stated, testable mitigation
  (iterative, self-auditing reprompting).
---

# The Illusion of Secure LLM Code: Closing the Security Gap via Iterative Reprompting

## Summary

Evaluates whether AI coding assistants reliably generate secure
authentication systems. Using static analysis and penetration testing
mapped against NIST guidelines, the authors test five prominent models
across four prompting approaches, ranging from generic functional requests
to explicit NIST-based security guidance to iterative "reprompting" that
re-audits and revises the generated code across multiple cycles. Code
generated from purely functional or generically "secure" prompts
consistently omits critical protections, including brute-force defenses
and proper session management, regardless of model. Explicit NIST-based
guidance in the prompt improves matters but is not sufficient on its own;
the paper's central finding is that iterative reprompting — a continuous
self-auditing cycle rather than a single well-crafted prompt — is
necessary to close the gap. The authors conclude that current AI coding
assistants lack secure-by-default behavior for authentication code, and
that enterprises relying on them need ongoing verification processes
rather than one-time prompt engineering.

## Why it matters

A concrete, testable caution and mitigation for any team using AI coding
assistants to generate authentication or other security-sensitive code:
naive or even security-worded prompts are not enough, and a single
generation pass should not be trusted — the paper gives both the specific
missing protections to check for and a stated process (iterative,
self-auditing reprompting) as a partial fix. Directly usable as a checklist
input for teams building deterministic guardrails around AI-generated
security-relevant code.

## Verification notes

arXiv abstract page fetched directly (2026-07-28); title, full author
list, "Submitted on 26 Jul 2026" confirmed. Every claim in the Summary —
the five-model, four-prompting-approach design, the NIST-mapped
static-analysis-plus-pentesting methodology, the consistent omission of
brute-force and session-management protections, and the iterative-
reprompting finding — traces directly to the fetched abstract text. Full
paper text not read at capture; no independent corroboration attempted
(pre-publication preprint). Upgrade path: read the full paper for the five
tested models' identities and the full list of protections checked.

## Updates

None yet.

## Related entries

None yet.
