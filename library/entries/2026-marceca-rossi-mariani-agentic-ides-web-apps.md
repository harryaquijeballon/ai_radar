---
slug: 2026-marceca-rossi-mariani-agentic-ides-web-apps
title: "Generation of Web Apps with Agentic IDEs: An Empirical Assessment"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.20903
canonical_ids: ["arxiv:2608.20903"]
publisher_or_author: "Manuel Marceca, Maria Teresa Rossi, Leonardo Mariani — arXiv preprint (cs.SE)"
published: 2026-08-24
captured: 2026-08-24
relevance:
  social_science: n/a
  ai_engineering: medium
rationale: >-
  Medium on lens 7 (AI-assisted software development): a comparative
  empirical study of three agentic IDEs (Copilot, Cursor, Windsurf)
  generating full-stack web apps from scratch, with a clear qualitative
  finding (established patterns handled well, uncommon distributed
  architectures fail more) but no quantified error rates in the abstract.
verification: partial
---

# Generation of Web Apps with Agentic IDEs: An Empirical Assessment

## Summary

The authors compare three agentic IDEs — Copilot, Cursor, and Windsurf — on their ability to generate complete full-stack web applications from scratch. The tools show high maturity generating established patterns such as CRUD operations and authentication features, but generation of less common distributed architectures, such as task-queue systems, produces significantly more errors. The authors conclude agentic IDEs cannot fully replace developers but instead shift the developer's role toward orchestrating LLM-based agents through natural-language instructions and iterative refinement; differences between the three tools tested were relatively narrow.

## Why it matters

A grounded, comparative reality check on agentic IDE capability (lens 7): common, well-represented patterns (CRUD, auth) are handled reliably, but the failure rate rises for architectures that are less common in training data, such as task queues. For teams deciding where to trust agentic IDEs unsupervised versus where to expect heavier review, this gives a concrete axis (pattern commonality) to reason about, rather than a blanket capability claim.

## Verification notes

Read via the arXiv abstract page, which states the qualitative comparison directly but reports no specific numerical error rates or metrics — the abstract itself notes the assessment is qualitative on this point, so verification is marked partial rather than verified.

## Updates

None yet.

## Related entries

None yet.
