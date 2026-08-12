# Validator contract

Deterministic guardrails for the unattended radar (plan `docs/plans/2026-07-23-001-feat-unattended-daily-radar-plan.md`, R41/R42/R47). Python 3.9+ standard library only — no dependencies, no install step, identical behaviour on macOS (manual runs) and ubuntu runners.

## The contract

Every validator in this directory obeys all of the following. Two implementers following this file must produce identically behaving validators.

**Exit codes (R42)**

| Code | Meaning | Caller behaviour |
|---|---|---|
| 0 | Pass — no violations | Continue |
| 1 | Violations found (one per stdout line) | Route by class, below |
| 2 | Internal error | Always treat as abort — fail closed |

**Violation classes (R42)**

- `abort` — the run stops: path/history breaches, missing scan evidence, a report item without its entry. Never repaired automatically.
- `repairable` — content defects (index drift, malformed record, schema field issues). The harness may grant at most one bounded repair pass, then rerun the **complete** validator suite; a second failure aborts.

**Output format** — one violation per line, machine-parseable:

```
CLASS RULE_ID path[:line] - message
```

`CLASS` is `ABORT` or `REPAIRABLE`; `RULE_ID` is UPPER_SNAKE. An internal error prints a single `INTERNAL VALIDATOR_ERROR - <ExceptionClassName>` line and exits 2.

**No-echo rule (R47)** — violation messages identify file, line, and rule only, plus short schema-controlled identifiers (a field name, a domain, a count). They never reproduce flagged file content. This is enforced structurally: `lib_radar.emit()` is the only way to build a violation, it accepts no free-text parameter, and every slot value is sanitized — anything with a newline, over 80 characters, or outside a conservative identifier charset is replaced with `[content redacted]`. Rule message templates are registered constants, not call-site strings. Paths are model-chosen too: any path segment outside the slug charset is replaced with `[redacted-<8-char digest>]` so the reviewer can locate the file without the output carrying its name.

**Fail closed** — wrap every validator's entry point in `lib_radar.run_main(main)`. Any uncaught exception prints the exception class name only and exits 2. Callers treat exit 2 as abort.

**Pristine-base invocation (R41)** — in the scheduled workflow, validators are executed from the read-only pristine copy of the base commit, never from the model-writable workspace. Nothing in this directory may assume it is running from the workspace checkout; take the repo root to inspect as an argument.

**Dates (R44)** — any notion of "today" comes from `lib_radar.london_today()` (Europe/London), never from the runner's local clock or UTC directly.

## Validator catalog

| Script | Enforces | Classes |
|---|---|---|
| `check_changed_paths.py` | Allowlist (R22/R23); history protection incl. `reviews/` audit trail (R50); entry-body and queue-record preservation; run-date report discipline (R44); `--mode unattended|manual` gates queue lifecycle transitions | abort |
| `check_clean_base.py` | Manual-run preconditions: clean tree, known upstream, no divergence (R24/R29) | abort |
| `check_scan_evidence.py` | Scan-evidence artifact presence/structure on every outcome (R39) | abort (TOOLING) |
| `check_library_consistency.py` | Entry schema conformance; slug/filename; INDEX agreement | repairable |
| `check_report_integrity.py` | Report bar: entry link resolves (abort), accepted+verified+high relevance, ≤3 items, quiet-day statement + evidence block | abort / repairable |
| `check_queue_records.py` | Queue structure, controlled vocabularies, URL hygiene, metadata-only bounds, duplicates incl. sibling-domain | repairable |
| `../make_run_summary.py` | R37 job summary — derived counts, controlled vocab, safe paths only; no model-authored text can reach it | n/a (generator) |

Queue-record and scan-evidence formats are DRAFT until the U5 engine revision adopts them (documented in `lib_queues.py` and `check_scan_evidence.py`).

## Adding a validator

1. Register rules at module import: `lib_radar.register_rule("MY_RULE", lib_radar.ABORT, "template with {slot}")`.
2. Build violations only via `lib_radar.emit("MY_RULE", path, line, slot=value)`.
3. Return `lib_radar.report(violations)` from `main()`, and guard with `sys.exit(lib_radar.run_main(main))`.
4. State in the module docstring which plan requirement the validator enforces.
5. Add fixture-based tests under `tests/validators/`, including at least one no-echo test proving flagged fixture content never appears in output.

## Running the tests

```
python3 -m unittest discover -s tests -v
```
