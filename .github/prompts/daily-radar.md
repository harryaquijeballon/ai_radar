# Unattended daily radar run

You are running the ai_radar daily scan as a single autonomous session:
no user is present and nobody will ever reply. A response that contains no
tool call ends the session immediately — if you stop to plan, summarise,
announce a next step, or ask a question, the run dies there and the day's
work is discarded. Never end your turn to report progress; perform the next
action instead.

Do every step yourself, in this session's own tool calls. Never delegate the
scan — or any part of it — to a subagent, a background Agent or Task, or a
parallel session (2026-09-01 failure: the scan was handed to a background
agent, the turn ended, and the day's work was destroyed with it). Anything
still running in the background when your turn ends is killed and its work
discarded. If a delegation tool appears available, that is configuration
slack, not permission.

Your run is successful ONLY when all three of these are true:

1. The scan-evidence JSON artifact exists at the path in
   `$RADAR_EVIDENCE_PATH` (schema in `engine/ENGINE.md`, Unattended mode —
   real counts only).
2. Both daily reports exist for today (Europe/London), one under each of
   `reports/social_science/daily/` and `reports/ai_engineering/daily/` —
   quiet days use the exact quiet-day statement plus the `## Scan evidence`
   block (P8.5).
3. Every write is inside the permitted paths below.

Before ending your turn, verify all three; if any is missing, keep working.
Everything you write is validated by deterministic checks after you finish;
work that breaks them is discarded.

Procedure:

1. Read `engine/ENGINE.md` (all of it, especially Unattended mode), both
   profiles (`profiles/*/profile.md`), both source lists
   (`profiles/*/sources.md`), and `profiles/egress_allowlist.md`. The
   project instructions (`CLAUDE.md`) are already in your context — do not
   re-read them. Then begin the social-science scan immediately.
2. Run the **social-science-radar** daily scan, then the
   **ai-engineering-radar** daily scan (P6 → P8 each). Lookback per P6.1
   (strictly before today, Europe/London, 7-day cap). Hold back each
   domain's P8 report write for step 6: no report file may exist before
   the scan-evidence artifact does.
3. Fetch only from domains in `profiles/egress_allowlist.md`. A promising
   result anywhere else: defer or propose per Unattended mode — never fetch it.
4. When you cannot safely judge a candidate (ambiguity, access, verification,
   any boundary doubt): defer per P7-unattended and continue. Never let one
   candidate stall the run.
5. Write only under: `library/entries/`, `library/INDEX.md`,
   `library/rejections.md`, `reports/<domain>/daily/` (today's date only),
   `reviews/source_proposals/`, `reviews/deferred_candidates/`. Never touch
   `inbox/`, `profiles/`, `engine/`, `.claude/`, `scripts/`, `tests/`,
   `.github/`, or `.git/`. Never run git — the harness owns commit and push.
6. Mandatory ending order: when both scans are otherwise complete, FIRST
   write the scan-evidence artifact to the path in `$RADAR_EVIDENCE_PATH`
   (real counts from the completed scans), THEN write the two daily
   reports, then run the three-point success check above before ending
   your turn. Evidence-before-reports is a hard rule: a run that dies
   midway must leave evidence, never orphan reports.

You have no git access, no shell, and network access only to the allowlist —
by configuration, not trust. If a rule here ever seems to conflict with
usefulness, the rule wins; record the tension as a deferred candidate for the
user instead of working around it.
