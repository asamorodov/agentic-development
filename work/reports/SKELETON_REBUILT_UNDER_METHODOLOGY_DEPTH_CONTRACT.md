# Skeleton rebuilt under methodology depth contract

Дата: 2026-06-07  
Статус: отчёт о применении methodology depth contract к skeleton v4.

## Что изменилось

Пользователь утвердил новую ось глубины: некоторые методологии не должны становиться deep anchors уровня SPDD/Gas Town, но всё равно должны получить protected depth.

На этой основе:

1. Создан `work/reports/METHODOLOGY_DEPTH_CONTRACT.md`.
2. Создан `work/decisions/ADR-0008-protected-methodology-profiles.md`.
3. Обновлён `work/approved-ai-sdlc-plan.md` addendum.
4. Перестроен `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`.

## Главный результат

Part V and Part VII now explicitly contain protected methodology profiles.

### Part V

Protected specification methodology profiles:

- Spec Kit;
- Kiro Specs;
- TDAD A/B;
- Constitutional SDD.

Plus comparative synthesis:

```text
SPDD / Spec Kit / Kiro / TDAD / Constitutional SDD
```

### Part VII

Protected process methodology profiles:

- GSD / Open GSD;
- BMAD.

Adjacent forms:

- Reversa;
- OpenSpec / AgentSPEX.

Plus comparative synthesis:

```text
Spec Kit / GSD / BMAD / Reversa / OpenSpec / AgentSPEX / Gas Town
```

## What remains

Before writing Parts V and VII, create methodology dossiers:

```text
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
```

Then create:

```text
work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md
```

## Quality judgment

This change solves the user concern: GSD/BMAD/Kiro/Spec Kit/Constitutional SDD are no longer vulnerable to becoming shallow three-page summaries.

Risk remains: Part V and VII will become heavier. The mitigation is to write profiles with required structure, then comparative synthesis, rather than expanding every source equally.
