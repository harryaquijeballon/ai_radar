---
handover_id: HDAI-AIRADAR-004
date: 2026-11-10
project: ai_radar
type: delta
previous_handover: HDAI-AIRADAR-003
repo_head_at_writing: main @ 3528b2c (this handover lands in the next commit, with plan 2026-11-09-001 Phase 3)
covers: 08076e3 .. 3528b2c, plus the Phase 3 commit that carries this file
visibility: public
visibility_note: >-
  Written from the public repository and the public GitHub Actions run logs
  and diagnostics artifact of runs 2026-09-10 → 2026-11-10. No internal,
  client or employer material was used.
topics:
  - hooks as the fast sensor for an agent without a shell
  - instruction-only dedup
  - enumerating the shapes of a failure
  - evidence retention shorter than the review cycle
  - commit trailers as a stateless metrics store
  - report-only alarms and who sees them
---

# HDAI-AIRADAR-004: delta handover, 2026-11-09 → 2026-11-10

Out-of-cycle delta, one day after HDAI-AIRADAR-003: the session built new harness knowledge (plan `docs/plans/2026-11-09-001-harden-repair-loop-plan.md`, all three phases). Tags as in the baseline: **[implemented]**, **[intended]**, **[measured]**, **[interpretation]**.

## 0. Summary

1. [implemented] Every fix proposed in HDAI-AIRADAR-003 §6 is now mechanism, not instruction: deferral tools denied, scan transcript snapshotted, queue text restored by the harness, repair scope checked, repair outcome reported, coverage floors enforced.
2. [measured] The first real run on those changes (2026-11-10, run 42819765946) confirmed four of them and failed for a new reason: the scan missed dedup on five archived papers, wrote over two entries and created three duplicates. Nothing was delivered.
3. [implemented] Dedup's mechanical part now runs as a hook on the agent's `Write` tool. This is the first sensor in this harness that acts during the model step rather than after it.
4. [implemented] The outer loop got four pieces: an effort and cost alarm, rule ids in the 90-day job log, a queue triage sheet, and a weekly reminder issue.
5. [measured] 2 scheduled runs in range: 1 delivered (11-09), 1 red (11-10). Tests 209 → 290.
6. [interpretation] Not yet proven in production: the hook, the repair-scope check and the repair-outcome row. The 2026-11-11 run is the first evidence.

## 1. What changed

| Commit | Change |
|---|---|
| `613e885` | daily run 2026-11-09 (delivered) |
| `571042a` | incident records for 10-30 and 11-05; HDAI-AIRADAR-003 |
| `64877dd` | Phase 1: deny deferral tools (U1), snapshot the scan transcript (U2), restore grow-only queue text (U3), pin the runner image (U4) |
| `3295b13` | Phase 2: repair scope (U5), repair outcome (U6), coverage floors enforced, no delivery below them (U7) |
| `3528b2c` | U7b: entry write guard hook, `ENTRY_DUPLICATE_IDENTIFIER`, incident record for 11-10 |
| next commit | Phase 3: effort alarm and commit trailers (U8), September review and rule ids in the summary (U9), queue triage sheet (U10), weekly reminder workflow (U11), this handover |

## 2. New or changed lessons

**L12 (new). An agent without a shell gets its fast sensor through a hook.**
- *Rule:* when the agent cannot run a check itself, register the check as a pre-tool hook. The harness runs it at the moment of action and the agent reads only the verdict.
- *Why:* dedup was an instruction. On 11-10 the scan skipped it for five papers; the post-run validators caught the two overwrites and the $6.09 run was discarded [measured, `docs/ops/2026-11-10-dedup-miss-incident.md`]. A post-run sensor can only reject the day. A sensor at the write lets the agent correct itself in the same run.
- *How to apply:* `scripts/entry_write_guard.py`, registered by `build_claude_settings.py --guard-script`, run from the read-only pristine base. Block messages name the existing entry and the allowed action. The guard fails open; the validators stay the gate [implemented].
- *How to check:* the run summary row `duplicate entry writes blocked by harness`; a non-zero count on a day with re-encounters, and no `entry guard errors` row [intended; first data 2026-11-11].

**L13 (new). When a sensor catches one shape of a failure, list the sibling shapes.**
- *Rule:* for each failure, enumerate the ways the same mistake can land, and check each has a sensor.
- *Why:* the dedup miss landed two ways. Writing over an existing entry was caught (`ENTRY_BODY_REWRITTEN`). Writing the same paper under a new slug was caught by nothing: three duplicates would have been delivered had they been the only defect [measured, `violations-1.txt` of run 42819765946 lists no finding for them].
- *How to apply:* `ENTRY_DUPLICATE_IDENTIFIER` (abort) in `check_library_consistency.py` [implemented].
- *How to check:* the library has no shared canonical identifier [measured: 465 entries, 0 shared; 2 pairs share a source URL and await triage].

**L14 (new). Keep evidence at least as long as the review cycle.**
- *Rule:* the facts a write-up needs must live in a store that outlasts the time to the write-up.
- *Why:* the findings of the 09-10, 09-11 and 09-12 failures were only in a 30-day artifact; the first write-up attempt came on day 34. Which rule fired on those three consecutive days is now unknowable, and 22 entries were discarded [measured, `docs/ops/2026-11-10-september-red-runs-review.md`].
- *How to apply:* rule ids and counts per validation stage are printed in the run summary, which goes to the 90-day job log [implemented]. Scan turns, cost and duration go into the daily commit as trailers, which do not expire [implemented].
- *How to check:* a red run's cause class can be read from `gh run view --log` alone.

