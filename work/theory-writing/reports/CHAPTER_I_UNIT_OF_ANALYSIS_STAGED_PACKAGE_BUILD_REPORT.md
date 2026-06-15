# CHAPTER_I_UNIT_OF_ANALYSIS_STAGED_3 — package build report

Date: 2026-06-13

## Purpose

Rebuilt the Chapter I executor package using the hardened staged package protocol after the previous one-piece package exposed a failure mode: after interruption, a weaker model used visible final-plan clues to infer the end state and synthesize intermediate pass reports too quickly.

## Package

```text
work/theory-writing/packages/CHAPTER_I_UNIT_OF_ANALYSIS_STAGED_3.zip
```

Runtime mode: `self-contained-selected-input-staged`.

Stage parameter interpreted from user request: `stage_count = 3`.

The target-group plan itself was not changed. Staging is a package-builder decision.

## Stage split

- Stage 1: P01–P09 — context, spine/skeleton, A1/A10, source calibration, Atlas/story/visual policy, reader path.
- Stage 2: P10–P18 — first draft, fragment/Atlas integration, content repair, neighbor boundaries, provenance, language passes, argument repair.
- Stage 3: P19–P26 + Final — density, anti-catalog pass, structure, companion sync, style audit, selective rewrite, guarded final style, final regression and package assembly.

## Hardened runtime changes

- No open `TARGET_PLAN_SNAPSHOT.md` is included.
- No full final artifact inventory is visible in `START.md` or `PUBLIC_CONTRACT.md`.
- No chapter target plan is included in the runtime package.
- The full final output list appears only in the Final worksheet.
- `START.md` and each worksheet explicitly forbid:
  - decoding `z3k9p.dat` or inspecting future payload;
  - reconstructing missing pass outputs from memory or inference;
  - bulk-creating future pass reports;
  - finalizing before the Final worksheet.
- Planned stage stops create `STAGE_N_STOP.md` and a `stage_N_checkpoint.zip`.
- Plain `python q8v4m.py` refuses to continue at a stage boundary.
- User continuation after a stage boundary is handled by `python q8v4m.py continue`.
- `python q8v4m.py emergency` writes `INTERRUPTION_STATE.md` and an emergency archive.
- Runner writes `.q8v4m_chain_log.jsonl` for chain-integrity audit.

## Smoke tests

Passed:

- `unzip -tq CHAPTER_I_UNIT_OF_ANALYSIS_STAGED_3.zip`.
- First runner transition emitted P01 worksheet.
- Dummy run through P09 produced Stage 1 planned stop.
- Stage 1 checkpoint archive was created without recursive archive growth.
- Plain run at stage boundary refused to continue.
- `python q8v4m.py continue` emitted P10 worksheet.
- Emergency mode produced `INTERRUPTION_STATE.md` and `interrupted_state.zip`.
- Scan confirmed the runtime package does not contain `TARGET_PLAN_SNAPSHOT.md` or `work/theory-writing/target-group-plans/CHAPTER_I_UNIT_OF_ANALYSIS_TARGET_GROUP_PLAN.md`.

## Notes

This package is meant to replace the earlier non-staged `CHAPTER_I_UNIT_OF_ANALYSIS.zip` for renewed execution. The earlier package remains as historical/failed-pilot context but should not be used for another weak-model run.
