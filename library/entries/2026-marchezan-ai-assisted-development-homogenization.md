---
slug: 2026-marchezan-ai-assisted-development-homogenization
title: "Does AI-Assisted Development Homogenize Software? An Empirical Study of Code Similarity, Quality, and Evolution"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.24093
canonical_ids: ["arxiv:2610.24093"]
publisher_or_author: "Luciano Marchezan et al."
published: 2026-10-20
captured: 2026-10-20
relevance:
  ai_engineering: high
  social_science: n/a
verification: partial
rationale: >-
  A 50-project, three-era empirical study finding no consistent evidence that
  AI-assisted/agentic development increases code homogenization — evidence
  against a widely assumed risk, with a transferable measurement method
  (embedding similarity + CodeBLEU + SonarQube metrics) for lens 7
  (AI-assisted software development).
---

# Does AI-Assisted Development Homogenize Software? An Empirical Study of Code Similarity, Quality, and Evolution

## Summary

The authors study whether AI-assisted and agentic coding tools are
homogenizing software, examining 50 long-lived open-source Java and Python
projects across three periods — pre-LLM, potentially LLM-assisted, and
detected agentic development — using snapshots from Software Heritage. They
measure similarity with embedding-based cosine similarity (semantic) and
CodeBLEU (syntactic); quality with SonarQube metrics for maintainability,
complexity, reliability, and security; and evolution via annualized growth
in lines of code, functions, classes, files, and statements, plus commit
activity in the three months before each snapshot.

Headline findings: the study found "no consistent evidence of increased
similarity." In Java, both semantic and syntactic similarity fell
significantly in the LLM and agentic eras relative to the pre-LLM period;
Python showed no significant difference across eras. Code quality was
largely stable overall, with the agentic era showing significantly lower
code-smell and SQALE-index densities (i.e., somewhat better on those
measures, not worse). Structural growth was generally lower in the agentic
era, especially for file counts, while Java development activity (commits,
lines added) rose moderately. The abstract reports statistical significance
and direction but not effect sizes.

## Why it matters

Pushes back, with a multi-project empirical design rather than anecdote,
against the common worry that AI coding tools make codebases converge toward
homogeneous, AI-flavored code — relevant for teams deciding how much weight
to put on that risk when adopting AI-assisted or agentic development, and
offers a reusable measurement combination (embedding similarity + CodeBLEU +
SonarQube) for anyone wanting to check the same question on their own
codebase.

## Verification notes

Read via the arXiv abstract page. The study design (50 projects, three eras,
Software Heritage snapshots), the three measurement families, and the
findings above are stated in the abstract and traceable to it; the abstract
itself notes it omits exact effect sizes. The full paper was not fetched, so
`verification: partial`.

## Updates

None yet.

## Related entries

None yet.
