---
slug: 2026-vir-flowcheck-constraint-verification
title: "Coding Agents Keep Shipping Silent Failures — Here Is How to Catch Them"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://towardsdatascience.com/coding-agents-keep-shipping-silent-failures-here-is-how-to-catch-them/
canonical_ids: []
publisher_or_author: "Reya Vir — Towards Data Science"
published: 2026-09-18
captured: 2026-09-19
relevance:
  social_science: n/a
  ai_engineering: high
verification: partial
rationale: >-
  High on lens 4 (evaluation, validation and deterministic guardrails): a
  concrete, code-level verification technique — user-specified UI constraints
  compiled into static-analysis queries — that catches a specific class of
  silent coding-agent failure, with a quantified head-to-head comparison
  against having frontier LLMs review the same code, directly usable for
  hardening agent-generated software in research/policy products.
---

# Coding Agents Keep Shipping Silent Failures — Here Is How to Catch Them

## Summary

Vir argues that "vibe coded" apps built via natural-language prompting often
look functional while containing silent failures — for example, a UI action
that appears to succeed but never actually performs the corresponding
database write — because reviewers cannot feasibly read all agent-generated
code, and because such bugs occur in code paths that specifically look
correct on the surface. She proposes FlowCheck, a four-step verification
technique that does not require reading the generated code: (1) the user
clicks on a UI component and expresses an expected behavior in a fixed
template ("When I take [action], these update: [component]"); (2) that
constraint is translated into a formal, probabilistic expression such as
"P(write(e) | action(A)) = 1" (a write must occur on every execution path
following the action); (3) the expression is compiled into a CodeQL static-
analysis query that traces data flow from the UI action through to the
database/storage operation; (4) CodeQL runs the query against the
application's own codebase and reports violations, pinpointing the exact
line where the expected write does not occur. Vir evaluated FlowCheck
against four simulated applications modeled on Amazon, Twitter, Airbnb, and
Slack, with 30 bugs deliberately injected across them. FlowCheck detected
30/30; three frontier LLMs asked to review the same code for the same bugs
(Claude Opus, DeepSeek V3, Gemini Pro) each caught at most 26/30, with
misses concentrated in cross-handler data flows and conditional branches.

## Why it matters

Offers builders of agent-generated software (including research and
policy-simulation products where a silently-broken data write could corrupt
downstream analysis without any visible error) a specific, implementable
alternative to code review by LLM or by human eye for one well-defined
failure class: hands the verification burden to a deterministic static
analyzer driven by a plain-language constraint the user already knows how to
state, rather than to another stochastic model doing the checking.

## Verification notes

Fetched directly from towardsdatascience.com (allowlisted). The FlowCheck
design (the four steps, the CodeQL-compilation approach, the probabilistic-
constraint formalism) is the author's own description of her proposed
technique and traces directly to the article's text. The evaluation
methodology and headline numbers (four simulated apps, 30 injected bugs,
FlowCheck 30/30 vs. frontier-model reviewers' 26/30 or fewer, misses
concentrated in cross-handler/conditional-branch cases) are also stated
directly in the article. `partial` rather than `verified`: this is the
author's own reported evaluation on her own simulated benchmark, not
independently reproduced or corroborated against a third-party source this
run.

## Updates

None yet.

## Related entries

None yet.
