---
slug: 2026-favaro-measuring-pace-ai-development-frontier-labs
title: "Measurements for understanding the pace of AI development inside frontier labs"
status: accepted
domains: [social_science, ai_engineering]
source_type: primary
source_url: https://www.anthropic.com/institute/measuring-pace-of-ai-development
canonical_ids: []
publisher_or_author: "Marina Favaro, Phillie Wright — The Anthropic Institute"
published: 2026-09-17
captured: 2026-10-16
relevance:
  social_science: medium
  ai_engineering: medium
verification: partial
rationale: >-
  Social science lens 4: proposes three measurements a frontier developer
  could disclose (share of AI R&D led by AI, oversight coverage of AI agents,
  compute share going to safety), with first values for one lab. That is
  useful input to the question of what regulators could ask labs to report.
  AI engineering lenses 4 and 5: reports an LLM-as-judge agreement check and
  the coverage of agent monitoring running at scale. Medium in both because
  the numbers are a single lab's self-report on prototype measures.
  Backfilled at the user's request after the Institute joined the watchlist.
---

# Measurements for understanding the pace of AI development inside frontier labs

## Summary

The Institute argues that the outside world cannot see how fast AI development is moving inside frontier labs. It proposes three measurement prototypes, framed as "What any AI developer could report today", each with Anthropic's own first values.

**1. AI R&D automation.** About 15,000 tasks, catalogued bottom-up from internal sources, are organised into a tree of 542 nodes (378 leaves). Each is rated on Epoch AI's six-level automation scale by a Claude judge, with weights based on person-time. Results:
- Claude "leads" (level AL4: completes most of the task end to end) 26% of Anthropic's AI R&D work.
- The share at or above "AI collaborates" is above 90%.
- No measured subset of work is fully autonomous (AL5).
- Judge reliability: model-versus-human exact agreement was 59%, against 35% for human-versus-human.

**2. Oversight of AI agents.** As of August 2026, about 30,000 agents were doing research and engineering work on the main internal platform. Every agent action passes through an online monitor before it runs, and 0.002% (about 1 in 47,000) were blocked over August 2026.

**3. Compute allocation.** Over one examined week, about 6% of the compute that went to AI R&D was allocated to safety, rising to about 12% of compute that went to AI-driven AI R&D. The authors call these "deliberately conservative estimates", produced by a Claude-based workload classifier over a sample of runs.

## Why it matters

For policy work, this is a concrete answer to the question of what a lab could disclose about internal acceleration. It turns "is AI speeding up AI research?" into three reportable indicators with a stated method, which a regulator or an outside researcher could ask other developers to match. The judge-reliability figure is the most transferable detail for research practice: the model judge agreed with humans more often than humans agreed with each other (59% vs 35% exact). That is a reminder that low human agreement, not just model error, limits task-level automation measures. Read every value as one vendor's self-report on its own prototype measures: none can be checked from outside, and the publisher has a direct stake in how its pace of development is perceived.

## Verification notes

The page was fetched on 2026-10-16 and its raw text checked string by string, with a deterministic script, for every figure in the Summary: 26%, above 90%, 542/378, 15,000, 59%/35%, 30,000, 0.002%, 6%/12%, and AL4/AL5. The publication date comes from the publisher's research index (www.anthropic.com/research lists the item as "Sep 17, 2026"); the article page itself carries no date. Partial: every claim traces to the source, but all values are internal measurements with no independent corroboration available. The linked Advanced AI Framework and August 2026 risk-report PDFs were not reviewed.

## Updates

- None yet.

## Related entries

[2026-favaro-clark-when-ai-builds-itself](2026-favaro-clark-when-ai-builds-itself.md) — companion Institute piece on AI accelerating AI development; shares an author.
[2026-korinek-economic-scenarios-transformative-ai](2026-korinek-economic-scenarios-transformative-ai.md) — Institute macro scenarios whose innovation channel this lab-level evidence bears on.
