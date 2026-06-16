# 04 — Внешний поиск и восстановление источников

## Статус

Веб-доступ был доступен. Проход выполнен как source discovery для главы X: не рынок инструментов и не общий обзор оркестрации, а проверка внешней фактуры вокруг Gas Town и Beads, чтобы глава могла опираться на текущие первичные источники, а не только на уже собранный Атлас и фрагменты.

Главное ограничение прохода: не расширять главу в сторону LangGraph, Temporal, AutoGen, CrewAI и других соседних систем. Они могут быть полезны для отдельного сравнительного материала, но для текущей главы важнее восстановить точную механику Gas Town/Beads и отделить её от общих рассуждений о «многоагентности».

## external_discovery_log

### Использованные внешние источники

| Источник | Тип источника | Что проверено | Как использовать в главе |
|---|---|---|---|
| https://github.com/gastownhall/gastown | основной репозиторий Gas Town | В README Gas Town описан как multi-agent orchestration / workspace manager для Claude Code, GitHub Copilot, Codex, Gemini и других агентов; там же заявлены persistent work tracking, git-backed hooks, mailboxes/handoffs, переход от ручной координации к 20–30 агентам, хранение состояния работы в Beads ledger. | Использовать как основной источник для общей рамки: Gas Town не «ещё один агент», а среда, которая обслуживает множество рабочих потоков, роли, handoffs и состояние работы. |
| https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md | design-документ Gas Town | Подтверждены два уровня Beads: town-level beads для Mayor mail/messages, convoy coordination, strategic issues/decisions и role-definition beads; rig-level beads для bugs/features/tasks, merge requests/code reviews, molecules и rig-level agent beads. Также подтверждена таксономия ролей: Mayor, Deacon, Boot, Dogs, Witness, Refinery, Polecats, Crew. | Использовать для центрального различения главы: durable organization над множеством работ строится поверх отдельных work items. Особенно важно для границы с главой VII про PWG. |
| https://github.com/gastownhall/gastown/blob/main/docs/design/polecat-lifecycle-patrol.md | design-документ Gas Town | Подтверждены жизненный цикл polecat, patrol, события `RECOVERED_BEAD`, `GUPP_VIOLATION`, `ORPHANED_WORK`, сообщения Witness → Refinery (`MERGE_READY`) и Refinery → Witness (`MERGED`, `MERGE_FAILED`), а также идея convergent state на основе Beads/Dolt, git и tmux. | Это сильнее, чем прежняя линия `MAIL_PROTOCOL`, для объяснения того, как среда замечает потерянную/застрявшую/нарушенную работу и возвращает её в управляемый поток. Использовать как один из главных механизмов главы. |
| https://github.com/gastownhall/gastown/blob/main/docs/design/escalation.md | design-документ Gas Town | Подтверждено, что escalations создаются, когда автоматическое разрешение невозможно; они severity-routed, tracked as beads, имеют stale detection и re-escalation. Поток: Agent → Deacon → Mayor → Overseer; цепочка фиксируется в bead comments. | Использовать для границы между автоматическим обслуживанием потока и возвращением проблемы человеку/Mayor. Не превращать в отдельную подглаву о нотификациях. |
| https://github.com/gastownhall/gastown/blob/main/docs/design/scheduler.md | design-документ Gas Town | Подтвержден deferred dispatch через `gt sling`, `scheduler.max_polecats`, batch size, spawn delay, capacity/backpressure, convoy integration и набор safety properties: idempotency, pristine work bead, cross-rig guard, dispatch serialization, atomic scheduling, formula pre-cooking, fresh state on save. | Использовать ограниченно: как фактуру о том, что масштабирование требует capacity/backpressure, а не только возможности запустить больше сессий. |
| https://github.com/gastownhall/gastown/blob/main/docs/glossary.md | глоссарий Gas Town | Подтверждены GUPP, MEOW, Hook, Wisp, Molecule. GUPP формулируется как правило: если на hook есть работа, её нужно выполнять. | Использовать для точного объяснения hook/GUPP без свободной переформулировки. Это удобно для раздела о том, почему «работа висит на крючке» — не метафора, а часть рабочего контракта. |
| https://github.com/gastownhall/gastown/blob/main/internal/templates/roles/mayor.md.tmpl | внутренний шаблон роли Mayor | Подтверждено, что для Mayor `gt sling <bead-id> <rig>` описан как команда dispatch: spawn polecat, hook work, start session. | Использовать осторожно, как вспомогательную проверку роли Mayor и команды `gt sling`; лучше не строить на шаблоне основной публичный тезис. |
| https://docs.gastownhall.ai/ | публичная документация Gas Town | Подтверждены infrastructure roles: Mayor, Deacon, Witness, Refinery; структура town root / rigs / crew / polecats / refinery / witness / deacon; convoys как cross-rig tracking, auto-notification и historical record; common mistake — ждать подтверждения от polecat, когда работа уже hooked. | Использовать для более читабельного объяснения архитектуры и для конкретных терминов, которые не хочется брать только из README. |
| https://docs.gastownhall.ai/reference/ | reference-документация Gas Town | Подтверждены стандартный workflow через convoy → `gt sling`, коммуникационные команды, handoff/peek/nudge/seance, `gt prime`, patrol loops, Beads as control plane, bare repo / worktrees, state transitions as git commits. | Использовать как справочник для командного слоя и для связки «состояние не только в голове агента, а в контрольной плоскости». |
| https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 | авторская статья Steve Yegge | Подтверждены мотивация «tedium of running multiple Claude Code instances», заявка на 20–30 агентов, предупреждение о дороговизне/сырости/необходимости hands-on режима, роли Town/Rigs/Overseer/Mayor/Polecats/Refinery/Witness/Deacon/Dogs/Crew, объяснение hook/GUPP/agent-is-not-session. | Использовать как авторский контекст и предупреждение о цене/сырости подхода. Для текущих деталей реализации предпочитать docs/repo, потому что статья может отставать от текущей Dolt/Beads-версии. |
| https://gastownhall.github.io/beads/architecture | официальная документация Beads | Подтверждена актуальная архитектура Beads: Dolt is the sole storage backend, version-controlled SQL, source of truth, server mode for multi-writer, recovery path, sync path, multi-clone race, ограничения для large teams / real-time collaboration / cross-repo use. Документация обновлена 14 июня 2026. | Использовать для исправления возможной устаревшей линии: Beads в текущих docs — не просто JSON-файлы, а Dolt-backed база/ledger. Это важно для главы, потому что durable work state — не декоративный журнал. |
| https://gastownhall.github.io/beads/cli-reference/prime | официальная документация Beads | `bd prime` выдаёт AI-optimized context; поддерживает MCP/CLI; рассчитан на SessionStart hooks для Claude Code/Gemini/Codex и на восстановление после context compaction. Документация обновлена 13 июня 2026. | Использовать в главе как мост между durable state и агентской сессией: агенту не просто «напоминают контекст», ему подают текущую рабочую картину из Beads. |
| https://gastownhall.github.io/beads/cli-reference/gate | официальная документация Beads | `bd gate create` блокирует issue до разрешения; blocked issue не появляется в `bd ready`; gate types: human, timer, gh:run, gh:pr. | Использовать как один из точных механизмов ожиданий и внешних условий, но не уводить главу в тему проверки результата — это ближе к XI. |
| https://gastownhall.github.io/beads/multi-agent/coordination | официальная документация Beads | Подтверждены `bd pin`, `bd hook`, sequential handoff, fan-out/fan-in, split work, dependencies for merge. | Использовать как прямую фактуру для multi-agent coordination на уровне work graph: назначение, hook, handoff, fan-out/fan-in. |
| https://gastownhall.github.io/beads/multi-agent/routing | официальная документация Beads | Подтверждены routes config, pattern matching по title/labels/path prefix, auto-routing, cross-repo dependencies и hydration. Документация обновлена 14 июня 2026. | Использовать для темы маршрутизации работы между rig/repo, но аккуратно: это Beads-уровень, не весь Gas Town. |
| https://gastownhall.github.io/beads/integrations/codex | официальная документация Beads | Подтверждены Codex lifecycle hooks: SessionStart injects `bd prime`; PreCompact checks memories-only and warns; PostCompact marks refresh; UserPromptSubmit injects full `bd prime`; отдельно указано, что PreCompact alone is not enough because of Codex stdout behavior. Документация обновлена 14 июня 2026. | Использовать как свежую фактуру о том, как Beads входит в агентскую среду через hooks. Это поддерживает связку с главой VI, но в X нужно показать не hooks сами по себе, а обслуживание потока работ. |
| https://gastownhall.github.io/beads/workflows | официальная документация Beads | Подтверждены formulas/TOML, molecules as work graphs, parent-child/dependencies/progress, gates, wisps as ephemeral `.beads-wisp`, команды `bd pour`, `bd wisp`, `bd mol list`, `bd pin`, `bd hook`. | Использовать для объяснения molecules/wisps/gates без переписывания всего Beads Handbook. |
| https://gastownhall.github.io/beads/workflows/molecules | официальная документация Beads | Molecule описан как persistent instance of formula; steps map to issues; состояние синхронизируется через `.beads`; зависимости управляют `bd ready`; есть lifecycle, hooks, pinning. | Использовать для тезиса: повторяемый процесс в такой среде становится не только текстовой процедурой, а экземпляром рабочего графа. |

