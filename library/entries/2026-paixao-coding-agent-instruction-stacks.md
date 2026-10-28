---
slug: 2026-paixao-coding-agent-instruction-stacks
title: "Hidden in Plain Sight: an Empirical Study about The Instruction Stacks of Coding Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.37332
canonical_ids: ["arxiv:2610.37332"]
publisher_or_author: "Felipe de Sant'Anna Paixão, Dhyego Tavares, Eduardo Almeida, Iftekhar Ahmed"
published: 2026-10-27
captured: 2026-10-28
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on harness and context engineering (lens 2): a large-scale,
  longitudinal, cross-agent empirical study of what coding agents actually
  send models (instructions, tool definitions, environment context) across
  1,886 releases of five agents, with a concrete, actionable finding
  (documentation of revision rationale is incomplete) that a builder or
  researcher could act on this quarter.
---

# Hidden in Plain Sight: an Empirical Study about The Instruction Stacks of Coding Agents

## Summary

Studies the "instruction stacks" that coding agents send to models alongside
the user's prompt — added instructions, tool definitions, and environmental
context — across the first model requests from 1,886 releases of five
coding agents: Claude Code, Codex, Gemini CLI, Qwen Code, and OpenCode. The
authors analyze each stack's composition and evolution under controlled
conditions and link changes in the four open-source agents to documented
motivations. Looking only at the system prompt, or reporting only the
model used, gives an incomplete picture of what the agent actually sends:
tool definitions make up most of the latest requests for three of the five
agents. Occasional concentrated revisions change instructions about tool
use, attribution, and coding style — changes that can make it harder to
tell which contributions were agent-authored and to interpret generated
code. Only 48% of the examined change units directly explain why a stack
was revised. Despite increasingly distinct wording, the agents share
common capabilities (unverified: the precise definition of "common
capabilities" beyond what the abstract states).

## Why it matters

Gives builders and researchers evaluating or comparing coding agents a
concrete reason not to treat "the system prompt" or "the model" as the
whole picture of what an agent sends — tool definitions dominate the
request for most agents studied, and revisions to instructions, tool use,
and attribution happen with incomplete documented rationale. A directly
actionable recommendation: document instruction stacks alongside releases
and models, and preserve the rationale for revisions, especially where
those revisions affect code-authorship attribution.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-28; single version,
submitted 27 Oct 2026, 14:38 UTC). The scope (1,886 releases, five named
agents), the composition finding (tool definitions dominate for three
agents), and the "48% of change units explain revision rationale" figure
trace to the fetched abstract text. Full methodology and the per-agent
breakdown were not independently reviewed beyond the abstract.

## Updates

None yet.

## Related entries

None yet.
