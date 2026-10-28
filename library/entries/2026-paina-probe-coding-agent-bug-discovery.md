---
slug: 2026-paina-probe-coding-agent-bug-discovery
title: "PROBE: Frontier Coding Agents Find Different Bugs Than Maintainers Fix"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.35987
canonical_ids: ["arxiv:2610.35987"]
publisher_or_author: "Marco Paina, Mark Niklas Müller, Niels Mündler-Sasahara, Martin Vechev"
published: 2026-10-26
captured: 2026-10-28
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation and validation (lens 4): a new benchmark built from
  2,457 real maintainer-fixed bugs across 20 repositories over 18 months,
  with a matching methodology against a necessarily partial reference set
  and quantified recall/precision results — directly usable by anyone
  evaluating proactive bug-finding agents.
---

# PROBE: Frontier Coding Agents Find Different Bugs Than Maintainers Fix

## Summary

Introduces PROBE, a benchmark for evaluating proactive bug-discovery by
coding agents, built from 2,457 bugs that human maintainers fixed over 18
months across 20 GitHub repositories, together with a method for matching
an agent's reported findings against this necessarily partial reference
set. Across frontier models tested, agents reach recall below 21% and
precision below 9%. Stronger models raise recall from about 8% to 17% but
do not improve precision. Despite the low precision, LLM and human
evaluators judge 85% of the agents' findings valid — i.e., most flagged
issues are real bugs, just not ones matching the maintainer-fix reference
set. Bug distributions are similar across different agents but differ
substantially from the distribution of maintainer-fixed bugs (unverified:
the specific statistical test or measure used for "differ substantially,"
beyond what the abstract states).

## Why it matters

Gives anyone evaluating or deploying proactive bug-finding agents a
benchmark and a matching methodology that accounts for the fact that no
fixed reference set of bugs is complete — and a concrete warning that
precision/recall against maintainer fixes understates validity (85% of
flagged findings are valid bugs even when most don't match the reference
set). Useful as a benchmark to cite or extend, and as a reminder that
evaluation against "what maintainers fixed" is a lower bound on an agent's
real bug-finding capability.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-28; single version,
submitted 26 Oct 2026). The benchmark's construction (2,457 bugs, 20
repositories, 18 months), the quantified recall/precision figures (<21%,
<9%, 8%→17% with stronger models), and the "85% of findings judged valid"
figure trace to the fetched abstract text. Full benchmark methodology and
the matching algorithm were not independently reviewed beyond the
abstract.

## Updates

None yet.

## Related entries

None yet.
