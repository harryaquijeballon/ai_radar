---
slug: 2026-fabrega-governing-delegation-genai
title: "Governing Delegation to Generative Artificial Intelligence: Human Direction, Work-Related Orientation, and Modes of Use"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.17624
canonical_ids: ["arxiv:2608.17624"]
publisher_or_author: "Jorge Fábrega"
published: 2026-08-18
captured: 2026-08-19
relevance:
  social_science: high
  ai_engineering: medium
verification: partial
rationale: >-
  Cross-domain: squarely on social-science lens 1/6 (AI-and-productivity,
  regulation/governance of AI use) with a usable empirical distinction
  (specified delegation vs. iterative coproduction) measured against real
  usage-mode data; on ai_engineering lens 6 (governance for institutional
  use) as a measurement approach for where human direction leaves
  observable evidence. Uses first-party Anthropic usage data — see the
  vendor-source caveat below.
---

# Governing Delegation to Generative Artificial Intelligence: Human Direction, Work-Related Orientation, and Modes of Use

## Summary

The paper examines how delegating cognitive tasks to generative AI raises
governance questions about maintaining human direction. It distinguishes
"specified delegation," where instructions precede execution, from
"iterative coproduction," where human guidance occurs during production.
Using Anthropic Economic Index data for April-May 2026, it analyzes two
usage modes — direct API access and Claude.ai (Chat and Cowork combined).
Work-oriented use correlates with greater specified delegation in both
modes, more strongly in API usage; iterative-coproduction responses differ
between modes, such that "the observable iterative response varies across
modes of use." The paper argues for measuring when human direction leaves
measurable evidence rather than focusing solely on task-execution volume
(unverified in detail — the full regression specification and sample
construction not read beyond the abstract).

**Vendor-source caveat:** the usage data is Anthropic's own first-party
Economic Index, describing Claude's user base and usage patterns first and
generative-AI-delegation behavior generally only by inference — the same
caveat this library already applies to Google's ATLAS series
([2026-google-atlas-gemini-economy-mapping](2026-google-atlas-gemini-economy-mapping.md)).

## Why it matters

**For social_science:** gives a usable conceptual and empirical split
(specified delegation vs. iterative coproduction) for studying how
governance and oversight of AI use might actually be measured — via
observable directional evidence rather than raw usage volume — directly
applicable to research or policy work on AI-use governance and workplace
AI adoption (lenses 1, 4, 6).

**For ai_engineering:** a measurement framing — where does human direction
leave observable evidence across a delegation interaction — that is
relevant to designing audit trails or oversight logging for institutional
agentic-AI deployments (lens 6), though the paper is a usage-pattern study,
not a systems/control proposal.

## Verification notes

Source is the arXiv abstract page; full PDF not fetched. The two-mode
distinction, the April-May 2026 Anthropic Economic Index data source, and
the directional-correlation findings are traced to the abstract, including
direct quotes. The regression specification, sample size, and full results
table were not independently corroborated — hence partial verification.
The vendor-source caveat is a judgment call from this radar's profile
guidance, not from the paper itself.

## Updates

- **2026-08-19** — Entry created from arXiv abstract during the daily scan.

## Related entries

- [2026-google-atlas-gemini-economy-mapping](2026-google-atlas-gemini-economy-mapping.md) — same vendor-source-caveat pattern (first-party usage data).
