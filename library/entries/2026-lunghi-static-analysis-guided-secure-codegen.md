---
slug: 2026-lunghi-static-analysis-guided-secure-codegen
title: "Guiding LLM Code Generation with Static Analysis Findings During Generation"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.26312
canonical_ids: ["arxiv:2611.26312"]
publisher_or_author: "Daniele Lunghi, Alberick Euraste Djiré, Zacharie Chenail-Larcher, Mélissa Tessa, Quentin Stiévenart, Jacques Klein, Florent Avellaneda, Naouel Moha, Tegawendé F. Bissyandé — arXiv preprint"
published: 2026-11-19
captured: 2026-11-20
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance): a concrete,
  cheap control for secure LLM code generation — feeding static-analyzer
  findings during generation instead of inside an expensive post-hoc repair
  loop — with a direct token-cost-vs-security-rate comparison against
  iterative repair and a clearly stated boundary condition for when it
  backfires.
---

# Guiding LLM Code Generation with Static Analysis Findings During Generation

## Summary

Examines whether static-analyzer findings can steer LLMs toward writing
more secure code more cheaply than the common approach of running the
analyzer inside an iterative post-hoc repair loop. The authors propose two
"guidance during generation" strategies: when an analyzer alert fires,
generation is rolled back and the finding is inserted either as a code
comment or in the user message. They compare these against two iterative
repair approaches and a no-analyzer control, across three models and three
Python benchmarks, scored against each benchmark's oracle. Quoted
directly: "Guidance during generation is cheap and can be effective," using
0.9–1.9x the baseline's output tokens versus up to 24.1x for iterative
approaches. With DeepSeek-V4.1-flash on RiskyPy, the steering strategy
raised the share of programs that were both functional and secure from
52.5% to 64.4% — close to the best iterative approach's 66.2% at under a
fifth of the token cost. Rules with a local fix benefited most. Limits: on
SecEvalPlus, analyzers flagged at most 5.6% of functional-but-insecure
programs, leaving little for the technique to act on; guidance backfired
when an alert contradicted the task, since models tended to follow the
analyzer and "break the program"; the two Qwen2.5 models often failed when
a fix required restructuring code.

## Why it matters

For anyone building coding agents or LLM-assisted development tools: a
direct cost/effectiveness comparison showing that cheap, inline
static-analysis guidance recovers most of iterative repair's security
benefit at roughly a fifth of the token cost — a concrete lever for
lowering the cost of secure-code guardrails without abandoning them — plus
an explicit boundary condition (alerts that conflict with task intent, or
require restructuring) for when to fall back to iterative repair or human
review instead.

## Verification notes

arXiv abstract page fetched directly (2026-11-20); title, full author
list, and a 19 November 2026 submission date confirmed. Verbatim quotes
obtained for the central "cheap and can be effective" claim and the token-
multiplier figures (0.9–1.9x vs up to 24.1x); the 52.5%→64.4%/66.2% RiskyPy
figures, the 5.6% SecEvalPlus ceiling, and the backfire/Qwen2.5 limitations
are as summarized from the abstract. Full paper (benchmark construction,
oracle definitions, per-model breakdowns) not read at capture. No
independent secondary corroboration attempted (new working paper, no
secondary coverage found this run).

## Updates

None yet.

## Related entries

None yet.
