# v2 rollout runbook — unattended daily radar

Graduated activation of `.github/workflows/radar-daily.yml` (plan U9). Each
stage exists to disprove one class of failure while the blast radius is still
controlled; no stage is marked passed by assertion — every pass records a run
URL, command output, or test reference. The activation gate in
`docs/ops/2026-07-23-v2-feasibility.md` binds throughout: **stages 3+ that
involve any model credential, model-dependent Actions run, or the schedule
wait for the user's explicit activation approval and resolution of Q1–Q4.**

## Accepted risks in force (user-acknowledged 2026-07-23)

- **S2** — unattended runs draw on the personal Claude subscription; CI
  rate/quota behaviour is observed live at stage 7 before daily activation.
- **S3** — `CLAUDE_CODE_OAUTH_TOKEN`, once created, is a one-year bearer
  credential in a GitHub Actions secret; renewal reminder required at
  activation (~11 months).
- **S4** — `main` has no platform branch protection (free-plan private repo);
  the deterministic validators, restricted credentials, and ff-only delivery
  are the principal controls.

Operational notes: GitHub keeps at most **one pending run** per concurrency
group (a newer queued dispatch replaces an older queued one; a running job is
never cancelled). Scheduled-run notifications route to the workflow's
creator/last-modifier — verify delivery at stage 7. A missing daily
notification is itself the failure signal; the R40 lookback self-heals missed
days.

## Stages

