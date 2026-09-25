---
slug: 2026-pang-codetta-agent-collusion
title: "Codetta: High-Capacity, Keyless, and Undetectable Multi-Agent Collusion"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2609.28900
canonical_ids: ["arxiv:2609.28900"]
publisher_or_author: "Qi Pang, Virginia Smith, Wenting Zheng — arXiv preprint"
published: 2026-09-24
captured: 2026-09-25
relevance:
  social_science: n/a
  ai_engineering: high
verification: verified
rationale: >-
  High on lens 6 (reproducibility, security and governance): demonstrates
  that steganographic collusion between independently deployed LLM agents
  is practically feasible without any pre-shared key, with quantified
  capacity and a certified failure-probability bound — directly relevant to
  anyone designing audit or monitoring controls for multi-agent deployments
  that assume transcript inspection is sufficient.
---

# Codetta: High-Capacity, Keyless, and Undetectable Multi-Agent Collusion

## Summary

The authors introduce Codetta, a steganographic protocol that lets
independently deployed LLM agents communicate hidden information through
message transcripts that look like ordinary model outputs — enabling
colluding agents to "exfiltrate confidential information or coordinate
unauthorized actions" while remaining, in the authors' words,
"computationally indistinguishable from ordinary model outputs." The
protocol combines a shared public model that estimates the communication
channel with a sampling mechanism preserving each sender's normal output
distribution, plus adaptive error-correcting codes. Critically, it
eliminates the need for a pre-shared key: independent agents can establish
a shared secret via steganographic key exchange alone. Quantified results:
up to 94× greater capacity than prior asymmetric steganographic protocols;
key exchange requires roughly 80,000 visible tokens; and the authors report
an empirically certified failure probability of at most 4.1×10⁻³.

## Why it matters

Most agent-security thinking about collusion or exfiltration assumes a
defender can inspect transcripts for suspicious content. This paper shows
that assumption is no longer safe: two independently deployed agents that
never coordinated keys out-of-band can still establish a covert channel
using ordinary-looking outputs, at a capacity high enough to be practically
useful to an attacker. For anyone designing audit, monitoring, or
multi-agent governance controls (lens 6), this is a concrete reason to
budget for statistical/behavioral detection methods rather than relying on
transcript content review alone.

## Verification notes

Fetched directly from the arXiv abstract page (2609.28900; v1 submitted
Thursday, 24 September 2026, 01:27:47 UTC — within this run's discovery
window). The steganographic-collusion framing, the keyless key-exchange
claim, the 94× capacity figure, the ~80,000-token key-exchange cost, and the
4.1×10⁻³ certified failure-probability bound all trace directly to the
abstract's own quoted text. Full paper (the error-correcting-code design,
the empirical certification methodology) not read at capture.

## Updates

None yet.

## Related entries

None yet.
