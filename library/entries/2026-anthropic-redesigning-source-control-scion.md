---
slug: 2026-anthropic-redesigning-source-control-scion
title: "Redesigning source control at Anthropic"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://www.anthropic.com/engineering/redesigning-source-control
canonical_ids: []
publisher_or_author: "Anthropic — Anthropic Engineering blog"
published: 2026-10-13
captured: 2026-10-14
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  AI-engineering lens 7 (AI-assisted software development at scale) with some
  lens 2 relevance: a first-party account of rebuilding source control for
  agent-scale merge volume. Medium because the figures are vendor-reported
  and the system is internal, so the transferable part is the design
  principles rather than a tool a builder can adopt.
---

# Redesigning source control at Anthropic

## Summary

Anthropic's engineering blog (2026-10-13) describes why and how it replaced git for its monorepo. Per the article, merged code changes grew from about 2,500 per day in May 2026 to over 30,000 per day by September, and source control became the main development bottleneck; the main-branch history is nearly 100 GB and CI performs about 25 million checkouts per day. A seven-person team migrated to an in-house system, Scion, in five months and also built a review tool, Antique. Reported results: about 200x smaller CPU and memory footprint than the previous git mirror fleet, CI and research checkouts dropping from minutes to seconds, about a 25% CI CPU capacity gain, and cache-tier hit rates above 99%. Design principles stated: clients assumed always online (most are agents and jobs), server-side cheap lock-free commits, source control exposed through APIs, optional sparse or virtualized working copies, and tiered caching. Antique expresses semantic approval rules that separate trivial from sensitive changes. Stated lessons on AI-assisted development: engineers often had to tell Claude "no" when it violated system constraints, adversarial AI review can be over-defensive, and a global merge-queue lock does not suit agent-scale merging, so the team relies on post-merge and pre-deploy testing. The article says Scion is not a general git replacement.

## Why it matters

A concrete, first-party data point on what changes when agents, not humans, dominate commit volume: assumptions such as offline work, human-paced merge queues and local clones stop holding. Builders of agent-driven development pipelines can borrow the principles (API-first access, tiered caching, risk-tiered review, post-merge testing) without the system itself. Treat all figures as Anthropic's own and not independently measured.

## Verification notes

Source reachable and read in full via the anthropic.com article page; claims above traced to its text. Simon Willison's 2026-10-13 post quotes and summarises the same figures, but it derives from the same source, so it is not independent corroboration. No external measurement of the performance or volume claims. Hence `partial`.

## Updates

None yet.

## Related entries

None yet.
