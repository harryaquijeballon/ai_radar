---
slug: 2026-demoura-coding-agent-memory-file-security
title: "Security Impact of Coding Agent's Memory Files"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.38521
canonical_ids: ["arxiv:2610.38521"]
publisher_or_author: "Thiago Santos de Moura, Selma Güler, Yannic Noller — arXiv (cs.SE)"
published: 2026-10-28
captured: 2026-10-31
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Squarely on lens 6 (reproducibility, security and governance): a
  controlled study showing memory files (e.g. CLAUDE.md) are a live attack
  surface for insecure code generation, with quantified, harness-specific
  disclosure behavior — directly actionable for anyone trusting agent
  memory files without review.
verification: verified
---

# Security Impact of Coding Agent's Memory Files

## Summary

Coding agents automatically load project memory files (such as CLAUDE.md)
at the start of each session and treat them as trusted guidance — anyone
who can edit such a file, including through a pull request, can steer the
agent without touching the developer's prompt. The authors study memory
files as an attack surface for insecure code generation, asking whether a
malicious file causes agents to write code that passes tests but is
vulnerable, and whether agents disclose that the file influenced their
output. For 12 CWE classes, they wrote two malicious variants per class — a
subtle one framing the removal of defensive checks as best practice, and a
forceful one demanding it — and ran Claude Code and OpenCode (two models
each) on 36 SecRepoBench tasks with and without the files. The secure
completion rate shifted by -8 to +6 percentage points with no consistent
direction. Claude Code mentioned the memory file's influence in about
two-thirds of its final messages to the developer; OpenCode mentioned it
almost only in its internal reasoning trace, which developers don't
typically read. Explicitly warning the agent that the memory file was an
attack did not reliably prevent vulnerable code.

## Why it matters

A concrete, quantified demonstration that project memory files are an
unreviewed trust boundary: teams relying on CLAUDE.md-style files (including
this very project) get a direct, actionable signal that such files warrant
the same code-review scrutiny as any other contributor-editable artifact,
and that an agent's own disclosure of having used the file cannot be relied
on as a safety net (harness-dependent, sometimes buried in a reasoning trace
developers don't read).

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.38521, v1 submitted
28 Oct 2026, cs.SE with cs.CR cross-list). The experimental design (12 CWE
classes, two malicious-file variants, 36 SecRepoBench tasks, two harnesses x
two models each), the -8 to +6 percentage-point range, and the
harness-dependent disclosure-rate contrast are traced to the abstract text
itself. No independent corroboration of SecRepoBench task design or raw
results was attempted.

## Updates

None yet.

## Related entries

None yet.
