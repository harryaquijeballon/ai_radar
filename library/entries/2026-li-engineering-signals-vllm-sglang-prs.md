---
slug: 2026-li-engineering-signals-vllm-sglang-prs
title: "Engineering Signals of Human-AI Collaboration in the Agentic Coding Era: A Longitudinal Analysis of 33,228 Pull Requests from vLLM and SGLang"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.13884
canonical_ids: ["arxiv:2608.13884"]
publisher_or_author: "Jiada Li, Xuesong Ye, Olamide Olowoniyi — arXiv preprint (cs.SE)"
published: 2026-08-14
captured: 2026-08-17
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 7 (AI-assisted software development): a quantified longitudinal
  analysis of 33,228 pull requests across two major AI-infrastructure
  open-source projects (vLLM, SGLang), decomposing throughput and review-load
  changes into human- vs bot-driven contributions — concrete benchmark
  figures a team could compare its own AI-assisted development metrics
  against.
---

# Engineering Signals of Human-AI Collaboration in the Agentic Coding Era: A Longitudinal Analysis of 33,228 Pull Requests from vLLM and SGLang

## Summary

The paper analyzes seven software-engineering metrics across 18,290 pull requests from vLLM (Feb 2023–June 2026) and 14,938 from SGLang (Jan 2024–June 2026), segmenting development into four eras aligned with major changes in AI-assisted software development. Headline findings: PR throughput rose 21x in vLLM and 17.9x in SGLang, with less than 0.2% of that growth attributable to bot-authored PRs — i.e., human-driven contributions dominated the velocity increase. Comment density rose 4.2x (vLLM) and 3.8x (SGLang), with bots contributing an estimated 15–20% of that increase. Median PR cycle time was 1.04 days (vLLM) and 0.62 days (SGLang), with P90 times of 16.8 and 14.3 days respectively; PR size stayed relatively stable across periods. The paper's title also claims implications for biomedical AI agents and bioinformatics pipeline development; that connection was not read in this pass and is marked (unverified) here.

## Why it matters

Gives engineering leads concrete throughput and cycle-time benchmarks from two real, high-velocity AI-infrastructure projects to compare against when assessing how much of their own team's velocity gains from agentic coding tools are genuinely AI-driven versus human-driven — directly serves lens 7's interest in measured results and transferable practices, rather than anecdotal claims about AI coding-tool impact.

## Verification notes

Read via the arXiv abstract page and search summary (2026-08-17). The headline quantitative figures (throughput multiples, comment-density multiples, cycle times, dataset sizes and date ranges) are quoted/paraphrased directly from the abstract. Not independently corroborated against a second source or the paper's full results tables; the bibliometric methodology (the four-era segmentation, metric definitions) was not independently checked. The abstract's claimed relevance to biomedical AI agents and bioinformatics pipelines is unverified — not read in this pass.

## Updates

None yet.

## Related entries

- [2026-mazloomzadeh-agentic-pull-requests](2026-mazloomzadeh-agentic-pull-requests.md) — same-topic: another empirical study of agentic pull requests.
- [2026-liang-decode-developer-edits-ai-code](2026-liang-decode-developer-edits-ai-code.md) — related: developer-side editing behaviour on AI-generated code, a complementary signal to this paper's throughput/review metrics.
