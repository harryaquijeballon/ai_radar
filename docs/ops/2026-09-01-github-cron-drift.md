# 2026-09-01 — GitHub scheduler drift: 04:37 UTC cron firing 5–12 h late since 2026-08-27

## What happened

The `radar-daily` schedule (`cron: "37 4 * * *"`, UTC, unchanged since
2026-07-27) fired within ~25 min of its slot from 2026-08-15 through
2026-08-26. From 2026-08-27 onwards every fire has been hours late:

| date | fire (UTC) | delay |
|---|---|---|
| 2026-08-26 | 05:07 | +0h30 |
| 2026-08-27 | 15:25 | +10h48 |
| 2026-08-28 | 16:52 | +12h15 |
| 2026-08-29 | 11:19 | +6h42 |
| 2026-08-30 | 10:04 | +5h27 |
| 2026-08-31 | 11:05 | +6h28 |
| 2026-09-01 | 09:33 | +4h56 |

## Assessment: GitHub-side, not our bug

- Nothing in the repository changed between the last on-time fire (08-26)
  and the first late one (08-27): no workflow, schedule, or harness edits.
- `on.schedule` is documented by GitHub as best-effort; delays under
  scheduler load are a known, widely reported behaviour, and the off-hour
  minute (`:37`) was already chosen to mitigate the milder form of it
  (see the 2026-07-27 ops note).
- The runs themselves execute normally once started — the drift affects
  start time only.

## Impact

- **Timeliness only, not correctness.** `london_today()` maps even the
  worst fire (16:52 UTC) to the same London calendar date, and the P6.1
  lookback is "strictly before today", so report dating and scan content
  are unaffected.
- The 2026-07-27 requirement that runs finish before the working day
  (~08:00 London) is currently not met: reports are landing mid-morning
  to mid-afternoon.
- Late fires land inside interactive working hours, recreating the
  shared-subscription rate-limit contention the 04:37 slot was chosen to
  avoid, and widening the window for push races with interactive commits
  (the 2026-08-27 `push-error` failure, run 33087741300, occurred in
  exactly that window; delivery now retries transient push errors 2–3
  times and preserves git stderr in diagnostics).

## Decision (2026-09-01)

Document and monitor; no schedule change now. If drift persists into
mid-September, the candidate mitigation is re-registering the schedule
(editing the cron minute), which anecdotally resets chronic drift —
a schedule change requires explicit user approval per the runbook.
Recovery for any missed day remains `workflow_dispatch mode=full`.

## Context

The four scheduled failures in the pilot window (2026-08-16, 08-27,
08-28, 09-01 — runs 31928062286, 33087741300, 33192047540, 33492847557)
have separate causes diagnosed 2026-09-01: one transient push error
(retry added), three evidence-missing model runs (2026-09-01: scan
delegated to a background agent — now forbidden by the run prompt, which
also mandates evidence-before-reports ordering). This note covers only
the shared timing drift.
