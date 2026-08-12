---
slug: 2026-sun-cursorrules-files-study
title: "A Study of Cursorrules Files in GitHub Open Source Projects"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.10622
canonical_ids: ["arxiv:2608.10622"]
publisher_or_author: "Shuang Sun, Jafar Akhoundali, Arina Kudriavtseva, Sengim Karayalcin, Olga Gadyatskaya — arXiv preprint (cs.SE); ICSOFT 2026"
published: 2026-08-11
captured: 2026-08-12
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on lens 2 (harness and context engineering): a large empirical
  survey (12,110 .cursorrules files, 11,427 repositories) of how real
  developers write AI-tool configuration prompts, with a practical
  finding — security guidance is comparatively neglected — worth knowing
  even though the artifact itself (.cursorrules) is already being
  superseded by .mdc files.
---

# A Study of Cursorrules Files in GitHub Open Source Projects

## Summary
The paper empirically studies .cursorrules files — configuration prompts used by the Cursor AI-assisted code editor — across 12,110 files from 11,427 GitHub repositories. Adoption is concentrated in small-scale, low-activity, single-maintainer repositories, suggesting toy-project rather than professional-development use. Using a 65-code codebook, the authors find developers' prompts emphasize code-quality guidance and project maintainability, with comparatively little attention to security considerations. The study also documents continuity of themes between the now-legacy .cursorrules format and the current .mdc standard.

## Why it matters
A rare empirical (rather than anecdotal) look at what developers actually write in AI-tool configuration/instruction files in the wild, and a concrete gap — security guidance is under-represented — that teams writing their own harness/instruction files (CLAUDE.md, .cursorrules, .mdc, or equivalent) could deliberately check for.

## Verification notes
Read via the arXiv abstract page. The file/repository counts and the codebook size are quoted/paraphrased directly from the abstract; not independently corroborated against a second source.

## Updates
None yet.

## Related entries
None yet.
