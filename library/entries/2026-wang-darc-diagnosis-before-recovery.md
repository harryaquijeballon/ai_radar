---
slug: 2026-wang-darc-diagnosis-before-recovery
title: "Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.11772
canonical_ids: ["arxiv:2608.11772"]
publisher_or_author: "Pan Wang, Yihao Hu, Hang Wang, Zirui Lv, Xin Zhang, Jianshe Li, Jiang-Ming Yang, Wei Wu, Yongqi Tong — arXiv preprint (cs.CL)"
published: 2026-08-12
captured: 2026-08-13
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 5 (observability and debugging): a named failure taxonomy
  (DARC) that diagnoses agent failure types before choosing a recovery
  intervention, tested across three distinct environments (ALFWorld,
  AppWorld, XBRL Finance) with reported gains in both success rate and
  efficiency — directly applicable to designing recovery logic for agent
  harnesses beyond coding agents specifically.
---

# Diagnosis Before Recovery: Turning Agent Failures into Selective Self-Correction

## Summary
Coding agents benefit from self-correction because compilers, tests, and execution traces turn many failures into typed recovery signals, but broader language-agent tasks often expose only a coarse task failure. The paper introduces DARC, which diagnoses failure types during development to determine which recovery interventions to apply at test time — rather than expanding context uniformly, DARC profiles failure modes, filters incompatible interventions, and deploys a cost-aware recovery policy. Tested across ALFWorld, AppWorld, and XBRL Finance, it improves over baseline agents while reducing environment steps or retrieval costs. The core reframing: self-correction as "recovery-interface design" rather than simple prompt expansion.

## Why it matters
Gives agent builders a named, transferable failure taxonomy and a design principle — match the recovery intervention to the diagnosed failure type rather than uniformly expanding context — validated across three unrelated task domains (embodied tasks, app automation, financial data). Directly usable for anyone building observability and self-correction logic into a general-purpose agent harness.

## Verification notes
Read via the arXiv abstract page (2026-08-13). The DARC system description, the three-environment test set, and the efficiency/success claims are quoted/paraphrased directly from the abstract; exact effect sizes are not stated in the abstract beyond "improvements over baseline agents while reducing environment steps or retrieval costs." Full paper (quantitative results table) not read at capture; findings not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
