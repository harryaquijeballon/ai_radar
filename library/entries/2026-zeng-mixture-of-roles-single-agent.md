---
slug: 2026-zeng-mixture-of-roles-single-agent
title: "One Model, Many Minds: Unlocking Multi-Agent Synergy in a Single Agent via Mixture of Roles"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2608.27338
canonical_ids: ["arxiv:2608.27338"]
publisher_or_author: "Zhichen Zeng, Huiyuan Chen, Jingru Cheng, Juan Zha, Ming Liu, Ying Chen, Xiyuan Yang, Chaosheng Dong, Haiyang Zhang, Hanghang Tong — arXiv preprint (cs.MA)"
published: 2026-08-27
captured: 2026-08-29
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Quantified evidence (matches multi-agent-system quality within 2.2%
  average while cutting token cost 20x) that a single steered agent can
  substitute for a multi-agent role-specialization pipeline in some
  settings — a directly cost-relevant data point for lens 1 (agent
  architecture and orchestration).
---

# One Model, Many Minds: Unlocking Multi-Agent Synergy in a Single Agent via Mixture of Roles

## Summary
The authors propose Mixture of Roles (MoRe): rather than orchestrating
separate role-specialized agents across multiple turns (the standard
multi-agent-system approach, which "inflate[s] context length and inference
cost"), MoRe learns a codebook of steering vectors, each encoding a latent
"role," and a query-aware router that fuses the codebook into a single
composed steering vector per query. Steering a frozen backbone LLM with this
composed vector lets one single-turn inference pass exhibit multiple-role
specialization, trained via a three-stage supervised-fine-tuning curriculum
plus GRPO post-training while the backbone itself stays frozen. Across
reasoning and personality benchmarks, MoRe outperforms single-agent
baselines by 2.2% on average and matches multi-agent-system performance
while reducing token cost 20x.

## Why it matters
A concrete, quantified cost/quality trade-off point for anyone weighing
multi-agent role-specialization pipelines against a cheaper single-agent
alternative: if a 20x token-cost reduction with near-parity quality holds up
outside the paper's own benchmarks, it directly informs when orchestrating
multiple specialized agents is worth its inference cost versus steering one
model to cover the same ground.

## Verification notes
Fetched the arXiv abstract directly (arxiv.org, allowlisted); the abstract
text, the 2.2% and 20x figures, and the training-procedure description
(three-stage SFT curriculum, GRPO post-training, frozen backbone) were
confirmed verbatim against the fetched source. No independent corroboration
of the benchmark results was attempted; this is treated as `verified` for
traceability to the cited abstract, not as independent confirmation of the
reported numbers.

## Updates
None yet.

## Related entries
None yet.
