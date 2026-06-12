# Отчёт: решение о концептуально-техническом атласе

Дата: 2026-06-11

## Решение

Технический атлас больше не трактуется как узкое техническое приложение. Он становится концептуально-техническим слоем: набором самостоятельных, связных и статей с опорой на источники о конкретных методологиях, механизмах и инструментальных формах.

Теория остаётся поперечным синтезом AI-driven SDLC. Атлас даёт другой путь чтения: от конкретной концепции к общей рамке. Это важно для читателей, которые хотят понять SPDD, PWG, Gas Town / Beads, TDAD, Spec Kit, Kiro, BMAD, GSD, ADR или соседний методологический профиль, не собирая материал из разных глав теории.

## Почему прежняя граница была недостаточной

Прежняя граница защищала теорию от выноса смысла в приложение, но была слишком жёсткой. Если атлас хранит только команды, файлы, скриншоты и источниковые заметки, читателю приходится сначала восстанавливать концепцию из разных мест теории, а затем отдельно прикладывать её к техническим деталям. Такой атлас теряет самостоятельную ценность.

## Новое правило

Контролируемое повторение тезисов из теории допустимо внутри статьи атласа, если оно нужно для самостоятельного понимания конкретной концепции.

Запрещены три перекоса:

- ссылаться из теории на атлас вместо объяснения механизма;
- механически копировать всю общую теорию в каждый раздел атласа;
- складывать технические детали, скриншоты и команды без связного объяснения концепции.

## Обновлённые файлы

```text
START.md
protocols/rules/theory-rebuild-rules.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
work/approved-ai-sdlc-plan.md
work/approved-decisions.md
work/decisions/ADR-0009-skeleton-v4-2-story-boundary-and-technical-atlas.md
work/decisions/ADR-0010-persistent-work-graph-deep-mechanism-anchor.md
work/decisions/ADR-0011-concept-first-technical-atlas.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CORE_NODES_TARGET_GROUP_PLANS_GENERATION_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CORE_NODES_WRITING_PACKAGES_BUILD_TARGET_GROUP_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
```

## Последствие для C5

C5 больше не должен объяснять жёсткое разделение «смысл в теории, детали в атласе». Он должен объяснить две траектории чтения:

- от теории к концепциям: поперечный SDLC-синтез;
- от конкретной концепции к общей рамке: самостоятельные статьи атласа на основе досье, источниковой фактуры, механики, визуальных материалов и ограничений.

Статус: `ready_for_next_fragment` для планирования C5, с оговоркой, что будущие пакеты атласа должны строиться по новому правилу концептуально-технического слоя.
