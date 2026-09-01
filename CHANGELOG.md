# Changelog

All notable changes to ai_radar are recorded here.

## v2.0.0 — activated 2026-07-23; pilot closed successful 2026-09-01

The unattended daily radar ran a six-week pilot (activation 2026-07-23 → review 2026-09-01; evaluation in `docs/ops/2026-09-01-pilot-evaluation.md`). Verifiable window 2026-08-13 → 2026-09-01: 16 of 20 scheduled runs delivered, 4 failures — every one loud (red run + diagnostics), none silent, zero library corruption across six distinct failure modes; the missed 2026-09-01 report was recovered same-day via `workflow_dispatch mode=full`. Library at review: 245 entries, 0 provisional outstanding, quiet days reported honestly throughout. Pilot-close decisions (user-approved): **R38** notifications switch to failure-only; **R45** `full` dispatch mode kept as the recovery path. Hardening applied on diagnosis day: run prompt forbids background-agent delegation and mandates evidence-before-reports ordering; delivery retries transient push errors (3 tries) and preserves redacted git stderr in diagnostics; GitHub-side cron drift (fires 5–12 h late since 2026-08-27) documented with a monitor-then-re-register plan (`docs/ops/2026-09-01-github-cron-drift.md`). Open at close: the U10 manual acceptance trace; OAuth token renewal due ~2027-06.

## v2 — implementation complete 2026-07-23 (not yet activated)

The unattended daily radar: a GitHub Actions harness (10:07 Europe/London, activation-gated) runs both skills' bounded discovery through the engine's new **Unattended mode** — defer-don't-guess review into append-only `reviews/` queues, egress restricted to `profiles/egress_allowlist.md`, machine-checked scan evidence — while repository-owned deterministic validators (`scripts/validators/`, 136 tests) enforce the path allowlist, history protection, entry-body preservation, report bar, and no-echo output from a read-only pristine base; the harness owns atomic commit, fast-forward-only push, and a statically unrolled second attempt. Authentication is bound to `CLAUDE_CODE_OAUTH_TOKEN` only (no API key, structurally checked). The v1 entry schema is unchanged. Built across units U1–U10 of `docs/plans/2026-07-23-001-feat-unattended-daily-radar-plan.md`; requirements in `docs/brainstorms/2026-07-23-unattended-daily-radar-requirements.md`. **No token exists, no model-dependent workflow has run, and the schedule is commented out** until the activation gate (Q1–Q4, `docs/ops/2026-07-23-v2-feasibility.md`) is explicitly approved; rollout follows `docs/ops/v2-rollout-runbook.md`. The `v2.0.0` tag is cut at activation.

## v1.0.0 — 2026-07-22

First complete version. A personal, public-source-first knowledge radar: two Claude Code agent skills over one shared engine that verify, score, deduplicate, and archive public developments into a structured markdown library, with a short daily report per skill. Built script-free, library-first, across eight user-reviewed implementation units (U1–U8).

### Delivered

- **Operating contract** (`CLAUDE.md`) — public-source-first, controlled-internal-access information boundary with a named five-question pre-write self-check; repository-governance rules (private by default); architecture map; diagram convention; run instructions.
- **Shared engine** (`engine/`) — `ENGINE.md` (the Skill contract plus procedures P1–P8: intake, review, disposition, verify-provisionals, resumable inbox processing, discovery, boundary self-check, report composition); `schema.md` (frozen v1 entry schema, four dispositions, identifier-first dedup, derived index, rejection log); entry and daily-report templates.
- **Two live skills** (`.claude/skills/`) — `social-science-radar` and `ai-engineering-radar`, thin domain adapters carrying identity only; ingestion, provisional verification, and daily scan.
- **Domain configuration** (`profiles/`) — user-edited interest profiles (8 relevance lenses each) and curated, typed, justified source watchlists per domain.
- **The library** (`library/`) — 25 entries at release across both domains, a regenerable `INDEX.md`, and a dated rejection log. Seeded from a real backlog plus discovery.
- **First daily reports** (`reports/`) — one per skill for 2026-07-22, each a filtered view over the library.

### Key architectural decisions

- **Two user-facing skills, one shared engine.** Identity lives in each skill and its profiles; all mechanics live in the engine. If editing text would change both skills' behaviour, it belongs in the engine — so the two cannot drift, and a third domain would just be a new profile.
- **The library is the product; reports are a filtered view.** Reports never become a second source of truth; every report item traces to a full library entry, which traces to the original source.
- **Review-gated admission with three ascending bars.** Discovery bar (enter review) < library bar (become an accepted entry) < report bar (accepted + verified + high relevance + practical implication). Manual saves skip only the discovery bar; nothing is auto-accepted.
- **Status and relevance are independent axes.** An entry can be `accepted` yet low-relevance (kept, never reported) or `provisional` (quarantined until verified). Reports admit only `accepted` + `verified` + high-relevance items, capped at three, with an honest quiet-day state.
- **State derived from artifacts, never duplicated.** Last-run date = newest report file; dedup = index + entries; no separate state files. The dedup index is regenerable from the entries.
- **Append-only entry history.** Corrections and updates are dated additions; original claims are never silently rewritten, preserving traceability over an entry's life.
- **Script-free v1.** The engine is markdown conventions an agent follows; Python tooling was deliberately deferred until the workflow is proven by hand.

### Deferred to v2 (by design)

- Scheduling and automation — the daily 2:00 pm run; v1 is manually triggered.
- Python/validation tooling — index rebuild, schema validation, link checking.
- A combined cross-domain overview report on top of the per-skill reports.
- Weekly/monthly synthesis reports; a sharing/publishing mechanism; additional domains beyond the two radars.

### v1 acceptance (U8, user-confirmed)

- Both reports judged shareable as-is with their intended audiences (economist/social-science colleagues; an applied AI product team).
- Report → library entry → original source chain verified end to end; reports confirmed to operate as filtered views, not a separate source of truth.
- Selection and relevance scoring confirmed working: the radar distinguishes high-value developments from general AI news, applies the profiles sensibly, and produces fewer than three items when the evidence does not justify more.
