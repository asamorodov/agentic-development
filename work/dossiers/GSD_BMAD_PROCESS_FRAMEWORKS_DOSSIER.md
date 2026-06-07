# GSD / BMAD process frameworks dossier

Дата: 2026-06-07  
Статус: selected dossier before skeleton v4.  
Связанные части плана: VI, VII, возможно XII.  
Глубина: medium.

## Роль в AI-driven SDLC

GSD and BMAD важны не как новые спецификационные методологии уровня SPDD and не как продуктовые платформы уровня Codex/GitHub/Claude. Они показывают другой слой: **рабочий процесс как устанавливаемый артефакт**.

Если SPDD отвечает на вопрос “как превратить намерение в управляемый спецификационный контур”, то GSD/BMAD отвечают на вопрос “как организовать повторяемую работу с агентом, чтобы контекст, роли, план, исполнение and проверка не оставались импровизацией”.

## Основные источники и материалы

- `From Prompt to Process` — сравнительная рамка frameworks по specification, context, roles, execution, validation, portability.
- GSD / Open GSD materials — context engineering, externalized state, fresh-context execution, discuss/plan/execute/verify/ship.
- BMAD Method docs — role-based AI-driven development framework, specialized agents, guided workflows, planning/architecture/implementation.
- Reversa / OpenSpec / AgentSPEX — соседние материалы для process-as-artifact and workflow specification.
- Внутренние файлы:
  - `work/reports/AGENTIC_FRAMEWORKS_COVERAGE_AUDIT.md`;
  - `work/source-expansion/stage_0_6/agentic_frameworks/`;
  - `work/source-expansion/stage_0_7/workflow_specification/`;
  - `work/approved-ai-sdlc-plan.md`.

## Сравнение функций

### GSD

Главная функция: бороться с распадом контекста and long-session drift.

Сильные элементы:

- внешнее состояние;
- small checkable plans;
- fresh-context subagents;
- verify step before closure;
- portability across coding assistants.

Роль в теории: Part VI/Part VII, как пример process continuity.

### BMAD

Главная функция: role-based organization of AI-assisted work.

Сильные элементы:

- specialized agents;
- guided workflows;
- analysis/planning/architecture/implementation;
- scale-adaptive planning.

Роль в теории: Part VII, как пример агентской методологии с ролями.

### Reversa

Главная функция: восстановление operational specifications from legacy systems.

Роль: medium/short bridge to Part VI/XII; важен для migration and implicit context recovery.

### OpenSpec / AgentSPEX

Главная функция: workflow specification and portability.

Роль: short/medium support for agent workflow specification, not deep case.

## Что этот слой объясняет лучше других

Он показывает, что в AI-driven SDLC иногда недостаточно набора документов. Нужен установленный процесс: какие роли есть, какие файлы состояния создаются, как task переходит от обсуждения к плану, от плана к исполнению, от исполнения к проверке.

## Внутренний workflow

Для process/framework layer useful generic workflow:

```text
context setup → role/process selection → plan/state artifact → execution loop → verification → handoff/ship → process repair
```

## Артефакты

- state file;
- context file;
- role definition;
- process step definition;
- task breakdown;
- verification step;
- handoff note;
- agent workflow specification.

## Human decision points

- когда брать лёгкий режим, а когда framework;
- когда framework creates more overhead than value;
- whether to promote GSD/BMAD to larger section;
- whether to let agent modify process files.

## Failure modes

1. **Framework as catalog.** Перечисление GSD/BMAD/OpenSpec/Reversa without lifecycle role.
2. **Process overkill.** Heavy framework for small reversible change.
3. **Role theater.** Agents receive names/roles, but no artifacts/evidence.
4. **Context fossilization.** External state becomes stale and trusted too much.
5. **Portability illusion.** Workflow spec claims portability but depends on specific tool behavior.

## Где в rebuilt theory

- Part VI: project state / externalized context.
- Part VII: process as installed artifact.
- Part VIII: agent workflow specification only as execution-control artifact.
- Part XII: process repair if framework state becomes stale.

## Что не сжимать

- GSD ≠ Spec Kit.
- BMAD ≠ Gas Town.
- Process framework ≠ platform docs.
- Medium-depth only until source dossiers prove more.

## Что уходит в Handbook / Fieldbook

- Practical comparison table.
- When to use GSD-like lightweight process.
- When BMAD-like role workflow is useful.
- Templates for state/context files.
