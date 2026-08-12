# 2026-07-28 — Model-bail reliability review and remediation

Third consecutive scheduled-run failure (run 30338099335). User-commissioned
focused review before any further change; user approved the remediation below
on 2026-07-28. Companion to `docs/ops/2026-07-27-scheduled-delivery-incident.md`
(which stands unmodified; one correction to its chronology is recorded here).

## Verified chronology of all scheduled runs since activation

| Date | Run | Fired (UTC) | Model activity | Cause class |
|---|---|---|---|---|
| 2026-07-24 | 30088493851 | 11:07 | 1 turn, $0, `is_error: true` | A — subscription usage limit (user-confirmed) |
| 2026-07-25 | 30154883225 | 10:40 | 43 turns, $1.50, 0 permission denials, no evidence | C — model bail |
| 2026-07-26 | 30198956789 | 10:49 | full scan: 134 turns + 30-turn repair | B — empty-`inputs` delivery gate (fixed 2026-07-27) |
| 2026-07-27 | 30266494641 | 12:34 | **full scan: 133 turns + 24-turn repair** | B — same gate bug (ran pre-fix) |
| 2026-07-28 | 30338099335 | 07:21 | 33 turns, $0.70, 0 permission denials, no evidence | C — model bail |

Chronology correction: the 2026-07-27 scheduled run was previously assumed
"same skip expected"; log verification shows it performed a complete
133-turn scan whose delivery the (since-fixed) gate discarded — class B, not
merely presumed. Classes A and B are closed. Class C is the subject here.

## Parity finding: schedule and dispatch present identical model inputs

Line-level diff of the claude-code-action invocation in bail run 30338099335
(schedule) versus successful recovery run 30267841509 (dispatch), plus source
review of `anthropics/claude-code-action` v1 (`src/modes/agent/index.ts`):

- Agent mode writes the workflow `prompt` input **verbatim** to the prompt
  file — no event context, no wrapper. Both events auto-detect mode `agent`.
- All 26 action inputs, the generated settings, SDK options, model
  (claude-sonnet-5), env (except `GITHUB_RUN_ID`/`GITHUB_EVENT_NAME`),
  workspace, and evidence path are identical.
- With Bash denied, the model cannot read `GITHUB_EVENT_NAME`: **no channel
  exists by which trigger type reaches the model.** The schedule-only failure
  pattern is not statistically significant at these sample sizes (2/4
  completed scheduled model runs vs 0/3 dispatched content runs; the Jul 23
  drill bail 30022109296 shows dispatch bails are possible).

## Root cause (class C)

Stochastic early turn-termination at the reading→execution boundary,
enabled by a prompt-contract gap. Signature (both occurrences): ~30–43
turns, clean `success` termination, **zero fetch attempts** (0 permission
denials vs 2–28 on real scans), no writes, no evidence artifact. The prompt
defined a task sequence but no terminal condition: nothing prohibited ending
the turn after the reading milestone, which is exactly where both bails sit.
Validators contained every failure; the library was never touched.

## Remediation (approved 2026-07-28)

1. **Completion-contract prompt** (`.github/prompts/daily-radar.md`):
   explicit "no one will ever reply / a tool-less response ends the run"
   framing, three-condition success definition up front, mandatory
   verify-before-ending step, redundant `CLAUDE.md` read dropped (auto-loaded
   project context), "begin the scan immediately" transition. Safety, egress,
   deferral, and path rules unchanged. Pinned by
   `test_workflow_structure.TestRuntimePrompt`.
2. **Bounded retry for the exact degenerate signature**: `validate` now
   emits `degenerate=true` iff the sole violation is `ABORT
   EVIDENCE_MISSING` (and no internal error). All five attempt-2 steps also
   fire on `degenerate == 'true' && model1.outcome == 'success'` — step
   outputs only, never `inputs.*` (2026-07-27 lesson). Excluded by
   construction: auth/usage failures (model step failure skips validate),
   credential/App failures (job fails earlier), any other violation
   (violation count > 1), malformed evidence (`EVIDENCE_MALFORMED` token),
   config errors (fail before the model step). Attempt 2 remains statically
   unrolled and final: a second bail fails the run as `tooling` (new
   `--deliver2-class` plumbing labels it correctly).
3. **Safe observability** (`scripts/summarize_execution_log.py`): derived
   `model-run-facts.json` in the diagnostics artifact (termination facts,
   tool-name counts, WebSearch/WebFetch counts, evidence/report write
   booleans, truncated final assistant message). The raw execution log
   contains tool results and fetched content and is **never** uploaded.
   Attempt 1's facts are snapshotted before a retry resets the workspace.

Explicitly rejected in review: raw transcript upload (content exposure),
schedule move or temporary disable (no evidence fire time contributes;
failures are contained and informative), model/action config changes (same
model completed five full scans). Scheduler delay (2h44m on 2026-07-28,
landing 08:21 London) is tracked as a separate operational condition.

## Verification

- Deterministic: full suite (`python3 -m unittest discover -s tests`),
  including new degenerate/classification/parser/prompt-contract tests.
- Live: one `workflow_dispatch mode=full` certification (valid for the new
  gates — they are step-output driven, unlike the 2026-07-26 bug), then the
  next scheduled fires. A future bail day should show `attempts: 2`, outcome
  `success`, and a populated `model-run-facts.json` naming the model's final
  message. Residual risk: retry squares, not eliminates, the bail
  probability; the facts record exists to cure the root cause if it persists.
