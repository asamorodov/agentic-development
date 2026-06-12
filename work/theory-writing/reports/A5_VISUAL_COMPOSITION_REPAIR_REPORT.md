# A5 visual/composition repair report

Дата: 2026-06-11.

## Повод

После обсуждения `A5_process_methodologies_synthesis.md` пользователь принял основные долги фрагмента: визуальный слой был тяжёлым, часть фигур дублировала прозу, подпись к Gas Town asset оставалась служебной, а структура всё ещё могла читаться как линейная шкала процесса. Нужно было сохранить источник и несущий аргумент, но сделать фрагмент более чистым как теоретический узел.

## Изменения в A5

Обновлены:

- `work/theory-writing/fragments/A5_process_methodologies_synthesis.md`;
- `work/theory-writing/fragments/A5_figure_candidates.md`;
- `work/theory-writing/fragments/A5_open_questions.md`;
- `work/theory-writing/fragments/A5_degradation_and_duplication_audit.md`;
- `work/theory-writing/fragments/A5_source_usage.md`;
- `work/theory-writing/fragments/A5_story_anchor_map.md`.

Основной A5 теперь содержит 4 inline-фигуры вместо 7:

1. `fig-a5-gsd-bmad-pwg-questions`;
2. `fig-a5-gsd-bmad-light-state`;
3. `fig-a5-method-pwg-organization-stack`;
4. `fig-a5-process-imitation-boundary`.

Из основного фрагмента вынесены в candidate/deferred слой:

- `fig-a5-process-carrier-ladder` — усиливала чтение A5 как линейной шкалы зрелости;
- `fig-a5-personal-memory-to-pwg` — дублировала абзац о Mark Erikson;
- `fig-a5-minimal-process-decision` — полезна как Fieldbook/technical atlas material, но избыточна в основном теоретическом фрагменте.

## Композиционный ремонт

A5 переписан вокруг разных рабочих разрывов, а не вокруг подъёма от простого процесса к сложному. GSD, BMAD, PWG и Gas Town теперь явно разведены как разные ответы на разные проблемы:

- продолжение работы после очистки контекста или следующего дня;
- разделение продуктового, архитектурного и исполнительского суждения;
- остановка, передача, блокировка и восстановление единицы работы;
- координация множества агентов в постоянной организационной среде.

Блок Reversa/OpenSpec/AgentSPEX сжат и переписан как проверка границы понятия: восстановить поведение, сохранить изменение, описать ход агента. Он больше не должен читаться как мини-обзор трёх дополнительных методологий.

## Визуальный и языковой ремонт

- Подпись к Gas Town asset переписана как публичная подпись без “восстановленная локальная схема” и без локального пути в основном объяснении.
- Реальный Gas Town asset сохранён как `<img>` и не превращался в текстовую схему.
- Формула “носитель состояния против театра процесса” заменена на “работающий процесс против имитации процесса”.
- В основном тексте убраны заметные гибриды вроде `recovery-петля`, `structured progress`, служебные asset-pass подписи и лишние англоязычные labels там, где русский вариант точнее.
- Сохранены точные имена инструментов, файлов, команд, фаз и полей: `research.md`, `plan.md`, `STATE.md`, `SPEC.md`, `bmad-spec`, `bd prime`, `hooks`, `mailboxes`, `handoffs`, `merge queue`, `scheduler/capacity governor` и другие source-specific names.

## Package consistency

B-пакеты были пересобраны после A5 repair, потому что их payload содержит обновляемые read-only файлы карты и writing plan. Прямого встраивания полного A5 в B1/B2/B3 package payload не обнаружено, но пересборка нужна для консистентности карты рабочих документов и отчётов.

Smoke-test после пересборки:

- `B1_SPDD_CONTRIBUTION_AND_LIMITS.zip`: `unzip -t`, first runner transition, second runner transition — OK.
- `B2_PWG_CONTRIBUTION.zip`: `unzip -t`, first runner transition, second runner transition — OK.
- `B3_GAS_TOWN_BEYOND_PWG.zip`: `unzip -t`, first runner transition, second runner transition — OK.

## Regression audit

- Баланс `<figure>` / `</figure>` в основном A5: 4 / 4.
- Количество `<img>`: 1.
- Локальный Gas Town asset существует: `content/assets/theory-images/gastown-architecture.svg`.
- В основном A5 нет служебных подписей “Восстановленная…” и “Локальный файл”.
- В основном A5 нет `recovery-петля`, `structured progress`, `fig-a5-process-theater-boundary` и формулы “театр процесса”.
- Markdown-ссылки основного A5 ведут на публичные первоисточники, новых источников не добавлялось.

## Readiness

Статус A5: `ready_with_known_debts`.

Фрагмент можно использовать как вход для следующих B/C-работ. Оставшиеся долги: обычная финальная проверка ссылок, возможный отдельный image-candidates pass по BMAD/Gas Town и композиционная сверка при сборке полной теории.
