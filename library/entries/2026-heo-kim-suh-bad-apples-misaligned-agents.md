---
slug: 2026-heo-kim-suh-bad-apples-misaligned-agents
title: "Bad Apples in the Kitchen: How LLM Teams Detect, Correct, and Calibrate Against Their Misaligned Members"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.22342
canonical_ids: ["arxiv:2611.22342"]
publisher_or_author: "Dongseok Heo, Junghwan Kim, Bongwon Suh — arXiv preprint"
published: 2026-11-17
captured: 2026-11-20
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 1 (agent architecture — failure recovery) and lens 6
  (reliability/governance): a controlled 720-episode study of how
  multi-agent teams detect and recover from a quietly misbehaving member,
  with a non-obvious, actionable finding about when explicit
  misalignment-attribution prompting helps versus hurts.
---

# Bad Apples in the Kitchen: How LLM Teams Detect, Correct, and Calibrate Against Their Misaligned Members

## Summary

Asks how an LLM team defends itself when one member quietly goes wrong,
noting that most multi-agent work assumes cooperative partners and that
real-time embodied cooperation is a harder case: a misaligned teammate can
keep speaking cooperatively while its actions diverge, and the team may
not identify the problem quickly enough. The authors inject three
theory-grounded misaligned agents into a custom four-player Overcooked
environment, each targeting a different joint-action layer (speech-action
mismatch, role invasion, disruption of aggregate progress), and break
robustness into three sequential gates — detection, correction, and
calibration — tested in a 3×4×2 design across 720 episodes. Nearly all
misaligned agents are eventually identified, but recovery happens
reliably only when attribution (who is the problem) and situational
diagnosis (what exactly is wrong) occur in the same utterance. Explicit
prompting to attribute the source of misalignment helps in the hardest
case but noticeably hurts performance when no misaligned agent is actually
present. The authors conclude that robustness depends more on how team
chat combines attribution with diagnosis than on detection ability alone,
and that sensitivity to misalignment should be targeted rather than raised
uniformly. (unverified: the exact per-condition recovery rates behind
these conclusions are as summarized from the abstract; full paper and
statistical results not read at capture.)

## Why it matters

For anyone designing multi-agent systems that must tolerate an occasional
misbehaving or faulty member: a specific, non-obvious design lesson —
simply telling agents to call out misalignment is not uniformly good,
because it costs performance when nothing is wrong. That argues for
calibrated, targeted misalignment-sensitivity mechanisms rather than
always-on suspicion, and for a team-communication design that pairs
attribution with concrete diagnosis rather than either alone.

## Verification notes

arXiv abstract page fetched directly (2026-11-20); title, full author
list, and a 17 November 2026 submission date confirmed (listed in arXiv's
cs.MA "recent" page under the 18 Nov announcement date, within the normal
one-day cross-list lag and this run's 7-day eligibility cap). The
experimental design (three misaligned-agent types, 3×4×2, 720 episodes)
and the core qualitative conclusions (attribution+diagnosis co-occurrence
required for recovery; explicit attribution prompting helps the hardest
case but hurts the no-misalignment case) are traceable to the fetched
abstract text and are condensed rather than quoted verbatim throughout;
marked `verification: partial` because the abstract itself is a condensed
summary rather than one offering clean verbatim figures for every claim.
Full paper not read at capture. No independent secondary corroboration
attempted (new working paper, no secondary coverage found this run).

## Updates

None yet.

## Related entries

None yet.