### Отклонённые или отложенные источники

| Источник / направление | Решение | Причина |
|---|---|---|
| Общий поиск по рынку multi-agent orchestration: LangGraph, Temporal, CrewAI, AutoGen, OpenAI Swarm/Agents SDK и т.п. | отложено | Это могло бы расширить главу, но текущий проход требует механизм главы через Gas Town/Beads. Широкое сравнение повысило бы риск расползания и повторения главы IX. |
| Hacker News / Reddit / случайные обсуждения Gas Town | не использовано | Полезны для reception/context, но для механики главы менее надёжны, чем README, docs, design docs и авторская статья. |
| Beads page `workflows/wisps` | частично заблокировано | Прямое открытие страницы дало ошибку инструмента, но базовая фактура по wisps найдена на общей странице `workflows`. Этого достаточно для текущей главы; подробная реконструкция wisps не нужна. |
| `MAIL_PROTOCOL` как самостоятельная линия | понижено в приоритете | После чтения `polecat-lifecycle-patrol.md`, escalation и reference docs более сильной стала линия patrol/lifecycle/merge/orphan/GUPP/recovery. Mail можно упоминать только как канал коммуникации, а не как главный механизм главы. |
| Внутренние шаблоны ролей Gas Town | использовать осторожно | Они полезны для проверки команд и role expectations, но публичный текст лучше строить на README/docs/design docs. |
| Старые формулировки про JSON-backed Beads | не переносить как актуальные | Текущая документация Beads явно описывает Dolt as sole storage backend / source of truth. Старые детали можно упоминать только как исторический след, если это специально понадобится. |

