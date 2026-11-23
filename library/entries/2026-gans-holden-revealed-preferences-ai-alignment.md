---
slug: 2026-gans-holden-revealed-preferences-ai-alignment
title: "Are Revealed Preferences All You Need for AI Alignment?"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://www.nber.org/papers/w36048
canonical_ids: ["doi:10.3386/w36048", "nber:w36048"]
publisher_or_author: "Joshua S. Gans and Richard T. Holden — NBER Working Paper"
published: 2026-11
captured: 2026-11-23
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  Applies revealed-preference theory to give a formal sufficiency criterion
  for when an AI's observations of a principal's choices are enough to act
  and to gather evidence well — lens 8 (philosophy of AI and trust): a
  rigorous framework sharpening when "doing what the principal would do" is
  actually safe; medium for ai_engineering as alignment theory rather than a
  directly applicable engineering pattern.
---

# Are Revealed Preferences All You Need for AI Alignment?

## Summary

NBER Working Paper 36048 (Joshua S. Gans, Richard T. Holden) studies how AI
agents can learn what their principals want from the choices those
principals make. The authors give a criterion for when a principal's
decisions, across every belief the AI might hold, are sufficient for the AI
to act well. For taking actions, the decisions are sufficient. For choosing
costless evidence to gather, they are sufficient only when the same evidence
is best across every block of "cautious" actions, such as deferring to a
person; otherwise the AI can act as its principal would yet still gather the
wrong evidence, and greater capability can turn that error into incorrect
actions. The paper argues that choices between two mistakes reveal
information that ordinary decisions miss.

## Why it matters

Gives economists and AI-alignment researchers a formal, falsifiable
condition for when "learn from revealed choices" is sufficient for AI
alignment and when it silently fails — directly relevant to anyone
evaluating preference-learning or RLHF-style approaches to deferring to
human judgment, and to the broader question of what makes an AI system's
inferred objectives trustworthy.

## Verification notes

Read directly from the NBER working paper abstract page
(nber.org/papers/w36048). The page shows "Issue Date: November 2026" with no
day-level date; the summarized claims (the sufficiency criterion, the
failure mode under capability increases) are taken directly from the
NBER-published abstract text. No independent corroboration sought — a
theoretical result reported by its own authors on the primary working-paper
page.

## Updates

None yet.

## Related entries

None yet.
