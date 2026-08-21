---
slug: 2026-chen-loreley-repository-scale-program-evolution
title: "Loreley: Repository-Scale Program Evolution"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.19703
canonical_ids: ["arxiv:2608.19703"]
publisher_or_author: "Mohan Chen"
published: 2026-08-20
captured: 2026-08-21
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  A rigorous, quantified negative result on quality-diversity search for
  self-improving coding agents — a useful evaluation-methodology and
  failure-mode lesson (lens 4) even though the tested method did not win.
---

# Loreley: Repository-Scale Program Evolution

## Summary

Loreley maintains a Quality-Diversity (QD) archive of full repository states —
stored as Git commits from isolated worktrees and judged by a project evaluator —
rather than discarding non-champion branches, as an alternative to sequential
champion-editing or independent-root-proposal search for self-improving coding
agents. In a matched experiment (7 paired blocks, 1,008 candidate jobs, using
Zstandard as the test repository), the author reports that at 48 jobs the QD
approach showed no established advantage over sequential champion editing
(-0.135 percentage points, confidence interval crossing zero) or independent-root
search, despite confirmed archive retention and sampling behavior — a rigorous
null result for the QD-for-coding-agents idea.

## Why it matters

A quantified, well-instrumented negative result against a popular architectural
idea (retaining a diverse archive of program variants) for self-improving coding
agents — useful for teams deciding whether to invest in QD-style archiving versus
simpler sequential search, and a good example of evaluation rigor (explicit
confidence intervals on a null result) worth emulating.

## Verification notes

Read directly from the arXiv abstract; the experimental design (7 paired blocks,
1,008 jobs, Zstandard test repo) and the quantified null result (-0.135pp, CI
crossing zero at 48 jobs) are traced to the source text. No independent
corroboration was possible — newly posted preprint (submitted 20 Aug 2026), single
author. Verification is `partial`.

## Updates

- **2026-08-21** — Entry created.

## Related entries

None yet.
