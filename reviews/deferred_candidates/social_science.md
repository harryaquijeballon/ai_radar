# Deferred candidates — social_science

> Review queue written by the unattended radar (engine `Unattended mode`;
> record format: `engine/templates/deferred-candidate.md`). Append-only audit
> trail: automation adds `pending` records and bumps `last_encountered`; only
> the user resolves, and resolved records stay here permanently. Machine-checked
> by `scripts/validators/check_queue_records.py`.

<!-- Example record — commented out; real records append below this comment.
### https://example.org/some-page
- title: Example public title
- domain: social_science
- first_encountered: 2026-07-23
- last_encountered: 2026-07-23
- source_type: commentary
- reason_class: verification_insufficient
- reason: underlying public artifact not yet located
- surfaced_by: watchlist:example
- action_needed: locate public artifact
- status: pending
-->

### https://www.nber.org/papers/w35451
- title: AI Premium
- domain: social_science
- first_encountered: 2026-07-23
- last_encountered: 2026-07-23
- source_type: academic
- reason_class: access_or_license_unclear
- reason: nber.org is on the egress allowlist but WebFetch could not retrieve the page this run (tool-permission error, not a site response); only a search-engine paraphrase was available, insufficient to trace claims to source text.
- surfaced_by: watchlist:nber-working-papers
- action_needed: retry direct fetch of the working paper in a future run, or have a human confirm the abstract/content directly.
- status: duplicate
- resolution_date: 2026-07-31
- resolution: Resolved itself — the 2026-07-29 unattended run fetched nber.org successfully and archived this paper as an accepted, verified entry. No action required.
- linked_ref: library/entries/2026-borri-tsyvinski-liu-ai-premium.md

### https://blog.cosmos-institute.org/p/can-ai-make-scientific-breakthroughs
- title: Can AI Make Scientific Breakthroughs?
- domain: social_science
- first_encountered: 2026-07-23
- last_encountered: 2026-07-23
- source_type: commentary
- reason_class: access_or_license_unclear
- reason: cosmos-institute.org is on the egress allowlist but WebFetch could not retrieve the page this run (tool-permission error, not a site response); only a search-engine paraphrase was available, insufficient to trace claims to source text.
- surfaced_by: watchlist:cosmos-institute
- action_needed: retry direct fetch in a future run, or have a human confirm the essay's argument directly.
- status: archived
- resolution_date: 2026-07-31
- resolution: Fetched successfully in an interactive session and read in full; user approved archiving. Original failure looks environmental, not a site restriction.
- linked_ref: library/entries/2026-georgescu-narayanamurti-tacit-knowledge-discovery.md

### https://www.sciencedirect.com/science/article/abs/pii/S0308596126000467
- title: Digital infrastructure and industrial integration: An assessment of the coupling coordination effect between digital and real economy in China
- domain: social_science
- first_encountered: 2026-07-23
- last_encountered: 2026-07-23
- source_type: academic
- reason_class: access_or_license_unclear
- reason: sciencedirect.com is on the egress allowlist but WebFetch returned HTTP 403 this run; only a search-engine paraphrase was available, insufficient to trace claims to source text (abstract-only access is typical for this publisher).
- surfaced_by: watchlist:telecommunications-policy
- action_needed: confirm accessible abstract/full text and re-review; check licence/paywall status.
- status: dismissed
- resolution_date: 2026-07-31
- resolution: ScienceDirect returns 403 to public fetch interactively too; structurally unreachable. Dismissed. Journal-level coverage gap flagged in profiles/social_science/sources.md.
- linked_ref: profiles/social_science/sources.md

### https://www.sciencedirect.com/science/article/pii/S030859612600042X
- title: "The impact of platform-level privacy policies on users' privacy concerns: Evidence from Apple App Tracking Transparency via a dynamic difference-in-difference analysis"
- domain: social_science
- first_encountered: 2026-07-23
- last_encountered: 2026-07-23
- source_type: academic
- reason_class: access_or_license_unclear
- reason: sciencedirect.com is on the egress allowlist but WebFetch returned HTTP 403 this run; only a search-engine paraphrase was available, insufficient to trace claims to source text (abstract-only access is typical for this publisher).
- surfaced_by: watchlist:telecommunications-policy
- action_needed: confirm accessible abstract/full text and re-review; check licence/paywall status.
- status: dismissed
- resolution_date: 2026-07-31
- resolution: ScienceDirect returns 403 to public fetch interactively too; structurally unreachable. Dismissed. Journal-level coverage gap flagged in profiles/social_science/sources.md.
- linked_ref: profiles/social_science/sources.md

### https://www.aei.org/economics/ai-capability-races-ahead-of-the-business-payoff/
- title: AI Capability Races Ahead of the Business Payoff
- domain: social_science
- first_encountered: 2026-07-28
- last_encountered: 2026-07-28
- source_type: commentary
- reason_class: access_or_license_unclear
- reason: aei.org is not on profiles/egress_allowlist.md; only a search-engine snippet was available (dated 2026-07-27, on the AI capability-vs-economic-payoff gap), insufficient to trace claims to source text and not fetchable this run.
- surfaced_by: open search (economic growth/productivity lens)
- action_needed: approve aei.org for the allowlist or have a human read and judge directly; otherwise dismiss.
- status: archived
- resolution_date: 2026-07-31
- resolution: Fetched and read interactively; user approved archiving AND approved aei.org for the egress allowlist, so this class is reachable by future unattended runs.
- linked_ref: library/entries/2026-pethokoukis-ai-capability-business-payoff.md

