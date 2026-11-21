---
slug: 2026-asada-code-review-rule-reuse
title: "From Code Review Comments to Reuse in Production: An Industrial Study of Extracted Rules"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.25918
canonical_ids: ["arxiv:2611.25918"]
publisher_or_author: "Mutsuha Asada, Yuhei Nakasaka, Keito Tabuchi, Shinpei Hayashi — arXiv preprint"
published: 2026-11-19
captured: 2026-11-21
relevance:
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 7 (AI-assisted software development, code review by/of AI):
  a 65-day production trace of a rule-extraction-and-reuse system showing
  that the standard metric teams use to judge which extracted rules are
  worth keeping (how often later comments cite them) does not track what a
  rule actually contributed, with a proposed per-stage auditing alternative.
---

# From Code Review Comments to Reuse in Production: An Industrial Study of Extracted Rules

## Summary

Studies Kleene, a production system that turns organization-specific code
review comments into rules a language model applies to later changes, over
65 days of real use. Of 56 clauses in 12 rules that later review comments
cited as their reason for firing, only 2 were explicit in the original
review thread that produced the rule; 38 added a condition not stated in
that thread, and 16 had no locatable source passage at all. Of 79 further
comments naming those rules, 45 requested no change, and 27 of those still
said the rule applied — a case the authors treat as weak evidence the rule
helped. In a controlled test on 20 constructed changes, a reviewer given
only the original review thread met detection criteria on 8 of 10 changes
that required a report; given the extracted rule instead, it met them on
10 of 10, though the confidence interval for that gap includes zero
(unverified: exact statistical test not confirmed from the abstract alone).
Across 464 rules deployed while a rule-based reviewer subagent ran, 259
(55.8%) were ever named, 195 (42.0%) produced a comment that wasn't
withheld, and 94 (20.3%) led to a recorded code change — with the largest
drop-off occurring before any rule was even named. Keeping only the
top-ranked half of rules preserved 53.8% of those that later produced a
non-withheld comment, versus 49.2% under random selection, again a
difference whose confidence interval includes zero.

## Why it matters

For anyone building or operating an LLM-based code-review system that
extracts reusable rules from past review comments: a direct warning that
citation-count popularity is not evidence of a rule's value, with a
concrete alternative — trace each rule back through naming, non-withheld
comments, and recorded code changes as separate stages, and compare each
rule against the specific thread it was extracted from, rather than
trusting an aggregate citation tally to decide what to keep.

## Verification notes

arXiv abstract page fetched 2026-11-21 (paraphrased summary; full abstract
text not reproduced verbatim due to tool quoting limits). Submission
history shows v1 submitted Thu, 19 Nov 2026, 11:04 UTC — within this run's
discovery window (2026-11-20 → 2026-11-21) and the 7-day eligibility cap.
The quantified figures (56 clauses/12 rules, 79 comments, 464 rules, 259/
195/94 counts, 53.8% vs 49.2%) are traced to the fetched summary; the exact
statistical method behind the "confidence interval includes zero" claims
was not independently re-derived, so verification is partial. No secondary
coverage found (new preprint).

## Updates

None yet.

## Related entries

None yet.
