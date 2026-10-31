---
slug: 2026-sanko-oversight-loosening-agent-skills
title: "When Skills Tell Agents Not to Ask: A Large-Scale Study of Oversight Directives in Agent Skills"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.37734
canonical_ids: ["arxiv:2610.37734"]
publisher_or_author: "Timofey Sanko, Yuan Tian — arXiv (cs.CR)"
published: 2026-10-27
captured: 2026-10-31
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Squarely on lens 6 (governance, concrete controls): a large-scale,
  codebook-based measurement of how often agent-skill files instruct an
  agent to bypass human oversight, plus a benchmarked detector — directly
  usable by anyone auditing third-party skills before enabling them.
verification: verified
---

# When Skills Tell Agents Not to Ask: A Large-Scale Study of Oversight Directives in Agent Skills

## Summary

The authors study "oversight-loosening directives" — instructions embedded
in agent skill files that tell an AI agent to proceed without approval, skip
checks, or keep working without checking in with a human. They analyzed 1.53
million English-language skills and hand-labeled 2,097 text units to build a
codebook and a detector. They estimate that about 1 in 17 skills contains
such a directive, most often expressed through permission flags and usually
applied unconditionally rather than conditionally. Skills that run shell
code, install packages, or use sudo have roughly 1.7–1.8x the odds of
containing one, and a small number of upstream skill families account for
much of the spread (suggesting propagation through forking/copying rather
than independent authorship). Existing open-source scanners catch at most
46% of these directives, while an LLM prompted with the authors' codebook
catches 61%.

## Why it matters

Gives anyone building or vetting an agent-skill ecosystem a measured base
rate (1 in 17) and a concrete detection method for a specific, previously
undocumented governance failure mode — skills that quietly instruct an
agent to loosen its own oversight — along with a benchmark showing current
open-source scanners miss more than half of these directives.

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.37734, v1 submitted
27 Oct 2026, primary cs.CR, cross-listed cs.AI/cs.SE). The 1.53M-skill corpus
size, the 2,097-unit hand-labeled codebook, the ~1-in-17 base rate, the
1.7–1.8x odds ratio for shell/install/sudo skills, and the 46%/61% detector
recall figures are traced to the abstract text itself. No independent
corroboration of the underlying skill corpus or codebook was attempted.

## Updates

None yet.

## Related entries

None yet.
