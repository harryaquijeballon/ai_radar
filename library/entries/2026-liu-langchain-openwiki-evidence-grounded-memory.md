---
slug: 2026-liu-langchain-openwiki-evidence-grounded-memory
title: "Building Evidence-Grounded Agent Memory with OpenWiki and Graphs"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://www.langchain.com/blog/building-agent-memory-openwiki-graphs
canonical_ids: []
publisher_or_author: "Eugene Liu — LangChain blog"
published: 2026-10-28
captured: 2026-10-31
relevance:
  social_science: n/a
  ai_engineering: high
rationale: >-
  Squarely on lens 8 (RAG and document-grounding done rigorously, citation
  verification): a benchmarked technique — a compiled wiki with
  hash-anchored claims plus a typed evidence graph — for keeping multi-agent
  retrieval citations verifiably tied to source changes, with a transparent
  own-benchmark comparison against plain search. Framework-vendor source
  (LangChain); discounted accordingly per profiles/ai_engineering/sources.md.
verification: partial
---

# Building Evidence-Grounded Agent Memory with OpenWiki and Graphs

## Summary

Agents working across policies, manuals, tickets, and code must reconstruct
how sources relate on every question; retrieval finds passages but doesn't
resolve which rules apply, what has changed, or how documents affect each
other — especially where documents amend or supersede one another (e.g.
insurance policies). The post describes OpenWiki, an open-source CLI built
on Deep Agents, which compiles source documents into linked wiki pages
where each statement is a claim tied to specific source lines and their
hash; when source lines change, the hash changes and affected claims are
flagged for review without a model call, so only flagged claims need a model
pass to confirm, revise, or retract. An accompanying evidence graph splits
documents into paragraphs with unique IDs and links claims/paragraphs/pages
with typed edges (cites, refers_to, supersedes), built mostly from existing
citations so it needs no extra model calls. On a synthetic 111-document
insurance-policy benchmark (972-fact ledger, 80 simple-lookup + 50
connected questions, each asked three times): for simple lookups, search and
the wiki perform about the same (0.84 vs. 0.83 accuracy) and the wiki is
slower; for connected (multi-document) questions, wiki accuracy rises from
0.10 (search) to 0.52 and cost per correct answer falls from ~$0.55 to
~$0.19, though citation consistency drops to 0.25. Adding the evidence graph
on top of the wiki raises accuracy a further 27%, roughly doubles citation
consistency, cuts median answer time 40%, and cuts cost per correct answer
58%. Reported costs exclude compilation/update cost ($4.15 to compile 111
documents initially, ~$0.09 per added document).

## Why it matters

A concrete, benchmarked architecture for the specific reliability problem
that "RAG and document-grounding done rigorously" names: keeping citations
tied to source text that can change, and making multi-document reasoning
(not just single-passage lookup) both more accurate and cheaper — with the
authors' own honest caveat that plain search is as good and faster for
simple lookups, so the technique is worth its complexity mainly when agents
repeatedly reason across the same related, amendable sources.

## Verification notes

Read directly from the LangChain blog post
(langchain.com/blog/building-agent-memory-openwiki-graphs, published 28 Oct
2026, author Eugene Liu). The architecture description (hash-anchored
claims, typed evidence graph, locate/expand tools) and the benchmark figures
(0.84/0.83 simple-lookup accuracy, 0.10→0.52 connected-question accuracy,
$0.55→$0.19 cost, 0.25 citation consistency, the graph's further +27%
accuracy/58% cost reduction) are traced to the post text itself.
Verification is marked `partial`: the benchmark is the vendor's own synthetic
dataset, self-reported, with no independent replication attempted; the
post's own stated caveats (synthetic data, excluded compilation cost) are
carried into this entry rather than smoothed over, and the LangChain
framework-vendor discount from `profiles/ai_engineering/sources.md` applies.

## Updates

None yet.

## Related entries

None yet.
