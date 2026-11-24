---
slug: 2026-openai-cisco-shirudo-ebpf-security-shields
title: "OpenAI and Cisco Introduce Shirudo"
status: accepted
domains: [ai_engineering]
source_type: primary
source_url: https://openai.com/index/introducing-shirudo/
canonical_ids: ["repo:openai/shirudo"]
publisher_or_author: "OpenAI and Cisco"
published: 2026-11-23
captured: 2026-11-24
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  Lens 3 (tool use) and lens 6 (reproducibility, security, governance): a
  concrete agent-assisted security-patching architecture (eBPF shields,
  cryptographic signing, TPM-verified deployment records) with a working
  mechanism a builder could study. Scored medium rather than high: the only
  evidence given is a single controlled demonstration with no quantitative
  results (false-positive rate, performance overhead, broader coverage).
---

# OpenAI and Cisco Introduce Shirudo

## Summary

Shirudo ("shield" in Japanese) is an open-source runtime from OpenAI and Cisco that lets operators mitigate a known Linux vulnerability while a permanent patch is tested and deployed, without taking the affected service offline. It uses eBPF — verified programs that run at specific kernel points — to block vulnerable code paths selectively; operators can monitor a shield's effect before enforcing it. The intended workflow is agent-assisted: programmable controls let an AI agent investigate a vulnerability, build a targeted shield, and test it against exploits and real workloads, with security teams deciding what actually gets deployed. Shields are cryptographically signed and verified by the eBPF verifier before loading, and a Trusted Platform Module (TPM) provides a tamper-evident record of when shields were loaded or removed, which operators can check for compliance. The announcement also describes longer-term plans to harden the kernel and core services, limit workload permissions, and make updates and recovery safer.

The only evidence given is a single controlled demonstration: a shield generated with OpenAI's Codex was attached to a running Elasticsearch process to mitigate the Java4Shell vulnerability, adding an input check to Java's Base64 decoder that rejected the malicious input while letting Elasticsearch keep running. The announcement reports no quantitative results — no false-positive rate, performance overhead, or coverage across other vulnerabilities — and points to a Linux Plumbers Conference walkthrough, a companion Isovalent blog post, and a VM quickstart for readers who want to try it directly.

## Why it matters

A concrete, inspectable pattern for agent-assisted incident response that keeps a human security team as the deployment gatekeeper and uses independent, lower-level verification (the eBPF verifier, cryptographic signing, TPM-backed records) rather than trusting the agent's own claims — directly relevant to anyone designing how an AI agent's security or infrastructure actions get verified and audited before they take effect, even though the published evidence for its real-world effectiveness is currently limited to one demonstration.

## Verification notes

Fetched and read directly. The architecture description (eBPF shields, agent-assisted workflow, signing/verification, TPM-backed records) and the Java4Shell/Elasticsearch demonstration are as stated in the announcement. Load-bearing caveat: this is a single named demonstration, not a broader evaluation — no quantitative claim about false-positive rates, performance overhead, or generalization to other vulnerability classes is made or implied by the source, and none is asserted here.

## Updates

None yet.

## Related entries

None yet.
