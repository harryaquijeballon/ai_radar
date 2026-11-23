---
slug: 2026-yan-public-agent-evals-teardown
title: "How Public Evals Work, Where They Break, and What Should Change"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://eugeneyan.com/writing/public-evals/
canonical_ids: []
publisher_or_author: "Eugene Yan"
published: 2026-11-22
captured: 2026-11-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A teardown of 12 public agent benchmarks finding grader false negatives in
  8 of them, with a concrete list of mechanisms, failure modes, and fixes
  (pass^k, grader audits, versioned subsets, evaluate-in-your-own-harness) —
  squarely lens 4 (evaluation, validation and deterministic guardrails) and
  lens 5 (observability): practically usable by anyone selecting or building
  agent benchmarks.
---

# How Public Evals Work, Where They Break, and What Should Change

## Summary

Eugene Yan reviews 12 public agent benchmarks and argues headline scores
often mislead: in 8 of the 12, there is evidence the grader rejected correct
work, and many benchmarks measure what is easy to check rather than what
matters in real work. The post breaks benchmark construction into four
components (instruction, environment, grader, optional human reference
solution) and catalogs failure modes on both sides: agent-side (skipping
verification, dropping stated requirements, declaring success on failures)
and grader-side (false negatives from checks stricter than the prompt,
unstated requirements, or wrong answer keys; false positives from shallow
keyword or rubric checks; metric blind spots such as average pass rate
hiding inconsistency; harness confounds, since the same model scores
differently across harnesses; and environment noise). Its recommendations
include reporting pass^k (solved only if an agent passes all k trials)
alongside average pass rate, judging efficiency by human rework time rather
than token cost, testing multi-turn collaboration (clarifications, mid-task
changes) rather than single-shot instructions, auditing both failing and
*passing* runs for reward hacking, publishing a versioned fixed-subset score
to track progress across benchmark releases, and evaluating candidate models
in the harness you will actually deploy rather than trusting cross-harness
comparisons.

## Why it matters

A directly actionable checklist for anyone selecting a public agent
benchmark to guide a build-or-buy decision, or designing an internal one: it
names specific, checkable failure modes (grader false negatives/positives,
harness confounds, metric blind spots) and specific fixes (pass^k,
versioned subsets, in-harness evaluation) rather than general skepticism
about benchmarks.

## Verification notes

Read directly from the source post (eugeneyan.com/writing/public-evals/),
dated 2026-11-22 per the site's RSS feed. The summarized mechanisms, failure
modes, and recommendations are taken directly from the fetched post text.
No independent corroboration of the "8 of 12 benchmarks" finding was sought
beyond the author's own stated review.

## Updates

None yet.

## Related entries

None yet.
