# 2026-09-01 — Pilot evaluation (U10 / runbook stage 9)

Stage-9 review of the unattended daily radar pilot, due 2026-08-07 to
2026-08-20 and held 2026-09-01 (overdue; the delay itself produced no harm —
the observation-mode rule held and every failure was loud). The R38 and R45
recommendations below were **approved by the user on 2026-09-01** and are
recorded in the runbook stage-9 row.

## 1. Window and evidence basis

Two phases, with different evidence quality:

- **Private phase, 2026-07-23 → 2026-08-12.** Run history did not migrate to
  the public repository ("ai_radar: public debut", 2026-08-12, squashed
  history). Evidence: the ops notes written at the time
  (2026-07-27 incident, 2026-07-28 model-bail review, 2026-07-31 pilot
  learnings and one-week extension, 2026-08-12 validation-abort review) and
  the report/library artifacts carried into the tree. Report gaps in this
  phase: 07-24 to 07-26 (documented first-fire failures), 08-01, 08-02,
  08-05, 08-07 (documented in the extension-period notes).
- **Public phase, 2026-08-13 → 2026-09-01.** Fully verifiable from the
  Actions API and the tree. **20 scheduled fires, 16 success / 4 failure
  (80%)**; no day passed silently (see §3).

## 2. Scheduled-run reliability (verifiable phase)

| date | outcome | class | note |
|---|---|---|---|
| 08-13 → 08-15 | success ×3 | — | fires within ~25 min of slot |
| 08-16 | **failure** | tooling | evidence-missing model run (run 31928062286); attempt-2 also degenerate |
| 08-17 → 08-26 | success ×10 | — | longest clean streak of the pilot |
| 08-27 | **failure** | push | single transient push error discarded a complete run (run 33087741300) |
| 08-28 | **failure** | tooling | evidence-missing model run (run 33192047540) |
| 08-29 → 08-31 | success ×3 | — | fires now 5–7 h late (cron drift, see below) |
| 09-01 | **failure** | tooling | scan delegated to a background agent, died with the turn (run 33492847557); recovered same day by `workflow_dispatch mode=full` |

Two operational findings, both addressed 2026-09-01 (commit `03189dc`):

1. **Model-bail variants persist** (3 of 4 failures). New run-prompt rules:
   delegation to background agents forbidden outright; scan-evidence
   artifact must be written before the reports, so a dying run leaves
   evidence, never orphan reports.
2. **A single transient push error could discard a perfect run.** Delivery
   now retries transient pushes (3 tries, 5 s/15 s backoff) and preserves
   redacted git stderr in the diagnostics artifact.

Separately, **GitHub scheduler drift** since 2026-08-27 (fires 5–12 h late;
GitHub-side, timeliness impact only) is documented in
`2026-09-01-github-cron-drift.md`: monitor, re-register the cron minute with
user approval if it persists into mid-September.

## 3. The headline guarantee held

The plan's acceptance question — *did any day pass silently?* — answers
**no** for the entire pilot. Every one of the four verifiable failures
failed the outcome gate (red run + notification + diagnostics artifact),
and on no failed day did a report or partial library state reach the tree.
Across every failure mode observed since activation (auth, model bail,
harness bug, push race, push error, background-agent delegation) the
library was never corrupted and no bad report was published — consistent
with the 2026-07-31 finding, now over a much longer window.

## 4. Product quality over the pilot

- **Library**: 245 entries at review date; the accumulating structured
  library remained the single source of truth and INDEX stayed derivable.
- **Provisional hygiene**: 0 provisional entries outstanding — everything
  ingested was either verified up to `accepted` or logged as rejected.
- **Quiet-day honesty (R39)**: of 31 report days in the tree per domain,
  social_science reported 22 quiet days and ai_engineering 12, each with
  the verbatim statement plus scan-evidence block. No padded reports
  observed.
- **Updates discipline**: corrections continued to land as append-only
  dated additions; no original claims rewritten.

## 5. Review queues and human burden

| queue | records | pending |
|---|---|---|
| deferred_candidates/social_science | 16 | 7 |
| deferred_candidates/ai_engineering | 13 | 9 |
| source_proposals (both domains) | 2 | 2 |

The 2026-07-31 warning stands: the queues are the design's safety valve and
they are accumulating faster than they are triaged. 18 pending records
across the four files need a first triage pass; a standing cadence
(suggested: weekly, alongside report reading) should be part of pilot
close.

## 6. U10 close-out decisions (user-approved 2026-09-01)

1. **R38 — notifications: failure-only.** 20 days of evidence show success
   is the norm and every failure is independently loud (red run +
   diagnostics artifact). Every-run notifications have served their pilot
   purpose. Applied as a user-side GitHub setting: Settings →
   Notifications → Actions → "Only notify for failed workflows".
2. **R45 — `workflow_dispatch` `full` mode: kept enabled.** It is the
   recovery path for missed days and was used for exactly that on
   2026-07-27 and 2026-09-01; it is user-triggered and inherits every
   guardrail of the scheduled path.
3. **Token renewal reminder.** Clarified 2026-09-01: the
   `CLAUDE_CODE_OAUTH_TOKEN` secret is generated from the user's Claude
   Max subscription (`claude setup-token`) — no separate cost, ever; only
   the credential string expires (~1 year from 2026-07-23, so renewal due
   ~2027-06 per activation step 3's calendar reminder). On expiry the
   failure mode is a loud AUTH-class red run, never silent breakage.
4. **Manual acceptance test — the one open item.** User picks one pilot
   day at random and traces report → entry → cited source, and job
   summary → commit. v2's definition of done closes when this trace is
   recorded here.

## 7. Recommendation

Close the pilot as **successful**: the failure-containment guarantee held
for six weeks under six distinct failure modes, quiet-day honesty is
demonstrated at scale, and the two systematic defects the window exposed
were fixed on diagnosis day. Residual risks (scheduler drift, queue
triage debt, personal-account repo ownership) are documented with owners
and triggers rather than left implicit.
