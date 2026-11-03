---
slug: 2026-yao-destructive-tool-approval-mcp
title: "When Neither Side Confirms: Destructive Tool Approval Across MCP Servers and Hosts"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.02527
canonical_ids: ["arxiv:2611.02527"]
publisher_or_author: "Junwei Yao, Zike Yang, Zhijun Wang, Yongxi Zhou, Wenbo Ye"
published: 2026-11-02
captured: 2026-11-03
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on tool use and MCP (lens 3) and reproducibility/security/governance
  (lens 6): a large-scale source-code study (1,000 MCP registry
  repositories, 41 hosts/SDKs) quantifying how rarely either side of the
  MCP human-approval contract for destructive tool calls is actually
  enforced, with a measured mitigation effect — directly actionable for
  anyone deploying MCP-based agents with write/delete-capable tools.
---

# When Neither Side Confirms: Destructive Tool Approval Across MCP Servers and Hosts

## Summary

Studies how LLM agents calling destructive tools through the Model Context
Protocol (MCP) actually get human approval in practice. The MCP
specification expects a human to be able to deny a tool call, but
responsibility is split between servers (which can flag tools or request
confirmation through the host) and host applications (which decide whether
to prompt the user at all). Examining source code in two samples: across
1,000 repositories from the official MCP registry, about 90% of
destructive tools have no server-side confirmation, and many servers that
do request confirmation proceed anyway or fall back to a model-settable
flag when the host cannot relay the question. Across 41 popular
open-source hosts and agent SDKs, 32 have no default approval step
(including 16 of 25 end-user applications); in paired samples of
destructive tools and applications, 60.7% had no enforced default human
approval. In live tests across four agent SDKs, four of five low-cost
models executed an injected deletion in 479 of 960 runs. Simulation
suggests prompting for every tool not explicitly marked read-only/
non-destructive would cut the unapproved share to 5.4%, while universal
elicitation support alone would still leave 56.7% unapproved (as stated in
the fetched abstract; full methodology and per-host/per-model breakdowns
not reviewed at capture).

## Why it matters

Quantifies a widespread, severe gap in the MCP ecosystem's human-approval
contract for destructive actions: most servers don't ask, most hosts don't
prompt, and low-cost models will execute an injected destructive call
roughly half the time when nothing stops them. Directly actionable for
anyone building or deploying MCP-based agents with write/delete-capable
tools — the paper's own simulated mitigation (deny-by-default for anything
not explicitly marked safe, cutting unapproved execution to 5.4%) is a
concrete, measured configuration change, not just a recommendation to "add
a confirmation step."

## Verification notes

Read via the arXiv abstract page (captured 2026-11-03; single version,
submitted 2 Nov 2026, no revisions). The two-sample source-code study
design (1,000 registry repos; 41 hosts/SDKs), the ~90%/60.7%/32-of-41
figures, the 479-of-960 live-test result, and the 5.4%/56.7% simulated
mitigation figures all trace to the fetched abstract text, which is the
paper's own stated summary of its results — treated as `verified` on this
library's convention for single-source arXiv preprints whose headline
figures are self-reported empirical findings rather than claims requiring
third-party corroboration. The full paper (per-host/per-SDK breakdowns,
injected-deletion test design) was not reviewed at capture.

## Updates

None yet.

## Related entries

None yet.
