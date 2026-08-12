"""Real-git fixture repos for U3 validator tests.

Builds one origin repository with a representative base state (entries,
reports, rejection log, protected paths, scripts), clones it once as a
template, and hands each test a fresh copy. Everything runs against real
git so the validators are exercised end-to-end.
"""

import os
import shutil
import subprocess

FIXTURES = os.path.join(os.path.dirname(__file__), "fixtures", "entries")

ACCEPTED_ENTRY = "library/entries/2023-korinek-genai-economic-research.md"
PROVISIONAL_ENTRY = "library/entries/2026-imas-ai-productivity-paradox.md"
REJECTIONS = "library/rejections.md"
PAST_REPORT = "reports/social_science/daily/2026-07-22.md"
TODAY_REPORT = "reports/social_science/daily/2026-07-23.md"

REJECTIONS_BASE = (
    "# Rejection log\n\n"
    "- 2026-07-21 - example.org/one - below discovery bar\n"
    "- 2026-07-22 - example.org/two - duplicate of existing entry\n"
)

INDEX_BASE = (
    "# Library Index\n\n"
    "| slug | title | domains | status | canonical ids / URL |\n"
    "|------|-------|---------|--------|---------------------|\n"
    "| 2023-korinek-genai-economic-research | Generative AI for Economic"
    " Research | social_science | accepted | doi:10.1257/jel.20231736 |\n"
    "| 2026-imas-ai-productivity-paradox | What is the impact of AI on"
    " productivity? | social_science | provisional | aleximas.substack.com |\n"
)


def quiet_report(domain_name):
    return (
        "# %s radar - 2026-07-23\n\n"
        "Window searched: 2026-07-22 to 2026-07-23.\n\n"
        "## Today's developments\n\n"
        "The %s radar searched its window across curated sources and open "
        "search. No material developments cleared the reporting bar today.\n\n"
        "## Scan evidence\n\n"
        "- curated sources fetched: 5\n"
        "- queries executed: 3\n" % (domain_name, domain_name.lower())
    )

DEFERRED_FILE = "reviews/deferred_candidates/social_science.md"
DEFERRED_BASE = (
    "# Deferred candidates - social_science\n"
    "\n"
    "### https://example.org/walled-post\n"
    "- title: Walled discussion of AI adoption\n"
    "- domain: social_science\n"
    "- first_encountered: 2026-07-20\n"
    "- last_encountered: 2026-07-21\n"
    "- reason_class: verification_insufficient\n"
    "- reason: underlying public artifact not yet located\n"
    "- surfaced_by: watchlist:example\n"
    "- action_needed: locate public artifact\n"
    "- status: pending\n"
)

PROPOSALS_FILE = "reviews/source_proposals/social_science.md"
PROPOSALS_BASE = (
    "# Source proposals - social_science\n"
    "\n"
    "### https://newoutlet.example/research\n"
    "- source_name: New Outlet Research\n"
    "- domain: social_science\n"
    "- first_discovered: 2026-07-19\n"
    "- last_encountered: 2026-07-21\n"
    "- why_useful: frequent credible AI-economics coverage\n"
    "- surfaced_by: discovery query\n"
    "- proposed_purpose: watchlist candidate\n"
    "- status: pending\n"
)

NEW_DEFERRED_RECORD = (
    "\n### https://example.org/second-candidate\n"
    "- title: Second candidate\n"
    "- domain: social_science\n"
    "- first_encountered: 2026-07-23\n"
    "- last_encountered: 2026-07-23\n"
    "- reason_class: access_or_license_unclear\n"
    "- reason: domain not on the egress allowlist\n"
    "- surfaced_by: open search\n"
    "- action_needed: approve domain or dismiss\n"
    "- status: pending\n"
)


def _git(args, cwd):
    subprocess.run(
        ["git", "-c", "user.name=fixture", "-c", "user.email=fixture@test",
         "-c", "commit.gpgsign=false"] + args,
        cwd=cwd, check=True, capture_output=True)


def _write(root, rel, content):
    full = os.path.join(root, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as handle:
        handle.write(content)


def _fixture_text(name):
    with open(os.path.join(FIXTURES, name), encoding="utf-8") as handle:
        return handle.read()


def build_template(base_dir):
    """Create origin + template clone under base_dir; return template path."""
    origin = os.path.join(base_dir, "origin")
    os.makedirs(origin)
    _git(["init", "-q"], origin)
    _git(["symbolic-ref", "HEAD", "refs/heads/main"], origin)

    _write(origin, ACCEPTED_ENTRY,
           _fixture_text("2023-korinek-genai-economic-research.md"))
    _write(origin, PROVISIONAL_ENTRY,
           _fixture_text("2026-imas-ai-productivity-paradox.md"))
    _write(origin, "library/INDEX.md", INDEX_BASE)
    _write(origin, REJECTIONS, REJECTIONS_BASE)
    _write(origin, PAST_REPORT, "# Daily report - 2026-07-22\n\nPast content.\n")
    _write(origin, TODAY_REPORT, quiet_report("Social science"))
    _write(origin, "reports/ai_engineering/daily/2026-07-23.md",
           quiet_report("AI engineering"))
    _write(origin, PROPOSALS_FILE, PROPOSALS_BASE)
    _write(origin, DEFERRED_FILE, DEFERRED_BASE)
    _write(origin, "reviews/deferred_candidates/ai_engineering.md",
           "# Deferred candidates - ai_engineering\n")
    _write(origin, "profiles/social_science/profile.md", "# Profile\n")
    _write(origin, "engine/ENGINE.md", "# Engine\n")
    _write(origin, ".claude/skills/social-science-radar/SKILL.md", "# Skill\n")
    _write(origin, "scripts/validators/check_changed_paths.py", "# validator source\n")
    _write(origin, "scripts/run_delivery.sh", "# delivery script\n")

    _git(["add", "-A"], origin)
    _git(["commit", "-q", "-m", "base"], origin)
    # Allow test pushes into this non-bare origin; updateInstead keeps its
    # working tree in sync so later fixture commits start from current state.
    _git(["config", "receive.denyCurrentBranch", "updateInstead"], origin)

    template = os.path.join(base_dir, "template")
    subprocess.run(["git", "clone", "-q", origin, template],
                   check=True, capture_output=True)
    return origin, template


_COUNTER = {"n": 0}


def fresh_workspace(base_dir, template):
    _COUNTER["n"] += 1
    workspace = os.path.join(base_dir, "ws%03d" % _COUNTER["n"])
    shutil.copytree(template, workspace)
    return workspace


def write(workspace, rel, content):
    _write(workspace, rel, content)


def read(workspace, rel):
    with open(os.path.join(workspace, rel), encoding="utf-8") as handle:
        return handle.read()


def remove(workspace, rel):
    os.remove(os.path.join(workspace, rel))


def commit_all(repo, message):
    _git(["add", "-A"], repo)
    _git(["commit", "-q", "-m", message], repo)


def fetch(repo):
    _git(["fetch", "-q", "origin"], repo)
