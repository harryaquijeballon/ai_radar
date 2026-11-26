---
slug: 2026-zhang-long-skillsbench-audit
title: "What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of SkillsBench"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.33943
canonical_ids: ["arxiv:2611.33943"]
publisher_or_author: "Haozhe Zhang, Zhen Long — arXiv preprint"
published: 2026-11-25
captured: 2026-11-26
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A source-code-level audit of a widely cited agent-skills benchmark,
  showing its per-task "skill lift" numbers are substantially shaped by
  grading artifacts and run-level noise rather than a clean skill effect —
  a directly usable caution and reanalysis method for lens 4 (evaluation
  validity).
---

# What Does Skill Lift Actually Measure? A Source-Code-Level Audit and Noise-Aware Reanalysis of SkillsBench

## Summary

Agent skills are directories of instructions, reference materials, and
scripts that coding agents load on demand. SkillsBench reported that
human-curated skills raise pass rates by about 16.6 percentage points on
average, though with lower results on some tasks; later work began gating
or removing skills based on per-task gains. The authors audit SkillsBench at
the source-code level and reanalyze 7,554 public trials (1,421 paired
configuration/task cells). They find grader dependence, placeholder skill
directories, and a harness that silently added 48 built-in skills in most
runs. Their own full-set average lift is 18.7 pp, but three tasks with
identified grading artifacts (two verified grader-dependence cases plus one
operational-definition gap) show an average lift of 74.6 pp — far above the
overall average, suggesting the measured lift is inflated by grading
artifacts rather than skill effects. After pooled reanalysis with
multiple-testing correction, no task-level reduction from skills was
statistically significant; with at most three runs per condition per cell,
58% of cells could not even arithmetically have shown a decrease. A
skill-free gating strategy that appeared to improve results by 2–3 pp still
showed a 4–7 pp "improvement" after shuffling condition labels to remove any
real skill effect, and showed no significant improvement on held-out runs —
confirming the apparent gain was a methodological artifact.

## Why it matters

A directly transferable auditing method for anyone relying on an agent-skill
or tool benchmark's headline numbers: check for grader dependence,
placeholder/injected configuration, and run noise before trusting a
per-task lift or harm claim, and use a label-shuffling control to test
whether an apparent gating improvement is real. The finding that a widely
cited benchmark's own numbers don't support its skill-harm claims is a
direct, concrete warning for lens 4's core concern — eval and guardrail
validity.

## Verification notes

Fetched the arXiv abstract page directly (arXiv:2611.33943, v1 submitted
2026-11-25). The audit methodology, scope (7,554 trials, 1,421 cells), and
all quantified figures above (16.6pp/18.7pp/74.6pp lift figures, the 2-3pp
vs. 4-7pp shuffled-label comparison, the 58% statistical-power figure) are
traced to the abstract's own description. No independent corroboration was
available or attempted beyond the source text; this is the paper's own
novel audit and reanalysis contribution.

## Updates

None yet.

## Related entries

None yet.
