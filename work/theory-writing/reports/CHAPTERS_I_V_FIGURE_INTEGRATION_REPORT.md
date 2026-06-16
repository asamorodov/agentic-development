# Chapters I–V figure integration report

Date: 2026-06-15

This pass turned the previously collected illustration candidates for Chapters I–V into actual chapter figures.

## What was added

### Chapter I
- Replaced the old inline synthetic table with a local image asset explaining partial carriers versus software change.
- Added a second local image asset showing the minimal lifecycle axis of a software change.

### Chapter II
- Added a source-backed redraw showing that the session is wider than chat.
- Replaced the inline synthetic trace-to-state block with a local image asset.

### Chapter III
- Added three local ADR/atlas assets: minimal ADR record, ADR lifecycle, and MADR confirmation.

### Chapter IV
- Added the REASONS Canvas figure.
- Kept the existing SPDD workflow figure.
- Added an OpenSPDD sync / bidirectional-flow figure.

### Chapter V
- Added a TDAD pipeline redraw.
- Added a Constitutional SDD hierarchy / traceability redraw.
- Added a comparative matrix of protected specification profiles.

## Files changed

- `work/theory-writing/chapters/I_unit_of_analysis.md`
- `work/theory-writing/chapters/II_agentic_session_trace.md`
- `work/theory-writing/chapters/III_intent_spec_contract_adr.md`
- `work/theory-writing/chapters/IV_spdd_specification_lifecycle.md`
- `work/theory-writing/chapters/V_protected_specification_profiles.md`
- `content/assets/theory-images/MANIFEST.md`
- seven new local theory image assets under `content/assets/theory-images/`

## Visual policy outcome

This pass deliberately mixed three visual modes:
- existing local assets where the repository already had a strong source-backed image,
- source-backed redraws where the source logic was helpful but the chapter needed a cleaner local presentation,
- synthetic explanatory figures where the chapter’s own synthesis was the main thing to communicate.
