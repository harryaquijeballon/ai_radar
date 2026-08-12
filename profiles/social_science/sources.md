# Social-science curated sources

> **Strawman draft — edit me.** Every source is public. Types: primary | academic | commentary. Discovery (ENGINE.md P6) checks the active lists first; the radar may append to "Proposed" with justification but never queries it.

## Researchers (via their public trails: working papers, university pages, public posts)

| who | type | why included |
|-----|------|--------------|
| Daron Acemoglu (MIT) | academic | Task-based framework anchoring most credible AI-macro estimates; growth, automation, institutions — lenses 1, 4. |
| Anton Korinek (UVA) | academic | The reference author on generative AI *for* economic research practice; maintains living capability updates — lenses 6, 7. |
| Pedro Sant'Anna (Emory) | academic | Frontier difference-in-differences methods; user already follows — lens 5. |
| Erik Brynjolfsson (Stanford Digital Economy Lab) | academic | Digital economics, productivity J-curve, AI measurement — lenses 1, 3. |
| Susan Athey (Stanford GSB) | academic | ML-assisted causal inference and market design; bridges methods and policy — lenses 5, 4. |
| John Horton (MIT) | academic | LLMs as simulated economic agents ("homo silicus") — the credibility frontier of lens 6. |
| Stefanie Stantcheva (Harvard) | academic | Survey-based methods and public-economics evidence; increasingly AI-instrumented — lenses 5, 4. |
| Ethan Mollick (Wharton) | commentary | Highest-signal practitioner commentary on working with AI; strong on practical workflows — lens 6. |

## Institutions, series and outlets

| source | type | why included |
|--------|------|--------------|
| NBER working papers (weekly digest) | academic | Primary pipeline for new empirical economics, incl. AI/digital topics — all lenses. |
| OECD — AI Papers & Economics Dept. working papers | academic | Cross-country policy-grade analysis (already anchoring the library) — lenses 1, 3, 4. |
| VoxEU / CEPR columns | academic | Fast, citable digests of new research by the authors themselves — all lenses. |
| VoxDev | academic | Development-economics counterpart to VoxEU — lens 2. |
| IMF working papers & blogs | academic | Macro/AI and digital-economy analysis with global coverage — lenses 1, 2. |
| World Bank blogs & working papers (incl. WDR 2026 background papers) | academic | Development + digital adoption evidence, now anchoring lens 2 with firm-level AI-adoption surveys (WDR 2026: The Promise of Artificial Intelligence, worldbank.org/en/publication/wdr2026). Content lives on subdomains — www/blogs/documents/thedocs/openknowledge.worldbank.org — not the bare domain; see the 2026-08-12 coverage note below. Lenses 1, 2, 3. |
| J-PAL / policy evaluation publications | academic | RCT-grade evidence and methods for policy research — lenses 2, 5. |
| GSMA Intelligence — public research | primary | Published connectivity/digital-economy research; public GSMA material is explicitly in scope — lens 3. |
| ITU data and reports | primary | Authoritative connectivity statistics and policy reports — lens 3. |
| arXiv econ.GN (Economics) | academic | Preprint pipeline for AI-and-economics work ahead of journals — lenses 1, 5, 6. |
| Cosmos Institute (cosmos-institute.org) | academic | Philosophy of technology — human flourishing, autonomy, and AI; the anchor source for lens 8. |
| Google / Google DeepMind economics research (ai.google) | academic | First-party economic research on realised AI usage at scale — the ATLAS series maps Gemini usage to BLS occupations, O*NET tasks, ATUS activities, countries and languages. Lenses 1, 2, 3. **Vendor source: treat every distributional result as describing Google's user base first and the economy by inference; never report a first-party adoption claim without that caveat.** Added by user approval 2026-07-31. |
| Telecommunications Policy (journal) | academic | Directly on the connectivity/regulation lenses and not captured upstream — unlike top-5 econ journals, whose content arrives earlier via the NBER/arXiv pipeline (the criterion for adding journals here). Lenses 3, 4. **Known coverage gap — see note below.** |
| Political Analysis (journal) | academic | Computational and quantitative political-science methods venue supporting lenses 5, 7. |
| Towards Data Science | commentary | User's existing high-yield source for applied methods write-ups — lenses 5, 7. |
| One Useful Thing (Mollick's newsletter) | commentary | See researcher row; the newsletter is the trail to watch — lenses 6, 7. |

## Deliberately not covered

**Aniket Panjwani** — retired by user decision 2026-08-12, after the first
~3 pilot weeks produced no archived entries from this trail. The user's
assessment: commentary *about* using AI rather than economic research *with*
AI of the Acemoglu/Korinek grade this watchlist is for. Removed from both
domain watchlists on the same date (it was cross-listed in ai_engineering).
His site remains fetchable if a specific piece is ever user-submitted.

**World Bank coverage note (2026-08-12)** — the pilot's scans could not see
World Bank content: only bare `worldbank.org` was on the egress allowlist
(exact-host, no `www.`/subdomain variants), while the Bank publishes on
`www.worldbank.org`, `blogs.worldbank.org`, `documents.worldbank.org`,
`thedocs.worldbank.org`, and `openknowledge.worldbank.org`. The WDR 2026
background paper "Adopting Fast and Slow" (public 2026-08-03, squarely
lens 2) was missed this way and ingested manually on 2026-08-12.

**LinkedIn** — not a source this radar checks, by user decision 2026-07-31.
Posts are behind a login wall, so no claim can ever be traced to source text
and any entry is stuck permanently at metadata-only provisional. Three such
entries accumulated during v1 and were retired to `library/rejections.md` on
the same date. If a LinkedIn post points to a paper, report, or article,
ingest **that public artifact** instead — the post itself is not the source.

Note that `engine/schema.md` disposition 3 still permits a metadata-only
provisional entry for a walled URL supplied manually. This profile note
records the domain decision; it does not change engine behaviour. Enforcing
it in the engine is a candidate change for pilot close.

## Known coverage gaps

**Telecommunications Policy (Elsevier / ScienceDirect)** — structurally
unreachable by the radar. `sciencedirect.com` is on the egress allowlist, but
the publisher returns HTTP 403 to public fetches of article pages, both in
unattended runs and interactively (confirmed 2026-07-31 against two separate
2026 articles, which were dismissed from the deferred queue for this reason).
Search engines surface titles and paraphrases only, which never satisfy the
engine's claims-traced-to-source requirement.

Consequence: arguably the most profile-relevant journal on this watchlist cannot
be covered by automation at all. Closing this gap requires a human with
institutional access to read items and supply them through manual ingestion —
it is not fixable by allowlist or prompt changes. Until then, treat the
radar's connectivity/regulation coverage (lenses 3, 4) as incomplete on the
peer-reviewed journal side, and well covered on the working-paper and
policy-institution side.

## Proposed (pending approval)

*(moved — proposals now live as pending records in `reviews/source_proposals/social_science.md` (engine P6.5); only the user promotes one into the active lists above. No pending proposals existed at migration, 2026-07-23.)*
