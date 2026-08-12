---
slug: 2026-yang-skillgate-malicious-skill-detection
title: "SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.25619
canonical_ids: ["arxiv:2607.25619"]
publisher_or_author: "Rui Yang, Michael Fu, Kla Tantithamthavorn, Chetan Arora, Joey Chua — arXiv preprint"
published: 2026-07-28
captured: 2026-07-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on reproducibility, security and governance (lens 6): a deployable
  runtime control against malicious agent-skill files (credential
  exfiltration, backdoor injection) with measured detection performance
  (F1 0.817, 1.13% false-positive rate) and a stated 77% reduction in LLM
  token cost versus full-file analysis — a concrete, evaluable extension of
  this radar's existing skill-security thread.
---

# SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents

## Summary

Addresses malicious "skill" files that coding agents download and install:
per the paper, a malicious skill file "can silently reprogram agent
behavior, exfiltrating credentials, injecting backdoors into generated
code." SkillGate is a security gateway that hybridizes regex filtering with
LLM-based judgment to screen skill packages before installation, optimized
for cost: files that pass regex screening skip the LLM entirely, and files
flagged for LLM review send only the relevant snippet rather than the full
file. Evaluated on SkillsBench (1,650 samples, 9.1% malicious), SkillGate
reports an F1 score of 0.817 with a 1.13% false-positive rate, cutting LLM
token input by 77% compared to full-file analysis while outperforming
existing tools on the reported metrics (unverified — comparison baselines
and exact competing-tool numbers not read at capture).

## Why it matters

A directly deployable, cost-aware control for the same skill-security
problem this radar has already tracked via SkillSpector and OpenSkillRisk:
runtime screening before installation, not just post-hoc auditing, with
concrete numbers (F1, false-positive rate, token savings) a team could use
to evaluate whether to adopt a similar gateway ahead of installing
third-party agent skills.

## Verification notes

arXiv abstract page fetched directly (2026-07-29); title, full author list,
and "Submitted on 28 Jul 2026" confirmed. The regex+LLM hybrid design, the
snippet-only escalation mechanism, the SkillsBench evaluation (1,650
samples, 9.1% malicious), and the F1/false-positive/token-reduction figures
all trace to the fetched abstract text. The "outperforming existing tools"
claim is the abstract's own framing, not independently checked against
competing tools — marked unverified above. Full paper not read at capture.

## Updates

None yet.

## Related entries

[2026-vu-skillspector-agent-skill-scanner](2026-vu-skillspector-agent-skill-scanner.md) — prior entry on auditing agent skills for hidden vulnerabilities; SkillGate is a runtime detection control for the same threat class.
[2026-liu-openskillrisk-benchmark](2026-liu-openskillrisk-benchmark.md) — benchmark for agent safety against risky third-party skills; SkillsBench here is a comparable evaluation resource.
