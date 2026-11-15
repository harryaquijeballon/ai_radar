---
slug: 2026-willison-beep-locator-coding-agent-senses
title: "Locating the source of a mysterious beep with Claude"
status: accepted
domains: [ai_engineering]
source_type: commentary
source_url: https://simonwillison.net/2026/Nov/9/mysterious-beeps/
canonical_ids: []
publisher_or_author: "Simon Willison — personal weblog"
published: 2026-11-09
captured: 2026-11-15
relevance:
  social_science: n/a
  ai_engineering: medium
verification: verified
rationale: >-
  A personal demo rather than a validated production pattern, but it names
  a concrete, reusable tool-integration technique (lens 3) — giving a
  coding agent real-time multi-device sensor input via browser WebAudio/
  WebSocket, plus live remote code push to connected clients — worth
  knowing even without a reliability evaluation attached.
---

# Locating the source of a mysterious beep with Claude

## Summary
Faced with an intermittent beep coming from a room of unpacked boxes,
Simon Willison had Claude Code build "Beep Locator": a system that uses
several ordinary devices (two iPads, a phone, a MacBook Pro, a Surface
Ultra) as a microphone array to triangulate the sound's source. The system
narrowed the beep's location to within about 40cm, leading him to an old
carbon-monoxide detector that needed new batteries.

Architecture: a Python web server coordinates "listener" clients that join
via a QR code/URL and run in the browser using WebAudio and WebSockets.
Each listener keeps a rolling 60-second audio buffer and runs a beep
detector (FFT plus a high-pass filter). Localization is inspired by the
2007 "BeepBeep" acoustic-ranging paper: devices play calibration chirps to
estimate inter-device distances, and when a beep is detected, clips from
every listener are aligned and compared. An `installModule()` method lets
the server push new JavaScript to already-connected listeners over the
open WebSocket, so the system's behavior could be changed live without
re-visiting each device.

Development process: started on a phone via Claude Code Cloud (Opus 5.5);
Claude found the BeepBeep paper and wrote most of the system from a
problem description. The author then ran it from a laptop with Claude
Code attached to live logs, iterating conversationally. Development
coincided with the release of "Fable 5.2," used for the later stage
(unverified: no comparison of model versions on this task is given).

## Why it matters
Illustrates a concrete, reusable pattern for lens 3 (tool use): extending a
coding agent's effective senses by having it build ordinary browser
clients (WebAudio capture, WebSocket transport) rather than relying on
native multimodal input the model lacks — plus a live remote-code-push
mechanism for iterating on already-deployed listener clients without
redeploying to each device. Both are general techniques transferable to
other agent-built, multi-device monitoring or data-collection tools, even
though this instance is a one-off personal demo with no formal evaluation
of accuracy or reliability.

## Verification notes
Fetched simonwillison.net's post directly; the architecture, hardware
list, localization method, and development narrative above are traced to
its text. No independent corroboration was sought for the ~40cm
localization claim (a single self-reported outcome on one personal
project, not a load-bearing comparative or benchmark figure).

## Updates
None yet.

## Related entries
None yet.
