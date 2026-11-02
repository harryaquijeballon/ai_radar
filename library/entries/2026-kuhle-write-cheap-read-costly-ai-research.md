---
slug: 2026-kuhle-write-cheap-read-costly-ai-research
title: "AI-Augmented Research: Free to Write, Costly to Read"
status: accepted
domains: [social_science, ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.32355
canonical_ids: ["arxiv:2610.32355"]
publisher_or_author: "Wolfgang Kuhle"
published: 2026-10-23
captured: 2026-11-02
relevance:
  social_science: high
  ai_engineering: medium
verification: verified
rationale: >-
  High on philosophy of AI and trust (lens 8, social_science): a formal
  model of how cheap AI-assisted writing collapses the incentive to verify
  research, sharpening the epistemology-of-AI-generated-knowledge question
  with a specific mechanism (reader time scarcity, reputation-only impact
  in the costless-writing limit) rather than a general worry. Medium on
  reliable research and policy products (lens 8, ai_engineering): names a
  concrete correlated-error risk in using AI to summarize or peer-review a
  literature that AI itself increasingly wrote, relevant to citation
  verification and human-in-the-loop review design, though the paper is a
  formal model rather than a built technique. First reviewed by a prior run
  and logged in rejections.md on 2026-10-26 for a submission/listing date
  gap; re-reviewed on its merits per the revised ENGINE.md P6.1 rule that a
  date-only rejection is not a dedup match, and the 2026-10-26 econ.GN
  listing date is within this run's 7-day eligibility cap.
---

# AI-Augmented Research: Free to Write, Costly to Read

## Summary

Models how generative AI lowers the cost of writing a research paper
faster than it lowers the cost of reading and verifying one. Authors
differ in reputation; time-limited readers (e.g., referees) choose to
ignore, verify, or trust a given paper. As writing costs fall, fewer
papers get verified in equilibrium: low-reputation ("outsider") authors go
unread, and high-reputation ("established") authors go unchecked. In the
costless-writing limit, no papers are verified at all, and a paper's
perceived impact depends only on its author's reputation, not its
content. The paper notes that readers could try to escape the resulting
volume by having AI summarize the literature for them, but argues such
summaries are reliable only if the AI's errors are sufficiently
independent across papers; once many papers and summaries share the same
underlying AI, summary errors become correlated, and AI-assisted review
filters out exactly the original, independent research that could have
caught them (all claims as stated in the fetched abstract; the full
formal model and proofs were not reviewed at capture).

## Why it matters

**For social-science readers:** a specific, mechanism-level argument
about why cheap AI writing does not just add noise to the literature but
can structurally remove the incentive to verify it — useful for anyone
reasoning about referee incentives, journal policy on AI-assisted
submissions, or why reputation effects might strengthen rather than
weaken as AI-assisted writing scales.

**For AI-engineering readers:** a concrete failure mode for any pipeline
that uses one AI system to both help write and help review or summarize
research: if the same model (or models with correlated errors) sits on
both sides, the correlated-error risk the paper describes applies
directly to AI-assisted literature synthesis, LLM-as-judge peer review,
and citation-verification tooling — a reason to deliberately diversify or
independently ground the models used for generation versus verification
in a research pipeline.

## Verification notes

Read via the arXiv abstract page (captured 2026-11-02; single version,
submitted 23 Oct 2026, no revisions). The core model setup (reputation,
reader time budget, ignore/verify/trust choice), the costless-writing
limit result, and the correlated-error argument against AI-summarization
as an escape valve all trace to the fetched abstract text — the paper's
own stated summary — treated as `verified` on the convention applied
elsewhere in this library to single-source arXiv preprints whose claims
are the paper's own formal results rather than empirical claims requiring
third-party corroboration. The full derivation was not reviewed at
capture.

Dedup note: this candidate first surfaced on 2026-10-26 and was logged to
`rejections.md` that day with "not a new development... late cross-post"
reasoning based on a submission-to-listing gap. `engine/ENGINE.md` P6.1
(revised 2026-10-26) states that a rejection-log line whose only reason
was the date is not a dedup match for discovery, and that the candidate
should be reviewed on its merits; the 2026-10-26 econ.GN listing date is
within this run's 7-day eligibility window (cap: 2026-10-26). The original
rejection-log line is left unedited per the append-only rule; this entry
is the merits-based review the revised rule calls for.

## Updates

None yet.

## Related entries

None yet.
