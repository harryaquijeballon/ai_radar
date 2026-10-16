---
handover_id: HDAI-AIRADAR-002
date: 2026-10-16
project: ai_radar
type: delta
previous_handover: HDAI-AIRADAR-001
repo_head_at_writing: main @ c6f54a7 (this handover lands in the next commit, together with two wording corrections it depends on)
covers: 10bdbc4 .. c6f54a7
visibility: public
visibility_note: >-
  Written from the public repository, public GitHub Actions run logs and
  diagnostics artifacts, and one local agent-memory file (section 8). No
  internal, client or employer material was used.
topics:
  - silent model drift
  - pinning agent dependencies
  - adequacy sensors vs existence sensors
  - same-day A/B on a production harness
  - verifying summariser output against raw source
  - discovery-window proxies
  - source coverage
---

# HDAI-AIRADAR-002: delta handover, 2026-10-14 → 2026-10-16

Out-of-cycle delta. A single session built a lot of new agentic-engineering knowledge, centred on one incident: **the unattended radar ran hollow for 18 days while every run reported success.** Tags as in the baseline: **[implemented]**, **[intended]**, **[measured]**, **[interpretation]**.

## 0. Summary

1. [measured] From 2026-09-29 to 2026-10-16, all 18 scheduled runs were green, but they checked 1–4 curated sources per domain (25 and 17 active), against 9–17 before, and finished in 1–2 minutes instead of 8–19. **This corrects the baseline:** its "green for 17 consecutive runs" and "0 silent days" (HDAI-AIRADAR-001 §12, §14) describe hollow runs.
2. [measured] Cause: the workflow used a floating action tag and no model ID. On 2026-09-29 the default model changed from `claude-sonnet-5` to `claude-sonnet-5-5`. A same-day A/B on the production harness confirmed it: 83 turns and 10 entries against 22 turns and 0 entries (`docs/ops/2026-10-16-scan-depth-collapse-incident.md`).
3. [implemented] Model and action are now pinned (`c6f54a7`). Tests forbid a floating action tag.
4. [measured] The guardrail missed it because the scan-evidence check proves the receipt *exists*, not that the work was *adequate*, and the agent's self-reported counts did not even separate the two A/B runs (4/4 vs 3/4).
5. [measured] A second, older defect surfaced in the same investigation: 243 rejections were date-only, 157 of them self-scored as otherwise high, caused by judging "new" by submission date instead of visibility (`docs/plans/2026-10-16-001-fix-discovery-coverage-plan.md`).
6. [intended] Plan U12–U16: a coverage sensor checked against actual fetch tool calls, eligibility by dedup instead of date, re-review of the lost candidates, and loop metrics.

## 1. What changed

**Library and sources**
- `27bde75`: ingested the user-supplied "Economic Scenarios for Transformative AI" (Anthropic Institute WP 2026-02).
- `b31ad25`: Anthropic Institute added to the social-science watchlist with a vendor-source caveat; `www.anthropic.com` and `www-cdn.anthropic.com` added to the egress allowlist.
- `0d482cf`: backfilled four further Institute items; the watchlist row now names the Economics team's dated listing page.

**Diagnosis and fix (plan unit U11)**
- `20252ca`: draft plan `docs/plans/2026-10-16-001-fix-discovery-coverage-plan.md` (U11–U16).
- `9825f03`: incident note, diagnosis from run logs.
- `0212b11`: per-run `model` input for manual dispatches, passed via env and validated as a `claude-*` ID.
- `d552fe5`: A/B result recorded.
- `c6f54a7`: `PINNED_MODEL = "claude-sonnet-5"` in `scripts/build_claude_settings.py`; `anthropics/claude-code-action` pinned to `374f254` at all three `uses:` lines.

**Daily runs**
- `1bf80e3`, `75c96e0`: scheduled runs of 2026-10-15 and 2026-10-16. Both green, both on the hollow configuration.

## 2. New or changed lessons