**L15 (new, [interpretation]). A report-only alarm needs a reader.**
- *Rule:* an alarm that does not fail the run must be routed to someone on a schedule.
- *Why:* GitHub notifies on failure only. The effort alarm (`low_turns`, `high_cost`) is a warning annotation and a summary row by design, so that a cheap or dear day still delivers.
- *How to apply:* the weekly reminder issue carries the week's scan turns and cost from the trailers and is assigned to the owner [implemented]. Whether a weekly look is fast enough is open.
- *How to check:* days between an alarm and its first mention in a handover.

**L8 → implemented.** Deferral tools are denied by bare name; the 11-10 run accepted the settings and called none [measured, `model-run-facts.json`].
**L9 → implemented.** The harness restores grow-only text before every validation; the first real run restored 0 fields [measured]. No recurrence can be claimed yet.
**L10 → implemented, unexercised.** No repair pass has run since.
**L11 → implemented and confirmed.** Coverage on 11-10 was read from the scan's own transcript: 16 of 19 and 16 of 17 [measured].

## 3. Incidents

| Run | Outcome | Write-up |
|---|---|---|
| 2026-11-10, 42819765946 | `validation`, nothing delivered | `docs/ops/2026-11-10-dedup-miss-incident.md` |
| 2026-09-10, 09-11, 09-12, 09-27 (older, now written up) | `validation` | `docs/ops/2026-11-10-september-red-runs-review.md` |

Every red scheduled run since 2026-09-01 now has a write-up.

## 4. Loop changes

- **Feedforward:** the run prompt tells the agent to search the index before each entry and how to act on a guard block; the repair prompt forbids delegation, shortening queue text and raising verification.
- **Fast sensor (new layer, during the model step):** entry write guard hook.
- **Post-run sensors:** coverage floors (social science ≥ 12 of 19, AI engineering ≥ 6 of 17 attempted; below them no delivery, outcome `coverage`), repair scope, duplicate identifier.
- **Mechanical steps moved from agent to script:** queue grow-only text.
- **Outer loop:** effort alarm; rule ids in the job log; `scripts/make_queue_triage.py`; `.github/workflows/handover-reminder.yml`.
- **Loop metrics, new:** repair outcome, queue fields restored, duplicate writes blocked, scan turns / cost / duration (summary rows and commit trailers).

## 5. Decisions

| Date | Decision | Reason | Record |
|---|---|---|---|
| 2026-11-09 | Coverage floors at 12 of 19 and 6 of 17 attempted; below the floor the run is not delivered | user decision; every valid reading since 10-26 clears them (lowest: AI engineering 7) | plan 2026-11-09-001, Phase 2 |
| 2026-11-10 | Dedup by a harness check at the write, not a post-run clean-up of duplicates | user decision (option 1 of 3) | plan 2026-11-09-001, Phase 2b |
| 2026-11-10 | Effort alarm is report-only | a low or dear day should still deliver; the coverage floors are the blocking gate | `scripts/run_metrics.py` |
| 2026-11-10 | Metrics history in commit trailers | "no state files" convention; run logs expire after 90 days | `scripts/run_metrics.py` |

## 6. Open items

| Item (HDAI-AIRADAR-003 §6) | Status |
|---|---|
| Deny deferral tools; snapshot transcript; structural fix for the queue deadlock; repair scope and outcome | Done (`64877dd`, `3295b13`) |
| U12 coverage floors | Done, enforced (`3295b13`) |
| Write-ups for 09-10, 09-11, 09-12, 09-27 | Done; cause of the first three not recoverable |
| Effort and cost alarm | Done, report-only |
| Queue triage: 22 pending, 10 within 15 characters of the cap, none resolved since 2026-08-12 | Open; sheet at `docs/ops/2026-11-10-queue-triage-sheet.md` |
| U15 re-review of 210 window rejections | Paused by the user |
| **New:** confirm the hook runs on the pinned action | Open; check the 2026-11-11 run |
| **New:** two pairs of entries share a source URL | Open; user triage |
| **New:** cost per scan is rising ($1.60 on 10-18 to $6.09 on 11-10) | Open; cause not investigated |

## 7. Metrics delta

| Metric | HDAI-AIRADAR-003 | Now | Source |
|---|---|---|---|
| Scheduled runs delivered, since 10-17 | 21 of 23 | 22 of 25 | `gh run list --workflow radar-daily.yml` |
| Library entries | 457 | 465 | `ls library/entries \| wc -l` |
| Tests | 209 | 290 | `python3 -m unittest discover -s tests` |
| Scan turns, last seven delivered runs (median) | n/a | 127 | run logs, `num_turns` |
| Scan cost, highest single run | n/a | $6.09 (11-10) | run logs, `total_cost_usd` |
| Pending queue records | 22 | 22 | `python3 scripts/make_queue_triage.py` |
| Pending records within 15 characters of the cap | 9 | 10 | same |
| Red runs since 09-01 without a write-up | 4 | 0 | `ls docs/ops` |

## 8. Memory harvest delta

One project memory changed (status of the coverage and repair-loop plans). Its general content is in this handover as L12 to L15 and in the plan. Nothing generalisable remains only in memory.

## 9. Verification

- Rechecked: the 11-10 findings and tool counts, from the downloaded diagnostics artifact; turns, cost and duration for 29 runs, from `gh run view --log`; the library's identifier and URL clashes, by script over all 465 entries.
- Replayed: the effort alarm over the 24 scheduled scans 10-18 → 11-10 raises nothing; the queue normaliser over 22 delivered commits restores nothing.
- Not verified: that the pinned action executes hooks from the settings file; the repair-scope and repair-outcome paths on a real run; the reminder workflow's issue step (it runs first on Monday 2026-11-16, or by manual dispatch).
- Not recoverable: the rules behind the 09-10, 09-11 and 09-12 aborts.
