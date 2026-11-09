---
slug: 2026-mehtiyev-stale-instruction-files-documentation-debt
title: "When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.09802
canonical_ids: ["arxiv:2611.09802"]
publisher_or_author: "Tural Mehtiyev, Biruk Tadesse, Lawrence Arkoh, Wesley Assunção"
published: 2026-11-06
captured: 2026-11-09
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on harness and context engineering (lens 2): a controlled study
  (732 trajectories, two models, three real stale instructions from active
  open-source projects) quantifying a cost that task-success-only
  evaluation misses — directly actionable for anyone maintaining
  AGENTS.md/CLAUDE.md-style instruction files.
---

# When Instruction Files Go Stale: Documentation Debt and Hidden Cost in Coding Agents

## Summary

Coding agents such as Claude Code read repository instruction files (e.g., AGENTS.md, CLAUDE.md) at the start of every session. As code changes — a test folder moves, a command changes — these files can fall out of date; the authors frame a stale instruction as documentation debt whose cost accumulates across every later session, and argue task-success-only evaluation can miss this cost entirely, letting stale files persist unnoticed.

Using three real stale instructions drawn from active open-source projects (a test command, a code location, and a component-addition procedure), the authors ran 22 maintenance tasks under three versions of each instruction (stale, corrected, removed), holding code and tasks constant, and analyzed 732 trajectories from two models at the level of individual tool calls.

Findings: agents follow stale guidance when it is relevant to the task, even when correct information is available elsewhere in the repository. For the stale test-command case, Claude Sonnet 5.5 needed about two extra tool calls per run versus the corrected version — roughly a third more — though no difference was detected in the other two cases. Agents generally recovered from the immediate failures the stale instruction caused, but none repaired the instruction file itself. Correcting the file eliminated operations on obsolete paths; removing it prevented most of them.

## Why it matters

A concrete, measured answer to a maintenance question every team running coding agents on a real repository faces: stale instruction files cost extra tool calls silently, agents don't self-heal them, and task-success metrics won't catch the drift. Directly actionable — periodically audit and correct (or remove) instruction files rather than assuming agents will route around staleness — and a useful complement to this library's prior entry on instruction-file growth (CLAUDE.md "catastrophic remembering"), this time on the staleness/decay side rather than the bloat side.

## Verification notes

Fetched the arXiv abstract page directly; the methodology (three real stale instructions, 22 tasks, three conditions, 732 trajectories, two models) and the quantified finding (about two extra tool calls, roughly a third more, for the stale test-command case) are as stated in the abstract. Load-bearing claims are traced to the source; no independent replication exists yet for this single study.

## Updates

None yet.

## Related entries

- [2026-chakrabarti-claude-md-catastrophic-remembering](2026-chakrabarti-claude-md-catastrophic-remembering.md) — the companion failure mode: instruction files growing unboundedly rather than going stale; read together for a fuller picture of instruction-file maintenance costs.
- [2026-sun-cursorrules-files-study](2026-sun-cursorrules-files-study.md) — an empirical study of a related instruction-file convention (`.cursorrules`) in open-source projects.
