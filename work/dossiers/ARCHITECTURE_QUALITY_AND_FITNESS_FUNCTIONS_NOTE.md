# Architecture quality and fitness functions note

Дата: 2026-06-07  
Статус: selected note before skeleton v4.  
Связанные части плана: III, VIII, X, XII.  
Глубина: medium-high.

## Роль

Этот слой был подтверждён Stage 0.12 как важный residual gap. Архитектурные качества нельзя растворять между ADR, specification and tests.

## Источники

- ATAM / quality attribute scenarios.
- Architecture evaluation / tradeoff analysis.
- Fitness functions / evolutionary architecture.
- ArchUnit / architecture tests.
- LLM-assisted architecture evaluation.
- ADR violation detection sources.

## Различение

- ADR: why a decision was taken.
- Specification: desired behavior and constraints.
- Quality attribute scenario: quality the architecture must preserve.
- Fitness function: check that gives feedback about that quality.
- Architecture test: executable guardrail.
- Tradeoff/risk record: why one quality was prioritized over another.

## Почему важно для агентов

Агент может сделать локально рабочее изменение, но ухудшить:

- слойность;
- модульность;
- зависимость;
- deployability;
- performance tradeoff;
- security boundary;
- modifiability;
- architecture decision compliance.

Green unit tests may not catch that.

## Артефакты

- quality attribute scenario;
- architecture constraint;
- utility tree / quality priority;
- architecture fitness function;
- architecture test;
- layer/dependency/cycle rule;
- fitness result;
- architecture drift note;
- stale fitness function note.

## Где в theory

- Part III: introduce quality attribute scenario / architecture constraint.
- Part VIII: executable architecture constraints.
- Part X: named subsection `Архитектурные качества как проверяемые ограничения`.
- Part XII: architecture drift and maintenance.

## Failure modes

1. Quality attributes stated but not checked.
2. Fitness functions stale or gameable.
3. Architecture tests too narrow.
4. LLM suggests architecture fix without context.
5. Tradeoff hidden inside code diff.

## Формула

> Архитектурное качество — это не “ещё один тест”. Это способ удержать свойства системы, которые локально корректный diff может незаметно разрушить.
