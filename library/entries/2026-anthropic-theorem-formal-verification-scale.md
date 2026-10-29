---
slug: 2026-anthropic-theorem-formal-verification-scale
title: "LLMs Are Making Formal Software Verification Feasible at a Much Larger Scale"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://www.anthropic.com/research/formal-verification
canonical_ids: []
publisher_or_author: "Anthropic Frontier Red Team, with Theorem"
published: 2026-10-22
captured: 2026-10-29
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on reproducibility, security and governance (lens 6): a concrete
  control (machine-checked formal proofs of memory/crash safety, generated
  and verified at scale) with named scope limits and trusted-component
  caveats stated by the authors themselves — the kind of deterministic
  guardrail around a stochastic component this profile's policy-simulation
  interest is built around. Vendor source: Anthropic has a stake in
  Claude's perceived capability; scored on the mechanism and stated
  limitations, not the headline.
---

# LLMs Are Making Formal Software Verification Feasible at a Much Larger Scale

## Summary

Anthropic's Frontier Red Team, working with the verification company
Theorem, used Claude to generate and check formal proofs of memory- and
crash-safety properties for compiled RISC-V binaries. Claude converted
existing fuzz tests from open-source libraries (mostly Google's OSS-Fuzz
corpus) into formal specifications — each stating that a given entry
point never crashes on inputs up to 64 MB — then wrote proofs against
Theorem's RISC-V and Linux process semantics, checked by the Rocq proof
assistant. When Claude found a bug, it patched the code, regenerated the
spec, and re-proved it; patches were logged and penalized to discourage
reward hacking (changing the program just to make a proof trivially
pass). Proofs assume a single-threaded static binary, a fixed memory
budget, RISC-V, and Linux.

Over a few weeks, 239 entry points across 123 open-source libraries were
proven free of crashes under this model, totaling about 180 million lines
of Rocq proof (a typical proof ~600,000 lines, for binaries with a median
of 18,000 RISC-V instructions). The process surfaced hundreds of bugs,
including a counter underflow in a decompressor, an out-of-bounds read in
an image decoder, and a rediscovered libexpat vulnerability (CVE-2026-56132).
Separately, Claude proved the Linux kernel's zlib matches its RFC 1950
spec (repeated for ~6 more libraries, finding only minor unexploitable
bugs), proved a Rust-written Python interpreter matches CPython behavior
on 99.95% of 1.7 million random programs, and in one week of effort on a
PDF reader surfaced roughly as many security bugs as are typically
reported in a year for that codebase. On 36 small verification tasks,
Opus 5.5 proved half using about 40% fewer tokens than Opus 5; sharing
proofs across agents cut token use by a further 17%.

## Why it matters

A concrete deterministic-guardrail technique directly relevant to
building AI systems whose outputs must be *defensible*, not just
plausible: machine-checked proof rather than test coverage or model
self-report. The authors' own stated limits are as important as the
headline — "formally verified" depends entirely on the specification and
machine model used (here, RISC-V/musl/static linking, not the x86/ARM +
dynamic glibc most software actually ships as), trusted components
(the Rocq checker, the semantics models, the hardware/compiler) remain
unverified themselves, and proofs can cost hundreds of millions of
tokens — giving builders a template for both the technique and the
caveats to disclose when claiming "AI-verified" for any component.

## Verification notes

Read in full via direct fetch of the Anthropic research page (captured
2026-10-29; published 2026-10-22; team and contributor list, methodology,
and all quantified figures — 239 entry points, 123 libraries, 180M lines
of Rocq, ~600,000-line typical proof, 18,000-instruction median binary,
CVE-2026-56132, 99.95% Python-interpreter match across 1.7M programs,
the 40%/17% token-efficiency figures — are stated directly on the primary
source page, not relayed through a third party. The page's own stated
limitations (spec/machine-model dependence, trusted-component risk,
RISC-V/musl scope, high proof cost, withheld proofs for unpatched bugs)
are preserved here rather than omitted. Independent corroboration beyond
the vendor's own page was not attempted this run; Anthropic has a direct
stake in Claude's perceived verification capability.

## Updates

None yet.

## Related entries

[2026-anthropic-discovering-vulnerabilities-claude](2026-anthropic-discovering-vulnerabilities-claude.md) — same team (Anthropic Frontier Red Team), published five days apart: this one applies Claude to defensive formal verification, the other to offensive vulnerability discovery.
