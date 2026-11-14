---
slug: 2026-gottesman-multiloop-evolving-harnesses
title: "MULTILOOP: Evolving Multi-Agent Harnesses for Complex Information-Seeking Tasks"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.15754
canonical_ids: ["arxiv:2611.15754"]
publisher_or_author: "Daniela Gottesman, Gal Yona, Ori Ram, Zorik Gekhman, Jonathan Herzig, Mor Geva, Roee Aharoni — arXiv preprint (cs.MA); NeurIPS 2026 CL4FMAgents Workshop"
published: 2026-11-11
captured: 2026-11-14
relevance:
  social_science: n/a
  ai_engineering: medium
rationale: >-
  Medium on lens 1/2 (agent architecture, harness engineering): a
  self-evolution loop where a coding agent edits its own multi-agent
  harness, with quantified but modest gains (4.6% over the base harness)
  and an honest failure-mode analysis showing orchestration failures
  largely persist — on-lens, workshop-validated, but early rather than a
  settled, broadly transferable technique.
verification: verified
---

# MULTILOOP: Evolving Multi-Agent Harnesses for Complex Information-Seeking Tasks

## Summary

The paper studies whether automated optimization can diagnose and repair
failures in multi-agent LLM systems, using complex information-seeking tasks
from DeepSearchQA. MULTILOOP is a loop in which a coding agent analyzes,
evaluates, and edits the harness itself — the prompts, tools, and
orchestration logic binding the multi-agent system together — rather than
tuning prompts in isolation. With only 10 training samples, the evolved
harness improved accuracy by 4.6% over the base harness and by 3.2% over the
best single-agent system tested. Failure-mode analysis found that
orchestration failures (how agents delegate and share information) largely
persisted despite the harness edits, which the authors argue motivates
future work on methods that change delegation and information-sharing
patterns directly rather than just the surrounding harness code. The paper
was accepted to the NeurIPS 2026 CL4FMAgents workshop.

## Why it matters

A concrete demonstration of harness self-evolution (an agent editing its own
multi-agent orchestration code) with a quantified, if modest, improvement
and — more usefully — an honest accounting of what this approach does *not*
fix: orchestration/delegation failures. That negative result is itself
actionable for anyone evaluating whether to invest in automated harness
optimization versus redesigning delegation logic directly.

## Verification notes

Claims traced to the arXiv abstract page, read directly. The quantified
results (4.6% and 3.2% gains, 10 training samples) and the persisting-
failure finding are drawn from the abstract text. Workshop-acceptance status
is stated on the abstract page. Full paper body was not read; no independent
corroboration of the DeepSearchQA benchmark results was sought.

## Updates

None yet.

## Related entries

None yet.
