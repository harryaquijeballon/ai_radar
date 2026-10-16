---
slug: 2026-favaro-clark-when-ai-builds-itself
title: "When AI builds itself"
status: accepted
domains: [social_science, ai_engineering]
source_type: commentary
source_url: https://www.anthropic.com/institute/recursive-self-improvement
canonical_ids: []
publisher_or_author: "Marina Favaro, Jack Clark — The Anthropic Institute"
published: unknown
captured: 2026-10-16
relevance:
  social_science: medium
  ai_engineering: medium
verification: partial
rationale: >-
  Social science lenses 1 and 4: an essay on recursive self-improvement that
  combines public benchmark trends, first-party data on AI's share of one
  lab's engineering and research work, and policy options for coordinating a
  slowdown or pause. AI engineering lens 7: measured, though self-reported,
  figures on coding-agent output in a real codebase. Medium in both because
  it is commentary built on one lab's internal data. Backfilled at the
  user's request.
---

# When AI builds itself

## Summary

An essay asking whether AI is beginning to accelerate its own development, with evidence from public benchmarks and from inside Anthropic. It sets out possible futures and policy options.

**External trends cited:**
- The length of task models can reliably complete on their own has been "doubling roughly every four months", up from an earlier seven-month trend.
- On the most open-ended tasks, Claude's success rate reached 76% in May 2026, "up 50 percentage points in six months".

**First-party data:**
- As of May 2026, more than 80% of the code merged into Anthropic's codebase was authored by Claude.
- In Q2 2026, the typical engineer merged 8× as much code per day as in 2024. The authors themselves flag this as "almost certainly an overstatement" of true productivity, because lines of code measure quantity rather than quality.
- A March 2026 poll of 130 employees across research teams is reported (median self-estimated output gain).
- In an automated alignment-research experiment, agents recovered 97% of a performance gap over 800 cumulative hours (about $18,000 of compute), against roughly 23% for two human researchers over about a week.

**Policy:** the essay argues it would be good for the world to have the option to slow or temporarily pause frontier AI development, so that societal structures can adapt, and discusses ways to coordinate that.

## Why it matters

For economists, this is the micro-level evidence behind the "AI automates research" channel that macro models treat as a parameter. It is a useful counterpoint to [2026-korinek-economic-scenarios-transformative-ai](2026-korinek-economic-scenarios-transformative-ai.md), whose innovation block finds this channel small by 2030. For builders, the code-authorship and output figures are among the few at-scale numbers on coding agents in real use. The authors' own warning that lines of code overstate productivity is the right way to read them. All internal figures come from a lab with a direct stake in the narrative and cannot be independently checked.

Not to be confused with "The Economics of Recursive Self-Improvement" (Cunningham et al., arXiv:2609.15802), a separate paper that this library rejected on 2026-09-15 for a discovery-window reason.

## Verification notes

The page was fetched on 2026-10-16 and its raw text checked string by string for every figure in the Summary: "four months"/seven months, 76% and +50 pp, more than 80%, 8×, 130 employees, 97%/23%/800 hours/$18,000, and the pause passage. Two figures in an automated summary of the page could not be found in its text and were left out: a "52×" experiment speed-up and an update "from about 26% to 91%". The page states no publication date, only an "Update 9/18/2026" heading, so `published` is recorded as unknown. Partial: claims trace to the source, but the first-party figures cannot be corroborated externally. The cited external sources (METR, CORE-Bench) were not re-checked.

## Updates

- None yet.

## Related entries

[2026-favaro-measuring-pace-ai-development-frontier-labs](2026-favaro-measuring-pace-ai-development-frontier-labs.md) — companion Institute piece proposing reportable measures of the same acceleration; shares an author.
[2026-korinek-economic-scenarios-transformative-ai](2026-korinek-economic-scenarios-transformative-ai.md) — macro model in which the AI-research channel stays small by 2030.
