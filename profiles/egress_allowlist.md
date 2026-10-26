# Egress allowlist — unattended runs only

The only domains the unattended radar may fetch from (U1 decision, Option A;
plan R48). Human-controlled: scans never add domains — a promising result on
any other domain becomes a deferred candidate or source proposal instead.
The harness derives the model step's `WebFetch(domain:…)` permission rules
from this file (`scripts/build_claude_settings.py`); it is never duplicated
in workflow steps. One `- domain` line per entry. Interactive sessions are
not bound by this list.

Seeded 2026-07-23 from the active watchlists in `profiles/*/sources.md` plus
established academic repositories and publishers — **review and edit freely**.
`WebFetch(domain:…)` rules match the exact host, so needed subdomains are
listed individually (user decision 2026-07-23: no wildcards, no automatic
`www.` variants; `www.nber.org` and `blog.cosmos-institute.org` added after
the stage-4b run observed exact-match permission errors on them).

User approvals 2026-07-31, during the first deferred-queue review: `aei.org`
/ `www.aei.org` (US economic-policy commentary; a deferred candidate the run
could not reach), and `papers.ssrn.com` / `ideas.repec.org` (mirror routes to
working papers — `cepr.org` has returned HTTP 403 on every attempt across
four runs and interactively, so its underlying artifacts are only reachable
through these). Also `ai.google` — first-party Google/DeepMind economics
research (the ATLAS series); added with the vendor-source caveat recorded in
`profiles/social_science/sources.md`.

User approvals 2026-08-12, during the source review that retired the
Panjwani watchlist row: five World Bank hosts (`www.`, `blogs.`,
`documents.`, `thedocs.`, `openknowledge.` — the Bank publishes on
subdomains, so bare `worldbank.org` alone left the source effectively
unreachable; a WDR 2026 background paper public 2026-08-03 was missed this
way) and `www.oneusefulthing.org` (bare domain fails DNS — open scan-note
item since 2026-07-27). Removed on the same date: `aniketpanjwani.com`
(source retired from both watchlists; see `profiles/*/sources.md`).

User approval 2026-10-16: `www.anthropic.com` and `www-cdn.anthropic.com`,
for the Anthropic Institute economics watchlist row. Institute pages live on
`www.`, and its working-paper PDFs on the CDN host. Bare `anthropic.com`,
listed below for ai_engineering, does not match either host under
exact-host matching.

User approval 2026-10-26: eight `www.`/`www2.` hosts that the supervised
U12 check run (40345891512) tried and was denied. Each site redirects its
bare domain to that host, and WebFetch does not follow a redirect to
another host, so these sources were reachable in name only: `www.imf.org`,
`www.oecd.org`, `www.povertyactionlab.org`, `www.gsmaintelligence.com`,
`www.itu.int`, `www2.nber.org`, `www.langchain.com`, `www.llamaindex.ai`.
The bare hosts stay listed, because the first request still goes to them.

## Academic repositories, publishers, identifiers

- arxiv.org
- ssrn.com
- papers.ssrn.com
- ideas.repec.org
- nber.org
- www.nber.org
- www2.nber.org
- doi.org
- aeaweb.org
- sciencedirect.com
- cambridge.org
- oecd.org
- www.oecd.org
- oecd-ilibrary.org
- bis.org
- imf.org
- www.imf.org
- worldbank.org
- www.worldbank.org
- blogs.worldbank.org
- documents.worldbank.org
- thedocs.worldbank.org
- openknowledge.worldbank.org
- ifc.org
- itu.int
- www.itu.int
- povertyactionlab.org
- www.povertyactionlab.org

## Social-science watchlist domains

- cepr.org
- voxeu.org
- voxdev.org
- gsma.com
- gsmaintelligence.com
- www.gsmaintelligence.com
- cosmos-institute.org
- blog.cosmos-institute.org
- aei.org
- www.aei.org
- ai.google
- www.anthropic.com
- www-cdn.anthropic.com
- economics.mit.edu
- oneusefulthing.org
- www.oneusefulthing.org
- substack.com
- towardsdatascience.com

## AI-engineering watchlist domains

- anthropic.com
- openai.com
- deepmind.google
- modelcontextprotocol.io
- huggingface.co
- metr.org
- hai.stanford.edu
- epoch.ai
- github.com
- karpathy.ai
- simonwillison.net
- hamel.dev
- eugeneyan.com
- huyenchip.com
- lilianweng.github.io
- langchain.com
- www.langchain.com
- llamaindex.ai
- www.llamaindex.ai
- kaggle.com
