---
slug: 2026-malo-customer-is-the-builder
title: "The Customer Is the Builder: How AI Coding Agents Are Rewriting the Economics of Software"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.30307
canonical_ids: ["arxiv:2610.30307"]
publisher_or_author: "Ripon Chandra Malo, Zimeng Yu, Tong Qiu"
published: 2026-10-21
captured: 2026-10-23
relevance:
  social_science: medium
  ai_engineering: high
verification: partial
rationale: >-
  High on ai_engineering lens 7 (AI-assisted software development): a
  quantified look at how rising coding-agent capability shifts the
  build-vs-buy boundary for software, with a named "software substitution
  frontier" concept and multiple independent evidence sources. Medium on
  social_science lens 1/4: a firm-behavior/software-market economics
  argument, but extrapolative rather than causal, and the authors flag their
  own self-report and completeness limitations.
---

# The Customer Is the Builder: How AI Coding Agents Are Rewriting the Economics of Software

## Summary
The paper argues that AI coding agents may push organizations to build
software in-house that they would otherwise buy. It defines a "software
substitution frontier": the set of functions customers could build and
maintain at an acceptable standard for less than the cost of buying them.
The authors warn this growing build capacity could shape individual buying
decisions well before any broad market shift becomes visible in aggregate
data.

The study combines several public evidence sources rather than a single
dataset: agent-benchmark trends, a broad search for open-source alternatives
to commercial products, a case study of public development activity, market
indicators, and an organizational survey. Quantified findings: since 2023,
the length of benchmark tasks leading agents complete at a 50% success rate
(measured in human working time) has doubled roughly every 129 days. A
search identified 575 potential open-source alternatives to selected
commercial products, though the authors note some functional matches still
need validation. A case example — the "Craft suite" — produced 12
application repositories over 12.0 days of public development, described by
the authors as early, unverified-completeness versions. Market evidence is
mixed: purchased software gained U.S. investment share and tracked
commercial installations grew. In an organizational survey, 32% of
respondents said they had forgone at least one software purchase because
they could build the functionality with coding agents — a self-report that,
the authors caution, does not establish how much spending was actually
displaced or how reliable the resulting tools are. The authors describe
their projections as extrapolation, not forecast.

## Why it matters
For AI-engineering audiences, this gives a quantified, named framework
(the substitution frontier, the 129-day benchmark-doubling cadence) for
reasoning about when "build it with an agent" becomes viable for a given
function — directly useful to teams deciding whether to build or buy parts
of a research/policy product's software stack. For social-science
audiences, it is a citable, if extrapolative, firm-behavior argument about
how AI changes make-vs-buy economics in the software industry, usable as a
framing device for competition/market-structure questions (lens 4) even
though it stops short of causal identification.

## Verification notes
Read directly from the arXiv abstract page (arXiv:2610.30307, v1, submitted
21 Oct 2026). The quantified figures (doubling cadence, 575 alternatives
count, 12-repo/12-day case, 32% survey figure) are stated directly in the
abstract and traceable to it. Verification is `partial`, not `verified`:
the authors themselves flag load-bearing limitations on several of these
figures (unvalidated functional matches among the 575 alternatives,
unverified completeness/reliability of the Craft suite repositories, and
the survey's inability to establish actual spending displacement), so the
headline numbers are traceable but not independently corroborated or free
of self-reported caveats. No load-bearing claim is unverifiable outright,
so the entry clears `accepted` despite the partial grade.

## Updates

- None yet.

## Related entries
None yet.
