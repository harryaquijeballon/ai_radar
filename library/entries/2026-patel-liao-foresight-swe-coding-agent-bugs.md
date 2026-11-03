---
slug: 2026-patel-liao-foresight-swe-coding-agent-bugs
title: "Do Coding Agents Catch Their Own Bugs? (They Don't.)"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.01181
canonical_ids: ["arxiv:2611.01181"]
publisher_or_author: "Shaswat Patel, Michel Liao, Peter Henderson, He He, Valerie Chen"
published: 2026-10-31
captured: 2026-11-03
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation/validation/deterministic guardrails (lens 4) and
  AI-assisted software development (lens 7): introduces Foresight-SWE, a
  new benchmark isolating whether coding agents anticipate and avoid
  defects their own change will require a later fix for, with a
  quantified, uniformly low pass rate across eleven models.
---

# Do Coding Agents Catch Their Own Bugs? (They Don't.)

## Summary

Introduces Foresight-SWE, a benchmark testing whether coding agents
anticipate and fix problems a task does not explicitly ask them to handle.
It has 212 samples across four programming languages and 35 popular
open-source repositories, each built from a pair of real pull requests
where the second PR fixes a defect the first one introduced. The authors
define the "foresight resolve rate" (FRR): the share of cases where an
agent fully completes the original task without introducing the defect
that the later PR had to fix. Across eleven LLMs, FRR ranges from 6.13% to
24.53% — models mostly fail to avoid the very problems the paired
historical PRs show their own kind of change tends to create. The authors
argue this raises questions about how models are trained/aligned for
coding and how code-review tooling could be improved to catch such
foreseeable defects (as stated in the fetched abstract; full per-model
breakdown and benchmark construction method not reviewed at capture).

## Why it matters

A sharply quantified, low ceiling (6-25% across eleven models) on coding
agents' ability to avoid self-inflicted, foreseeable defects — directly
relevant to teams deciding how much unsupervised scope to give a coding
agent, and a concrete argument for code-review tooling that specifically
checks for the failure-pattern class a given kind of change is known to
introduce, rather than relying on the agent's own foresight.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 31 Oct 2026, no revisions). The Foresight-SWE benchmark design
(212 samples, four languages, 35 repositories, paired-PR construction),
the FRR metric definition, and the 6.13%-24.53% range across eleven models
all trace to the fetched abstract text, which is the paper's own stated
summary of its results — treated as `verified` on this library's
convention for single-source arXiv preprints whose headline figures are
self-reported. The full paper (per-model/per-language results, benchmark
construction detail, author affiliations) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
