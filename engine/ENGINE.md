# Engine Pipeline — procedures both radar skills follow

The skills (`social-science-radar`, `ai-engineering-radar`) are thin adapters: they carry domain identity and invoke these procedures by name. Anything that would change both skills' behavior lives here. Entry formats, dispositions' write details, dedup matching rules, and the index/rejection formats live in `engine/schema.md`; this file defines *when* each happens.

State is derived from artifacts, never stored separately: a skill's last run date is the date of its newest file in `reports/<domain>/daily/`; dedup state is `library/INDEX.md` plus the entries; rejected sources are `library/rejections.md`.

## Skill contract

How every radar skill invokes this engine — skills add only identity on top (domain tag, profile and source pointers, audience voice, routing boundary):

- **Clean base first** — every interactive run (ingest or daily scan) begins by running `python3 scripts/validators/check_clean_base.py`. On any `ABORT` line, stop and show it to the user — commit, stash, discard, or conflict resolution is theirs, never the run's. Behind-only is synchronised with a fast-forward-only pull before proceeding; the same-day union rule (P8.6) applies only after a passing check.
- **Ingest** — pasted candidates run P1 → P2 → P3; inbox files run P5. P7 runs before every write. Score every candidate against both domain profiles (cross-domain rule), leading with the invoking skill's domain lenses. Report each disposition to the user: the decision, the driving lens and tier, and the path of any artifact written.
- **Verify provisionals** — run P4 on explicit request or whenever P2 dedup matches a provisional entry.
- **Daily scan** — run P6 → P8 for the invoking skill's domain, writing that skill's dated report. Each skill states its own availability for this mode.

All run-scoped dates — "today", report filenames, `captured` — derive from Europe/London, never from the machine's local clock or UTC.

## The three bars

1. **Discovery bar** — a *discovered* candidate enters review only if a quick read scores at least `medium` relevance for the running skill's domain profile. Below: drop silently (no artifact). Manually supplied candidates skip this bar — deliberate user submission is itself a relevance signal — but never skip review.
2. **Library bar** — the review judgment (P3): a candidate is archived only when it adds a development worth retaining under the profiles; weak or off-profile candidates are rejected with the reason logged, even if manually supplied.
3. **Report bar** — the highest: `status: accepted` AND `verification: verified` AND relevance `high` for the reporting domain AND a practical implication a reader could act on. Provisional or partially verified entries never appear as report items.

## P1 — Intake

Accept candidates from three paths:

- **Pasted**: the user provides one or more URLs/references in conversation. Each becomes a candidate; batch failures never abort the batch.
- **Inbox file**: a text/markdown file in `inbox/` with one source per line (optional note after the URL). Process line-by-line per P5.
- **Discovered**: candidates produced by P6 (Discovery). Apply the discovery bar before review.

For every candidate, run P2 → P3. Apply the information-boundary self-check (P7) before every write, whatever the path.

## P2 — Review

For each candidate:

1. **Fetch and read** the source. If unreachable, distinguish two cases. *Real but walled* (e.g., LinkedIn, paywall — the source verifiably exists): manual path → metadata-only provisional entry (schema.md disposition 3) with a note requesting the underlying public artifact; discovery path → skip entirely. *Dead or non-resolving* (404, no such identifier): failure — annotate/report `failed: <reason>`, write no artifact on either path.
2. **Verify**: trace every claim you intend to summarize back to the source text; label anything untraceable "(unverified)". Attempt independent corroboration only for load-bearing factual claims (headline numbers, benchmark results, bibliographic identity). Record what was and was not corroborated in Verification notes.
3. **Score** against *both* domain profiles (`profiles/*/profile.md`): tier high/medium/low/n-a per domain, with a one-line reason each. A candidate tagging `medium`+ in both domains is cross-domain: one entry, both tags.
4. **Dedup** against `INDEX.md` and `rejections.md` per schema.md's matching rules (identifier first, similarity second, same-artifact rule). A match to a provisional entry triggers P4 for that entry. A match in the rejection log ends processing (discovery) or prompts the user (manual re-submission — their insistence triggers re-review).

## P3 — Disposition

Choose exactly one per candidate (write details in schema.md):

