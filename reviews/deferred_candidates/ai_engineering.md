# Deferred candidates — ai_engineering

> Review queue written by the unattended radar (engine `Unattended mode`;
> record format: `engine/templates/deferred-candidate.md`). Append-only audit
> trail: automation adds `pending` records and bumps `last_encountered`; only
> the user resolves, and resolved records stay here permanently. Machine-checked
> by `scripts/validators/check_queue_records.py`.

<!-- Example record — commented out; real records append below this comment.
### https://example.org/some-tool-post
- title: Example public title
- domain: ai_engineering
- first_encountered: 2026-07-23
- last_encountered: 2026-07-23
- source_type: commentary
- reason_class: relevance_requires_judgment
- reason: practical applicability unclear from the abstract alone
- surfaced_by: open search
- action_needed: judge relevance against the profile
- status: pending
-->

### https://openai.com/index/continuous-voice-interaction-with-gpt-live/
- title: How we built a realtime system for responsive voice AI in six months
- domain: ai_engineering
- first_encountered: 2026-08-04
- last_encountered: 2026-08-08
- source_type: primary
- reason_class: access_or_license_unclear
- reason: openai.com is allowlisted but this page returned HTTP 403; search snippets describe an Aug 2026 deep-dive on GPT-Live's low-latency architecture, unverifiable without a direct fetch.; re-encountered 2026-08-06, same result (HTTP 403).
- surfaced_by: watchlist:openai-research
- action_needed: retry direct fetch in a future run, or have a human read and confirm the architecture/latency claims directly.; 08-08: still genuine 403; secondary sources confirm 2026-08-03 pub date — out of window regardless.
- status: dismissed
- resolution_date: 2026-08-12
- resolution: Still 403 interactively 2026-08-12 — openai.com bot-blocks this page, so claims are untraceable; published 2026-08-03, now out of window. User dismissed; rejection logged so future runs skip it.
- linked_ref: library/rejections.md

### https://www.langchain.com/blog/how-stripe-built-their-knowledge-ai-platform-on-deep-agents
- title: How Stripe Built Kai on Deep Agents in 1 Week
- domain: ai_engineering
- first_encountered: 2026-08-04
- last_encountered: 2026-08-06
- source_type: commentary
- reason_class: access_or_license_unclear
- reason: langchain.com is allowlisted but WebFetch gave a tool-permission error every attempt; search snippets describe an Aug 2026 case study on Stripe's Kai agent on the Deep Agents harness, unverifiable without a direct fetch.
- surfaced_by: watchlist:langchain-blog
- action_needed: retry direct fetch in a future run, or have a human read and confirm the architecture claims directly; discount for framework-vendor promotion per profiles/ai_engineering/sources.md.; 08-06: fetched OK, dated 08-03 (OOW); no retry needed.
- status: dismissed
- resolution_date: 2026-08-12
- resolution: Read in full interactively. Out of window (published 2026-08-03) and vendor-promotional per the sources.md discount; adoption claims unverifiable. User dismissed; rejection logged so future runs skip it.
- linked_ref: library/rejections.md

### https://simonwillison.net/2026/Aug/7/pdfs-are-terrible/
- title: The Tokenpocalypse Is Here: Companies Are Scrambling To Stop Spending So Much on AI
- domain: ai_engineering
- first_encountered: 2026-08-08
- last_encountered: 2026-08-09
- source_type: commentary
- reason_class: verification_insufficient
- reason: Willison's post relays a leaked-meeting-audio anecdote (404 Media, 2026-06-24, not allowlisted) about non-engineering staff wasting tokens on PDF-to-markdown conversion; single unquantified anecdote, primary source uncorroborable.
- surfaced_by: watchlist:simon-willison
- action_needed: human should judge whether this thin, uncorroborated anecdote clears the library bar (lens 5) or should be dismissed as too weak to archive even provisionally.; 08-09: re-encountered, no new corroboration, still newest post.
- status: dismissed
- resolution_date: 2026-08-12
- resolution: Read in full interactively: leaked-audio anecdote relayed second-hand, zero quantification, primary source uncorroborable. User dismissed as below the library bar; rejection logged so future runs skip it.
- linked_ref: library/rejections.md

### https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions
- title: Maximizing the value of your Claude Code sessions
- domain: ai_engineering
- first_encountered: 2026-08-15
- last_encountered: 2026-08-15
- source_type: primary
- reason_class: access_or_license_unclear
- reason: claude.com is not on the egress allowlist (only anthropic.com is); search snippets describe an Aug 14 2026 guide on Claude Code context/cache efficiency practices, unverifiable without a direct fetch.
- surfaced_by: open search (harness/context-engineering lens)
- action_needed: approve claude.com (or the specific blog path) for the allowlist, or have a human read and confirm the practices directly; otherwise dismiss.
- status: pending

