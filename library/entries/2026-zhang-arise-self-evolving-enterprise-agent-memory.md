---
slug: 2026-zhang-arise-self-evolving-enterprise-agent-memory
title: "ARISE: Practical Self-Evolving Memory for Accurate and Cost-Efficient Enterprise Agents"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.23588
canonical_ids: ["arxiv:2611.23588"]
publisher_or_author: "Jiangyun Zhang, Zhou Tang, Kristen Surrao, Zhiyu Chen, Albert Guan, Tor Nitayanont, Yupei Zhang, Roopali Singh, Yunkai Xiao, Shreya Pandit, Julia Huang, Shayan Ali Akbar, Erwin Cornejo, Yuan Li, Yi Zhang — arXiv preprint (cs.AI)"
published: 2026-11-17
captured: 2026-11-19
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 2 (harness and context engineering) and lens 5 (cost
  monitoring): a memory architecture that improves an enterprise agent from
  its own failures without retraining or workflow changes, gating each new
  rule on held-out accuracy, with quantified accuracy gains and a small net
  cost reduction across two enterprise benchmarks and five models.
---

# ARISE: Practical Self-Evolving Memory for Accurate and Cost-Efficient Enterprise Agents

## Summary

Addresses enterprise LLM agents that must keep up with frequently changing
foundation models and workflows under accuracy and cost constraints. The
authors propose ARISE ("Agent Refinement through Iterative Self-
Evaluation"), a memory architecture that improves an agent from its own
failures without changing model weights, tools, or workflow logic: the
deployed model itself, or a stronger teacher model, diagnoses why a failure
happened and proposes a fix; fixes are stored as retrievable micro-memories
and later consolidated into broader macro rules, with a rule adopted only
if it improves accuracy on held-out data. Across 14 enterprise workflow
domains from SOP-Bench and τ²-bench, using five models, the teacher-
assisted variant (ARISE-Teacher, using Claude Opus 4.6 for attribution and
consolidation) improves over baseline by 10.9 points on SOP-Bench and 5.8
points on τ²-bench, outperforming the GEPA baseline by 4.5 points on
τ²-bench and 1.4 points on SOP-Bench. The self-attributing variant (ARISE-
Self, where the deployed model analyzes its own failures) still gains 10.0
points on SOP-Bench. ARISE-Teacher also makes 4.0% fewer model calls and
produces 5.2% fewer output tokens, for a roughly flat (1.0% lower) per-task
cost.

## Why it matters

For anyone operating an enterprise agent that must keep working as models
and workflows change underneath it: a concrete, held-out-gated mechanism
for an agent to learn from its own mistakes without a retraining cycle or
manual rule-writing, with quantified accuracy gains that beat a named prior
method (GEPA) at roughly flat cost. The micro-memory-to-macro-rule
consolidation pattern, gated on measured accuracy improvement rather than
plausibility, is a directly reusable design for teams building their own
agent-memory or self-correction layers.

## Verification notes

arXiv abstract page fetched directly (2026-11-19); title, full 15-author
list, "Submitted on 17 November 2026" date (v1 only), and cs.AI (primary) /
cs.MA / ACM class I.2.7 subject categories confirmed. Every quantitative
claim in the Summary (14 domains, SOP-Bench/τ²-bench, five models, the
10.9/5.8-point gains, the GEPA comparison, the 10.0-point ARISE-Self gain,
and the 4.0%/5.2%/1.0% cost figures) traces to the fetched abstract text.
Full paper body not read at capture; no independent corroboration attempted
(new working paper, no secondary coverage found). Appeared in arXiv's
cs.MA "recent" listing dated Thu, 19 Nov 2026, two days after its 17 Nov
2026 submission — within normal moderation lag and the 7-day eligibility
cap. Upgrade path: read the full PDF for the failure-attribution prompts
and the rule-consolidation algorithm.

## Updates

None yet.

## Related entries

None yet.
