# ai_radar

A personal research radar that runs itself: every morning, two AI agents scan the public web for developments in AI economics and AI engineering, verify what they find against original sources, and archive the survivors as structured, citable library entries — under deterministic guardrails that make an autonomous AI system safe to leave alone.

Built by an economist, not a software engineer, as a working answer to a question I kept meeting in my own field: *what does it take to turn a language model into a system you can actually trust with a real, recurring job?*

The radar covers two fields:

- **Social science** — credible developments in generative AI, agentic systems, and AI engineering applied to economics, sociology, political science, and policy research, with particular attention to growth, development, digital technologies, regulation, and empirical methods.
- **AI engineering** — technical practice for building reliable AI-powered research and policy products: agent architecture, harness engineering, tool use, evaluation, validation, observability, context engineering, deterministic guardrails, security, and reproducibility.

Two Claude Code agent skills share one engine: findings are verified, scored against public interest profiles, deduplicated, and archived as structured markdown entries in a growing library (100+ entries and counting). Each skill writes a short daily report for its own audience. The library — not the reports — is the product.

## The interesting part: judgment to the model, guarantees to code

The unattended daily run (04:37 UTC, GitHub Actions, live since 23 July 2026) is designed around one principle: **the model exercises judgment; deterministic code enforces the guarantees.**

- Claude Code performs discovery, review, verification, and report writing — under least privilege: no shell, no git, network restricted to a human-controlled, exact-host domain allowlist.
- Deterministic Python validators (170+ tests) check everything the model wrote from a read-only pristine base: path allowlist, append-only history protection, report integrity, metadata-only review queues, no-echo output. Work that breaks an invariant is discarded — a failed day costs one day's harvest, never library corruption.
- Anything the run cannot safely judge — ambiguous provenance, unreachable sources, boundary doubts — is **deferred into a human review queue instead of guessed at**. Only a human resolves those records, and resolutions are append-only audit trail.
- The harness owns the atomic commit and fast-forward-only push. Authentication is a Claude subscription OAuth token in Actions secrets — never an API key, never in the tree.
- Failures get engineering discipline: every incident is root-caused in a dated write-up under `docs/ops/` (the failure classes so far have all been specification defects, caught by the guardrails at zero corruption cost).

## What the skills do

- **Two live skills** — `social-science-radar` and `ai-engineering-radar` — thin domain adapters over one shared engine, so pipeline behaviour cannot drift between them.
- **Manual ingestion** — paste URLs (singly or in batches) or drop a list file in `inbox/`; batch processing is line-annotated and safely resumable after interruption.
- **Review-gated library** — every candidate gets one of four dispositions (archive · merge/link · retain provisional · reject-with-reason). Nothing enters the accepted library unreviewed; entries carry provenance, source type, per-domain relevance, verification state, and an explicit selection rationale.
- **Provisional verification** — walled or unverifiable sources are quarantined as `provisional` (never report-eligible) and upgraded when their underlying public artifact is supplied.
- **Web discovery** — per-skill daily scan: curated watchlists first, then open web search from the interest profile, over a lookback window derived from the last report (capped at 7 days).
- **Structured library** — one markdown entry per development in `library/entries/`, a regenerable dedup index (`library/INDEX.md`), and a dated rejection log. Quiet days are reported honestly — never padded.

## Repository map

| path | what it is |
|---|---|
| `engine/` | the shared pipeline contract (`ENGINE.md`), entry schema, templates |
| `.claude/skills/` | the two thin domain skills |
| `profiles/` | interest profiles, curated sources, the egress allowlist |
| `library/` | the product: entries, dedup index, rejection log |
| `reports/` | daily reports per domain — a filtered view over the library |
| `reviews/` | human review queues written by automation, resolved only by a human |
| `scripts/` + `tests/` | deterministic validators and their fixture-based test suite |
| `docs/` | requirements, plans, feasibility gates, runbooks, incident write-ups |
| `.github/` | the unattended harness (workflow + run prompt) |

The `docs/` directory is deliberately part of the showcase: the project was built requirement-first (numbered requirements with acceptance criteria, staged rollout gates, rollback plans), and the ops notes record real failures with real root causes.

## Reuse

Everything here is public-source-derived and public-safe. Content enters only through public web discovery or deliberately supplied URLs; a five-question information-boundary self-check runs before every write (see `CLAUDE.md`).

- **Code** (`scripts/`, `tests/`, `engine/`, `.claude/`, `.github/`): MIT — see `LICENSE`.
- **Content** (`library/`, `reports/`): CC BY 4.0 — see `CONTENT_LICENSE.md`. Entries summarize and quote third-party public sources under their own terms; each entry cites its source.

To replicate the setup you need a Claude subscription (the workflow expects a `CLAUDE_CODE_OAUTH_TOKEN` Actions secret, generated with `claude setup-token`), your own interest profiles under `profiles/`, and your own egress allowlist. No other credentials exist anywhere in this repository.

---

Part of [Harry Does AI](https://harryaquijeballon.com/) — my applied AI implementation work as an economist.
