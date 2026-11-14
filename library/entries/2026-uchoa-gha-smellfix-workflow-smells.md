---
slug: 2026-uchoa-gha-smellfix-workflow-smells
title: "GHA-SmellFix: Taking Action with Agentic LLMs for Detecting and Refactoring GitHub Actions Workflow Smells"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.14963
canonical_ids: ["arxiv:2611.14963"]
publisher_or_author: "Anderson Uchôa, Jhefferson Souza, Emanuel Ávila, Gabriel Silva, Kevin Lira, Hui Sun, Nelson Araújo, Arthur Cordeiro, Rohit Gheyi, Wesley Assunção — arXiv preprint (cs.SE, cs.MA)"
published: 2026-11-11
captured: 2026-11-14
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  High on lens 4 (evaluation/guardrails) and lens 7 (AI-assisted software
  development): a quantified empirical comparison of agent-pipeline designs
  for a real CI/CD maintenance task, with a named, transferable bottleneck
  (detection, not refactoring) and a stated engineering implication
  (abstention and construct-aware validation) rather than a bare capability
  demo.
verification: verified
---

# GHA-SmellFix: Taking Action with Agentic LLMs for Detecting and Refactoring GitHub Actions Workflow Smells

## Summary

The authors present GHA-SmellFix, an agentic LLM pipeline that detects and
refactors configuration smells in GitHub Actions workflows. They compare a
"Joint" design (one agent both detects and refactors) against a
"Decomposed" design (separate agents for each task), evaluating 19 smell
types across four LLMs on 570 sampled pairs drawn from a ground truth of
1,710 workflow-smell pairs. Decomposition does not uniformly improve patch
quality; its main value is controlling *when* a patch is attempted, which
helps models that under-detect smells and reduces unnecessary patching.
Detection — not refactoring — is the main end-to-end bottleneck, and false
positives can produce harmful edits to execution-relevant workflow code. The
authors conclude that CI/CD agents need reliable abstention mechanisms and
construct-aware validation rather than more aggressive automatic patching.

## Why it matters

Names a concrete, transferable lesson for anyone building agentic CI/CD or
code-maintenance tooling: the reliability bottleneck in this class of task is
detection accuracy, not the downstream fix, and an agent that always acts on
its own detections risks harmful edits. The abstention-plus-validation
framing is directly applicable beyond GitHub Actions to any agentic
patch-generation pipeline.

## Verification notes

Claims traced to the arXiv abstract page, read directly. The quantified
study design (19 smells, 1,710 ground-truth pairs, 570 sampled, four LLMs)
and the stated conclusions (decomposition's real value, detection as
bottleneck, the abstention/validation recommendation) are drawn from the
abstract text. Full paper body was not read; per-model or per-smell-type
breakdown figures were not independently checked.

## Updates

None yet.

## Related entries

None yet.
