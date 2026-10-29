---
slug: 2026-horikawa-detecting-ai-agent-commits
title: "Agent or Human? Detecting Commits by AI Coding Agents in the Absence of Authorship Signatures"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.36229
canonical_ids: ["arxiv:2610.36229"]
publisher_or_author: "Kosei Horikawa, Hao Li, Yutaro Kashiwa, Youssef Esseddiq Ouatiti, Mohammed Sayagh, Bram Adams, Hajimu Iida, Ahmed E. Hassan"
published: 2026-10-26
captured: 2026-10-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on AI-assisted software development (lens 7): a large-scale study
  (7.8M commits, 1,226 repositories, five agents) with a measured,
  actionable, and appropriately cautious conclusion — detection without
  authorship signatures is partially possible but too unreliable across
  agents and time to replace recorded attribution — directly relevant to
  governance and code-review-prioritization decisions.
---

# Agent or Human? Detecting Commits by AI Coding Agents in the Absence of Authorship Signatures

## Summary

Studies whether commits made by AI coding agents (e.g. Claude Code,
GitHub Copilot's coding agent, Cursor) can be distinguished from human
commits once explicit authorship signatures — bot accounts,
Co-authored-by trailers — are removed. The authors analyze 7,837,946
commits from 1,226 repositories spanning five coding agents plus human
commits, training detectors (including TF-IDF and XGBoost features, and
an unfine-tuned frontier model) and testing transfer to held-out agents.

The best detector reaches an ROC AUC of up to 0.859 after signature
masking, driven mainly by message verbosity and change size, but
precision on the full test set at the observed agent share is only 0.332.
Transfer to held-out Claude Code and Copilot commits is weaker — TF-IDF
reaches AUC 0.524 on Claude Code — and an unfine-tuned model (gpt-6-sol)
performs similarly to the fitted XGBoost/TF-IDF detectors on the shared
sample. Detector performance is agent- and time-dependent: Copilot's AUC
drops and later recovers over time, and more training history helps
detection of Claude Code commits but not Copilot's. The authors conclude
detection can help prioritize review but is too unreliable to replace
recorded attribution (all figures as stated in the fetched abstract; full
paper, feature sets, and modeling details not reviewed at capture).

## Why it matters

A large-scale, appropriately cautious evidence base for a governance
question many teams now face: can you tell which commits an AI agent
wrote without relying on self-reported attribution? The answer here is
"partially, and unreliably" — useful for triaging review effort (message
verbosity, change size as weak signals) but not as a substitute for
requiring or trusting recorded Co-authored-by trailers, and the
agent/time-dependence findings (Copilot's detectability drifting, more
history not helping uniformly) are a concrete warning against assuming a
detector trained today stays accurate as agents and usage change.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-29; single version,
submitted 26 Oct 2026, 20:08 UTC, 834 KB). The dataset scale (7,837,946
commits, 1,226 repositories, five agents), the AUC/precision figures
(0.859, 0.332, 0.524 transfer AUC), and the time/agent-dependence findings
all trace to the fetched abstract text. The feature engineering, model
training procedure, and statistical tests were not independently
reviewed; the precision figure in particular depends on the (unstated in
the abstract) observed agent base rate in the test set.

## Updates

None yet.

## Related entries

None yet.