## Содержательные находки для главы

### 1. Gas Town следует описывать как слой обслуживания множества рабочих потоков, а не как «много агентов»

README и документация подтверждают: Gas Town одновременно говорит о workspace manager, persistent work tracking, hooks, mailboxes, handoffs, roles, convoys, patrol loops, scheduler/backpressure и Beads ledger. Это важно для первой половины главы: проблема не в том, чтобы запустить ещё одну модельную сессию, а в том, чтобы многим сессиям было куда возвращать результат, где получать работу, как оставлять след, как обнаруживать потерянную работу и как передавать проблемы человеку.

Для главы лучше формула не «Gas Town масштабирует агентов», а: Gas Town пытается превратить множество разрозненных агентских действий в обслуживаемую городскую среду, где работа имеет адрес, состояние, владельца, маршрут, историю и механизмы восстановления.

### 2. Различие town-level и rig-level Beads даёт точную границу с PWG

`architecture.md` показывает, что Beads существует на двух уровнях: town-level для координации города, решений, сообщений, convoy coordination и role-definition beads; rig-level для задач, code reviews, merge requests, molecules и локальных рабочих графов. Это почти готовая структурная опора для главы X.

Глава VII может говорить о persistent work graph как форме одного долговременного рабочего узла или набора связанных узлов. Глава X должна показать второй этаж: когда таких узлов много, нужна городская организация, которая распределяет, наблюдает, маршрутизирует и чинит их поток.

### 3. Polecat lifecycle/patrol — лучший источник для драматургии сбоя

Самый полезный внешний документ для главы — `polecat-lifecycle-patrol.md`. Он даёт не абстрактный «мониторинг», а конкретные состояния и события: `GUPP_VIOLATION`, `ORPHANED_WORK`, `RECOVERED_BEAD`, `MERGE_READY`, `MERGED`, `MERGE_FAILED`. Это позволяет написать главу не как архитектурный обзор, а как историю распада управляемости и последующего восстановления.

Хороший пример для основного текста: работа была создана и повешена на hook; polecat перестал вести её по GUPP; часть результата есть, но она не слита; Witness замечает нарушение, Deacon/Refinery/Mayor получают сигнал, bead возвращается в управляемый контур. Именно это отличает среду от набора вкладок с агентами.

### 4. Escalation — не «уведомления», а механизм признания предела автоматики

`escalation.md` важен тем, что фиксирует момент, когда automated resolution is not possible. Проблема маршрутизируется по severity, пишется в beads, имеет stale detection и re-escalation. Поток Deacon → Mayor → Overseer хорошо ложится на мысль о том, что человеческое вмешательство должно быть не случайным чатом «посмотри, я застрял», а частью трассируемой системы.

В главе это лучше держать в одном разделе с patrol/recovery: среда сначала пытается обслуживать поток автоматически, затем умеет вывести проблему на уровень человека, не теряя следа.

### 5. Scheduler нужен как небольшой, но важный аргумент про backpressure

