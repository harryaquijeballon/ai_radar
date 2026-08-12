---
slug: 2026-gao-explainable-ai-trust-code-review
title: "Evaluating the Impact of Explainable AI on Trust in AI-Assisted Code Review"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2607.24601
canonical_ids: ["arxiv:2607.24601"]
publisher_or_author: "Zhenhan Gao, Marvin Muñoz Barón, Umm-e Habiba, Daniel Graziotin, Stefan Wagner — arXiv preprint, accepted to ISSTA 2026"
published: 2026-07-27
captured: 2026-07-28
relevance:
  ai_engineering: high
  social_science: n/a
verification: verified
rationale: >-
  High on the AI-assisted software development lens: a controlled study (34
  participants, three explanation-level conditions) with measured,
  sometimes counterintuitive results — more explanation raises trust but
  not agreement, and prompts more critical scrutiny of AI suggestions —
  giving transferable design guidance rather than a demo.
---

# Evaluating the Impact of Explainable AI on Trust in AI-Assisted Code Review

## Summary

Reports a controlled study, accepted to ISSTA 2026, testing how
explainability affects developer trust in LLM-based code review tools. 34
participants used three versions of a review tool: one giving detailed
explanations for each flagged issue, one giving basic feedback only, and
one giving no explanation at all. Full explanations produced the highest
perceived trust (mean 3.99 out of 5) but not the highest agreement with the
tool's suggestions; moderate explanations instead achieved the highest
agreement, at 89.22%. Explanation level did not measurably affect how long
review took. A notable finding is that fuller explanations made developers
more critical of the AI's suggestions rather than more deferential —
comprehensive explanations prompted developers to question the tool more,
not simply trust it more.

## Why it matters

Direct, measured design guidance for anyone building or deploying
AI-assisted code review: adding explanations is not a simple trust dial —
full explanations build the most trust but can reduce agreement and
increase scrutiny, while moderate explanations may align developer and
tool judgments better. Useful for teams calibrating how much explanation
to surface in a review or validation UI when the goal is well-calibrated
reliance rather than maximal trust.

## Verification notes

arXiv abstract page fetched directly (2026-07-28); title, full author
list, "Submitted on 27 Jul 2026," ISSTA 2026 acceptance note confirmed.
Every claim in the Summary — the 34-participant design, the three
explanation conditions, the 3.99/5 trust figure, the 89.22% agreement
figure for moderate explanations, the null effect on review duration, and
the increased-scrutiny finding — traces directly to the fetched abstract
text. Full paper text not read at capture; no independent corroboration
attempted beyond the stated peer-reviewed acceptance (pre-publication
preprint of an accepted paper). Upgrade path: read the full paper for the
study's task design and statistical detail.

## Updates

None yet.

## Related entries

None yet.
