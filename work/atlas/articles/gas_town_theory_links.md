# gas_town — theory links

Статус после Final: теория синхронизирована с фактической статьёй. Здесь нет `C5/A10 sync pending`; внутренние обозначения заменены публичными различениями внутри статьи.

## Как статья входит в общую теорию

Gas Town используется как граничный случай после Persistent Work Graph и рядом со средой исполнения. Статья не доказывает всю теорию заново. Она показывает, что долговечный рабочий граф сам по себе не организует флот: нужны роли, очереди, восстановление, наблюдаемость, сервисная работа и человеческие решения.

## Current semantic links

| Theory question | Gas Town answer in article | Reverse contribution to theory |
|---|---|---|
| Что должно пережить сессию? | Beads/PWG-подобное состояние: узлы, зависимости, gates, claim, handoff, prime, memory. | Durable state нужен не только для восстановления контекста, но и для координации нескольких исполнителей. |
| Когда роль или фаза становится реальной? | Mayor, Polecat, Witness, Refinery, Deacon/Dogs имеют смысл, когда меняют допустимое следующее действие. | Process language без state transition превращается в имитацию процесса. |
| Где граница среды исполнения? | Worktree/session изолирует действие, но не решает readiness, acceptance и lifecycle closure. | Runtime events должны быть связаны с PWG/state before becoming work-state transitions. |
| Чем наблюдение отличается от свидетельства? | Dashboard, Problems View, telemetry и mail помогают видеть флот, но сами не закрывают работу. | Visibility не равна acceptance; evidence depends on promised result. |
| Кто может действовать, а кто завершает? | Polecat/Refinery/Witness/Deacon могут выполнять или готовить переходы; human/authorized verdict закрывает риск, merge, release или product decision. | Agentic action must be separated from authority to complete. |
| Как ремонтировать lifecycle после сбоя? | Prime, recovery hooks, handoff, cleanup and service agents restore safe continuation. | Repair is a lifecycle function, not a retry of the same session. |

## Связь с public entry после P22

- H1 и первые секции теперь идут от практической проблемы: один чат, одно рабочее дерево и ручное наблюдение перестают держать работу.
- Contract/minimal frame появляется после pressure ladder, поэтому теория не перегружает вход.
- Финальная таблица остаётся обратным мостом к атласу, а не prerequisite для чтения статьи.

## Theory-link blockers

Нет отдельных theory blockers. Оставшиеся blockers относятся к публикации: external images, source freshness and final density/style pass.