1. **Archive new** — clears the library bar with verification `verified` or `partial`: new entry + INDEX row. `partial` verification with substantial traceability may still be `accepted` if no load-bearing claim is unverified; otherwise `provisional`.
2. **Merge / link** — dedup matched an existing development: dated Updates line and/or Related link on the existing entry; extend `canonical_ids`; no new entry.
3. **Retain provisional** — relevance clears the library bar but claims cannot be verified now: entry with `status: provisional`, upgrade path noted in Verification notes.
4. **Reject** — below the library bar or fails the boundary check: one line in `rejections.md` with the reason. Manual submissions get rejected too when they don't fit the library — record the reason so the user can see why.

Ordering rule (interruption safety): write the disposition artifacts (entry, INDEX row, rejection line) **before** annotating any inbox line or reporting the candidate done.

## P4 — Verify Provisionals

Fires in two ways: (a) P2 dedup matches a new candidate to a `provisional` entry; (b) the user explicitly asks to verify provisional entries.

For each target entry: re-attempt verification using the new candidate and/or a fresh fetch. On success: edit `status` to `accepted`, update `verification`, append a dated Updates line naming what verified it. On failure: leave provisional, append a dated line recording the attempt. Never delete a provisional entry for failing verification — only the user removes entries.

## P5 — Inbox processing

For each unannotated line in an inbox file, oldest file first:

1. Run P1→P3 for the line's source.
2. **After** disposition artifacts are written, annotate the line in place with `→ archived <entry-path>` / `→ merged <entry-path>` / `→ provisional <entry-path>` / `→ rejected: <reason>` / `→ failed: <reason>`.
3. A failure annotates the line and continues; it never aborts the batch.
4. Resume rule: a rerun processes only unannotated lines. (If an entry exists but its line is unannotated — the interruption window — dedup catches the reprocess as a merge, which is safe.)
5. When every line is annotated, move the file to `inbox/processed/`.

## P6 — Discovery (per skill)

