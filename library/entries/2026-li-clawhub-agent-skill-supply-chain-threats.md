---
slug: 2026-li-clawhub-agent-skill-supply-chain-threats
title: "Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.30932
canonical_ids: ["arxiv:2611.30932"]
publisher_or_author: "Li Kaixuan et al."
published: 2026-11-24
captured: 2026-11-24
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  Lens 6 (reproducibility, security, governance): a registry-scale study
  (all 48,682 skills on ClawHub) quantifying real, reachable vulnerabilities
  in agent-skill packages, distinguishing carried-over (dependency) from
  agent-native (install-instruction, credential-leak) risks with sandbox
  and live-agent reachability testing — directly actionable for anyone
  running or publishing agent skills.
---

# Carried-Over and Agent-Native Threats in the Supply Chain of LLM Agent Skills

## Summary

This paper studies security risks in reusable "agent skill" packages, which bundle scripts, third-party dependencies, and natural-language instructions for LLM agents. Because agents build skill arguments from user requests and untrusted external content, a flaw left by a well-intentioned skill author could let a prompt injection escalate to code execution; the authors note that prior work focused on deliberately malicious skills or single attack vectors and did not test whether agents can actually reach such flaws in practice.

The authors ran a registry-scale study of all 48,682 skills on ClawHub, examining two carried-over risks (dependencies, first-party code) and two agent-native risks (install instructions, credentials printed to stdout), via static analysis across all skills, manual review of the 3,428 flagged cases, sandboxed reachability testing on a sample, and a live LLM agent tested under indirect prompt injection. Findings: 49.6% of skills with resolvable dependencies use a version with a known CVE, and 78.3% of those were already vulnerable at publication (unlike npm packages, which typically become vulnerable after release) — but agent input reaches the vulnerable function in only 3.0% of affected skills. First-party code flaws were far more exploitable: 21 of 22 sampled flaws were exploited end to end in sandbox testing. In the live-agent test, the agent executed an injected payload in 48.5% of sampled flagged skills, but mostly in its own shell before the skill ran; the payload reached a flaw inside the skill itself in only 5.0% of cases. The authors recommend registries prioritize first-party flaws over dependency alerts, and that agent runtimes stop passing skill arguments through a shell.

## Why it matters

A rare registry-wide (not sampled) empirical measurement of which agent-skill vulnerability classes are actually reachable by an agent in practice, not just theoretically present — the finding that dependency CVEs are common but rarely reachable (3.0%), while first-party code flaws are rare but almost always exploitable when present (21/22), gives skill-registry maintainers and agent-runtime builders a concrete prioritization rule instead of a generic "patch your dependencies" recommendation.

## Verification notes

Fetched directly from arXiv; abstract and metadata confirmed (v1 submitted 23 November 2026, within the discovery window; primary category cs.CR, cross-listed cs.SE). All figures above are as stated in the abstract. The static-analysis/manual-review pipeline and the live-agent prompt-injection setup were not independently re-derived from the full paper text, only the abstract.

## Updates

None yet.

## Related entries

- [2026-yang-skillgate-malicious-skill-detection](2026-yang-skillgate-malicious-skill-detection.md) — related prior work on detecting malicious skill files at runtime.
- [2026-vu-skillspector-agent-skill-scanner](2026-vu-skillspector-agent-skill-scanner.md) — related prior work on auditing agent skills for hidden vulnerabilities.
