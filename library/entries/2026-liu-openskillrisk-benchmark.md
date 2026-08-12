---
slug: 2026-liu-openskillrisk-benchmark
title: "OpenSkillRisk: Benchmarking Agent Safety When Using Real-World Risky Third-Party Skills"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.20121
canonical_ids: ["arxiv:2607.20121"]
publisher_or_author: "Qiyuan Liu, Tingfeng Hui, Kun Zhan, Kaike Zhang, Ning Miao"
published: 2026-07-22
captured: 2026-07-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on the evaluation/validation and security/governance lenses: a
  263-skill, seven-threat-category benchmark spanning 13 LLMs and 3 CLI agent
  frameworks, quantifying that even the safest configurations act unsafely
  in about 17% of cases. A directly usable benchmark and failure-mode
  taxonomy for eval design around third-party tool/skill risk. Discovered in
  the 22-23 Jul 2026 window via arXiv cs.SE/cs.MA.
---

# OpenSkillRisk: Benchmarking Agent Safety When Using Real-World Risky Third-Party Skills

## Summary

Paper (Qiyuan Liu, Tingfeng Hui, Kun Zhan, Kaike Zhang, Ning Miao;
arXiv:2607.20121, submitted 22 July 2026) introducing OpenSkillRisk, a
benchmark of 263 risky "skills" drawn from public marketplaces, organized
into seven threat categories, each paired with a user task and a sandbox for
evaluation. Testing thirteen state-of-the-art LLMs across three CLI agent
frameworks, the authors report that "even the safest configurations still
execute unsafe actions in about 17% of cases." The analysis identifies three
recurring failure patterns: agents failing to recognize risk at all,
recognizing risk but failing to intervene before acting, and following
skill instructions beyond the user's intended scope.

## Why it matters

A directly usable benchmark and failure taxonomy for anyone evaluating
agent frameworks that consume third-party tools or skills: the three named
failure modes (no-recognition, recognize-but-proceed, scope-overrun) give a
concrete rubric for red-teaming an agent's skill-execution boundary, rather
than a generic "test for bad behavior" mandate.

## Verification notes

Abstract page fetched and read directly; title, authors, submission date,
benchmark composition (263 skills, seven threat categories, 13 models,
3 frameworks), the ~17% unsafe-action figure, and the three failure patterns
are all traced to the source text. No independent corroboration attempted
for the benchmark's empirical results (would require access to the full
paper and reproduction); load-bearing quantitative claims are reported as
stated by the authors.

## Updates

*(none yet)*

## Related entries

[2026-vu-skillspector-agent-skill-scanner.md](2026-vu-skillspector-agent-skill-scanner.md) — a scanning tool aimed at catching the same class of risky third-party skill before install/execution time that this benchmark measures agents failing to handle safely at runtime.
