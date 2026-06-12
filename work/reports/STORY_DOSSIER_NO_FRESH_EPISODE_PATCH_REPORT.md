# Story dossier no-fresh + episode emphasis patch

## Purpose

This patch updates the story dossier source-accumulation mode without changing the TS loop core.

## Changes

- `RUN_STORY_DOSSIERS_SOURCE_ACCUMULATION.md` now forbids `fresh` for real runs.
- Missing story dossier files must be initialized by the controller with a minimal stub before invoking the loop, not by `--mode fresh`.
- Each worker-subagent should run exactly one pass and exit; the controller proceeds round by round.
- The lower prompt keeps the earlier anti-anchoring direction, but lightly shifts emphasis from analytical “turns/framing” toward concrete episodes: `что было → что сделали → как стало → чем это подтверждается`.
- `run-story-dossier-loop.cmd` defaults to `--mode continue` and does not pass `--fresh-action`.

## TS core

No TS files are changed.
