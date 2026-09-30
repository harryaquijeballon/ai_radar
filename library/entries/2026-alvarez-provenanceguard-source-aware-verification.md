---
slug: 2026-alvarez-provenanceguard-source-aware-verification
title: "ProvenanceGuard: Source-Aware Verification for MCP Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source
canonical_ids: ["arxiv:2606.18037"]
publisher_or_author: "Ander Alvarez, Santhiya Rajan, Alessandro Genuardi, Oliver Wirjadi, Samuel Mugel, Román Orús — Multiverse Computing (arXiv preprint; Hugging Face blog post)"
published: 2026-09-29
captured: 2026-09-30
relevance:
  social_science: low
  ai_engineering: high
verification: verified
rationale: >-
  Lens 4 (deterministic checks around stochastic components), lens 3 (MCP
  tool-output traces) and lens 8 (citation and attribution verification):
  a post-generation verifier that checks not just whether a claim is
  supported but whether the source the answer names is the one that supports
  it. Directly transferable to research and policy agents that cite tool outputs.
---

# ProvenanceGuard: Source-Aware Verification for MCP Agents

## Summary

The Hugging Face blog post (2026-09-29) presents ProvenanceGuard, a verifier for answers produced by multi-tool agents using the Model Context Protocol (MCP). It targets "cross-source conflation": a claim that is true somewhere in the evidence but attributed to the wrong source (the post's example attributes a refund window to an account record when it comes from a policy document). Per the post and the arXiv abstract page, the verifier consumes captured MCP traces with stable tool and source IDs, decomposes the answer into atomic claims, routes each claim to source-specific evidence, checks support, and separately compares the stated attribution with the routed source, producing per-claim verdicts and an overall decision.

Reported results (arXiv page): on 40 held-out traces with 260 source-eligible claims, block F1 of 0.802 and source accuracy of 0.858; all 50 controlled clinical attribution swaps detected; evaluation spanned 281 medical-domain agent traces with 361 human-verified labels.

Additional details from the blog post only: the post names MiniLM-embedding routing, a DeBERTa NLI support check, and RARR-style repair; it reports 138 of 139 unsupported claims caught and block F1 above MiniCheck (0.783), RAGAS (0.758), AlignScore (0.662) and SummaC-ZS (0.436); it says it runs offline with local models. Stated limitations: source-identification F1 falls to 50.3% when several sources look similar; 144 of 173 repaired answers ended in fallback text rather than substantive rewrites; it needs preserved MCP traces with source IDs and does not apply to single-passage RAG.

## Why it matters

For builders of agentic research and policy products, this frames attribution as a separate verification axis from factuality: an agent can be right about a fact and still cite the wrong document, which breaks auditability. The practical pattern is to log MCP tool calls with stable source IDs and run a deterministic, claim-level attribution check after generation. The limitations, and the evaluation being confined to a medical domain, argue for piloting on one's own traces before relying on the reported figures.

## Verification notes

Blog post and arXiv abstract page (2606.18037, submitted 2026-06-16, latest revision 2026-08-27) both fetched. Headline figures (block F1 0.802, source accuracy 0.858, 40 held-out traces, 260 claims, 50 swaps, 281 traces, 361 labels) agree across the two. Baseline comparisons, the 138/139 figure, component model names and limitation figures appear in the blog post only and were not checked against the full paper text. Results are the authors' own, on a single medical-domain dataset; no independent replication. The arXiv preprint is not peer reviewed. Note the blog author list differs from the arXiv list; both are recorded on their own pages.

## Updates

- **2026-09-30** — Entry created from the daily scan.

## Related entries

None yet.
