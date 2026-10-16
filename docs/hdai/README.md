# HDAI handovers: ai_radar

This folder holds agentic-engineering handovers from this project to HDAI, the owner's evidence base on building with AI agents. HDAI reads them from the `main` branch. A handover that has not been merged to `main` is invisible to HDAI.

Project short name: `AIRADAR`. IDs follow `HDAI-AIRADAR-<NNN>`, numbered in sequence with no gaps.

## Index

| ID | Date | Type | File |
|---|---|---|---|
| HDAI-AIRADAR-001 | 2026-10-14 | baseline | [2026-10-14_handover_001_agentic_engineering.md](2026-10-14_handover_001_agentic_engineering.md) |
| HDAI-AIRADAR-002 | 2026-10-16 | delta | [2026-10-16_handover_002_delta.md](2026-10-16_handover_002_delta.md) |

Add one row per handover, newest last.

## When to write one

- **Weekly:** a delta handover covering the past week.
- **Out of cycle:** whenever a session builds new agentic-engineering knowledge, such as an incident, a new guardrail, or a design decision about agents or the harness.
- **Quiet week:** still write the delta. Say that nothing new was learned and give the metrics, the same way the radar reports a quiet day.

## Delta handover format

File name: `docs/hdai/<YYYY-MM-DD>_handover_<NNN>_delta.md`

```markdown
---
handover_id: HDAI-AIRADAR-<NNN>
date: YYYY-MM-DD
project: ai_radar
type: delta
previous_handover: HDAI-AIRADAR-<NNN-1>
repo_head_at_writing: main @ <short hash>
covers: <previous handover's repo_head> .. <this repo_head>
visibility: public | internal | private   # the most restrictive source used
topics: [ ... ]
---
```

Sections (omit a section only if it is empty, and say so):

0. **Summary**: at most six lines.
1. **What changed**: commits in range, grouped. Each item has a hash and one line.
2. **New or changed lessons**: one entry per lesson, in the baseline's four-part playbook form (Rule / Why / How to apply / How to check). Mark each as *new*, *revises P<n>* or *retires P<n>* of the baseline playbook.
3. **Incidents**: each red run in range, with its write-up path. If there is no write-up, say so.
4. **Loop changes**: any change to feedforward guides, sensors, the outer loop or loop metrics (the baseline section 5 layers).
5. **Decisions**: date, decision, reason, record.
6. **Open items**: status changes against the previous handover's list.
7. **Metrics delta**: the baseline section 14 metrics that moved, as before → after, each with its source command.
8. **Memory harvest delta**: memories added or changed since the last handover that generalise, and whether each is now in a versioned file.
9. **Verification**: what was rechecked, what was corrected, and what could not be verified.

Rules, as in the baseline:
- Every claim cites a path or commit hash.
- Mark claims as implemented or intended, and as measured or interpretation.
- Compute every count with a command and cite the command.
- Public-safe content only. No secrets.
