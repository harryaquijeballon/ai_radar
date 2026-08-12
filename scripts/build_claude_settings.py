"""Generate the model step's permission settings from the egress allowlist
(plan U7/U8; enforces R48 and the S1 Option A egress decision).

The unattended model step gets exactly:
- file Read/Edit inside the workspace checkout, minus `.git/`;
- Read/Edit on the harness-designated evidence directory (outside the repo);
- WebSearch, and WebFetch only for domains listed in
  `profiles/egress_allowlist.md` — no other network surface;
- no Bash, no PowerShell (bare-name deny removes them from the model's
  context entirely), and no access to the runner temp directory where the
  GitHub control files ($GITHUB_ENV, $GITHUB_OUTPUT, ...) live.

Deny rules override allows; in a non-interactive run, anything not allowed
does not execute. Run from the pristine base copy (R41).
"""

from __future__ import annotations

import argparse
import json
import re
import sys

DOMAIN_RE = re.compile(r"^- ([a-z0-9][a-z0-9.-]*\.[a-z]{2,})$")


def read_allowlist(path: str) -> list:
    domains = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            match = DOMAIN_RE.match(line.strip())
            if match and match.group(1) not in domains:
                domains.append(match.group(1))
    if not domains:
        raise ValueError("egress allowlist contains no domains")
    return domains


def build_settings(domains: list, evidence_dir: str, runner_temp: str) -> dict:
    allow = [
        "Read(./**)",
        "Edit(./**)",
        "Read(//%s/**)" % evidence_dir.strip("/"),
        "Edit(//%s/**)" % evidence_dir.strip("/"),
        "WebSearch",
    ]
    allow += ["WebFetch(domain:%s)" % domain for domain in domains]
    deny = [
        "Bash",
        "PowerShell",
        "Read(.git/**)",
        "Edit(.git/**)",
        "Read(//%s/**)" % runner_temp.strip("/"),
        "Edit(//%s/**)" % runner_temp.strip("/"),
    ]
    return {"permissions": {"allow": allow, "deny": deny}}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--allowlist", required=True)
    parser.add_argument("--evidence-dir", required=True)
    parser.add_argument("--runner-temp", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    settings = build_settings(read_allowlist(args.allowlist),
                              args.evidence_dir, args.runner_temp)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(settings, handle, indent=2)
        handle.write("\n")
    print("settings written: %d fetch domains allowed"
          % sum(1 for rule in settings["permissions"]["allow"]
                if rule.startswith("WebFetch(")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
