# v2 Feasibility and Governance Gate (U1)

Dossier for the U1 go/no-go checkpoint of `docs/plans/2026-07-23-001-feat-unattended-daily-radar-plan.md`. Every claim below is classified **confirmed fact** (verified against current official primary documentation or a live probe on 2026-07-23), **implementation assumption**, **accepted risk** (needs user sign-off), or **unresolved organisational question**. No credentials were created, printed, or stored in producing this dossier; no `ANTHROPIC_API_KEY` exists and none will be created.

## Gate table

| # | Gate item | Finding | Authoritative source | Verdict | Consequence for preferred architecture | Fallback |
|---|---|---|---|---|---|---|
| 1 | Unattended scheduled execution with `CLAUDE_CODE_OAUTH_TOKEN` | The official action defines `claude_code_oauth_token` ("alternative to anthropic_api_key"); `anthropic_api_key` is optional; automation mode runs from a `prompt` input on any trigger, with an official scheduled "daily report" example | `anthropics/claude-code-action` `action.yml` (fetched raw, 2026-07-23); code.claude.com/docs/en/github-actions | **pass** | Preferred architecture viable exactly as planned | Cloud Routine (origin R33) — not needed |
| 2 | Token generation, storage, rotation, revocation, expiry | `claude setup-token`: browser flow, one-year token, printed once, never saved locally; env var `CLAUDE_CODE_OAUTH_TOKEN`; Pro/Max/Team/Enterprise; "can only make model requests"; expired credentials fail requests with an explicit auth error. Rotation = regenerate + replace secret. Revocation mechanism: not documented | code.claude.com/docs/en/authentication (fetched 2026-07-23) | **conditional** | Lifecycle manageable: store only in GitHub Actions secrets; ~11-month renewal reminder; AUTH failure class in the harness catches expiry. Revocation path must be confirmed before an incident, not during one | If revocation proves impossible short of account-level logout, document token-compromise response as rotate-and-replace plus Anthropic support contact |
| 3 | Billing / quota / subscription implications | Token "authenticates with your Claude subscription" — usage draws on subscription limits, not API metering. CI rate-limit behaviour: not documented. GitHub side: free plan includes 2,000 Actions minutes/month for private repos; one daily run (≤2 model attempts) fits comfortably | code.claude.com/docs/en/authentication; docs.github.com (Actions billing) | **requires user/employer confirmation** | Daily unattended runs consume the user's personal subscription quota; heavy days could contend with interactive use | U9 stage-7 supervised runs observe real usage before daily activation; reduce scan breadth if contention appears |
| 4 | Token / GitHub credentials / control files visible from model tool context | The token reaches the runtime as an environment variable (auth precedence item 5). Environment variables are readable only through shell execution; a bare-name `Bash` deny rule "removes the tool from Claude's context entirely" (same for `PowerShell`), and file tools read files, not env. GitHub credentials: `persist-credentials: false` keeps the job token out of the model workspace. Control files (`$GITHUB_ENV` etc.) are ordinary files — governed by the write-scope rules in item 5 | code.claude.com/docs/en/permissions ("Permission rules are enforced by Claude Code, not by the model"; deny-rule semantics); docs.github.com github_token; action.yml (`settings`, `claude_args` inputs) | **conditional pass** | Structural mitigation exists by configuration: deny `Bash`/`PowerShell` outright, allow-list writes. Certified only by the U7 drills and the U9 re-probe against the assembled workflow (plan R48/R49) | If a drill shows the token retrievable despite the tool restrictions → no-go on the preferred path; revisit with Claude Code sandboxing or the Routine fallback |
| 5 | Write scope structurally limited to workspace + evidence path, deny-all `.git/`, credentials, control files | Permission rules support gitignore-style path scoping: `Edit(/src/**)` (project-relative), `Edit(//abs/path)` (absolute); `Edit` rules "cover all file-editing tools"; evaluation order is deny → ask → allow, and un-allowed calls in a non-interactive run do not proceed. The R48 scope is expressible as: allow `Edit` on workspace-relative paths + one absolute evidence path; deny `Edit(/.git/**)`; deny `Bash`. Caveat: Read/Edit rules bind Claude's file tools, "not arbitrary subprocesses" — moot with `Bash` denied; Claude Code sandboxing exists for OS-level enforcement as defence-in-depth | code.claude.com/docs/en/permissions (rule syntax, deny precedence, v2.1.210 Edit-covers-writes note, subprocess warning) | **pass (expressible); drill-certified later** | R48's exact scope is implementable with documented syntax via the action's `settings` input; U7 tamper/control-file drills prove it | If the action's `settings` path proved unable to carry permission rules, `claude_args` `--disallowedTools` is the second documented mechanism |
| 6 | Network egress restricted to the discovery surface | Per-domain restriction is supported: `WebFetch(domain:example.com)` allow rules; deny rules can remove `Bash` network commands entirely. But open-web discovery (engine P6, second phase) wants breadth: a fetch-domain allowlist restricts discovery to enumerable domains. Full restriction and full discovery are in tension | code.claude.com/docs/en/permissions (WebFetch domain rules; network-access guidance) | **requires user sign-off** (option choice) | Option A (pilot default, recommended): WebFetch domain allowlist = watchlist domains + major venues (arXiv, NBER, SSRN, OECD, BIS, GitHub, major labs/outlets from `profiles/*/sources.md`), reviewed as part of profiles; open-search results outside the allowlist are deferred as candidates rather than fetched. Option B: unrestricted WebFetch — full discovery breadth, but the read-plus-fetch exfiltration channel is open and must be signed off as an accepted risk (bounded by the repo being public-safe by construction and no model-readable credential per item 4) | Start with Option A, widen the allowlist from deferred-candidate evidence; switch to B only by explicit later decision |
| 7 | GitHub Actions: schedule, concurrency, artifacts, notifications, job summary | `on.schedule` supports `timezone:` with IANA strings ("By default, scheduled workflows run in UTC. You can optionally specify a timezone…", example YAML confirmed); delays documented at high load (top of hour — 10:07 avoids it); 60-day auto-disable is scoped to public repositories only; `concurrency` + `cancel-in-progress: false` queues without cancelling (one pending slot); `$GITHUB_STEP_SUMMARY` 1 MiB/step; per-run notifications configurable (all statuses or failure-only) routed to the workflow's creator/last-modifier; `actions/upload-artifact@v7`, `if: failure()` conditional upload | docs.github.com events-that-trigger-workflows (fetched 2026-07-23, timezone text quoted verbatim); docs.github.com workflow-syntax, concurrency, notifications, workflow-commands pages (verified 2026-07-23 in planning research) | **pass** | All required platform behaviour exists as designed, including the exact `cron: "7 10 * * *"` / `timezone: "Europe/London"` shape recorded in the requirements | None needed; dual-cron UTC fallback documented in the rollout runbook if the young timezone feature misfires |
| 8 | Private visibility confirmed through GitHub | Live API probe: `gh repo view harryaquijeballon/ai_radar --json visibility,isPrivate` → `{"isPrivate":true,"visibility":"PRIVATE"}`. Corollary probe: branch-protection API returns 403 "Upgrade to GitHub Pro…" — the free plan cannot have protection rules on private repos, so (a) nothing blocks the workflow's `GITHUB_TOKEN` push, and (b) `main` has no platform-level protection: the repository validators are the only guard on unattended pushes, as the plan already assumes | Live `gh` probes, 2026-07-23 (read-only) | **pass** | R35 satisfied by API evidence, not local inference; push path unobstructed | Re-verify at U9 acceptance (already planned); repo visibility is a point-in-time check — governance rule stands |
| 9 | Employer policy / approval questions | Not determinable technically — enumerated below for the user | — | **requires user/employer confirmation** | Unattended execution must not be authorised until answered | None — organisational gate |

