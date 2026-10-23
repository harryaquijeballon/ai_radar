---
slug: 2026-zeinali-joules-to-gdp
title: "Joules-to-GDP: How Much Economic Value Do AI Systems Produce per Unit of Energy?"
status: accepted
domains: [social_science]
source_type: academic
source_url: https://arxiv.org/abs/2610.30858
canonical_ids: ["arxiv:2610.30858"]
publisher_or_author: "Amirreza Zeinali, Jon Saad-Falcon, Avanika Narayan, Mersad Abbasi, Jonathan S. Hartley, John Hennessy, Christopher Re, Azalia Mirhoseini"
published: 2026-10-22
captured: 2026-10-23
relevance:
  social_science: high
  ai_engineering: low
rationale: >-
  High on lens 1 (economic growth and productivity): a new, directly
  measured productivity-per-energy metric for AI systems (Net Value per
  Joule, Time Saving per Joule) across real tasks, models and accelerators —
  a usable addition to the productivity-measurement debate beyond
  benchmark-accuracy framing. Low on ai_engineering: a cost/energy
  efficiency metric for model and hardware selection, not an engineering
  pattern for reliability.
verification: verified
---

# Joules-to-GDP: How Much Economic Value Do AI Systems Produce per Unit of Energy?

## Summary
The paper proposes two metrics for the economic value AI systems produce
per unit of energy consumed: Net Value per Joule (NVJ — output dollar value
minus AI execution cost, divided by measured energy, in USD/MJ) and Time
Saving per Joule (TSJ — expert completion time minus AI completion time,
divided by energy, in hours/MJ). The authors apply these to 220 public
GDPval tasks across 44 occupations, running five open-weight models locally
and measuring end-to-end energy across four accelerator types.

Key findings: occupations where AI succeeds most often, or delivers the
most dollar value or time saved, do not necessarily deliver the highest
value per joule — engineering tasks yield about 10% more net dollar value
per task than software-development tasks, but software-development tasks
yield about 27% more net value per joule. GLM 5.2 had the highest average
net dollar value ($72.27/task, 0.430 MJ); Gemma 4 31B delivered 56% of that
value using 23% of the energy (roughly 2.5x the NVJ, 2.8x the TSJ). Across
four single-accelerator deployments of Qwen3.6-27B, NVJ varied by a factor
of 4.32 and TSJ by 9.27, with the B200 leading both. One H100 and eight
H100s delivered similar net dollar value; eight H100s cut completion time
by 22% but used 3.24x the energy.

## Why it matters
This gives growth/productivity researchers a directly measured,
task-grounded economic-value-per-energy metric to cite instead of relying
on benchmark accuracy or raw cost as a proxy for AI's productivity
contribution — usable in debates about AI's measured versus actual economic
value (lens 1's productivity-measurement theme) and in any analysis that
needs to net out AI's energy/compute costs against its output value, a
question increasingly relevant to AI-datacenter-and-growth accounting.

## Verification notes
Read directly from the arXiv abstract page (arXiv:2610.30858, v1, submitted
22 Oct 2026). All summarized figures (dollar values, energy ratios,
percentage comparisons) are stated directly in the abstract and traceable
to it; the underlying GDPval task set and accelerator benchmarking give the
headline comparisons a concrete, replicable basis. Full paper and
independent replication not checked this run.

## Updates

- None yet.

## Related entries
None yet.
