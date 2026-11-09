---
handover_id: HDAI-AIRADAR-003
date: 2026-11-09
project: ai_radar
type: delta
previous_handover: HDAI-AIRADAR-002
repo_head_at_writing: main @ 08076e3 (this handover lands in the next commit, together with the two incident records it cites)
covers: 9fe3e09 .. 08076e3
visibility: public
visibility_note: >-
  Written from the public repository, public GitHub Actions run logs and
  diagnostics artifacts of runs 2026-10-16 → 2026-11-08, and two local
  agent-memory files (section 8). No internal, client or employer material
  was used.
topics:
  - repair-pass failure modes
  - tools that defer work past a non-interactive session
  - instruction-only fixes for structural deadlocks
  - testing what a sensor actually reads
  - eligibility by dedup instead of date (first results)
  - effort and cost trend after pinning
---

# HDAI-AIRADAR-003: delta handover, 2026-10-16 → 2026-11-09

Weekly delta, written late: it covers three weeks, from the HDAI-AIRADAR-002 commit `9fe3e09` to `main` @ `08076e3`. Today's scheduled run (2026-11-09) was still in progress at writing and is not counted. Tags as in the baseline: **[implemented]**, **[intended]**, **[measured]**, **[interpretation]**.

## 0. Summary

1. [measured] The model pin held. 21 of 23 scheduled runs (10-17 → 11-08) delivered, all on `claude-sonnet-5` and CLI v2.1.301, adding 142 entries (315 → 457). The hollow-scan failure of HDAI-AIRADAR-002 has not recurred.
2. [measured] The two red runs, 10-30 and 11-05, both failed at revalidation after the single repair pass. 10-30: **the repair pass delegated its fix to background subagents and ended without an edit.** 11-05: **the queue grow-only/length-cap deadlock (P9) recurred for the fourth time**, because the repair trimmed two queue fields that were already at the cap.
3. [measured] The new U12 coverage sensor reports 0 coverage on every run that needs a repair, because the repair transcript overwrites the scan transcript at a shared path (6 of 13 runs since U12). Its floors cannot be enforced until this is fixed.
4. [implemented] U12 (coverage sensor, report-only), U13/U14 (search window separated from eligibility) and an allowlist fix for eight `www.` hosts landed on 10-26. [interpretation] Entries per scheduled run rose from 2.8 to 8.8 and rejections fell from 52 to 9 across the two periods; the changes landed together, so their effects are not separated.
5. [measured] Effort and cost per run rose after 10-26: mean $2.43 → $3.91, median turns 89.5 → 118.
6. [intended] Proposed fixes, none applied: deny delegation and scheduling tools in unattended runs; a structural P9 fix; preserve attempt 1's transcript before the repair; keep verification judgments out of the repair pass.

## 1. What changed

**Discovery-coverage plan (`docs/plans/2026-10-16-001-fix-discovery-coverage-plan.md`)**
- `2168f2b` (10-26): U12. `scripts/validators/check_scan_coverage.py` matches the scan's actual `WebFetch` calls against a new `fetch hosts` column in `profiles/<domain>/sources.md`. Report-only until per-domain floors are set.
- `2b17678` (10-26): U13/U14. Engine P6.1 separates *where* a run searches (window) from *whether* a find is new (dedup plus a 7-day visibility cap; the arXiv listing date counts). No date-only rejections.
- `f3fbf68` (10-26): eight `www.`/`www2.` hosts added to the egress allowlist and watchlists. The supervised U12 check run (40345891512) had been denied on each.
- `1b1bd69` (10-28): U15 list, `inbox/2026-10-26-window-rereview.md`: 210 arXiv papers rejected in August–September only for their date. Processing deferred by the user.

**Daily runs**
- 21 run commits from `fe0fb05` (10-17) to `08076e3` (11-08). None for 10-30 or 11-05.

**Incident records (this commit)**
- `docs/ops/2026-10-30-repair-pass-stall-incident.md`
- `docs/ops/2026-11-05-queue-deadlock-recurrence-incident.md`

## 2. New or changed lessons