## Confirmed facts (primary-source, 2026-07-23)

1. `claude_code_oauth_token` is a first-class input of the official action; no API key required (action.yml, fetched raw).
2. Automation mode with a `prompt` runs on `schedule` triggers; officially documented with a scheduled example (code.claude.com/docs/en/github-actions).
3. `claude setup-token` mints a one-year, subscription-authenticated, model-requests-only token intended for CI; printed once, never persisted locally (code.claude.com/docs/en/authentication).
4. GitHub Actions `on.schedule` supports IANA `timezone:`; UTC is only the default (docs.github.com, quoted verbatim).
5. The 60-day scheduled-workflow auto-disable applies to public repositories only (docs.github.com).
6. Claude Code permission rules: gitignore-style path scoping on `Edit` (covering all file-editing tools), `WebFetch(domain:…)` scoping, deny-overrides-allow, and bare-name `Bash` deny removing the tool from the model's context; rules are enforced by Claude Code, not the model (code.claude.com/docs/en/permissions).
7. The action accepts permission configuration via its `settings` input (JSON string or file path) and `claude_args` (action.yml).
8. Repository visibility is `PRIVATE` per the GitHub API; branch protection is unavailable on this plan, so no rule can block the delivery push.
9. Default-`GITHUB_TOKEN` pushes cannot trigger other workflows; `contents: write` is the needed permission (docs.github.com github_token, verified in planning research).

