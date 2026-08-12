---
slug: 2026-chakrabarti-claude-md-catastrophic-remembering
title: "Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.11095
canonical_ids: ["arxiv:2608.11095"]
publisher_or_author: "Kushal Chakrabarti — arXiv preprint (cs.SE)"
published: 2026-08-11
captured: 2026-08-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 2 (harness and context engineering): a large-scale empirical
  study (247,694 instruction instances across 1,867 repositories) of why
  agent instruction files grow indefinitely, naming the mechanism
  ("catastrophic remembering") and quantifying a concrete, cheap mitigation —
  directly actionable for anyone maintaining a CLAUDE.md-style harness file,
  which this project itself does.
---

# Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding

## Summary
The paper studies why instruction files in agentic coding repositories (e.g. CLAUDE.md-style files) expand indefinitely rather than staying curated. Across 247,694 instruction instances in 1,867 repositories, instructions grew over 200% during their lifetime and became increasingly resistant to removal over time. The author attributes this to imperfect recall: appending an instruction is always cheap, but once its original rationale is lost, deleting it without risking a correctness regression becomes combinatorially expensive ("costs O(2^|D|)"). The paper frames this as "catastrophic remembering" — the inverse of catastrophic forgetting in continual learning — and tests a mitigation: attaching explanatory comments to instructions. In controlled experiments this removed 99.3% of excess instructions and improved real-world instruction-following accuracy by up to 23.1%.

## Why it matters
A concrete, low-cost engineering practice for harness/context maintenance: instructions should carry their rationale inline, not just their directive, because the directive alone can't be safely pruned later. Directly applicable to any project (including this one) that maintains a growing agent-instructions file, and a named failure mode worth watching for.

## Verification notes
Read via the arXiv abstract page. The instance/repository counts, growth percentage, and the 99.3%/23.1% mitigation figures are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
