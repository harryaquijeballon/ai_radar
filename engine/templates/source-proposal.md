# Source-proposal record template (engine P6.5; plan R18–R21)

One record per proposed source in `reviews/source_proposals/<domain>.md`. The
H3 heading is the source's canonical URL — the record's stable identity and
dedup key. Free-text fields are single-line, at most 240 characters.
Machine-checked by `scripts/validators/check_queue_records.py`.

```text
### <canonical source URL>
- source_name: <name of the researcher, outlet, or repository>
- domain: <social_science | ai_engineering>
- first_discovered: YYYY-MM-DD
- last_encountered: YYYY-MM-DD
- source_type: <researcher | outlet | repository | institution — free label>
- why_useful: <one-line justification against the domain profile>
- surfaced_by: <the discovery or entry that surfaced it>
- proposed_purpose: <what watching it would add>
- status: pending
- review_note: <empty until the user reviews>
```

Only the user promotes a proposal into `profiles/<domain>/sources.md` (status
→ `promoted`) or resolves it `rejected` / `already_covered`. Scans never query
pending sources and never edit `profiles/`. Resolved records stay in the file;
automation skips them silently on re-encounter.