**L1 (new). Pin everything that can change agent behaviour.**
- *Rule:* reference the agent runtime by commit SHA and the model by explicit ID; a default is a dependency that upgrades itself.
- *Why:* the action tag `@v1` moved three times in 18 days (`756cc22` → `8ce9314` → `374f254`), the CLI went from 2.1.283 to 2.1.301, and the default model changed, all without a commit. One of those changes collapsed the run (incident note, Evidence table).
- *How to apply:* set the model in the generated settings (`scripts/build_claude_settings.py`); pin actions with the tag in a comment; upgrade by deliberate commit.
- *How to check:* `tests/validators/test_workflow_structure.py` fails on a floating `claude-code-action@v<n>` and asserts the settings always contain a model.

**L2 (revises P13). Proof of work must be checked for adequacy, and self-attested counts are not proof.**
- *Rule:* a sensor that checks only that a work receipt exists will turn degradation into green runs; check the receipt against independent evidence.
- *Why:* P13's scan-evidence block made quiet days look honest, so 18 hollow days passed as honest quiet days [measured: social science 14/18 quiet, AI engineering 13/18]. The agent's own curated count was 4/4 in a run that made 23 web fetches and 3/4 in one that found nothing (diagnostics of run 38925669047; job summary of run 38928404856).
- *How to apply:* record names, not counts, and cross-check them against the tool-call record the harness already derives (`model-run-facts.json`: `web_fetches`, per-tool counts) [intended, plan U12].
- *How to check:* a run below a per-domain coverage floor fails loudly (plan U12 test scenarios).

**L3 (new). Effort metrics are a regression sensor; watch their trend.**
- *Rule:* track turns, model-step duration, cost and output per run, and alarm on a step change.
- *Why:* the collapse was visible from day one. Run duration fell from 8–19 min to 1–2 min and cost from $2.93 to $0.35 (`gh run list`; run logs), and nobody looked, because each run was individually "success".
- *How to apply:* add the four numbers to the run summary and compare them with a rolling baseline [intended, U16].
- *How to check:* replaying the 2026-09-29 run against the 2026-09-28 baseline must raise the alarm.

