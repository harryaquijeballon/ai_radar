---
slug: 2026-shanto-agent-instruction-files-template
title: "Toward an Evidence-Based Template for Agent Instruction Files: An Empirical Study of Adoption, Consistency, and Maintenance"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.02383
canonical_ids: ["arxiv:2611.02383"]
publisher_or_author: "Mehedi Hasan Shanto, Md. Anaytul Islam, Muhammad Asaduzzaman, Alioune Ngom"
published: 2026-11-02
captured: 2026-11-03
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on harness and context engineering (lens 2) and AI-assisted
  software development (lens 7): a large empirical study (3,387 files,
  1,000 repositories, four instruction-file formats) producing a
  ten-category evidence-based template, with a quantified before/after
  coverage improvement when teams follow it explicitly.
---

# Toward an Evidence-Based Template for Agent Instruction Files: An Empirical Study of Adoption, Consistency, and Maintenance

## Summary

Studies how AI coding agents' repository-level instruction files
(AGENTS.md, CLAUDE.md, GitHub Copilot instructions, Cursor rules) are
actually used, analyzing 3,387 files across 1,000 GitHub repositories.
Key findings: 42.2% of instruction-bearing repositories in the
higher-popularity cohort use multiple formats at once; 16.1% of 386
manually compared section pairs give divergent guidance between coexisting
formats; and 40.4% of files have only one recorded modification ever. From
these findings the authors derive an evidence-based template with ten
Required, four Gap, and two Recommended categories. In an exploratory
experiment, giving explicit template guidance raised structural category
coverage in generated instruction files from 18.7% to 82.8%. The paper
also introduces AGIT-Instruct, a benchmark for generating instruction
files, on which retrieval-augmented generation scored highest (ROUGE-1 F1
of 0.459); a manual review of 278 generated categories found 19.4% fully
and 61.2% partially preserved developer intent (as stated in the fetched
abstract; full template text and benchmark construction not reviewed at
capture).

## Why it matters

Gives teams writing or maintaining AGENTS.md/CLAUDE.md-style instruction
files concrete, evidence-based guidance instead of ad hoc convention:
multi-format repositories risk silently divergent instructions (16.1% of
compared sections disagreed), most instruction files are written once and
never revisited (40.4%), and following an explicit category template more
than quadrupled measured structural coverage (18.7%→82.8%) in the authors'
test. Directly usable as a checklist when auditing or authoring a
project's own agent instruction files.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 2 Nov 2026, no revisions). The 3,387-file/1,000-repository
study design, the 42.2%/16.1%/40.4% findings, the ten/four/two-category
template, the 18.7%→82.8% coverage result, and the AGIT-Instruct
benchmark figures (ROUGE-1 F1 0.459; 19.4%/61.2% intent preservation) all
trace to the fetched abstract text, which is the paper's own stated
summary of its results — treated as `verified` on this library's
convention for single-source arXiv preprints whose headline figures are
self-reported. The full paper (template text, benchmark construction,
author affiliations) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
