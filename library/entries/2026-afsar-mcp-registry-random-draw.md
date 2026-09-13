---
slug: 2026-afsar-mcp-registry-random-draw
title: "What a Random Draw from the MCP Registry Contains, and What Tool-Use Benchmarks Contain Instead"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2609.10962
canonical_ids: ["arxiv:2609.10962"]
publisher_or_author: "Haseeb Mohammed Afsar"
published: 2026-09-10
captured: 2026-09-13
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A quantified, reproducible measurement of the real Model Context Protocol
  server ecosystem set against tool-use benchmark corpora — directly on lens
  3 (MCP, tool-interface reliability) and lens 4 (benchmark validity), with a
  concrete curation-bias finding builders can act on this quarter.
---

# What a Random Draw from the MCP Registry Contains, and What Tool-Use Benchmarks Contain Instead

## Summary

The paper draws an unrepaired probability sample of 400 npm/stdio servers
from a registry of 24,135 MCP servers and finds that only 48.8% of the
random sample complete an `initialize` handshake, versus 66.7% for
hand-curated samples — evidence that hand-curated MCP samples used elsewhere
overstate real-world reliability. The dominant failure mode among the random
sample is servers that simply fail to start (37.5%), not missing
credentials (13.3%). Among functioning servers, optional safety annotations
vary widely. Real MCP tools show minimal near-duplication (2.8% at cosine
similarity 0.70), while benchmark corpora show far more: 16.7% for BFCL v4,
and exact name-plus-description repeats of 68.8% (BFCL) and 85.6%
(UltraTool) versus 0.4% for real MCP tools. The author states that "all
figures regenerate from released scripts and a published seed."

## Why it matters

Anyone building or evaluating MCP tool-use systems gets two directly
actionable findings: (1) reliability numbers drawn from hand-picked MCP
servers substantially overstate what a real, registry-wide integration will
encounter — over half of a random draw fails to even complete a handshake;
and (2) widely used tool-use benchmarks (BFCL v4, UltraTool) contain far more
near-duplicate and exact-repeat tool definitions than the real ecosystem
does, which likely inflates measured tool-selection accuracy relative to
production conditions. Both are concrete, reproducible cautions for eval
design (lens 4) and MCP integration planning (lens 3).

## Verification notes

Read the arXiv abstract directly (source is the primary artifact itself, no
secondary relay). All summarized figures (48.8%/66.7% handshake rates,
37.5%/13.3% failure-mode split, 2.8%/16.7% near-duplication, 68.8%/85.6%/0.4%
exact-repeat rates) are quoted or closely paraphrased from the abstract
text. The author's reproducibility claim ("all figures regenerate from
released scripts and a published seed") was read as stated but not
independently re-run.

## Updates

None yet.

## Related entries

None yet.
