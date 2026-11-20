---
slug: 2026-wang-rogue-ai-incident-replication
title: "Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.26553
canonical_ids: ["arxiv:2611.26553"]
publisher_or_author: "Mengxiao Wang, Mahbub Alam, Kalyan Nakka, Nitesh Saxena — arXiv preprint"
published: 2026-11-19
captured: 2026-11-20
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 5 (observability and debugging) and lens 6 (reproducibility,
  security and governance): a reusable offline-replication framework that
  distinguishes real root cause from mere incident description, with a
  quantified, counterintuitive finding — attacker-free "ordinary hazard"
  failures cause more harm than prompt-injection failures across five
  current frontier models — directly actionable as a pre-release audit a
  vendor or operator could rerun.
---

# Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)

## Summary

LLM-based agents increasingly take real-world actions (deleting files,
sending payments) on a user's behalf, but public incident reports rarely
verify whether the reported harm is real or test the specific cause the
report blames. The authors present ROGUE-AI, a multi-agent framework that
rebuilds each reported incident offline, pairing it with a matched control
that removes only the blamed cause, then running agents on both. Quoted
directly: "reproduce the reported harm in 89% of its 108 attempted
replications." Agents built on five current GPT, Claude, Gemini, and
DeepSeek models repeated the reported mistake in 18%–33% of runs, versus at
most 1% on the matched control. Of 72 incidents with real-world harm, 62
had no attacker: agents completed their assigned task but overlooked an
ordinary hazard (e.g., a database shared with a live site). Quoted:
"Replications without an attacker caused more harm than replications of
prompt injection for all five models." Because these attacker-free
replications contain no injected instructions, defenses that scan for
injected text would not catch them. A warning inserted after each tool
output that names the specific hazard and its consequence reduced harm
across all five models; a same-length warning that omitted the hazard left
most of the harm in place.

## Why it matters

For anyone operating LLM agents with real-world side effects: a concrete,
quantified warning that most measured agentic harm in this study came from
agents faithfully completing ordinary tasks while missing routine hazards,
not from attackers — meaning prompt-injection defenses alone leave the
larger share of real incidents uncovered. The paper's replication method
(incident + matched no-cause control, rerun across models) and its
finding that specific, consequence-naming warnings reduce harm while
generic warnings do not are both directly reusable as a pre-release audit
step.

## Verification notes

arXiv abstract page fetched directly (2026-11-20); title, authors, and a
19 November 2026 submission date confirmed. Verbatim quotes obtained for
the headline replication rate (89% of 108), the attacker-free-vs-injection
comparison, and the 62-of-72-no-attacker figure. The 18%–33% model-level
repeat-rate range and the warning-intervention result are as summarized
from the abstract; full paper (replication methodology detail, per-model
breakdown, warning-text design) not read at capture. No independent
secondary corroboration attempted (new working paper, no secondary
coverage found this run).

## Updates

None yet.

## Related entries

None yet.
