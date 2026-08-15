---
slug: 2026-willison-hallucinate-tag-embeddings
title: "Don't classify. Hallucinate!"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Aug/14/dont-classify-hallucinate/
canonical_ids: []
publisher_or_author: "Simon Willison, summarizing Doug Turnbull (softwaredoug.com) — simonwillison.net"
published: 2026-08-14
captured: 2026-08-15
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Medium on tool-use/interface design and reliable document-grounding
  (lenses 3, 8): a reusable pattern for classification against very large
  label vocabularies — let the model generate unconstrained tags, then
  reconcile them to the real vocabulary post-hoc with embeddings — useful
  context rather than a validated, quantified result.
---

# Don't classify. Hallucinate!

## Summary

Simon Willison relays a technique from Doug Turnbull (softwaredoug.com):
rather than constraining an LLM to select from an existing tag vocabulary
(1,856+ tags in Turnbull's case, impractical to feed as a constraint list),
let the model freely generate ("hallucinate") novel classification tags
for a piece of content, then use vector embeddings to map each invented
tag to its closest match in the real vocabulary. This separates generation
from matching into two distinct steps instead of forcing the model to
choose from a massive predefined list in one pass.

## Why it matters

A practical, low-effort pattern for any classification or tagging task
where the label space is too large to enumerate as a prompt constraint:
generate freely, then reconcile deterministically via embedding similarity.
Directly applicable to metadata tagging, taxonomy assignment, or routing
tasks in document-processing pipelines.

## Verification notes

simonwillison.net fetched directly (2026-08-15); the technique description,
the 1,856+ tag figure, the attribution to Doug Turnbull/softwaredoug.com,
and Willison's framing all trace to the fetched page. Marked `verified`
rather than `partial` because the claim being made is a technique
description (traceable in full to the fetched source), not a quantified
empirical result requiring independent corroboration; Turnbull's original
post (softwaredoug.com) is off the project's egress allowlist and was not
independently fetched this run.

## Updates

None yet.

## Related entries

None yet.
