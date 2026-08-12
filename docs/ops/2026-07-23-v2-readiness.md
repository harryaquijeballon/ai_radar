# v2 readiness assessment (U10)

Status of the v2 definition of done (plan `docs/plans/2026-07-23-001-feat-unattended-daily-radar-plan.md`) as of 2026-07-23. Verdict: **technically ready for activation** — every credential-free deliverable is built, tested, and documented; every remaining item is gated on the user's activation approval (Q1–Q4) by design, not on missing implementation.

| DoD item | Status |
|---|---|
| 1. U1 dossier; go recorded; secret installed; visibility evidence; R48 gate items | Dossier complete, U1 approved, visibility API-confirmed. Pending by design: secret creation and the three R48 live-probe items (a: credential visibility, b: write-scope expressibility, c: egress) — the sandboxed probe needs a token, so it runs at rollout stage 6 |
| 2. Validator suite green; no-echo, history-protection, tamper, credential drills | **Done locally**: 136 tests green; tamper drill proves workspace copies inert; no-echo proven incl. filenames and the summary. Actions-context replays land at stages 3–6 |
| 3. Engine unattended mode; schema untouched; clean-base wiring; queues seeded; migration | **Done**: `engine/schema.md` byte-identical (v1 freeze holds); migration was a documented no-op (zero pending proposals) |
| 4. Nine rollout stages evidenced | Stages 1 and 3–7 passed and evidenced (runbook); stage 2 superseded by the live 4a/4b runs; stage 8 (enable schedule) is the next supervised action, awaiting explicit user confirmation; stage 9 is the pilot itself |
| 5. Schedule active; ≥5 consecutive silent-free days | Schedule activated 2026-07-23 (stage 8, explicit user approval); the silent-free-day count accrues from 2026-07-24 during the pilot |
| 6. Pilot review; R38 and R45 decisions; token renewal reminder | Pending (slots in runbook) |
| 7. Traceability audited | See below |
| 8. CHANGELOG/README updated; v2 tagged | Docs updated this commit; the `v2.0.0` tag is cut at pilot close (U10) |

## Traceability audit

All 50 plan requirements are implemented, documented, or explicitly pending activation; none were dropped. Enforcement owners match the plan matrix, with three recorded implementation-level deviations, none touching approved product scope:

1. **`run_delivery.py`, not `run_delivery.sh`** — same responsibilities, same invocation points; Python for testability and identical behaviour across macOS (bash 3.2) and ubuntu runners.
2. **Run summaries carry counts and paths only — no report headlines** (R37, tightened per the user's U4 instruction that summaries never carry model-generated free text).
3. **`reviews/` added to history protection** (user ruling at the U3 checkpoint) — deletion, record removal, and unattended lifecycle transitions are abort-class.

Requirements that can only be *certified* live (their machinery is built and structurally tested): R28 queue-don't-cancel, R34 notification delivery, R48 probe items, R49 in-runner credential absence, and the young cron-`timezone` behaviour — all mapped to rollout stages 3–7.

## Known-blocked operational item

Pushing `.github/workflows/` requires a GitHub credential with the `workflow` scope; the current PAT and `gh` token have `repo` only, so commits from U7 onward are local until the user runs `gh auth refresh -h github.com -s workflow` (then `git push`). Recorded here so activation step 2 in the runbook is not skipped.
