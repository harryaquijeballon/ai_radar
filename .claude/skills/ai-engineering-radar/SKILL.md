---
name: ai-engineering-radar
description: 'Currently ingests, reviews, and archives AI-engineering material into the ai_radar library — articles, papers, documentation, and saved links about building reliable AI products: agent architecture and orchestration, harness and context engineering, tool use and MCP, evaluations and validation, deterministic guardrails, observability and debugging, reproducibility and testing, security and governance, AI-assisted software development, and model selection, routing, cost or latency. Use for requests like "save this engineering post", "add this to my AI engineering radar", "ingest these tooling links", or "run the AI engineering scan". Does not trigger merely because a source mentions AI — economics, policy, and societal-impact material belongs to social-science-radar. Handles ingestion, provisional verification, and the AI-engineering daily scan.'
---

# ai-engineering-radar

Thin domain adapter over the shared engine. Domain identity lives here and in `profiles/ai_engineering/`; all mechanics live in `engine/ENGINE.md` (Skill contract, procedures P1–P8) and `engine/schema.md`. If an instruction would change how *both* radars behave, it belongs in the engine, not here.

## Identity

- **Domain tag:** `ai_engineering`
- **Profile:** `profiles/ai_engineering/profile.md` — eight lenses and the tier rules. Read it before any scoring; it, not this file, defines relevance.
- **Sources:** `profiles/ai_engineering/sources.md` — active watchlists checked first in discovery; proposals recorded per engine P6.5 as pending records in `reviews/source_proposals/ai_engineering.md` (only the user promotes them).
- **Audience voice:** economists, data scientists, and developers building AI products together. Technically precise but readable by a multidisciplinary product team. Always say what a development changes for *building, testing, or operating* an AI product — never merely report that a model or feature exists.

## Modes

### Ingest (available now)

Trigger: the user shares URLs or references, asks to save/review AI-engineering material, or asks to process `inbox/` files. Follow the engine **Skill contract** (ingest), leading with this domain's lenses.

### Verify provisionals (available now)

Follow the engine **Skill contract** (verify provisionals).

### Daily scan (available now)

Follow the engine **Skill contract** (daily scan): P6 Discovery (curated sources first, then open search; derived lookback) → P8 report composition, writing `reports/ai_engineering/daily/YYYY-MM-DD.md`.

### Unattended daily run (built; pending activation)

The GitHub Actions harness (`.github/workflows/radar-daily.yml`) runs this skill's daily scan with no user present, under the engine's **Unattended mode** section: defer-don't-guess review into `reviews/deferred_candidates/`, egress limited to `profiles/egress_allowlist.md`, scan-evidence artifact required, no git operations. Activation is gated in `docs/ops/2026-07-23-v2-feasibility.md`.

## Hard rules

`CLAUDE.md` is the operating contract — especially the information-boundary policy and its five-question pre-write self-check (engine P7). Rules are referenced, not restated, so they cannot drift.
