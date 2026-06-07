# Обновлённый следующий рабочий план

Дата: 2026-06-05
Статус: обновлено после фиксации baseline-restore rule для SPDD и Gas Town.

## 1. Новая последовательность

```text
Stage 0. Утверждённый design v2
Stage 1. Skeleton v2 для Theoretical_synthesis_rebuilt.md
Stage 2. Specification-zone dossiers
Stage 2.5. Anchor baseline restoration: SPDD and Gas Town from old site baseline
Stage 3. Parts I–III draft
Stage 4. Part IV / SPDD standalone draft
Stage 5. Part V / neighboring specification regimes draft
Stage 6. Anti-catalog audit Parts III–V
Stage 7. Context / Delegation / Execution drafts
Stage 8. Gas Town baseline restoration + dossier + standalone draft
Stage 9. Evidence / Governance / Lifecycle-tail drafts
Stage 10. Whole-document synthesis audit
```

## 2. Stage 1: skeleton v2

Создать:

```text
current/Theoretical_synthesis_rebuilt.md
planning/SKELETON_V2_AI_SDLC_SPDD_SPEC_DEEP.md
reports/SKELETON_V2_CHECKS.json
```

Skeleton должен включать:

- все 12 частей;
- управляющий тезис каждой части;
- функцию каждой части;
- anchor/medium/contrast/drop placeholders;
- links to dossiers;
- explicit warning not to use expanded theory as form.

## 3. Stage 2: specification-zone dossiers

Создать:

```text
cases/SPDD_DOSSIER.md
cases/SPEC_KIT_DOSSIER.md
cases/KIRO_DOSSIER.md
cases/TDAD_DISAMBIGUATION_AND_DOSSIER.md
cases/CONSTITUTIONAL_SDD_DOSSIER.md
reports/SPECIFICATION_CLUSTER_COMPARISON_MATRIX.md
reports/SPECIFICATION_CLUSTER_SOURCE_GAPS.md
```

Codex/agent task should not write final prose yet. It should extract, reconstruct and compare.


## 3A. Stage 2.5: Anchor baseline restoration before deep-case writing

This stage is mandatory before writing SPDD or Gas Town final prose.

Create:

```text
baseline_extracts/SPDD_FROM_SITE_BASELINE.md
baseline_extracts/GAS_TOWN_FROM_SITE_BASELINE.md
drafts/part_iv_spdd_seed_unchanged.md
drafts/part_ix_gas_town_seed_unchanged.md
reports/SPDD_BASELINE_STRUCTURE_MAP.md
reports/GAS_TOWN_BASELINE_STRUCTURE_MAP.md
reports/SPDD_BASELINE_DETAIL_INVENTORY.md
reports/GAS_TOWN_BASELINE_DETAIL_INVENTORY.md
reports/ANCHOR_BASELINE_RESTORE_CHECKS.json
```

Rules:

- Extract SPDD and Gas Town from the old site/document baseline, not from the latest expanded synthesis.
- Preserve each extracted section unchanged in the seed files.
- Use latest expanded synthesis only as supplementary quarry after baseline restoration.
- Do not compress details by default.
- Any loss, move or condensation of baseline material requires an explicit report and human gate.

## 4. Stage 3: Parts I–III draft

Purpose:

- set voice;
- establish AI-driven SDLC as non-corporate lifecycle frame;
- ground theory in real session evidence;
- prepare specification zone without starting SPDD too early.

## 5. Stage 4: SPDD standalone draft

Must use:

- `baseline_extracts/SPDD_FROM_SITE_BASELINE.md`;
- `drafts/part_iv_spdd_seed_unchanged.md`;
- SPDD dossier;
- latest expanded synthesis only as supplementary quarry.

Must preserve high detail. Must avoid turning SPDD into universal recipe. Must include anti-degradation check against the old site baseline.

Required outputs:

```text
drafts/part_iv_spdd_draft.md
reports/part_iv_spdd_source_coverage.md
reports/part_iv_spdd_depth_audit.md
reports/SPDD_ANTI_DEGRADATION_CHECK.md
```

## 6. Stage 5: neighboring specification regimes

Must use all four dossiers and final comparison matrix.

Required outputs:

```text
drafts/part_v_spec_regimes_draft.md
reports/part_v_anti_catalog_audit.md
reports/part_v_source_depth_audit.md
```

## 7. Stage 6: Anti-catalog audit Parts III–V

Audit questions:

1. Is Part III a clean theoretical entry, not a mini catalog?
2. Does Part IV let SPDD breathe?
3. Does Part V have one governing line?
4. Are Spec Kit/Kiro/TDAD/Constitutional SDD deeply enough developed?
5. Are sources subordinated to lifecycle logic?
6. Does the document return from specification to context cleanly?

## 8. Human gates

Additional mandatory gates for SPDD and Gas Town:

- approve SPDD baseline extract before adaptation;
- approve Gas Town baseline extract before adaptation;
- review anti-degradation reports before either section is marked complete.

Required decisions for user:

1. Approve skeleton v2.
2. Approve specification cluster comparison matrix.
3. Approve SPDD depth before full Part IV draft.
4. Approve Part V anti-catalog structure.
5. Approve whether any of Spec Kit/Kiro/TDAD/Constitutional SDD should be moved down from main text to source map after dossier review.

## 9. Codex prompt shape

A single Codex task should execute a full stage, not ask the user to run repeated micro-prompts.

Example:

```text
Run Stage 2: specification-zone dossiers.
Do not write final theory prose.
Read the source map, old baseline, expanded quarry, SPDD experiment, approved design v2, and source links.
Create all required dossier files, comparison matrix, source gaps report and checks.json.
Stop only when all artifacts exist or when a true human decision is required.
```