## Implementation assumptions (to be certified by drills, not documentation)

- A1. With `Bash`/`PowerShell` denied bare-name and writes allow-listed, no tool surface reads environment variables → token not retrievable from the model context. Certified at U7 drills and the U9 re-probe (plan R48).
- A2. The action's `settings` input carries the permission block into the headless run unchanged. Certified at U7.
- A3. An expired/revoked OAuth token surfaces as a step-failing auth error the harness can classify as AUTH. Certified at the U9 revoked-token rehearsal.
- A4. Un-allowed tool calls in non-interactive mode are denied rather than queued for a prompt. Certified at U7 (control-file drill).

## Egress decision — S1 resolved (user, 2026-07-23)

**Option A adopted: restricted WebFetch domain allowlist.** The unattended workflow may fetch only from: active sources and domains in the approved domain profiles; established academic repositories, publishers, and institutions included in the allowlist; and other domains explicitly approved through the source-proposal review process. When discovery identifies a potentially useful result on a non-allowlisted domain, the run does not fetch the page; it creates or updates a metadata-only deferred candidate or source proposal (as appropriate), records that domain approval is required (reason class `access_or_license_unclear` or a dedicated note), and continues safely. Unknown domains are never added to the allowlist automatically — promotion requires explicit human approval.

Design consequence for U5/U7/U8: the allowlist is configuration-driven and human-controlled — one file under `profiles/` (a protected path; e.g., `profiles/egress_allowlist.md`), from which the workflow derives the `WebFetch(domain:…)` permission rules at run start. It is never duplicated across workflow steps.

## Accepted risks — acknowledged by the user (2026-07-23)

Acknowledged for planning and development; acknowledgment does not mean activation. Each must remain visible in the rollout runbook and checklist (U9).

- S2. **Subscription consumption (gate 3).** Daily unattended runs draw on the personal Claude subscription's usage limits; CI-specific rate/quota behaviour remains to be observed during controlled rollout (U9 stage 7).
- S3. **Token longevity.** If and when generated, `CLAUDE_CODE_OAUTH_TOKEN` is a long-lived (one-year) bearer credential stored as a GitHub Actions secret. Mitigations: secrets-only storage, no-echo rules, renewal reminder, drill-certified non-retrievability.
- S4. **Unprotected `main`.** Platform branch protection is unavailable on this plan; deterministic validators, restricted credentials, and fast-forward-only delivery are the principal controls protecting `main`.

## Activation gate (recorded 2026-07-23)

> **No OAuth token may be generated, no GitHub secret may be created, and no model-dependent GitHub Actions run may execute until Q1–Q4 are resolved and the user explicitly approves activation.**

Q1–Q4 below are mandatory **pre-activation blockers**. They do not block credential-free work.

**Permitted before activation:** deterministic validators; fixtures and tests; engine and review-queue documentation; non-secret workflow linting; local dry runs that do not invoke Claude remotely.

**Prohibited before activation:** `claude setup-token`; creation of `CLAUDE_CODE_OAUTH_TOKEN`; storing any model credential in GitHub; any GitHub Actions run that invokes Claude; activation of the daily schedule.

## Pre-activation blockers — RESOLVED for the supervised rollout (user approval, 2026-07-23)

The user approved Q1–Q4 on 2026-07-23, with organisational context confirmed: work authorised by the user's employer on an authorised Claude plan and GitHub account; public sources only; no confidential ingestion; no API keys, Console credits, alternative providers, or custom LLM clients. Cost controls confirmed external to this repo: Claude usage credits off, no pay-as-you-go billing, GitHub Actions $0 paid-usage budget with stop-usage enabled. `CLAUDE_CODE_OAUTH_TOKEN` was created manually by the user as an encrypted Actions repository secret (verified present 2026-07-23; no other secret exists).

- Q1 **approved** — employer-related use of this unattended agent is authorised for this product and the supervised pilot.
- Q2 **approved** — the OAuth token as an encrypted GitHub Actions repository secret.
- Q3 **approved** — `claude setup-token` through the existing authorised plan; no API key, Console credits, alternative provider, or custom LLM client may be introduced.
- Q4 **approved** — compromise response: disable the workflow, delete the GitHub secret, revoke or replace the token (runbook rollback table).

