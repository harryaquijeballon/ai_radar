---
slug: 2026-liu-copilot-culprit-bug-reporting
title: "Copilot or Culprit? How AI Is Changing Open-Source Bug Reporting and Maintenance"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.25605
canonical_ids: ["arxiv:2611.25605"]
publisher_or_author: "Yinuo Liu, Yunlong Lyu, Zichao Luo, Tian Dong, Zian Luo, Peng Chen, Hao Chen — arXiv preprint"
published: 2026-11-19
captured: 2026-11-21
relevance:
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 7 (AI-assisted software development): the largest empirical
  study to date of AI's role in open-source bug reporting and maintenance
  (120,918 reports, 101 projects, Jan 2024-Sep 2026), with a measured,
  actionable distinction between AI uses that correlate with higher report
  validity and uses that do not, plus a tested reporting-guidance protocol.
---

# Copilot or Culprit? How AI Is Changing Open-Source Bug Reporting and Maintenance

## Summary

Traces AI involvement across 120,918 bug reports from 101 open-source
projects (January 2024-September 2026), from discovery and reporting
through validation and resolution. AI-involved reports become more
complete over time, and a growing share are confirmed as valid. In
reporting, using AI for reproduction and diagnosis correlates with higher
report validity, while using AI for report writing alone does not. In
maintenance, maintainers increasingly use AI to investigate code and
recommend fixes, but spend more effort on AI-assisted reports of
human-found bugs than on reports of AI-discovered bugs — read by the
authors as evidence of AI's growing investigative role alongside a
continued need for verification and follow-up. The authors turn this into
practical guidance for converting AI-generated findings into verifiable
reports (emphasizing reproducibility, verification, and accountability),
applied it themselves to submit 53 reports of AI-discovered bugs, and
report a 69.81% maintainer-acceptance rate as of writing (unverified:
acceptance rate as stated by the authors, not independently re-counted).

## Why it matters

For teams integrating AI into bug discovery, reporting, or triage: a
measured basis for deciding *which* AI uses to trust — reproduction and
diagnosis assistance appears to raise report validity, report-writing
assistance alone does not — plus a concrete, tested protocol (and a
real acceptance-rate result) for turning AI-discovered bugs into reports
maintainers will actually accept.

## Verification notes

arXiv abstract page fetched 2026-11-21 (paraphrased summary; full abstract
text not reproduced verbatim due to tool quoting limits). Submission
history shows v1 submitted Thu, 19 Nov 2026, 06:53:32 UTC — within this
run's discovery window (2026-11-20 → 2026-11-21) and the 7-day eligibility
cap. Scale figures (120,918 reports, 101 projects, date range, 53 reports,
69.81% acceptance) are traced to the fetched summary; the underlying
statistical tests for the "correlates with higher validity" claims were
not independently re-derived, so verification is partial. No secondary
coverage found (new preprint).

## Updates

None yet.

## Related entries

None yet.
