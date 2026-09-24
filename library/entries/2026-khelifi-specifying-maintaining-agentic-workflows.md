---
slug: 2026-khelifi-specifying-maintaining-agentic-workflows
title: "Specifying and Maintaining Agentic Workflows: An Empirical Study of GitHub Agentic Workflows"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2609.27263
canonical_ids: ["arxiv:2609.27263"]
publisher_or_author: "Jasem Khelifi, Issam Oukhay, Ali Ouni, Mohammed Sayagh, Mohamed Aymen Saied — arXiv preprint (cs.SE)"
published: 2026-09-23
captured: 2026-09-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 2 (harness and context engineering) and lens 6
  (reproducibility, security and governance): a large empirical study
  (1,248 files, 276 repositories) of how GitHub Agentic Workflows are
  authored and maintained, with a specific, auditable security finding
  (only 9.4% address prompt-injection defense) — names a mechanism and
  quantifies a gap a builder can check for directly.
---

# Specifying and Maintaining Agentic Workflows: An Empirical Study of GitHub Agentic Workflows

## Summary

GitHub Agentic Workflows are Markdown files combining natural-language
instructions with configuration that compile into executable GitHub
Actions. The authors analyzed 1,248 such files from 276 repositories,
finding that workflow instructions contain "a median of 556.5 words and
code blocks in 62.1% of files." Among workflows with sustained activity,
"78.2% still receive updates in month 4." A security-relevant finding:
"only 9.4% explicitly address prompt-injection defense." The authors also
built a machine-learning classifier for some aspect of workflow content
achieving an F1 score of 0.818, and recommend developers incorporate
prompt-injection safeguards and resource budgets when applicable.

## Why it matters

For anyone authoring or auditing agentic workflows (natural-language-driven
automation compiled into executable actions), this gives a quantified
baseline for two things: how much maintenance burden to expect (most
active workflows keep receiving updates for months, not one-off scripts)
and a concrete security gap to check for — the large majority of observed
workflows do not explicitly address prompt-injection defense, which is a
direct audit item for anyone deploying similar natural-language-configured
automation.

## Verification notes

Fetched directly from the arXiv abstract page (2609.27263; v1 submitted
2026-09-23 02:47:24 UTC). The dataset scale (1,248 files, 276 repositories),
the word-count/code-block, month-4-retention, and prompt-injection-defense
figures, and the classifier F1 score all trace directly to the abstract's
own quoted text. Full paper (classifier target variable, per-repository
breakdown) not read at capture.

## Updates

None yet.

## Related entries

None yet.
