# A4 composition / visual / style repair report

Дата: 2026-06-11.

## Оценка до repair

A4 уже выполнял основную задачу: показывал PWG как механизм продолжимого рабочего состояния и проводил границу с трекерами задач, Beads, durable execution, CRDT/STORM, Task Master и Gas Town. Содержательный статус был ближе к `ready_with_known_debts`, чем к сырому черновику.

Основные проблемы:

1. **Визуальный перегруз.** В основном тексте было 10 `<figure>`, почти все с классом `figure-candidate`, то есть основной фрагмент всё ещё содержал следы рабочего реестра фигур.
2. **Служебная подпись к реальному asset.** Подпись к `beads-task-graph-memory.svg` рассказывала о восстановлении локальной схемы и локальном файле, а не о смысле иллюстрации для читателя.
3. **Английский связующий слой.** В прозе оставались формулы вроде `graph theater`, `false completion`, `wrong authority`, `handoff`, `recovery`, `evidence packages` там, где точный английский термин не был нужен.
4. **Плохая метафора.** Формула про «хвост жизненного цикла» была стилистически слабой и противоречила обновлённым правилам человеческого технического стиля.
5. **Риск ухода в technical atlas.** Подробные схемы gate lifecycle, prime/handoff/recovery, lifecycle cleanup и parallel source work начинали превращать A4 в техническую карту PWG, хотя задача фрагмента — удержать теоретическую границу механизма.

## Применённые изменения

- A4 сокращён с 10 inline-фигур до 4.
- В основном тексте оставлены:
  - `fig-a4-pwg-minimal-node` как `local_image_asset` с нормальной публичной подписью;
  - `fig-a4-readiness-gate-owner` как нетривиальная синтетическая таблица;
  - `fig-a4-source-state-machine` как документно-специфическая синтетическая таблица;
  - `fig-a4-boundary-map` как центральная boundary-таблица.
- Сняты с inline или объединены в другие фигуры: opening failure diagram, ready queue, gate lifecycle, prime/handoff/recovery, parallel source work, runtime-vs-work-state, CRDT/STORM limit, cleanup tail, object lifecycle, evidence-before-done, authority boundaries and related variants.
- Подпись к Beads image asset очищена от служебного текста.
- Английские служебные формулы заменены русскими: имитация графа, устаревший граф, ложное завершение, ошибка полномочий, проверяемый пакет, передача работы, восстановление, очистка/архивирование.
- Основной аргумент сохранён: PWG остаётся механизмом продолжимого состояния работы, а не трекером задач, декомпозицией задач, долговечной средой исполнения, слоем согласования общего состояния или Gas Town.

## Оценка после repair

- Рабочая ценность: примерно **8.2/10**.
- Публикационная готовность: примерно **7.4/10**.
- Статус: `ready_with_known_debts`.

Оставшиеся долги:

- решить судьбу английских lifecycle-статусов (`ready/blocked/done`, `waiting gate`, `completed with evidence`, `cleaned/archived`) в публикационной версии;
- возможно вынести подробные lifecycle/gate/prime/cleanup схемы в technical atlas;
- при общей композиции проверить, не дублирует ли A4 часть B2, где PWG раскрывается глубже как anchor contribution.


## Повторный repair после выбора слабых фрагментов

По сравнению repair-отчётов A4 остался одним из двух самых слабых фрагментов по явной публикационной готовности. Повторный проход был направлен не на новый source pass, а на остаточный language/lifecycle repair.

В основном A4 заменены слабые формулы: “Ложное завершение” → “преждевременное закрытие”; `gates` объяснены как контрольные барьеры (`gates`) только при первом точном упоминании Beads; `cleanup`, `organizational OS`, `provenance`, `STORM-like mediator` переведены в русскую рабочую речь там, где они не являются обязательными source terms. Lifecycle-цепочка теперь дана по-русски, а не как длинная англоязычная status-line. Статус остаётся `ready_with_known_debts`, но прежний lifecycle/status blocker снят. Детали: `work/theory-writing/reports/WEAKEST_A2_A4_SECOND_REPAIR_REPORT.md`.
