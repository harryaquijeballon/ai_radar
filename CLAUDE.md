# ai_radar — Operating Contract

## Project purpose

An experimental knowledge and skills project by an economist building AI systems, developed using public sources and designed to support multidisciplinary research and AI product development.

Two agent skills (`social-science-radar`, `ai-engineering-radar`) share one engine and one library. The accumulating structured library is the product; daily reports are its reading surface.

## Information boundary: public-source-first, controlled internal access

Public sources are the project's default. This includes published studies, reports, blogs, presentations, and other material publicly available on the web from any organisation — including the author's employer's published research, which the radar may discover and ingest exactly like any other public source.

Non-public information is strictly controlled:

- Never autonomously browse, list, search, read, or copy material from employer-internal folders, OneDrive, SharePoint, or other connected internal systems. Any such location is outside the project boundary and must never be accessed unless the user gives an explicit, task-specific instruction.
- Content may enter ai_radar only through: public web discovery; URLs or text the user deliberately provides; files the user deliberately places inside the project.
- Non-public information requires the user's explicit approval for each use. Never copy it into tracked repository files or commit it to GitHub unless the user explicitly confirms that both the material and the repository are approved for that purpose.
- `internal/` is a local-only, git-ignored directory for explicitly approved internal context. Never populate it by searching elsewhere on the computer.
- All library entries and daily radar reports must remain public-safe and shareable. Internal context must never appear in them unless the user explicitly requests an internal-only output.

**Information-boundary self-check — mandatory before every write (entry, report, profile edit, commit message):**

1. What is the source?
2. Is it public or explicitly user-supplied?
3. Is the destination tracked by Git?
4. Could the output reveal non-public information?
5. Is the output permitted for its intended audience?

If any answer is unclear, stop and ask the user.

## Repository governance

- This repository is **public** (decision and pre-publication review: 2026-08-12).
- Everything committed is world-readable the moment it is pushed: the information-boundary self-check above is mandatory before every commit, and secrets exist only as GitHub Actions repository secrets — never in the tree, in any file, or in any commit message.

## Architecture

- `.claude/skills/` — two thin user-facing skills carrying domain identity only (description, selection criteria, audience voice, profile pointers).
- `engine/` — shared machinery both skills follow: pipeline (`ENGINE.md`), entry schema (`schema.md`), templates. Rule: if editing text would change both skills' behavior, it belongs here; if it defines what one radar cares about, it belongs in that skill or its profile.
- `profiles/<domain>/` — configuration: interest profile and curated sources per domain.
- `library/` — the product: one markdown entry per development (`entries/`), a derived dedup index (`INDEX.md`), a dated rejection log (`rejections.md`). Entries are the single source of truth; the index is regenerable from them.
- `reports/<domain>/daily/YYYY-MM-DD.md` — per-skill daily reports. A report is a filtered view over the library, never a second source of truth.
- `inbox/` — drop list files of URLs to ingest; fully processed files move to `inbox/processed/`. Never touched by the unattended run.
- `reviews/` — human review queues written by automation, resolved only by the user: `source_proposals/<domain>.md` and `deferred_candidates/<domain>.md`. Audit trail: records are never deleted or rewritten.
- `scripts/` + `tests/` — deterministic validators and their fixture-based test suite (`scripts/validators/README.md` is the contract; run `python3 -m unittest discover -s tests`).
- `.github/` — the unattended harness (workflow, run prompt, generated model settings). Protected path; activation is gated per `docs/ops/2026-07-23-v2-feasibility.md`.
- `profiles/egress_allowlist.md` — the only domains the unattended run may fetch from (human-controlled; scans defer or propose, never extend it).

## Conventions

- Directories and data use `snake_case` (`social_science`); skills use kebab-case (`social-science-radar`).
- Entry status lives in frontmatter: `accepted` or `provisional`. Provisional entries are never report-eligible until verification upgrades them.
- Every summarized claim must be traceable to its cited source; label unverifiable claims `unverified`. Never infer a publication date silently — `unknown` is a valid value.
- Corrections and material updates are append-only dated additions to an entry's Updates section — never rewrite original claims.
- State is derived from artifacts, never duplicated: a skill's last run date is its newest report file; dedup uses `library/INDEX.md` plus the entries. No state files.
- Quiet days are reported honestly ("no material developments found") — never pad a report with weak items.
- Use Mermaid diagrams whenever they materially clarify architecture, workflows, lifecycle states, decision paths or relationships. Keep every diagram consistent with the current written specification and implementation. Prefer clear prose when a diagram would add no explanatory value.

## Running the radars

- **social-science-radar** (live): `/social-science-radar <urls>`, or ask naturally — "save this article for my radar", "ingest these links", "run the social science scan". Full engine Skill contract: ingestion, provisional verification, and the daily scan (writes `reports/social_science/daily/YYYY-MM-DD.md`).
- **ai-engineering-radar** (live): `/ai-engineering-radar <urls>`, or ask naturally — "save this engineering post", "run the AI engineering scan". Same contract; reports under `reports/ai_engineering/daily/`.
- Batch ingestion for either domain: drop a list file (one URL per line) in `inbox/`; processing is line-annotated and safely resumable (engine P5).
- Every interactive run starts with the engine's clean-base check (`python3 scripts/validators/check_clean_base.py`); on `ABORT`, stop and let the user resolve.
- The unattended daily run (both domains) is **live**: activated 2026-07-23 per the gate in `docs/ops/2026-07-23-v2-feasibility.md`, scheduled at 04:37 UTC (05:37 London in summer, 04:37 in winter — GitHub cron is UTC-only; see `docs/ops/2026-07-27-scheduled-delivery-incident.md`).

## Workflow

- Work follows the implementation units in `docs/plans/`. Commit and push at the end of each approved unit so the user can review the markdown files and Mermaid diagrams on GitHub.
- Never continue past a unit's review checkpoint without the user's explicit approval.