**This approval authorises supervised rollout tests only.** Still NOT authorised: enabling the daily 10:07 schedule; distributing reports to additional recipients; ingesting private/confidential employer information; introducing paid API usage; removing safety or validation controls.

## Original blocker text (historical)

- Q1. Confirmation that employer policy permits an unattended Claude Code agent using a personal subscription credential on GitHub-hosted runners for this work-oriented private repository. (Security/IT confirmation.)
- Q2. Confirmation that storing a Claude subscription OAuth token in GitHub Actions secrets is acceptable under the employer's credential and security policy.
- Q3. Confirmation that the user's Claude subscription type and ownership permit `setup-token` use for this workflow, including any relevant usage or billing implications.
- Q4. A documented and tested token revocation or compromise-response path, in place before the token is generated or installed.
- ~~Q5. Egress option choice~~ — resolved 2026-07-23: Option A (see Egress decision above).

## Probes performed (all non-destructive, no credentials involved)

| Probe | Result |
|---|---|
| Raw fetch of `anthropics/claude-code-action` `action.yml` | 39 inputs enumerated; auth and tool-config inputs confirmed |
| Fetch code.claude.com/docs/en/authentication | Token lifecycle confirmed; revocation undocumented |
| Fetch code.claude.com/docs/en/permissions | Path/domain rule syntax, deny semantics, subprocess caveat confirmed |
| Fetch docs.github.com events-that-trigger-workflows | `timezone:` support, delay and auto-disable scoping confirmed |
| `gh repo view --json visibility,isPrivate` | `PRIVATE` / `true` |
| `gh api …/branches/main/protection` | 403 "Upgrade to GitHub Pro" → no protection rules possible on this plan |

Also observed: the local `gh` keyring reports an invalid token for `harryaquijeballon` while API calls still succeed via the active credential — worth a `gh auth refresh` at the user's convenience; not a gate item.

## Authentication boundary (binding contract)

> **Claude Code performs all model-dependent work using subscription OAuth authentication through `CLAUDE_CODE_OAUTH_TOKEN`. No `ANTHROPIC_API_KEY`, Anthropic Console API billing integration, or custom LLM API client is permitted.**

The boundary is total, not preferential. This project must not create, store, reference, or use: `ANTHROPIC_API_KEY`; an Anthropic Console API key; custom Python, JavaScript, or shell code calling an Anthropic model API directly; pay-as-you-go API authentication as a fallback; or Bedrock/Vertex/Foundry or any other model provider, absent an explicit later redesign. "Claude Code only" means Claude Code and its official Action are the sole model interface, authenticated through subscription OAuth — not that the model operates without contacting Anthropic's service.

**Deterministic enforcement (implemented and drilled at U7/U8; recorded here as contract):**

1. The workflow contains no `anthropic_api_key` input (statically checkable against `radar-daily.yml`).
2. `ANTHROPIC_API_KEY` is absent from the workflow environment.
3. The workflow fails closed if `ANTHROPIC_API_KEY` is unexpectedly present.
4. The Action receives only `${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}` for Anthropic authentication.
5. No implementation may silently fall back to API-key authentication.
6. Logs and summaries never reveal more than a boolean OAuth-secret readiness result, and never print any portion of the token.

**Two distinct conclusions, kept separate:**

- **Pass:** no Anthropic API key or custom API integration is technically required anywhere in the preferred architecture. Two documented edge features are excluded by design rather than needed: the action's `classify_inline_comments` option requires an API key (a PR-comment feature this workflow never enables), and Claude Code's `--bare` mode does not read `CLAUDE_CODE_OAUTH_TOKEN` (this workflow does not use bare mode).
- **Still conditional:** using a subscription OAuth token for unattended work-oriented automation awaits confirmation on subscription usage (S2/Q3), credential policy (Q2), and organisational approval (Q1).

## Architecture verdict

**Conditional GO for the preferred architecture** (GitHub Actions harness + official Claude Code action + `CLAUDE_CODE_OAUTH_TOKEN`). No structural no-go was found: every platform capability the plan depends on is confirmed in current primary documentation, and the two security-critical properties (credential invisibility, write-scope enforcement) are expressible with documented mechanisms and are already scheduled for drill certification (U7/U9). The Routine fallback (origin R33) remains documented and unneeded.

**U1 verdict approved by the user on 2026-07-23**, subject to the activation gate above: S1 resolved as Option A; S2–S4 acknowledged; Q1–Q4 stand as pre-activation blockers. Credential-free implementation (U2 onward, per the permitted list) may proceed; nothing model-dependent or credential-bearing may run before explicit activation approval.
