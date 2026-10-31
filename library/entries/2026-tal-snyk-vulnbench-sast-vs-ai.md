---
slug: 2026-tal-snyk-vulnbench-sast-vs-ai
title: "How Deterministic SAST and AI Security Agents Divide the Work: Coverage, Harness Policy and Cost in Snyk VulnBench 2.0"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.38617
canonical_ids: ["arxiv:2610.38617"]
publisher_or_author: "Liran Tal, Chris Liu, Charlotte Fereday, Sebastian Roth, Brian Clark — arXiv (cs.CR); Snyk"
published: 2026-10-28
captured: 2026-10-31
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Squarely on lens 4 (evaluation of AI output against deterministic
  checks): a blind, quantified comparison of static analysis versus AI
  coding-security agents on a hand-curated vulnerability benchmark, with a
  practical, falsifiable conclusion (use both) and a harness-matters
  finding. Vendor-authored (Snyk) — scored on the benchmark's own
  transparency and reproducibility, not on the publisher's claims.
verification: verified
---

# How Deterministic SAST and AI Security Agents Divide the Work: Coverage, Harness Policy and Cost in Snyk VulnBench 2.0

## Summary

The paper asks what AI coding agents and AI security harnesses find that
deterministic static application security testing (SAST) misses, and vice
versa, using VulnBench 2.0: 108 hand-curated, attacker-reachable
vulnerabilities across 20 open-source web apps in Go, JavaScript/TypeScript,
Python, and Java (62 spanning more than one file). A finding counts only if
it correctly locates both the attacker-controlled source and the dangerous
sink, each within two lines. Nine product configurations were tested under
one blind protocol, including Snyk Code, Claude Code's /security-review,
Codex Security, and the DeepSec scanner. Snyk Code reached 82.4% recall (89
of 108); Claude Code with Opus 5 at xhigh effort reached 79.3% (85 of 108) —
a gap too small to separate the two reliably. Neither tool alone was
sufficient: together they found 101 of 108. The AI configurations also
reported at least seven real vulnerabilities outside the reference set that
Snyk Code missed. The harness mattered as much as the model: without Claude
Code's built-in review policy, the same model found 16 of 20 vulnerabilities
in classes the policy excludes or restricts, versus 9 of 20 with the policy
active (a supplementary run on 19 of 20 apps). Codex Security located 80
vulnerabilities at file level but only 34 at line level. DeepSec's
model-free file selection covered only 56 of 108 flows. Coverage and cost
were only loosely related. The harness, fixtures, reference set, and run
data are stated as publicly available.

## Why it matters

A rare blind, apples-to-apples comparison (not a vendor's own cherry-picked
benchmark) showing that combining deterministic SAST with an AI security
agent beats either alone, and — more importantly for harness design — that
a tool's own safety/review policy can materially suppress findings in
excluded vulnerability classes, a hidden cost of guardrail design that
builders configuring AI security tooling need to account for explicitly.

## Verification notes

Read directly from the arXiv abstract page (arXiv:2610.38617, v1 submitted
28 Oct 2026, primary cs.CR, cross-listed cs.AI/cs.SE). The benchmark size
(108 vulnerabilities, 20 apps), the recall figures for each configuration
(82.4%, 79.3%, combined 101/108, 80/34 file/line for Codex, 56/108 for
DeepSec), and the 16-vs-9 policy-suppression finding are traced to the
abstract text itself. The paper is authored by Snyk employees about Snyk's
own product category; this is flagged rather than treated as neutral, though
the blind multi-vendor protocol and stated public availability of the
benchmark/run data mitigate the conflict. No independent corroboration of
raw run data was attempted.

## Updates

None yet.

## Related entries

None yet.