### https://simonwillison.net/2026/Aug/10/openclaw/
- title: A quote from OpenClaw
- domain: ai_engineering
- first_encountered: 2026-08-11
- last_encountered: 2026-08-11
- source_type: commentary
- reason_class: relevance_requires_judgment
- reason: Single-quote post relaying an ABC News item: "OpenClaw" found an authorization-check bug in a gym-booking API. Unclear if OpenClaw is an AI/agent system (lens 6) or unrelated; ABC News is not on the egress allowlist.
- surfaced_by: watchlist:simon-willison
- action_needed: confirm what OpenClaw is and whether the finding was agent-driven; if so, judge against lens 6; if not, dismiss as off-profile.
- status: dismissed
- resolution_date: 2026-08-12
- resolution: Confirmed agent-driven (OpenClaw agent on Claude; ABC News 2026-08-10 primary source read interactively). User dismissed as a single-incident news story below the library bar; rejection logged so future runs skip it.
- linked_ref: library/rejections.md

### https://arxiv.org/abs/2608.14825
- title: Emergent Misaligned Communication in Long-Horizon Multi-Agent LLM Commerce
- domain: ai_engineering
- first_encountered: 2026-08-18
- last_encountered: 2026-08-18
- source_type: academic
- reason_class: possible_duplicate_requires_review
- reason: Appeared in today's cs.MA listing but submitted 14 Aug 2026 (4-day gap); unclear if genuine new cross-list or prior circulation. Would score high on lens 6 (misalignment/deception in multi-agent commerce sim).
- surfaced_by: watchlist:arxiv-cs.MA
- action_needed: confirm whether this had prior public visibility before 2026-08-18; if genuinely new, archive at high relevance (lens 6).
- status: pending

### https://arxiv.org/abs/2608.14668
- title: BRA-Audit: Budgeted Runtime Auditing for LLM Multi-Agent Systems via Cumulative-Exposure Audit-Point Placement
- domain: ai_engineering
- first_encountered: 2026-08-18
- last_encountered: 2026-08-18
- source_type: academic
- reason_class: possible_duplicate_requires_review
- reason: Appeared in today's cs.MA listing but submitted 2 Aug 2026 (16 days prior) — outside the 7-day window if operative; likely a late cross-list, not new. Would score high on lens 5/6 (token-cost reduction for audit scheduling).
- surfaced_by: watchlist:arxiv-cs.MA
- action_needed: confirm the paper's true first-public date; if it predates the window, treat as not-new and skip in future runs.
- status: pending

### https://arxiv.org/abs/2608.15424
- title: "ETHOS: Towards a Modular Ethics Framework for Clinical Multi-Agent Systems"
- domain: ai_engineering
- first_encountered: 2026-08-18
- last_encountered: 2026-08-18
- source_type: academic
- reason_class: possible_duplicate_requires_review
- reason: Appeared in today's cs.MA listing but submitted 15 Aug 2026 (3-day gap); unclear if genuinely new-to-radar. On-profile for lens 6 (governance meta-agent architecture for clinical multi-agent systems) if window clears.
- surfaced_by: watchlist:arxiv-cs.MA
- action_needed: confirm true first-public date; if within a reasonable window, archive at medium-high relevance (lens 6).
- status: pending

### https://arxiv.org/abs/2608.15181
- title: "Insurance as AI Risk Infrastructure: A Generative-Agent Simulation of AI Adoption"
- domain: ai_engineering, social_science
- first_encountered: 2026-08-18
- last_encountered: 2026-08-18
- source_type: academic
- reason_class: possible_duplicate_requires_review
- reason: Appeared in today's cs.MA listing but submitted 15 Aug 2026 (3-day gap). Cross-domain candidate (agent-based simulation of firm-level AI-adoption economics) — on-profile for both radars if window resolves favorably.
- surfaced_by: watchlist:arxiv-cs.MA
- action_needed: confirm true first-public date; if within a reasonable window, review for cross-domain archiving.
- status: pending

### https://alignment.anthropic.com/2026/agentic-misalignment-summer-2026/
- title: Agentic Misalignment in Summer 2026
- domain: ai_engineering
- first_encountered: 2026-08-18
- last_encountered: 2026-08-18
- source_type: primary
- reason_class: access_or_license_unclear
- reason: alignment.anthropic.com is a subdomain not on the egress allowlist (only bare anthropic.com is listed); snippet describes frontier-lab agentic-misalignment simulations, unverified without a direct fetch, publish date unconfirmed.
- surfaced_by: open search (governance/reproducibility lens)
- action_needed: approve alignment.anthropic.com for the allowlist, or have a human read and confirm the publish date and findings directly; otherwise dismiss.
- status: pending
