---
slug: 2026-mosk-frontier-ai-cyber-defense-glasswing
title: "Does Frontier AI Strengthen Cyber Defense? Evidence from Project Glasswing"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.06629
canonical_ids: ["arxiv:2611.06629"]
publisher_or_author: "Thomas Mosk"
published: 2026-11-04
captured: 2026-11-08
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  High on social_science lenses 4 and 7: a quantified natural-experiment-style
  estimate of what restricted early access to a frontier AI vulnerability-
  finding model does to defenders, researchers, and attackers, directly
  engaging the AI-access-policy and AI-geopolitics debate. Medium on
  ai_engineering lens 6: a real-world governance case of controlled model
  release for security use, though the paper's lens is economic effects, not
  engineering mechanism.
---

# Does Frontier AI Strengthen Cyber Defense? Evidence from Project Glasswing

## Summary

Studies the effects of early, restricted access to "Claude Mythos Preview," a
frontier AI model for finding software vulnerabilities, granted to a small
group of large US tech firms through Project Glasswing. Using all publicly
disclosed vulnerabilities, the author finds: firms with access more than
doubled their vulnerability disclosures compared with Chinese and Russian
tech firms without access, and disclosed about 150% more high-impact
vulnerabilities, with no change in how fast they fixed reported flaws.
External bug-bounty researchers, in response, reported about half as many
vulnerabilities in access-firms' code (while staying in the market and
reporting more on other firms' code). There is no evidence attackers
exploited the additional disclosed flaws: the share exploited within a month
of disclosure fell by about two-thirds, mainly because fewer were already
exploited at disclosure, while the absolute number exploited was unchanged.
The author concludes frontier AI helped defenders find and fix flaws before
attackers could exploit them, but that restricted release creates a
cross-country asymmetry in software security.

## Why it matters

For social_science: a rare quantified empirical answer — not a model or a
forecast — to a live AI-governance question: does restricting frontier-model
access to trusted firms measurably change real-world security outcomes, and
does it create geopolitical asymmetry? Directly usable in debates over export
controls, early-access programs, and the economics of AI-driven cybersecurity
(lenses 4, 7). For ai_engineering: a concrete, measured case of what
controlled release of a model for a sensitive capability (vulnerability
discovery) actually does to the surrounding ecosystem — relevant to anyone
designing access tiers or governance policy for dual-use agentic tools (lens
6), though the paper itself offers no engineering mechanism, only the outcome
data.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-08; single version,
submitted 4 Nov 2026, no revisions). All quantified claims (the disclosure
and high-impact-disclosure multiples, the bug-bounty-researcher response, the
two-thirds drop in share-exploited-within-a-month, the unchanged absolute
exploited count and fix speed) trace to the fetched abstract text, which is
the paper's own stated summary — treated as `verified` per this library's
standing convention for single-source arXiv preprints whose headline claims
are self-reported (cf. the Popov filename-bias entry). The full paper
(empirical design, data sources for "all publicly disclosed vulnerabilities,"
country/firm identification) was not reviewed at capture. The model name
"Claude Mythos Preview" and "Project Glasswing" are as stated in the fetched
abstract and not independently corroborated against a separate public
announcement.

## Updates

None yet.

## Related entries

None yet.
