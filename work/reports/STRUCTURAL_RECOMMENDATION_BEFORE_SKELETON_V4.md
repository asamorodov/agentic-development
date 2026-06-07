# Structural recommendation before skeleton v4

Дата: 2026-06-07  
Статус: recommended composition strategy for skeleton v4.  
Связанные файлы:
- `work/approved-ai-sdlc-plan.md`;
- `work/reports/STRUCTURAL_COHERENCE_ALTERNATIVES_FOR_PARTS_VI_XII.md`;
- `work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md`;
- `work/reports/UPDATED_PLAN_QUALITY_AUDIT.md`.

## Recommended decision

Do not change the top-level part list now.

Use approved plan v4 as architecture, but build skeleton VI–XII through **narrative tensions**, not artifact classes.

## Why

The current top-level sequence is still right:

```text
context → delegation → execution → Gas Town → evidence → completion → tail
```

The problem is not the sequence. The problem is how each part may be written internally.

## Skeleton rule

For Parts VI–XII each subsection must be one of these:

1. A lifecycle tension.
2. A transition from one kind of work to another.
3. A comparative mechanism.
4. A deep anchor section already approved.

It must not be just an artifact label.

Bad:

```text
## AGENTS.md
## ADR
## Test data
## SBOM
```

Good:

```text
## Где живёт состояние задачи, если оно больше не помещается в чат
## Когда процесс становится устанавливаемым артефактом
## Почему “тесты прошли” ещё не значит, что изменение доказано
## Кто имеет право завершить изменение
## Как хвост lifecycle возвращает опыт в среду
```

## Recommended VI–XII skeleton headings

### VI. Контекст и рабочее состояние: проект как интерфейс агента

1. Что агент должен знать, чтобы не действовать вслепую.
2. Где живёт состояние задачи.
3. Почему больше контекста не значит лучше.
4. Как кодовая база становится рабочей поверхностью.
5. Как проект показывает агенту владельцев, правила and runnable path.
6. Где контекст начинает устаревать.

### VII. Делегирование: выбор режима работы, а не выбор инструмента

1. Когда достаточно разговора.
2. Когда сначала нужен research or plan.
3. Когда нужен spec-first.
4. Когда процесс становится устанавливаемым артефактом.
5. GSD/BMAD as process-artifact spectrum.
6. Когда агенту надо отказать.

### VIII. Исполнение: среда агента, harness, tools, permissions

1. Возможность действовать.
2. Граница действия.
3. Воспроизводимость действия.
4. Исполняемые ограничения.
5. След действия.
6. Где environment itself becomes debt.

### IX. Gas Town / Beads

Keep as approved deep case with baseline restore.

### X. Свидетельства, тесты, ревью и качество доказательства

1. Почему summary агента не является свидетельством.
2. Почему один тип свидетельства не подходит всем изменениям.
3. Поведенческая правильность.
4. Граничная правильность.
5. Архитектурная сохранность.
6. Надёжность доказательства: данные, среда, oracle.
7. Социальная проверка.
8. Трасса выполнения.

### XI. Завершение, governance и внешний контур

1. Агент может выполнить работу, но не владеть её завершением.
2. Кто обязан смотреть.
3. Кто может принять.
4. Кто отвечает за выпуск.
5. Внешний контур and AI-generated contributions.
6. Восстановимость завершения.

### XII. Хвост lifecycle

1. Release feedback.
2. Incident feedback.
3. Drift feedback.
4. Supply/security feedback.
5. User-facing memory.
6. Возврат в specs, tests, policies, context files and skills.

## How to use comparative cases

Use comparisons inside parts, not as new top-level structure:

- GSD/BMAD in VII.
- Harness/Sandvault/platform tools in VIII.
- Architecture fitness/contracts/test data in X.
- SASE/open-source policies/CODEOWNERS in XI.
- Incident/stale ADR/context cleanup in XII.

## What to update next

The next artifact should be:

```text
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
```

It should follow this structural recommendation, not simply copy the full approved plan list.
