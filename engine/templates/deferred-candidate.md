# Deferred-candidate record template (engine unattended mode; plan R12–R14)

One record per candidate in `reviews/deferred_candidates/<domain>.md`. The H3
heading is the canonical public URL — the record's stable identity and dedup
key (tracking parameters, credentials, and tokens stripped). Records are
metadata-only: never candidate content, quotes, or fenced blocks. Free-text
fields are single-line, at most 240 characters. Machine-checked by
`scripts/validators/check_queue_records.py`.

```text
### <canonical public URL>
- title: <public title, only when publicly visible — omit otherwise>
- domain: <social_science | ai_engineering | both, comma-separated>
- first_encountered: YYYY-MM-DD
- last_encountered: YYYY-MM-DD
- source_type: <primary | academic | commentary — omit when not determinable>
- reason_class: <information_boundary_unclear | access_or_license_unclear |
    source_identity_unclear | verification_insufficient |
    relevance_requires_judgment | possible_duplicate_requires_review | other>
- reason: <concise deferral reason — metadata, never captured content>
- surfaced_by: <discovery query or active source that surfaced it>
- action_needed: <what the reviewer must do>
- status: pending
```

Human resolution (interactive session only) appends, never rewrites:

```text
- resolution_date: YYYY-MM-DD
- resolution: <what was decided>
- linked_ref: <library/entries/<slug>.md or rejection-log reference>
```

and edits `status` to one of `archived | provisional | rejected | dismissed |
duplicate`. Record the resolution here **before** writing the destination
artifacts, so the audit trail leads. Resolved records stay in the file
permanently; automation skips them silently on re-encounter.