| # | Stage | Status | Evidence |
|---|---|---|---|
| 1 | Local validator suite green, including the adversarial drills | **passed 2026-07-23** | `python3 -m unittest discover -s tests` → 136 tests OK. Drills: tampered workspace validator + delivery script provably inert (`test_run_delivery.TestValidate.test_tampered_workspace_scripts_are_inert_and_flagged`); history-protection deletion/rewrite fixtures (`test_check_changed_paths.TestHistoryProtection`, `TestQueueProtection`); no-echo proofs incl. poisoned filenames and summary (`TestNoEcho*`, `test_make_run_summary`); missing-evidence → TOOLING (`test_run_delivery.TestValidate.test_missing_evidence_is_tooling_abort_even_with_empty_diff`); race → rejected → push-failed (`test_run_delivery.TestDeliver`); auth-boundary and credential-scope structure (`test_workflow_structure`) |
| 2 | Local dry run — user executes the run prompt in an interactive session against a scratch branch; validators pass on its output | pending (user-triggered; no credentials needed) | — |
| 3 | `workflow_dispatch` **dry-run** on GitHub (stub, no model, no push, no secret) | **passed 2026-07-23** | Run 30014685714 (github.com/harryaquijeballon/ai_radar/actions/runs/30014685714): completed/success. Repo unchanged at `7750a6b`; OAuth readiness boolean true; no `ANTHROPIC_API_KEY` present; credential-free checkout, read-only pristine harness, 44-domain egress settings generated, full validator suite `verdict=pass`. No model step, delivery, push, or artifact upload occurred |
| 4 | Dispatch **no-push**, then **full** — first real cloud commit | **passed 2026-07-23** (4a and 4b user-accepted) | **First 4a attempts, 2026-07-23:** runs 30015121255 and 30015373481 failed pre-model (missing `id-token: write`, then the Claude GitHub App not installed — both fixed; app installed repo-scoped by the user). **Run 30016278453: qualified result** — handshake, OAuth (claude-sonnet-5, 29 turns), pristine-base validation all worked and the validators correctly caught 1 tooling-class violation (`verdict=abort`), but the job stayed green in no-push mode and `if: failure()` diagnostics never uploaded. Fixed by the outcome gate + incomplete-diagnostics + summary-tee change. **4a repeat, run 30017400376: accepted success 2026-07-23** — claude-sonnet-5, 96 turns, 11m24s; `verdict=pass`, 0 violations; 2 candidates deferred (egress + verification classes) exactly per design; no repair, no attempt 2, repo untouched. Per-domain scan-evidence counts added to the safe summary (fail-closed, integers only) before 4b. **4b, run 30018799754: accepted full success 2026-07-23** (github.com/harryaquijeballon/ai_radar/actions/runs/30018799754) — App + OAuth auth passed (claude-sonnet-5, 83 turns, 16m36s); scans 4q/17f (social_science) and 4q/20f (ai_engineering); 6 accepted entries, 0 provisional, 4 deferred (`access_or_license_unclear`), 0 rejected; ai_engineering report 3 items, social_science honest quiet day; repair path executed once then full-suite revalidation passed; atomic generated-content commit `d8569d2` pushed; all four validators re-run locally against the pushed state → clean; no security, history, credential, egress, or protected-path violation. Egress finding: `WebFetch(domain:…)` is exact-host — `www.nber.org` and `blog.cosmos-institute.org` added to the allowlist by user approval (no wildcards); `sciencedirect.com` 403 confirmed as an external site response, no change made. **Observation for stage 6:** the official action rewrites the model workspace's git remote with its GitHub App token ("Updated remote URL with authentication token"); protections confirmed in force — Bash/PowerShell denied (no shell git), `.git/**` denied to file tools, delivery credential separate, no-push cannot deliver. No documented action input disables this; do not redesign — probe at stage 6 |
| 5 | Concurrency + remote-advance drills | **passed 2026-07-23** | Concurrency (runs 30020745839/30020756594, dry-run pair 8s apart): second run queued while first executed (created 15:29:09 inside run 1's job window :05-:14; its job started :16, after completion), nothing cancelled, both green. Remote advance (drill B retry, run 30022444070): attempt-1 delivery **rejected** on human marker `efc7084`; workspace and its local commit `0c865bc` discarded; fresh re-checkout + pristine re-materialization from the new head; one model rerun; second human marker `532c2d3` pushed during attempt 2; **safe abort** with attempts=2 - no merge/rebase/force-push/stash, both markers intact in linear history, no generated content delivered after the second advance. The specific deliver2-rejected `push` outcome is certified by composition: live deliver-rejection (attempt 1) + live final-mode escalation (attempt 2) + the local push-failed test. Earlier drill runs 30020895058 (paraphrase abort, led to the repairable/QUEUE_HISTORY_REWRITTEN split) and 30022109296 (6-turn model bail, caught live by EVIDENCE_MISSING) stand as genuine negative-path evidence |
| 6 | Live security and permission probes | **passed 2026-07-23** | Four in-run probes, both attempts of run 30022444070, recorded in the diagnostics evidence artifacts: `read_git_config: denied`, `shell: denied`, `runner_temp_read: denied`, `off_allowlist_fetch: denied` - the model cannot read `.git/**` (incl. the action-injected app-token remote), run shell/git, reach runner control files, or fetch off-allowlist. Delivery credential isolated to delivery steps (structural tests + live env). Planted-fixture drills (protected-path edit, deletion, body rewrite, missing evidence) certified by the local suite plus live negatives: protected paths and history live-enforced at drill A / 4b validators, missing-evidence live at run 30022109296. Revoked-token AUTH rehearsal deliberately deferred to first token rotation (destructive to the live credential). Note: bounded-scan drill *guidance* drifted at attempt 2 (full-breadth scan) - soft instructions are probabilistic, hard rules held: the design thesis demonstrated |
| 7 | Notifications, summaries, diagnostics, usage | **passed 2026-07-23** (one user check open) | Success vs failure distinguishable (4b green with content; three drills red via the outcome gate). Safe summary in job summary + plain log + artifact on every run since `f34111b`. Diagnostics artifacts on all three incomplete runs (evidence, violations, summary - no content, no secrets). Usage: normal full run 80-100 turns, ~$3.4-4.6 nominal subscription metering, 11-17 Actions minutes; estimate ~15 min/day, ~450 min/month (within the 2,000-min free tier); Actions $0 budget + stop-usage are external account settings this repo cannot alter. Supervised near-time cron fires and inbox-delivery confirmation remain folded into stage 8 activation (first scheduled fires ARE the supervised fires). Notification delivery **confirmed by the user 2026-07-23 for both completed and intentionally failed runs** |
| 8 | Activate the real schedule | **activated 2026-07-23 by explicit user approval** | Full certification (stages 1, 3-7) accepted by the user; schedule block enabled at exactly `cron: "7 10 * * *"` / `timezone: "Europe/London"` in the activation commit; no other trigger, permission, model, egress, validation, or delivery behaviour changed. First scheduled fire expected 2026-07-24 10:07 Europe/London (09:07 UTC, BST) |
| 9 | Pilot — 2-4 weeks of every-run notifications, then record the R38 decision (keep or failure-only) and the R45 decision (keep `full` dispatch mode or restrict) here | **review held 2026-09-01; decisions recorded (user-approved)** | Full evaluation: `docs/ops/2026-09-01-pilot-evaluation.md`. Verifiable window 2026-08-13 → 2026-09-01: 16/20 scheduled fires green; 4 failures (all loud, none silent, zero corruption); 09-01 recovered same day via `workflow_dispatch mode=full`. **R38: failure-only notifications** (user setting: GitHub → Settings → Notifications → Actions → "Only notify for failed workflows"). **R45: `full` dispatch mode kept** — it is the recovery path (used 2026-07-27 and 2026-09-01), user-triggered, and inherits every scheduled-path guardrail. Token renewal: due ~2027-06 per activation step 3's calendar reminder; regenerate via `claude setup-token`, update the Actions secret. Open item: the U10 manual acceptance trace (user picks one pilot day; report → entry → source, summary → commit) |

## Exact activation steps (in order, all user-gated)

1. Resolve Q1–Q3 (employer policy, credential policy, subscription eligibility)
   and Q4 (documented revocation path) in
   `docs/ops/2026-07-23-v2-feasibility.md`.
2. Refresh the GitHub credential with `workflow` scope if not already done:
   `gh auth refresh -h github.com -s workflow`.
3. Run `claude setup-token` locally; paste the printed token into a new
   repository secret named `CLAUDE_CODE_OAUTH_TOKEN`
   (Settings → Secrets and variables → Actions). Never store it anywhere else.
   Set a calendar reminder ~11 months out to regenerate it.
4. Execute stages 3–7 in order, recording evidence above.
5. Uncomment the schedule block (stage 8), commit, push.
6. Set the stage-9 pilot review date (+2–4 weeks).

## Rollback and disable

| Situation | Action |
|---|---|
| Pause the schedule quickly | Actions tab → radar-daily → "…" → Disable workflow, or `gh workflow disable radar-daily.yml` |
| Remove the schedule durably | Re-comment the `schedule:` block, commit, push |
| Suspected token compromise | Delete the `CLAUDE_CODE_OAUTH_TOKEN` repo secret immediately; regenerate via `claude setup-token` only when ready to resume; follow the Q4-documented revocation path for the old token |
| Bad content pushed by a run | Never rewrite `main`: revert commits (`git revert <sha>`), or correct via the normal append-only conventions; every run is one atomic commit, so reverts are clean |
| Validators aborting every run | The library is untouched by design (fail closed); disable the schedule, fix under tests locally, re-run stages 3–4 before re-enabling |

## Standing rule

The workflow is **not activated** until stage 8 is explicitly approved by the
user. Nothing in this runbook overrides the activation gate.
