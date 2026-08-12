# 2026-07-27 — First scheduled runs failed: delivery gate never fired on `schedule` triggers

## What happened

The schedule activated at stage 8 fired for the first time over 2026-07-24 →
2026-07-27. All scheduled runs failed the outcome gate:

| date | run | duration | what actually happened |
|---|---|---|---|
| 2026-07-24 | 30088493851 | 36s | Model step died instantly (1 turn, 562 ms, $0, `is_error: true`) — an immediate API-side error on the OAuth session (transient / usage-related; output hidden by the action). Classified `auth`. Not a harness defect. |
| 2026-07-25 | 30154883225 | 3m5s | Model completed (43 turns, no error) but bailed without performing the scan or writing `scan-evidence.json`. `check_scan_evidence` correctly aborted (`ABORT EVIDENCE_MISSING`, class `tooling`). Guardrail worked as designed against a degenerate model run — same live negative as drill run 30022109296. |
| 2026-07-26 | 30198956789 | 18m34s | **Full correct run discarded by the harness bug below.** Model produced 7 accepted entries + 1 merge + 4 deferrals; validate found 4 REPAIRABLE findings; repair pass fixed them; full-suite revalidation passed. Delivery was then *skipped*, outcome classified `tooling`, work thrown away. |
| 2026-07-27 | 30266494641 | — | Scheduled run executed before the fix landed; same skip expected. Recovery: post-fix `workflow_dispatch mode=full`. |

## Root cause (the 2026-07-26 class)

`Deliver (attempt 1)` was gated on `inputs.mode == 'full'`. The `inputs`
context is only populated on `workflow_dispatch`; on `schedule` triggers
`inputs.mode` is the empty string, so the condition was false on **every**
scheduled run — delivery could never happen, and `classify_outcome` mapped
the resulting `deliver1 == none` under `mode=schedule` to `tooling`.

All rollout drills (stages 3–7) ran via `workflow_dispatch` with an explicit
mode, so the gate always evaluated as intended during certification; the first
scheduled fires were the first time the empty-`inputs` path was exercised.

## Fix

The gate now treats a scheduled run as a full run:

```yaml
if: >
  (steps.validate1.outputs.verdict == 'pass' ||
   steps.revalidate1.outputs.verdict == 'pass') &&
  (inputs.mode == 'full' || github.event_name == 'schedule')
```

No validator, delivery-script, or classification change was needed —
`deliver1=pushed` under `mode=schedule` already classifies `success`.
Structural regression test added:
`test_workflow_structure.test_delivery_gate_covers_scheduled_runs`.

## Non-defects observed in the same window

- 2026-07-24 instant model failure: transient API error; single-attempt design
  accepts this (next day retries naturally). Watch frequency; no change now.
- 2026-07-25 model bail without scan: caught by the evidence validator exactly
  as certified. Probabilistic model behaviour; hard rules held.
- Scheduled fires landed 10:40–12:34 UTC against an expected 09:07 UTC
  (10:07 Europe/London). The delay pattern is consistent with GitHub either
  ignoring the `timezone` key on `on.schedule` or ordinary scheduler delay —
  to be resolved with the planned move of the schedule to early morning.

## Reschedule (2026-07-27, user-approved)

Requirement: the run must complete before the user's working day (~08:00
London) so it never competes with interactive Claude usage for the shared
subscription's rate limits — the likely aggravator of the 2026-07-24
instant model failure.

Decision: `cron: "37 4 * * *"` declared **in UTC**, `timezone` key removed.

- All four live fires started 33 min–2 h 27 min after 10:07 **UTC**, matching
  a UTC interpretation of the cron plus normal scheduler delay — the
  `timezone` key was accepted but evidently not honoured. Declaring UTC
  directly removes the ambiguity.
- 04:37 UTC = 05:37 London (BST) / 04:37 (GMT): pre-workday year-round with
  ample headroom for GitHub's scheduler delay (observed up to ~2.5 h) plus
  the 12–19 min run itself. No exact-time requirement per the user.
- Off-hour minute (`:37`) per GitHub's guidance to avoid the top-of-hour
  scheduler congestion, which both delays fires and raises drop risk.
- Run-date safety: `london_today()` maps 04:37/05:37 to the same London
  calendar date in both seasons — no report-date rollover edge.
- Structural test updated to pin the new schedule
  (`test_schedule_active_at_approved_time_only`).
- First fire on the new schedule expected 2026-07-28 ~04:37 UTC — also the
  first end-to-end proof of the schedule-trigger delivery fix above.
