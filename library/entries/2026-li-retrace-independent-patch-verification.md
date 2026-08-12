---
slug: 2026-li-retrace-independent-patch-verification
title: "Independent Patch Verification for Coding Agents with a Bidirectional Reconstruct-and-Verify Framework"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.08950
canonical_ids: ["arxiv:2608.08950"]
publisher_or_author: "Chenglin Li, Yisen Xu, Zehao Wang, Shin Hwei Tan, Tse-Hsun (Peter) Chen — arXiv preprint (cs.SE)"
published: 2026-08-09
captured: 2026-08-11
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 4 (evaluation, validation, deterministic guardrails):
  directly addresses a core reliability gap — once a patch is produced, no
  mechanism independently verifies whether it truly resolves the reported
  problem — with a training-free verification framework and quantified
  pass-rate gains on a standard benchmark.
---

# Independent Patch Verification for Coding Agents with a Bidirectional Reconstruct-and-Verify Framework

## Summary
The paper proposes RETRACE, a training-free framework for independently verifying whether an autonomous coding agent's patch actually resolves the issue it targets. Forward reconstruction builds a repair rationale from the issue description and the agent's trajectory; backward reconstruction independently infers, from the patch alone, what problem it addresses; a reconciliation stage checks consistency between the two and either approves the patch or proposes targeted revisions. On SWE-bench Verified, RETRACE improves Pass@1 by +7.0 percentage points for GPT-4-mini and +3.6 points for MiniMax-2.5, with comparable gains demonstrated on OpenHands without modification. Ablations show both reconstruction directions and the reconciliation stage each contribute independently.

## Why it matters
A concrete instance of the "independent verification" pattern that makes agent output trustworthy: rather than trusting an agent's own claim that a patch is correct, RETRACE cross-checks the patch against an independently inferred account of the problem it's meant to solve — directly transferable to any pipeline where an agent's output needs a check that doesn't rely on the agent's own self-report.

## Verification notes
Read via the arXiv abstract page. Pass@1 gains, the OpenHands generalization claim, and the ablation-study conclusion are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