### https://www.oecd.org/en/publications/oecd-artificial-intelligence-papers_dee339a8-en.html
- title: Recent policy developments on AI in the labour market
- domain: social_science
- first_encountered: 2026-07-27
- last_encountered: 2026-07-27
- source_type: primary
- reason_class: access_or_license_unclear
- reason: oecd.org allowlisted but WebFetch gave a tool-permission error on every attempt; a 24 Jul 2026 policy paper was search-indicated but not fetched, so claims can't be traced to source text. Link is the series page, not item-specific.
- surfaced_by: watchlist:oecd-ai-papers
- action_needed: locate the item-specific URL and confirm content directly; interactive retry 2026-07-31 also returned HTTP 403, so a further unattended retry is unlikely to help.
- status: archived
- resolution_date: 2026-07-31
- resolution: User supplied the item-specific PDF URL; publisher pages still 403. PDF text extracted and read directly. Archived at medium relevance — a comparative policy inventory, not report-eligible.
- linked_ref: library/entries/2026-oecd-ai-labour-market-policy-review.md

### https://www.oecd.org/en/publications/the-adoption-of-artificial-intelligence-in-firms_f9ef33c3-en.html
- title: The Adoption of Artificial Intelligence in Firms
- domain: social_science
- first_encountered: 2026-08-03
- last_encountered: 2026-08-08
- source_type: primary
- reason_class: verification_insufficient
- reason: oecd.org gave a tool-permission error on every fetch attempt; search snippet claimed a 31 Aug 2026 pub date (future, unverifiable) — cannot confirm the artifact is actually public yet.; re-encountered 2026-08-04, same result
- surfaced_by: watchlist:oecd-ai-papers
- action_needed: fetch the page directly to confirm the real publication date; if not yet published, dismiss as not-yet-public.; 08-06: still blocked; WebSearch again suggests a 2025, not 2026, publication.; 08-08: same block; 2025-05-02 pub date found.
- status: archived
- resolution_date: 2026-08-12
- resolution: User supplied the item PDF (publisher HTML still 403s). Confirmed May 2025 OECD/BCG/INSEAD publication, CC BY 4.0; the 2026 snippet date was wrong. Archived at high by user exception for pre-radar publications of anchor value.
- linked_ref: library/entries/2025-oecd-bcg-insead-ai-adoption-firms.md

### https://arxiv.org/abs/2608.01540
- title: Do people rely on ChatGPT more than their peers to detect deepfake news?
- domain: social_science
- first_encountered: 2026-08-06
- last_encountered: 2026-08-09
- source_type: academic
- reason_class: possible_duplicate_requires_review
- reason: arXiv cross-list dated 2026-08-05; also appears in a 2026 Journal of Economic Interaction and Coordination issue — true first-publication date unconfirmed, possibly a late cross-post.
- surfaced_by: open search (political science / misinformation lens)
- action_needed: confirm the journal publication date; if it predates this window, log as a rejection (already-public cross-post per 2026-08-06 rejections.md entries); if new, review for archiving.; 08-08: found DOI 10.1007/s11403-026-00490-6.
- status: dismissed
- resolution_date: 2026-08-12
- resolution: Public since at least Dec 2024 as ISER DP 1233r (Osaka); arXiv Aug 2026 posting is a late cross-post, not a new development. User dismissed; rejection logged 2026-08-12 so future runs skip it.
- linked_ref: library/rejections.md

### https://thedocs.worldbank.org/en/doc/eb0c4ff411fe0b8cca09c4587ba27eb7-0050062026/original/AI-Adoption-Among-Frontier-Firms.pdf
- title: WDR 2026 | Decoding AI for Development | Background Paper 1: AI Adoption Among Frontier Firms
- domain: social_science
- first_encountered: 2026-08-17
- last_encountered: 2026-08-17
- source_type: primary
- reason_class: information_boundary_unclear
- reason: thedocs.worldbank.org is allowlisted and the PDF opens, but its own cover page is marked "Official Use Only" despite the public URL; unclear whether this is boilerplate or a genuine restricted-distribution document.
- surfaced_by: open search (economic development / lens 2, World Bank AI adoption)
- action_needed: a human should confirm whether "Official Use Only" WDR background papers on public thedocs.worldbank.org URLs are safe to cite, or whether this one was published prematurely/in error.
- status: pending

### https://cepr.org/voxeu/columns/task-based-returns-generative-ai-evidence-central-bank
- title: "Task-based returns to generative AI: Evidence from a central bank"
- domain: social_science
- first_encountered: 2026-07-31
- last_encountered: 2026-07-31
- source_type: academic
- reason_class: access_or_license_unclear
- reason: cepr.org allowlisted but WebFetch returned HTTP 403 repeatedly, as in prior runs; SSRN mirror subdomain also not allowlisted. Search-engine paraphrase only (Marsal & Perkowski, NBS, 31 Jul 2026); can't verify against source text.
- surfaced_by: watchlist:voxeu-cepr
- action_needed: retry direct fetch of the cepr.org column in a future run, or have a human read and confirm the column/underlying paper directly; consider proposing papers.ssrn.com's exact subdomain for the allowlist if SSRN mirrors recur as a blocker.
- status: archived
- resolution_date: 2026-07-31
- resolution: cepr.org still 403 interactively; underlying NBS working paper retrieved via RePEc and archived in its place. User approved papers.ssrn.com and ideas.repec.org for the allowlist.
- linked_ref: library/entries/2026-marsal-perkowski-task-based-genai-central-bank.md
