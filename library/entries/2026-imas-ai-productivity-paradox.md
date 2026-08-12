---
slug: 2026-imas-ai-productivity-paradox
title: "What is the impact of AI on productivity?"
status: accepted
domains: [social_science]
source_type: commentary
source_url: https://aleximas.substack.com/p/what-is-the-impact-of-ai-on-productivity
canonical_ids: []
publisher_or_author: "Alex Imas — Ghosts of Electricity (Substack)"
published: 2026-01-29
captured: 2026-07-22
relevance:
  social_science: high
  ai_engineering: low
verification: verified
rationale: >-
  Directly on the growth/productivity and empirical-methods lenses: a
  micro-vs-macro synthesis of AI productivity evidence by an academic
  economist. Upgraded from provisional on 2026-07-31 after a sample of the
  load-bearing micro studies was corroborated against primary sources and
  every figure matched (see Updates). The post's forward-looking prediction
  remains inherently unverifiable and is marked as such in the Summary.
---

# What is the impact of AI on productivity?

## Summary

Imas argues that micro-level studies show genuine AI productivity gains — the post cites 20+ studies with task-level improvements of roughly 14–55% across coding, customer service, medical imaging, and consulting *(corrected — see Updates 2026-07-31: the post states neither a "14–55%" range nor a count of 20+, and its micro evidence includes substantial null and negative results this sentence omits)* — while aggregate data show minimal impact, a disconnect he reads as a rerun of the Solow paradox. Adoption is concentrated among higher-skilled workers (citing the Anthropic Economic Index and a BCG survey). The post attributes the gap to organizational bottlenecks that keep task-level gains from scaling (unverified — asserted without citation, as logical inference) *(qualified — see Updates 2026-07-31: the mechanism is in fact stated explicitly and is the standard task-based framework, though the post cites no source for it)*, and predicts macro effects will appear soon as those frictions diminish (unverified — forward-looking claim).

## Why it matters

A compact, citation-dense framing of the question digital-economy analysis keeps hitting: why measured productivity lags demonstrated capability. The micro/macro disconnect framing — and its skill-concentration evidence — is directly reusable when assessing AI-impact claims for digital-economy work.

## Verification notes

Post fetched and read in full (published 2026-01-29, updated March 2026); all summarized claims traced to the post itself. Not done in this review: independent corroboration of the 20+ cited micro studies and macro sources — the 14–55% range is reported as the post states it, not re-verified. The organizational-bottleneck mechanism is asserted without citation; the macro-effects-soon prediction is inherently unverifiable. Upgrade path: corroborate the load-bearing micro-study range against the cited papers.

*(This upgrade path was completed on 2026-07-31 — see Updates for the corroboration results and for two corrections to the Summary that the same review surfaced. The notes above are preserved as the original review's record.)*

## Updates

- **2026-07-31** — **Upgraded provisional → accepted; verification partial → verified.** Trigger: explicit user request to close the upgrade path recorded in the original Verification notes. A sample of the load-bearing micro studies was corroborated against primary sources, and every figure the post attributes to them matched:
  - Brynjolfsson, Li & Raymond — [NBER w31161](https://www.nber.org/papers/w31161): 14% average increase in issues resolved per hour, 34% for novice and low-skilled workers. Post reports "14–15 percent" and "30–35 percent"; both brackets contain the paper's figures (the published version revises the average to 15%).
  - Peng, Kalliamvakou, Cihon & Demirer — [arXiv:2302.06590](https://arxiv.org/abs/2302.06590): treatment group completed the task "55.8% faster." Post reports 55.8%. Exact match.
  - Becker, Rush, Barnes & Rein (METR) — [arXiv:2507.09089](https://arxiv.org/abs/2507.09089): "allowing AI actually increases completion time by 19%," against a developer pre-forecast of a 24% speedup. Post reports 19% slower against 24% expected. Exact match.
  - Dell'Acqua et al., *Navigating the Jagged Technological Frontier* — 12.2% more tasks completed, 25.1% more quickly, and 19 percentage points less likely to produce correct solutions on a task outside the frontier. Post reports all three. Match. Not separately confirmed: the "40 percent higher quality" figure, which the primary abstract states qualitatively as "significantly improved quality."

  Conclusion: the post's reporting of its own citations is accurate, which was the open question. Full-text methodology of the cited studies was not reviewed, and the macro-effects-soon prediction remains unverifiable by nature.

- **2026-07-31** — **Correction to the Summary, from the same review.** Two claims above were wrong about the source and are marked in place:
  1. *The "14–55%" range is this library's construction, not the post's.* The post's own framing is: "Studies find productivity gains ranging from modest increases on some tasks to substantial returns (50%+) to AI." The 14% and 55% endpoints appear in the post only as figures belonging to individual studies (Brynjolfsson et al.; Yeverechyahu et al.). No such range should be attributed to Imas.
  2. *The post is a balanced synthesis, not an argument that gains are real.* It cites roughly 35 studies, not "20+", and a substantial share report null or negative results — METR (19% slower), Humlum & Vestergaard (precise null effects on earnings, hours and wages, ruling out effects larger than 2%), Otis et al. (no significant average effect; low performers roughly 8–10% worse), Shen & Tamkin (a 17-percentage-point learning deficit), and Dell'Acqua et al.'s outside-the-frontier result. The original Summary's "micro-level studies show genuine AI productivity gains" materially understates that balance.

  Root cause: the original review traced claims to the post but paraphrased its evidence base without re-reading it closely enough — the failure mode the verification step exists to catch. Corrected here rather than by rewriting, per `engine/schema.md`.

## Related entries

[2023-korinek-genai-economic-research](2023-korinek-genai-economic-research.md) — task-level productivity framework underlying several of the micro studies discussed.

- [2026-pethokoukis-ai-capability-business-payoff](2026-pethokoukis-ai-capability-business-payoff.md) — the aggregate side of the same gap, with mid-2026 TFP measurements.
- [2026-marsal-perkowski-task-based-genai-central-bank](2026-marsal-perkowski-task-based-genai-central-bank.md) — experimental evidence for the organisational-bottleneck mechanism this post asserts without citation: task reallocation alone yields 7.3% more output.
- [2025-oecd-filippucci-ai-productivity-g7](2025-oecd-filippucci-ai-productivity-g7.md) — macro projections for the G7 that the post's aggregate scepticism bears on.
