---
slug: 2026-deepmind-alphaproof-code-formal-verification
title: "Introducing AlphaProof Code: a breakthrough in verifying complex software at depth"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://deepmind.google/blog/introducing-alphaproof-code/
canonical_ids: []
publisher_or_author: "Pushmeet Kohli, Swarat Chaudhuri — Google DeepMind"
published: 2026-11-10
captured: 2026-11-14
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance — formal
  verification as a concrete control) and lens 4 (deterministic guardrails
  around a stochastic agentic process): a named, scaled technique — agents
  write Lean proofs, Lean checks them, humans review only the ~1% flagged —
  with a built-in correctness check (reintroducing known bugs and confirming
  the system still catches them) rather than a bare capability claim.
---

# Introducing AlphaProof Code: a breakthrough in verifying complex software at depth

## Summary

Google DeepMind announced AlphaProof Code, a multi-LLM agentic framework for
formal verification. Human experts translate a target system's security
goals into formal mathematical specifications in Lean (each spec reviewed by
humans); agents built on Gemini Carbon then generate proofs against those
specifications; Lean checks the proofs automatically, and the agents flag
roughly 1% of the codebase for human review. Applied to Signal's core
cryptographic protocol (PQXDH and the Triple Ratchet in libsignal, compiled
to a 64-bit Arm executable rather than verified only at the source-code
level), the system generated over six million lines of Lean proof in about
four weeks — work the post says historically takes expert teams years. The
proofs show the compiled code preserves specified security properties,
including protection of messages before and after a device is temporarily
compromised. As a validity check, the team reintroduced two previously fixed
real bugs into an isolated version of the code; in both cases the system
produced a machine-checked proof that the buggy version was insecure,
demonstrating the method distinguishes correct from buggy code rather than
merely proving whatever it is pointed at. The post reports no new
vulnerabilities found in current Signal code, and states this is the first
AI-driven formal verification of a widely deployed cryptographic protocol's
actual compiled implementation (unverified: DeepMind's own claim of
precedence, not independently checked here). DeepMind plans to open-source
the verification artifacts and has linked a technical paper.

## Why it matters

A concrete, scaled demonstration that agent-generated formal proofs — not
just agent-generated code — can be made trustworthy enough for high-stakes
software, with an explicit audit mechanism (the reintroduced-bug test) that
other teams building agentic verification pipelines could adopt as a
validity check on their own systems. Directly relevant to the policy-
simulation reliability interest: it is a worked example of making a
stochastic agent's output deterministically checkable before anyone acts on
it.

## Verification notes

Fetched and read in full from the primary source (deepmind.google blog post
by the named DeepMind researchers). Scale and outcome claims (six million
lines of Lean, four weeks, the reintroduced-bug test, the ~1% human-review
flag rate) are quoted or closely paraphrased directly from the post. The
"first time" precedence claims and the comparison to "years" of historical
expert-team effort are the vendor's own framing and were not independently
corroborated against a third-party source; no new vulnerabilities were
independently verified, as this draws solely on DeepMind's own announcement.

## Updates

None yet.

## Related entries

None yet.
