# Codebase readiness and context files note

Дата: 2026-06-07  
Статус: selected note before skeleton v4.  
Связанные части плана: VI, VIII, XII.  
Глубина: medium.

## Роль в AI-driven SDLC

Эта заметка удерживает важную поправку: эффективность агента зависит не только от модели и не только от количества контекста. Она зависит от состояния кодовой базы как рабочей среды: тестов, инструкций, CI, метрик, наблюдаемости, setup, архитектурной ясности and качества контекстных файлов.

## Источники

- AI Codebase Maturity Model.
- Agent READMEs.
- Developer-provided context / Cursor rules studies.
- Evaluating AGENTS.md.
- Codex/Claude/GitHub docs on repo instructions.
- Старые материалы про “кодовая база как контекстный интерфейс”.

## Основная мысль

Контекстные файлы — это не магические подсказки. Они становятся configuration-like artifacts. Их надо поддерживать, проверять and ограничивать.

Важная отрицательная поправка: more context is not automatically better. Лишние или устаревшие требования могут снижать успешность задачи and increase cost.

## Артефакты

- `AGENTS.md`;
- Cursor rules;
- Agent README;
- setup/run commands;
- codebase readiness note;
- project conventions;
- quality gates summary;
- local developer environment instructions.

## Внутренний workflow

```text
project state → context file → agent interpretation → action → evidence → update context or remove stale guidance
```

## Failure modes

1. **Context overload.** Агент получает слишком много правил.
2. **Stale instructions.** Файл описывает старый проект.
3. **Hidden non-functional gaps.** Security/performance/reliability absent from context files.
4. **Instruction conflict.** Rules conflict across files.
5. **Agent compliance with bad context.** Агент следует неверной инструкции.

## Где в theory

- Part VI: project as agent interface.
- Part VIII: environment and instructions before execution.
- Part XII: context cleanup / context debt.

## Что писать в финальном тексте

Не “создайте AGENTS.md”. А:

> Контекстный файл становится частью рабочей среды. Он помогает только если он точен, поддерживается and связан с проверками. Иначе он превращается в ещё один источник дрейфа.
