# 2026-10-30: the repair pass delegated its fix and ended without editing

Scheduled run 41044727227 (`radar-daily`, 2026-10-30, base `6317dc7`). It failed at **"Enforce run outcome (fail on incomplete)"** with `ABORT RUN_INCOMPLETE - outcome validation`. That step only reports the outcome; the run failed earlier, at revalidation after the repair pass. Status: **cause established from the run log and diagnostics artifact; no fix applied; no recovery run.**

## What happened

| Step | Result | Evidence |
|---|---|---|
| Radar run (attempt 1) | success: 112 turns, 1,056 s, $3.99, model `claude-sonnet-5` | log, result block |
| Validate (attempt 1) | `verdict=repairable`, 2 violations | log; `violations-1.txt` |
| Repair pass (one allowed) | success: 16 turns, 50 s, $0.38, **0 edits** | log, result block; `model-run-facts.json` |
| Revalidate (final) | `verdict=abort`, `failure_class=validation`, the same 2 violations | log; `violations-1b.txt` |
| Deliver | skipped, so no commit and no report for 2026-10-30 | job summary: `commit \| none` |

The two violations, identical before and after the repair (from the diagnostics artifact):

```
REPAIRABLE QUEUE_RECORD_REWRITTEN reviews/deferred_candidates/social_science.md:155 - justification text must grow, never be rephrased (action_needed)
REPAIRABLE QUEUE_TEXT_TOO_LONG reviews/deferred_candidates/social_science.md:290 - free-text field action_needed exceeds the metadata-only length bound
```

- Line 155 is the existing pending record for `nber.org/papers/w35621`. Its `action_needed` was 207 characters at the base. Attempt 1 rephrased the text instead of appending to it.
- Line 290 lies past the end of the base file (288 lines), so it is a **new** record whose `action_needed` exceeded 240 characters.

Both violations could be repaired. Restoring the original text and appending fixes line 155. Shortening fixes line 290, because a new record has no grow-only history. This was not the grow-only/length-cap deadlock (P9).

## Root cause

**The repair pass did no repair.** Its tool calls (`model-run-facts.json`) were `Agent` ×2, `ScheduleWakeup` ×3, `ListAgents` ×2, `ToolSearch` ×3, `Read` ×7, `Grep` ×6, `Glob` ×1, and **no `Edit`**. Its final message was:

> Both agents are still running; waiting for completion notifications.

The repair agent handed the fix to two background subagents and then ended its turn to wait for them. In a non-interactive action run, the end of the turn ends the session, so the subagents' work never reached the workspace. Revalidation then found the same two violations. Under the bounded-repair rule (P11, one pass), a validation abort ends the run; attempt 2 runs only after a push race or a degenerate attempt 1.

**Why the agent could do this:** `scripts/build_claude_settings.py` lists allowed and denied tools, but denies only `Bash`, `PowerShell` and the `.git/` and runner-temp paths. `Agent`, `ScheduleWakeup` and `ListAgents` are neither allowed nor denied, and they executed. The repair prompt ("fix only those findings. Change nothing else.") does not say the work must be finished within the session.

**Contributing:** attempt 1 rephrased an existing queue record (line 155). The engine's deferral procedure already forbids this ("never rephrase, shorten, or rewrite it", `engine/ENGINE.md`, Deferral procedure), so this is a model-adherence miss against a written rule.

## Impact

- No 2026-10-30 report in either domain. Attempt 1's 14 accepted entries and 6 report items (3 per domain) were discarded with the workspace. Their identities cannot be recovered from the diagnostics, which by design carry derived facts only (R43).
- $4.37 of model spend produced no delivery.
- The run summary's coverage rows read `0 of 19` / `0 of 17` attempted. That is wrong: see the coverage-sensor defect in `docs/ops/2026-11-05-queue-deadlock-recurrence-incident.md`.
- The next scheduled run (2026-10-31, `8b76d1e`) delivered 16 entries. Whether it recovered any of the 14 is unknown.

## Proposed fixes (not applied; protected paths need the user's approval)

1. **Deny delegation and scheduling tools in unattended runs.** Add `Agent`, `ScheduleWakeup`, `ListAgents` and `SendMessage` to the deny list in `scripts/build_claude_settings.py`, with a test in `tests/validators/` asserting they are denied. An unattended run must do its work in its own session.
2. **Tell the repair prompt what "done" means.** Say that the session ends when the agent stops, so every edit must be made directly before stopping.
3. **Make the repair sensor say why it failed.** If a repair pass makes no edits and the violations do not change, record that as its own failure class in the run summary (for example `repair_no_op`), separate from "the repair made things worse".

## Lessons

- In a non-interactive harness, any tool that defers work past the end of the turn (background subagents, wake-ups) silently drops that work. Deny such tools by default; do not leave them merely unallowed.
- A repair pass needs its own sensor. "Repair ran successfully" (the step's outcome) and "repair changed anything" are different facts, and only the second matters.

## Update 2026-11-09: fixes 1 and 2 applied

Plan `docs/plans/2026-11-09-001-harden-repair-loop-plan.md`, Phase 1, approved by the user:
- **U1:** the deferral tools are denied by bare name (`DEFERRAL_TOOLS` in `scripts/build_claude_settings.py`). The repair prompt says the session ends when the agent stops and forbids handing work off.
- **U3:** the rephrased existing record (line 155) is now restored by the harness before validation. Only the new over-cap record (line 290) would have reached the repair pass.

Fix 3 (repair outcome classes) is Phase 2, U6. This incident also repeats the 2026-09-01 failure (run 33492847557), where the scan delegated to a background agent despite a prompt rule. That is why U1 is a deny rule and not another instruction.
