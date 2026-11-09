---
slug: 2026-segal-agents-patch-path-security-remediation
title: "Agents on the Patch Path: Mining AI-Associated Security Remediation in GitHub Security Advisories"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.09808
canonical_ids: ["arxiv:2611.09808"]
publisher_or_author: "Claudio Segal, Paulo Segal, Hudson Silva Borges, Paulo Silveira, Daniel S. Menasché, Eduardo Santana de Almeida, Felipe de Sant'Anna Paixão, Joanna C. S. Santos, Anton Kocheturov, Gaurav Srivastava, Raphael Machado"
published: 2026-11-06
captured: 2026-11-09
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on AI-assisted software development (lens 7) and
  reproducibility/governance (lens 6): a large-scale empirical mining study
  (469 candidate advisories across 189 repositories) establishing, with a
  reproducible detection pipeline, that coding agents are already involved
  in real-world security remediation, including high/critical-severity
  fixes — evidence, not a demo or opinion piece.
---

# Agents on the Patch Path: Mining AI-Associated Security Remediation in GitHub Security Advisories

## Summary

The authors study whether autonomous coding agents take part in real-world security fixes — previously poorly documented — by mining commits linked to reviewed GitHub Security Advisories (GHSAs). They built a local-Git mining pipeline that detects agent activity through known agent accounts, commit-message attribution, repository instruction files, and agent configuration artifacts, then characterized the affected vulnerabilities and compared review-lag timing to each advisory's disclosure route.

The pipeline yielded 469 candidate advisories across 189 repositories: 448 with direct attribution, 21 supported only by repository-level evidence. Claude was the most frequently observed tool, followed by Copilot and Cursor. Against advisories published in the same months, candidate advisories had a modestly longer mean review lag, attributed mostly to timing within disclosure routes rather than a different mix of routes. Against a historical baseline, they had substantially shorter mean review lags, driven by both route composition and within-route timing. The authors conclude agent involvement is already observable across hundreds of advisories, including high- and critical-severity vulnerabilities.

## Why it matters

The first large-scale empirical evidence (rather than anecdote) that coding agents are already a measurable part of the real-world security-patch pipeline, with a named, reusable detection methodology (account signatures, commit attribution, instruction-file and config-artifact fingerprints) that other researchers or practitioners could apply to their own repositories or ecosystems. The mixed review-lag finding — faster than historical baseline, slightly slower than contemporaneous peers — is a specific, falsifiable data point for the AI-assisted-development productivity debate (lens 7), useful as a corrective against both "agents slow review down" and "agents have solved security patching" narratives.

## Verification notes

Fetched the arXiv abstract page directly; the pipeline description, sample sizes (469 candidates, 189 repositories, 448/21 attribution split), tool ranking, and the two comparative review-lag findings are as stated in the abstract. Load-bearing quantified claims are traced to the source; the underlying mining methodology and dataset were not independently re-run.

## Updates

None yet.

## Related entries

- [2026-mazloomzadeh-agentic-pull-requests](2026-mazloomzadeh-agentic-pull-requests.md) — the closest methodological sibling: another large-scale empirical mining study of real agentic pull requests, different outcome (security advisories vs. general PR characteristics).
- [2026-li-engineering-signals-vllm-sglang-prs](2026-li-engineering-signals-vllm-sglang-prs.md) — a comparable longitudinal PR-mining study on two specific repositories.
