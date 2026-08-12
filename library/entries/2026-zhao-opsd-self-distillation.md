---
slug: 2026-zhao-opsd-self-distillation
title: "Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2601.18734
canonical_ids: ["arxiv:2601.18734", "doi:10.48550/arXiv.2601.18734", "repo:siyan-zhao/OPSD"]
publisher_or_author: "Siyan Zhao, Zhihui Xie, Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen, Aditya Grover — arXiv preprint"
published: 2026-01
captured: 2026-07-22
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
license: "CC BY 4.0"
rationale: >-
  User-submitted post-training method paper. Medium for ai_engineering: a
  token-efficient alternative to RL post-training that teams adapting small
  open models could apply (cost/efficiency concern), but it is model-training
  research adjacent to — not squarely on — the profile's build/operate lenses,
  and evidence is early (models ≤8B, math benchmarks only).
---

# Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models

## Summary

Proposes On-Policy Self-Distillation (OPSD): a single LLM acts as both teacher
and student with identical parameters but different contexts. The student
conditions only on the problem; the teacher additionally conditions on
privileged information (the verified ground-truth solution). Training minimizes
per-token divergence (forward KL worked best) between the teacher's and
student's next-token distributions along the student's own rollouts.

Self-reported results on Qwen3 models (1.7B/4B/8B) trained on ~30K
problem–solution pairs from OpenThoughts, evaluated on AIME 2024/2025 and
HMMT 2025: on Qwen3-1.7B, OPSD reaches 43.4% average accuracy vs 37.7% for
GRPO and 35.8% for SFT. The headline efficiency claim is that OPSD converged
within ~100 steps sampling 1,024 tokens per problem, where GRPO required 8
rollouts of 16k tokens each — substantially fewer training tokens for better
accuracy at the same step count.

Stated limitations: experiments capped at 8B parameters; the approach depends
on problem difficulty — if problems exceed the model's comprehension
threshold, the privileged-context teacher cannot provide meaningful
supervision. Code released at github.com/siyan-zhao/OPSD.

## Why it matters

For a team considering fine-tuning small open models (e.g., for cost, latency,
or data-governance reasons), OPSD suggests a markedly cheaper post-training
route than RL methods like GRPO: no separate teacher model, far fewer sampled
tokens, and a simple objective. The privileged-context teacher idea — same
model, richer context, distill the gap — is also a transferable pattern for
anyone building distillation or self-improvement pipelines. Not directly
actionable for API-only product teams; relevant the moment model adaptation
enters the roadmap.

## Verification notes

Source reachable (arXiv abstract page and v3 HTML full text, fetched
2026-07-22). Bibliographic identity corroborated across both pages: arXiv
2601.18734, v1 2026-01-26, v3 2026-03-20, cs.LG/cs.CL, CC BY 4.0. Method
description and all quantitative claims (43.4% vs 37.7%/35.8%; 100 steps ×
1,024 tokens vs 8 × 16k-token rollouts) traced to the paper's own text and
Table 2. These are the authors' self-reported benchmark results and were not
independently corroborated (no third-party replication found or sought) —
hence `partial`. Code repository existence not independently fetched.

## Updates

None yet.

## Related entries

None yet.