`scheduler.md` не должен становиться отдельным техническим подразделом. Но он даёт факт, которого не хватало в раннем плане: если город умеет запускать 20–30 агентов, он должен иметь не только команды запуска, но и capacity/backpressure. `scheduler.max_polecats`, deferred dispatch, batch size, spawn delay и safety properties показывают, что масштабирование — это ограничение нагрузки, а не романтическое «пусть агенты параллелятся».

Для главы достаточно одного абзаца: в зрелой среде работа может быть отложена, поставлена в очередь, связана с convoy и запущена только когда есть capacity.

### 6. Beads сейчас надо подавать как Dolt-backed control/work state, а не как простой issue tracker

Документация Beads, обновлённая 13–14 июня 2026, даёт несколько важных уточнений:

- Dolt is the sole storage backend / source of truth.
- Beads uses version-controlled SQL.
- Для multi-writer есть server mode.
- `bd prime` подаёт AI-optimized context в сессию.
- `bd gate` умеет блокировать `bd ready` до human/timer/GitHub conditions.
- Multi-agent docs описывают `bd pin`, `bd hook`, sequential handoff и fan-out/fan-in.
- Routing docs описывают pattern-based routing, auto-routing, cross-repo dependencies и hydration.
- Codex integration docs показывают, как Beads входит в lifecycle hooks и переживает compaction.

Это позволяет написать Beads не как «внешний список задач», а как рабочую память/контрольную плоскость, через которую агентская среда получает durable state, маршрутизацию, зависимости, gates и контекст для следующего входа модели.

### 7. Molecules/wisps дают хороший, но вторичный материал

Molecules полезны для связи с идеей process profile: formula/TOML превращается в persistent instance, шаги становятся issues, dependencies управляют `bd ready`, hooks/pinning привязывают шаги к агентам. Это поможет объяснить, как повторяемая процедура превращается в экземпляр рабочего графа.

Wisps лучше не раскрывать широко. Для главы достаточно сказать, что в Beads есть и более лёгкая ephemeral форма для черновых/быстрых заметок (`.beads-wisp`), но главная линия главы — durable work graph and city-level servicing.

### 8. Авторская статья Yegge полезна как предупреждение против рекламного тона

Статья Steve Yegge особенно полезна не только описанием ролей, но и предупреждениями: Gas Town дорогой, сырой, hands-on, frontier, требует аккуратности. Это важно для человеческого тона главы: не писать «вот готовая технология будущего», а показать реальный прототипный режим, где ценность концепта сочетается с высокой стоимостью и хрупкостью.

В главе стоит явно удержать это: Gas Town ценен не потому, что уже решает всё, а потому что называет и собирает правильный класс механизмов для следующего уровня агентской разработки.

## Решение по включению в будущий текст

1. Ввести Gas Town через сбой масштаба: много локально разумных агентских сессий не образуют управляемый поток.
2. Затем объяснить Beads/PWG как нижний durable слой: работа получает состояние, зависимости, gates, pin/hook, routing и контекст через `bd prime`.
3. После этого подняться на Gas Town как городскую организацию: Mayor, rigs, polecats, crew, convoys, Witness, Refinery, Deacon, Dogs.
4. Основную фактуру сбоя брать из polecat lifecycle/patrol: `GUPP_VIOLATION`, `ORPHANED_WORK`, `RECOVERED_BEAD`, `MERGE_READY`, `MERGED`, `MERGE_FAILED`.
5. Scheduler/backpressure включить коротко, чтобы не получалось, будто масштабирование равно запуску большего числа агентов.
6. Escalation включить как момент возврата к человеку, а не как отдельную систему уведомлений.
7. Beads Codex integration и `bd prime` использовать как мост к уже написанной главе VI, но не повторять главу VI про hooks/skills/MCP/subagents.
8. Авторскую статью использовать для контекста и анти-рекламной оговорки: система frontier/expensive/hands-on, её ценность в концептуальной форме механизмов, а не в зрелости продукта.

## Открытые вопросы после поиска

1. Нужна ли в главе отдельная мини-схема `Beads → hooks/pinning/routing/gates → Gas Town roles → patrol/recovery/escalation`? По внешней фактуре такая схема оправдана.
2. Достаточно ли одного Gas Town/Beads кейса для главы или нужно во второй половине коротко сопоставить его с Stripe/Shopify/Mae? По текущей карте — да, сопоставление нужно, но только как supporting parallels, не как второй равноправный центр.
3. Стоит ли упоминать конкретные ограничения Beads (large teams, real-time collaboration, cross-repo limits)? Да, но кратко: это поможет сохранить честный тон и не превратить главу в рекламное описание.
4. Нужно ли возвращаться к `MAIL_PROTOCOL`? Только если при написании главы потребуется пример communication channel. Основной механизм уже найден в patrol/lifecycle/escalation/reference docs.