**L4 (new). A/B the production harness, same day, one variable, and know the platform's constraints.**
- *Rule:* confirm a suspected cause with a same-day pair of runs on the real harness that differ in exactly one input.
- *Why:* correlation across three logs pointed at the model, but action and CLI had also changed; the pair isolated the model (incident note, A/B section). The first attempt failed for a non-obvious reason: `claude-code-action` refuses to run a workflow file that differs from the default branch (runs 38922704387, 38922909935).
- *How to apply:* add test knobs to `main` as dispatch-only inputs that are inert on the scheduled path, and prove inertness (the generated settings were byte-identical, `cmp` against `main`'s builder before `0212b11` merged).
- *How to check:* the scheduled path's generated settings are unchanged by the knob.

**L5 (revises P14). Check every figure against the raw source text with a script, not just "the source".**
- *Rule:* P14 says a summary is a lead, never a source. Apply it mechanically: fetch the raw page and string-check every number and quotation before writing.
- *Why:* across five Institute pages, a summariser's output contained two figures that are not in the text ("52×", "26% to 91%") and an unsupported date ("18 March"), and the agent's own draft misquoted one phrase. All four were caught by a string check, none by reading (`0d482cf` Verification notes) [measured].
- *How to apply:* keep a claims list per entry; a small script checks each against tag-stripped page text, including chart labels.
- *How to check:* zero missing strings before the entry is written.

**L6 (new). A date window is a lossy proxy for "seen before".**
- *Rule:* bound *where* a run searches by date, but decide *whether* a find is new by dedup against the library.
- *Why:* arXiv lists papers the day after submission, so a paper submitted on the last covered day is invisible to that run and "already covered" for the next: 243 date-only rejections, 157 self-scored high (`library/rejections.md`) [measured].
- *How to apply:* engine P6.1 rewrite [intended, U13].
- *How to check:* replaying arXiv:2609.15802 yields a review, not a rejection.

**L7 (new). A coverage miss is usually a chain; fix every link.**
- *Rule:* when a relevant source is missed, check the watchlist, the egress allowlist (exact-host) and the source's discoverability (feed or dated listing) separately.
- *Why:* the Anthropic Institute was missed for all three reasons at once: not watched, `www.` and CDN hosts not allowlisted (an Anthropic post was already deferred on 2026-08-20 for this), and no RSS or dated list on the Institute page (`b31ad25`, `0d482cf`). This recurs the baseline's exact-host and first-party-research anti-patterns (HDAI-AIRADAR-001 §8).
- *How to check:* the next scan note lists the Institute among curated sources fetched.

## 3. Incidents

| Run | Outcome | What happened | Write-up |
|---|---|---|---|
| 36558180331 → 38878997439 (all scheduled runs 2026-09-29 → 10-16) | green, hollow | Scan-depth collapse after the silent model change | `docs/ops/2026-10-16-scan-depth-collapse-incident.md` |
| 38922704387, 38922909935 (dispatch, branch) | red, `tooling` | Action refused a workflow file differing from `main`; model never ran | same note, A/B section |
| 38925669047 (dispatch, A/B with `claude-sonnet-5`) | red, `validation` | `REJECTIONS_NOT_APPEND_ONLY`: the run altered `library/rejections.md` other than by appending; cause not recoverable, because diagnostics exclude violating files (R43) | same note; open item |
| 38928404856 (dispatch, A/B default model) | green, `no-change` | 22 turns, 0 entries | same note |

No scheduled run in range was red.

## 4. Loop changes

- **Feedforward:** watchlist row for the Institute with an explicit "score on merits, never by publisher" caveat; the row names the pages to check because the source has no feed (`profiles/social_science/sources.md`) [implemented].
- **Fast sensor:** none new inside the agent's run.
- **Harness sensors:** model and action pinning, enforced by tests (`c6f54a7`) [implemented]. Coverage sensor checked against tool calls [intended, U12].
- **Interpretation sensors:** during manual ingestion, a raw-text string check of every cited figure (L5) [implemented as a session practice, not yet a repository script].
- **Outer loop:** this incident went from detection to confirmed cause, fix and write-up in one session, with an incident note and a plan [implemented]. Re-review of the 243 lost candidates as an agent to-do list [intended, U15].
- **Loop metrics:** cost and turns per run now measured from logs for six runs (§7) [measured]; trend alarm [intended, U16].

## 5. Decisions

| Date | Decision | Reason | Record |
|---|---|---|---|
| 2026-10-16 | Watch the Anthropic Institute, but rank each item on its merits, with no automatic "high" | The user's rule: papers earn their place by quality, not by publisher; it is a vendor source | `b31ad25`; `profiles/social_science/sources.md` |
| 2026-10-16 | Allowlist `www.anthropic.com`, `www-cdn.anthropic.com` | Exact-host matching; the source was unreachable | `profiles/egress_allowlist.md` header |
| 2026-10-16 | Diagnose before fixing; plan U11 first, U13–U16 blocked on it | A window fix cannot be judged on a hollow scan | plan, Key Technical Decisions |
| 2026-10-16 | Pin `claude-sonnet-5` and action `374f254` despite one unexplained violation | The validator aborts delivery on a recurrence, so the risk is a lost day, not library damage; the unpinned state loses every day | `c6f54a7`; incident note |
| 2026-10-16 | Local permission rule for `gh run view/list/download` outside the sandbox | Needed to read run logs; kept git-ignored, not versioned | `.claude/settings.local.json` (local only) |

## 6. Open items

| Item (baseline §12 unless new) | Status change |
|---|---|
| Measure model cost per run | Partly closed: measured from logs for six runs (§7); not yet in run summaries |
| Deferred engine change: vendor-lab watchlist review | Partly done for one lab (Anthropic Institute) |
| Write-ups for 09-10, 09-11, 09-12, 09-27 failures | Unchanged, open. The 09-27 cause (queue-text deadlock) is reconfirmed from its artifact |
| Queue triage (19 pending) | Unchanged: 32 records, 19 pending |
| **New:** first pinned scheduled run (2026-10-17): verify depth and delivery | Open |
| **New:** `REJECTIONS_NOT_APPEND_ONLY` in the A/B run, cause unknown | Open; agreed structural fix: rejection lines appended by the harness, never edited by the model |
| **New:** plan U12–U16 (coverage sensor, window fix, re-review of 243, gap catch-up 09-29 → fix date, metrics) | Open, each unit needs user approval |
| **New:** Economics team publications not in the library (~11 items) | Open, offered to the user |
| **New:** why `claude-sonnet-5-5` stops early | Open; needs the run transcripts |

## 7. Metrics delta

| Metric | Before (10bdbc4) → after (c6f54a7) | Source |
|---|---|---|
| Library entries | 307 → 315 (5 manual on 10-16, 3 by daily runs) | `ls library/entries/*.md \| wc -l`; `git log --diff-filter=A 10bdbc4..HEAD -- library/entries/` |
| Verification | 186 verified / 121 partial → 187 / 128 | `grep -h '^verification:' library/entries/*.md` |
| Rejection-log rows | 291 → 291 (none since 2026-09-28) | `grep -c '^\| 20' library/rejections.md` |
| Daily-run entries, 18 days before vs after 2026-09-29 | 33 → 15 | `git log --diff-filter=A --since/--until … --grep='daily run'` |
| Rejections logged, same windows | 133 → 0 | `grep -cE '^\| 2026-…' library/rejections.md` |
| Curated sources per run (SS / AE), before → after 09-29 | 9–17 / 12–15 → 1–4 / 1–3 | report scan-evidence blocks |
| Scheduled run duration | 8–19 min → 1–2 min | `gh run list --workflow radar-daily.yml` |
| Model cost per run | not measured → $2.93 (09-28), $0.35 (09-29), $0.54 (10-16), A/B $2.66 vs $0.22 | `gh run view <id> --log`, result block |
| Substantive scheduled-run success after the pilot | baseline reported 39/43 (09-02 → 10-14); 16 of those 39 green runs (09-29 → 10-14) were hollow, so 23/43 were substantive | `gh run list`; report scan-evidence blocks |
| Validator tests | 177 → 180 | `python3 -m unittest discover -s tests` |
| Egress allowlist | 56 → 58 domains | `scripts/build_claude_settings.py` output |
| Deferred queue | 32 records, 19 pending → unchanged | regex count excluding commented examples |

## 8. Memory harvest delta

| File | Lesson that generalises | In a versioned file? |
|---|---|---|
| `discovery-coverage-fix-status.md` (new, project) | After pinning a fix, the first production run is the test; check it before any other work | **Yes**: the incident note and plan carry the open item; the memory only adds the "check first" ordering |
| same | Sandbox exclusions match only a single plain command; loops and pipes run sandboxed | **No** (local tooling detail, deliberately not versioned) |

## 9. Verification

**Rechecked:** every count in §0 and §7 with the cited commands on 2026-10-16. The A/B figures come from the run logs' init and result blocks, and the violation rule from the downloaded diagnostics artifact. The schedule-path inertness of `0212b11` was checked with `cmp` against `main`'s builder output.

**Corrected during the session:**
- My first statement that the hollow runs stopped writing to the deferred queues "entirely" was wrong (2 of 17 run commits touched them); corrected in the plan and the incident note in the same commit as this handover.
- My first plan draft recommended a single 60% coverage threshold, which would have failed healthy social-science days (36–68%); replaced with per-domain floors before commit.
- "Four `uses:` lines" corrected to three.
- I first told the user that "When AI builds itself" was probably the rejected arXiv paper; it is not (the entry records the distinction).

**Could not verify:**
- What exactly the A/B run did to `library/rejections.md`: violating files are excluded from diagnostics by design.
- Why `claude-sonnet-5-5` stops early: the transcripts were not read.
- Whether the pinned configuration is healthy on the schedule trigger: the first run is 2026-10-17.
