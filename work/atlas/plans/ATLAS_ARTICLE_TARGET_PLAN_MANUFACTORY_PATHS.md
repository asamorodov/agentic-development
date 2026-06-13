# Conventions: выходные пути meta-package для atlas article target plans

Статус: обязательные локальные conventions для последующих шагов текущего meta-package.  
Основание: G03, `ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_LEDGER.md`, blueprint статей атласа и правила target-group plans.  
Ограничение: `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` отсутствует в текущем snapshot; conventions ниже берут приоритет из рабочего листа G03.

## 1. Основная конвенция

Все target-group plans для статей концептуально-технического атласа создаются здесь:

```text
work/atlas/target-group-plans/<article_id>_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

Это локальная конвенция данной meta-package ветки. Она важнее общей исторической конвенции `work/theory-writing/target-group-plans/` для обычных фрагментов теории, потому что G03 явно задаёт отдельный atlas namespace.

## 2. Reports и step notes

Для каждой статьи создаётся итоговый report:

```text
work/atlas/plans/reports/<article_id>_target_plan_manufacture_report.md
```

Промежуточные notes по шагам S01–S05 создаются в той же директории:

```text
work/atlas/plans/reports/<article_id>_S01_article_contract.md
work/atlas/plans/reports/<article_id>_S02_initial_target_plan.md
work/atlas/plans/reports/<article_id>_S03_plan_repair.md
work/atlas/plans/reports/<article_id>_S04_buildability_audit.md
work/atlas/plans/reports/<article_id>_S05_final_plan_review.md
```

Имена notes могут уточняться по содержанию, но должны сохранять префикс `<article_id>_Sxx_`, чтобы runner and reviewer могли видеть порядок работы.

## 3. Final matrices

Общие матрицы meta-package:

```text
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_READINESS_MATRIX.md
work/atlas/plans/ATLAS_ARTICLE_BOUNDARY_MATRIX.md
```

`READINESS_MATRIX` показывает готовность каждого article target-group plan к будущей package manufacture: готовность входов, наличие exact paths, source/asset/readiness debts, C5/A10 sync status and blockers.

`BOUNDARY_MATRIX` фиксирует границы между соседними статьями и опасные пары: SPDD / Spec Kit / Kiro / Constitutional SDD, PWG / Beads / Gas Town, GSD / BMAD / process profiles, TDAD / evidence / testing, ADR / lifecycle repair / specification, а также любые дополнительные пересечения, обнаруженные в S03–S05.

## 4. Article ids from ledger

Текущий ledger использует следующие `article_id`:

```text
spdd_method
persistent_work_graph
gas_town_beads
adr
spec_kit_method
kiro_specs
tdad
constitutional_sdd
gsd
bmad
```

Для них действуют следующие target plan paths:

```text
work/atlas/target-group-plans/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/gas_town_beads_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/adr_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/spec_kit_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/kiro_specs_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/tdad_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/constitutional_sdd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/gsd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/bmad_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

## 5. Consistency rule

Начиная с G03, все новые рабочие листы, reports, matrices and target-group plans должны использовать paths из этого файла. Если ранний ledger или note содержит старый путь, он должен быть исправлен на `work/atlas/target-group-plans/<article_id>_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`.

Meta-package по-прежнему не создаёт article-writing packages and не пишет статьи. Target-group plan — это build-time plan for future package, а не черновик самой статьи.

- `tdad_comparative` target plan: `work/atlas/target-group-plans/tdad_comparative_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`

- `adr_method` target plan: `work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`

- `gsd_open_gsd` target plan: `work/atlas/target-group-plans/gsd_open_gsd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