**L8 (new). Deny, rather than just not allow, every tool that defers work past the session.**
- *Rule:* in a non-interactive harness, the end of the agent's turn is the end of the run. Background subagents, wake-ups and message passing must be denied, not merely left out of the allow list.
- *Why:* the 10-30 repair pass called `Agent` ×2 and `ScheduleWakeup` ×3, made no edit, and ended with "Both agents are still running; waiting for completion notifications." Revalidation found the same two violations, and the day was lost (`docs/ops/2026-10-30-repair-pass-stall-incident.md`) [measured]. `scripts/build_claude_settings.py` denies only `Bash`, `PowerShell` and two path scopes [measured].
- *How to apply:* add `Agent`, `ScheduleWakeup`, `ListAgents` and `SendMessage` to the deny list [intended].
- *How to check:* a test asserts the deny list; no run's `model-run-facts.json` shows those tools.

**L9 (revalidates P9). An instruction-only fix for a structural deadlock fails at the model's adherence rate.**
- *Rule:* unchanged from P9: never combine a grow-only rule with a length cap.
- *Why:* the fourth recurrence (after 08-05, 08-07 and 09-27) came on 11-05. Attempt 1 appended to fields at 233 and 240 characters despite the engine's "date-only bump" instruction, and the repair trimmed them [measured]. The exposure is growing: 9 pending `action_needed` fields are now within 15 characters of the cap [measured, `lib_queues.parse_queue_file` over both queues at `08076e3`].
- *How to apply:* move re-encounter notes out of the capped field, or make the violation message name the only safe repair: restore the base text and bump `last_encountered` [intended].
- *How to check:* a fixture with a field at the cap plus an over-cap append, when passed through the repair instruction, ends in a pass.

**L10 (revises P11). A bounded repair also needs a scope and its own sensor.**
- *Rule:* the repair pass may fix form, never make evidence judgments; and "repair step succeeded" must be distinguished from "repair changed anything" and from "repair made things worse".
- *Why:* across 23 scheduled runs there were 9 repair passes; 7 ended in a pass [measured, `verdict=` lines in run logs]. Of the 2 failures, one changed nothing (10-30) and one created new violations (11-05). On 11-05 the repair also set `verification: partial` on 15 entries with zero web fetches, which is a verification decision made without evidence [measured, `model-run-facts.json`].
- *How to apply:* exclude `verification` and `status` from repairable edits, and route a missing `verification` field to `provisional` or abort; record `repair_no_op` and `repair_regressed` as distinct outcomes in the run summary [intended].
- *How to check:* the run summary reports the repair outcome class; the P11 metric (repair pass rate) is computed from it.

**L11 (new). Test what a sensor reads, not the name of its input.**
- *Rule:* when a sensor consumes an artifact, test the artifact's contents on every path, including retries and repairs.
- *Why:* the workflow correctly passes attempt 1's `execution_file` output to the coverage sensor, and a structure test asserts this. But the action writes every invocation to `/home/runner/work/_temp/claude-execution-output.json`, so after a repair pass the sensor reads the repair transcript. 6 of 13 scheduled runs since U12 report 0/19 and 0/17; the other 7 report 16–17/19 and 7–17/17 [measured].
- *How to apply:* copy attempt 1's transcript to `$RADAR_DIR` immediately after the model step, and point the sensor at the copy [intended].
- *How to check:* the coverage figures of a run with a repair are within the range of runs without one.

**L6 (status update, from HDAI-AIRADAR-002). Eligibility by dedup: first results.**
- [implemented] `2b17678`. [measured] Scheduled runs 10-17 → 10-26 (10 runs) added 28 entries and logged 52 rejections. Runs 10-27 → 11-08 (13 runs, 11 delivered) added 114 entries and logged 9 rejections. [interpretation] This is consistent with fewer date-only rejections. The change is confounded with `f3fbf68` (eight more fetchable hosts), and run-to-run variation is large (1–18 entries per run).

## 3. Incidents

