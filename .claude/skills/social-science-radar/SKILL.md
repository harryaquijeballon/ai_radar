---
name: social-science-radar
description: Ingests, reviews, and archives social-science material into the ai_radar library, and runs the social-science daily scan. Use when the user shares articles, papers, or links about economics, growth, development, digital policy, regulation, causal methods, political science, or AI's societal impacts — for example, "save this article", "add this paper to my radar", "ingest these links", "review my saved articles", or "run the social science scan". Not for AI-engineering material such as agent architecture, evaluations, tooling, or MCP — that belongs to ai-engineering-radar.
---

# social-science-radar

Thin domain adapter over the shared engine. Domain identity lives here and in `profiles/social_science/`; all mechanics live in `engine/ENGINE.md` (Skill contract, procedures P1–P8) and `engine/schema.md`. If an instruction would change how *both* radars behave, it belongs in the engine, not here.

## Identity

- **Domain tag:** `social_science`
- **Profile:** `profiles/social_science/profile.md` — eight lenses and the tier rules. Read it before any scoring; it, not this file, defines relevance.
- **Sources:** `profiles/social_science/sources.md` — active watchlists checked first in discovery; proposals recorded per engine P6.5 as pending records in `reviews/source_proposals/social_science.md` (only the user promotes them).
- **Audience voice:** economist and social-science colleagues. Precise about methods, evidence, and identification; no AI hype; always say what a finding changes for research or policy practice.

## Modes

### Ingest (available now)

Trigger: the user shares URLs or references, asks to save/review social-science material, or asks to process `inbox/` files. Follow the engine **Skill contract** (ingest), leading with this domain's lenses.

### Verify provisionals (available now)

Follow the engine **Skill contract** (verify provisionals).

### Daily scan (available now)

Follow the engine **Skill contract** (daily scan): P6 Discovery (curated sources first, then open search; derived lookback) → P8 report composition, writing `reports/social_science/daily/YYYY-MM-DD.md`.

### Unattended daily run (built; pending activation)

The GitHub Actions harness (`.github/workflows/radar-daily.yml`) runs this skill's daily scan with no user present, under the engine's **Unattended mode** section: defer-don't-guess review into `reviews/deferred_candidates/`, egress limited to `profiles/egress_allowlist.md`, scan-evidence artifact required, no git operations. Activation is gated in `docs/ops/2026-07-23-v2-feasibility.md`.

## Hard rules

`CLAUDE.md` is the operating contract — especially the information-boundary policy and its five-question pre-write self-check (engine P7). Rules are referenced, not restated, so they cannot drift.
