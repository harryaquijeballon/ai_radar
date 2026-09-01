# ai_radar

A personal research radar that runs itself. Every morning, two AI agents scan the public web for developments in AI economics and AI engineering, verify what they find against original sources, and archive the selected papers as structured, citable library entries, under deterministic guardrails that make an autonomous AI system safe to leave alone.

The radar covers two fields.

- **Social science.** Credible developments in generative AI, agentic systems, and AI engineering applied to economics, sociology, political science, and policy research, with particular attention to growth, development, digital technologies, regulation, and empirical methods.
- **AI engineering.** Technical practice for building reliable AI-powered research and policy products. Agent architecture, harness engineering, tool use, evaluation, validation, observability, context engineering, deterministic guardrails, security, and reproducibility.

Two Claude Code agent skills share one engine. Findings are verified, scored against public interest profiles, deduplicated, and archived as structured markdown entries in a growing library (240+ entries and counting). Each skill writes a short daily report for its own audience. The final product is the library, built over time as a curated selection of papers across the two categories.

## Judgment to the model, guarantees to code

The unattended daily run (04:37 UTC, GitHub Actions, live since 23 July 2026; pilot reviewed successful on 1 September 2026) is designed around one principle. **The model exercises judgment, and deterministic code enforces the guarantees.**

- Claude Code performs discovery, review, verification, and report writing under least privilege. No shell, no git, and network access restricted to a human-controlled, exact-host domain allowlist.
- Deterministic Python validators (170+ tests) check everything the model wrote from a read-only pristine base. Path allowlist, append-only history protection, report integrity, metadata-only review queues, no-echo output. Work that breaks an invariant is discarded, so a failed day costs one day's harvest, never library corruption.
- Anything the run cannot safely judge, such as ambiguous provenance, unreachable sources, or boundary doubts, is **deferred into a human review queue instead of guessed at**. Only a human resolves those records, and resolutions are an append-only audit trail.
- The harness owns the atomic commit and fast-forward-only push. Authentication is a Claude subscription OAuth token in Actions secrets, never an API key, and never in the tree.
- Failures get engineering discipline. Every incident is root-caused in a dated write-up under `docs/ops/` (the failure classes so far have all been specification defects, caught by the guardrails at zero corruption cost).

## What the skills do

- **Two live skills**, `social-science-radar` and `ai-engineering-radar`, are thin domain adapters over one shared engine, so pipeline behaviour cannot drift between them.
- **Manual ingestion.** Paste URLs (singly or in batches) or drop a list file in `inbox/`. Batch processing is line-annotated and safely resumable after interruption.
- **Review-gated library.** Every candidate gets one of four dispositions (archive · merge/link · retain provisional · reject with reason). Nothing enters the accepted library unreviewed. Entries carry provenance, source type, per-domain relevance, verification state, and an explicit selection rationale.
- **Provisional verification.** Walled or unverifiable sources are quarantined as `provisional` (never report-eligible) and upgraded when their underlying public artifact is supplied.
- **Web discovery.** Per-skill daily scan. Curated watchlists first, then open web search from the interest profile, over a lookback window derived from the last report (capped at 7 days).
- **Structured library.** One markdown entry per development in `library/entries/`, a regenerable dedup index (`library/INDEX.md`), and a dated rejection log. Quiet days are reported honestly, never padded.

## Repository map

| path | what it is |
|---|---|
| `engine/` | the shared pipeline contract (`ENGINE.md`), entry schema, templates |
| `.claude/skills/` | the two thin domain skills |
| `profiles/` | interest profiles, curated sources, the egress allowlist |
| `library/` | the product. Entries, dedup index, rejection log |
| `reports/` | daily reports per domain, a filtered view over the library |
| `reviews/` | human review queues written by automation, resolved only by a human |
| `scripts/` + `tests/` | deterministic validators and their fixture-based test suite |
| `docs/` | requirements, plans, feasibility gates, runbooks, incident write-ups |
| `.github/` | the unattended harness (workflow + run prompt) |

The `docs/` directory is deliberately part of the showcase. The project was built requirement-first (numbered requirements with acceptance criteria, staged rollout gates, rollback plans), and the ops notes record real failures with real root causes.

## Reuse

Everything here is public-source-derived and public-safe. Content enters only through public web discovery or deliberately supplied URLs, and a five-question information-boundary self-check runs before every write (see `CLAUDE.md`).

- **Code** (`scripts/`, `tests/`, `engine/`, `.claude/`, `.github/`) is MIT licensed. See `LICENSE`.
- **Content** (`library/`, `reports/`) is CC BY 4.0. See `CONTENT_LICENSE.md`. Entries summarize and quote third-party public sources under their own terms, and each entry cites its source.

To replicate the setup you need a Claude subscription (the workflow expects a `CLAUDE_CODE_OAUTH_TOKEN` Actions secret, generated with `claude setup-token`), your own interest profiles under `profiles/`, and your own egress allowlist. No other credentials exist anywhere in this repository.

---

Part of [Harry Does AI](https://harryaquijeballon.com/), my applied AI implementation work as an economist.