| Run | Outcome | What happened | Write-up |
|---|---|---|---|
| 41044727227 (scheduled, 10-30) | red, `validation` | Repair pass delegated to background subagents, made no edit; same 2 queue violations at revalidation | `docs/ops/2026-10-30-repair-pass-stall-incident.md` |
| 42029203188 (scheduled, 11-05) | red, `validation` | 23 violations (15 entries without `verification`, 6 ineligible report items, 2 over-cap queue fields); repair fixed 21 but trimmed the 2 queue fields, so P9 deadlock abort | `docs/ops/2026-11-05-queue-deadlock-recurrence-incident.md` |
| 39018527044 (scheduled, 10-17) | green after retry | Attempt 1 ended after 3 turns ($0.16) and was classified `abort`; attempt 2 delivered 10 entries | none; not red. First run on the pin |
| 6 scheduled runs with a repair pass since 10-26 | green or red | Coverage sensor read the repair transcript (L11) | in the 11-05 record |

No recovery dispatch was run for 10-30 or 11-05; neither day has a report.

## 4. Loop changes

- **Feedforward:** engine P6.1 rewritten (`2b17678`); run prompt points at it and states the ban on date-only rejections [implemented]. Watchlists gained a `fetch hosts` column (`2168f2b`) [implemented].
- **Fast sensor (in-run):** none new.
- **Harness sensors:** coverage measured from the transcript, not from the agent's self-report (`2168f2b`) [implemented, report-only]. It is defective on repaired runs (L11) [measured]; floors are not set [intended].
- **Repair loop:** two new failure modes measured: no-op (L8) and an evidence judgment made by the repair (L10).
- **Outer loop:** both red runs have a write-up within this handover's window [implemented]. The four older red runs (09-10, 09-11, 09-12, 09-27) still have none. No human queue resolution since 2026-08-12 [measured: 35 records, 22 pending].
- **Loop metrics:** turns, cost and coverage per run measured from logs for 23 scheduled runs (§7) [measured]; not yet in the run summary or alarmed [intended, U16].

## 5. Decisions

| Date | Decision | Reason | Record |
|---|---|---|---|
| 2026-10-26 | U12 report-only; set floors after ~7 runs of real coverage data | No historical execution logs to calibrate on | `2168f2b` |
| 2026-10-26 | Adopt U13/U14 (window vs eligibility) | 243 date-only rejections, 157 self-scored high | `2b17678` |
| 2026-10-26 | Allowlist eight `www.`/`www2.` hosts; keep the bare hosts | Exact-host matching; bare domains redirect there | `f3fbf68`; `profiles/egress_allowlist.md` |
| 2026-10-28 | Generate the U15 re-review list; defer processing, no date set | User's choice | `1b1bd69` |
| 2026-11-09 | Write up both red runs and this handover; fixes proposed, not applied | Protected paths; fixes need user approval per unit | this commit |

## 6. Open items

| Item | Status change |
|---|---|
| First pinned scheduled run (10-17): verify depth and delivery | **Closed:** delivered 10 entries on attempt 2 |
| `REJECTIONS_NOT_APPEND_ONLY` in the A/B run, cause unknown | Not recurred in 23 scheduled runs; cause still unknown; harness-side rejection appends not built |
| Plan U12 | Built, report-only (`2168f2b`). Floors not set. **Now blocked** on the transcript-overwrite defect (L11) |
| Plan U13/U14 | **Closed:** done (`2b17678`) |
| Plan U15 | Paused at the list checkpoint (`1b1bd69`); the user deferred processing |
| Plan U16 (metrics, handover) | Partly done by this handover (§7); run-summary metrics and alarms not built |
| Measure model cost per run | Measured for 23 runs (§7); still not in the run summary |
| Write-ups for 09-10, 09-11, 09-12, 09-27 failures | Unchanged, open |
| Queue triage | Worse: 32 records / 19 pending → 35 / 22 |
| Structural P9 fix | Open since HDAI-AIRADAR-001; **recurred 11-05** |
| Why `claude-sonnet-5-5` stops early | Unchanged, open |
| Vendor-lab watchlist review; Economics team publications (~11 items) | Not worked in this range |
| **New:** deny delegation/scheduling tools in unattended runs (L8) | Open, proposed |
| **New:** keep `verification` out of the repair pass (L10) | Open, proposed |
| **New:** no recovery runs or reports for 10-30 and 11-05 | Open; decide whether a catch-up scan is wanted |
| **New:** `runs-on: ubuntu-latest` is an unpinned input (L1) | Open, no incident: runs moved to `ubuntu-26.04` by 10-27 without effect [measured, runner image lines in logs] |

