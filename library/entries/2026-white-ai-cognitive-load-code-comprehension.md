---
slug: 2026-white-ai-cognitive-load-code-comprehension
title: "Feeling Easier, Working Harder: Cognitive Load in AI-Assisted Code Comprehension"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.12019
canonical_ids: ["arxiv:2611.12019"]
publisher_or_author: "Maryangela White, Maximilian Rose, Matthew Buckman, Amy McDonnell, Francisco Ortega, Bianca Trinkenreich — arXiv preprint (cs.SE), accepted ICSE 2027"
published: 2026-11-09
captured: 2026-11-12
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on AI-assisted software development (lens 7): a controlled study
  with an objective, continuously-measured workload instrument (not just
  self-report) finding a "dual-task penalty" — AI assistance raised
  measured cognitive workload without raising perceived workload or
  measurable comprehension gains — a concrete, actionable caution for
  tool design and code-review practice.
---

# Feeling Easier, Working Harder: Cognitive Load in AI-Assisted Code Comprehension

## Summary

Examines how access to generative AI affects developers' real-time
cognitive workload, code comprehension performance, and self-perceived
comprehension strategies. Twenty novice CS students read Java snippets of
varying length, with or without AI assistance, then took a quiz without AI
available. Workload was measured continuously with a Detection-Response
Task (a secondary-task reaction-time measure) and compared against
post-quiz NASA-TLX (self-reported workload) and SEQ scores in a 3×2
within-subjects design. AI assistance significantly increased objective
cognitive workload — detection-task reaction times rose 11.2% — while
self-reported workload (NASA-TLX) did not change. Comprehension scores
were high in both conditions with no evidence AI improved comprehension at
the difficulty levels tested (a ceiling effect limited detection of
benefits on harder tasks). Participants trusted AI output conditionally:
checking it on complex snippets but accepting it directly on simpler code,
and a notable subset shifted toward skimming code or reading AI
explanations instead of the code itself.

## Why it matters

A concrete caution for AI-assisted code review and comprehension tooling:
developers may not accurately perceive the cognitive resources AI
assistance actually costs them, since perceived ease (unchanged NASA-TLX)
diverged from measured cost (higher reaction-time workload). This "dual-task
penalty" is directly relevant to how teams should interpret
developer-reported ease-of-use for AI coding tools, and to how tool and
process designers should think about when lighter AI assistance (or none)
may serve comprehension better than it feels like it does.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.12019,
2026-11-12); title, authors, submission date (9 Nov 2026), category
(cs.SE), and ICSE 2027 acceptance confirmed there. The study design (20
participants, 3×2 within-subjects, tDRT/NASA-TLX/SEQ instruments) and the
quantified finding (11.2% reaction-time increase) trace to the fetched
abstract text. The abstract did not report the comprehension-score
statistics or significance values for the trust/skimming findings, which
are described only qualitatively above; full paper not read at capture.

## Updates

None yet.

## Related entries

None yet.
