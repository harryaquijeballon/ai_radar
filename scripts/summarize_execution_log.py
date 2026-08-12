"""Derive a minimal, safe diagnostic record from a Claude Code execution log.

The claude-code-action exposes its raw execution log (the `execution_file`
step output) as a JSON array of SDK messages. That file contains tool inputs
and tool results — including fetched web content — so it must never be
uploaded raw. This parser (2026-07-28 model-bail review) extracts only what a
degenerate-run diagnosis needs:

- how the session terminated (result subtype, error flag, turns, duration,
  cost, permission denials);
- which tools were called, by name and count only (no inputs, no results);
- whether discovery began (WebSearch / WebFetch counts);
- whether the scan-evidence artifact and any daily report files were written;
- the model's final message text, truncated — the only model-authored field.

Never emitted: credentials, tool results, fetched content, URLs, reasoning
blocks, or paths outside the repository-relative `reports/` prefix.

A missing or empty --execution-log is not an error (the model step may not
have run); the script writes nothing and exits 0. A malformed log writes a
record containing only `parse_error`, so the diagnostics step never fails.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

FINAL_MESSAGE_LIMIT = 1500
WRITE_TOOLS = ("Write", "Edit", "MultiEdit", "NotebookEdit")
RESULT_FIELDS = ("subtype", "is_error", "num_turns", "duration_ms",
                 "total_cost_usd", "permission_denials_count")


def build_record(messages, evidence_path):
    tool_counts = {}
    evidence_written = False
    reports_written = set()
    final_text = None
    result = {}

    for message in messages:
        if not isinstance(message, dict):
            continue
        if message.get("type") == "result":
            result = {key: message.get(key) for key in RESULT_FIELDS
                      if key in message}
            continue
        if message.get("type") != "assistant":
            continue
        payload = message.get("message")
        content = payload.get("content") if isinstance(payload, dict) else None
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict):
                continue
            if block.get("type") == "text":
                text = block.get("text")
                if isinstance(text, str) and text.strip():
                    final_text = text
            elif block.get("type") == "tool_use":
                name = str(block.get("name", "unknown"))
                tool_counts[name] = tool_counts.get(name, 0) + 1
                if name in WRITE_TOOLS:
                    target = block.get("input", {})
                    path = str(target.get("file_path", "")
                               if isinstance(target, dict) else "")
                    if evidence_path and path == evidence_path:
                        evidence_written = True
                    marker = path.find("reports/")
                    if marker != -1 and path.endswith(".md"):
                        reports_written.add(path[marker:])

    truncated = final_text is not None and len(final_text) > FINAL_MESSAGE_LIMIT
    return {
        "result": result,
        "tool_calls": dict(sorted(tool_counts.items())),
        "web_searches": tool_counts.get("WebSearch", 0),
        "web_fetches": tool_counts.get("WebFetch", 0),
        "evidence_artifact_written": evidence_written,
        "report_files_written": sorted(reports_written),
        "final_message": (final_text[:FINAL_MESSAGE_LIMIT]
                          if final_text is not None else None),
        "final_message_truncated": truncated,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execution-log", default="")
    parser.add_argument("--evidence-path", default="")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    if not args.execution_log or not os.path.isfile(args.execution_log):
        return 0

    try:
        with open(args.execution_log, encoding="utf-8") as handle:
            messages = json.load(handle)
        if not isinstance(messages, list):
            raise ValueError("execution log is not a JSON array")
        record = build_record(messages, args.evidence_path)
    except (ValueError, OSError) as error:
        record = {"parse_error": str(error)}

    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(record, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
