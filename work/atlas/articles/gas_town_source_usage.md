# gas_town — source usage

Статус после Final: companion-файл синхронизирован с текущей статьёй `gas_town.md`. Это не полный список всех просмотренных материалов, а карта источников, которые реально поддерживают опубликованную фактуру статьи.

## Основная опора статьи

| Источник | Где используется в статье | Что именно поддерживает | Граница доверия |
|---|---|---|---|
| [Gas Town README](https://github.com/gastownhall/gastown) | вступление; delivery loop; observability | Gas Town как система для нескольких кодовых агентов; базовая петля `You → Mayor → Convoy → Agent → Hook → completion → summary`; Problems View как текстовая/табличная поверхность проблем | Использовать как проектный источник, но не как доказательство зрелости или универсальности системы. |
| [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) | вступление; town/rig; роли; hook/pinned bead; внешние фигуры | ранняя/хаотичная/дорогая природа системы; intended audience; two-tier Beads flow; worker roles; pinned bead, role beads, agent beads | Авторский источник, важен для концепта и исходных изображений; не подменяет документацию текущей реализации. |
| [Gas Town Docs](https://docs.gastownhall.ai/) и [Gas Town Reference](https://docs.gastownhall.ai/reference/) | роли, маршрутизация, observability | Mayor/Hub, справочная поверхность системы, routing/reference details | Проверить свежесть перед публикацией, если статья превращается в точное product reference. |
| [Gas Town architecture docs](https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md) | town/rig split | town-level и rig-level состояние, архитектурная организация | Поддерживает архитектурный тезис, но не должен расширять статью в дизайн-документ. |
| [Mayor role template](https://github.com/gastownhall/gastown/blob/main/internal/templates/roles/mayor.md.tmpl) | delivery loop | дисциплина `filed and slung`, `bd create`, `gt sling` | Внутренний шаблон; использовать только как техническую опору роли Mayor, не как публичный API-контракт. |
| [Gas Town mail protocol](https://github.com/gastownhall/gastown/blob/main/docs/MAIL_PROTOCOL.md) | delivery loop; status feedback | `POLECAT_DONE`, `MERGE_READY`, `MERGED` и типизированная почтовая обратная связь | Сохранять как пример протокольных статусов, не как исчерпывающий список. |
| [Gas Town CHANGELOG](https://github.com/gastownhall/gastown/blob/main/CHANGELOG.md) | очередь, backpressure, observability, recovery | `gt queue`, dispatcher, heartbeat, spawn pressure, `FIX_NEEDED`, `awaiting_verdict`, Dashboard, telemetry, spawn storm, merge queue | Версионно чувствительный источник; перед публикацией стоит проверить актуальность названий и формулировок. |
| [Gas Town Scheduler design](https://github.com/gastownhall/gastown/blob/main/docs/design/scheduler.md) | queue/backpressure | различие ready work и safe dispatch; `gt sling --queue`, `max_polecats`, `batch_size`, `spawn_delay`, circuit breaker | Дизайн-документ; сохранять как источник для границы queue/scheduler, но проверить свежесть перед выпуском. |

## Beads как нижний слой, не самостоятельная статья

| Источник | Где используется | Что поддерживает | Граница доверия |
|---|---|---|---|
| [Beads Documentation](https://gastownhall.github.io/beads/) и [Beads Architecture](https://gastownhall.github.io/beads/architecture) | нижний слой; small-process boundary; нерешённые границы | Beads как Dolt-backed task tracker; source of truth; границы применения Beads в больших/командных сценариях | Не расширять в обзор Beads. В статье нужны только функции, объясняющие Gas Town. |
| [Beads Quick Start](https://gastownhall.github.io/beads/getting-started/quickstart), [Beads CLI Reference](https://gastownhall.github.io/beads/cli-reference), [`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime) | нижний слой; recovery | `bd ready`, `--explain`, `bd update --claim`, `bd dep add`, `bd prime` | Команды оставлены как технические якоря, а не как tutorial. |
| [Beads Routing](https://gastownhall.github.io/beads/multi-agent/routing) | town/rig routing | prefix-based routing, route map, debug routing | Используется для адресации и риска неправильного графа работы. |
| [Beads Workflows](https://gastownhall.github.io/beads/workflows), [Beads Molecules](https://gastownhall.github.io/beads/workflows/molecules), [Beads Wisps](https://gastownhall.github.io/beads/workflows/wisps), [`bd gate`](https://gastownhall.github.io/beads/cli-reference/gate) | decomposition | Formula, Molecule, Wisp, Gate как язык разбиения и удержания работы | Не превращать раздел в workflow-engine статью. |
| [Beads Codex Integration](https://gastownhall.github.io/beads/integrations/codex) | recovery | hook marker и восстановление контекста после compaction/разрыва | Поддерживает recovery boundary, не общий совет по Codex. |
| [Beads Troubleshooting](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md) | infrastructure risk | backup, `doctor`, debug flags, sandbox mode, sync/hash mismatch risks | Техническая опора инфраструктурной секции. |
| [Beads Releases](https://github.com/gastownhall/beads/releases) и [DoltHub: Common Beads Classic Workflows](https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/) | sync/infrastructure risk | gated release/migration risk, Dolt sync/workflow tradeoffs | Версионно чувствительно; перед публикацией проверить, что формулировка о release/context не устарела. |

## Ограниченные и неканонические источники

| Источник | Использование | Ограничение |
|---|---|---|
| [Gas Town discussion #363](https://github.com/gastownhall/gastown/discussions/363) | operation-log gap и возможность `append-only operation log` | Это обсуждение/предложение, не текущая реализованная гарантия. В статье оно явно названо пробелом. |
| [HN: Welcome to Gas Town discussion](https://news.ycombinator.com/item?id=46458936) | сигнал внешнего восприятия: перегрузка понятиями, баги, merge/review bottleneck | Неканонический источник. Не использовать для фактов о реализации; оставить только как perception signal или удалить перед публикацией. |

## Источники, которые не должны расширять статью

- Материалы Beads вне перечисленных команд/механизмов не должны превращать текст в Beads manual.
- Ролевые и тематические фигуры Gas Town вне текущих двух external placeholders не должны превращать статью в role glossary или UI-tour.
- C5/A10 больше не являются `sync pending`: соответствующая теория уже перенесена в финальный theory-link section и small-process transfer section как самодостаточные различения.

## Текущие source blockers

1. Проверить свежесть версионно чувствительных деталей: CHANGELOG, Scheduler design, Beads Releases, DoltHub sync workflow.
2. Решить, остаётся ли Hacker News ссылка в публичной статье или уходит только в source notes.
3. Перед публикацией убедиться, что Medium/GitHub/docs ссылки доступны и не требуют иных формулировок для прав/изображений.
