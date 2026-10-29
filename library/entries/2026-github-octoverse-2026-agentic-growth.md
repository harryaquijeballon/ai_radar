---
slug: 2026-github-octoverse-2026-agentic-growth
title: "GitHub Octoverse 2026: Merged PRs, Commits, and New Repositories Roughly Tripled"
status: provisional
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Oct/28/github-octoverse-2026/
canonical_ids: []
publisher_or_author: "GitHub (Octoverse 2026 report, announced by EVP Jay Parikh) — relayed via Simon Willison's Weblog"
published: 2026-10-28
captured: 2026-10-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: unverified
rationale: >-
  On-profile for AI-assisted software development (lens 7) at platform
  scale — if the figures hold, a striking measured signal of agentic
  engineering's volume impact — but the load-bearing growth claims trace
  only to a commentary relay of GitHub's own report; the primary report
  (github.blog / octoverse.github.com) is not on the egress allowlist and
  was not independently fetched, and open search found no independent
  corroboration (the report appears too new to be indexed elsewhere).
  Retained provisional rather than accepted per schema's rule that
  uncorroborated load-bearing claims cap verification at partial/provisional.
---

# GitHub Octoverse 2026: Merged PRs, Commits, and New Repositories Roughly Tripled

## Summary

GitHub's annual Octoverse 2026 report, announced by EVP Jay Parikh at
GitHub Universe and relayed by Simon Willison (who disclosed receiving a
free conference ticket via GitHub's "Stars" program), reports three
headline monthly figures for 2026: merged pull requests roughly tripled
in under a year to about 220 million per month; commits rose to about
7.38 billion per month, more than tripling, with most of the increase in
the second half of the year; and new-repository creation roughly doubled
to about 30.3 million per month. Methodology notes relayed in the post:
country attribution uses an LLM to extract country codes from user
profiles to correct for VPN bias; industry classification uses a
fine-tuned multilingual embedding model on repository names, descriptions,
topics, and READMEs; "interoperability" repositories are counted by
keyword match (reverse engineering, clean-room implementation, drop-in
replacement, etc.). Willison calls the figures "a pretty stark
representation of the impact of agentic engineering on GitHub" and
raises no methodological objection of his own (unverified: whether these
methodology choices — especially the keyword-based interoperability count
and the LLM-based country attribution — were validated against ground
truth; that assessment is not in the relayed post).

## Why it matters

If accurate, platform-scale evidence (not a survey or a lab study) that
AI coding agents have driven roughly a tripling of GitHub's merged-PR and
commit volume within a year — a scale and speed relevant to anyone
reasoning about AI-assisted software development's current trajectory
(lens 7) or planning capacity around growing agent-generated contribution
volume. The entry is kept provisional specifically because this
magnitude of claim is exactly the kind of figure this project's
verification bar exists to catch before treating it as established.

## Verification notes

Read via direct fetch of Simon Willison's relay post (captured
2026-10-29; published 2026-10-28, 4:45pm, no timezone stated). The three
headline figures and the methodology notes trace to the fetched post
text. GitHub's own primary report (github.blog, octoverse.github.com) is
not on `profiles/egress_allowlist.md` and was not fetched this run, per
the Unattended-mode egress rule. A web search for independent
corroboration of the 2026 figures found only GitHub's 2025 Octoverse
figures (518.7M PRs/year, ~1B commits/year — both far below a tripling),
consistent with the 2026 report simply being too new to be indexed
elsewhere yet, not with the figures being wrong. Load-bearing claims
(the tripling figures) are therefore traced but not independently
corroborated — per schema this caps verification below "verified" even
though the relaying source (Simon Willison, a curated, trusted source)
is itself reliable. Upgrade path: a future run that can fetch GitHub's
primary report directly (if added to the allowlist) or independent press
coverage of the 2026 figures should re-attempt verification per engine P4.

## Updates

None yet.

## Related entries

None yet.
