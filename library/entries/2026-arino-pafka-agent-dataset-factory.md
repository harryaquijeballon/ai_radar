---
slug: 2026-arino-pafka-agent-dataset-factory
title: "Operating an Agent-Driven Dataset Factory: Discovery, Construction, and Public Release"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.21957
canonical_ids: ["arxiv:2611.21957"]
publisher_or_author: "Eduardo Ariño de la Rubia, Szilard Pafka — arXiv preprint"
published: 2026-11-16
captured: 2026-11-20
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 8 (reliable research and policy products) and lens 2
  (harness engineering): a real, running system report — not a proposal —
  on dividing dataset-construction work between LLM tasks and deterministic
  infrastructure, with a concrete, quantified operating cost and a
  cautionary finding about validating task *meaning*, not just successful
  execution.
---

# Operating an Agent-Driven Dataset Factory: Discovery, Construction, and Public Release

## Summary

Addresses the end-to-end work of turning public data into usable
prediction datasets — finding sources, defining tasks, constructing
datasets, and distributing them — by reporting on an operated system,
Dataset Factory, that the authors ran continuously under a standing
release policy. Quoted directly: "We deployed Dataset Factory to perform
these steps continuously under a standing release policy." The
architecture splits responsibilities deliberately: language-model tasks
interpret sources, write construction code, and review task meaning, while
deterministic software handles state, workers, retries, and publication.
Over an 81.53-hour run, the factory published 14 datasets at an estimated
recurring cost of about $2.74 per publication, a figure that includes
failed attempts, inference, workers, and hosting; separate agents ran
prediction experiments on all twelve evaluated releases. The authors also
report a concrete failure caught by their own process: quoted, "Source
review nevertheless identified a task whose construction filters
contradicted its population declaration" — the original reviewer had
accepted later-record exclusions without checking them against the
published selection rule. They conclude that successful execution and
genuine consumer usability require separate checks, since a dataset can
run to completion and still misdescribe what it contains.

## Why it matters

For anyone building agent pipelines that construct research or policy
datasets: a rare operating cost figure (~$2.74 per published dataset over
an 81.53-hour run) to benchmark automation economics against, plus a
sharply concrete cautionary case — a dataset whose construction filters
silently contradicted its own stated population — that argues for a
dedicated "does this dataset mean what it claims to mean" review step,
separate from checking that the pipeline ran and produced output. That
distinction (execution success vs. semantic correctness) is directly
transferable to any AI-assisted data-construction pipeline for research use.

## Verification notes

arXiv abstract page fetched directly (2026-11-20); title, authors, and a
16 November 2026 submission date confirmed (surfaced via arXiv's cs.SE
"recent" cross-list listing dated 18 Nov 2026, within this run's 7-day
eligibility cap). Verbatim quotes obtained for the standing-release-policy
claim and the construction-filter/population-declaration contradiction.
The 81.53-hour runtime, 14-dataset count, and $2.74-per-publication cost
figure are as stated in the abstract. Full paper (system architecture
detail, the twelve prediction experiments) not read at capture. No
independent secondary corroboration attempted (new working paper, no
secondary coverage found this run).

## Updates

None yet.

## Related entries

None yet.
