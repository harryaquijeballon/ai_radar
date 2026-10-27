---
slug: 2026-verma-structured-output-pydantic-failure-taxonomy
title: "Why Does Structured Output Fail? An Empirical Study of Prompt-Enforced Pydantic Schemas Across Nine LLMs"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2610.33949
canonical_ids: ["arxiv:2610.33949"]
publisher_or_author: "Amit Verma"
published: 2026-10-24
captured: 2026-10-27
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on evaluation, validation and deterministic guardrails (lens 4): a
  deterministic failure-mode taxonomy for prompt-enforced schema outputs
  across nine model/API configurations, with quantified results and four
  derived, mostly data-supported engineering practices for validator,
  schema, retry, and evaluation design.
---

# Why Does Structured Output Fail? An Empirical Study of Prompt-Enforced Pydantic Schemas Across Nine LLMs

## Summary

Many LLM pipelines request structured output by placing a Pydantic schema
in the prompt, validating the response, and retrying on failure. The
paper argues that reporting pipeline reliability as a single validity rate
hides why outputs fail and which fixes would help. The author introduces a
failure-mode taxonomy for schema-conformance failures and a deterministic
classifier that labels failures from model responses and Pydantic
validation errors, applying it to 3,997 generation attempts across nine
OpenAI and Anthropic model/API configurations, using questions from
HotpotQA and FinanceBench. Reported findings: similar overall validity
rates can conceal different underlying failure patterns, and the dominant
failure type depends on schema constraints and task. Markdown-fenced JSON
is reported as the single most common failure; of 681 fenced failures,
48.0% pass validation once the fences are removed, with the remainder
containing other violations, mostly field-length violations. An
exploratory prompt ablation suggests suppressing fences shifts failures
toward length violations, which the author argues reveals violations that
were already present rather than creating new ones. The paper derives four
engineering practices for validator, schema, retry, and evaluation design;
three are stated as data-supported and one (concerning retry feedback) is
proposed but untested. The classifier, completions, and annotations are
reported as released (all figures as stated in the fetched abstract; full
taxonomy and released artifacts not reviewed at capture).

## Why it matters

A concrete, quantified correction to the common practice of reporting
structured-output reliability as one number: the finding that markdown
fencing alone accounts for a large share of "failures" (nearly half of
which are trivially recoverable) is directly actionable — a validator
should strip fences before judging a response invalid. The four derived
design practices (validator, schema, retry, evaluation) give builders a
checklist grounded in a labeled, multi-model dataset rather than a single
provider's behaviour.

## Verification notes

Read via the arXiv abstract page (captured 2026-10-27; single version,
submitted 24 Oct 2026). The 3,997-generation / nine-configuration /
HotpotQA-FinanceBench setup, the markdown-fencing failure dominance, the
681/48.0% fenced-failure figures, the four derived practices (three
data-supported, one untested), and the stated release of the classifier,
completions, and annotations all trace to the fetched abstract text. The
full taxonomy, the released artifacts, and the per-configuration breakdown
were not reviewed — load-bearing figures are traced to the source's own
stated summary but not independently corroborated.

## Updates

None yet.

## Related entries

None yet.
