# Gas Town — системное методологическое досье

Статус: системно-интеграционная версия после прохода 11 с исправленным справочным хвостом. Верхний слой досье приведён к системной карте методологии; источники и кандидаты на иллюстрации восстановлены внутри этого досье в единых разделах. Фактура из предыдущих проходов не удалялась: подробные сведения сохранены в тематических разделах и в локальном source/image registry этого же файла.

Основание: `GAS_TOWN_METHOD_DOSSIER.md` из pass 11.

Граница досье: это рабочий source buffer для будущей теории, не финальная глава. Текст должен помогать модели и человеку видеть устройство метода, а не историю накопительных проходов.

## Устройство досье


- **Главный центр:** Beads как устойчивый граф работы и плоскость данных/управления.

- **Надстройка Gas Town:** Town/Rig/roles, tmux/worktrees, hooks, agents, handoff и наблюдение.

- **Грамматика работы:** MEOW, molecules, formulas, gates, wisps, GUPP.

- **Исполнение:** queue, scheduler, dispatch, pressure checks, FIX_NEEDED/awaiting_verdict, convoys.

- **Долговечность:** Dolt-backed state, recovery hooks, `bd prime`, routing, mail, dashboards и operation log gaps.

- **Границы:** стоимость флота агентов, merge/sync, ответственность, перегрузка понятий и local-first limits.

## Системно-интеграционная карта Gas Town

Gas Town в этом досье следует читать не как набор ролей с внутренней терминологией, а как систему управления длительной агентной работой. Центральный элемент — Beads: устойчивый граф задач, зависимостей, ownership, маршрутизации и восстановления. Поверх него строятся роли, пространства, scheduler, queue, hooks, recovery, наблюдаемость и внешние интерфейсы.

Рабочая карта метода в досье устроена так:

1. **Проблема и статус.** Здесь объясняется, почему Gas Town появляется как ответ на ограничения одного агента, одного контекстного окна и ручной координации.
2. **Beads как substrate.** Это центральный раздел. Здесь собраны Dolt-backed state, ready queue, dependencies, `bd prime`, `bd gate`, routing, multi-agent coordination, debug/troubleshooting и цена persistent work substrate.
3. **Грамматика работы.** Здесь находятся MEOW, GUPP, molecules, formulas, gates, wisps и planning fuel: как работа превращается в переносимые объекты, а не остаётся в голове агента.
4. **Пространства и роли.** Здесь разложены Town, Rig, Mayor, Crew, Polecats, Refinery, Witness, Deacon, Dogs и их функции в системе.
5. **Исполнение и back-pressure.** Здесь собраны scheduler, queue, dispatch, convoys, pressure checks, FIX_NEEDED, pinning, handoff и conflict prevention.
6. **Восстановление и наблюдаемость.** Здесь находятся Codex hooks, compaction recovery, telemetry, dashboard, shadow database, locks and cleanup/compaction risks.
7. **Платформенные границы и риски.** Здесь собраны limits, local-first constraints, sync/merge conflicts, future architecture, cost of agent fleets and responsibility bottlenecks.

Ссылки на источники остаются рядом с фактами. Источники, поисковые формулировки и кандидаты на иллюстрации собраны в единых справочных разделах внутри этого досье, чтобы основной текст не превращался в хронологию проходов.

## Краткая рабочая карта

Gas Town в этом досье нужно читать через **Beads as central плоскость данных и управления**. Без Beads Gas Town выглядит как набор ролей вокруг tmux/worktrees; с Beads становится видно главное: work, identity, memory, dependencies, hooks, handoffs, recovery и coordination вынесены из chat/session context в persistent task substrate. Поэтому Beads остаётся внутри Gas Town-главы как центральный подраздел, а не отделяется в самостоятельную историю.


## Проблема, назначение и статус Gas Town

### Сводный синтез