## 7. Metrics delta

| Metric | Before (9fe3e09) → after (08076e3) | Source |
|---|---|---|
| Library entries | 315 → 457 (all 142 from daily runs) | `ls library/entries/*.md \| wc -l`; `git log --diff-filter=A 9fe3e09..HEAD -- library/entries/` |
| Verification | 187 verified / 128 partial → 300 / 155 / 2 unverified | `grep -h '^verification:' library/entries/*.md \| sort \| uniq -c` |
| Rejection-log rows | 291 → 352 (52 dated 10-17 → 10-26, 9 dated 10-27 →) | `grep -c '^\| 20' library/rejections.md`; awk on the date column |
| Scheduled runs green | 21 / 23 (10-17 → 11-08) | `gh run list --workflow radar-daily.yml` |
| Repair passes ending in a pass | 7 / 9 | `verdict=` lines, `gh run view <id> --log` |
| Entries per scheduled run, 10-17 → 10-26 vs 10-27 → 11-08 | 2.8 → 8.8 | entry-add counts per run commit |
| Mean cost per scheduled run (scan + repair) | $2.43 (10 runs) → $3.91 (13 runs); max $5.43 (11-04) | `total_cost_usd` in run logs |
| Median turns per scan attempt | 89.5 → 118 (range 75–108 → 97–173) | `num_turns` in run logs |
| Spend on the two red runs | $9.04, no delivery | run logs |
| Curated coverage, runs without repair (SS / AE) | not measured → 16–17 of 19 / 7–17 of 17 (7 runs) | `curated coverage` rows in run summaries |
| Coverage readings invalid (repair overwrote the transcript) | 6 of 13 scheduled runs since 10-27 | same |
| Pending queue fields within 15 chars of the 240 cap | not measured → 9 | `lib_queues.parse_queue_file` over both deferred queues |
| Deferred queue | 32 records / 19 pending → 35 / 22 | `lib_queues.parse_queue_file` |
| Validator tests | 180 → 209 | `python3 -m unittest discover -s tests` |
| Egress allowlist | 58 → 66 domains | `scripts/build_claude_settings.py` output at each revision |
| Library consistency | pass → pass | `python3 scripts/validators/check_library_consistency.py` (exit 0) |

## 8. Memory harvest delta

| File | Lesson that generalises | In a versioned file? |
|---|---|---|
| `proceed-once-approved.md` (new, feedback) | Once the user approves the next unit, start it; stop only at its review checkpoint | **No**: a working-style preference; `CLAUDE.md` holds only the checkpoint half |
| `discovery-coverage-fix-status.md` (changed) | Coverage calibration: the `succeeded` figure is soft (a redirect is not an error), so `attempted` is the metric; calibrate only on runs under one prompt version | **Partly**: `f3fbf68` records the redirect cause; the calibration rule is only in memory |
| same | Check the run log before planning on top of a sensor's output | **Yes**, now: L11 and the 11-05 record |

## 9. Verification

**Rechecked:** every count in §0 and §7 with the cited commands on 2026-11-09. Run outcomes, verdicts, turns, costs and coverage rows were read from `gh run view <id> --log` for all 28 completed runs since 2026-10-16 (23 scheduled). The violations and repair tool calls come from the two failed runs' downloaded diagnostics artifacts. The base lengths of the two deadlocked fields were measured at `1d9d25f`. The shared transcript path appears twice in run 41044727227's log ("Log saved to …" after attempt 1 and after the repair).

**Corrected while writing:**
- My first draft said the date-only bump needed a new validator rule. It does not: `last_encountered` is already the only unattended-mutable field. What is missing is a safe repair path.
- I first wrote that the missing `verification` field had not recurred. That cannot be shown, because diagnostics are uploaded only for incomplete runs.

**Could not verify:**
- The 14 entries discarded on 10-30. Diagnostics carry no content, by design (R43).
- Whether the 10-30 subagents edited anything before the session ended. Only the main agent's tool calls are summarised, and the unchanged violations show that nothing effective landed.
- Which of the 15 discarded 11-05 entries were archived later. A keyword check found at least 6, not matched item by item.
- Separate effects of U13/U14 and `f3fbf68` on the entry rate.
