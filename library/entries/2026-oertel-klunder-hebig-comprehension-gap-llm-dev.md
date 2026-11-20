---
slug: 2026-oertel-klunder-hebig-comprehension-gap-llm-dev
title: "The Comprehension Gap in LLM-Assisted Software Development: An Experiment"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.24216
canonical_ids: ["arxiv:2611.24216"]
publisher_or_author: "Julian Oertel, Jil Klünder, Regina Hebig — arXiv preprint"
published: 2026-11-18
captured: 2026-11-20
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 7 (AI-assisted software development): a controlled
  crossover experiment with a measured result (not just a framing claim)
  on when LLM assistance degrades a developer's understanding of their own
  code, including an interaction effect (reliance plus low engagement)
  teams could use as a concrete risk signal.
---

# The Comprehension Gap in LLM-Assisted Software Development: An Experiment

## Summary

Studies whether developers understand code they generate with LLM
assistance as well as code they write themselves or unfamiliar code they
have never seen, motivated by concern that heavy LLM use creates
"cognitive debt" that must be repaid before developers can work
efficiently again. The authors ran a crossover experiment with 35
participants (students, academic staff, and professional developers), who
completed two programming tasks with or without LLM chat assistance, then
tried to find mutations introduced into both the code they had just
produced and unseen code, supplemented by interviews and screen
recordings. Quoted directly: "36% of participants report a better
understanding of self-written code compared to their generated code."
Participants solved the comprehension task roughly 20% faster and found
about 11% more mutations in self-written code than in LLM-assisted code.
They needed significantly less time for the programming tasks themselves
when using the LLM. Quoted: "participants with high reliance on the LLM
chat and low task engagement showed significantly decreased
comprehension" — an interaction effect, not reliance alone. Qualitative
responses ranged from accepting the comprehension gap, to changing
prompting habits, to avoiding the tools entirely.

## Why it matters

For engineering teams adopting AI coding assistants: direct experimental
evidence — not just a plausibility argument — that comprehension loss from
LLM assistance is conditional (high reliance *combined with* low
engagement), not an automatic cost of using the tools, giving teams a
concrete lever (keep engagement high even under high reliance) rather than
an all-or-nothing choice between speed and understanding. The ~20%/~11%
comprehension-task gap is also a usable baseline for measuring whether a
team's own AI-assisted workflow is producing the same effect.

## Verification notes

arXiv abstract page fetched directly (2026-11-20); title, full author
list, and an 18 November 2026 submission date confirmed. Verbatim quotes
obtained for the 36% self-reported comprehension claim and the reliance-
times-engagement interaction finding; the ~20% faster / ~11% more
mutations figures are as summarized (stated as averages) from the
abstract. Full paper (experimental task design, statistical tests, full
interview coding) not read at capture. No independent secondary
corroboration attempted (new working paper, no secondary coverage found
this run).

## Updates

None yet.

## Related entries

None yet.
