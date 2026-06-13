# Ledger: dossier-backed article set for concept-first atlas target plans

Статус: рабочий ledger для meta-package.  
Основание: `work/theory-writing/WORKING_DOCUMENTS_MAP.md`, `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md`, `work/decisions/ADR-0011-concept-first-technical-atlas.md`, `work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_ORIENTATION.md` и фактическое содержимое `work/dossiers/`.  
Текущий статус: `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md`, C5 and A10 доступны в post-import repo state. Ledger не расширяет набор статей внешним поиском и берёт только dossier-backed набор, уже перечисленный в карте документов как активные методологические досье для теории и технического атласа.

## 1. Known dossier-backed set

| Article id | Working title | Dossier path | Dossier exists | Preliminary article tier | Target-group plan output path | Preliminary readiness | Known sync debts |
|---|---|---|---|---|---|---|---|
| `spdd_method` | SPDD / OpenSPDD | `work/dossiers/SPDD_METHOD_DOSSIER.md` | yes | `core concept / method article` | `work/atlas/target-group-plans/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | `C5/A10 available`; manufactury-plan present; human review recommended |
| `persistent_work_graph` | Persistent Work Graph / Beads | `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | yes | `core concept article` | `work/atlas/target-group-plans/persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | `C5/A10 available`; manufactury-plan present; human review recommended |
| `gas_town` | Gas Town | `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | yes | `core concept / organizational article` | `work/atlas/target-group-plans/gas_town_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | `C5/A10 available`; manufactury-plan present; human review recommended; normalized from `gas_town_beads` |
| `adr_method` | ADR as method / decision memory | `work/dossiers/ADR_METHOD_DOSSIER.md` | yes | `method article` | `work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | `C5/A10 available`; manufactury-plan present; human review recommended |
| `spec_kit_method` | Spec Kit | `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md` | yes | `method / tool-form article` | `work/atlas/target-group-plans/spec_kit_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | `C5/A10 available`; manufactury-plan present; human review recommended |
| `kiro_specs` | Kiro Specs | `work/dossiers/KIRO_SPECS_DOSSIER.md` | yes | `tool/form article` | `work/atlas/target-group-plans/kiro_specs_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | `C5/A10 available`; manufactury-plan present; human review recommended |
| `tdad_comparative` | TDAD | `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md` | yes | `method article` | `work/atlas/target-group-plans/tdad_comparative_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | `C5/A10 available`; manufactury-plan present; human review recommended |
| `constitutional_sdd` | Constitutional SDD | `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md` | yes | `method article` | `work/atlas/target-group-plans/constitutional_sdd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | `C5/A10 available`; manufactury-plan present; human review recommended |
| `gsd_open_gsd` | GSD / Open GSD | `work/dossiers/GSD_METHOD_DOSSIER.md` | yes | `method article` | `work/atlas/target-group-plans/gsd_open_gsd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | `C5/A10 available`; manufactury-plan present; human review recommended |
| `bmad_method` | BMAD | `work/dossiers/BMAD_METHOD_DOSSIER.md` | yes | `method article` | `work/atlas/target-group-plans/bmad_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` | `ready_for_package_manufacture_after_manual_review` | `C5/A10 available`; manufactury-plan present; human review recommended |

## 2. Post-import context

`work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` присутствует в текущем repo state. C5 и A10 также доступны как read-only context для будущих article-writing packages. Старые стандартные долги `C5 sync pending`, `A10 sync pending` и `missing manufactury-plan provenance` закрыты на уровне ledger; будущие планы должны фиксировать только конкретные article-level долги, если они возникнут.

## 3. Unplanned dossiers

Проверка `work/dossiers/` нашла ровно те 10 досье, которые включены в known set выше:

```text
ADR_METHOD_DOSSIER.md
BMAD_METHOD_DOSSIER.md
CONSTITUTIONAL_SDD_DOSSIER.md
GAS_TOWN_METHOD_DOSSIER.md
GSD_METHOD_DOSSIER.md
KIRO_SPECS_DOSSIER.md
PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
SPDD_METHOD_DOSSIER.md
SPEC_KIT_METHOD_DOSSIER.md
TDAD_COMPARATIVE_DOSSIER.md
```

Unplanned dossiers: none.

## 4. Shared preliminary debts

- C5/A10 are available as read-only context in the current repo state. Future article packages should verify article-specific links and reader routing, not keep default sync-pending notes.


## 5. Path convention correction

G03 зафиксировал явную конвенцию для atlas article target-group plans: `work/atlas/target-group-plans/<article_id>_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`. Ledger обновлён под эту конвенцию; прежняя общая template-конвенция `work/theory-writing/target-group-plans/` не используется для этой meta-package ветки.

## S05 readiness updates

- `spdd_method`: status set to `ready_for_package_manufacture_after_manual_review`; executor package manufacture is allowed after manual review of article contract/tier/boundaries and C5/A10 context.

- `bmad_method`: status set to `ready_for_package_manufacture_after_manual_review`; executor package manufacture is allowed after manual review of article contract/tier/boundaries and C5/A10 context.

- `persistent_work_graph`: status set to `ready_for_package_manufacture_after_manual_review`; executor package manufacture is allowed after manual review of article contract/tier/boundaries and C5/A10 context.

- `gas_town`: status set to `ready_for_package_manufacture_after_manual_review`; executor package manufacture is allowed after manual review of article contract/tier/boundaries and C5/A10 context.


### 2026-06-12 — persistent_work_graph plan repair and package manufacture

- Plan repaired after manual review.
- Package built: `work/atlas/packages/persistent_work_graph_ATLAS_ARTICLE.zip`.
- Status: `ready_for_package_manufacture_after_manual_review`; package smoke-tested.


### 2026-06-12 — gas_town plan repair and package manufacture

- Plan repaired after manual review.
- Package built: `work/atlas/packages/gas_town_ATLAS_ARTICLE.zip`.
- Status: `ready_for_package_manufacture_after_manual_review`; package smoke-tested.


## 2026-06-12 — remaining atlas plans repaired and packages built

- `spec_kit_method` → `work/atlas/packages/spec_kit_method_ATLAS_ARTICLE.zip` (self-contained; 63 files).
- `kiro_specs` → `work/atlas/packages/kiro_specs_ATLAS_ARTICLE.zip` (self-contained; 64 files).
- `constitutional_sdd` → `work/atlas/packages/constitutional_sdd_ATLAS_ARTICLE.zip` (self-contained; 63 files).
- `tdad_comparative` → `work/atlas/packages/tdad_comparative_ATLAS_ARTICLE.zip` (self-contained; 64 files).
- `gsd_open_gsd` → `work/atlas/packages/gsd_open_gsd_ATLAS_ARTICLE.zip` (self-contained; 66 files).
- `bmad_method` → `work/atlas/packages/bmad_method_ATLAS_ARTICLE.zip` (self-contained; 68 files).
