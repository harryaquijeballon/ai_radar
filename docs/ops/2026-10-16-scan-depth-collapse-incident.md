# 2026-10-16 — Scan depth collapsed on 2026-09-29 behind a "success" signal

Unit U11 of `docs/plans/2026-10-16-001-fix-discovery-coverage-plan.md`. Status: **diagnosed; fix not yet applied** (pinning awaits user approval).

## What happened

From the 2026-09-29 run onward, every scheduled run finished in 1–2 minutes and was classified `success`, while checking 1–4 curated sources per domain (25 social science, 17 AI engineering active). The healthy runs before it checked 9–17 and 12–15 sources and took 8–19 minutes. Nothing in the repository changed between the two runs. The runs also stopped writing rejections and deferrals altogether.

## Evidence

From `gh run view <id> --log` (the model step's init and result blocks):

| | 2026-09-28 (run 36414063914, healthy) | 2026-09-29 (run 36558180331, first collapsed) | 2026-10-16 (run 38878997439) |
|---|---|---|---|
| `anthropics/claude-code-action@v1` resolved to | `756cc22e19660d20e8cc9496b4f242475a7f7790` | `8ce9314fa9a404564fa7e954cd84f25bcba2b829` | `374f254f5efaf968abfe15d399fd90972e8138b9` |
| Claude Code CLI | v2.1.283 | v2.1.284 | v2.1.301 |
| Model (workflow sets none) | `claude-sonnet-5` | `claude-sonnet-5-5` | `claude-sonnet-5-5` |
| Turns | 104 | 25 | 41 |
| Model step duration | 540 s | 41 s | 141 s |
| Cost | $2.93 | $0.35 | $0.54 |
| Curated sources (SS / AE) | 9 / 13 | 2 / 2 | 2 / 3 |

## Root cause

**Unpinned inputs moved underneath the run.** The workflow references the action by the floating tag `@v1` and sets no model, so the action version, the CLI version and the default model can all change without a commit. On 2026-09-29 all three changed at once.

**The model change is the leading cause.** The action and the CLI have since moved again (three action SHAs, CLI 2.1.284 → 2.1.301) while the collapse has persisted unchanged. The only factor that changed on 2026-09-29 and has held constant since is the default model: `claude-sonnet-5` → `claude-sonnet-5-5`. With the new model, the same run prompt completes in a quarter to two-fifths of the turns (25–41 vs 104). Why it stops early has not been examined: that needs the transcripts.

**Not yet proven.** This is a correlation across three runs, not an isolated test. The full transcripts are in the runs' execution-output artifacts, which were not downloaded. The confirming experiment is a single `workflow_dispatch` no-push run on today's action with the model pinned to `claude-sonnet-5`. If coverage returns to its pre-collapse range, the model change is the cause.

**Why nothing caught it.** `check_scan_evidence` validates that the evidence artifact exists and is well formed, not that its counts are adequate. "curated sources fetched: 1" passes. The v2 plan recorded the depth of model-attested activity as an accepted model-judgment risk; this incident is that risk occurring, unmeasured. Fix: U12's coverage sensor.

## Proposed fix (awaiting approval; protected paths)

1. **Pin the model** in one place: `scripts/build_claude_settings.py` writes `"model": "<id>"` into the generated settings, which every model step (attempts 1 and 2, both repair passes) already loads.
2. **Pin the action by SHA** at its four `uses:` lines in `.github/workflows/radar-daily.yml`, with the tag as a comment (`@<sha> # v1, pinned 2026-10-xx`). Upgrades then become deliberate commits.
3. **Confirm causality first:** one no-push `workflow_dispatch` with the model pinned to `claude-sonnet-5`, then decide which model to pin long term. Choosing `claude-sonnet-5-5` would require U12's coverage sensor (and possibly prompt changes) before the scan can be trusted.

## Lessons

- Any input that is not pinned is a dependency that can change without a commit. Here, a model upgrade silently changed the system's behaviour.
- A guardrail that checks a receipt exists, without checking the work it records, turns degradation into green runs. Sensors have to check adequacy.
