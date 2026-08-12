---
slug: 2026-vu-skillspector-agent-skill-scanner
title: "SkillSpector: auditing AI agent skills for hidden vulnerabilities"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/from-green-checkmark-to-real-judgment-auditing-ai-agent-skills-with-skillspector/
canonical_ids: []
publisher_or_author: "Chien Vu Minh — Towards Data Science"
published: 2026-07-22
captured: 2026-07-23
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on the security/governance and tool-use lenses: a concrete, usable
  scanning methodology for Markdown-based agent-skill packages (deterministic
  pattern/CVE matching plus layered LLM semantic passes), with a quantified
  false-positive-filtering result. Directly applicable for anyone installing
  or distributing agent skills. Discovered in the 22-23 Jul 2026 window via
  Towards Data Science.
---

# SkillSpector: auditing AI agent skills for hidden vulnerabilities

## Summary

Practitioner write-up (Chien Vu Minh, Towards Data Science, 22 July 2026)
describing SkillSpector, reported as an NVIDIA open-source scanner that
evaluates agent "skills" (SKILL.md files and bundled scripts) before
installation. Per the article, it combines a static layer (pattern matching
and CVE lookups) with three parallel LLM-based semantic passes — hunting for
prompt injection, developer-intent violations, and policy issues — followed
by a fourth model pass that filters findings for genuine risk. On a
deliberately malicious test skill it returned a 100/100 "do not install"
score; on a legitimate GitHub-automation skill, the static layer alone
produced 20 findings, which semantic filtering reduced to 4 representing
real behavior worth scrutinizing. The article states the static layer runs
at roughly 20% precision on legitimate skills, catching obvious threats but
generating substantial noise without the semantic filtering stage.

## Why it matters

The core transferable lesson: a raw static-analysis score on natural-language
"skill" instructions is not a reliable install/block signal on its own — the
semantic-filtering stage is what turns a noisy pattern-match count into an
actionable decision. For any project (like this one) that installs or writes
agent skills, this is a directly usable control pattern: don't gate on static
findings alone, and expect roughly 4-in-5 static hits on a legitimate skill
to be noise absent a semantic pass.

## Verification notes

Article fetched and read in full; the mechanism description, the two
worked examples (malicious-skill score, legitimate-skill filtering from 20
to 4 findings), and the precision figure are traced directly to the source
text. Not independently corroborated: NVIDIA's own repository or
announcement for SkillSpector was not separately located or fetched this
run, so the tool's authorship and existence rest on this single commentary
source — verification recorded as **partial** on that basis, though the
technical claims themselves are clearly traceable to the article.

## Updates

*(none yet)*

## Related entries

[2026-liu-openskillrisk-benchmark.md](2026-liu-openskillrisk-benchmark.md) — a benchmark quantifying the same underlying problem (agents unsafely executing risky third-party skills) that this scanner is designed to catch before install time.
