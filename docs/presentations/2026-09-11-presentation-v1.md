# Presentation v1 — the radar in four ideas

One screen for a short talk. The diagram is the story; the table underneath holds the links to open live, top to bottom, ending with the pilot.

```mermaid
flowchart TB
    I1["<b>1 · A library, not a chatbot</b><br/>Every claim traces to a source.<br/>The AI's opinion is labelled as the AI's."]
    I2["<b>2 · It runs itself</b><br/>GitHub Actions wakes Claude Code every morning.<br/>No scan run by hand since 23 July."]
    I3["<b>3 · 10% model, 90% harness</b><br/>The model is the analyst. The harness is the<br/>editor, the security guard and the publisher."]
    I4["<b>4 · Run it like engineering</b><br/>Quiet days are reported honestly.<br/>Every failure gets a written root cause."]
    P["<b>THE PILOT</b> — live unattended since 23 July 2026 · reviewed successful 1 September 2026 · 260 library entries · 177 validator tests · 0 days passed silently · 0 library corruptions"]
    I1 --> P
    I2 --> P
    I3 --> P
    I4 --> P
    classDef idea fill:#f6f8fa,stroke:#57606a,stroke-width:1px,color:#24292f
    classDef pilot fill:#1f6feb,stroke:#1f6feb,stroke-width:2px,color:#ffffff
    class I1,I2,I3,I4 idea
    class P pilot
```

## What to open on screen

| # | idea | say | open |
|---|---|---|---|
| 1 | A library, not a chatbot | Two agents scan public sources daily and archive what clears the bar as structured, citable entries. Frontmatter carries provenance, relevance per domain, verification state and the selection rationale. The "Why it matters" section is marked as the radar's own view. | [one entry](../../library/entries/2026-acemoglu-knowledge-collapse.md) · [the index](../../library/INDEX.md) |
| 2 | It runs itself | Five steps. Actions fires on a schedule. It checks out a pristine copy. Claude Code runs with no shell, no git and a fixed list of websites. Validators diff what it wrote. Only then the harness commits. | [one commit per day](https://github.com/harryaquijeballon/ai_radar/commits/main) · [the workflow](../../.github/workflows/radar-daily.yml) |
| 3 | 10% model, 90% harness | The 10% is one prompt file. The 90% is the egress allowlist, the validators, the human review queues and the tests. Spend the engineering effort on the 90%. | [the prompt](../../.github/prompts/daily-radar.md) · [the validators](../../scripts/validators/README.md) · [the allowlist](../../profiles/egress_allowlist.md) |
| 4 | Run it like engineering | Requirement-first build with acceptance criteria and staged gates. Every incident has a dated write-up. A day with nothing material says so, with the scan evidence listed. | [ops notes](../ops/) · [one incident](../ops/2026-08-12-validation-abort-review.md) · [a quiet day](../../reports/social_science/daily/2026-09-08.md) |
| — | The pilot | Six weeks unattended. Failures were loud, root-caused and fixed. The library never moved on a bad day. | [pilot evaluation](../ops/2026-09-01-pilot-evaluation.md) |

## Key message

Agentic AI does real research monitoring unattended when you split the job. The model judges, the harness enforces, a human resolves doubt. The interesting engineering is in the harness, and the harness is reusable: a new domain is a profile file, not new code.