Gas Town в этом досье следует читать не как «несколько агентов в tmux» и не как набор остроумных ролей, а как попытку построить рабочую среду для длительной параллельной агентной разработки. Его центральная проблема: один агент и один markdown-план ещё могут удерживаться человеком вручную, но при нескольких агентах, ветках, рабочих деревьях, сессиях, задачах и handoff простая память чата перестаёт быть рабочей поверхностью. Нужен внешний substrate, который хранит work state, зависимости, ownership, готовность к исполнению, события, сообщения, восстановление и историю. В Gas Town эту роль выполняет Beads, а поверх него строятся роли, scheduler, queue, hooks, recovery, dashboards и человеческая поверхность управления ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04), [Gas Town GitHub](https://github.com/gastownhall/gastown), [Beads docs](https://gastownhall.github.io/beads/)).

Системная картина Gas Town складывается из пяти связанных слоёв.

1. **Persistent work graph.** Beads хранит задачи, зависимости, ready queue, identities, memories, gates, history и Dolt-backed state. Это не просто issue tracker рядом с кодом: для агента Beads становится рабочей базой, через которую можно узнать, что готово, что заблокировано, кто чем владеет, что было найдено во время реализации и какой контекст нужно восстановить перед продолжением ([Beads architecture](https://gastownhall.github.io/beads/architecture), [Beads CLI reference](https://gastownhall.github.io/beads/cli-reference)).
2. **Addressing and decomposition layer.** Routing по префиксам, MEOW, GUPP, formulas, molecules, gates и wisps превращают работу в адресуемые и раскладываемые объекты. Это важно: флот агентов нельзя координировать только словами в prompt-е; рабочие единицы должны иметь идентификаторы, типы, зависимости, состояния и правила передачи.
3. **Runtime and role layer.** Town, Rig, Mayor, Crew, Polecats, Refinery, Witness, Deacon и Dogs — не персонажи, а функции операционной среды. Они распределяют видимость, выполнение, ревью, восстановление, эскалацию, очистку и сервисные действия. Роли понятны только после Beads: без persistent substrate они были бы декоративной терминологией.
4. **Capacity, queue and recovery layer.** Scheduler, dispatch, pressure checks, `FIX_NEEDED`, `awaiting_verdict`, convoys, pinning, handoff, Codex hooks, `bd prime`, compaction recovery, shadow database, locks, cleanup/compaction и circuit breaker показывают, что многоагентная разработка требует back-pressure и repair mechanics, а не только больше параллельных сессий ([Gas Town changelog](https://github.com/gastownhall/gastown/blob/main/CHANGELOG.md), [Beads troubleshooting](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md)).
5. **Observability and responsibility layer.** Dashboard, telemetry, quality gates, refinery strategy, mail, operation-log gaps and external critique показывают ограничение Gas Town: persistent work graph делает работу видимой, но не снимает ответственность человека за ревью, принятие решений, merge/sync и стоимость флота агентов.

Главный итог: Gas Town не доказывает, что флот агентов сам по себе масштабирует разработку. Он доказывает более узкую и полезную вещь: если разработчик пытается управлять параллельными, временными и stateful агентами, ему нужен маленький operating system for work — queryable work graph, event-driven context rehydration, typed handoff, queue, heartbeat, recovery, capacity limits and explicit worker identity. Beads делает работу достаточно долговечной, чтобы поверх неё могли появиться scheduler, witness, recovery и human control surface; но Beads сам становится инфраструктурой, которую нужно версионировать, синхронизировать, диагностировать, чинить и ограничивать.

Для будущей теории Gas Town важен как дальний край пространства AI-driven SDLC. Большинству разработчиков не нужна полная версия Gas Town; но почти всем зрелым агентным процессам постепенно понадобятся его отдельные примитивы: external work state, ready/blocked, ownership, compact rehydration, safe resume, source precedence, cleanup rules, observable handoff and explicit responsibility. Для нашего многопроходного документного процесса это особенно прямой урок: недостаточно множить `pass`-файлы и `status.json`. Если проходы должны переживать timeout, compaction, рестарт и частичное выполнение, у них должны быть адресуемые рабочие зоны, строгая модель владения, понятное состояние, восстановление контекста, диагностика и fallback для sandboxed runs.

### Уточнение статуса Gas Town

Gas Town нужно описывать как multi-agent workspace manager / orchestration system, а не просто как «много Claude Code в tmux». README формулирует это как систему для Claude Code, GitHub Copilot, Codex, Gemini и other AI agents with persistent work tracking; ключевой механизм — не держать context in session, а persist work state in git-backed hooks ([Gas Town GitHub](https://github.com/gastownhall/gastown)). Medium-пост усиливает это: Gas Town помогает с потерей состояния, отслеживанием кто что делает и ручным управлением большим числом однотипных coding agents ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

Критически важно сохранить источникную оговорку: Gas Town не зрелый enterprise orchestrator. В Medium-посте он описан как свежий, дорогой, хаотичный, hands-on-the-wheel system, рассчитанный на пользователей, которые уже дошли примерно до multi-agent CLI / hand-managed 10+ agents stage. Это не анти-пиар, а часть метода: throughput покупается ценой шума, стоимости, потерь и необходимости постоянного человеческого управления ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

### Роль в AI-driven SDLC

Gas Town находится в верхней, тяжёлой зоне AI-driven SDLC: долгие задачи, несколько агентов, несколько веток, рабочие деревья, очередь слияния, восстановление сессий, почта, события, устойчивые идентичности, обслуживающие агенты и человеческая поверхность управления. Он показывает не “prompt engineering”, а организационную среду, где работа должна переживать сессии и быть управляемой через внешнее состояние. Корпусный фрагмент: [§41](../../content/Theoretical_synthesis.md#25-pochemu-gas-town-zasluzhivaet-otdelnogo-razdela), источник: [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04).

Gas Town в текущей теории логически продолжает раздел о том, что большая часть сложности агентской системы находится не в модели. Хорошая модель в плохой среде может быть бесполезной или опасной; более слабая модель в хорошей среде может надёжно выполнять узкий класс задач, если получает правильный контекст, ограниченные инструменты, быстрые проверки и понятные границы. Разборы Claude Code и AI Harness Engineering в теории используются как общий фон: сложность находится в permissions, context management, tool routing, error recovery, session compaction, state storage, telemetry, subagents, skills, hooks и policies. Корпусный фрагмент: [§39](../../content/Theoretical_synthesis.md#23-bolshaya-chast-slozhnosti-agentskoy-sistemy-nahoditsya-ne-v-modeli).

### Проблема, которую решает Gas Town

Проблема начинается ещё до собственно Gas Town: markdown-план удобен, пока задача одна, исполнитель один и горизонт короткий. Когда появляется несколько агентов, несколько веток, долгие задачи и фоновая работа, простой план перегружается. У него нет нативного понятия блокера, атомарного закрепления, графа зависимостей, истории статуса, почтового ящика для передачи сообщений между агентами и простого ответа на вопрос «какие задачи готовы сейчас?». Корпусный фрагмент: [§40](../../content/Theoretical_synthesis.md#24-graf-zadach-kak-vneshnyaya-pamyat-agenta).

Граф задач даёт другую форму: задачи, решения, открытые вопросы, блокеры, PR, проверки и передача состояния связаны зависимостями, конфликтами, принадлежностью к более крупной работе и происхождением. У каждой рабочей единицы появляется состояние: готова ли она к выполнению, взята ли кем-то, заблокирована ли, требует ли ревью или человеческого решения. Корпусный фрагмент: [§40](../../content/Theoretical_synthesis.md#24-graf-zadach-kak-vneshnyaya-pamyat-agenta).

Такой граф отвечает на вопросы, критичные при работе с несколькими агентами: что можно делать прямо сейчас, что заблокировано, кто уже работает над задачей, какие изменения зависят друг от друга, где нужен человек, какие решения были приняты раньше, что агент должен вспомнить перед продолжением, какие результаты конфликтуют. Корпусный фрагмент: [§40](../../content/Theoretical_synthesis.md#24-graf-zadach-kak-vneshnyaya-pamyat-agenta).


## Центральный подраздел: Beads как substrate Gas Town


### Troubleshooting как свидетельство сложности persistent work substrate

Документация Beads `TROUBLESHOOTING.md` полезна не как справочник команд, а как свидетельство того, что persistent work graph приносит собственную эксплуатационную сложность. Там описаны случаи, когда `bd` показывает ноль задач, хотя база содержит данные: причина может быть в подключении к неправильному Dolt server/database, старом `metadata.json` или shadow database. Для исправления предлагается проверять `.beads/metadata.json`, список баз в Dolt server, прямой `SELECT COUNT(*) FROM issues` и `bd doctor --server`.[^beads-troubleshooting-shadow]

Другой важный блок связан с восстановлением после сбоев. При повреждении Dolt journal после перезапуска документация не советует “почистить lock-файл”. Наоборот, она явно предупреждает, что удаление внутренних файлов Dolt вроде `noms/LOCK` может привести к невосстановимой порче данных; безопасный путь зависит от того, актуален ли remote, и может включать перенос corrupt directory, `bd bootstrap --dry-run`, `bd bootstrap --yes`, `bd stats`, а при сомнении — forensic inspection через `dolt fsck`.[^beads-troubleshooting-corruption]

Для Gas Town это важнее, чем кажется. Beads делает работу агентов долговечной, но долговечность превращает ephemeral agent memory в настоящую базу состояния. У такой базы появляются shadow state, stale server cache, circuit breaker, corrupt journal, remote sync и orphan handling. Поэтому Beads нельзя описывать только как “удобный task tracker для агентов”. Это operational substrate, который нужно диагностировать, ремонтировать и сопровождать.

[^beads-troubleshooting-shadow]: Beads docs, [`TROUBLESHOOTING.md`](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md), разделы `bd shows 0 issues but the database has data` и configured server unreachable.
[^beads-troubleshooting-corruption]: Beads docs, [`TROUBLESHOOTING.md`](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md), разделы Dolt journal corruption, database locked, circuit breaker и server mode.

### Ready work, зависимости и agent confusion: где Beads нуждается в дисциплине

В troubleshooting-документации отдельно описан слой `Ready Work и Dependencies`. Если `bd ready` ничего не показывает, хотя open issues есть, нужно проверять `bd blocked`, `bd dep tree <issue-id>`, удалять лишние `blocks` dependencies или перестраивать структуру зависимостей. Документация подчёркивает, что только `blocks` влияет на ready work; `related`, `parent-child` и `discovered-from` имеют другую семантику.[^beads-troubleshooting-ready]

Это добавляет к досье важную границу: ready queue работает только тогда, когда dependency graph достаточно дисциплинирован. Если агент создаёт duplicate issues, цепляет loose relationships как blockers или строит слишком сложные dependency trees, Beads не магически упрощает работу. Он делает проблему видимой и даёт команды диагностики: `bd dep tree`, `bd dep cycles`, `bd merge`, labels for loose relationships. Для будущего многопроходного документного процесса это переносится прямо: если мы заведём graph/state layer для проходов, надо заранее разделять hard blockers, soft links и provenance links, иначе очередь готовой работы станет ненадёжной.

[^beads-troubleshooting-ready]: Beads docs, [`TROUBLESHOOTING.md`](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md), разделы Ready Work и Dependencies, circular dependency errors, agent creates duplicate issues и agent gets confused by complex dependencies.

### Beads routing: работа адресуется по префиксу, а не по памяти агента

Gas Town Reference уточняет практический слой, который раньше был недораскрыт. Команды `bd` маршрутизируются по префиксу issue ID: `gp-*` уходит в Beads конкретного rig-а, `hq-*` — в town-level Beads для Mayor mail и cross-rig coordination, `wyv-*` — в другой rig. Карта маршрутов хранится в `~/gt/.beads/routes.jsonl`, а диагностика может включать `BD_DEBUG_ROUTING=1 bd show <id>`.[^gt-reference]

Это важная деталь для Gas Town как глубокий якорь. Если Beads — центральный substrate, то Gas Town добавляет слой маршрутизации: агенту не нужно каждый раз понимать, в какой базе лежит задача. Он работает с идентификатором, а среда ведёт его к правильному графу работы. Для будущего многопроходного документного процесса это переносится как требование: если появятся несколько рабочих зон, артефакты проходов и состояние задач должны иметь ясное адресное пространство. Иначе агент начнёт читать не тот status, продолжать не тот проход или писать результат в чужое досье.

[^gt-reference]: Gas Town Docs, [Reference](https://docs.gastownhall.ai/reference/), разделы Beads Routing, rig config, layered configuration и Beads commands.

### Внешнее положительное чтение: Beads как состояние вне контекстного окна

Разбор Eric Koziol полезен тем, что показывает, какая идея считывается снаружи без знания всей внутренней терминологии Gas Town. Он выделяет Beads как атомарную единицу работы и как устойчивое внешнее состояние задачи за пределами контекстного окна агента. Эта формулировка частично устарела относительно нынешнего Dolt-backed Beads, но переносимый тезис остаётся важным: перезапуск агента, заполненный контекст или crash не должны стирать состояние работы.[^gt-koziol]

В досье это лучше использовать как внешний интерпретирующий источник, а не как технический baseline. С технической стороны текущий Beads уже описывается через Dolt-backed state. Но для объяснения читателю формула “состояние вне контекстного окна” очень удачна: она сразу показывает, почему Beads должен быть центральным подразделом Gas Town.

[^gt-koziol]: Eric Koziol, [“Exploring Gas Town”](https://embracingenigmas.substack.com/p/exploring-gas-town), section on Beads as persistent externalized task state.

### Beads solves “flat issue tracker thrashing” через ready queue

Beads quickstart даёт хороший micro-example, которого не хватало в досье: flat tracker показывает open items, и агент может сразу выбрать blocked task. Beads строит dependency graph и computes a очередь готовых задач: `bd ready` показывает только работу without active blockers; `bd ready --explain --json` объясняет, почему задача заблокирована. Это не просто удобный список задач, а минимальный planning substrate для агентов: модель получает не “всё открытое”, а **semantically executable next work**. [Beads Quick Start](https://gastownhall.github.io/beads/getting-started/quickstart)

Для Gas Town это центрально: масштабирование не должно означать “запусти ещё 20 агентов”. Сначала нужна структура, которая предотвращает wasted cycles. Beads очередь готовых задач является более сильной формой state than markdown checklist, because it can compute blocked/ready status from explicit dependencies. [Beads Quick Start](https://gastownhall.github.io/beads/getting-started/quickstart)

### Идентификаторы, иерархия и dependencies as anti-collision mechanics

Quickstart также уточняет нижний слой граф работы: issue IDs are hash-based to prevent collisions when multiple agents/branches work concurrently; large features can use hierarchical issues; dependencies produce dependency trees; `bd blocked`, `bd stats` и `bd dep tree` make state queryable. [Beads Quick Start](https://gastownhall.github.io/beads/getting-started/quickstart)

Это полезно для будущей теории: устойчивый граф работы is not only memory. It is collision avoidance, dependency reasoning, handoff target, и progress query interface. В многопроходном документном процессе аналогом должны быть not only pass files, but durable task/pass/state graph with explicit blockers и next-ready computations.

### Claude integration: `bd prime` as token-bounded rehydration protocol

Claude Code integration adds another useful contrast: session starts with `bd prime`, which injects about 1–2k tokens of context, и after compaction runs refresh again. Essential commands are deliberately JSON-first: create issues with descriptions, use `bd ready --json`, claim work with `bd update --claim --json`, close with reason, push before session end. [Beads Claude Code integration](https://gastownhall.github.io/beads/integrations/claude-code)

Это уточняет economic side: Beads не пытается подсовывать агенту весь граф работы. Он подаёт compact operational context и lets the agent query precise commands. Для многопроходного документного процесса это важнее, чем ещё один большой `discourse.md`: нужен `prime`-like компактный контекст + queryable state.

### Multi-agent coordination: routing, pinning и cross-repo dependencies

Beads multi-agent docs фиксируют три переносимых механизма: routing by pattern to target repo, cross-repo dependencies и work assignment/handoff. Work can be pinned to a specific agent with `bd pin ... --for agent-1 --start`, и `bd hook --agent agent-1` shows pinned work. [Beads Multi-Agent Coordination](https://gastownhall.github.io/beads/multi-agent)

Для Gas Town это даёт более точное чтение Crew/Polecats/GUPP: роли сами по себе не решают координацию; координация появляется, когда work objects have routing, ownership, dependencies и agent-facing hooks. Это также explains why Beads belongs at the center of Gas Town dossier.

### External architecture reading: Bead, Dolt и tmux as three strata

Bill de hÓra’s short analysis is useful as an external reading, not as primary documentation. He frames Gas Town around three abstractions: Bead as versioned/queryable data record, Dolt as transactional backing/query support, и tmux as agent runtime. He also describes layered memory: ephemeral sessions, sandboxes backed by git, и permanent agent identity backed by bead, with mailboxes reminiscent of actor systems. [Bill de hÓra on Gas Town](https://dehora.net/journal/2026/2/initial-thoughts-on-welcome-to-gas-town)

This is useful for theory because it strips away theme names. Gas Town can be described as: runtime surface + versioned work substrate + agent identity/mailbox layer. That is clearer than treating Mayor/Crew/Polecats as only colorful roles.

### DoltHub view: Beads started as agent memory, then moved toward Dolt-backed structured state

DoltHub’s “A Day in Gas Town” gives an external historical detail: Beads began as a coding-agent memory system using Git plus SQLite to version structured data, и Dolt was suggested as a better backend. It also states the practical problem: после PR review or later rework, the original coding-agent session may be gone, so a new session needs durable task memory. [DoltHub: A Day in Gas Town](https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/)

This helps explain why Beads is not just issue tracking. It addresses session loss, delayed review, и restart discontinuity — exactly the problems that become worse when agents operate over hours/days rather than one chat turn.

### Beads command surface: не issue tracker, а agent-facing рабочая система

Beads CLI reference for bd v1.0.5 lists 106 live top-level commands. Важны не только `create/list/show/update/close`, но и `ready`, `dep`, `mol`, `formula`, `prime`, `doctor`, `gate`, `history`, `mail`, `memories`, `remember`, `graph`, `query`, `stale`, `status/statuses`, `supersede`, `worktree`, `backup`, `dolt`, integrations (`github`, `gitlab`, `jira`, `linear`, `notion`) и recovery/migration commands. Источник: [Beads CLI Reference](https://gastownhall.github.io/beads/cli-reference). Это уточняет центральный тезис: Beads в Gas Town — не tiny local todo list, а типизированная рабочая основа with commands for readiness, dependency management, memory, messages, lifecycle и integrations.

### Agent ingestion surface: `bd init`, `bd setup`, `AGENTS.md`, `bd prime`

Beads README shows that `bd init` creates or updates `AGENTS.md` by default и can install project Claude/Codex integrations; supported setups include `bd setup codex`, `bd setup claude`, `bd setup cursor` и others. Minimal agent instructions explicitly say: run `bd prime` for рабочий процесс context и command guidance; use `bd ready`, `bd show`, `bd update --claim`, `bd close`; use `bd remember` for persistent project memory; do not use markdown TODO lists. Источник: [Beads README](https://github.com/gastownhall/beads). Для теории это очень важный detail: Beads работает не только как storage, but as **agent onboarding contract**. Он внедряет себя в тот файл/канал, который агент читает, и задаёт рабочую грамматику прямо на входе в сессию.

### Dolt рабочий процесс details: полезность и новая непрозрачность

DoltHub Common Beads Classic Workflows clarifies a current version shift: in v1.0.1 Beads issues are mastered in a Dolt database и are no longer written to JSONL files by default, although JSONL export remains available. Single-agent/default mode uses the registered Git remote as Dolt remote; `bd init` configures this и Dolt can push in the background. The same source notes opacity: users may not visually see changes on GitHub even though Beads data is preserved remotely. For multiple clones/parallel agents, shared remote visibility is useful but introduces synchronization/merge-conflict tradeoffs when several clones write to the same Beads database. Источник: [DoltHub Common Beads Classic Workflows](https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/).

Architecture docs explain why this shift matters technically: Dolt gives SQL queries, native version control, auto-committed writes, push/pull distribution и backup/restore preserving history; every `bd create` or update writes to Dolt immediately и auto-commits, while reads query local Dolt via SQL. Источник: [Beads Architecture](https://github.com/gastownhall/beads/blob/main/docs/ARCHITECTURE.md). Досье должно держать обе стороны: Dolt makes Beads much stronger as устойчивый граф работы, but less transparent than old JSONL-in-repo mental model for some users.

### Changelog evidence: dashboard, two-level beads и ephemeral polecats

Gas Town changelog 0.2.0 adds concrete maturity details: Convoy Dashboard with real-time activity monitoring, Refinery Merge Queue status, dynamic convoy status columns и 10-second auto-refresh; two-level Beads architecture with town-level `hq-*` и rig-level project-specific prefixes; multi-rig management; batch slinging; immediate recycling of Polecats after each work unit; и formula changes for ephemeral polecat lifecycle. Источник: [Gas Town CHANGELOG](https://github.com/gastownhall/gastown/blob/main/CHANGELOG.md). Это усиливает Gas Town as operational platform, not just conceptual article.

### Work graph: issue, dependency, ready queue и discovered work

Core Concepts уточняют структуру рабочих единиц: issues have hash-based or hierarchical IDs, type, priority, status, labels и dependencies. Dependency types include `blocks`, `parent-child`, `discovered-from`, и `related`; only hard `blocks` dependencies affect the очередь готовых задач ([Beads Core Concepts](https://gastownhall.github.io/beads/core-concepts)). Это важно: Beads не просто хранит список задач, а отличает blocking structure from provenance и soft association.

Для агентской работы особенно важен тип `discovered-from`: он позволяет сохранять work discovered during implementation как связанную, но не обязательно blocking задачу. В документации quick examples directly instruct agents to create discovered work with dependencies и to use JSON output for programmatic access ([Beads Documentation](https://gastownhall.github.io/beads/)). В будущей теории это можно связать с проблемой “agent found more work than the current pass should perform”: найденная работа не теряется и не раздувает scope текущего изменения.

### Dolt as источник истины, not JSONL as truth

Architecture page говорит, что Beads uses Dolt as its sole storage backend: a version-controlled SQL database with git-like branch/merge/diff/push/pull semantics. Every write auto-commits to Dolt history; `.beads/issues.jsonl` is useful as export/interchange, but not the full источник истины ([Beads Architecture](https://gastownhall.github.io/beads/architecture), [Beads GitHub](https://github.com/gastownhall/beads)). Это сильно уточняет переносимый урок: durable agent memory should not be only a markdown file or JSONL export if the process needs multi-agent merge, queries, recovery и history.

Важна и граница: docs explicitly warn Beads is not suitable for large 10+ teams, non-developers, real-time collaboration, cross-repository tracking or rich media attachments; for such cases they point back to GitHub Issues, Linear or Jira ([Beads Architecture](https://gastownhall.github.io/beads/architecture)). Поэтому в теории Beads нужно использовать как powerful developer-local substrate, not universal replacement for organizational issue trackers.

### Agent entry ritual: `bd prime`, `bd remember`, hooks и compaction recovery

Beads README gives a minimal agent instruction block: run `bd prime`, use `bd ready`, `bd show`, `bd update --claim`, `bd close`, use `bd remember` for persistent project memory, и do not create markdown TODO lists for task tracking ([Beads GitHub](https://github.com/gastownhall/beads)). This is almost a formal entry ritual for an agent: obtain current рабочий процесс context и memories, claim real work, record new memory in a structured place.

Codex integration turns that into lifecycle mechanics: `bd setup codex` installs a Beads skill, managed `AGENTS.md` guidance и native Codex hooks; `SessionStart` injects full `bd prime`, `PreCompact` checks memories-only context, `PostCompact` marks the need for refresh, и `UserPromptSubmit` injects `bd prime` once after compaction ([Beads Codex Integration](https://gastownhall.github.io/beads/integrations/codex)). Для нашего многопроходного документного процесса это особенно важно: context recovery после compaction/обрыва должен быть не “прочитай всё заново”, а lifecycle hook + compact priming.

### Beads как durable work database, а не “память агента” в общем смысле

Beads README и docs describe Beads as a distributed graph issue tracker for AI agents, powered by Dolt, replacing markdown plans with a dependency-aware graph for long-horizon tasks ([Beads README](https://github.com/gastownhall/beads), [Beads Architecture](https://gastownhall.github.io/beads/architecture)). Четвёртый проход уточняет: “memory” здесь не психологическая метафора. Это database-backed work substrate: issues, dependencies, metadata, gates, formulas, molecules, mail, agent identities и history become queryable objects.

Архитектурный документ Beads говорит, что Dolt is the источник истины; every write auto-commits to Dolt history; Dolt provides SQL queries, version control, branching, merge, diff, push/pull at database level; server mode supports concurrent agents, while embedded mode remains usable for CI/scripts/single-use scenarios ([Beads Architecture](https://gastownhall.github.io/beads/architecture)). Для нашей теории это сильнее, чем прежняя формулировка “git-backed issue tracker”: Beads brings **database semantics** into agent work, not just file persistence.

### Two-level Beads in Gas Town: town-level и rig-level state

Предыдущий проход уже ввёл two-tier Beads, но его нужно сделать центральным. Gas Town architecture distinguishes town-level Beads under `~/gt/.beads/` for cross-rig coordination, mayor mail и agent identity, и rig-level Beads inside each project for implementation work, merge requests и project issues ([Gas Town architecture docs](https://github.com/gastownhall/gastown/blob/main/docs/ARCHITECTURE.md), [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

Это не второстепенная деталь. Two-level Beads separates **control-plane coordination** from **implementation-plane work**. Для будущей теории это можно сравнить с нашим многопроходным документным процессом: если все run/status/pass artifacts лежат в одном плоском слое, диагностика и orchestration смешиваются. Gas Town показывает более зрелую форму: отдельная база для town-level orchestration и separate rig-level issue graphs.

### Command surface matters: `bd prime`, `bd gate`, `bd mail`, `bd mol`

В Gas Town/Beads важны не только сущности, но и команды, через которые агент обновляет/восстанавливает состояние. `bd prime` outputs essential Beads рабочий процесс context in AI-optimized markdown; it can output brief MCP reminders around ~50 tokens or full CLI output around 1–2k tokens, и is designed for Claude Code, Gemini CLI и Codex SessionStart hooks to prevent agents from forgetting Beads рабочий процесс after context compaction ([`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime)). Это прямо связано с экономикой нашего многопроходного документного процесса: durable state must be rehydrated cheaply, not by rereading full logs.

`bd gate` turns waits into first-class async conditions: human, timer, GitHub run, GitHub PR и bead gates. Gate issues can block another issue until resolved, и automatic checks can resolve or escalate gates depending on рабочий процесс status, PR merge status, timeout or target bead closure ([`bd gate`](https://gastownhall.github.io/beads/cli-reference/gate)). Это важный механизм для long-running agent orchestration: ждать CI или human review не надо держанием живого agent-thread; ожидание становится durable object.

`bd mail` и Gas Town’s mail protocol make inter-agent coordination an issue-graph operation. Gas Town mail messages are routed through Beads и can carry signals like `POLECAT_DONE`, `MERGE_READY` и `MERGED` between Polecats, Witness и Refinery ([Gas Town mail protocol](https://github.com/gastownhall/gastown/blob/main/docs/MAIL_PROTOCOL.md)). В теории это полезно как пример: agent communication should be inspectable work state, not only ephemeral chat text.

### Beads как data/control plane

Gas Town built on Beads: Medium прямо говорит, что alternate backend нет, а Beads является Universal Git-Backed data plane / control plane для всего, что происходит в Gas Town ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)). Beads README формулирует Beads как distributed graph issue tracker for AI agents, powered by Dolt; он заменяет markdown plans на dependency-aware graph, помогает агентам вести long-horizon tasks without losing context и добавляет commands вроде `bd ready`, `bd update <id> --claim`, `bd dep add`, `bd show`, `bd prime`, `bd remember` ([Beads GitHub](https://github.com/gastownhall/beads)).

Это уточняет, что Beads в Gas Town — не просто issue tracker. Он хранит work units, identities, mail, events, hooks, role beads, agent beads и ephemeral orchestration. В Medium-посте отдельно выделены rig-level beads и town-level beads; rig-level — project work, town-level — orchestration, patrols и one-shot workflows. Есть cross-rig routing по префиксам вроде `bd-` / `wy-`, чтобы команды Beads понимали, к какой базе относится issue ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

### Beads как минимальная механика внешней памяти работы

Beads в текущей теории — предшествующий и базовый слой для понимания Gas Town. [Yegge описывает Beads](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a) как универсальный Git-backed data plane, а в контексте Gas Town он фактически становится и control plane. Корпусный фрагмент: [§45](../../content/Theoretical_synthesis.md#29-beads-kak-sloy-dannyh-sloy-upravleniya-i-sloy-pochemu).

На уровне task graph Beads даёт конкретные команды. `bd ready` показывает задачи без открытых блокеров, `bd update --claim` закрепляет задачу за исполнителем, `bd dep add` связывает задачи, `bd remember` сохраняет проектную память. Эти команды важны не сами по себе, а как доказательство того, что память агента становится инструментом управления работой, а не пассивной базой заметок. Корпусный фрагмент: [§40](../../content/Theoretical_synthesis.md#24-graf-zadach-kak-vneshnyaya-pamyat-agenta), источник: [Introducing Beads](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a).

У Beads есть важная входная механика: память должна не только храниться, но и подаваться агенту в момент входа в работу. `bd remember` сохраняет проектную память, а `bd prime` выдаёт агенту рабочий контекст и устойчивые воспоминания при входе в задачу. В текущей теории это названо почти формальным ритуалом входа агента в проект: не «поищи сам, что важно», а «получи актуальную карту работы и памяти». Корпусный фрагмент: [§40](../../content/Theoretical_synthesis.md#24-graf-zadach-kak-vneshnyaya-pamyat-agenta).

Gas Town построен на Beads. Через него проходят рабочие единицы, идентичности, почта, события, хуки, role beads, agent beads, работа уровня rig и town. Корпусный фрагмент: [§45](../../content/Theoretical_synthesis.md#29-beads-kak-sloy-dannyh-sloy-upravleniya-i-sloy-pochemu), источники: [Introducing Beads](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a), [Beads GitHub](https://github.com/gastownhall/beads).

Beads добавляет слой «почему», которого обычно не хватает Git. Git хранит, что изменилось, где изменилось, кто изменил и как выглядит история коммитов. Но Git плохо хранит жизненный цикл причины: почему задача появилась, какие варианты обсуждались, что было отклонено, какой агент взял работу, где был блокер, почему решение передали дальше, как оно связано с другими задачами. Beads связывает изменение с причиной, блокерами, зависимостями, обсуждением, памятью и дальнейшим состоянием. Корпусный фрагмент: [§45](../../content/Theoretical_synthesis.md#29-beads-kak-sloy-dannyh-sloy-upravleniya-i-sloy-pochemu).

Для doc-first-разработки это почти прямой аналог слоя происхождения: код хранит результат, а граф задач хранит смысловую и операционную историю появления результата. Корпусный фрагмент: [§45](../../content/Theoretical_synthesis.md#29-beads-kak-sloy-dannyh-sloy-upravleniya-i-sloy-pochemu).



### Beads Classic после перехода на Dolt: режимы хранения и новые трения

DoltHub-разбор Beads v1.0.1 уточняет, что переход на Dolt изменил не только backend, но и пользовательскую модель. В classic single-agent режиме `bd init` использует зарегистрированный Git remote как Dolt remote, чтобы Beads-данные могли путешествовать рядом с кодом без отдельной инфраструктуры. При этом issues больше не живут в Git-branch как прежний JSONL/SQLite-слой: они находятся в Dolt database, и пользователь может не видеть изменений как обычные Git-коммиты. Это даёт долговечную структурированную базу, но добавляет непрозрачность. [DoltHub: Common Beads Classic Workflows](https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/)

Тот же источник показывает, что multi-agent / multi-clone режим не является бесплатным расширением single-agent режима. Если несколько clones используют один и тот же `origin` как Dolt remote, они получают общую видимость Beads, но записи нужно синхронизировать, а изменения в одних и тех же issues могут конфликтовать примерно так же, как конфликтуют строки кода в Git. Для Gas Town это важная фактура: Beads решает проблему исчезающего контекста агента, но переносит часть сложности в sync, remote topology и conflict discipline. [DoltHub: Common Beads Classic Workflows](https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/)

GitHub README Beads подтверждает это с другой стороны: embedded mode по умолчанию использует in-process Dolt и single-writer file locking; server mode подключается к внешнему `dolt sql-server` и поддерживает concurrent writers; `.beads/issues.jsonl` остаётся экспортом для просмотра и обмена, но не является source of truth или полноценной резервной копией. Это полезная граница для теории: durable work graph должен иметь понятный режим хранения, восстановления и синхронизации, иначе он сам становится новым источником сбоев. [Beads README](https://github.com/gastownhall/beads)

## Грамматика работы: MEOW, GUPP, molecules, formulas, gates и wisps

### MEOW: декомпозиция работы как формальный язык, а не просто стиль планирования

Glossary вводит MEOW — Molecular Expression of Work: разбиение крупной цели на детальные инструкции для агентов, поддержанное Beads, Epics, Formulas и Molecules. Это уточняет роль molecules/formulas. Они не просто удобный шаблон. Они превращают декомпозицию работы в формальный язык, где крупная цель раскладывается на отслеживаемые атомарные единицы, которые агенты могут исполнять автономно.[^gt-glossary]

Для досье это меняет тон Beads-подраздела. Beads хранит граф и состояние, а MEOW даёт способ порождать элементы этого графа в форме, пригодной для агентов. В терминах будущей теории это ближе к “артефактизированной декомпозиции”: сложная задача становится не запросом на 300 строк, а набором атомарных единиц с зависимостями, владельцами, статусами и путём восстановления.

[^gt-glossary]: Gas Town [Glossary](https://github.com/gastownhall/gastown/blob/main/docs/glossary.md), определение Gas Town и MEOW.

### Gas Town role templates: GUPP as concrete instruction, not metaphor

Mayor role template makes the Gas Town propulsion principle operational: on startup, check hook; if work is hooked, execute without confirmation; if hook is empty, check mail и then wait. It names the failure mode directly: Mayor restarts, announces itself, waits for “ok go,” human is AFK, Witnesses wait, Polecats idle, Gas Town stops. The same template’s “File It, Sling It” rule says a code change should by default become `bd create ...` plus `gt sling <bead-id> <rig>`, и gives a decision tree: coordination is Mayor’s job, code change should be slung, truly trivial changes can be done directly; if unsure, sling it. Источник: [Gas Town mayor role template](https://github.com/gastownhall/gastown/blob/main/internal/templates/roles/mayor.md.tmpl).

Это сильный материал для будущей теории: Gas Town isn’t only architecture; it encodes behavior in role prompts. Throughput depends on removing confirmation stalls и making the устойчивый граф работы the authority. Это напрямую связано с нашим многопроходным документным процессом: resumable state и status files are not enough if the next agent invocation waits for human re-authorization instead of consuming assigned work.

### Molecules, formulas, gates и wisps: Beads as рабочий процесс substrate

Документация Beads Workflows уточняет химический слой конкретнее, чем общий Medium-пост о Gas Town. `Formula` is a декларативный шаблон рабочего процесса in TOML/JSON; `Molecule` is a persistent instance created from a formula, stored in `.beads/`, syncing with git, with steps mapped to issues и parent-child relationships; `Wisp` is the ephemeral counterpart stored in `.beads-wisp/`, не синхронизируется в Git и автоматически истекает после завершения ([Beads Workflows](https://gastownhall.github.io/beads/workflows), [Beads Molecules](https://gastownhall.github.io/beads/workflows/molecules), [Beads Wisps](https://gastownhall.github.io/beads/workflows/wisps)).

Formulas support variables, dependencies, step types и aspects; gates are async coordination primitives that block progress until human approval, timer expiration or external GitHub event. Docs explicitly include human gates и CI/PR gates, plus emergency skip и timeout/best-practice warnings ([Beads Formulas](https://gastownhall.github.io/beads/workflows/formulas), [Beads Gates](https://gastownhall.github.io/beads/workflows/gates)). Это делает Beads ближе к рабочий процесс DSL / orchestration substrate than issue list. Для Gas Town это объясняет, почему molecules/wisps matter: they turn repeatable multi-step work into tracked state, not just a prompt.

### GUPP, hook, pinned beads и agent-not-session

GUPP — центральный принцип движения Gas Town: если на hook есть работа, агент должен её выполнять. В Medium-посте это связано с главной проблемой Claude Code-like agents: сессия заканчивается, контекст заполняется, агент останавливается. Gas Town решает это не удлинением одной сессии, а вынесением work, identity, hook, mail и events в persistent Beads layer ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

Важное уточнение: `agent is not a session`. Sessions are cattle; persistent agents, role beads, agent beads и hooks live in Beads/Git. `Hook` — pinned bead; на него помещается работа. Role Beads и Agent Beads тоже pinned beads: они не закрываются как обычные issues и представляют устойчивые identities / domains in data plane ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

### Molecules, formulas, wisps и nondeterministic idempotence

Medium-пост добавляет важный слой, которого в content-derived досье было мало. `Molecules` — workflows, chained with Beads: sequenced small tasks, которые агент должен выполнять по порядку. `Protomolecules` — шаблоны; `Formulas` — source form in TOML, which are cooked into protomolecules и instantiated into wisps or molecules in Beads. Это механизм превращения длинного процесса, вроде release рабочий процесс, в цепочку маленьких устойчивых steps с activity feed и recovery ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

Gas Town называет свой принцип durability `Nondeterministic Idempotence` (NDI). Это не Temporal deterministic replay, и источник прямо предупреждает, что Gas Town is not a replacement for Temporal; но для developer tool он даёт practical рабочий процесс guarantees. Если molecule находится на hook, persistent agent + persistent hook + persistent molecule in Git позволяют другой сессии продолжить выполнение после crash/context exhaustion/restart ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

`Wisps` — ephemeral Beads: они есть в базе и действуют как обычные Beads, но не пишутся в JSONL/Git, а в конце burn/destroy, иногда squash into digest. Их задача — high-velocity orchestration without polluting Git; patrol agents, Refinery, Witness, Deacon и Polecats create wisp molecules for patrol/рабочий процесс runs ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

### Planning fuel и интеграция с другими методами

Gas Town быстро потребляет work backlog. Medium-пост прямо говорит, что на production side можно использовать свои planning tools — Spec Kit or BMAD — а затем попросить агента convert plan into Beads epics; если план большой, его можно swarm as a convoy. Это хороший мост между SPDD/Spec Kit/BMAD и Gas Town: первые создают structured intent/plans, Gas Town превращает их в распределённую очередь persistent agent work ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

### Рабочий процесс и организация Gas Town

Gas Town показывает, что долгую агентскую работу нельзя привязывать к конкретной Claude Code-сессии. Сессия может оборваться, исчерпать контекст, быть перезапущена, заменена другой сессией. Работа не должна исчезать вместе с ней. Корпусный фрагмент: [§44](../../content/Theoretical_synthesis.md#28-agent-ne-sessiya), источник: [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04).

В текущей теории ключевой ход сформулирован так: Gas Town не пытается сделать одну сессию бесконечно умной. Он признаёт, что сессии расходуемы. Устойчивыми должны быть не сессии, а работа, роли, память, события и граф задач. Корпусный фрагмент: [§41](../../content/Theoretical_synthesis.md#25-pochemu-gas-town-zasluzhivaet-otdelnogo-razdela).

Сессии моделей становятся временными исполнителями, которых можно бросать на устойчивую работу. В теории это прямо сравнивается с Kubernetes-логикой «не держаться за конкретный pod», но в применении к agent sessions. Если сессия умерла, новая должна получить роль, hook, рабочую единицу, передачу состояния и контекст из системы. Корпусный фрагмент: [§44](../../content/Theoretical_synthesis.md#28-agent-ne-sessiya), источник: [Introducing Beads](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a).

### GUPP, hooks, molecules и wisps

Gas Town вводит GUPP — принцип, по которому агент должен запускать работу, если она лежит на его hook. В текущей теории важно не само смешное название, а механизм: работа не «просится» в свободном тексте, а подвешивается на устойчивый hook агента. Корпусный фрагмент: [§46](../../content/Theoretical_synthesis.md#30-gupp-huki-molecules-i-wisps-rabota-kak-tsepochka-ustoychivyh-deystviy), источник: [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04).

Hook в Gas Town — не просто событие оболочки. Это pinned bead, устойчивый объект в Beads data plane. На hook помещаются molecules — цепочки рабочих шагов. Для более эфемерной оркестрации используются wisps: они позволяют выполнять временные рабочие процессы без засорения Git постоянным шумом. Патрульные агенты — Refinery, Witness и Deacon — выполняют свои patrols как повторяющиеся цепочки действий, постепенно засыпая через backoff, если работы нет. Корпусный фрагмент: [§46](../../content/Theoretical_synthesis.md#30-gupp-huki-molecules-i-wisps-rabota-kak-tsepochka-ustoychivyh-deystviy), источник: [Introducing Beads](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a).

Смысл механики: работа становится внешней по отношению к сессии. Агент может завершить сессию, очистить контекст, перезапуститься, получить подталкивание и продолжить с hook. Даже если модель слишком вежлива и ждёт ввода, система может подталкивать её к чтению hook и почты. Это не идеальная автономия: в текущей теории подчёркнуто, что Yegge описывает необходимость подталкивания и патрулей. Но именно поэтому пример ценен: он показывает реальные механизмы компенсации хрупкости агентских сессий. Корпусный фрагмент: [§46](../../content/Theoretical_synthesis.md#30-gupp-huki-molecules-i-wisps-rabota-kak-tsepochka-ustoychivyh-deystviy).

Для практического dev-process здесь важна форма, а не словарь molecules/wisps: долгую работу нужно представить как цепочку устойчивых шагов, связанных с исполнителем, состоянием и механизмом продолжения. Если этого нет, передача состояния остаётся ручной заметкой. Если есть, следующий агент может продолжить не по памяти чата, а по внешней структуре работы. Корпусный фрагмент: [§46](../../content/Theoretical_synthesis.md#30-gupp-huki-molecules-i-wisps-rabota-kak-tsepochka-ustoychivyh-deystviy).


## Пространства и роли: Town, Rig, Mayor, Crew, Polecats, Refinery, Witness, Deacon, Dogs

### Итог для Gas Town-досье

После этого pass Gas Town should not receive another broad проход с раскрытием источников unless new primary material appears. Further work should happen in two places:

- Gas Town story/dossier — keep Beads central и explain role orchestration around it.
- Persistent Work Graph mechanism dossier — compare Beads with Spec Kit `tasks.md`, BMAD story files, GSD trace/state, и our multi-pass document workflow status/ledger model.

### Почему Beads теперь стоит в центре Gas Town-досье

Третий проход специально проверял не ещё один общий рассказ о Gas Town, а документацию Beads как нижний операционный слой: [Beads docs](https://gastownhall.github.io/beads/), [Core Concepts](https://gastownhall.github.io/beads/core-concepts), [Architecture](https://gastownhall.github.io/beads/architecture), [Workflows](https://gastownhall.github.io/beads/workflows), [Molecules](https://gastownhall.github.io/beads/workflows/molecules), [Formulas](https://gastownhall.github.io/beads/workflows/formulas), [Gates](https://gastownhall.github.io/beads/workflows/gates), [Wisps](https://gastownhall.github.io/beads/workflows/wisps), [Multi-Agent](https://gastownhall.github.io/beads/multi-agent), [Agent Coordination](https://gastownhall.github.io/beads/multi-agent/coordination) и [Codex Integration](https://gastownhall.github.io/beads/integrations/codex). После этого Beads надо описывать не как “issue tracker used by Gas Town”, а как **устойчивый граф работы + память агента + основа координации**.

Официальная документация Beads определяет его как Dolt-powered issue tracker for AI-supervised coding workflows и says it was built for AI-native workflows, dependency-aware execution, formulas и multi-agent coordination ([Beads Documentation](https://gastownhall.github.io/beads/)). README ещё резче формулирует: Beads replaces messy markdown plans with a dependency-aware graph, allowing agents to handle long-horizon tasks without losing context ([Beads GitHub](https://github.com/gastownhall/beads)). Это и есть центральный переносимый механизм для нашей теории.

### What Beads contributes to the theory of Gas Town

The theoretical unit is therefore not “Beads = issue tracker”. More accurate formula:

> Beads is the place where agent work becomes an object: claimable, dependency-aware, resumable, routable, handoff-able, auditable и recoverable.

Gas Town uses this object layer to run a theatrical multi-agent town. But the transferable idea is lower и more important: mature agentic development needs an external граф работы that can survive sessions, compaction, branch/worktree boundaries и agent handoff. In future theory, Gas Town should be introduced through this: **Beads first, roles second**.

### Роли и пространства: точная карта после source opening

Gas Town имеет несколько разных уровней идентичности и ответственности. `Town` — HQ/workspace, отдельный root вроде `~/gt`, где живёт конфигурация и управление несколькими project rigs. `Rig` — проект/repository под управлением Gas Town; некоторые роли существуют per-rig, другие town-level. `Overseer` — человек, восьмая роль, с identity и inbox в системе ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)).

`Mayor` — главный интерфейс человека: concierge / chief-of-staff, через него обычно стартуют convoys и приходят уведомления. `Crew` — long-lived per-rig coding agents, которыми человек пользуется напрямую; они имеют имена и устойчивые identities. `Polecats` — ephemeral per-rig workers, которые запускаются on demand, производят Merge Requests и are decommissioned after merge. `Refinery` — merge queue processor, который последовательно доводит изменения до main. `Witness` — per-rig supervisor for polecats, следит за stuck work и nudges/recycles. `Deacon` — town-level daemon/patrol agent; `Dogs` — короткоживущие helpers Deacon-а для инфраструктурной работы ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04), [Gas Town Docs](https://docs.gastownhall.ai/)).

В docs уточнено различие `Crew` / `Polecat`: Crew persistent, user-controlled, подходит для exploratory work, long-running projects и tasks requiring human judgment; Polecat transient, Witness-managed, slung via `gt sling`, работает в branch/worktree и Refinery merges, подходит для discrete, well-defined, parallelizable tasks ([Gas Town Docs](https://docs.gastownhall.ai/)). Это важнее для теории, чем игровая терминология: роли выражают разные lifecycle contracts.

### Роли: организационные функции, а не персонажи

В текущей теории перечислены основные роли и пространства Gas Town. Сохранять эти названия важно: за игровой терминологией скрывается структура многоагентной рабочей среды. Корпусный фрагмент: [§42](../../content/Theoretical_synthesis.md#26-roli-ne-personazhi-a-organizatsionnye-funktsii), источник: [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04).

- **Town** — управляющее пространство. Корпусный фрагмент: [§42](../../content/Theoretical_synthesis.md#26-roli-ne-personazhi-a-organizatsionnye-funktsii).
- **Rigs** — проекты, то есть репозитории под управлением Gas Town. Корпусный фрагмент: [§42](../../content/Theoretical_synthesis.md#26-roli-ne-personazhi-a-organizatsionnye-funktsii).
- **Overseer** — человек с собственной идентичностью и почтой. Корпусный фрагмент: [§42](../../content/Theoretical_synthesis.md#26-roli-ne-personazhi-a-organizatsionnye-funktsii).
- **Mayor** — главный интерфейс к системе, агент-координатор и помощник руководителя. Корпусный фрагмент: [§42–43](../../content/Theoretical_synthesis.md#27-mayor-vidimost-bez-chteniya).
- **Crew** — долгоживущие агенты, с которыми человек ведёт дизайн и обсуждение. Корпусный фрагмент: [§42](../../content/Theoretical_synthesis.md#26-roli-ne-personazhi-a-organizatsionnye-funktsii).
- **Polecats** — одноразовые исполнители, которые создаются под работу и после выполнения исчезают. Корпусный фрагмент: [§42](../../content/Theoretical_synthesis.md#26-roli-ne-personazhi-a-organizatsionnye-funktsii).
- **Refinery** — агент, который обрабатывает очередь слияния. Корпусный фрагмент: [§42](../../content/Theoretical_synthesis.md#26-roli-ne-personazhi-a-organizatsionnye-funktsii), подробнее [§47](../../content/Theoretical_synthesis.md#31-refinery-witness-deacon-obsluzhivayuschie-agenty).
- **Witness** — наблюдатель за рабочими агентами, помогающий им не застревать. Корпусный фрагмент: [§42](../../content/Theoretical_synthesis.md#26-roli-ne-personazhi-a-organizatsionnye-funktsii), подробнее [§47](../../content/Theoretical_synthesis.md#31-refinery-witness-deacon-obsluzhivayuschie-agenty).
- **Deacon и Dogs** — служебный слой, который регулярно патрулирует систему, поддерживает движение и выполняет обслуживание. Корпусный фрагмент: [§42](../../content/Theoretical_synthesis.md#26-roli-ne-personazhi-a-organizatsionnye-funktsii), подробнее [§47](../../content/Theoretical_synthesis.md#31-refinery-witness-deacon-obsluzhivayuschie-agenty).

За этими ролями стоят устойчивые функции: принять задание от человека, создать исполнителей, проследить за зависшими задачами, слить изменения, обслужить систему и удержать долгий дизайн-разговор. В малом процессе это не обязано быть отдельными агентами: функции могут стать ритуалами, скриптами или ручными checkpoint-ами. Корпусный фрагмент: [§42](../../content/Theoretical_synthesis.md#26-roli-ne-personazhi-a-organizatsionnye-funktsii).

### Mayor: видимость без чтения

Mayor особенно важен как human surface. Когда агентов много, человек не может читать весь поток вывода. Ему нужен интерфейс, который сам читает шум, вытаскивает важное, показывает состояние, предлагает следующий вопрос и помогает управлять рабочей силой агентов без постоянного погружения в каждый терминал. Корпусный фрагмент: [§43](../../content/Theoretical_synthesis.md#27-mayor-vidimost-bez-chteniya), визуальный источник: [Gas Town Docs](https://docs.gastownhall.ai/).

Текущая теория называет это «видимость без чтения»: человек остаётся владельцем решения, но не обязан потреблять весь низкоуровневый поток. Для систем активной памяти это важный аналог. Такая память должна не только хранить состояние, но и возвращать человеку управляемую картину: что важно, что изменилось, где блокер, где нужен выбор, какие линии работы связаны между собой. Корпусный фрагмент: [§43](../../content/Theoretical_synthesis.md#27-mayor-vidimost-bez-chteniya).

Если перевести этот принцип в будущий dev-process, интерфейс к агентской работе должен показывать больше, чем логи: состояние, решения, группы изменений, предупреждения о конфликте, очередь, точку возвращения человека и значимые детали исполнения без необходимости читать всё. Корпусный фрагмент: [§43](../../content/Theoretical_synthesis.md#27-mayor-vidimost-bez-chteniya).

### Обслуживающие агенты: Refinery, Witness, Deacon и Dogs

Когда появляется много исполнителей, часть агентов должна заниматься не продуктовой работой, а обслуживанием самого процесса. Корпусный фрагмент: [§47](../../content/Theoretical_synthesis.md#31-refinery-witness-deacon-obsluzhivayuschie-agenty), источник: [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04).

**Refinery** решает проблему очереди слияния. Если много Polecats создают изменения параллельно, они начинают конфликтовать с меняющейся базой. Поздний исполнитель может пытаться слиться в `main`, который уже сильно изменился. Нужен агент, который по одному обрабатывает изменения, rebases, rebuilds, иногда заставляет переосмыслить подход и эскалирует, если нельзя безопасно продолжать. Корпусный фрагмент: [§47](../../content/Theoretical_synthesis.md#31-refinery-witness-deacon-obsluzhivayuschie-agenty).

**Witness** решает проблему застревания рабочих агентов. Когда Polecats много, часть из них зависает, не отправляет MR, ждёт, теряет контекст или требует пинка. Witness следит за ними и помогает удерживать поток работы. Корпусный фрагмент: [§47](../../content/Theoretical_synthesis.md#31-refinery-witness-deacon-obsluzhivayuschie-agenty).

**Deacon и Dogs** решают проблему регулярного обслуживания. Deacon запускает patrol в цикле, Dogs разгружают его от грязной работы: устаревшие ветки, плагины, служебная уборка, вспомогательные задачи. Корпусный фрагмент: [§47](../../content/Theoretical_synthesis.md#31-refinery-witness-deacon-obsluzhivayuschie-agenty).

Главный переносимый урок: когда агентская система растёт, часть работы становится не работой над фичами, а сопровождением агентской организации. Для будущего dev-process это означает процедуры, которые чистят рабочие деревья, проверяют зависшие задачи, обновляют handoff, закрывают старые ветки, находят устаревшие инструкции, смотрят повторяющиеся сбои, предлагают удаление лишних skills, проверяют очереди CI и ревью. В малом личном процессе это могут быть не агенты, а ритуалы или скрипты. Корпусный фрагмент: [§47](../../content/Theoretical_synthesis.md#31-refinery-witness-deacon-obsluzhivayuschie-agenty).

### От Gas Town к платформенным примитивам

Ещё один важный урок: переход от одного оркестратора к набору примитивов, из которых можно собирать разные оркестраторы. Текущая теория формулирует это так: Yegge фактически движется от «у меня есть система для управления агентами» к более общей платформе — identities, roles, mail, sessions, cost, model routing, skills, priming, hooks, GUPP, molecules, beads, epics, convoys, orders, patrols, plugins, tmux, восстановление старых сессий. Корпусный фрагмент: [§49](../../content/Theoretical_synthesis.md#33-ot-gas-town-k-platformennym-primitivam), источник: [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04).

Для будущего dev-process нужен не один идеальный рабочий процесс, а набор устойчивых примитивов: рабочая единица, роль, состояние, очередь, передача состояния, проверка, эскалация, обслуживающий проход, восстановление, журнал решений, область действия. Из этих примитивов можно строить разные ритуалы под разные проекты и этапы зрелости. Корпусный фрагмент: [§49](../../content/Theoretical_synthesis.md#33-ot-gas-town-k-platformennym-primitivam).

Для систем активной памяти и долгих разработческих процессов это особенно важно. Среда не должна заранее навязывать один «правильный» процесс. Более сильная архитектура — дать устойчивые примитивы, а затем позволить человеку и агенту собирать из них подходящий экзоскелет: для одиночной задачи, долгого исследования, серии изменений, командной работы или ремонта процесса. Корпусный фрагмент: [§49](../../content/Theoretical_synthesis.md#33-ot-gas-town-k-platformennym-primitivam).


## Исполнение и управление потоком: scheduler, queue, dispatch, convoys и back-pressure

### Event-driven polecat lifecycle и FIX_NEEDED loop

Релизные заметки Gas Town показывают важный сдвиг: polecat lifecycle moves from polling-style management toward event-driven feedback. `FIX_NEEDED` петля обратной связи, `awaiting_verdict` state, refinery → polecat failure routing и Witness handling of awaiting verdicts all make agent work less like fire-and-forget delegation и more like tracked asynchronous protocol.

В досье это стоит связать с Beads centrality: Beads stores work state, but Gas Town needs protocol messages и role logic around it. Persistent graph alone is insufficient. Нужны typed transitions, feedback states, и agents that know how to interpret them.

### Queue, pressure checks и back-pressure as production realism

Gas Town release history adds a stronger обратное давление layer than earlier досье: `gt queue`, queue daemon heartbeat, `gt sling --queue`, config-driven capacity scheduler with sling context beads, opt-in CPU/memory pressure checks before agent spawns, non-destructive queue/wait-idle nudges. Это подтверждает, что “много агентов” быстро превращается в resource-governance problem.

Для многопроходного документного процесса это переносится почти напрямую: если несколько workers запускаются параллельно, недостаточно просто снизить concurrency вручную. Нужно иметь explicit ready/queue state, capacity rules, heartbeat, retry/resume semantics и no-destructive nudging. Gas Town therefore becomes not only external case, but implementation warning for our loop framework.

### Multi-agent coordination: pinning, hook, handoff, fan-out/fan-in и conflict prevention

Agent Coordination docs give the missing operational grammar: `bd pin` assigns work to an agent, `bd hook` shows what is pinned, sequential handoff closes/reassigns work, parallel work pins separate issues to separate agents, fan-out/fan-in uses child issues и dependencies, и conflict prevention includes file reservations и issue locking ([Beads Agent Coordination](https://gastownhall.github.io/beads/multi-agent/coordination)). This is central to Gas Town: Crew/Polecat/Refinery/Witness roles only become tractable because the substrate can represent assignment, ownership, handoff, blockers и merge/fan-in relations.

Multi-Repo Routing docs add another substrate-level idea: pattern-based routes can send issues to specific repos, cross-repo dependencies can be tracked, и `bd hydrate` can pull related issues from other repos ([Beads Routing](https://gastownhall.github.io/beads/multi-agent/routing)). For the Gas Town section, this supports the town/rig distinction: coordination state и repo-local work can be separated but still linked.

### Convoys, sling, handoff и surfaces наблюдения

`Convoy` — work-order/ticketing unit, который wraps a bunch of work into a unit tracked for delivery. Даже одиночная slung task может быть wrapped in convoy, чтобы человек видел не отдельный issue-id, а delivery unit. Primitive for work distribution is `gt sling`: Mayor or human creates/fetches issue и slings it to Polecat/Crew/rig; swarm agents may attack the same convoy across iterations ([Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04), [Gas Town GitHub](https://github.com/gastownhall/gastown)).

README подтверждает базовую петлю: You → Mayor → Convoy → Agent → Hook → completion → summary. Есть recommended Mayor рабочий процесс for complex multi-issue work, Manual Convoy Рабочий процесс for direct control, Beads Formula Рабочий процесс for repeatable processes и Minimal Mode without tmux, where Gas Town tracks state while individual runtime instances are run manually ([Gas Town GitHub](https://github.com/gastownhall/gastown)).

Наблюдаемость не сводится к чтению terminal output. `gt feed --problems` groups agents by health state: GUPP Violation, Stalled, Zombie, Working, Idle, и provides intervention keys such as nudge и handoff. Это почти готовая аналогия для будущего многопроходного документного процесса: вместо чтения всех логов система должна surface stuck runs, zombies, stalled progress и needed human intervention ([Gas Town GitHub](https://github.com/gastownhall/gastown)).



### Диагностика Beads: debug-флаги как признак реальной сложности substrate

`TROUBLESHOOTING.md` важен не как пользовательская инструкция, а как карта подсистем, которые реально приходится отлаживать. В документе перечислены отдельные debug-флаги: `BD_DEBUG` для общего вывода, `BD_DEBUG_RPC` для связи CLI с Dolt server, `BD_DEBUG_SYNC` для sync/import timestamp protection, `BD_DEBUG_ROUTING` для multi-repo routing, `BD_DEBUG_FRESHNESS` для обнаружения замены database file и переподключения. Для Gas Town это подтверждает, что Beads — не пассивный список задач, а рабочий слой с RPC, синхронизацией, маршрутизацией и состоянием базы. [Beads Troubleshooting](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md)

Эти debug-флаги полезны и для проектирования нашего многопроходного документного процесса. Если многопроходный документный процесс будет хранить состояние проходов, очереди, recovery и routing в файлах или базе, ему нужны не только `status.json`, но и диагностируемые контуры: почему задача не видит последний pass, почему route пошёл не туда, почему состояние устарело, почему восстановление не сработало. Gas Town/Beads показывает это на уровне готового инструмента: durable state without observability quickly becomes opaque state.

## Восстановление, наблюдаемость и долговечность состояния

### Codex integration: context recovery через hook lifecycle, а не через надежду на память сессии

Beads Codex integration даёт очень сильный material for our own loop framework. `bd setup codex` uses a `beads` skill, managed `AGENTS.md` guidance и native Codex hooks. The hook lifecycle is specific: `SessionStart` injects full `bd prime`; `PreCompact` checks `bd prime --memories-only`; `PostCompact` records that session needs refresh; `UserPromptSubmit` injects full `bd prime` once after compaction и clears marker. Crucial detail: `PreCompact` alone does not inject context because Codex ignores plain stdout from compact hooks; the post-compact marker plus first-prompt refresh is the reliable recovery path. [Beads Codex integration](https://gastownhall.github.io/beads/integrations/codex)

Это почти готовый design lesson for многопроходный документный процесс: если long-running pass/рабочий процесс может пережить compaction / restart / timeout, refresh must be event-driven и state-backed. Не достаточно написать “прочитай status.json”; нужно иметь lifecycle point, marker и rehydration command.

### Compaction recovery: Beads as context refresh system

Beads Codex integration is especially useful for our multi-pass document workflow. The docs say `bd setup codex` installs a Beads skill, managed `AGENTS.md` guidance и native Codex hooks; `SessionStart` injects full `bd prime`, `PreCompact` checks `bd prime --memories-only`, `PostCompact` marks the session as needing a Beads refresh, и `UserPromptSubmit` injects full `bd prime` once after compaction because `PreCompact` stdout is not a reliable injection surface ([Beads Codex integration](https://gastownhall.github.io/beads/integrations/codex)).

Это более точная версия того, что нам нужно для многопроходного документного процесса. Не “читать всё прошлое состояние”, а делать compact rehydration через fixed command surface. Если переносить механизм в нашу инфраструктуру, аналогом было бы не перечитывание `work/automation/runs/...`, а короткий `loop prime`: last pass, current shard, unresolved gates, token budget, next action.


## Платформенные примитивы, внешнее чтение и архитектурные границы

### Release history as architecture evidence

Gas Town changelog полезен не как “новости”, а как evidence of real architectural pressure. Система постоянно наращивает не только features, но и repair mechanisms: work queue и dispatch engine, queue heartbeat, OTEL instrumentation, dog subsystem, wisp compaction, configurable quality gates, spawn storm detection, MR bead verification, pressure checks, event-driven polecat lifecycle, non-destructive nudges, и typed enums replacing fragile status strings.

Это меняет тон досье: Gas Town нельзя подавать как уже settled ideal architecture. Это evolving control system under stress. История релизов показывает, что multi-agent workspace требует всё больше explicit mechanics: capacity governors, watchdog chain, telemetry, queues, recovery, typed state и release guards. Для будущей теории это очень важно: если Beads is work substrate, Gas Town is the living example of what happens when that substrate is pushed into fleet orchestration.

### External practice reports: Beads has solo и fleet modes

DoltHub reports help avoid over-reading Gas Town as only large-fleet architecture. “A Day in Gas Town” describes Beads as a command-line tool coding agents use to manage tasks, storing tasks as issues in `.beads`; the example problem is losing continuity after PR review и needing a new session ([DoltHub: A Day in Gas Town](https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/)). “Restoring Beads Classic” adds that some users want a single-process, single-agent Beads experience rather than scaling to Gastown/Gas City/Wasteland, и that backend migration to Dolt had to preserve the solo-user experience ([DoltHub: Restoring Beads Classic](https://www.dolthub.com/blog/2026-04-02-restoring-beads-classic/)). “Two Weeks in Gas Town” frames Gas Town as a workspace manager coordinating many agents и Beads as a way for agents to persist what they need after context compression; it analogizes Beads to institutional memory stored in Jira tickets ([DoltHub: Two Weeks in Gas Town](https://www.dolthub.com/blog/2026-04-16-two-weeks-in-gastown/)).

Эти внешние источники дают важное разделение: **Beads ≠ Gas Town**. Beads может работать как single-agent память и граф работы. Gas Town — это fleet/workspace-оркестрация поверх Beads. Поэтому в истории Gas Town Beads центральный, но в теории Beads должен ещё появиться как более общий persistent-work-graph mechanism.



### Release-gating как свидетельство sync-risk

Release notes Beads v1.0.5 дают особенно сильную негативную фактуру: pre-release был помечен как gated, с прямым предупреждением не обновляться, потому что migration `0043` могла тихо и необратимо сломать multi-machine `bd dolt sync` после обновления обоих clones. Пользователям, которые уже были на v1.0.5, предлагалось не запускать `bd dolt push` / `bd dolt pull` между машинами до исправления. [Beads Releases](https://github.com/gastownhall/beads/releases)

Это важно для будущей теории сильнее, чем очередной список команд. Beads показывает правильное направление — вынести агентную работу из контекстного окна в версионируемую базу. Но как только эта база становится общей для нескольких машин и агентов, миграция схемы и протокол синхронизации превращаются в критические части методологии. Поэтому Gas Town нельзя описывать только через пропускную способность агентов и удобство Beads. Его нижний слой требует release-gates, дисциплины миграций, резервного копирования, восстановления и отката.

## Риски, стоимость и сценарии сбоев


### Routine maintenance can fail: cleanup/compaction как опасное место

Issue `gastownhall/beads#3313` даёт хороший negative source по Beads. Пользователь описывает, что `bd admin cleanup` и `bd admin compact` возвращали `not yet supported in embedded mode`, хотя `dolt sql-server` уже обслуживал эту базу и обычные `bd list`, `bd show`, `bd update` работали в той же shell-сессии. Контекст особенно важен: проблема возникла во время Dolt CPU / heartbeat-bloat incident, где 12k+ closed heartbeat beads поднимали стоимость reconcile, а документированное средство `bd admin compact --days 0` не запускалось. Обходной путь через прямой SQL `DELETE` был рабочим, но bypassed audit trail и was explicitly framed as a foot-gun.[^beads-issue-3313]

Это не опровергает Beads. Напротив, это показывает, что Beads уже находится в зоне настоящей инфраструктуры. Если work graph становится центральным состоянием многоагентной работы, routine maintenance — cleanup, compaction, old-heartbeat removal, sync repair — становится частью безопасности метода. В досье это стоит сохранить как контрпример к слишком гладкому чтению Gas Town: persistent state помогает агентам продолжать работу, но приносит команды обслуживания, audit trail, compatibility modes и восстановление после сбоя as load-bearing details.

[^beads-issue-3313]: Issue `gastownhall/beads#3313`, [`bd admin cleanup / bd admin compact fail with not yet supported in embedded mode`](https://github.com/gastownhall/beads/issues/3313), описывает failure pattern for admin cleanup/compact, Beads v1.0.2, Dolt 1.86.1 и heartbeat-bloat incident.

### Sandboxed agents: прямой урок для Codex-like сред

Beads troubleshooting отдельно выделяет sandboxed environments вроде Codex и Claude Code. Симптомы: повторяющиеся `Database out of sync` ошибки после `bd dolt pull`, невозможность остановить Dolt server из-за restrictions, hash mismatch warnings. Документация объясняет root cause: sandbox cannot signal or kill existing Dolt server process. Начиная с версии, где sandbox auto-detection available, `bd` может включать sandbox mode; вручную его можно вызвать через `bd --sandbox ready`, `bd --sandbox create ...`, `bd --sandbox update ... --claim`.[^beads-troubleshooting-sandbox]

Для Gas Town это важное ограничение переносимости. Среда, которая отлично работает в обычной shell-сессии, может вести себя иначе в sandboxed agent runtime. Если Gas Town/Beads переносить в многопроходный документный процесс, нужно не только хранить state, но и учитывать права процесса: можно ли агенту стартовать server, останавливать его, писать metadata, читать status, cleanly recover. Иначе persistent work graph станет не опорой, а дополнительным источником stuck states.

[^beads-troubleshooting-sandbox]: Beads docs, [`TROUBLESHOOTING.md`](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md), раздел `Sandboxed environments (Codex, Claude Code, etc.)`.

### Внешняя критика: перегрузка понятий, трение merge/sync и узкое место ответственности

Hacker News обсуждение нельзя использовать как надёжный источник фактов о внутреннем устройстве Gas Town. Но как сигнал восприятия и практического трения оно полезно. Несколько комментариев формулируют одну и ту же проблему: Beads кажется сильной идеей, но пользователи опасаются большого числа пересекающихся понятий, багов, merge conflicts и неясная ответственность. Один комментатор прямо связывает ограничение Gas Town с ответственностью за ревью: много параллельных агентов не снимают bottleneck человеческого ревью и владение.[^gt-hn]

Эта критика нужна в досье не для того, чтобы “опровергнуть” Gas Town, а чтобы не романтизировать его. Чем сильнее мы ставим Beads в центр, тем честнее надо показать цену: устойчивый граф работы помогает агентам продолжать работу, но сам граф становится системой, которая может ломаться, конфликтовать, расходиться с реальностью и перегружать человека. В теории это важный контрапункт к тезису “много агентов + внешняя память = масштабирование”. Масштабирование начинается только там, где есть достаточная ёмкость ревью, назначение ответственности, дисциплина merge и playbook восстановления.

[^gt-hn]: Hacker News discussion [“Welcome to Gas Town”](https://news.ycombinator.com/item?id=46458936), особенно комментарии о bugs/overlap, merge conflicts и accountability/review bottleneck. Используется как слабый внешний сигнал, не как canonical documentation.

### Риски и ограничения

* **Риск адресации.** В системе с несколькими rig-ами и уровнями состояния агенту нужна надёжная маршрутизация; иначе он может читать или менять чужую рабочую область.
* **Перегрузка понятий.** Gas Town/Beads легко перегружает пользователя множеством объектов: bead, molecule, formula, wisp, convoy, rig, mayor, polecat, witness. Это может разрушить adoptability даже при сильной базовой идее.
* **Трение merge/sync.** Устойчивое состояние не отменяет конфликтов. При ошибках синхронизации или merge-а агент может потерять или перезаписать человеческую работу.
* **Узкое место ревью и ответственности.** Параллельные агенты повышают throughput только до границы, где человек или команда ещё способны проверять, принимать ответственность и принимать результаты в merge.
* **Устаревающие внешние чтения.** Внешние статьи могут описывать старые версии Beads через JSON/Git, тогда как текущий источник истины уже Dolt-backed. Такие материалы полезны для восприятия, но не должны заменять официальную архитектуру.

### Future architecture: Witness with Agent Teams

Design doc `Witness AT Team Lead` важен как источник границ, а не как текущая реализация. Он прямо помечен as future architecture / not yet implemented. Но он valuable because it names structural blockers: no per-teammate working directory, no session resumption for teammates, token cost around 7x per teammate, hook compatibility и experimental API risk. Proposed mitigations include PreToolUse hook for worktree scope, PreCompact handoff + beads state recovery + Witness respawn, и cost-tier role assignment.

Это добавляет в досье важный theoretical point: even if transport layer changes from tmux to Agent Teams, Gas Town keeps Beads as ledger, `gt mail`, molecules/formulas и `gt done`. То есть stable architectural center is not tmux. Stable center is persistent work state plus protocol surface around it.

### Beads release-gating as sync-risk evidence

Release notes Beads дают жёсткое эксплуатационное предупреждение: v1.0.5 был gated, потому что migration `0043` могла тихо и необратимо сломать multi-machine `bd dolt` sync после обновления обоих clones. Пользователям прямо говорили не запускать `bd dolt push/pull` между машинами до исправления. Для теории это важный контрпример к романтизации Dolt-backed state: версионируемое структурированное состояние полезно, но миграции схемы и multi-machine sync становятся новыми поверхностями риска.

Для Gas Town-досье это means: “Dolt as источник истины” is not free robustness. It shifts failure from ephemeral prompt memory to distributed state, migration discipline, sync policy и playbook восстановленияs.

### Риски и ограничения

* **Distributed-state fragility** — Dolt-backed граф работы adds migration/sync сценарии сбоев.
* **Transport-layer instability** — tmux/Agent Teams/Claude/Codex runtimes differ; orchestration must not depend on one fragile transport.
* **No-resumption risk** — teammates/agents may crash without resumable session; state recovery must be external.
* **Capacity illusion** — launching more agents is not scaling unless queue, pressure, cost и merge capacity are governed.
* **Status-protocol brittleness** — stringly-typed or implicit states create recovery bugs; typed transitions matter.

### Limits: Beads is local-first, not universal project management

Beads architecture docs explicitly list non-goals и limits: not suitable for large teams with high-frequency concurrent edits, non-developers, real-time collaboration, cross-repository tracking as default, or rich media attachments; it relies on local/offline version-controlled database semantics и explicit sync. [Beads Architecture](https://gastownhall.github.io/beads/architecture)

This is important for Gas Town: устойчивый граф работы is powerful, but it does not remove coordination cost. It shifts cost from model memory to database/рабочий процесс discipline. For our multi-pass document workflow, this means: a local-first graph could be excellent for one user / small agent cluster, but not automatically a team-scale Jira replacement.

### Риски и ограничения

* **Ready queue quality depends on dependency modeling.** Если dependencies неверны или неполны, `bd ready` can confidently route agents into bad work.
* **Hook recovery is environment-specific.** Codex integration has a precise lifecycle; other tools need different hooks. Portability exists, but not uniformly.
* **Local-first sync creates race/recovery rituals.** Dolt helps, but users still must push/pull, stop server in some workflows, и know recovery procedures.
* **CLI surface is very large.** 106 top-level commands make Beads powerful but also hard to master; AI agents may need much narrower “approved command subset”. [Beads CLI Reference](https://gastownhall.github.io/beads/cli-reference)
* **Not a rich collaboration platform.** Architecture docs explicitly route large-team и real-time collaboration cases toward GitHub Issues / Linear / Jira rather than Beads. [Beads Architecture](https://gastownhall.github.io/beads/architecture)

### Known gap: operation log / agent-first version control

GitHub discussion #363 is not canonical design, but useful as a limitation signal: proposed priorities include automatic workspace management tied to agent lifecycle, structured operation log queryable by agent/session/bead, и auto-merge for non-conflicting concurrent changes. Источник: [Gas Town discussion #363](https://github.com/gastownhall/gastown/discussions/363). Это помогает не переоценивать текущий Gas Town/Beads stack: Beads gives durable граф работы и history, but fine-grained operation ledger и safer parallel merge semantics remain active design pressure.

### Operation log: что ещё не хватает даже Gas Town/Beads

Обсуждение Agent-First Version Control for Gas Town & Beads добавляет важный failure-analysis слой. Там прямо сказано, что сейчас, когда что-то идёт не так, приходится реконструировать события from git log, beads history и mail threads; proposed improvement is an immutable append-only operation log capturing agent identity, session ID, model и token count, so “what did agent X do during session Y?” becomes one query ([GitHub discussion #363](https://github.com/gastownhall/gastown/discussions/363)).

Для нашей теории это очень ценно: даже Beads/Gas Town ещё не полностью решает provenance. Persistent граф работы — необходимый шаг, но не полный execution ledger. В будущей главе про exoskeleton и многопроходный документный процесс это можно взять почти напрямую: status.json/pass artifacts are not enough; нужно durable operation log with agent/session/model/token identity.

### New сценарии сбоев и limits from fourth проход

- **Dolt/server complexity.** Beads gains SQL/version-control/merge semantics, but also introduces Dolt server/embedded-mode decisions, sync discipline и recovery procedures.
- **Race и clone discipline.** Architecture docs explicitly warn about race conditions in multi-clone/worktree workflows и prescribe server/embedded mode choices и sync discipline ([Beads Architecture](https://gastownhall.github.io/beads/architecture)).
- **Gate sprawl.** Gates solve long waits but can create their own blocked graph if humans/CI/watchers do not resolve or escalate them.
- **Mail и history are not enough.** Gas Town discussion shows that reconstructing execution from git log, beads history и mail threads is still too indirect; operation-log support remains a frontier need.
- **Not for every team.** Beads docs explicitly say it is not suitable for large teams, non-developers, real-time collaboration, cross-repository tracking or rich media attachments, и suggest GitHub Issues/Linear/Jira for those cases ([Beads Architecture](https://gastownhall.github.io/beads/architecture)).

### Риски и границы после source opening

После раскрытия источников риски стали ещё яснее. Gas Town требует высокой зрелости пользователя, готовности к множеству agents, cost burn, tmux discipline и chaotic recovery. Он полезен не как универсальная рекомендация для опытного разработчика, а как frontier example: что происходит, когда одиночная агентская сессия превращается в multi-agent operating environment with persistent state, roles, work routing, service agents, observation surfaces и recovery mechanisms.

Для будущей теории это означает: Gas Town не надо включать в Handbook как раннюю практическую рекомендацию. Его лучше использовать как теоретический крайний случай — максимальная externalization of agent work state и process orchestration.

### Цена Gas Town: пропускная способность против понимания

Gas Town не нужно романтизировать. В текущей теории, со ссылкой на Yegge, зафиксировано: система дорогая, хаотичная, требует большого опыта, tmux-дисциплины, постоянного человеческого управления и готовности мириться с потерями. Некоторые исправления будут сделаны дважды, часть работы потеряется, часть придётся выбирать вручную, часть агентов застрянет. Корпусный фрагмент: [§48](../../content/Theoretical_synthesis.md#32-tsena-gas-town-propusknaya-sposobnost-protiv-ponimaniya), источник: [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04).

Это не делает Gas Town бесполезным. Он показывает цену перехода от «один агент помогает мне» к «я управляю агентской рабочей силой». Вместе с ростом throughput растут шум, потребность в очереди слияния, наблюдателях, восстановлении сессий, почте, событиях, устойчивых идентичностях, обслуживании самой системы и защите человеческого понимания. Корпусный фрагмент: [§48](../../content/Theoretical_synthesis.md#32-tsena-gas-town-propusknaya-sposobnost-protiv-ponimaniya).

Правильный вывод текущей теории: Gas Town не должен превращаться в совет «используйте Gas Town». Это дальний край пространства, предупреждение и карта будущих примитивов. Большинству разработчиков не нужна полная версия, но почти всем, кто будет углубляться в агентскую разработку, постепенно понадобятся её малые элементы: привязка задач к рабочим деревьям, состояние задач, передача состояния, очередь, эскалация, обслуживающий проход, восстановление сессии и наблюдаемость агентской работы. Корпусный фрагмент: [§48](../../content/Theoretical_synthesis.md#32-tsena-gas-town-propusknaya-sposobnost-protiv-ponimaniya).


## Источникный контекст и сохранённые поисковые заметки

### Beads command surface, lifecycle instructions и real operational limits

Поисковый угол этого прохода: не “что такое Gas Town” и не ещё раз Beads architecture, а **какая конкретная operational surface делает Beads usable для агентов**: CLI command set, `AGENTS.md`/setup integration, Dolt workflows, role templates, dashboard/lifecycle changelog и known limits. Это усиливает Gas Town как глубокий якорь: Beads становится не просто центральным подразделом, а практическим интерфейсом устойчивой агентной работы.

### Beads вынесен в mechanism dossier про persistent work graph

Этот проход не должен дальше раздувать Gas Town как историю. Пользовательский выбор зафиксирован: **в Gas Town Beads остаётся центральным подразделом**. Но Beads уже несёт более общий механизм, который нужен теории отдельно: устойчивый граф работы / durable agent work substrate. Поэтому пятый проход делает две вещи:

1. в Gas Town сохраняет Beads как data/control substrate, без которого Gas Town нельзя объяснять;
2. выносит переносимый механизм в отдельное досье `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`.

Основные источники для этого шага: Beads documentation, architecture, multi-agent coordination, Codex integration, `bd prime`, `bd gate`, routing/recovery pages, и DoltHub field explanations of Beads/Gas Town persistence.

### anchor-depth слой — Beads command surface, gates, recovery и operation logs

Этот проход сделан с явным редакционным решением: **Beads остаётся центральным подразделом Gas Town**, потому что именно он превращает Gas Town из “много агентов в tmux” в durable work operating system. Поиск был смещён с ролей и общей архитектуры на Beads docs, command surface, Codex integration, Dolt-backed recovery, gate mechanics и external practice reports. Основные источники прохода: [Beads Architecture Overview](https://gastownhall.github.io/beads/architecture), [Beads CLI Reference](https://gastownhall.github.io/beads/cli-reference), [`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime), [`bd gate`](https://gastownhall.github.io/beads/cli-reference/gate), [Beads Codex integration](https://gastownhall.github.io/beads/integrations/codex), [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04), [Agent-first version-control discussion](https://github.com/gastownhall/gastown/discussions/363) и DoltHub practice reports [A Day in Gas Town](https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/), [Restoring Beads Classic](https://www.dolthub.com/blog/2026-04-02-restoring-beads-classic/) и [Two Weeks in Gas Town](https://www.dolthub.com/blog/2026-04-16-two-weeks-in-gastown/).

### Beads-first search angle

Этот проход искал иначе: не `Gas Town roles`, а `Beads docs`, `Dolt architecture`, `agent coordination`, `Codex integration`, `molecules`, `gates`, `wisps`, `multi-repo routing`. Результат: Gas Town-досье усилено в сторону central Beads subsection; Beads остаётся внутри Gas Town history/case, но в theory layer его можно отдельно использовать как mechanism: устойчивый граф работы / task memory / externalized agent state.

### что добавлено после раскрытия источников

Этот раздел добавлен после открытия внешних источников: Steve Yegge, [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04), Steve Yegge, [Introducing Beads](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a), [Gas Town GitHub README](https://github.com/gastownhall/gastown), [Beads GitHub README](https://github.com/gastownhall/beads) и [Gas Town Docs](https://docs.gastownhall.ai/). Цель прохода — не переписать досье в обзор, а проверить термины, роли, рабочие примитивы, риски и иллюстрации.


## Дополнительные сохранённые заметки

### Что вынесено в отдельный mechanism dossier

Новый `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` раскрывает переносимые примитивы:

- versioned structured state through Dolt;
- work item as durable object, not prompt memory;
- dependency-aware очередь готовых задач;
- pinning, ownership и handoff;
- fan-out/fan-in и file reservations;
- gates as durable asynchronous waits;
- `bd prime` as cheap rehydration surface after session start/compaction;
- routing/hydration across repositories;
- recovery runbooks и `bd doctor`/`bd status`/`bd blocked` workflows;
- lessons for our multi-pass document workflow: resumable state, semantic heartbeats, readiness queue, guardrails against lost progress.

Это не новая история. Это mechanism dossier для теории и design of multi-pass document workflow. Gas Town remains the main story/context; Beads becomes the central example of the mechanism.

### Заметки для будущей проверки источников

- Разделить Beads и Gas Town в будущей теории: Beads = persistent graph memory/data plane; Gas Town = orchestration/workspace/role system поверх Beads.
- Для Handbook оставить Gas Town как high-complexity / frontier pattern, не как рекомендацию по умолчанию.
- Для многопроходного документного процесса особенно забрать три механизма: persistent work unit, problems view for stalled/zombie runs, и resumable molecules/wisps instead of one long session.
- Если делать полный visual pass, лучше брать GitHub Mermaid-схемы и docs-схемы раньше Medium-картинок: они проще, чище и ближе к механике.


Gas Town в текущей теории — предельный пример агентской организации. Он важен не потому, что его терминологию нужно копировать, а потому что показывает, во что превращается agentic development, когда человек управляет не одним помощником, а десятками агентских исполнителей. Основной корпусный раздел: [«Gas Town как отдельный разбор агентской организации»](../../content/Theoretical_synthesis.md#25-pochemu-gas-town-zasluzhivaet-otdelnogo-razdela), внешний источник: [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04).

Главная формула текущей теории: Gas Town показывает, что происходит, когда граф задач и внешняя память работы разрастаются до многоагентной рабочей среды. Появляются роли, очередь слияния, наблюдатели, обслуживающие агенты и человеческий интерфейс к шуму агентской работы. Это уже не «несколько Claude Code в разных терминалах», а маленькая операционная модель: координатор, исполнители, долгоживущие консультанты, наблюдатель, очередь слияния, служебные патрули, почта, роли, проекты, рабочие единицы, состояние и обслуживающие агенты. Корпусные фрагменты: [§40](../../content/Theoretical_synthesis.md#24-graf-zadach-kak-vneshnyaya-pamyat-agenta), [§41](../../content/Theoretical_synthesis.md#25-pochemu-gas-town-zasluzhivaet-otdelnogo-razdela).

Gas Town не задаёт норму для обычного разработчика. В текущей теории он прямо назван предельным примером: карта будущих примитивов и предупреждение о цене перехода от «один агент помогает мне» к «я управляю агентской рабочей силой». Корпусные фрагменты: [§41](../../content/Theoretical_synthesis.md#25-pochemu-gas-town-zasluzhivaet-otdelnogo-razdela), [§48](../../content/Theoretical_synthesis.md#32-tsena-gas-town-propusknaya-sposobnost-protiv-ponimaniya).

### Связи в текущем корпусе

`Handbook.md` использует Beads/Gas Town как верхнюю ступень для долгой фоновой или многоагентной работы: нужны external task memory, worktrees, action log и человеческий шлюзs; риск — результатов больше, чем человек способен проверить. Корпусный фрагмент: [Handbook, выбор режима](../../content/Handbook.md).

В разделе Handbook о task graphs указано, что граф задач вроде [Beads](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a) или [Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04)-подобного рабочего пространства нужен не на старте, а тогда, когда обычные документы перестают показывать зависимости и состояние. Для большинства одиночных задач достаточно плана, GitHub issue, PR и файла передачи состояния. Корпусный фрагмент: [Handbook, task graphs](../../content/Handbook.md).

История Calvin French-Owen фиксирует промежуточную позицию между простым файловым `plans/` и будущей системой управления агентскими задачами и памятью: Calvin упоминает David Cramer’s Dex и Steve Yegge’s beads как инструменты в похожем направлении, но считает их пока немного тяжелее, чем нужно. `/focus` закрывает личное восстановление состояния через `plans`, PR и worktrees, но не решает полностью долговременную очередь, связи между задачами, память решений и фоновую работу нескольких агентов. Корпусный фрагмент: [Calvin French-Owen story](../../content/stories/09_calvin_french_owen_maximum_deep_reconstruction_connected.md).

История Matt Pocock указывает, что источник задач для Ralph может быть не только локальный `PRD.md`, но и GitHub Issues, Linear или beads; результат может быть веткой и PR. Но критерий остаётся тем же: задача должна подходить под форму «посмотреть репозиторий, сделать один проверяемый шаг, зафиксировать состояние». Корпусный фрагмент: [Matt Pocock story](../../content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md).

Итоговая рамка теории связывает Beads/Gas Town с будущим усилением памяти задач, наблюдаемости агентской работы, структурированных графов задач, границ прав, узких инструментальных поверхностей, контуров ремонта процесса и роли платформенных команд. Корпусный фрагмент: [итоговая рамка](../../content/Theoretical_synthesis.md#53-itogovaya-ramka).

## Источники и provenance

Этот раздел восстановлен внутрь досье `GAS_TOWN_METHOD_DOSSIER.md` после ошибочного выноса в общий реестр. Хронология проходов здесь снята: источники сгруппированы по функции в методологии, а не по моменту добавления. Inline-ссылки в основном тексте сохранены рядом с конкретными утверждениями; этот раздел нужен для проверки покрытия и подготовки дальнейших проходов.

### Основные источники Gas Town и корпусные связи

- Steve Yegge, [`Beads Best Practices`](https://steve-yegge.medium.com/beads-best-practices-2db636b9760c) — daily `bd doctor`, cleanup discipline и issue-count hygiene; использовать как author practice note, not neutral documentation.
- Gas Town GitHub — [Glossary](https://github.com/gastownhall/gastown/blob/main/docs/glossary.md) — источник по MEOW, Gas Town definition и work decomposition language.
- Hacker News — [Welcome to Gas Town discussion](https://news.ycombinator.com/item?id=46458936) — слабый внешний источник по perceived friction: concept overload, Beads bugs/merge conflicts и human accountability bottleneck. Не использовать как canonical техническое описание.
- `content/Theoretical_synthesis.md`, разделы 40–49 — основной корпусный источник: task graph, Beads commands, Gas Town roles, Mayor, agent-not-session, Beads as data/control/why layer, GUPP/hooks/molecules/wisps, service agents, costs, platform primitives.
- Steve Yegge — Welcome to Gas Town: [https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) — основной внешний источник для Gas Town as multi-agent working environment, roles, organization, cost и platform primitives.
- Steve Yegge — Introducing Beads: [https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a) — основной внешний источник для Beads as task memory / Git-backed data plane, agent memory, commands и persistent state.
- Gas Town GitHub: [https://github.com/gastownhall/gastown](https://github.com/gastownhall/gastown) — источник для архитектурной схемы Gas Town, рабочий процесс и README-level mechanics.
- Gas Town Docs: [https://docs.gastownhall.ai/](https://docs.gastownhall.ai/) — источник для Mayor’s Hub illustration и human-facing control surface.
- Gas Town GitHub README: [https://github.com/gastownhall/gastown](https://github.com/gastownhall/gastown) — повторно использован для сверки Beads Integration, Core Concepts и how Beads fits into Mayor/Convoy/Agent/Hook/Refinery/Scheduler.
- `content/Handbook.md` — uses Beads/Gas Town as high-complexity mode for long-running or multi-agent work; warns not to recommend task graphs too early.
- `content/stories/09_calvin_french_owen_maximum_deep_reconstruction_connected.md` — shows a practitioner positioned between local `plans/` и heavier Dex/beads-like systems.
- `content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md` — mentions beads as possible task source for Ralph-like workflows.
- `content/Cross_story_synthesis.md` — contains limited or indirect linkage; no major additional Gas Town detail found beyond theory/Handbook layer.
* [Bill de hÓra: Thoughts on Welcome to Gas Town](https://dehora.net/journal/2026/2/initial-thoughts-on-welcome-to-gas-town) — external conceptual reading: Bead/Dolt/tmux strata и layered memory/mailbox model.

### Beads: persistent work graph, CLI, Dolt и integration surface

- DoltHub, [Common Beads Classic Workflows](https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/) — основной новый источник по режимам single-agent/default и multi-clone, использованию Git remote как Dolt remote, переходу от JSONL к Dolt, развязке Git-веток и Beads-state, непрозрачности и sync/merge-conflict tradeoffs.
- Beads [`ROUTING.md`](https://github.com/gastownhall/beads/blob/main/docs/ROUTING.md) — уточнение роли auto-routing для разделения contributor/maintainer и локального планирования без загрязнения upstream PRs.
- Gas Town Docs — [Reference](https://docs.gastownhall.ai/reference/) — источник по Beads Routing, `routes.jsonl`, prefix-based routing, rig config, layered configuration и Beads command summary.
- Eric Koziol — [Exploring Gas Town](https://embracingenigmas.substack.com/p/exploring-gas-town) — external interpretive источник по Beads as externalized task state outside контекстное окно агента; использовать осторожно because storage description may lag current Dolt-backed architecture.
- [Beads Architecture](https://gastownhall.github.io/beads/architecture) — источник по Dolt as источник истины, version-controlled SQL, embedded/server modes, recovery, и when not to use Beads.
- [`bd gate`](https://gastownhall.github.io/beads/cli-reference/gate) — источник по durable async wait conditions: human approval, timers, GitHub runs/PRs, bead dependencies.
- [Beads Recovery Overview](https://gastownhall.github.io/beads/recovery) — источник по quick checks, `bd status`, `bd doctor`, `bd blocked` и recovery runbook format.
- [Beads Routing](https://gastownhall.github.io/beads/multi-agent/routing) — источник по cross-repo routing, hydrated dependencies и shared work queues.
- DoltHub — [A Day in Gas Town](https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/) — external field источник по Beads as coding-agent memory/task system и persistent state after lost sessions/PR review.
- DoltHub — [Multi-Agent Coordination with Dolt и Beads](https://www.dolthub.com/blog/2026-04-22-multi-agent-dolt-beads/) — external источник по structured/versioned agent task data, semi-trusted concurrent writes и Dolt as persistence layer for Gas Town/Beads-style work.
- Beads GitHub: [https://github.com/gastownhall/beads](https://github.com/gastownhall/beads) — источник для task graph / memory scheme и command-level mechanics.
- Gas Town docs — Architecture: [https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md](https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md) — источник по two-level beads architecture, town/rig split, agent beads, role beads, redirects и directory structure.
- Tenzin Wangdhen — Gas Town: The Good, The Bad, The Ugly: [https://tenzinwangdhen.com/posts/gastown-good-bad-ugly/](https://tenzinwangdhen.com/posts/gastown-good-bad-ugly/) — secondary field report по maximalist nature, Beads as modular component, Mayor usefulness, polecats as full sessions и GUPP.
- DoltHub — A Day in Gas Town: [https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/](https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/) — secondary источник по Beads as `.beads` task state и recovery from lost agent sessions.
- Beads Architecture: [https://gastownhall.github.io/beads/architecture](https://gastownhall.github.io/beads/architecture) — источник по Dolt as sole storage backend, embedded/server modes, multi-writer support, recovery, trade-offs и when not to use Beads.
- Beads CLI Reference: [https://gastownhall.github.io/beads/cli-reference](https://gastownhall.github.io/beads/cli-reference) — источник по command surface breadth, generated from `bd help`, и command families including `bd prime`, `bd remember`, `bd graph`, `bd hook`, `bd gate`, `bd mol`, `bd wisp`.
- Beads Workflows: [https://gastownhall.github.io/beads/workflows](https://gastownhall.github.io/beads/workflows) — источник по фазы Formula / Molecule / Wisp и краткое описание команд.
- Beads Formulas: [https://gastownhall.github.io/beads/workflows/formulas](https://gastownhall.github.io/beads/workflows/formulas) — источник по TOML/JSON formulas, variables, step types, dependencies, gates и aspects.
- Beads Gates: [https://gastownhall.github.io/beads/workflows/gates](https://gastownhall.github.io/beads/workflows/gates) — источник по human/timer/GitHub gates, gate states, approval, CI и best practices.
- Beads Wisps: [https://gastownhall.github.io/beads/workflows/wisps](https://gastownhall.github.io/beads/workflows/wisps) — источник по ephemeral workflows stored in `.beads-wisp/`, no git sync и auto-expiration.
- Beads GitHub README: [https://github.com/gastownhall/beads](https://github.com/gastownhall/beads) — источник по essential commands, `bd prime`, `bd remember`, markdown TODO prohibition, features и storage modes.
- [Beads Architecture Overview](https://gastownhall.github.io/beads/architecture) — Dolt as sole storage backend, источник истины, embedded/server mode, multi-clone race conditions, recovery, trade-offs и when not to use Beads.
- [Beads CLI Reference](https://gastownhall.github.io/beads/cli-reference) — command surface breadth; especially `bd prime`, `bd gate`, `bd mail`, `bd mol`.
- [`bd gate`](https://gastownhall.github.io/beads/cli-reference/gate) — async wait conditions, human/timer/GitHub/bead gates, wake notifications, resolved/escalated semantics.
- [Gas Town mail protocol](https://github.com/gastownhall/gastown/blob/main/docs/MAIL_PROTOCOL.md) — Beads-backed inter-agent messages и completion/merge signals.
- [GitHub discussion #363: Agent-First Version Control for Gas Town & Beads](https://github.com/gastownhall/gastown/discussions/363) — operation-log gap, conflict handling, agent/session/model/token provenance.
- [DoltHub: A Day in Gas Town](https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/) — external explanation of Beads as coding-agent memory/task system и continuity after PR review.
- [DoltHub: Restoring Beads Classic](https://www.dolthub.com/blog/2026-04-02-restoring-beads-classic/) — solo Beads users, Embedded Dolt, concurrency-safety concern.
- Beads CLI Reference — generated reference for bd v1.0.5 и its live command surface: https://gastownhall.github.io/beads/cli-reference
- Beads README — setup, `AGENTS.md` integration, essential commands, persistent memory guidance и feature list: https://github.com/gastownhall/beads
- DoltHub, “Common Beads Classic Workflows” — single-agent/default рабочий процесс, multi-clone рабочий процесс, Dolt remote behavior и opacity/tradeoffs after v1.0.1: https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/
- Beads Architecture — Dolt write/read path, auto-committed writes, SQL queries, backup/export и distribution rationale: https://github.com/gastownhall/beads/blob/main/docs/ARCHITECTURE.md
- Gas Town CHANGELOG — Convoy Dashboard, two-level Beads architecture, multi-agent changes и ephemeral Polecat lifecycle: https://github.com/gastownhall/gastown/blob/main/CHANGELOG.md
* [Beads Quick Start](https://gastownhall.github.io/beads/getting-started/quickstart) — очередь готовых задач, dependency explanation, hash IDs, hierarchy, role configuration и Dolt sync рабочий процесс.
* [Beads Multi-Agent Coordination](https://gastownhall.github.io/beads/multi-agent) — routing, cross-repo dependencies, pinned work и handoff primitives.
* [Beads Architecture Overview](https://gastownhall.github.io/beads/architecture) — Dolt as источник истины, server/embedded modes, recovery sequence и explicit not-suitable cases.
* [DoltHub: A Day in Gas Town](https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/) — external history of Beads as coding-agent memory system и Dolt migration motivation.
- Gas Town design doc [Witness AT Team Lead](https://github.com/gastownhall/gastown/blob/main/docs/design/witness-at-team-lead.md) — future/not-implemented источник по transport-layer replacement, Agent Teams blockers, no per-teammate cwd, no teammate resumption, token cost и recovery via Beads state.

### Gas Town orchestration: роли, scheduler, recovery, changelog и future architecture

- Gas Town docs — Molecules: [https://github.com/gastownhall/gastown/blob/main/docs/concepts/molecules.md](https://github.com/gastownhall/gastown/blob/main/docs/concepts/molecules.md) — источник по Formula → Protomolecule → Molecule/Wisp lifecycle, root-only vs poured workflows, `gt prime`, `gt done`, `gt patrol report`.
- Gas Town docs — Scheduler: [https://github.com/gastownhall/gastown/blob/main/docs/design/scheduler.md](https://github.com/gastownhall/gastown/blob/main/docs/design/scheduler.md) — источник по `scheduler.max_polecats`, `batch_size`, `spawn_delay`, direct vs deferred dispatch, capacity, circuit breaker и safety properties.
- Gas Town docs — Witness at Team Lead: [https://github.com/gastownhall/gastown/blob/main/docs/design/witness-at-team-lead.md](https://github.com/gastownhall/gastown/blob/main/docs/design/witness-at-team-lead.md) — источник по stuck/crash handling, handoff/nudge и transition toward event-driven teammate hooks.
- Gas Town mayor role template — propulsion principle, hook startup behavior, capability ledger и “File It, Sling It” decision tree: https://github.com/gastownhall/gastown/blob/main/internal/templates/roles/mayor.md.tmpl
- Gas Town discussion #363 — non-canonical but useful limitation signal around operation log, automatic workspace management и auto-merge: https://github.com/gastownhall/gastown/discussions/363
- Gas Town [CHANGELOG](https://github.com/gastownhall/gastown/blob/main/CHANGELOG.md) — источник по queue/dispatch engine, OTEL, dog subsystem, event-driven lifecycle, FIX_NEEDED loop, pressure checks, typed state и release-history evidence of operational stress.
- Gas Town [Releases](https://github.com/gastownhall/gastown/releases) — источник по concrete release items: `FIX_NEEDED`, Witness dispatch messages, direct/PR merge strategies, background nudges, GitHub sheriff, partial clones, pressure checks и event-driven polecat lifecycle.

### Beads: эксплуатационные ограничения, troubleshooting и release-risk

- Beads docs, [`TROUBLESHOOTING.md`](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md) — shadow database, configured server unreachable, Dolt journal corruption, database locked, circuit breaker, merge conflicts, ready/dependency diagnostics, duplicate issues, sandboxed environments.
- Issue `gastownhall/beads#3313`, [`bd admin cleanup / bd admin compact fail with not yet supported in embedded mode`](https://github.com/gastownhall/beads/issues/3313) — concrete maintenance failure around cleanup/compaction и heartbeat-bloat incident.
- Beads releases, [`gastownhall/beads/releases`](https://github.com/gastownhall/beads/releases) — release-level signal around embedded mode, `bd ready --explain`, integration charter, rules audit/compact и data-corruption fixes.
- Beads [`README`](https://github.com/gastownhall/beads) — повторно использован для режимов хранения: embedded mode, server mode, `.beads/issues.jsonl` как экспорт/обмен, но не источник истины и не полная резервная копия.
- Beads [`TROUBLESHOOTING.md`](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md) — новый источник по диагностике: `BD_DEBUG`, `BD_DEBUG_RPC`, `BD_DEBUG_SYNC`, `BD_DEBUG_ROUTING`, `BD_DEBUG_FRESHNESS` и подсистемы, которым нужна видимость.
- Beads [`Releases`](https://github.com/gastownhall/beads/releases) — повторно, но глубже использован как негативный эксплуатационный источник по gated v1.0.5 и риску migration `0043` для multi-machine sync.
- [Beads Documentation](https://gastownhall.github.io/beads/) — основной источник по Beads as Dolt-powered issue tracker for AI-supervised coding workflows, AI-native workflows, formulas и multi-agent coordination.
- [Beads Multi-Agent Coordination](https://gastownhall.github.io/beads/multi-agent/coordination) — источник по pinning, handoff, parallel work, fan-out/fan-in, file reservations и issue locking.
- [Beads Codex Integration](https://gastownhall.github.io/beads/integrations/codex) — источник по AGENTS.md, skill setup, hooks, SessionStart/PreCompact/PostCompact/UserPromptSubmit и `bd prime` injection.
- [`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime) — источник по cheap AI context rehydration after session start/compaction, MCP vs CLI output size и PRIME.md override.
- Beads Documentation: [https://gastownhall.github.io/beads/](https://gastownhall.github.io/beads/) — основной источник третьего pass: Beads as Dolt-powered issue tracker for AI-supervised coding workflows, AI-native workflows, dependency-aware execution, formulas и multi-agent coordination.
- Beads Core Concepts: [https://gastownhall.github.io/beads/core-concepts](https://gastownhall.github.io/beads/core-concepts) — источник по issues, IDs, priorities, labels, dependency types (`blocks`, `parent-child`, `discovered-from`, `related`), очередь готовых задач и formulas.
- Beads Molecules: [https://gastownhall.github.io/beads/workflows/molecules](https://gastownhall.github.io/beads/workflows/molecules) — источник по molecule as persistent formula instance, step dependencies, parent-child issues, `bd ready`, lifecycle и pinning.
- Beads Multi-Agent / Routing / Coordination: [https://gastownhall.github.io/beads/multi-agent](https://gastownhall.github.io/beads/multi-agent), [routing](https://gastownhall.github.io/beads/multi-agent/routing), [coordination](https://gastownhall.github.io/beads/multi-agent/coordination) — источник по routing, cross-repo deps, pinning, handoff, fan-out/fan-in, file reservations и issue locking.
- Beads Codex Integration: [https://gastownhall.github.io/beads/integrations/codex](https://gastownhall.github.io/beads/integrations/codex) — источник по `bd setup codex`, Beads skill, AGENTS.md guidance, lifecycle hooks и `bd prime` injection/recovery after compaction.
- [`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime) — AI-optimized context rehydration, MCP vs CLI output size, SessionStart hooks, memories-only compact mode.
- [Beads Codex integration](https://gastownhall.github.io/beads/integrations/codex) — Codex hooks, compaction recovery и post-compact refresh path.
- [DoltHub: Two Weeks in Gas Town](https://www.dolthub.com/blog/2026-04-16-two-weeks-in-gastown/) — Gas Town as workspace manager over Beads; Beads as institutional memory after compaction.
* [Beads Codex integration](https://gastownhall.github.io/beads/integrations/codex) — lifecycle hooks for `bd prime`, compaction recovery marker и Codex-specific context injection constraints.
* [Beads Claude Code integration](https://gastownhall.github.io/beads/integrations/claude-code) — `bd prime` as compact context injection, JSON-first agent commands, push-before-session-end discipline.
- Beads [Releases](https://github.com/gastownhall/beads/releases) — источник по gated v1.0.5 migration и multi-machine Dolt sync risk.

### Прочие источники и заметки к проверке

- Maggie Appleton — Gas Town’s Agent Patterns, Design Bottlenecks, и Vibecoding at Scale: [https://maggieappleton.com/gastown](https://maggieappleton.com/gastown) — secondary interpretive источник по design/planning bottleneck и orchestration patterns.

## Поисковые формулировки и углы будущих проверок

Этот раздел сохранён как рабочая память поисковых направлений. Хронология проходов снята: формулировки сгруппированы как единый набор проверочных углов, чтобы они не задавали отдельную структуру досье.

- `gastownhall beads troubleshooting shadow database dolt journal corruption sandbox Codex`
- `beads admin cleanup compact embedded mode heartbeat bloat issue`
- `beads ready dependencies duplicate issues dep tree cycles`
- `beads releases bd ready --explain integration charter rules compact`
- `Beads Classic Workflows Dolt remote multi-clone conflict v1.0.1`
- `Beads troubleshooting BD_DEBUG_SYNC BD_DEBUG_ROUTING BD_DEBUG_FRESHNESS`
- `Beads gated release migration 0043 multi-machine bd dolt sync`
- `Beads embedded mode server mode issues.jsonl источник истины backup`
- `Beads auto routing maintainer contributor local planning upstream PR`
* `Gas Town changelog event-driven polecat lifecycle FIX_NEEDED awaiting_verdict`
* `Gas Town queue dispatch engine pressure checks OTEL dog subsystem`
* `Gas Town Witness Agent Teams no teammate working directory session resumption token cost`
* `Beads release gated migration 0043 multi-machine dolt sync`
* `Gas Town releases direct PR merge strategy witness dispatch messages`
* `Gas Town future architecture transport layer Beads ledger remains`
* `Gas Town reference Beads routing routes.jsonl prefix hq gp wyv`
* `Gas Town glossary MEOW Molecular Expression of Work`
* `Exploring Gas Town Beads persistent externalized task state context window`
* `Hacker News Welcome to Gas Town Beads bugs merge conflicts accountability`
* `Gas Town external critique review bottleneck token cost multi agent orchestration`
- durable identity: role beads и agent beads;
- durable work: Beads ledger, town/rig prefixes, canonical storage;
- durable рабочий процесс: formulas, protomolecules, molecules, wisps;
- durable dispatch: convoys, sling contexts, scheduler capacity;
- durable supervision: Witness, Deacon, Dogs, patrol cycles;
- durable recovery: nudges, handoff, checkpointed poured workflows, circuit breakers.
- `Beads Documentation Dolt-powered issue tracker AI-supervised coding workflows dependency-aware execution`
- `Beads Core Concepts dependency types discovered-from blocks очередь готовых задач`
- `Beads Architecture Dolt источник истины embedded server mode multi-writer when not to use`
- `Beads Codex Integration bd prime SessionStart PreCompact PostCompact UserPromptSubmit`
- `Beads Agent Coordination pin hook handoff fan-out fan-in file reservations issue locking`
- `Beads workflows formulas molecules gates wisps .beads-wisp`
- `Gas Town Beads central data plane граф работы agent memory`
- `Gas Town molecules formula protomolecule wisp root-only poured checkpoint recovery`
- `Gas Town scheduler max_polecats batch_size deferred dispatch capacity`
- `Gas Town Witness handoff nudge stuck agents Deacon Dogs`
- `Gas Town two-level beads architecture town rig agent bead role bead`
- `Gas Town good bad ugly Beads maximalist polecats full sessions GUPP`
- `A Day in Gas Town DoltHub Beads .beads AGENTS.md agent memory`
- `Steve Yegge Welcome to Gas Town Mayor Crew Polecats Refinery Witness Deacon Dogs`
- `Gas Town GitHub README Mayor Town Rig Polecats hooks worktrees architecture`
- `Gas Town Docs Mayor Hub screenshot`
- `Beads coding agent memory system bd ready bd update --claim bd dep add bd remember bd prime`
- `Gas Town GUPP hooks molecules wisps pinned bead`
- `Gas Town agent not session Role Bead Agent Bead mail hook administrative state`
- `Gas Town Refinery merge queue Witness stuck agents Deacon Dogs patrol`
- `Gas Town tmux discipline cost chaotic multi-agent coding agents`
- `Beads architecture Dolt источник истины multi writer agents recovery`
- `Beads bd prime Codex SessionStart compaction UserPromptSubmit`
- `Beads bd gate human timer GitHub run PR bead wait conditions`
- `Gas Town Beads mail protocol POLECAT_DONE MERGE_READY MERGED`
- `Gas Town Beads operation log agent identity session model token count`
- `DoltHub Restoring Beads Classic single agent Embedded Dolt`
- `Beads устойчивый граф работы AI coding agents Dolt`
- `Beads bd prime Codex hooks compaction recovery`
- `Beads bd gate human approval GitHub run wait condition`
- `Beads multi agent coordination handoff fan-out fan-in file reservations`
- `Dolt Beads Gas Town agentic memory structured versioned data`
- `persistent issue graph agent orchestration durable state`
- `Beads CLI reference bd prime bd gate bd ready bd remember`
- `Beads Dolt workflows single agent multiple clone remote conflicts`
- `Gas Town mayor role template file it sling it hook execute`
- `Gas Town changelog two-level beads Convoy Dashboard ephemeral polecats`
- `Gas Town Beads operation log agent-first version control`
* `Beads Quick Start очередь готовых задач blocked dependencies bd ready explain`
* `Beads Codex integration hooks SessionStart PreCompact PostCompact UserPromptSubmit bd prime`
* `Beads Claude Code integration bd prime 1-2k tokens json commands`
* `Beads multi-agent routing pin handoff cross repo dependencies`
* `Gas Town Bill de Hora Bead Dolt tmux abstractions`
* `DoltHub A Day in Gas Town Beads memory system Dolt`

## Кандидаты на иллюстрации

Кандидаты возвращены внутрь `GAS_TOWN_METHOD_DOSSIER.md` и сгруппированы по смыслу. Это не финальный asset manifest: перед вставкой на сайт изображения нужно отдельно проверить, сохранить локально и привязать к конкретным местам текста.

### Beads и persistent work graph

* Layer diagram: Beads / protocol / capacity / recovery / observability.
* “Transport changes, ledger remains” diagram: tmux vs Agent Teams over same Beads + mail + molecule layer.
* Beads Quick Start очередь готовых задач example: flat tracker vs `bd ready --explain` with blocked dependencies.
* Three-layer Gas Town diagram: runtime sessions / Beads-Dolt substrate / orchestration roles.
* Multi-agent routing diagram from Beads docs: main repo coordinator routes frontend/backend work.
* Dolt write/read/sync path diagram: `bd create` → Dolt auto-commit → `bd dolt push/pull`.
- Beads CLI command taxonomy / generated CLI reference: 106 commands grouped by task, dependency, memory, mail, рабочий процесс, integration, recovery.
- `AGENTS.md` minimal Beads instructions as an onboarding surface: `bd prime`, `bd ready`, `bd show`, `bd update --claim`, `bd close`, `bd remember`.
- DoltHub рабочий процесс diagrams: single-agent single-remote и multi-agent/multiple-clone workflows.
- Gas Town changelog screenshots for Convoy Dashboard, two-level Beads architecture и ephemeral Polecat lifecycle.
- `fig-gastown-beads-first-reading` — Beads docs + Gas Town README — Beads/data plane at center; Mayor/Crew/Polecats/Refinery/Witness as layers around it — Чтобы не объяснять Gas Town as swarm-first.
- `fig-gastown-to-persistent-work-graph` — new mechanism dossier — Стрелка: Gas Town case → Beads mechanism → transferable loop primitives — Показывает, почему Beads внутри истории, но механизм отдельно в теории.
- `fig-beads-vs-multi-pass-document-workflow-state` — Beads docs + our multi-pass document workflow design notes — Bead/status/gate/prime vs pass/status/ledger/heartbeat — Полезно для будущего проектного прохода по многопроходному документному процессу.
- `fig-gastown-beads-two-plane-architecture` — [Beads Architecture](https://gastownhall.github.io/beads/architecture), Gas Town architecture docs — Dolt источник истины → town-level Beads → rig-level Beads → agents/hooks/mail/work. — Центральная схема для Gas Town как глубокий якорь.
- `fig-beads-prime-compaction-recovery` — [`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime), [Beads Codex integration](https://gastownhall.github.io/beads/integrations/codex) — SessionStart → `bd prime`; PreCompact memories-only check; PostCompact marker; UserPromptSubmit refresh. — Прямо полезно для будущей архитектуры многопроходного документного процесса.
- `fig-beads-gate-lifecycle` — [`bd gate`](https://gastownhall.github.io/beads/cli-reference/gate) — Gate types: human/timer/GitHub run/PR/bead; resolved/escalated paths; blocked issue returns to очередь готовых задач. — Хороший visual для long-running orchestration without live session.
- `fig-gastown-operation-log-gap` — [GitHub discussion #363](https://github.com/gastownhall/gastown/discussions/363) — Current reconstruction from git log + beads history + mail vs proposed operation log with agent/session/model/token. — Нужна для честной критики: даже Gas Town lacks perfect provenance.
- `fig-beads-solo-vs-fleet` — [Restoring Beads Classic](https://www.dolthub.com/blog/2026-04-02-restoring-beads-classic/), [Two Weeks in Gas Town](https://www.dolthub.com/blog/2026-04-16-two-weeks-in-gastown/) — Single-agent Beads Classic → multi-agent Gas Town/Gas City/Wasteland. — Помогает не смешивать Beads as mechanism и Gas Town as fleet orchestration.
- `fig-gastown-two-tier-beads-flow` — [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) — Figure 6: Two-Tier Beads Flow. — Нужна для различения rig-level и town-level work. — Высокий приоритет.
- `fig-beads-command-table` — [Beads GitHub](https://github.com/gastownhall/beads) — Команды `bd ready`, `bd update --claim`, `bd dep add`, `bd prime`, `bd remember`. — Лучше как текстовая вставка или таблица, не обязательно картинка. — Можно сделать локальную схему самому.
- `fig-beads-task-graph-memory` / `assets/theory-images/beads-task-graph-memory.svg` — [Beads GitHub](https://github.com/gastownhall/beads) / [Introducing Beads](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a) — Локальная схема: Beads как граф задач, зависимостей, claim-состояний и памяти агента. — Нужна для перехода от markdown-plan к task graph и external task memory. — Раздел «Граф задач как внешняя память агента» или начало Gas Town dossier. — Уже локально вставлено в теорию; можно переиспользовать.
- `fig-gastown-molecules-lifecycle` / candidate — [Gas Town Molecules](https://github.com/gastownhall/gastown/blob/main/docs/concepts/molecules.md) — Formula → `bd cook` → Protomolecule → `bd mol pour` / `bd mol wisp --root-only`; root-only vs poured. — Показывает, как Gas Town выбирает между дешёвым inline рабочий процесс и durable checkpointed рабочий процесс. — Раздел molecules / рабочий процесс state. — Кандидат; лучше перерисовать локально.
- `fig-gastown-two-level-beads` / candidate — [Gas Town Architecture](https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md) — Town-level `hq-*` beads vs rig-level project beads; agent beads и redirects. — Показывает separation of coordination state и implementation state. — Раздел Beads architecture / externalized agent identity. — Кандидат для собственной схемы.
- `fig-beads-core-dependency-types` / candidate — [Beads Core Concepts](https://gastownhall.github.io/beads/core-concepts) — Issue object + four dependency types: `blocks`, `parent-child`, `discovered-from`, `related`, и which affect очередь готовых задач. — Очень полезно для объяснения Beads как graph substrate, а не списка задач. — Центральный Beads-подраздел Gas Town. — Новый кандидат; лучше перерисовать локально.
- `fig-beads-dolt-architecture` / candidate — [Beads Architecture](https://gastownhall.github.io/beads/architecture) — Dolt DB → local history → remote; embedded vs server mode; различие между source of truth и экспортом. — Показывает, почему Beads не просто JSONL/markdown: есть versioned SQL и recovery model. — Раздел Beads плоскость данных и управления. — Новый кандидат для собственной схемы.
- `fig-beads-agent-entry-ritual` / candidate — [Beads GitHub README](https://github.com/gastownhall/beads) + [Codex Integration](https://gastownhall.github.io/beads/integrations/codex) — `bd prime` → ready/show/update/close → `bd remember`; SessionStart / compaction recovery hooks. — Прямо полезно для будущего многопроходного документного процесса: recovery context should be injected by lifecycle, not rediscovered by reading everything. — Раздел Beads/Codex/multi-pass-document-workflow lessons. — Новый кандидат.
- `fig-beads-coordination-patterns` / candidate — [Beads Agent Coordination](https://gastownhall.github.io/beads/multi-agent/coordination) — Pinning, hook, sequential handoff, parallel work, fan-out/fan-in, file reservations. — Показывает how work becomes assignable и handoff-able. — Раздел multi-agent coordination / Gas Town roles. — Новый кандидат.
- `fig-beads-gates-and-wisps` / candidate — [Beads Gates](https://gastownhall.github.io/beads/workflows/gates), [Beads Wisps](https://gastownhall.github.io/beads/workflows/wisps) — Persistent molecule vs ephemeral wisp; gates as human/timer/GitHub blockers. — Помогает объяснить durable vs ephemeral orchestration. — Раздел molecules/wisps/workflows. — Новый кандидат.
- `fig-beads-as-data-plane` — Beads docs + Gas Town — Beads в центре, вокруг roles и agent sessions — Главная картинка Gas Town story.
- `fig-persistent-work-graph-primitives` — mechanism dossier — Node types: work item, dependency, owner, gate, handoff, recovery, history — Главная картинка theory mechanism.
- `fig-bd-prime-compaction-recovery` — `bd prime` + Codex integration — SessionStart/compaction → `bd prime` → restored context — Для раздела про context rehydration.
- `fig-bd-gate-durable-wait` — `bd gate` docs — Issue blocked by gate until human/CI/timer/bead resolution — Для gates/human-in-the-loop section.
* Beads Quick Start flat tracker vs `bd ready --explain` comparison.
* Beads Codex hook lifecycle diagram from integration docs.
* Beads Multi-Agent Coordination routing diagram.
* DoltHub “A Day in Gas Town” image/thread about Beads moving from Git+SQLite to Dolt.
* External three-strata sketch for Gas Town: Bead / Dolt / tmux.
* Sync-risk map: Dolt state, migrations, multi-machine push/pull, recovery playbook.
* Transport diagram: tmux today vs Agent Teams future, same Beads ledger underneath.
- Диаграмма Beads operational substrate: `bd` CLI → metadata → Dolt embedded/server mode → remote sync → issue graph → ready queue; рядом troubleshooting paths.
- Схема failure/recovery: shadow database → diagnostics → metadata/server check → repair; Dolt journal corruption → safe recovery vs dangerous lock-file deletion.
- Схема dependency semantics: `blocks` vs `related` vs `parent-child` vs `discovered-from`; только `blocks` влияет на `bd ready`.
- `fig-beads-classic-single-agent` — [DoltHub Common Beads Classic Workflows](https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/) — Схема single-agent / single-project / single-remote workflow. — Показать минимальный режим Beads до Gas Town-scale orchestration.
- `fig-beads-multi-clone-shared-remote` — [DoltHub Common Beads Classic Workflows](https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/) — Схема multiple agents / multiple clones / shared Dolt remote. — Объяснить sync/merge-conflict tradeoff при параллельных агентах.
- `fig-beads-debug-subsystems` — [Beads Troubleshooting](https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md) — Таблица debug-флагов: RPC, sync, routing, freshness. — Показать, что persistent work graph требует наблюдаемости, а не только хранения.
- `fig-beads-gated-release-warning` — [Beads Releases](https://github.com/gastownhall/beads/releases) — Warning block v1.0.5: gated release, migration `0043`, do not upgrade/push/pull. — Дать сильный контрпример к романтизации durable state: migration/sync can fail dangerously.
- `fig-gastown-beads-routing-prefixes` — Gas Town Reference — `hq-*`, `gp-*`, `wyv-*` → different Beads locations via `routes.jsonl`. — Показать адресное пространство Gas Town и why durable state needs routing.
- `fig-gastown-external-internal-state-model` — Koziol + Beads architecture docs — контекстное окно агента outside vs persistent Beads state inside repo/Dolt. — Простая картинка для читателя: why Beads matters.

### Архитектура Gas Town, роли и рабочие пространства

* Timeline: release-history pressure points from initial Gas Town to queue/OTEL/event-driven lifecycle.
- Mayor role decision tree: coordination vs code change vs trivial change; “File it, sling it.”
- `fig-gastown-worker-roles` — [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) — Figure 5: Gas Town’s Worker Roles. — Быстро показывает Mayor, Crew, Polecats, Refinery, Witness, Deacon, Dogs и Overseer. — Высокий приоритет, если можно легально/технически сохранить.
- `fig-gastown-formulas-cooking` — [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) — Figure 10: Formulas и Cooking. — Показывает chain/template/source-form для molecules. — Средний/высокий приоритет.
- `fig-gastown-ndi` — [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) — Figure 11: Nondeterministic Idempotence. — Полезна для объяснения durability/recovery without Temporal replay. — Средний приоритет.
- `fig-gastown-patrols` — [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) — Figure 12: Gas Town’s Patrols. — Поддерживает раздел про service agents / patrol loops / exponential backoff. — Средний приоритет.
- `fig-gastown-convoy-cli` — [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) — Figure 14: Convoy CLI display. — Даёт реальную поверхность tracking unit. — Средний приоритет.
- `fig-gastown-basic-рабочий процесс` — [Gas Town GitHub](https://github.com/gastownhall/gastown) — Mermaid sequence: You → Mayor → Convoy → Agent → Hook. — Лучше всего подходит как простая схема для сайта. — Возможно уже сохранено локально; проверить assets.
- `fig-gastown-architecture-readme` — [Gas Town GitHub](https://github.com/gastownhall/gastown) — Mermaid architecture: Mayor, Town, Rigs, Crew, Hooks, Polecats. — Показывает structural workspace view. — Возможно уже сохранено локально.
- `fig-gastown-problems-view` — [Gas Town GitHub](https://github.com/gastownhall/gastown) / `gt feed --problems` — Состояния GUPP Violation / Stalled / Zombie / Working / Idle. — Особенно полезно для будущего раздела про monitoring long-running agents. — Нужно проверить, есть ли screenshot/docs image.
- `fig-gastown-architecture` / `assets/theory-images/gastown-architecture.svg` — [Gas Town GitHub](https://github.com/gastownhall/gastown) — Локальная схема архитектуры Gas Town: Mayor, town workspace, rigs, crew, hooks, polecats и git worktrees. — Показывает, что Gas Town — не один чат, а организация рабочих областей, ролей, hooks, worker agents и Git-границ. — В начале раздела о Gas Town или рядом с ролями. — Уже локально вставлено.
- `fig-gastown-mayor-hub` / `assets/theory-images/gastown-mayor-hub.webp` — [Gas Town Docs](https://docs.gastownhall.ai/) — Mayor’s Hub как поверхность наблюдения и выбора. — Поддерживает мысль «видимость без чтения»: Mayor нужен не как ещё один лог, а как интерфейс управляемой видимости. — Раздел Mayor / human-facing surface. — Уже локально вставлено.
- `fig-gastown-basic-рабочий процесс` / `assets/theory-images/gastown-basic-рабочий процесс.svg` — [Gas Town GitHub](https://github.com/gastownhall/gastown) — Базовая петля: пользователь, Mayor, Convoy, Agent, Hook и возврат состояния. — Показывает, как задача перестаёт быть сообщением в чате и становится цепочкой действий с диспетчеризацией, исполнителем, hook и состоянием. — Раздел GUPP/hooks/molecules/wisps или рабочий процесс. — Уже локально вставлено.
- `fig-anthropic-multi-agent-process-diagram` / `assets/theory-images/anthropic-multi-agent-process-diagram.webp` — [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) — Многоагентский процесс Anthropic с ведущим агентом, подагентами, памятью и citation agent. — Не Gas Town-specific, но полезен как фон формы: долгоживущая задача восстанавливается через роли, подзадачи, память и финальный отчёт, а не через одну длинную сессию. — Ввод к долгоживущим задачам / recovery, если нужна внешняя аналогия. — Уже локально вставлено в теорию; использовать осторожно, чтобы не смешать с Gas Town.
- `fig-gastown-scheduler-capacity` / candidate — [Gas Town Scheduler](https://github.com/gastownhall/gastown/blob/main/docs/design/scheduler.md) — Direct dispatch vs deferred dispatch; `max_polecats`, `batch_size`, `spawn_delay`, circuit breaker. — Очень полезно для связи Gas Town с нашим многопроходным документным процессом: concurrency/обратное давление должны быть частью системы. — Раздел scheduler / recovery / loop framework. — Кандидат для собственной схемы.
- `fig-gastown-witness-recovery` / candidate — [Witness design](https://github.com/gastownhall/gastown/blob/main/docs/design/witness-at-team-lead.md) — Crash/stuck/test-failure/merge-conflict → respawn/nudge/block/reassign/retry. — Поддерживает мысль, что service agents are recovery loops, not decorative roles. — Раздел Witness/Deacon / monitoring. — Кандидат для собственной схемы.
* Release-history timeline: initial Gas Town → queue/dispatch → event-driven lifecycle → pressure checks.
- `fig-gastown-meow-decomposition` — Gas Town Glossary — Goal → Epics/Formulas/Molecules → atomic trackable work units. — Объяснить MEOW как formalized decomposition, not planning prose.
- `fig-gastown-accountability-bottleneck` — Hacker News discussion + theory synthesis — Agent throughput ↑ vs human review/ownership capacity. — Контрапункт к naive multi-agent scaling.

### Очереди, зависимости, gates и back-pressure

* Failure-mode map: dead polecat, sync migration break, queue overload, merge failure, compaction/handoff gap.

### Recovery, hooks, наблюдаемость и service agents

* Codex integration hook lifecycle: `SessionStart` → `PreCompact` → `PostCompact marker` → `UserPromptSubmit refresh`.
- Схема sandboxed runtime risk: Codex/Claude Code sandbox → cannot stop server → out-of-sync/hash mismatch → sandbox mode / doctor / fallback.

### Дополнительные визуальные кандидаты Gas Town

* State-machine diagram: `assigned → running → done → awaiting_verdict → fix_needed/merged`.
* State machine: polecat assigned/running/done/awaiting_verdict/FIX_NEEDED/merged.

## Открытые вопросы и следующий возможный проход

Открытые вопросы сведены в единый список без привязки к номерам проходов.

- Нужно ли разделить Gas Town-досье на Beads data plane, Gas Town orchestration, и external critiques? После второго прохода это стало ещё более оправдано.
- Нужно ли извлечь из Gas Town отдельный mini-dossier для нашего многопроходного документного процесса: capacity-controlled dispatch, heartbeat, watchdog, circuit breaker, resume/handoff?
- Нужно ли скачать/перерисовать Molecules, Scheduler и Two-level Beads diagrams as local source assets before writing theory?
- Нужно ли сделать отдельный проход с раскрытием источников по Gas Town GitHub README и docs, потому что текущая теория уже содержит локальные схемы, но досье сейчас не перепроверяет исходные README/details.
- Нужно ли разделить Beads и Gas Town на два досье: Beads как task-memory/data-plane и Gas Town как multi-agent organization. Сейчас они связаны, но Beads имеет самостоятельную важность.
- Насколько глубоко переносить игровую терминологию Gas Town в будущую теорию. Текущая позиция: названия сохранять как источникные labels, но переносимый смысл формулировать через роли, состояние, очередь, recovery и service loops.
- Нужно ли в будущем досье раскрыть `convoys`, `orders`, `epics`, `plugins`, `tmux`, cost/routing и model-selection details. Текущая теория перечисляет их как platform primitives, но не раскрывает.
- Как связать Gas Town с будущим многопроходным документным процессом: semantic heartbeats, resumable state, external pass artifacts, service pass, merge/refinery-like queue и watchdog/witness-like monitoring.
- Нужно ли отдельно анализировать право/безопасность: при большом числе agents возрастают не только throughput и noise, но и риски прав, секретов, destructive commands и hidden drift.
- Нужно ли в будущей теории явно начинать Gas Town subsection с Beads, а не с Mayor/roles, чтобы читатель сразу видел граф работы/data plane?
- Нужно ли сделать отдельный mechanism dossier не `BEADS.md`, а шире: `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`, где Beads будет главным примером alongside Spec Kit tasks, BMAD stories и GSD state?
- Нужно ли перенести Beads Codex integration в план улучшения многопроходного документного процесса: SessionStart `bd prime`, post-compaction refresh marker, one-time context refresh after compaction?
- Нужно ли отдельно сравнить Beads with GitHub Issues/Linear/Jira: docs themselves say Beads is not for large teams, real-time collaboration, rich media, cross-repo tracking at organizational scale.
- Нужно ли для сайта перерисовать Beads diagrams rather than screenshot docs: dependency types, Dolt источник истины, agent entry ritual, coordination patterns?
- Нужен ли отдельный `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`, где Beads будет главным примером, а `tasks.md`, BMAD story files, GSD state и our multi-pass document workflow ledgers — сравнительными случаями?
- Какие элементы Beads реально переносимы в наш многопроходный документный процесс без Dolt: `prime`, gates, operation log, issue metadata, очередь готовых задач, blocked graph?
- Должна ли многопроходный документный процесс иметь свой lightweight gate layer для CI/human review/timer/usage-limit waits, вместо долгих живых subagent sessions?
- Нужно ли отдельно раскрыть `bd mail` / Gas Town mail protocol через source pass, если будущая теория будет говорить о inter-agent communication?
- Где граница между Beads as solo-agent memory и Gas Town as multi-agent orchestration: показывать это в одной главе или двумя связанными подразделами?
- Нужно ли в Gas Town-главе объяснять текущий Dolt-backed Beads отдельно от старого JSONL mental model, чтобы не вводить читателя в заблуждение?
- Где провести границу между Gas Town as orchestration workspace и Beads as reusable устойчивый граф работы mechanism?
- Нужно ли отдельное сравнение Beads command surface with our multi-pass document workflow status/ledger/passes model before rewriting the theory?
* Какой минимальный subset команд Beads нужен агенту, чтобы получить пользу без перегрузки 106-command surface?
* Может ли многопроходный документный процесс использовать готовый Beads-like очередь готовых задач, или нужен более узкий pass/рабочий процесс graph без полного issue-tracker слоя?
* Насколько Codex hook lifecycle можно надёжно использовать для long-running document passes, если часть работы идёт не в интерактивной Codex session, а через external wrapper?
* Где граница между Beads as local-first agent substrate и normal project-management systems вроде Linear/Jira?
* Насколько future `Witness AT Team Lead` стоит использовать в основной теории, если документ explicitly says not yet implemented?
* Можно ли из Gas Town release history вывести generic requirements for многопроходный документный процесс: queue, heartbeat, pressure gates, typed status, recovery after compaction?
* Где в Gas Town заканчивается Beads и starts protocol/recovery OS?
* Нужно ли добавить отдельный раздел про release-history as source evidence for agentic systems, not only docs/blogs?
* Нужно ли в теории отдельно объяснять prefix-based routing как обязательную часть multi-workspace agent state, а не частную деталь Gas Town?
* Какой минимальный язык декомпозиции нужен нашему многопроходному документному процессу: достаточно ли pass/status/ledger или нужен Beads-like formula/molecule слой?
* Насколько внешнюю критику HN стоит вводить в основной текст: как короткий risk signal или как отдельный anti-pattern block?
* Как не дать Beads/Gas Town перегрузить будущую главу терминологией, если переносимый смысл проще: durable граф работы, routing, очередь готовых задач, recovery, ownership?

## Языко-стилевые и редакционные замечания
### Языко-стилевые замечания

В добавленных разделах английские слова оставлены только как имена точных механизмов, команд, полей и метки источников: `bd`, `gp-*`, `hq-*`, `routes.jsonl`, `BD_DEBUG_ROUTING`, MEOW, Beads, Gas Town. Обычные объяснения переведены: `state` — “состояние”, `review` — “ревью/проверка” по контексту, `accountability` — “ответственность”, `friction` — “трение”, `рабочий процесс` — “рабочий процесс”. Внешние английские формулировки не оставлены длинными цитатами, а пересказаны по-русски со ссылками.
