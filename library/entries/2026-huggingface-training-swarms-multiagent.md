---
slug: 2026-huggingface-training-swarms-multiagent
title: "Swarms, Flocks, Gangs: How to Build, Train, and Evaluate Multi-Agent Systems"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://huggingface.co/blog/training-swarms
canonical_ids: []
publisher_or_author: "Hugging Face — blog"
published: 2026-11-25
captured: 2026-11-26
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  A quantified, reproducible evaluation-and-training methodology for
  deciding when multi-agent coordination earns its extra cost, including a
  worked RL-training example with concrete before/after numbers — squarely
  lenses 1 and 4.
---

# Swarms, Flocks, Gangs: How to Build, Train, and Evaluate Multi-Agent Systems

## Summary

The post's core argument: multi-agent systems only justify their cost if
communication helps beyond what extra compute buys, so comparisons should
match token budgets, not just agent counts. Independent retries are the
right baseline — four attempts can beat one simply by having more tries, at
four times the cost. Citing Anthropic's own vulnerability-finding study,
coordinated agents found more bugs but used more tokens; restricted to the
same directories, results per million tokens were roughly equal. One
researcher estimated under 10% of OpenAI's Navier-Stokes result came from
multi-agent cooperation. On training, the authors frame multi-agent RL as a
decentralized partially observable Markov decision process (shifting
teammates, credit assignment, messages that change what others observe) and
describe two common architectures: a hierarchy (lead delegates, sometimes
training only the orchestrator with subagents frozen) or a distributed peer
team. In a worked example — four agents, each holding one private integer,
cooperating to submit a correctly sorted list, with a token-budget penalty —
training raised success from 6.6% to 82.3% (first vs. last five updates of
75 total), with held-out success of 81.25% at checkpoint 75 (93.2% after 200
updates reported in the source paper). Generated tokens per team fell about
37.4% (roughly 12.8k to 8.0k) while messages per team rose (3.48 to 6.28)
and broadcasts increased. An untrained team using best-of-8 retries solved
about 37.5% of problems using roughly 103k tokens per problem; the trained
team's single attempt solved 82.3% using about 8k tokens. A reproduction
recipe runs the open-source TRL example on two H200 GPUs for 50 updates
(about 5 hours, roughly $50), reaching 60.9% held-out success at checkpoint
50 in TRL's own run.

## Why it matters

A directly actionable methodology for anyone deciding whether to build a
multi-agent system rather than scaling a single agent with more retries: the
matched-token-budget comparison protocol is a reusable evaluation standard
(lens 4), and the worked, reproducible RL-training example with concrete
cost/success numbers (and a ~$50, few-hour reproduction recipe) makes the
architecture and training-method guidance (lens 1) something a team could
replicate this quarter rather than just read about.

## Verification notes

Fetched the Hugging Face blog post directly
(huggingface.co/blog/training-swarms, published 2026-11-25). All figures and
the methodology description above are traced to the post's own text,
including its citation of Anthropic's vulnerability-finding study and the
OpenAI Navier-Stokes estimate (both relayed secondhand within the post, not
independently verified against their original sources here). No further
independent corroboration was attempted.

## Updates

None yet.

## Related entries

None yet.