1. **Window**: search back to the newest report in `reports/<domain>/daily/` dated **strictly before today** (Europe/London), capped at 7 days. No such report → the full 7-day cap. (A report already written today — by an earlier manual run or the scheduled run — never collapses the window to zero.)
2. **Curated sources first**: work through the active list in `profiles/<domain>/sources.md` — new output from watched researchers, outlets, repositories within the window.
3. **Open search second**: queries derived from the profile's interest lenses (and watchlist names) for material the curated list would miss.
4. Each candidate: discovery bar → P2 → P3.
5. **Source proposals**: a genuinely good source not on the active list becomes a `pending` record in `reviews/source_proposals/<domain>.md` (format: `engine/templates/source-proposal.md`). Check first whether the source is already active, already proposed, rejected, or clearly covered; a re-encountered pending proposal gets only its `last_encountered` date bumped plus materially new justification appended — never a duplicate record. Never query pending sources; only the user (or an interactive session with the user's explicit approval) promotes one into `profiles/<domain>/sources.md`. `profiles/` is never written by a scan.

## P7 — Information-boundary self-check (before every write)

Run the five questions from `CLAUDE.md` (source? public or user-supplied? destination tracked? could it reveal non-public information? permitted for its audience?) before writing any entry, report, profile edit, index/log line, or commit message. If any answer is unclear: stop and ask the user.

## P8 — Compose daily report (per skill)

Written to `reports/<domain>/daily/YYYY-MM-DD.md` from `engine/templates/daily-report.md`, only by a radar run (ingestion alone never writes reports).

1. **Candidates**: today's archived/updated entries relevant to this domain. An updated entry re-qualifies only if the *new* information itself clears the report bar (shown flagged "update:", linking the entry).
2. **Selection**: apply the report bar. More than 3 qualify → rank by relevance strength, then recency; keep the top 3.
3. **Items**: each carries title; why-it-matters for *this* skill's audience; source, publication date, source type; entry link; one-line selection rationale.
4. **Footer — "Also archived today"**: one-liners for displaced qualifying items (flagged as such) and other entries archived today that didn't reach the bar. Nothing disappears silently.
5. **Quiet day**: nothing qualifies → the report states, verbatim: "No material developments cleared the reporting bar today." — and carries a `## Scan evidence` block (`- curated sources fetched: <n>` / `- queries executed: <n>`). A quiet day without scan evidence is not a quiet day; it is an incomplete run. Never pad.
6. **Same-day rerun**: regenerate the file as the union of the day's qualifying items. Existing items keep their places unless a new item strictly outranks them; displaced items move to the footer.
7. **Cross-domain entries** may appear in both skills' reports — audiences and why-it-matters differ — always backed by the single shared entry.
8. **Deferred candidates** (unattended mode, below) never appear as items or footer lines.

## Unattended mode

How the scheduled harness (`.github/workflows/radar-daily.yml`) runs both skills with no user available. Everything above applies unchanged except as stated here. The deterministic validators (`scripts/validators/`) enforce these rules from a read-only pristine base — this section instructs the run; the validators are what guarantee it.

**Candidate lifecycle.** Unattended review adds one state beside the schema's entry statuses: a candidate is `accepted`, `provisional` (clearly appropriate for the library, verification incomplete), **`deferred`** (safe admissibility unresolved — a metadata-only queue record, **no entry of any kind**), or `rejected`. `deferred` is a queue-level state: `engine/schema.md` and entry frontmatter are unchanged. Resolution of a deferred record is human-only.

**P7-unattended.** The manual rule "stop and ask the user" becomes: **defer this candidate and continue safely.** When a candidate is ambiguous, inaccessible, insufficiently verified for even a provisional judgment, or raises any information-boundary doubt: do not guess, do not stop the run — append one metadata-only record to `reviews/deferred_candidates/<domain>.md` (format: `engine/templates/deferred-candidate.md`; reason classes and statuses are closed vocabularies) and move on. A boundary doubt always produces `deferred`, never `provisional`, never an entry: provisional assumes inclusion is appropriate; deferral means appropriateness itself is unresolved. Boundary uncertainty is never resolved in favour of inclusion.

**Deferral procedure.** Before writing, dedup the candidate URL against `INDEX.md`, `rejections.md`, and both deferred queue files. New and unresolved → one `pending` record. Already `pending` → bump `last_encountered` and, for materially new context, keep the existing `reason`/`action_needed` text **verbatim** and append after it (e.g. `; re-encountered via open search`) — never rephrase, shorten, or rewrite it, and never write a duplicate record. Appends share the field's hard 240-character budget (the queue validator's per-field bound): keep them telegraphic, and when a dated append cannot fit within the bound, record only the `last_encountered` bump — the bound always outranks the append, and shortening existing text to make room is itself a violation. Any resolved status (`archived`, `provisional`, `rejected`, `dismissed`, `duplicate`) → silent skip, exactly like a rejection-log line. Never resolve, remove, or rewrite a record. A cross-domain deferral gets **one** record in the surfacing domain's file, `domain` listing both.

**Egress rule (user decision, Option A).** Fetch only from domains on `profiles/egress_allowlist.md`. A promising result on any other domain is never fetched: defer it (`reason_class: access_or_license_unclear`, action: approve domain or dismiss) or record a source proposal, and continue. Unknown domains are never added to the allowlist by a run.

**Scan-evidence artifact.** Before finishing, write machine-readable evidence to the path in `$RADAR_EVIDENCE_PATH` (outside the repository tree):

```json
{"run_date": "YYYY-MM-DD",
 "domains": {"social_science": {"curated_sources_fetched": N, "queries_executed": N},
             "ai_engineering": {"curated_sources_fetched": N, "queries_executed": N}}}
```

Counts are actual activity performed. The harness treats a missing or malformed artifact as a TOOLING failure on every outcome, including no-change.

**Hard boundaries.** Never touch `inbox/` (batch material is a separate, user-triggered workflow), `profiles/`, `engine/`, `.claude/`, `scripts/`, `tests/`, `.github/`, or any git operation — the harness owns commit and push. Never modify a report dated other than today, delete anything, rewrite existing entry bodies (changes to an existing entry are the permitted frontmatter fields plus dated appends in or after its Updates section), or alter existing queue records beyond the deferral procedure above.

**Degraded operation.** One difficult candidate never blocks the run — defer it and continue. Growing and validating the library with quiet-day reports is success; finding nothing with evidence of a real scan is success; a report item without its accepted library entry is failure; work that exists only in the runner is an incomplete run.
