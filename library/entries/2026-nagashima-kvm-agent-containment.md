---
slug: 2026-nagashima-kvm-agent-containment
title: "Coding Agents in KVM: Practical Containment and User Control with Limited Resources"
status: accepted
domains: [ai_engineering]
source_type: academic
source_url: https://arxiv.org/abs/2611.12823
canonical_ids: ["arxiv:2611.12823"]
publisher_or_author: "Yutaka Nagashima — arXiv preprint (cs.SE)"
published: 2026-11-09
captured: 2026-11-12
relevance:
  social_science: n/a
  ai_engineering: medium
verification: partial
rationale: >-
  Medium on reproducibility, security and governance (lens 6): a concrete,
  open-source sandboxing architecture (KVM-Agent) for giving a coding agent
  broad authority inside replaceable, disposable VMs while keeping host
  administration outside them — practically adoptable, but a tool/design
  paper with no benchmarked evaluation of its security or resource claims.
---

# Coding Agents in KVM: Practical Containment and User Control with Limited Resources

## Summary

Presents KVM-Agent, an open-source tool for containing coding agents that
need broad authority to be useful. The author argues off-the-shelf cloud
agent workspaces can contain agents but risk vendor lock-in. KVM-Agent
instead gives an agent broad authority inside a replaceable Ubuntu virtual
machine, keeping host administration outside the VM, and automates most of
the setup and provisioning. It supports multiple coding-agent applications,
model services, and remote job delegation, aiming to preserve familiar
workflows and user choice rather than tying users to a specific vendor
platform. (unverified: the abstract makes only qualitative claims — no
benchmarks, security evaluation, or measured resource-usage results are
reported.)

## Why it matters

A concrete, adoptable pattern for teams who want agent sandboxing without
committing to a vendor-specific cloud agent workspace: VM-level containment
with automated provisioning, applicable to self-hosted or resource-limited
setups. Its residual risks — VM resource usage, maintenance overhead,
secrets reachable inside the VM, and whatever network access is permitted
— are the open questions a team adopting this pattern would still need to
close, since the paper itself reports no evaluation of them.

## Verification notes

Fetched directly from the arXiv abstract page (arxiv.org/abs/2611.12823,
2026-11-12); title, sole author (Yutaka Nagashima), submission date (9 Nov
2026), and category (cs.SE) confirmed there. The architecture description
traces to the fetched abstract text. No quantitative claims were made to
verify; the entry is accepted rather than provisional because the
described architecture itself (not an unverifiable performance claim) is
the substance of the development. Full paper not read at capture.

## Updates

None yet.

## Related entries

None yet.
