---
slug: 2026-rahman-plausible-is-not-enough-ai-pr-trust
title: "Plausible Is Not Enough: Trust and Evidence in AI-Authored Pull Request Review"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.21144
canonical_ids: ["arxiv:2610.21144"]
publisher_or_author: "Md Shamimur Rahman, Khairul Alam, Banani Roy, Chanchal K. Roy — arXiv preprint"
published: 2026-10-15
captured: 2026-10-17
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on AI-assisted software development (lens 7): a 239-practitioner,
  31-country survey with matched questions quantifying how reviewers' trust
  criteria and evidence demands differ for AI-authored vs. human-authored
  pull requests, with a concrete recommendation (expose provenance, separate
  generated claims from human-validated evidence) that review tooling could
  act on.
---

# Plausible Is Not Enough: Trust and Evidence in AI-Authored Pull Request Review

## Summary

Per the arXiv abstract page (v1 submitted 15 Oct 2026, CC BY 4.0), the paper surveys 239 practitioners across 31 countries with matched questions about reviewing AI-authored pull requests (AIPRs) versus human-authored ones (HPRs), asking whether the same trust criteria apply to both. Reported figures: 64.9% of respondents reported lower initial trust in AIPRs; 61.1% reported higher evidence requirements for AIPRs; the share who would block approval under residual uncertainty rose from 19.4% (HPRs) to 43.9% (AIPRs); 55.2% considered their own reasoning through critical cases sufficient to approve an AIPR versus 28.5% for an HPR; and unclear ownership of a change was more likely to pause review for an AIPR than an HPR (29.3% vs. 14.6%). Reviewers reported leaning on the prompter's expertise and bounded change size rather than the author's track record for AIPRs, prioritising test inspection, project context, and local execution, and being more likely to partially reimplement non-trivial logic to verify it themselves. The authors frame AI-authored-PR review as fundamentally an evidence-ownership problem rather than a correctness check, and recommend that review tools and agentic workflows expose provenance, separate generated claims from human-validated evidence, and surface uncertainty before approval.

## Why it matters

Directly actionable for anyone designing AI-assisted code-review tooling or team practice: the quantified shift from track-record-based to evidence-based trust, and the specific recommendation to separate "claimed" from "human-validated" evidence in the review UI, gives a concrete design target rather than a general exhortation to "review AI code carefully."

## Verification notes

Source reachable (arXiv abstract page). Claims traced to the abstract-level summary only; the full paper (survey instrument, demographic breakdown, statistical tests) was not opened, and the reported percentages were not independently corroborated beyond the abstract page's own statement of them.

## Updates

None yet.

## Related entries

None yet.
