# GSD / Open GSD

## Черновое назначение

Документ создан режимом fresh для накопления материала из первоисточников. Это рабочее методологическое досье по GSD / Open GSD: не финальный раздел сайта и не краткая карточка, а буфер фактуры о том, как методология устроена как процесс разработки с AI coding agents.

Текущее состояние источников: девятый содержательный проход, 2026-06-09. Основной корпус фактуры взят из актуальных первичных источников Open GSD: сайт, документация `gsd-core`, документация `gsd-pi`, GitHub-репозитории, roadmap, страницы `Promise` и `Origin Credit`. Второй проход углубил внутреннюю механику: architecture/configuration `gsd-core`, command/configuration/troubleshooting/migration `gsd-pi`, recovery и диагностику состояния. Третий проход добавил низкоуровневые контракты агентских ролей `gsd-core`: `gsd-planner`, `gsd-plan-checker` и `gsd-executor`. Четвёртый проход сверил эти контракты с текущими файлами `open-gsd/gsd-core/main/agents/*` и уточнил, что это уже не только lineage из `get-shit-done-redux`, а актуальная поверхность `gsd-core`. Пятый проход добавил детали observability, audit trail, security boundary для ключей, headless/MCP/forensics-команд `gsd-pi`, hooks/workflows и runtime context. Шестой проход добавил текущие детали `gsd-core` из `docs/v1/user-guide`, `docs/v1/configuration`, `docs/INVENTORY.md` и `docs/issue-driven-orchestration.md`: namespace routing, Nyquist validation, plan drift guard, code review, backlog/seeds/threads/workstreams, security hardening, issue-driven orchestration, state sync и cost/model controls. Седьмой проход добавил низкоуровневые reference-файлы `gsd-core` (`checkpoints.md`, `gates.md`, `context-budget.md`) и первичные docs `gsd-browser`, чтобы точнее описать человеческие остановки, типы gates, бюджет контекста и browser evidence как companion verification layer. Восьмой проход добавил детали `verification-patterns.md`, `artifact-types.md` и `model-profiles.md`: четыре уровня проверки реализации, жизненный цикл и потребителей артефактов, `HANDOFF.json` / `.continue-here.md`, model profile routing, `inherit` для non-Anthropic runtimes и dynamic routing escalation. Девятый проход уточнил текущую `gsd-core`-конфигурацию и команды: phased `models`, `model_profile`, `fast_mode`, `effort`, `agent_skills`, `global_learnings`, `graphify`, `ingest_docs`, `parallelization`, Codex command spelling, `worktree-path-safety` и обновлённый release/version контекст [источники: `gsd-core` configuration docs, https://www.opengsd.net/docs/v1/configuration; `gsd-core` commands docs, https://www.opengsd.net/docs/v1/commands; GitHub `open-gsd/gsd-core` releases, https://github.com/open-gsd/gsd-core/releases].

## Короткая ориентация

GSD в текущем Open GSD-контуре означает `Git. Ship. Done.` и описывает дисциплинированный цикл работы с AI coding agents: обсудить решение, спланировать, выполнить, проверить и довести до поставки. В старой и разговорной традиции название также раскрывалось как `Get Shit Done`; Open GSD сохраняет эту линию, но в продуктовой поверхности использует более нейтральное `Git. Ship. Done.` [источники: GitHub `open-gsd/gsd-core`, https://github.com/open-gsd/gsd-core; Open GSD homepage, https://www.opengsd.net/; Origin Credit, https://opengsd.net/origin].

В Open GSD есть несколько поверхностей, которые важно не смешивать:

- `gsd-core` — prompt-driven framework / набор команд, skills и агентов, который встраивает GSD-цикл в существующие AI coding runtimes: Claude Code, Codex, Gemini CLI, OpenCode, Copilot, Cursor, Windsurf и другие. Он хранит рабочее состояние в `.planning/` и ведёт разработку фазами [источники: product page `gsd-core`, https://opengsd.net/products/gsd-core; GitHub `open-gsd/gsd-core`, https://github.com/open-gsd/gsd-core].
- `gsd-pi` — local-first terminal-native coding agent и оркестратор, который сам ведёт milestones, slices и tasks, хранит runtime state в SQLite-базе проекта и проецирует состояние в `.gsd/` markdown-файлы для review, prompt context и git-friendly history [источники: GitHub `open-gsd/gsd-pi`, https://github.com/open-gsd/gsd-pi; Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `gsd-browser` — отдельный companion product для browser proof: deterministic Chrome control, MCP tools, assertions, traces, screenshots, recordings и human takeover. Roadmap явно говорит, что это не GSD surface, а продукт рядом с GSD, который может подставлять evidence в verification loop [источник: roadmap, https://opengsd.net/roadmap].
- `gsd-workbench` и `gsd-cloud` заявлены как будущие surfaces: desktop workspace и hosted cloud для проектного состояния и удалённого ведения milestones [источник: roadmap, https://opengsd.net/roadmap].

Для будущей теории важно писать не про один инструмент, а про семейство поверхностей вокруг одного рабочего цикла. `gsd-core` показывает GSD как методологию поверх уже выбранного агента. `gsd-pi` показывает тот же мотив как самостоятельный runtime / orchestrator с базой состояния, supervisor-логикой, worktrees, recovery и cost controls.

## Роль в AI-driven SDLC

GSD занимает место между свободным chat-driven coding и тяжёлой enterprise SDLC. Его задача — сделать работу AI coding agents проверяемой и возобновляемой, когда фича уже слишком сложна для одного короткого prompt, но команда ещё не хочет заводить отдельную бюрократическую систему планирования.

Главный тезис Open GSD: AI-assisted engineering деградирует, когда вся работа копится в одном длинном контексте. Сайт формулирует это через `context bloat`, `explicit plans`, `clean execution contexts`, `real verification` и git history, которая отражает реальную работу [источник: Open GSD homepage, https://www.opengsd.net/]. В `gsd-core` это раскрыто как `context rot`: модель не ломается резко, но начинает хуже удерживать ранние решения, стиль, constraints, file names и сигнатуры функций по мере заполнения context window [источник: `docs/explanation/context-engineering.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/context-engineering.md].

GSD отвечает на это не одним большим spec-файлом, а разбиением разработки на bounded phases / slices и переносом состояния в durable artifacts. Для `gsd-core` это `.planning/` с markdown/json-артефактами. Для `gsd-pi` это `.gsd/` projection layer плюс SQLite database как authoritative runtime state. В обоих вариантах один артефакт становится входом для следующего шага, а агенту не нужно держать весь ход работы в памяти одной беседы.

Архитектура `gsd-core` прямо описывает его как meta-prompting framework между пользователем и AI coding agents. Внутри есть command layer (`commands/gsd/*.md`), workflow layer (`get-shit-done/workflows/*.md`), agent layer с fresh-context агентами, CLI tools layer (`gsd-tools.cjs` и command-routing hub) и файловый слой `.planning/`. Это важно для будущей теории: GSD не только набор красивых команд, а система маршрутизации prompt-workflows, где thin orchestrator загружает контекст, запускает специализированных агентов, собирает результаты и обновляет state между шагами [источник: `gsd-core` architecture, https://www.opengsd.net/docs/v1/architecture].

Текущая `gsd-core`-документация показывает ещё один методологический мотив: сама поверхность команд стала достаточно большой, чтобы требовать слой маршрутизации. `User Guide` описывает шесть namespace meta-skills: `/gsd-workflow`, `/gsd-project`, `/gsd-quality`, `/gsd-context`, `/gsd-manage`, `/gsd-ideate`. Они нужны не как новые ручные команды, а как первый слой маршрутизации, чтобы модель видела короткий список routers вместо плоского списка из десятков skills; конкретные команды вроде `/gsd-plan-phase` всё равно можно вызывать напрямую [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].

## Проблема, которую решает методология

### Context rot и деградация длинной сессии

Документация `gsd-core` описывает context rot как снижение качества ответов в длинной coding session: модель начинает противоречить ранним решениям, уходить от стиля проекта, игнорировать требования, которые были заданы раньше, или выдумывать имена файлов и сигнатуры, которые ранее называла правильно [источник: `context-engineering.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/context-engineering.md].

Простое `/clear` решает проблему шума, но теряет continuity. GSD предлагает другой ход: основной orchestrator остаётся тонким, тяжёлую работу выполняют fresh-context subagents, а результаты фиксируются в файлах. В `gsd-core` orchestrator не должен сам лезть в source files; он запускает agents, собирает результаты, обновляет shared state и маршрутизирует следующий шаг [источник: `context-engineering.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/context-engineering.md].

### Непроверенная реализация

GSD исходит из того, что "код написан" не равно "фаза завершена". В `gsd-core` Verify step сверяет phase goal, решения из `CONTEXT.md`, планы и execution summaries; он проверяет requirement coverage, decision coverage и alignment с целью фазы. Если есть расхождения, создаются targeted fix plans [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].

В `gsd-pi` эта идея доведена до runtime-механики: после unit GSD проверяет наличие ожидаемого artifact на диске; для `run-uat` файл assessment должен иметь canonical verdict, например `PASS`, `FAIL` или `PARTIAL`. Artifact verification retries ограничены тремя попытками; после этого auto mode pauses вместо бесконечного цикла [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

### Потеря состояния между sessions

GSD фиксирует decisions, requirements, roadmap, plans, summaries, verification и handoff в файловых или DB-backed артефактах. В `gsd-core` `STATE.md` — навигационный слой, который показывает active milestone, phase, completed/pending plans и blockers; workflows читают его при старте [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].

В `gsd-pi` SQLite database является source of truth для milestones, slices, tasks, requirements, summaries и completion status. Markdown-файлы `.gsd/` — projections для review, prompts и git-friendly history; редактирование projections само по себе не перезаписывает database state, если команда GSD явно не импортирует или не сохраняет изменения [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

## Workflow: gsd-core

`gsd-core` организует работу milestone за milestone, phase за phase. Центральная модель: `Discuss -> (UI design) -> Plan -> Execute -> Verify -> Ship` [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].

### 1. Initialize / new project

Стартовая команда:

```text
/gsd-new-project
```

Она задаёт вопросы, может запускать research, формирует requirements и roadmap. В tutorial first project результатом становятся `.planning/PROJECT.md`, `.planning/REQUIREMENTS.md`, `.planning/ROADMAP.md`, `.planning/STATE.md` и `.planning/config.json` [источники: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md; `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].

Для brownfield-репозитория README рекомендует сначала выполнить `/gsd-map-codebase`, чтобы переиндексировать codebase, а затем `/gsd-new-project` для восстановления planning context [источник: GitHub `open-gsd/gsd-core`, https://github.com/open-gsd/gsd-core].

### 2. Discuss phase

Команда:

```text
/gsd-discuss-phase [N]
```

Discuss фиксирует implementation decisions до планирования: библиотеки, error-handling, API shape, data structures, edge cases, UI behaviour. Документация подчёркивает, что phase goal в `ROADMAP.md` говорит, что надо получить, а Discuss нужен, чтобы решить, как именно это строить. Иначе planner будет сам делать правдоподобные, но потенциально неверные предположения [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].

Выход: `CONTEXT.md` в phase directory и `DISCUSSION-LOG.md` как audit trail. Tutorial показывает файл `.planning/phases/01-core-cli/CONTEXT.md` с `## Implementation Decisions`; planner затем читает этот файл, поэтому решения пользователя доходят до task plans [источники: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md; `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].

### 3. Optional UI design

Для frontend/UI phase есть отдельный шаг:

```text
/gsd-ui-phase [N]
```

Он создаёт `{phase}-UI-SPEC.md` / `UI-SPEC.md`: design contract для layout, interaction и visual behaviour до написания кода. Документация считает этот шаг полезным, когда UI достаточно сложен, чтобы неоднозначность дизайна привела к расходящимся реализациям [источники: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md; `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].

### 4. Plan phase

Команда:

```text
/gsd-plan-phase [N]
```

Plan выполняет research, decomposition и plan verification. В описании phase loop участвуют fresh-context subagents: researcher пишет `RESEARCH.md`, planner читает `RESEARCH.md` и `CONTEXT.md`, создаёт `PLAN.md` files, а plan-checker проверяет completeness, consistency и scope [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].

Каждый `PLAN.md` должен описывать bounded unit of work: files to touch, specific changes, acceptance criteria. Plans упорядочиваются в dependency waves, чтобы parallel execution была безопасной: executors в одной wave не должны трогать пересекающиеся concerns [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].

Команда поддерживает flags, которые показывают зрелость рабочего процесса: `--research`, `--skip-research`, `--validate`, `--prd`, `--ingest`, `--reviews`, `--bounce`, `--mvp`, `--tdd`. `--mvp` организует задачи как vertical slices и может породить `SKELETON.md` для Walking Skeleton; `--tdd` помечает подходящие behavior-adding tasks как начинающиеся с failing test [источник: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].

Отдельно важен Package Legitimacy Gate: если researcher рекомендует внешние packages, `slopcheck install <package> --json` пишет audit table в `RESEARCH.md`; `[SLOP]` удаляется, `[SUS]` и WebSearch `[ASSUMED]` получают `checkpoint:human-verify` перед install task. Если `slopcheck` недоступен, все пакеты считаются `[ASSUMED]` и gate включается [источник: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].

Architecture docs уточняют, что package gate встроен в pipeline researcher -> planner -> executor: researcher запускает registry-specific checks, planner добавляет `checkpoint:human-verify` и supply-chain row для install-bearing plans, executor не делает silent substitutions при провалившемся install. В том же pipeline есть decision coverage gate: на plan-phase он blocking, а на verify-phase validation уже non-blocking; это разделяет "не планировать без переноса решений" и "зафиксировать расхождение после реализации" [источник: `gsd-core` architecture, https://www.opengsd.net/docs/v1/architecture].

В текущем `User Guide` поверх прежних gates явно вынесен `Nyquist pre-flight validation`. Он срабатывает перед выполнением планов и проверяет планы, ссылаемые файлы, критерии приёмки и граф зависимостей до того, как агент начнёт менять код. Если находка исправима автоматически, GSD пишет `PLAN-REPAIRS.md` и пересобирает план; если нужен человек, создаётся `CHECKPOINT-NYQUIST.md`; если всё чисто, появляется `NYQUIST-PASS.md`. Для методологии это важная деталь: часть проверки сдвинута в момент перед dispatch, где ещё дешево остановить плохой план [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].

Низкоуровневый `gsd-planner` показывает, что `PLAN.md` в GSD задуман как исполняемый запрос для отдельного executor-агента, а не как предварительная заметка. Planner обязан сначала разобрать locked decisions из `CONTEXT.md`, ссылаться на `D-NN` в действиях задачи, не переносить deferred ideas в план и не заменять пользовательские решения формулировками вроде `v1`, `static for now`, `future enhancement`, `placeholder` или `basic version`. Если весь объём не помещается в безопасный контекст, planner должен предложить split phase, а не молча урезать требования [источник: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md].

У `gsd-planner` есть обязательный multi-source coverage audit по четырём типам входа: `GOAL` из `ROADMAP.md`, `REQ` из `REQUIREMENTS.md`, `RESEARCH` из `RESEARCH.md` и `CONTEXT` decisions. Каждый элемент должен быть покрыт планом; если что-то не покрыто, planner возвращает предупреждение о незапланированных пунктах с вариантами: добавить план, разделить фазу или отложить только после developer confirmation. Это важная деталь для будущей теории: GSD пытается не только разбивать работу, но и формально защищать перенос решений из предыдущих артефактов в исполняемую работу [источник: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md].

Task anatomy у `gsd-planner` жёсткая: каждая задача должна иметь exact file paths, конкретные действия, verification command и measurable done criteria. Проверка должна быть выполнимой быстро; если теста нет, план обязан явно сказать, что Wave 0 создаёт test scaffold. В `must_haves` planner выводит observable truths, required artifacts и key links: что пользователь должен уметь сделать, какие файлы или database objects должны существовать, какие соединения между компонентами, API и database особенно вероятно сломаются [источник: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md].

Pass 04 сверил те же контракты агентских ролей в текущем `open-gsd/gsd-core`. Это закрывает часть осторожности из pass 03: `gsd-planner`, `gsd-plan-checker` и `gsd-executor` лежат прямо в актуальном `gsd-core`, поэтому их можно использовать как первичный источник для текущей методологии, а не только как исторический источник. При этом старое название repository всё ещё полезно как provenance для lineage, но финальный текст может ссылаться на текущие файлы `open-gsd/gsd-core/main/agents/*` [источники: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md; `agents/gsd-plan-checker.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md; `agents/gsd-executor.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md].

Из текущего `gsd-planner` для будущего Handbook важна ещё одна рабочая деталь: планирование не должно выдавать задачи без явной модели владения файлами. Для parallel execution `PLAN.md` должен делать конфликтующие paths видимыми заранее; если две задачи трогают один и тот же файл или одну и ту же область состояния, они не должны попадать в одну wave. Это связывает plan quality с будущей безопасностью executor wave, а не только с полнотой текста плана [источник: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md].

Planner также переводит размер работы в context budget, а не в человеко-часы. План должен обычно завершаться примерно в пределах 50% context; одна задача целится в 10-30% context, TDD plan — около 40%, потому что `RED -> GREEN -> REFACTOR` требует дополнительного чтения, запусков и анализа вывода. Это не только оптимизация: в логике GSD качество падает при росте контекста, поэтому планирование управляет размером задач через ожидаемое потребление контекста [источник: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md].

Для `--mvp` planner требует vertical feature slices: после каждой задачи реальный пользователь должен получить новое observable capability. Горизонтальная foundation-задача допускается только как Walking Skeleton, где создаётся `SKELETON.md` с framework, DB, auth, deployment и directory layout decisions; последующие phases не должны заново обсуждать эти решения. Если одновременно включён TDD mode, первая задача становится failing end-to-end test for the happy path [источник: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md].

Новый `Plan Drift Guard` закрывает ещё один слабый участок: план может быть хорошим в момент создания, но устареть после изменения кода, `CONTEXT.md`, `REQUIREMENTS.md`, `ROADMAP.md` или исследовательских файлов. `User Guide` описывает проверку `/gsd-plan-status`, которая сравнивает заголовки плана, хэши зависимостей, `source_sha` и `HEAD`; статусы делятся на `valid`, `stale`, `orphaned`, `dirty` и `expired`. Если план устарел, GSD предлагает обновить, синхронизировать, перепланировать или отдать ситуацию на ручное ревью. Это отличает "план есть" от "план всё ещё применим к текущему репозиторию" [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].

### 5. Execute phase

Команда:

```text
/gsd-execute-phase <N>
```

Execution запускает plans, часто в parallel waves. Каждый executor получает fresh context window с project summary, phase context, research и конкретным `PLAN.md`. Executor пишет code и делает atomic commit; один commit соответствует completed task in plan [источники: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md; `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].

`COMMANDS.md` уточняет, что команда создаёт per-plan summaries, git commits и phase verification artifact после полного завершения. Если install step падает из-за пакета, executor surfaces `checkpoint:human-verify` и останавливается; он не должен silently install similarly-named alternative, потому что это риск slopsquatting [источник: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].

`gsd-executor` исполняет `PLAN.md` атомарно: читает frontmatter, objective, context references, tasks, verification и success criteria; для `type="auto"` выполняет задачу, проверяет done criteria, делает commit и фиксирует completion с commit hash для `SUMMARY.md`. Если план содержит checkpoint, executor выполняет работу до checkpoint и останавливается со structured checkpoint message; продолжение должно запускаться свежим агентом, который сверяет предыдущие commits и возобновляется с указанной точки [источник: `agents/gsd-executor.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md].

Deviation rules у executor показывают, где GSD проводит границу автономности. Сбои, missing critical functionality и blockers, напрямую вызванные текущей задачей, исправляются автоматически с тестами/проверками и записываются в summary. Но architectural change — новая таблица, серьёзная схема, новая service layer, смена библиотеки, auth approach, infrastructure или breaking API — требует остановки и checkpoint с описанием impact and alternatives. Package-manager install failure тоже не auto-fixable: executor не ищет похожий пакет и не повторяет установку под другим именем, а требует `checkpoint:human-verify` [источник: `agents/gsd-executor.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md].

Executor содержит явный stuck-signal: если во время task execution агент сделал пять и более подряд `Read`/`Grep`/`Glob` без `Edit`/`Write`/`Bash`, он должен остановиться, коротко объяснить, почему ещё ничего не написал, и либо начать действие, либо признать конкретный blocker. Это неудобная, но ценная деталь: GSD пытается обнаружить бесконечное чтение и analysis paralysis внутри самой агентской роли, а не только на уровне внешнего таймера [источник: `agents/gsd-executor.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md].

Между execution и UAT появился отдельный слой ревью: `/gsd-code-review-phase`, `/gsd-code-review-plan`, `/gsd-code-review-file`, `/gsd-code-review-task`, `/gsd-code-review-changes`, `/gsd-code-review-diff`, `/gsd-code-review-commit`, `/gsd-code-review-branch` и `/gsd-code-review-pr`. Документация позиционирует его как проверку с новой агентской перспективы до ship: корректность, сопровождаемость, безопасность, тесты и согласованность с планом. Важная граница: review не заменяет `/gsd-verify-work`, потому что он оценивает изменение как код и процесс, а verification проверяет наблюдаемое поведение и критерии приёмки [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].

### 6. Verify work

Команда:

```text
/gsd-verify-work [N]
```

Это user acceptance testing with auto-diagnosis. В tutorial GSD пошагово спрашивает пользователя, проходят ли observable checks (`node todo.js add`, `todo list`, `todo done`), записывает outcomes в `UAT.md`, а при провале диагностирует cause и создаёт fix plan [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].

Для browser-backed UAT текущий Open GSD companion — `gsd-browser`, который даёт deterministic navigation, versioned refs, assertions, screenshots, visual diffs, recordings и human takeover. Legacy Playwright MCP servers остаются usable, если уже настроены [источник: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].

`gsd-browser` стоит описывать как evidence backend рядом с GSD, а не как ещё один вариант `gsd-core`. Его product page и docs показывают отдельный operating loop: установить CLI, запустить `gsd-browser mcp`, навигировать, делать snapshots с versioned refs вроде `@v1:e1`, выполнять действия, явно проверять outcomes через assertions и сохранять доказательства. В доказательства входят screenshots, recordings, traces, HAR, PDF exports, annotations, debug bundles и live viewer sessions, которые человек может проверить или взять под управление [источники: `gsd-browser` product page, https://opengsd.net/products/gsd-browser; `gsd-browser` CLI & MCP Commands, https://opengsd.net/docs/v5/commands].

### 7. Ship

Команда:

```text
/gsd-ship [N]
```

Ship создаёт PR из verified phase work, требует passed `/gsd-verify-work`, установленный и authenticated `gh` CLI. PR body включает phase goal из `ROADMAP.md`, changes summary из `SUMMARY.md`, addressed REQ-IDs, verification status, key decisions и optional configured PRD-style sections из `ship.pr_body_sections`. `STATE.md` обновляется [источник: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].

### Навигация и lightweight пути

`/gsd-progress --next` auto-detects and runs next logical workflow step: нет проекта -> `/gsd-new-project`, phase needs discussion -> `/gsd-discuss-phase`, needs planning -> `/gsd-plan-phase`, needs execution -> `/gsd-execute-phase`, needs verification -> `/gsd-verify-work`, all phases complete -> suggests `/gsd-complete-milestone` [источник: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].

Для задач ниже порога full phase loop есть `/gsd-quick` и `/gsd-fast`. Документация прямо говорит, что phase loop чрезмерен для rename variable, typo fix или missing import; правило: если задача полностью задаётся коротким prompt и может быть выполнена в один агентский turn без clarification, лучше пропустить phase loop [источник: `context-engineering.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/context-engineering.md].

Командная поверхность `gsd-core` показывает, что "лёгкий путь" не сводится к одному quick prompt. `/gsd-manager` умеет ставить фоновые задачи по чек-листу, хранить их в `.planning/todos/`, показывать heartbeat/status и откатывать task state; `/gsd-ingest-docs` принимает внешние документы в `.planning/`, классифицирует их как `prd`, `api-docs`, `tech-spec`, `design`, `requirements` или `notes`, дедуплицирует и пишет conflicts в `INGEST-CONFLICTS.md`; `/gsd-graphify` строит dependency graph из `ROADMAP.md`/requirements/issues/plans/code map в `.planning/graphs/` и затем может выводить critical path или blocked work. Это важный источник фактуры: вокруг фазового loop есть слой управления входящим материалом и очередью работы, чтобы не превращать каждый небольшой запрос в полный milestone [источник: `gsd-core` commands docs, https://www.opengsd.net/docs/v1/commands].

### Внутренняя механика `gsd-core`

`gsd-core` держит отдельные reference-файлы для gates, checkpoints, model profiles, verification patterns, planning config, git integration, context budget, continuation format, domain probes, revision loop, anti-patterns и artifact types. Это объясняет, почему методология выглядит как "команды", но ведёт себя как повторяемая система: workflow-команда не должна заново изобретать правила проверки, ветвления или continuation; она подключает общий reference layer [источник: `gsd-core` architecture, https://www.opengsd.net/docs/v1/architecture].

Reference layer полезен ещё и тем, что фиксирует правила, которые легко потерять в высокоуровневом описании. `context-budget.md` запрещает orchestrator читать `agents/*.md`, потому что `subagent_type` сам загружает agent definition; запрещает встраивать большие файлы в prompts subagents; для context window меньше 500K tokens рекомендует читать только frontmatter/status/summaries у тяжёлых артефактов, а полные тела `SUMMARY.md`, `VERIFICATION.md` и `RESEARCH.md` оставлять для больших окон и реальной необходимости. Это делает "thin orchestrator" не метафорой, а конкретной дисциплиной чтения [источник: `context-budget.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/context-budget.md].

Тот же файл вводит degradation tiers: при 0-30% контекста возможны полные операции, при 30-50% нужно предпочитать frontmatter и делегирование, при 50-70% экономить и предупреждать пользователя, при 70%+ сразу checkpoint progress. Набор warning signs практичен: silent partial completion, возрастающая расплывчатость формулировок и пропуск шагов протокола. Важная оговорка источника: orchestrator не может семантически доказать качество результата subagent, он проверяет прежде всего структурную полноту, поэтому нужны `must_haves` и spot-check verification [источник: `context-budget.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/context-budget.md].

`model-profiles.md` показывает, что управление стоимостью в GSD встроено не только в размер контекста, но и в routing моделей. Базовые profiles `quality`, `balanced`, `budget`, `adaptive` и `inherit` задают разные модели для ролей: planner и debugger получают более сильные модели там, где важны архитектурные решения и diagnosis; codebase mapper, synthesizer, checker и auditor могут уходить на более дешёвые модели, если задача структурная и массовая. Это методологически важно: GSD не предполагает, что каждый agent должен работать на максимальной модели, а связывает качество модели с ценой ошибки в конкретной фазе [источник: `model-profiles.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/model-profiles.md].

В том же reference-файле есть два неудобных operational rules. Для non-Claude runtimes installer выставляет `resolve_model_ids: "omit"` в `~/.gsd/defaults.json`, чтобы subagents использовали default model выбранного runtime; если человек хочет разные модели по агентам, он задаёт `model_overrides` именами, которые понимает этот runtime, например `o3` или `o4-mini`. Для Claude Code с OpenRouter или local provider нужен profile `inherit`; иначе default `balanced` может spawning Anthropic model aliases и привести к неожиданным расходам. Dynamic routing, если включён, берёт default tier агента (`light`, `standard`, `heavy`) и при soft failure может подняться на следующий tier, но hard failures должны всплывать сразу [источник: `model-profiles.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/model-profiles.md].

Текущая configuration page раскрывает тот же механизм уже как пользовательскую конфигурацию. `models.planning`, `models.execution`, `models.verification`, `models.research`, `models.code_review`, `models.ui_review`, `models.debug`, `models.issue_triage`, `models.graph_analysis` задают фазовые модели; `model_overrides.<agent-name>` перекрывает их для конкретных ролей; `runtime: "claude" | "codex" | "gemini" | "opencode" | "github-copilot" | "cursor" | "windsurf" | "kilo"` включает runtime-aware настройки по умолчанию. `model_profile: "quality" | "balanced" | "budget" | "adaptive"` остаётся более крупной ручкой, а `fast_mode` и `effort` дают быстрый путь к дешёвым/скоростным настройкам без ручного заполнения всех agent overrides. Для методологии это означает, что выбор модели становится частью политики рабочего процесса, а не личной привычкой оператора [источник: `gsd-core` configuration docs, https://www.opengsd.net/docs/v1/configuration].

В той же конфигурации появились `agent_skills` и `global_learnings`, которые точнее отвечают на вопрос "где живёт контекст". `agent_skills` управляет тем, какие проектные skills подмешиваются к субагентам: можно задать глобальные skills для всех агентов, skills по имени агента и skills по типу фазы. `global_learnings` задаёт файл, куда пишутся повторно используемые паттерны, предпочтения и уроки; это не артефакт фазы, а слой памяти поверх отдельных фаз. Такая настройка опасна при переносе между проектами: неправильно подобранные skills или глобальные learnings могут незаметно изменить поведение planner/executor сильнее, чем сама команда `/gsd-plan-phase` [источник: `gsd-core` configuration docs, https://www.opengsd.net/docs/v1/configuration].

В `execute-phase` планы группируются в dependency waves. Каждый executor получает fresh context, конкретный `PLAN.md`, project context из `PROJECT.md`/`STATE.md` и phase context из `CONTEXT.md`/`RESEARCH.md`. Для больших context windows, начиная примерно с 500K tokens, включается adaptive context enrichment: executors получают больше prior summaries, а verifier получает все `PLAN.md`, `SUMMARY.md`, `CONTEXT.md` и `REQUIREMENTS.md`. Для parallel commit safety используются `--no-verify` commits внутри wave с последующим запуском pre-commit hooks один раз после wave, а запись `STATE.md` защищается lockfile-механикой [источник: `gsd-core` architecture, https://www.opengsd.net/docs/v1/architecture].

Файловая модель `.planning/` шире, чем базовые `PROJECT.md`/`REQUIREMENTS.md`/`ROADMAP.md`: architecture docs перечисляют `research/`, `codebase/`, `quick/`, `todos/`, `threads/`, `seeds/`, `debug/`, `ui-reviews/` и `continue-here.md`. Для brownfield-проектов особенно важна `.planning/codebase/`: после последней execution wave non-blocking `codebase_drift_gate` сравнивает diff от `last_mapped_commit` с `.planning/codebase/STRUCTURE.md` и, если появились новые структурные элементы, предупреждает или запускает scoped remap. Это не блокирует verification, но показывает, что GSD пытается поддерживать карту кода после изменений [источник: `gsd-core` architecture, https://www.opengsd.net/docs/v1/architecture].

`User Guide` уточняет назначение трёх долго живущих поверхностей рядом с фазовым loop. Backlog (`/gsd-capture`, `/gsd-todo-*`) хранит идеи, bugs и будущую работу в `.planning/backlog/` до превращения в пункт roadmap. Seeds (`/gsd-seed`, `/gsd-seed-harvest`, `/gsd-seed-promote`) сохраняют architectural hints и speculative ideas в `.planning/seeds/` и позволяют позже повысить их до требований или решений. Threads (`/gsd-thread`, `/gsd-thread-continue`, `/gsd-thread-status`, `/gsd-thread-close`) дают постоянный контекст исследования или обсуждения в `.planning/threads/`, чтобы длительное расследование не смешивалось с phase execution. Это важно для переноса методологии: не весь контекст должен становиться phase context; часть контекста живёт как ожидание, гипотеза или отдельная нить исследования [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].

Workstreams (`/gsd-workstream-create`, `/gsd-workstream-branch`, `/gsd-workstream-switch`, `/gsd-workstream-checkpoint`, `/gsd-workstream-merge`, `/gsd-workstream-status`, `/gsd-workstream-list`, `/gsd-workstream-close`) добавляют ещё один уровень изоляции: параллельные направления работы получают собственные ветки и состояние планирования. Это не та же вещь, что dependency waves внутри одной phase: waves параллелят проверенные plan tasks, а workstreams разделяют более крупные направления, которые могут жить дольше одной phase и позже сходиться через merge/checkpoint [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].

На уровне контрактов агентских ролей эта механика становится ещё жёстче: `gsd-plan-checker` работает как pre-execution Revision Gate. Он не исправляет планы молча и не запускает реализацию; его результат — `PASS`, `NEEDS_REVISION` или `BLOCKED_BY_MISSING_INPUT`. При `NEEDS_REVISION` checker должен назвать concrete changes needed, expected plan updates и не давать execution-ready verdict. Это делает plan review самостоятельной фазой, а не украшением вокруг planner output [источник: `agents/gsd-plan-checker.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md].

`gsd-plan-checker` проверяет не только полноту списка задач. Его checklist включает objective coverage, requirement coverage, research coverage, explicit decisions from `CONTEXT.md`, отсутствие незапланированных TODO, dependency order, non-overlap for parallel tasks, observable acceptance criteria, verification commands, rollback/recovery path, context budget и наличие key links. Отдельная проверка ловит "happy path only" plans: если план описывает реализацию без error paths, empty states, auth/permission, migration/data safety или user-visible failure modes, он не должен проходить как execution-ready [источник: `agents/gsd-plan-checker.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md].

Текущая сверка с `open-gsd/gsd-core` усилила важное различение: plan-checker не является вторым planner. Его работа — вернуть verdict и объяснить, какие именно изменения должны появиться в плане. Это удерживает цепочку ответственности: planner исправляет plan artifact, checker повторно оценивает, executor получает только проверенный input. Если checker начнёт "чинить по дороге", GSD потеряет проверяемую границу между ревью плана и исполнением [источник: `agents/gsd-plan-checker.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md].

Observability в `gsd-core` встроена в command-routing layer, но по умолчанию не шумит. При сбое routing hub пишет одну JSON-строку в stderr с `kind`, `traceId`, `command`, `timestamp` и `message`; `kind` различает `UnknownCommand`, `InvalidArgs`, `HandlerRefusal` и `HandlerFailure`. Полный audit trail включается явно через `GSD_AUDIT=1` или `config.audit.enabled`; тогда dispatch events пишутся в `.planning/.gsd-trace.jsonl`, один JSON object на строку, с `traceId` и, когда он передан, `parentTraceId`. Файл append-only, gitignored и не ротируется автоматически, поэтому это операторский диагностический след, а не пользовательский артефакт сайта или документации [источник: `gsd-core` configuration docs, https://www.opengsd.net/docs/v1/configuration].

У audit trail есть важная privacy граница. Аргументы команд по умолчанию не попадают ни в stderr events, ни в audit file; для записи аргументов нужен явный `GSD_AUDIT_ARGS=1`. В тех же configuration docs API keys для Brave/Firecrawl/Exa маскируются в UI, confirmation tables, logs и `config-set` output, но plaintext хранится в `.planning/config.json`; документация прямо называет этот файл security boundary. Для будущего текста это неудобная, но важная деталь: GSD делает операции наблюдаемыми, но безопасность зависит от того, как команда обращается с `.planning/config.json` и audit logs [источник: `gsd-core` configuration docs, https://www.opengsd.net/docs/v1/configuration].

Текущие configuration docs добавляют `security_hardening`: атомарные записи с backup-файлами, проверку `.planning/` в `.gitignore`, проверку целостности installer, enforcement для опасных git-команд и явные permission gates для инструментов. Отдельный `safety.dangerous_git_policy` может быть `block`, `confirm` или `allow`; default `confirm` требует явного согласия перед destructive git operations. В `tools.allowed`, `tools.denied` и `tools.confirm_required` можно задать политику для команд и MCP tools. Это показывает, что GSD постепенно переносит безопасность из общих советов в конфигурационный слой процесса [источник: `gsd-core` configuration docs, https://www.opengsd.net/docs/v1/configuration].

`parallelization` и worktree safety показывают другой край этой конфигурации. В `gsd-core` можно управлять `max_agents`, `conflict_strategy`, `auto_commit`, `branch_naming`, `wave_strategy`, `checkpoint_after_wave`, `checkpoint_after_task`, `require_clean_worktree`, `protect_branches` и `worktree_path`. Отдельный reference `worktree-path-safety` описывает типовые сбои: HEAD остаётся на `main`, а milestone ветка создаётся рядом; агент стартует не из ожидаемого worktree; путь worktree выходит за допустимую базу; защищённая ветка попадает под запись. Это не второстепенная реализационная деталь: параллельное исполнение в GSD безопасно только при явной политике веток, путей и checkpoint-ритма [источники: `gsd-core` configuration docs, https://www.opengsd.net/docs/v1/configuration; `gsd-core` commands docs, https://www.opengsd.net/docs/v1/commands].

Отдельная context-budget деталь относится к MCP как к внешнему ограничителю метода. `context-budget.md` подчёркивает, что каждый включённый MCP server добавляет schema в каждый turn, даже если инструменты не вызываются; тяжёлые servers могут стоить десятки тысяч tokens на turn. Это не настраивается через `.planning/config.json`, а живёт в `.claude/settings.json` через `enabledMcpjsonServers` / `disabledMcpjsonServers`. Для GSD это важный failure mode: методология может аккуратно выбирать `model_profile`, но потерять выигрыш из-за неаудированного MCP-набора перед длинной phase [источник: `context-budget.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/context-budget.md].

## Workflow: gsd-pi

`gsd-pi` переносит тот же мотив в самостоятельный local-first agent. Установка:

```text
npx @opengsd/gsd-pi@latest
npm install -g @opengsd/gsd-pi@latest
```

Минимальные требования в Getting Started: Node.js 22.0.0, npm, Git 2.20 и credentials одного supported model provider. Direct global install и non-interactive install `--yes` тоже описаны [источник: Getting Started, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/getting-started.md].

### Сессия и команды

Базовый запуск:

```text
gsd
```

Распространённые slash commands внутри session:

```text
/gsd config
/gsd auto
/gsd quick "Describe the task"
/gsd status
```

`gsd-pi` хранит планирование проекта и состояние выполнения в `.gsd/` [источник: GitHub `open-gsd/gsd-pi`, https://github.com/open-gsd/gsd-pi].

Справочник команд показывает, что `gsd-pi` вырос из одного `/gsd auto` в полноценную рабочую оболочку. Базовая системная поверхность включает `/gsd prefs`, `/gsd model`, `/gsd mode`, `/gsd config`, `/gsd keys`, `/gsd doctor`, `/gsd inspect`, `/gsd show-config`, `/gsd init`, `/gsd mcp`, `/gsd context`, `/gsd skill-health`, `/gsd hooks`, `/gsd migrate`, `/gsd recover --confirm`, `/gsd rebuild markdown` и `/gsd rebuild database`. Важно, что `rebuild markdown` пересобирает projections из canonical database, а stale completion projections карантинятся и не импортируются; `rebuild database` зарезервирован для DB-native rebuilds и не импортирует markdown projections. Это усиливает общий принцип `gsd-pi`: markdown удобен для чтения, но не должен молча подменять runtime truth [источник: `gsd-pi` commands, https://www.opengsd.net/docs/v2/commands].

Операционная поверхность тоже широкая: `/gsd queue` управляет будущими milestones, `/gsd debug` и `/gsd debug continue` ведут длительные debug-сессии, `/gsd dispatch` запускает конкретную фазу напрямую, `/gsd verdict` переопределяет milestone validation verdict с rationale, `/gsd history` и `/gsd usage` показывают историю и расход, `/gsd forensics` запускает debugger с полным доступом для разборов auto-mode failures, `/gsd closeout` чинит провалившиеся git closeout actions, `/gsd worktree` управляет worktrees, `/gsd brief` создаёт автономные visual HTML briefs, `/gsd extract-learnings` сохраняет Decisions/Lessons/Patterns/Surprises после milestone [источник: `gsd-pi` commands, https://www.opengsd.net/docs/v2/commands].

Для headless/CI-сценариев есть `gsd headless`: он запускает auto mode без TUI, умеет `next`, `query`, `dispatch`, `new-milestone --context`, `new-milestone --context-text`, принимает timeout и `--max-restarts`, а `gsd headless query` возвращает быстрый JSON snapshot с active milestone/slice/task, blockers, next action и cost. Exit codes различают completion, error/timeout и blocked. `gsd headless recover` даёт non-TTY эквивалент `/gsd recover --confirm` и после него документация рекомендует проверять rebuilt state через `gsd headless query`. Это делает `gsd-pi` не только interactive terminal agent, но и потенциальной внутренней службой для внешнего orchestrator [источник: `gsd-pi` commands, https://www.opengsd.net/docs/v2/commands].

Ещё одна текущая поверхность — MCP server mode. `gsd --mode mcp` запускает GSD как MCP server over stdin/stdout и exposes tools from the agent session to external AI clients. Отдельно описан Cloud MCP Gateway Runtime: `gsd-cloud-mcp-gateway` поднимает HTTP gateway, а `gsd-daemon cloud` pairs and connects local runtime to that gateway. Для методологического досье это важно как расширение границы GSD: методология может быть не только локальной TUI-сессией, но и инструментальным backend для внешних клиентов и удалённых orchestrators [источник: `gsd-pi` commands, https://www.opengsd.net/docs/v2/commands].

### Auto mode как state machine

Ключевой режим:

```text
/gsd auto
```

Auto mode описан как autonomous execution engine: он берёт следующий unit of work из authoritative SQLite state at project root, создаёт fresh agent session, injects focused prompt with relevant context pre-inlined, даёт LLM выполнить unit, сохраняет результат в database, обновляет markdown projections вроде `STATE.md` и dispatches next unit [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

Основной loop по slice:

```text
Plan (with integrated research)
-> Execute (per task)
-> Complete
-> Reassess Roadmap
-> Next Slice
-> Validate Milestone
-> Complete Milestone
```

Plan scouts codebase, researches relevant docs и decomposes slice into tasks with must-haves. Execute runs each task in a fresh context window. Complete writes summary, UAT script, marks roadmap и commits. Reassess checks whether roadmap still makes sense. Validate Milestone compares roadmap success criteria against actual results before sealing milestone [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

Progressive planning: GSD может полностью спланировать first slice, а later slices оставить sketches с `[sketch]` badge в `M###-ROADMAP.md`. Перед execution auto mode запускает `refine-slice`, чтобы превратить sketch в full slice plan на основании текущего codebase и prior slice summaries [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

### Deep planning mode

Для проектов, где нужна предварительная discovery, включается:

```yaml
planning_depth: deep
```

или запуск:

```text
/gsd new-project --deep
/gsd new-milestone --deep
```

Deep mode добавляет staged discovery flow перед milestone-level planning: Workflow Preferences -> Project Context -> Requirements -> Research Decision -> Optional Project Research -> Milestone Context/Roadmap. Артефакты: `.gsd/PREFERENCES.md`, `.gsd/PROJECT.md`, `.gsd/REQUIREMENTS.md`, `.gsd/runtime/research-decision.json`, `.gsd/research/STACK.md`, `FEATURES.md`, `ARCHITECTURE.md`, `PITFALLS.md`, затем `.gsd/milestones/<...>/M###-CONTEXT.md` и `M###-ROADMAP.md` [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

Важная оговорка: project research informational, not binding. Если research выявил новое обязательство, его нужно добавить в `.gsd/REQUIREMENTS.md`, прежде чем planning будет на него полагаться [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

В v2 docs это ограничение сформулировано жёстче: `REQUIREMENTS.md` рендерится из requirements, сохранённых в database; agents должны сохранять отдельные requirements через `gsd_requirement_save`, а финальный `gsd_summary_save` для `REQUIREMENTS` проваливается, если активных requirement rows нет. Это защита от ситуации, где markdown выглядит как контракт, но runtime state не знает о требованиях [источник: Auto Mode docs, https://www.opengsd.net/docs/v2/auto-mode].

### Tool policy и границы действий

Каждый auto-mode unit имеет `UnitContextManifest` с `ToolsPolicy`; GSD enforces policy before tool calls execute. Execution units используют `all` mode и могут редактировать project files, запускать shell commands и dispatch subagents. Planning/discussion units обычно работают в `planning` mode: broad reads, writes только planning artifacts under `.gsd/`, read-only shell commands, no subagent dispatch. `planning-dispatch` разрешает subagent dispatch для isolated recon/planning/review. `docs` mode дополнительно разрешает explicit documentation globs вроде `docs/**`, top-level `README*.md`, `CHANGELOG.md`, top-level `*.md` [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

Эта деталь важна для теории: в `gsd-pi` безопасность workflow не только prompt convention, но runtime policy. Запрещённые writes, unsafe bash и неправильный subagent dispatch должны блокироваться hard policy error, а не оставаться "на совести" LLM [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

### Context pre-loading и context mode

Dispatch prompt inlines task plan, slice plan, prior task summaries, dependency summaries, roadmap excerpt и decisions register. Token profile управляет объёмом: budget inlines minimal context, quality inlines everything [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

Context Mode default-on. Units получают guidance: использовать `gsd_exec` для noisy scans, builds, tests и diagnostics; `gsd_exec_search` перед повтором previous sandboxed run; `gsd_resume` после compaction/session resume для чтения `.gsd/last-snapshot.md`. `gsd_exec` пишет capped stdout/stderr и metadata в `.gsd/exec/`, а agent получает короткий digest. В milestone worktree mode `gsd_exec` rejects scripts targeting original project root через `cd ../../..` и похожие traversal patterns [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

### Git isolation

`gsd-pi` поддерживает `git.isolation`:

- `none` default — work happens directly on current branch, no milestone branch/worktree. Полезно для hot-reload workflows, где file isolation ломает dev tooling.
- `worktree` — each milestone runs in `.gsd/worktrees/<MID>/` on `milestone/<MID>` branch. Requires at least one commit; in zero-commit repo временно runs as `none`.
- `branch` — work happens in project root on `milestone/<MID>` branch, useful for submodule-heavy repos.

В worktree/branch mode milestone squash-merged to main as one clean commit. Commits inside milestone sequential and use conventional commit format with GSD metadata trailers such as `GSD-Task: M001/S01/T01` [источники: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md; Git Strategy, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/git-strategy.md].

### Parallel execution и single-host constraint

Auto mode и parallel coordination опираются на project-root SQLite database in WAL mode на local disk. Это supports multiple terminals / worker processes on one machine, но sharing `.gsd/gsd.db*` across machines or network filesystems unsupported. Если нужна cross-host orchestration, нужен external coordinator [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

Parallel orchestration: independent milestones can run simultaneously; each milestone gets its own worker process and worktree, а shared project-root SQLite/WAL runtime coordinates worker heartbeats, milestone leases, dispatch ownership, retry windows и control commands [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

Reactive task execution default-on: GSD derives dependency graph from IO annotations in task plans. Если минимум три ready tasks можно считать safe, non-conflicting tasks dispatch in parallel via subagents; dependent tasks ждут predecessors. Если graph ambiguous или ready tasks меньше threshold, auto mode falls back to normal sequential executor. Implementation названа: `reactive-graph.ts`, integration into `auto-dispatch.ts` и `auto-prompts.ts` [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

### Recovery и supervision

`gsd-pi` явно проектируется для long-running autonomous work:

- Crash recovery: worker state, unit-dispatch state и paused-session metadata сохраняются в SQLite; next `/gsd auto` reconstructs interrupted unit, reads surviving session file и synthesizes recovery briefing from tool calls on disk [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Headless auto-restart: `gsd headless auto` restarts after crashes with exponential backoff 5s -> 10s -> 30s cap, default 3 attempts, configurable `--max-restarts N`; SIGINT/SIGTERM bypass restart [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Provider error recovery: rate limits auto-resume after retry-after or 60s; server errors auto-resume after 30s; permanent errors such as unauthorized, invalid key, billing pause indefinitely and require manual resume [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Context Pressure Monitor: at 70% context usage GSD sends wrap-up signal to finish durable output before context window fills [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Stuck Detection: sliding-window analysis detects repeated dispatch patterns, including A -> B -> A -> B; retry once with diagnostic prompt, then stop for human intervention [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Timeout supervision: soft 20 min, idle 10 min, hard 30 min by default; runtime records timeout phase, timeoutAt, lastProgressAt, lastProgressKind, recoveryAttempts, lastRecoveryReason [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

### Verification enforcement

`gsd-pi` позволяет задавать controlled verification commands:

```yaml
verification_commands:
  - npm run lint
  - npm run test
verification_auto_fix: true
verification_max_retries: 2
```

Команды должны быть directly runnable checks. Single shell pipeline with `|` разрешён, но `||`, redirects, semicolons, backticks и command substitution отвергаются, потому что verification runs as controlled command list, not arbitrary shell program. Если commands не заданы и task plan не даёт `verify`, GSD пытается project discovery: `package.json` scripts first, затем Python pytest markers [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

### Управление auto mode

Команды управления:

```text
/gsd auto
Escape
/gsd stop
/gsd steer
/gsd capture "add rate limiting to API endpoints"
/gsd visualize
/gsd status
```

Escape pauses после current unit while preserving conversation. `/gsd auto` resumes from latest DB state. `/gsd steer` позволяет hard-steer plan documents during execution, changes picked up at next phase boundary. `/gsd capture` сохраняет мысль "fire-and-forget", которая triaged automatically between tasks. Dashboard через `Ctrl+Alt+G` или `/gsd status` показывает current milestone/slice/task, elapsed time, per-unit cost/token breakdown, cost projections, completed/in-progress units, pending captures и parallel worker status [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

Telegram remote control: `/pause`, `/resume`, `/status`, `/progress`, `/budget`, `/log [n]`; GSD polls incoming Telegram commands every ~5 seconds during active auto-mode sessions [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

### Configuration и внешние интеграции `gsd-pi`

Preferences живут в `~/.gsd/PREFERENCES.md` и `.gsd/PREFERENCES.md`; локальные значения проекта либо переопределяют глобальные, либо объединяются с ними по типу поля. Через `/gsd prefs` оператор управляет моделями, timeouts, budget ceiling, token profile и staged discovery. Tool API keys хранятся глобально в `~/.gsd/agent/auth.json` и подставляются во все проекты; environment variables имеют приоритет над сохранёнными ключами [источник: `gsd-pi` configuration, https://www.opengsd.net/docs/v2/configuration].

MCP server configs читаются из `.mcp.json` и `.gsd/mcp.json`. Первый путь подходит для MCP configuration, общей для репозитория, второй — для machine-local paths, local-only secrets и личных сервисов. Документация рекомендует проверять серверы через `mcp_servers`, `mcp_discover` и `mcp_call`, а для `stdio` использовать absolute paths и `env` внутри config, а не полагаться на interactive shell profile [источник: `gsd-pi` configuration, https://www.opengsd.net/docs/v2/configuration].

`token_profile` координирует выбор модели, пропуск фаз и сжатие контекста: `budget` пропускает research/reassessment и выбирает более дешёвые модели, `balanced` выполняет стандартный цикл, `quality` предпочитает более качественные модели. Дополнительные phase toggles позволяют явно управлять `skip_research`, `skip_reassess`, `skip_slice_research`, `reassess_after_slice` и `require_slice_discussion` [источник: `gsd-pi` configuration, https://www.opengsd.net/docs/v2/configuration].

Для multi-repo работы есть `workspace.mode: parent`: `plan-slice` проверяет `targetRepositories` against declared repository IDs, пути задач ограничиваются объявленными repo roots, а per-repo config может задавать role, verification commands и commit policy. Это важная граница: GSD может вести parent workspace, но только если репозитории явно объявлены и пути не выходят за их корни [источник: `gsd-pi` configuration, https://www.opengsd.net/docs/v2/configuration].

`gsd-pi` configuration также показывает, что рабочий процесс расширяется через hooks, workflow templates, skill routing и runtime context. `post_unit_hooks` запускаются после известных unit types вроде `execute-task`, `complete-slice`, `reassess-roadmap` и `run-uat`; `pre_dispatch_hooks` могут modify, skip или replace unit prompt до отправки. `always_use_skills`, `prefer_skills`, `avoid_skills` и `skill_rules` управляют выбором skills по ситуации. `.gsd/RUNTIME.md` встраивается в task execution prompts и хранит сведения о runtime environment: API endpoints, service ports, deployment targets, environment-specific configuration. Это важное уточнение к "где живёт контекст": не только в roadmap/decisions/knowledge, но и в отдельном runtime-файле, который предотвращает выдумывание путей, URL и окружений во время execution [источник: `gsd-pi` configuration, https://www.opengsd.net/docs/v2/configuration].

## Артефакты

### `gsd-core` / `.planning/`

Низкоуровневый `artifact-types.md` задаёт важное правило: форматированный файл сам по себе ещё не рабочий артефакт. У каждого artifact type должны быть shape, lifecycle, location и consumption mechanism; артефакт, который ни один workflow не читает, методологически инертен. Поэтому для GSD важно не только перечислять `.planning/*.md`, но и показывать, какая команда или агент потребляет файл на следующем шаге [источник: `artifact-types.md`, https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md].

Основные артефакты:

- `.planning/PROJECT.md` — project description and requirements from initial discussion [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- `.planning/REQUIREMENTS.md` — REQ-IDs for capabilities [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- `.planning/ROADMAP.md` — phases, goals, status, success criteria [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- `.planning/STATE.md` — current milestone, phase progress, active decisions, blockers, progress metrics; workflows orient from it [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].
- `.planning/config.json` — workflow settings, model profile, gates, git strategy, safety, hooks, model overrides, workflow toggles [источник: configuration docs, https://opengsd.net/docs/v1/configuration].
- `.planning/.gsd-trace.jsonl` — opt-in append-only dispatch audit file, включается через `GSD_AUDIT=1` или `config.audit.enabled`; файл gitignored, команды получают `traceId`, а args по умолчанию редактируются из событий [источник: configuration docs, https://opengsd.net/docs/v1/configuration].
- `.planning/AGENTS.md` или иной файл `agent_skills.source` — проектные инструкции и skills, которые конфигурация может подмешивать всем агентам, отдельным agent names или phase types; это делает навыки отдельным контекстным артефактом, а не только содержанием системного prompt [источник: configuration docs, https://opengsd.net/docs/v1/configuration].
- `.planning/GLOBAL_LEARNINGS.md` или файл из `global_learnings.path` — долговременные project patterns/preferences/lessons, которые могут переживать отдельную phase и затем влиять на будущие планы и исполнение [источник: configuration docs, https://opengsd.net/docs/v1/configuration].
- `.planning/research/STACK.md`, `FEATURES.md`, `ARCHITECTURE.md`, `PITFALLS.md` — project-level research artifacts from new-project flow [источник: `gsd-core` architecture, https://www.opengsd.net/docs/v1/architecture].
- `.planning/codebase/STACK.md`, `ARCHITECTURE.md`, `CONVENTIONS.md`, `CONCERNS.md`, `STRUCTURE.md`, `TESTING.md`, `INTEGRATIONS.md` — brownfield mapping artifacts; YAML frontmatter carries `last_mapped_commit` for drift gate [источник: `gsd-core` architecture, https://www.opengsd.net/docs/v1/architecture].
- `.planning/phases/<phase>/CONTEXT.md` — decisions from Discuss [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].
- `.planning/phases/<phase>/RESEARCH.md` — findings from phase research [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- `{phase}-{N}-PLAN.md` / `PLAN.md` — files to touch, action steps, verify command, done condition, dependency wave [источники: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md; `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- `{phase}-{N}-SUMMARY.md` — what executor built and committed [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- `VERIFICATION.md` — requirement/decision/goal coverage and fix plans if needed [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].
- `UAT.md` — manual acceptance checks and outcomes from `/gsd-verify-work` [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- `.planning/HANDOFF.json` + `.planning/phases/<phase>/.continue-here.md` — structured pause state: machine-readable JSON плюс human-readable resume instructions. Lifecycle: created on pause, consumed by `resume-project`, replaced by next pause. Эта пара показывает, что continuation в GSD является отдельным artifact type, а не только последним сообщением в чате [источник: `artifact-types.md`, https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md].
- PR body from `/gsd-ship` — Summary, Changes, Requirements Addressed, Verification, Key Decisions, optional configured sections [источник: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].
- `.planning/quick/`, `todos/`, `threads/`, `seeds/`, `debug/`, `ui-reviews/`, `continue-here.md` — дополнительные рабочие поверхности для quick tasks, captured ideas, persistent threads, forward-looking seeds, debug-сессий, UI screenshots и передачи контекста [источник: `gsd-core` architecture, https://www.opengsd.net/docs/v1/architecture].
- `.planning/backlog/` — очередь захваченной работы для идей, bugs и будущих улучшений; команды `/gsd-capture` и `/gsd-todo-*` позволяют сохранить материал без немедленного превращения в phase plan [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].
- `.planning/seeds/` — архитектурные или продуктовые hints на будущее; seeds можно harvest/promote в requirements, roadmap items или decisions, когда они становятся достаточно зрелыми [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].
- `.planning/threads/` — постоянные discussion/research threads; полезны для длительных вопросов, где контекст нужен позже, но его рано смешивать с active phase [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].
- `.planning/todos/` — состояние `/gsd-manager` для background tasks, checklist items, heartbeat/status и rollback; полезно как пример task queue рядом с фазовым процессом [источник: `gsd-core` commands docs, https://www.opengsd.net/docs/v1/commands].
- `.planning/graphs/` — артефакты `/gsd-graphify`: dependency graph, critical path, cycle detection, blocked work и schedule hints; этот слой нужен, когда roadmap/plans/issues уже слишком связаны для линейного чтения [источник: `gsd-core` commands docs, https://www.opengsd.net/docs/v1/commands].
- `.planning/intel/API-SURFACE.md` — discovery artifact из API/backend route analysis; команда `gsd-surface` строит карту endpoints, handlers, auth, schemas и downstream dependencies для планирования и проверки затронутых поверхностей [источник: `gsd-core` commands docs, https://www.opengsd.net/docs/v1/commands].
- `INGEST-CONFLICTS.md` — конфликтный журнал `/gsd-ingest-docs`, когда внешний документ противоречит уже существующим planning artifacts; это важно для traceability, потому что ingest не должен молча перезаписывать решения phase или roadmap [источник: `gsd-core` commands docs, https://www.opengsd.net/docs/v1/commands].
- `PLAN-REPAIRS.md`, `CHECKPOINT-NYQUIST.md`, `NYQUIST-PASS.md` — артефакты pre-flight validation перед execution; первый фиксирует auto-repairs, второй останавливает процесс на человеческое решение, третий подтверждает, что plan graph прошёл проверку [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].
- Plan status metadata: `source_sha`, dependency hashes, dirty/expired markers — данные для `/gsd-plan-status`, который отличает пригодный план от stale/orphaned/dirty/expired plan [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].
- Workstream artifacts and branches — состояние параллельных направлений через `/gsd-workstream-*`; это отдельный слой от phase waves, потому что workstream может иметь собственную ветку и checkpoints [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].

### `gsd-pi` / `.gsd/` + SQLite

Основные артефакты:

- project-root SQLite database `.gsd/gsd.db*` — authoritative runtime state for milestones, slices, tasks, requirements, summaries, completion status, memories, decisions [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `.gsd/STATE.md` — markdown projection refreshed from DB, useful for review and prompts, not source of truth when DB is available [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `.gsd/DECISIONS.md` — projected from architecture memories [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `.gsd/KNOWLEDGE.md` — Rules remain manually authored/file-canonical; Patterns and Lessons projected from memory rows [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `.gsd/PREFERENCES.md`, `.gsd/PROJECT.md`, `.gsd/REQUIREMENTS.md`, `.gsd/research/*.md`, `.gsd/milestones/*/M###-CONTEXT.md`, `M###-ROADMAP.md` in deep planning mode [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `.gsd/exec/` — capped stdout/stderr and metadata for noisy shell/build/test scans via `gsd_exec` [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `.gsd/journal/` — events such as `unit-start`, `unit-end`, `post-unit-finalize-start`, `post-unit-finalize-end`, `iteration-end`, used for forensics [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `.gsd/reports/` — self-contained HTML reports with project summary, progress tree, slice dependency graph, cost/token metrics, execution timeline, changelog, knowledge base [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `.gsd/worktrees/<MID>/` — worktree mode location for milestone work [источники: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md; Git Strategy, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/git-strategy.md].
- `.gsd/mcp.json` — machine-local MCP server config; `.mcp.json` остаётся вариантом для repo-shared config [источник: `gsd-pi` configuration, https://www.opengsd.net/docs/v2/configuration].
- `.gsd/RUNTIME.md` — runtime context для task execution prompts: endpoints, service ports, deployment targets, environment-specific configuration, если это не архитектурное решение и не project knowledge [источник: `gsd-pi` configuration, https://www.opengsd.net/docs/v2/configuration].
- `.gsd/workflows/<name>.{yaml,md}` и `~/.gsd/workflows/<name>.{yaml,md}` — project/global workflow definitions; command docs описывают discovery order before bundled workflows [источник: `gsd-pi` commands, https://www.opengsd.net/docs/v2/commands].
- `.gsd/migration/MIGRATION.md`, `.gsd/migration/manifest.json`, `.gsd/migration/legacy/` — audit artifacts and archived legacy `.planning` input after migration from v1 [источник: Migration from v1, https://www.opengsd.net/docs/v2/migration].
- `.gsd/activity/` — session logs, которые troubleshooting docs указывают как одно из мест для диагностики вместе с `/gsd status` и `/gsd forensics` [источник: Troubleshooting, https://www.opengsd.net/docs/v2/troubleshooting].

### `gsd-browser` / browser evidence artifacts

- `browser-artifacts/` или иной каталог из `[artifacts].dir` в `gsd-browser.toml` — место для screenshots, HAR, traces, recordings, PDFs, visual diffs и debug bundles, если команда использует `gsd-browser` как browser evidence backend. Это не `.planning/` и не `.gsd/`, поэтому в будущем Handbook нужно отдельно решать, что из этих файлов коммитится, что прикладывается к PR, а что остаётся локальным диагностическим материалом [источник: `gsd-browser` CLI & MCP Commands, https://opengsd.net/docs/v5/commands].

## Контекст и передача состояния

GSD полезен именно потому, что контекст не живёт только в conversation window. В `gsd-core` `.planning/` делает step outputs readable across sessions: `CONTEXT.md` survives until planner runs; `PLAN.md` survives until executor runs; `VERIFICATION.md` survives until review; `STATE.md` tells any agent where the project currently sits [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].

`artifact-types.md` уточняет эту передачу состояния через потребителей. `ROADMAP.md` читают `plan-phase`, `discuss-phase`, `execute-phase`, `progress` и state-команды; `STATE.md` читают все orchestration workflows и resume/progress/next; `CONTEXT.md` сначала потребляет planner, затем executor; `SUMMARY.md` после plan completion читают orchestrator, planner будущих планов и milestone summary; `HANDOFF.json` и `.continue-here.md` потребляет `resume-project`. Для будущей теории это сильная деталь: durable context работает потому, что у каждого файла есть следующий читатель, а не потому, что он лежит в репозитории [источник: `artifact-types.md`, https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md].

В `gsd-pi` перенос состояния ещё жёстче: database is authoritative, markdown projections are review/prompt/history surface. Это снижает риск, что agent восстановит runtime state из устаревшего markdown, но создаёт другое operational requirement: нельзя шарить SQLite/WAL runtime по network filesystem и нельзя считать ручную правку projection достаточной для изменения state [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

Для будущей теории это хороший пример различия между "file-as-state" и "DB-as-state with markdown projection". В `gsd-core` plain text artifacts сами являются рабочей памятью. В `gsd-pi` plain text artifacts остаются inspectable, но runtime truth находится в DB.

Миграция из v1 `.planning` в `.gsd` показывает, насколько серьёзно `gsd-pi` относится к state authority. `/gsd migrate` парсит старые `PROJECT.md`, `ROADMAP.md`, `REQUIREMENTS.md`, phase directories, plans, summaries, research, top-level `decisions/` и `seeds/`, мапит phases -> slices и plans -> tasks, пишет hierarchy в database и только затем рендерит markdown projections. Если уже есть `.gsd/`, она бэкапится в `.gsd-backups/migrate-YYYYMMDD-HHMMSS/`; полный legacy input архивируется в `.gsd/migration/legacy/` [источник: Migration from v1, https://www.opengsd.net/docs/v2/migration].

Если database отсутствует или повреждена, `gsd-pi` не должен молча восстанавливать runtime state из markdown. Документация предлагает явную операцию `/gsd recover`: она очищает persisted hierarchy plus validation-related state и реконструирует milestone/slice/task hierarchy from rendered markdown. Это destructive recovery/import, а не обычный путь чтения состояния [источник: Migration from v1, https://www.opengsd.net/docs/v2/migration].

В `gsd-core` похожая проблема решается легче, потому что `.planning/` остаётся файловым состоянием, но текущие docs всё равно добавляют state sync команды: `/gsd-state-sync`, `/gsd-state-recover`, `/gsd-recover-context`, `/gsd-resolve-execution` и `/gsd-plan-status`. Они нужны, когда planning state, git history, phase artifacts или interrupted execution перестают согласовываться. Для методологии это важная оговорка: durable artifacts помогают пережить context loss, но сами нуждаются в проверке свежести и восстановлении после interrupted work [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].

## Роли / агенты / участники

В `gsd-core` явные agent roles появляются в workflow:

- researcher / `gsd-phase-researcher`, `gsd-project-researcher`, `gsd-research-synthesizer`, `gsd-codebase-mapper`, `gsd-ui-researcher`;
- planner / `gsd-planner`, `gsd-roadmapper`, `gsd-pattern-mapper`;
- checker / `gsd-plan-checker`, `gsd-integration-checker`, `gsd-nyquist-auditor`, `gsd-ui-checker`;
- executor / `gsd-executor`, `gsd-debugger`, `gsd-doc-writer`;
- verifier / `gsd-verifier`, `gsd-doc-verifier`, `gsd-ui-auditor`.

Configuration docs показывают phase-type -> agent mapping и per-agent model/profile overrides; например `models.execution`, `models.verification`, `model_overrides.gsd-planner`, `runtime: "codex"` [источник: configuration docs, https://opengsd.net/docs/v1/configuration].

Architecture docs дают более низкоуровневую картину: agent definitions лежат в `agents/*.md` с frontmatter `name`, `description`, `tools`, `color`, а общий roster на момент документации — 33 agents. Это не только роли в тексте workflow, но и артефакты установки с разрешёнными инструментами (`Read`, `Write`, `Edit`, `Bash`, `Grep`, `Glob`, `WebSearch` и т.д.) [источник: `gsd-core` architecture, https://www.opengsd.net/docs/v1/architecture].

`agent_skills` добавляет ещё один слой роли: один и тот же `gsd-executor` может получить разные дополнительные project skills в зависимости от agent name или phase type. Это полезно, если команда хочет всегда давать frontend-фазам design-system skill, а backend-фазам API/security skill. Но это также усложняет provenance поведения: чтобы объяснить, почему агент выбрал конкретный паттерн, уже недостаточно смотреть только на `agents/gsd-executor.md` и `PLAN.md`; нужно проверить `.planning/config.json` и skill source, который был применён к этому запуску [источник: `gsd-core` configuration docs, https://www.opengsd.net/docs/v1/configuration].

Низкоуровневые контракты агентских ролей уточняют ответственность. `gsd-planner` отвечает за перевод roadmap goal, requirements, research и phase decisions в исполняемый `PLAN.md`, но не должен исполнять код. `gsd-plan-checker` отвечает за блокирующую проверку плана до execution и не должен сам чинить реализацию. `gsd-executor` отвечает за атомарное выполнение task plan, проверку done criteria, commit и summary, но не должен принимать архитектурные решения, если они выходят за рамки плана. Pass 04 сверил, что эти файлы доступны в текущем `open-gsd/gsd-core`, поэтому для будущего текста их лучше цитировать через `gsd-core/main/agents/*`, а `get-shit-done-redux` оставить только как исторический контекст lineage. Это разделение важно: GSD удерживает качество не только формой phase loop, но и запретом каждой роли брать чужую власть [источники: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md; `agents/gsd-plan-checker.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md; `agents/gsd-executor.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md].

Человек участвует не как постоянный micro-manager, а как owner ambiguity and acceptance: отвечает на Discuss questions, approves roadmap, verifies UAT, resolves `checkpoint:human-verify`, вмешивается в provider permanent errors, merge conflicts, stale worker/invalid worktree blocks и stuck loops.

## Человеческие подтверждения и gates

`gsd-core` по умолчанию interactive. `mode: interactive` confirms at each step; `mode: yolo` auto-approves decisions. Gate settings включают `confirm_project`, `confirm_phases`, `confirm_roadmap`, `confirm_breakdown`, `confirm_plan`, `execute_next_plan`, `issues_review`, `confirm_transition`. Safety settings включают `always_confirm_destructive` и `always_confirm_external_services` [источник: configuration docs, https://opengsd.net/docs/v1/configuration].

В phase loop human input особенно виден здесь:

- Approve proposed roadmap after `/gsd-new-project` [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- Answer implementation preference questions in `/gsd-discuss-phase`; эти answers become `CONTEXT.md` [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- Run `/gsd-verify-work` and answer observable success criteria; failure creates fix plans [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- Resolve `checkpoint:human-verify` before suspicious or assumed package install [источник: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].
- Resolve `CHECKPOINT-NYQUIST.md`, если pre-flight validation нашла проблему, которую нельзя безопасно исправить автоматически. Это человеческая точка решения ещё до execution, а не после того, как код уже изменён [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].
- Resolve Revision Gate outcomes before execution: если `gsd-plan-checker` возвращает `NEEDS_REVISION`, план должен быть исправлен и проверен заново, а не передан executor как "достаточно хороший" [источник: `agents/gsd-plan-checker.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md].
- Decide on architectural deviations raised by executor: новая схема данных, новая service layer, смена библиотеки, auth approach, infrastructure or breaking API требуют checkpoint, потому что executor не должен сам расширять архитектурный scope [источник: `agents/gsd-executor.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md].
- Checkpoint работает как structured continuation boundary: executor выполняет работу до checkpoint, пишет, что уже сделано, что осталось проверить человеком и с какой точки должен стартовать следующий fresh agent. Это не просто просьба "посмотреть"; это механизм сохранения состояния между остановкой и возобновлением [источник: `agents/gsd-executor.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md].
- Issue-driven orchestration добавляет ещё одну человеческую границу: GSD может импортировать GitHub issues в `.planning/issues/`, классифицировать их как `feature`, `bug`, `enhancement`, `documentation`, `technical-debt`, `research`, `question` or `invalid`, а затем человек подтверждает, что входит в milestone/phase scope. Документация подчёркивает human-in-the-loop review для issue plans, потому что issue tracker часто содержит шум, дубликаты и недоописанные пожелания [источник: `gsd-core` issue-driven orchestration, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/issue-driven-orchestration.md].

Reference `checkpoints.md` добавляет экономическую оговорку: human verification имеет холодный старт, потому что человеку нужно восстановить контекст, прочитать дифф и проверить работу. Поэтому GSD по умолчанию предлагает `human_verify_mode: "end-of-phase"`: несколько execution waves можно делать подряд, а затем запускать один consolidated human verification. Это снижает стоимость переключения внимания, но повышает риск позднего обнаружения ошибки; режимы `after-each-wave` и `after-each-task` есть как более строгие альтернативы для risky work [источник: `checkpoints.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/checkpoints.md].

Тот же reference различает human verification, human decision и human action. Решения по архитектуре, package legitimacy и scope не объединяются ради экономии: они должны останавливать работу immediately, потому что continuation без ответа меняет смысл плана. Human action checkpoint нужен для того, что агент не может сделать сам: OAuth/browser login, manual DNS, payment provider setup, credential rotation, App Store approval. В Claude Code-specific оговорке источник допускает автоматическое выполнение CLI/API setup, если ключи уже настроены; человеческое действие требуется только там, где нет API или нужна интерактивная auth [источник: `checkpoints.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/checkpoints.md].

В `gsd-pi` human gates выражены как controls over autonomous execution:

- Escape pauses active auto mode while preserving conversation [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `/gsd steer` changes plan documents during execution; changes picked up at next phase boundary [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `require_slice_discussion: true` pauses before each slice and presents slice context for review; after confirmation execution continues [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Permanent provider errors pause indefinitely and require manual resume [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Git conflicts and dirty overlap require manual cleanup before rerun [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `/gsd verdict <pass|needs-attention|needs-remediation>` может вручную переопределить recorded milestone validation verdict with explicit rationale; это человеческая точка ответственности после автоматической оценки [источник: `gsd-pi` commands, https://www.opengsd.net/docs/v2/commands].
- `/gsd doctor` и `/gsd doctor fix` становятся первым шагом, когда GSD застрял, шумит или ведёт себя неожиданно; doctor checks `.gsd/`, roadmap/slice/task references, runtime state и Git worktree health [источник: Troubleshooting, https://www.opengsd.net/docs/v2/troubleshooting].

## Проверка результата и качество

GSD проверяет качество на нескольких уровнях:

- Plan-checking before execution: plan-checker должен поймать incomplete/inconsistent/ambiguous plans до запуска parallel executors [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].
- Nyquist pre-flight validation: перед execution проверяются ссылаемые файлы, критерии приёмки и граф зависимостей; результатом становятся `PLAN-REPAIRS.md`, `CHECKPOINT-NYQUIST.md` или `NYQUIST-PASS.md` [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].
- Plan freshness: `/gsd-plan-status` проверяет `source_sha`, хэши зависимостей и связь plan artifacts с текущим `HEAD`; устаревший или dirty plan не должен восприниматься как execution-ready только потому, что файл существует [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].
- Revision Gate: `gsd-plan-checker` возвращает `PASS`, `NEEDS_REVISION` или `BLOCKED_BY_MISSING_INPUT`; при revision он перечисляет конкретные исправления плана, а не разрешает execution [источник: `agents/gsd-plan-checker.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md].
- Requirement coverage: `VERIFY` / verifier смотрит, covered ли REQ-IDs [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].
- Decision coverage: решения из `CONTEXT.md` должны попасть в plans and shipped code; configuration docs описывают decision coverage gates, где plan-phase translation gate blocking, а verify-phase validation gate non-blocking [источник: configuration docs, https://opengsd.net/docs/v1/configuration].
- Multi-source coverage audit: `gsd-planner` должен явно покрыть `GOAL`, `REQ`, `RESEARCH` и `CONTEXT` decisions; missing items становятся warning/action before execution, а не тихой потерей scope [источник: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md].
- Безопасность waves до execution: plan-checker должен увидеть dependency order и non-overlap для parallel tasks до запуска executor wave. Если план не показывает, какие файлы и concerns разделены, параллельность становится скрытым источником конфликтов, а не ускорением [источник: `agents/gsd-plan-checker.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md].
- Executor self-check: `gsd-executor` проверяет done criteria, запускает planned verification commands, коммитит только завершённую task и записывает commit hash для summary; при checkpoint продолжение должно стартовать fresh и сверить previous commits [источник: `agents/gsd-executor.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md].
- Verification ladder from `verification-patterns.md`: GSD различает четыре уровня проверки результата — файл существует в ожидаемом месте, содержимое является реальной реализацией, реализация подключена к остальной системе, поведение фактически работает при вызове. Первые три уровня часто можно проверить программно, а четвёртый нередко требует человеческой проверки или browser/runtime evidence. Это полезно для теории, потому что "artifact exists" не должен считаться равным "feature done" [источник: `verification-patterns.md`, https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/verification-patterns.md].
- Independent code review: `/gsd-code-review-*` смотрит на корректность, сопровождаемость, безопасность, тесты и согласованность с планом до ship; это отдельный слой от UAT и acceptance criteria [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].
- UAT: `/gsd-verify-work` walks through success criteria and writes `UAT.md` [источник: `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- Browser evidence: `gsd-browser` can provide screenshots, visual diffs, recordings, HAR, traces and assertions as proof in verification loop [источники: roadmap, https://opengsd.net/roadmap; `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].
- Controlled verification commands in `gsd-pi`: lint/test commands, auto-fix retries, command syntax restrictions [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Artifact existence and verdict validation in `gsd-pi`: missing artifact causes retry with explicit failure context; after cap, pause [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Cost and token visibility: dashboard and reports show per-unit cost/token breakdown, projections and budget-related state [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Codebase drift detection in `gsd-core`: after execute-phase, non-blocking drift gate compares new structural elements against mapped codebase docs and suggests `/gsd-map-codebase --paths ...` or auto-remaps if configured [источник: `gsd-core` architecture, https://www.opengsd.net/docs/v1/architecture].
- Runtime health checking in `gsd-pi`: `/gsd doctor` проверяет целостность `.gsd/`, roadmap/slice/task references, runtime state и Git worktree health перед возобновлением `/gsd auto` [источник: Troubleshooting, https://www.opengsd.net/docs/v2/troubleshooting].
- Dispatch observability in `gsd-core`: stderr error event даёт `traceId` даже без полного audit trail, а `.planning/.gsd-trace.jsonl` позволяет разбирать успешные и ошибочные dispatches после включения `GSD_AUDIT=1`. Это полезно не для acceptance criteria, а для диагностики самого GSD-процесса: какой handler отказал, какие child dispatches относятся к top-level invocation и где потерялась маршрутизация [источник: configuration docs, https://www.opengsd.net/docs/v1/configuration].

`gates.md` полезен как карта блокировок, потому что в high-level docs разные остановки легко смешать. Pre-flight gate срабатывает до expensive work: например, package legitimacy или missing API key должны остановить планирование/исполнение до того, как агент потратит много контекста. Revision gate проверяет artifact после создания: `PLAN.md` может получить `NEEDS_REVISION`, но это ещё не runtime error. Escalation gate нужен во время execution, когда появилась неразрешимая неоднозначность: package not found, архитектурное отклонение, ambiguous user intent. Abort gate используется для unrecoverable state: corrupted repository, impossible requirements или security breach. Для будущей теории важно, что GSD не просто "спрашивает человека", а выбирает разные типы остановки в зависимости от момента и цены продолжения [источник: `gates.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/gates.md].

`verification-patterns.md` даёт практическую сторону этой проверки: искать universal stub patterns (`TODO`, `FIXME`, `PLACEHOLDER`, `coming soon`, `lorem ipsum`, пустые обработчики, `return null`, hardcoded counts/IDs where dynamic expected), затем проверять wiring и runtime behavior. Для React/Next.js источник отдельно показывает, что экспорт компонента и JSX недостаточны: нужно увидеть использование props/state, imports, data fetching или handlers, а интерактивные элементы должны реально отвечать на действия. Эти детали лучше уйдут в Handbook, но в теории они нужны как пример того, что GSD проверяет реализацию против observable behavior, а не против наличия файлов [источник: `verification-patterns.md`, https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/verification-patterns.md].

`gsd-browser` в проверке качества добавляет не только screenshots, но и проверяемую цепочку browser state -> action -> assertion -> evidence. CLI/MCP docs показывают команды и инструменты для snapshot refs, `assert`, `screenshot`, `recording start/stop`, `trace`, `har`, `network`, `debug-bundle`, `timeline`, `session export`, визуальных сравнений и live human takeover. Для GSD это значит, что browser UAT можно превратить из "посмотри глазами" в воспроизводимый evidence artifact, но хранение и публикация этих файлов требуют отдельного правила [источник: `gsd-browser` CLI & MCP Commands, https://opengsd.net/docs/v5/commands].

## Хвост жизненного цикла

После реализации GSD не останавливается на commit:

- `gsd-core` runs `/gsd-verify-work`, then `/gsd-ship`, creates PR and updates `STATE.md` [источники: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md; `your-first-project.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md].
- `/gsd-complete-milestone` archives milestone and tags release; `/gsd-new-milestone` starts next version cycle [источник: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md].
- Issue-driven orchestration может закрывать GitHub issue после `/gsd-ship`, создавать план из issue intake и связывать phase work с issue metadata, но docs оставляют review/confirmation человеком перед включением issue в roadmap/phase [источник: `gsd-core` issue-driven orchestration, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/issue-driven-orchestration.md].
- `gsd-pi` milestone completion requires a latest `milestone-validation` assessment with verdict `pass`; fail/partial/absent blocks closeout [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- `gsd-pi` generates HTML reports in `.gsd/reports/` after milestone completion and can generate reports manually with `/gsd report` [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].
- Git strategy in `gsd-pi` can squash milestone branch/worktree into main as a clean commit and remove worktree/branch afterward [источник: Git Strategy, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/git-strategy.md].
- `git.auto_pr` in `gsd-pi` can push main and milestone branch, then create a PR via authenticated `gh pr create`; failure to create the PR is non-fatal and logged [источник: `gsd-pi` configuration, https://www.opengsd.net/docs/v2/configuration].
- GitHub sync can map milestones, slices and tasks to GitHub Issues, PRs and Milestones, persisting mapping in `.gsd/.github-sync.json` and skipping sync when GitHub API rate limit is low [источник: `gsd-pi` configuration, https://www.opengsd.net/docs/v2/configuration].
- `/gsd report` генерирует HTML reports for all milestones and opens the reports index; `/gsd export` остаётся alias. Для внешних систем `gsd headless query` даёт JSON snapshot без LLM session и RPC child, поэтому после реализации есть две разные поверхности чтения результата: человек смотрит HTML/report/dashboard, а automation читает structured state [источник: `gsd-pi` commands, https://www.opengsd.net/docs/v2/commands].

## Сильные стороны

- GSD даёт понятный operational loop для AI-assisted engineering: не "поговорили с моделью", а bounded phases / slices with durable artifacts.
- Context hygiene встроена в саму форму работы: heavy research, planning, execution и verification уходят в fresh contexts, а основной session остаётся тонким.
- Decisions фиксируются до planning, поэтому planner не обязан угадывать project preferences.
- Verification отделена от execution и может создавать fix plans вместо принятия "код скомпилировался" как done.
- Git history становится частью метода: atomic commits per plan в `gsd-core`, sequential task commits / milestone squash merge в `gsd-pi`.
- `gsd-pi` добавляет runtime-level safeguards: tool policy, DB-backed state, crash recovery, provider error recovery, stuck detection, timeout supervision, artifact verification retries.
- `gsd-core` теперь имеет несколько pre-execution safeguards: Nyquist validation, plan freshness checks, plan checker и code review layer. Это снижает вероятность, что stale or under-specified plan попадёт сразу к executor.
- Backlog, seeds, threads и workstreams дают место для контекста разной зрелости: идея может подождать, исследование может жить отдельно, параллельная линия может иметь собственный checkpoint.
- Artifact taxonomy связывает файлы с потребителями: `CONTEXT.md` нужен planner/executor, `SUMMARY.md` нужен последующим планам, `HANDOFF.json` нужен resume workflow. Это снижает риск накопления "документов для вида", если команда действительно соблюдает consumption mechanism [источник: `artifact-types.md`, https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md].
- Model profiles дают экономический слой метода: planning и debugging можно отправлять на более сильные модели, массовое mapping/checking — на дешёвые, а non-Anthropic runtimes удерживать через `inherit`/`omit`, чтобы workflow не создавал неожиданные model costs [источник: `model-profiles.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/model-profiles.md].
- Существуют lighter primitives (`/gsd-quick`, `/gsd-fast`), что важно: методология признаёт свой overhead и даёт альтернативу для small tasks.
- Open GSD ecosystem строится с visible roadmap, promise/origin pages и MIT-licensed repos; это важно после сложной истории доверия вокруг прежнего upstream [источники: Promise, https://opengsd.net/promise; Origin Credit, https://opengsd.net/origin; roadmap, https://opengsd.net/roadmap].

## Failure modes / overuse risks

### Overhead и ceremony

Документация честно фиксирует trade-offs: `/gsd-discuss-phase`, `/gsd-plan-phase` и `/gsd-execute-phase` как separate steps занимают больше времени, чем один plain prompt; spawning subagents медленнее одного in-context edit; для typo, rename или missing import phase loop overkill [источник: `context-engineering.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/context-engineering.md].

Низкоуровневые контракты агентских ролей усиливают этот риск: даже plan phase включает locked decision extraction, multi-source audit, context budgeting, optional TDD/MVP shaping и plan-checker Revision Gate. Для маленькой правки эта дисциплина будет дороже результата, поэтому GSD нельзя описывать как универсальный стиль для любого изменения [источники: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md; `agents/gsd-plan-checker.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md].

### Неверный размер phase

Слишком большая phase превращается в research project, planner struggles to decompose, executors блокируются, verification становится full audit. Слишком маленькая phase создаёт plan files на несколько строк, overhead больше пользы. Хорошая phase имеет single-sentence goal, bounded research, handful of non-overlapping plans и clear testable definition of done [источник: `the-phase-loop.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md].

Plan Drift Guard показывает ещё один вариант сбоя: даже правильно выбранная phase может породить план, который устареет до исполнения. Если между planning и execution изменился код, decisions, requirements или research, stale plan превращается в скрытую инструкцию к старому состоянию репозитория. Поэтому `/gsd-plan-status` и пути refresh/replan нужно описывать как обязательную проверку для отложенных или возобновлённых работ, а не как удобную диагностику [источник: `gsd-core` User Guide, https://www.opengsd.net/docs/v1/user-guide].

### Иллюзия автономности

`/gsd auto` звучит как "run and walk away", но docs показывают много условий, где нужна человеческая интервенция: permanent provider errors, merge conflicts, dirty overlap, invalid worktree, missing closeout tools, artifact retry exhaustion, stuck loops. Это не слабость, а граница применимости: GSD автоматизирует loop, но не отменяет ownership by operator [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

В `gsd-core` похожая граница видна внутри executor: он может автоматически исправлять прямые bugs текущей задачи, но architectural changes, package substitution и неясные blockers должны превращаться в checkpoint. Если эту границу убрать, GSD легко деградирует в "агент сам решил всё по дороге", а durable artifacts начнут фиксировать уже не человеческие решения, а самовольные отклонения исполнителя [источник: `agents/gsd-executor.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md].

`checkpoints.md` показывает обратный риск: если включить verification after every task, человек начнёт постоянно восстанавливать контекст и проверять малые диффы, а стоимость процесса вырастет быстрее, чем качество. Поэтому режим verification checkpoint должен зависеть от риска: end-of-phase для обычной работы, after-each-wave для рискованных waves, after-each-task только для особо чувствительных изменений. Человеческие decision/action checkpoints при этом нельзя откладывать тем же способом, потому что они блокируют смысловое продолжение [источник: `checkpoints.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/checkpoints.md].

### DB/projection confusion в `gsd-pi`

Ручная правка `.gsd/STATE.md`, `.gsd/DECISIONS.md` или `.gsd/KNOWLEDGE.md` может выглядеть как изменение состояния, но runtime source of truth — SQLite database. Editing projections does not override database unless imported/saved through GSD. Это потенциальный источник confusion для пользователей, привыкших к `gsd-core`, где markdown artifacts сами являются рабочим state [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

При повреждённой database recovery намеренно сделан явным: `/gsd recover` стирает persisted hierarchy and validation-related state before rebuilding from rendered markdown. Это защищает от silent state drift, но создаёт риск для оператора, который воспринимает recover как безобидную "починку" [источник: Migration from v1, https://www.opengsd.net/docs/v2/migration].

### Single-host constraint

`gsd-pi` parallel coordination depends on SQLite/WAL local disk. Попытка растянуть `.gsd/gsd.db*` через network filesystem или несколько machines unsupported. Для distributed orchestration нужен внешний coordinator [источник: Auto Mode docs, https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md].

### Supply-chain и trust

Open GSD явно возник как maintained continuation после trust/ownership concerns around former upstream. `Origin Credit` признаёт complicated chapter; `Promise` делает transparency/community/accountability частью нового проекта. Для методологического текста это нужно подавать аккуратно: не как gossip, а как operational lesson о доверии к agent tooling, installer surfaces, package scopes и migration path [источники: Promise, https://opengsd.net/promise; Origin Credit, https://opengsd.net/origin; GitHub `open-gsd/gsd-core`, https://github.com/open-gsd/gsd-core].

### Runtime-specific quirks

`gsd-core` поддерживает несколько runtimes, но command syntax differs: Claude Code / Copilot / OpenCode / Kilo use `/gsd-command-name`, Gemini uses `/gsd:command-name`, Codex uses `$gsd-command-name`. Installer writes the correct form. Direct file copying from `agents/` or `commands/` into non-Claude runtime skips conversion and can produce schema validation errors [источники: `COMMANDS.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md; GitHub `open-gsd/gsd-core`, https://github.com/open-gsd/gsd-core].

Commands docs уточняют для Codex отдельную operational detail: после установки команды запускаются как `$gsd-start`, `$gsd-progress --next`, `$gsd-plan-phase 1`, `$gsd-execute-phase 1` и т.п.; slash form здесь не является переносимой нормой. Это важно для Handbook: если будущий текст будет давать runnable examples для Codex, он должен использовать `$gsd-*`, а не копировать Claude-style `/gsd-*` [источник: `gsd-core` commands docs, https://www.opengsd.net/docs/v1/commands].

`model-profiles.md` добавляет ещё один runtime-specific risk: default profile может не соответствовать выбранному provider stack. Для Claude Code поверх OpenRouter/local provider нужен `inherit`, иначе GSD может пытаться вызывать Anthropic aliases для subagents; для Codex/OpenCode/Gemini CLI installer должен выставить `resolve_model_ids: "omit"`, чтобы runtime сам выбирал model. Если команда переносит `.planning/config.json` между средами без проверки этих настроек, методология может неожиданно изменить стоимость и качество execution [источник: `model-profiles.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/model-profiles.md].

`gsd-pi` troubleshooting отдельно фиксирует path/package/runtime friction: старый unscoped `gsd-pi` package может конфликтовать со scoped `@opengsd/gsd-pi`, npm global bin может отсутствовать в `PATH`, pnpm может ругаться на global bin directory, auto mode может писать artifacts в wrong directory при старой версии, Windows file locks (`EPERM`, `EBUSY`, `EACCES`) могут мешать обновлять `.gsd/` files или worktrees [источник: Troubleshooting, https://www.opengsd.net/docs/v2/troubleshooting].

В `gsd-core` похожий runtime/config drift возникает из-за слишком мощной `.planning/config.json`: `fast_mode`, `effort`, `model_profile`, per-agent model overrides, `agent_skills`, `global_learnings`, `search_gitignored`, `parallelization.*` и `safety.*` могут менять поведение процесса без видимого изменения команды. Это удобство для зрелой команды и риск для переноса методологии: два проекта оба "запускают `/gsd-plan-phase`", но фактически используют разные модели, skills, gates, границы поиска и политику параллельности [источник: `gsd-core` configuration docs, https://www.opengsd.net/docs/v1/configuration].

Осторожность pass 03 по lineage частично закрыта: низкоуровневые agent files, использованные для planner / plan-checker / executor, доступны в текущем `open-gsd/gsd-core`. Риск остаётся не в том, что источник "не тот", а в том, что такие контракты могут меняться быстрее, чем high-level docs. Перед публикацией стоит ещё раз сверить raw files и релизную версию, но досье уже может считать их первичными источниками текущего `gsd-core`, а не только историческим материалом [источники: `agents/gsd-planner.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md; `agents/gsd-plan-checker.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md; `agents/gsd-executor.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md; GitHub `open-gsd/gsd-core`, https://github.com/open-gsd/gsd-core].

### Инертные артефакты

`artifact-types.md` показывает риск, который легко пропустить при переносе GSD в другую команду: если файл не читает ни один workflow, он не участвует в процессе. Команда может создать красивые `METHODOLOGY.md`, `DISCUSSION-LOG.md`, handoff-файлы или custom notes, но без явного consumption point они становятся архивом рядом с работой. Для будущего текста это хорошая граница: durable artifacts усиливают SDLC только тогда, когда следующий шаг действительно использует их как вход [источник: `artifact-types.md`, https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md].

### Audit/privacy confusion

`gsd-core` audit file выглядит как удобное доказательство хода работы, но он специально выключен по умолчанию и gitignored. При включении `GSD_AUDIT_ARGS=1` аргументы команд попадают в events verbatim; при хранении API keys `.planning/config.json` является security boundary, потому что plaintext keys лежат именно там, хотя UI и logs их маскируют. Если команда будет коммитить `.planning/` без явного правила исключений, методология может создать новый риск утечки рядом с тем местом, где она пытается усилить traceability [источник: configuration docs, https://www.opengsd.net/docs/v1/configuration].

`security_hardening` снижает часть риска через atomic writes, backup files, проверку `.planning/` в `.gitignore`, dangerous git policy и tool permission gates, но не отменяет операторской ответственности. Если команда ослабит `safety.dangerous_git_policy`, добавит широкие `tools.allowed` или будет хранить provider keys в repo-visible `.planning/config.json`, GSD не сможет методологически компенсировать плохую security hygiene [источник: configuration docs, https://www.opengsd.net/docs/v1/configuration].

`gsd-browser` добавляет похожую privacy проблему со стороны evidence. Screenshots, HAR, recordings, PDF exports и trace/debug bundles могут содержать пользовательские данные, cookies, tokens, internal URLs или коммерческую информацию. Product/docs позиционируют эти артефакты как доказательство browser behaviour, но досье должно держать границу: evidence полезен для verification, однако не каждый evidence artifact безопасно коммитить или прикладывать к публичному issue/PR [источники: `gsd-browser` product page, https://opengsd.net/products/gsd-browser; `gsd-browser` CLI & MCP Commands, https://opengsd.net/docs/v5/commands].

### Surface area и routing complexity

Шесть namespace routers помогают скрыть от модели плоский список из десятков skills, но для человека это создаёт новый слой, который нужно понимать. Ошибка маршрутизации может привести к тому, что агент выберет quick/debug/management path вместо полного phase loop или наоборот. `docs/INVENTORY.md` полезен как диагностический источник: он показывает реальную поверхность команд, агентов и workflows, но сам факт такого inventory означает, что Open GSD уже достаточно велик, чтобы требовать сопровождения собственной карты [источник: `gsd-core` inventory, https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/INVENTORY.md].

Команды вроде `/gsd-ingest-docs`, `/gsd-graphify`, `/gsd-surface`, `/gsd-manager` и `/gsd-docs-*` усиливают метод, но расширяют входные каналы. Теперь ошибочный документ может попасть в planning state через ingest, dependency graph может устареть относительно codebase, background task может жить рядом с phase без явного roadmap item, а API surface map может быть прочитан как полная истина, хотя endpoint discovery всегда зависит от framework conventions. Это хорошие инструменты для зрелого процесса, но для теории нужно держать формулировку узкой: GSD работает, когда дополнительные поверхности имеют явных потребителей и проверки свежести [источник: `gsd-core` commands docs, https://www.opengsd.net/docs/v1/commands].

Есть ещё один скрытый источник surface-area cost: MCP schemas. `context-budget.md` прямо говорит, что enabled MCP servers увеличивают baseline token load каждого turn и не управляются обычной GSD-конфигурацией. Если команда подключила много серверов "на всякий случай", GSD может быстрее входить в degraded context tiers даже при аккуратной `.planning/` дисциплине [источник: `context-budget.md`, https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/context-budget.md].

## Что должно попасть в теорию

- GSD как пример "операционного цикла" для AI-driven SDLC: Discuss -> Plan -> Execute -> Verify -> Ship, где каждый шаг предотвращает конкретный класс failure.
- Context rot как practical driver: длинная сессия деградирует без явного reset/state strategy.
- Fresh-context subagents + durable artifacts как базовый паттерн: контекст укорачивается, но continuity сохраняется через files/DB.
- Различие `gsd-core` и `gsd-pi`: framework inside existing runtime vs standalone local-first agent/orchestrator.
- Human decision points: Discuss decisions before planning, approval of roadmap/plan, UAT, package legitimacy checkpoints, slice discussion gate, intervention after auto-mode blockers.
- Verification as artifact-producing phase, not an afterthought: `VERIFICATION.md`, `UAT.md`, browser evidence, controlled lint/test commands, artifact verification retries.
- Observability как отдельный слой качества: `traceId`, `.planning/.gsd-trace.jsonl`, `/gsd doctor`, `/gsd inspect`, `/gsd forensics`, `/gsd report`, `gsd headless query` показывают, что зрелая agentic SDLC методология должна проверять не только код, но и собственную orchestration state.
- Planning as executable transfer: `PLAN.md` должен переносить `GOAL`, `REQ`, `RESEARCH` и `CONTEXT` decisions в конкретные file paths, действия, verification commands, done criteria, `must_haves` и key links.
- Plan review as a blocking gate: `gsd-plan-checker` возвращает `NEEDS_REVISION`, если план теряет требования, решения, error paths, dependency order, verification или context budget.
- Контракты агентских ролей как источник методологии: текущие `open-gsd/gsd-core/main/agents/*` показывают не только роли, но и границы власти каждого агента, поэтому их можно использовать как материал для теории про delegation boundaries.
- Agent authority boundaries: planner не исполняет, checker не чинит реализацию, executor не меняет архитектуру без checkpoint.
- State models: `.planning/` as plain-text state in `gsd-core`; SQLite authoritative state + `.gsd/` projections in `gsd-pi`.
- Git as part of method: atomic commits, worktree/branch isolation, squash merge, PR body generated from planning artifacts.
- Overuse boundary: phase loop is useful when task spans files/sessions/research/decisions; quick/fast primitives are preferred for tiny changes.
- Health/recovery as first-class lifecycle: `/gsd doctor`, `/gsd forensics`, `/gsd recover`, `/gsd closeout`, headless query/recover и explicit migration показывают, что автономная работа требует отдельной механики диагностики, а не только prompt-дисциплины.
- Multi-repo and external integration boundary: `workspace.mode: parent`, MCP configs, GitHub sync и `git.auto_pr` расширяют GSD за пределы одного репозитория, но требуют явного объявления путей, ключей, серверов и `gh` authentication.
- Routing as methodology: namespace meta-skills показывают, что зрелая agentic methodology должна управлять не только кодом, но и собственной skill surface, иначе большой набор команд становится контекстным шумом.
- Pre-execution validity как отдельная тема: Nyquist validation и Plan Drift Guard проверяют, можно ли вообще передавать план executor, до того как появляется diff.
- Артефакт как передача ответственности: `artifact-types.md` помогает сформулировать правило, что durable context должен иметь следующего потребителя. Без consumption mechanism `.planning/` превращается в архив, а не в рабочую память.
- Многоуровневая проверка реализации: existence -> substance -> wiring -> behavior. Это хорошая рамка для различения "файл создан", "код не stub", "код подключён" и "пользовательское поведение работает".
- Model routing как часть методологии, а не только cost optimization: разные роли и фазы имеют разную цену ошибки, поэтому GSD связывает model profile с типом работы и runtime.
- Конфигурация как часть метода: `models.*`, `model_overrides`, `fast_mode`, `effort`, `agent_skills`, `global_learnings`, `parallelization.*` и `safety.*` могут менять реальный процесс без изменения видимой команды. В теории нужно показывать GSD не только как loop, но и как слой политики процесса вокруг loop.
- Входные каналы рядом с phase loop: ingest, graphify, API surface discovery и background tasks помогают управлять рабочим материалом до превращения в фазу, но требуют проверки свежести и явных потребителей.
- Контекст разной зрелости: backlog, seeds, threads и workstreams показывают, что durable context бывает не только "решение" или "план"; методология должна хранить идеи, гипотезы и параллельные линии без насильственного превращения всего в текущий phase scope.
- Gate taxonomy: pre-flight, revision, escalation и abort gates показывают, что "остановить агента" бывает разным действием с разной ценой и разным моментом применения.
- Checkpoint economics: human verification нужно группировать с учётом cold-start cost, а human decisions/actions нельзя откладывать только ради меньшего числа interruptions.
- Browser evidence как companion verification layer: `gsd-browser` показывает, как acceptance может подкрепляться assertions, recordings, traces, HAR и live takeover, не превращаясь в отдельную GSD surface.
- Context budget как часть методологии: правила чтения файлов, запрет на чтение `agents/*.md` orchestrator-ом, degradation tiers и MCP schema cost должны попасть в теорию про context hygiene.

## Что лучше уйдёт в Handbook / Fieldbook

- Командная шпаргалка по `gsd-core`: `/gsd-new-project`, `/gsd-discuss-phase`, `/gsd-plan-phase`, `/gsd-execute-phase`, `/gsd-verify-work`, `/gsd-ship`, `/gsd-progress --next`.
- Практическое правило выбора phase size: примеры good/too broad/too small phase.
- Пример структуры `.planning/phases/01-.../`: `CONTEXT.md`, `RESEARCH.md`, `PLAN.md`, `SUMMARY.md`, `VERIFICATION.md`, `UAT.md`.
- Рецепт для brownfield onboarding: `/gsd-map-codebase` -> `/gsd-new-project`.
- Рецепт для `gsd-pi` auto mode: install, provider setup, `/gsd auto`, pause/resume/stop/steer/capture/status.
- Настройка verification commands и ограничение shell syntax.
- Настройка git isolation: `none`, `worktree`, `branch`; когда hot reload ломается от worktree.
- Troubleshooting checklist для stuck auto-mode: `/gsd status`, `.gsd/journal/`, `/gsd forensics`, `/gsd doctor`, git conflict checks.
- Безопасная работа с package legitimacy checkpoints и suspicious packages.
- Рецепт migration/recovery: `/gsd migrate` для `.planning` -> `.gsd`, `/gsd doctor` после migration, `/gsd recover` только как явная destructive import from markdown.
- Headless recipe для CI/orchestrators: `gsd headless query`, `gsd headless dispatch`, `gsd headless new-milestone --context`, exit codes `0/1/2`.
- Fieldbook-рецепт для внешней automation: `gsd headless query` для чтения состояния, `gsd headless dispatch <phase>` для принудительного шага, `gsd headless recover` как явная recovery-команда, `gsd --mode mcp` только если внешний клиент действительно должен управлять GSD-инструментами.
- Multi-repo recipe: `workspace.mode: parent`, `repositories.<id>.path`, `targetRepositories`, per-repo verification и commit policy.
- Операторская памятка по audit/privacy: когда включать `GSD_AUDIT`, когда нельзя включать `GSD_AUDIT_ARGS`, почему `.planning/config.json` и `.planning/.gsd-trace.jsonl` нельзя автоматически считать безопасными артефактами для коммита.
- Шаблон качественного `PLAN.md`: exact file paths, task actions, acceptance criteria, verification command, rollback/recovery, context budget, `must_haves`, required artifacts, key links.
- Чек-лист для pre-execution plan review по `gsd-plan-checker`: coverage, dependency order, overlap, happy-path bias, testability, scope and missing input.
- Практическая памятка для fresh-agent continuation после checkpoint: что должно быть в structured checkpoint message, как новый executor сверяет previous commits и где человек подтверждает продолжение.
- Операторская инструкция по checkpoints: когда executor может исправить bug сам, а когда обязан остановиться из-за architecture/package/blocker decision.
- Шпаргалка по namespace routers `gsd-core`: `/gsd-workflow`, `/gsd-project`, `/gsd-quality`, `/gsd-context`, `/gsd-manage`, `/gsd-ideate`; когда вызывать router, а когда прямую команду.
- Рецепт pre-flight перед исполнением: `/gsd-plan-status`, Nyquist artifacts, refresh/replan path, что делать со stale/orphaned/dirty/expired plans.
- Verification recipes из `verification-patterns.md`: stub-pattern scan, проверка wiring, runtime smoke, browser-backed evidence и правила, когда программной проверки недостаточно.
- Artifact lifecycle recipes: для каждого файла указать producer, consumer, lifecycle, replacement/archival rule и resume behavior; особенно для `HANDOFF.json`, `.continue-here.md`, `SUMMARY.md`, `VERIFICATION.md`.
- Model profile recipes: как выбрать `quality` / `balanced` / `budget` / `adaptive` / `inherit`, как настроить `model_overrides`, где нужен `resolve_model_ids: "omit"` и как не получить неожиданные расходы через OpenRouter/local provider.
- Codex-specific command examples: использовать `$gsd-*` (`$gsd-start`, `$gsd-plan-phase 1`, `$gsd-progress --next`), а не Claude-style `/gsd-*`, если пример предназначен именно для Codex.
- Практика настройки `agent_skills` и `global_learnings`: где хранить project skills, как не смешать глобальные lessons между проектами и как проверять, какие skills были подмешаны конкретному агенту.
- Практика ingest/graphify/surface: когда запускать `/gsd-ingest-docs`, как читать `INGEST-CONFLICTS.md`, когда обновлять `.planning/graphs/`, как не считать `API-SURFACE.md` исчерпывающей картой без проверки framework-specific routes.
- Worktree/parallelization safety checklist: `require_clean_worktree`, protected branches, `worktree_path`, branch naming, checkpoint-after-wave/task и проверка, что агент действительно стартовал из нужного worktree.
- Практика backlog/seeds/threads: как захватывать будущую работу, когда promote seed to requirement/decision, когда заводить отдельный thread вместо обсуждения в active phase.
- Workstream recipe: создание, branch/checkpoint/merge/status/close, отличие workstream от dependency waves внутри одной phase.
- Security hardening checklist для `gsd-core`: `.planning/` gitignore validation, `safety.dangerous_git_policy`, `tools.allowed/denied/confirm_required`, atomic writes/backups, installer integrity checks.
- Issue-driven orchestration recipe: issue intake, classification, review, conversion into roadmap/phase work, closeout after ship.
- Checkpoint policy recipe: когда выбирать `end-of-phase`, `after-each-wave`, `after-each-task`, и почему decision/action checkpoints не откладываются как verification.
- Context-budget checklist: что читать полностью, что читать только как frontmatter/summary, когда делать checkpoint, как проверять `must_haves` у subagent output и как аудитить enabled MCP servers.
- Browser-proof recipe: `gsd-browser mcp`, snapshot refs, assertions, screenshots/recordings/traces/HAR, human takeover, artifacts retention и privacy policy для browser evidence.

## Локальные различения, чтобы не спутать

- GSD не равен Spec Kit. По имеющимся источникам GSD делает упор на recurring workflow loop, fresh-context subagents, durable state and verification; полноценное сравнение со Spec Kit нужно делать в отдельном сравнительном проходе.
- `gsd-core` не равен `gsd-pi`: первый встраивается в существующий runtime и хранит state в `.planning/`; второй сам является terminal agent/orchestrator и хранит authoritative runtime state в SQLite with `.gsd/` projections.
- `gsd-browser` не является GSD surface; roadmap называет его companion product для browser proof and evidence, который plugs into verification [источник: roadmap, https://opengsd.net/roadmap].
- Open GSD не нужно описывать как чисто новый проект без прошлого: `Origin Credit` прямо признаёт original GSD by Lex Christopherson / Taches, а `Promise` — rebuilding with transparency after trust damage [источники: Origin Credit, https://opengsd.net/origin; Promise, https://opengsd.net/promise].

## Источники

### Прочитанные первичные источники

- Open GSD homepage — https://www.opengsd.net/  
  Роль: общая позиция проекта; формулировки про explicit plans, clean execution contexts, real verification, git history. Первичный источник, высокий приоритет.

- `gsd-core` product page — https://opengsd.net/products/gsd-core  
  Роль: продуктовая поверхность `gsd-core`, supported runtimes, install command, main project artifacts, operating loop. Первичный источник, высокий приоритет.

- GitHub `open-gsd/gsd-core` — https://github.com/open-gsd/gsd-core  
  Роль: README current maintained repository, release/state metadata, five-step loop, repo files, current command surface. Первичный источник, высокий приоритет. Уточнение pass 09: GitHub releases page на 2026-06-09 показывает `v1.4.0-rc.2` от 2026-06-08 как pre-release; прежняя заметка про `v1.3.1` должна рассматриваться как более ранний стабильный контекст, а не как абсолютный latest.

- GitHub `open-gsd/gsd-core` releases — https://github.com/open-gsd/gsd-core/releases  
  Роль: release/version context for current `gsd-core`, distinction between pre-release and stable release facts. Первичный источник, высокий приоритет для дат и версий; перед публикацией нужно перепроверить ещё раз.

- `gsd-core` `docs/explanation/context-engineering.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/context-engineering.md  
  Роль: объяснение context rot, fresh-context subagents, `.planning/`, trade-offs and overuse boundary. Первичный источник, высокий приоритет.

- `gsd-core` `docs/explanation/the-phase-loop.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md  
  Роль: central mental model Discuss -> UI design -> Plan -> Execute -> Verify -> Ship; phase sizing; `.planning/` state transfer. Первичный источник, высокий приоритет.

- `gsd-core` `docs/tutorials/your-first-project.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/tutorials/your-first-project.md  
  Роль: concrete walkthrough with commands and artifacts. Первичный источник, высокий приоритет.

- `gsd-core` `docs/COMMANDS.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/COMMANDS.md  
  Роль: command syntax by runtime, stable commands, flags, produced artifacts, package legitimacy gate, verification, ship. Первичный источник, высокий приоритет.

- `gsd-core` commands docs — https://www.opengsd.net/docs/v1/commands  
  Роль: актуальная web-справка команд: Codex `$gsd-*` spellings, `manager`, `ingest-docs`, `graphify`, `surface`, docs commands, runtime command variants, generated artifacts. Первичный источник, высокий приоритет для pass 09.

- `gsd-core` configuration docs — https://opengsd.net/docs/v1/configuration  
  Роль: `.planning/config.json`, workflow toggles, gates, safety, phased `models`, `model_overrides`, `model_profile`, `fast_mode`, `effort`, agents, `agent_skills`, `global_learnings`, decision coverage, git branching, runtime-specific model handling, audit trail, trace IDs, args redaction, API key masking/security boundary, security hardening, dangerous git policy, tool permission gates and parallelization settings. Первичный источник, высокий приоритет.

- `gsd-core` User Guide — https://www.opengsd.net/docs/v1/user-guide  
  Роль: текущая поверхность команд, namespace routers, Nyquist validation, Plan Drift Guard, code review commands, backlog/seeds/threads/workstreams, state sync/recovery commands. Первичный источник, высокий приоритет для pass 06.

- `gsd-core` Inventory — https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/INVENTORY.md  
  Роль: machine-readable/current-ish inventory of commands, agents and workflows; полезен для понимания размера поверхности и routing complexity. Первичный источник, средний/высокий приоритет; counts могут устаревать быстрее, чем docs.

- `gsd-core` issue-driven orchestration — https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/issue-driven-orchestration.md  
  Роль: GitHub issue intake, classification, human review, conversion into roadmap/phase work, issue closeout after ship. Первичный источник, высокий приоритет для issue-driven lifecycle.

- `gsd-pi` product/GitHub repository — https://github.com/open-gsd/gsd-pi  
  Роль: README local-first agent, install/migration commands, common session commands, what GSD Pi does, repo status. Первичный источник, высокий приоритет. Примечание pass 06: GitHub `releases/latest`, проверенный 2026-06-09, указывает `v1.1.1`; прежняя заметка досье про `v1.2.0` требует отдельной перепроверки перед публикацией.

- `gsd-core` architecture docs — https://www.opengsd.net/docs/v1/architecture  
  Роль: внутренние слои `gsd-core`, agent/reference/template/hook model, data flow, `.planning/` layout, drift gate, installer adaptation, package legitimacy gate. Первичный источник, высокий приоритет для понимания методологии как рабочей системы.

- `gsd-pi` Getting Started — https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/getting-started.md  
  Роль: prerequisites, install commands, upgrade path. Первичный источник, высокий приоритет.

- `gsd-pi` Auto Mode docs — https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md  
  Роль: autonomous loop, SQLite state, deep planning, tool policy, context preloading, git isolation, recovery, verification, stuck detection, controls. Первичный источник, высокий приоритет.

- `gsd-pi` v2 Auto Mode docs — https://www.opengsd.net/docs/v2/auto-mode  
  Роль: актуализированная state authority, idempotent closeout, migration/recovery boundary, deep planning requirement persistence. Первичный источник, высокий приоритет.

- `gsd-pi` Commands Reference — https://www.opengsd.net/docs/v2/commands  
  Роль: session commands, diagnostics, visual briefs, headless mode, JSON query, headless recover, MCP server mode, cloud MCP gateway, reports, remote controls, workflow templates. Первичный источник, высокий приоритет.

- `gsd-pi` Configuration — https://www.opengsd.net/docs/v2/configuration  
  Роль: global/project preferences, auth, MCP config, token profiles, phase toggles, workspace/multi-repo, reactive execution, auto PR, GitHub sync, notifications, remote questions, hooks, skill routing, `.gsd/RUNTIME.md`. Первичный источник, высокий приоритет.

- `gsd-pi` Troubleshooting — https://www.opengsd.net/docs/v2/troubleshooting  
  Роль: `/gsd doctor`, install/package/path issues, provider errors, budget ceiling, stale session ownership, Git conflicts, wrong worktree, MCP, LSP, Windows file locks, recovery commands. Первичный источник, высокий приоритет.

- `gsd-pi` Migration from v1 — https://www.opengsd.net/docs/v2/migration  
  Роль: migration from `.planning` to `.gsd`, backup/preview/audit artifacts, database-first import, explicit destructive recovery from markdown. Первичный источник, высокий приоритет для state/provenance границы.

- `gsd-pi` Git Strategy docs — https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/git-strategy.md  
  Роль: `none` / `worktree` / `branch`, squash merge, sequential commits, worktree management, commit trailers, self-healing git behaviour. Первичный источник, высокий приоритет.

- Open GSD roadmap — https://opengsd.net/roadmap  
  Роль: surfaces: `gsd-core`, `gsd-pi`, `gsd-browser`, `gsd-workbench`, `gsd-cloud`; current direction and boundaries. Первичный источник, высокий приоритет.

- Open GSD Promise — https://opengsd.net/promise  
  Роль: governance/trust framing: transparency, accountability, community, no hidden agenda. Первичный источник, средний приоритет для методологии, высокий для provenance.

- Open GSD Origin Credit — https://opengsd.net/origin  
  Роль: origin credit to Lex Christopherson / Taches, continuity and rebuilding after trust damage. Первичный источник, средний приоритет для методологии, высокий для provenance.

- Open GSD Marketplace preview — https://marketplace.opengsd.dev/  
  Роль: future extension surface: agents, templates, tooling; status as preview/coming soon. Первичный источник, низкий/средний приоритет; не использовать как подтверждение текущей runtime-функции.

- `gsd-browser` product page — https://opengsd.net/products/gsd-browser  
  Роль: companion browser-proof product: deterministic Chrome control, MCP server, snapshots, assertions, screenshots, recordings, traces, live viewer and human takeover. Первичный источник, высокий приоритет для companion verification layer; не смешивать с `gsd-core` или `gsd-pi` как GSD surface.

- `gsd-browser` CLI & MCP Commands — https://opengsd.net/docs/v5/commands  
  Роль: concrete browser evidence commands/tools: snapshot refs, assertions, action recording/cache, screenshots, recordings, traces, HAR, visual diff, debug bundles, session export, live viewer/human takeover. Первичный источник, высокий приоритет для Handbook/Fieldbook по browser UAT.

- `open-gsd/gsd-core` `agents/gsd-planner.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md  
  Роль: низкоуровневый контракт planner-агента: locked decisions, multi-source coverage audit, task anatomy, context budget, TDD/MVP shaping, `must_haves`, key links, wave/file ownership. Первичный источник текущего `gsd-core`, высокий приоритет для понимания планирования.

- `open-gsd/gsd-core` `agents/gsd-plan-checker.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md  
  Роль: низкоуровневый контракт plan-checker: Revision Gate, verdicts `PASS` / `NEEDS_REVISION` / `BLOCKED_BY_MISSING_INPUT`, coverage/dependency/verification/context checks, happy-path bias detection. Первичный источник текущего `gsd-core`, высокий приоритет для понимания gates.

- `open-gsd/gsd-core` `agents/gsd-executor.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md  
  Роль: низкоуровневый контракт executor-агента: atomic task execution, checkpoint handling, deviation rules, architectural-stop boundary, package substitution stop, stuck-signal, commit/summary obligations. Первичный источник текущего `gsd-core`, высокий приоритет для понимания границ власти executor.

- `gsd-core` `get-shit-done/references/checkpoints.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/checkpoints.md  
  Роль: checkpoint taxonomy and economics: human verification cold-start cost, `human_verify_mode`, decision vs action checkpoints, Claude Code automation boundary for CLI/API setup. Первичный источник текущего `gsd-core`, высокий приоритет для human gates.

- `gsd-core` `get-shit-done/references/gates.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/gates.md  
  Роль: gate taxonomy: pre-flight, revision, escalation, abort; timing, examples and operator response. Первичный источник текущего `gsd-core`, высокий приоритет для quality gates.

- `gsd-core` `get-shit-done/references/context-budget.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/context-budget.md  
  Роль: concrete context hygiene rules: orchestrator read limits, subagent prompt limits, degradation tiers, `must_haves`, semantic-quality caveat, MCP schema token cost. Первичный источник текущего `gsd-core`, высокий приоритет для context management.

- `gsd-core` / Open GSD lineage `get-shit-done/references/verification-patterns.md` — https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/verification-patterns.md  
  Роль: verification ladder existence/substance/wiring/behavior, stub-pattern detection, wiring/runtime checks, React/Next.js examples, human verification boundary. Первичный источник reference layer, высокий приоритет для Handbook/Fieldbook; перед финальным текстом желательно сверить точный current path в `gsd-core`.

- `gsd-core` / Open GSD lineage `get-shit-done/references/artifact-types.md` — https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md  
  Роль: artifact taxonomy: shape, lifecycle, location, consumption mechanism; producer/consumer links for `ROADMAP.md`, `STATE.md`, `CONTEXT.md`, `PLAN.md`, `SUMMARY.md`, `HANDOFF.json`, `.continue-here.md`. Первичный источник reference layer, высокий приоритет для понимания durable context как рабочего процесса.

- `gsd-core` `get-shit-done/references/model-profiles.md` — https://raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/model-profiles.md  
  Роль: model profile routing (`quality`, `balanced`, `budget`, `adaptive`, `inherit`), per-agent role cost/quality mapping, non-Claude `resolve_model_ids: "omit"`, OpenRouter/local provider caveat, dynamic routing escalation. Первичный источник текущего `gsd-core`, высокий приоритет для cost/model controls.

### Найденные, но не использованные как основные

- Reddit discussions about migration/trust and user experience. Полезны как community signal, но не являются primary source для механики методологии. В этот проход не перенесены в основной текст, чтобы не подменять документацию слухами.
- ArXiv paper `From Prompt to Process: a Process Taxonomy and Comparative Assessment of Frameworks Supporting AI Software Development Agents` (2026-06-04/05 по выдаче поиска). Найден как потенциальный сравнительный источник, но не прочитан в этом проходе и не использован как подтверждение деталей. Лучше отложить для отдельного comparative synthesis.

## Поисковые формулировки

- `"Open GSD" methodology software development AI`
- `"GSD" "Open GSD" "AI" "software development"`
- `"OpenGSD" GitHub`
- `"Getting Shit Done" "Open GSD"`
- `site:opengsd.net/docs/v2 Open GSD gsd-core gsd auto mode`
- `site:opengsd.net/docs/v2 "gsd" "auto mode" "git"`
- `site:opengsd.net/docs/v2 "gsd" "configuration" "modes"`
- `site:opengsd.net/docs/v1 "GSD" "init" "plan" "execute"`
- `site:opengsd.net/docs/v1 "resolve-execution" "GSD"`
- `site:opengsd.net/docs/v1 "graphify" "Open GSD"`
- `site:opengsd.net/docs/v1/commands "gsd-manager" "heartbeat" "background task"`
- `site:opengsd.net/docs/v1/commands "gsd-ingest-docs" "INGEST-CONFLICTS"`
- `site:opengsd.net/docs/v1/commands "gsd-graphify" ".planning/graphs"`
- `site:opengsd.net/docs/v1/commands "gsd-surface" "API-SURFACE.md"`
- `site:opengsd.net/docs/v1 "planning" ".planning" "Open GSD"`
- `github open-gsd gsd-core agents README workflow`
- `github opengsd gsd-core agents gsd-planner`
- `site:github.com/open-gsd/gsd-core "agents" "README"`
- `raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md`
- `raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md`
- `raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md`
- `site:opengsd.net/docs/v1 "Commands" "gsd-new-project" "gsd-discuss"`
- `site:opengsd.net/docs/v1 "User Guide" "gsd-core" "slash-command"`
- `site:opengsd.net/docs/v1 "verify-phase" "ship" "GSD"`
- `site:opengsd.net/docs/v1 "GSD Core Architecture" "Package Legitimacy Gate"`
- `site:opengsd.net/docs/v1 "codebase_drift_gate" "last_mapped_commit"`
- `site:opengsd.net/docs/v2 "gsd headless query" "SQLite"`
- `site:opengsd.net/docs/v2 "Migration from v1" ".planning" ".gsd"`
- `site:opengsd.net/docs/v2 "workspace.mode" "targetRepositories" "GSD"`
- `site:opengsd.net/docs/v2 "gsd doctor" "runtime state" "worktree health"`
- `site:github.com/open-gsd/gsd-core "agents/gsd-planner.md"`
- `site:github.com/open-gsd/gsd-core "gsd-plan-checker" "NEEDS_REVISION"`
- `site:github.com/open-gsd/gsd-core "gsd-executor" "checkpoint:human-verify"`
- `site:opengsd.net/docs/v1 "GSD_AUDIT" ".gsd-trace.jsonl"`
- `site:opengsd.net/docs/v1 "GSD_AUDIT_ARGS" "config.audit.enabled"`
- `site:opengsd.net/docs/v2 "gsd headless recover" "headless query"`
- `site:opengsd.net/docs/v2 "gsd --mode mcp" "Cloud MCP Gateway"`
- `site:opengsd.net/docs/v2 "post_unit_hooks" "pre_dispatch_hooks" "RUNTIME.md"`
- `site:opengsd.net/docs/v1 "Nyquist" "PLAN-REPAIRS" "CHECKPOINT-NYQUIST"`
- `site:opengsd.net/docs/v1 "Plan Drift Guard" "source_sha" "stale"`
- `site:opengsd.net/docs/v1 "gsd-workstream" "checkpoint" "merge"`
- `site:opengsd.net/docs/v1 "gsd-thread" ".planning/threads"`
- `site:opengsd.net/docs/v1 "gsd-seed" "seed-promote"`
- `site:opengsd.net/docs/v1 "security_hardening" "dangerous_git_policy"`
- `site:opengsd.net/docs/v1/configuration "agent_skills" "global_learnings"`
- `site:opengsd.net/docs/v1/configuration "fast_mode" "effort" "model_overrides"`
- `site:opengsd.net/docs/v1/configuration "parallelization" "worktree_path" "protect_branches"`
- `site:opengsd.net/docs/v1/configuration "runtime" "codex" "model_profile"`
- `site:opengsd.net/docs/v1 "gsd-code-review-phase" "gsd-code-review-pr"`
- `site:github.com/open-gsd/gsd-core/releases "v1.4.0-rc.2" "pre-release"`
- `raw.githubusercontent.com/open-gsd/gsd-core/main/docs/INVENTORY.md`
- `raw.githubusercontent.com/open-gsd/gsd-core/main/docs/issue-driven-orchestration.md`
- `raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/checkpoints.md`
- `raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/gates.md`
- `raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/context-budget.md`
- `raw.githubusercontent.com/open-gsd/gsd-core/main/get-shit-done/references/model-profiles.md`
- `site:github.com/open-gsd/get-shit-done-redux "verification-patterns.md" "existence" "wiring" "behavior"`
- `site:github.com/open-gsd/get-shit-done-redux "artifact-types.md" "consumption mechanism" "HANDOFF.json"`
- `site:opengsd.net/products "gsd-browser" "browser proof"`
- `site:opengsd.net/docs/v5 "gsd-browser" "assert" "trace" "HAR"`
- `site:opengsd.net/docs/v5 "human takeover" "gsd-browser"`

## Кандидаты на иллюстрации

- Phase loop diagram for `gsd-core`: `Discuss -> (UI design) -> Plan -> Execute -> Verify -> Ship`; можно собрать свою схему по `the-phase-loop.md`, не копируя изображение [источник: https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md]. Статус: кандидат на авторскую схему.
- Artifact flow for `.planning/`: `PROJECT.md` / `REQUIREMENTS.md` / `ROADMAP.md` / `STATE.md` -> phase `CONTEXT.md` -> `RESEARCH.md` -> `PLAN.md` -> `SUMMARY.md` -> `VERIFICATION.md` -> `UAT.md` -> PR body. Статус: кандидат на авторскую схему.
- `gsd-pi` auto-mode state machine: Plan -> Execute -> Complete -> Reassess Roadmap -> Next Slice -> Validate Milestone -> Complete Milestone [источник: https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md]. Статус: кандидат на авторскую схему.
- `gsd-pi` state authority diagram: SQLite database as source of truth -> `.gsd/` markdown projections -> dispatch prompt/context -> unit result -> DB update. Статус: кандидат на авторскую схему.
- Migration/recovery diagram: legacy `.planning/` -> `/gsd migrate` preview -> DB import -> `.gsd/` projections -> `.gsd/migration/*`; damaged DB -> explicit `/gsd recover` -> rebuild from rendered markdown. Статус: кандидат на авторскую схему по migration docs.
- `gsd-core` architecture layers: user command -> command layer -> workflow layer -> fresh-context agents -> CLI tools -> `.planning/`. Статус: кандидат на краткую схему, полезную для объяснения "prompt framework vs standalone agent".
- Multi-repo workspace diagram for `gsd-pi`: parent `.gsd` state -> declared repository IDs -> path-scoped tasks -> per-repo verification/commit policy. Статус: кандидат на Handbook-схему.
- Git isolation diagram: `none`, `worktree`, `branch`; milestone branch/worktree squash merge to main [источник: https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/git-strategy.md]. Статус: кандидат на авторскую схему.
- Open GSD roadmap surface map: `gsd-core`, `gsd-pi`, `gsd-workbench`, `gsd-cloud`, companion `gsd-browser` [источник: https://opengsd.net/roadmap]. Статус: кандидат на краткую ecosystem map; не брать site artwork без проверки прав.
- Agent authority diagram for `gsd-core`: planner читает `ROADMAP.md`/`REQUIREMENTS.md`/`RESEARCH.md`/`CONTEXT.md` -> создаёт executable `PLAN.md`; plan-checker возвращает `PASS`/`NEEDS_REVISION`/`BLOCKED_BY_MISSING_INPUT`; executor выполняет atomic task, checkpoint or commit. Статус: кандидат на авторскую схему по контрактам агентских ролей.
- Coverage audit matrix: rows `GOAL`, `REQ`, `RESEARCH`, `CONTEXT decisions`; columns plan tasks / artifacts / verification / key links. Статус: кандидат на Handbook-схему для объяснения quality gate.
- Схема безопасности waves: `PLAN.md` tasks -> file/concern ownership -> dependency waves -> executor contexts -> summaries/commits. Статус: кандидат на Handbook-схему, чтобы объяснить, почему plan-checker проверяет overlap до execution.
- Карточка продолжения после checkpoint: trigger -> work completed so far -> human question/verification -> resume point -> fresh executor reads prior commits. Статус: кандидат на Fieldbook-памятку по человеческим gates.
- Observability stack diagram: `stderr HandlerFailure traceId` -> optional `.planning/.gsd-trace.jsonl` -> `/gsd doctor` / `/gsd inspect` / `/gsd forensics` -> `/gsd report` / `gsd headless query`. Статус: кандидат на Handbook-схему по диагностике самого процесса.
- Security boundary diagram: `.planning/config.json` with plaintext keys, masked UI/log output, `GSD_AUDIT_ARGS` off by default, `.gsd/mcp.json` for local-only MCP secrets. Статус: кандидат на Fieldbook-схему по безопасной эксплуатации.
- `gsd-core` routing surface: user intent -> namespace router (`workflow/project/quality/context/manage/ideate`) -> concrete command -> workflow/agent/reference layer. Статус: кандидат на схему "как не перегрузить модель списком команд".
- Pre-execution validity diagram: `PLAN.md` + `source_sha` + dependency hashes -> `/gsd-plan-status` -> Nyquist -> `PLAN-REPAIRS.md` / `CHECKPOINT-NYQUIST.md` / `NYQUIST-PASS.md` -> executor dispatch. Статус: кандидат на Handbook-схему.
- Context maturity map: backlog item -> seed -> thread -> roadmap/requirement/decision -> phase `CONTEXT.md`/`PLAN.md` -> shipped evidence. Статус: кандидат на теоретическую схему про разные состояния контекста.
- Workstream vs wave diagram: workstream branch/checkpoint/merge как долгоживущая линия; dependency wave как параллельное исполнение задач внутри phase. Статус: кандидат на Fieldbook-схему.
- Gate taxonomy diagram: pre-flight before expensive work, revision after artifact creation, escalation during execution, abort for unrecoverable state. Статус: кандидат на теоретическую схему по разным типам остановки.
- Checkpoint economics diagram: end-of-phase vs after-each-wave vs after-each-task verification, отдельно decision/action checkpoints. Статус: кандидат на Handbook-схему для выбора режима human gates.
- Browser evidence loop: snapshot refs -> action -> assertion -> screenshot/trace/HAR/recording -> UAT/PR evidence, с privacy boundary. Статус: кандидат на Fieldbook-схему для browser UAT.
- Context budget map: orchestrator frontmatter-only reading -> subagent `must_haves` -> degradation tiers -> MCP schema cost. Статус: кандидат на теоретическую схему про context hygiene.
- Verification ladder: existence -> substance -> wiring -> behavior, с отдельной отметкой, где достаточно static/runtime checks, а где нужен человек или browser evidence. Статус: кандидат на теоретическую и Handbook-схему.
- Artifact consumption graph: producer workflow -> artifact shape/location -> consumer workflow; особенно `CONTEXT.md` -> planner/executor, `SUMMARY.md` -> future planner/milestone summary, `HANDOFF.json` + `.continue-here.md` -> resume. Статус: кандидат на схему durable context.
- Model routing matrix: agent role / phase -> default tier (`light`, `standard`, `heavy`) -> profile (`quality`, `balanced`, `budget`, `adaptive`, `inherit`) -> runtime caveats (`omit`, OpenRouter/local). Статус: кандидат на Fieldbook-схему по стоимости и качеству.
- Configuration policy stack: visible command -> `.planning/config.json` -> runtime defaults -> `models.*` / `model_overrides` -> `agent_skills` -> `global_learnings` -> safety/parallelization gates. Статус: кандидат на теоретическую схему о том, что GSD-команда исполняется внутри policy layer.
- Intake and graph layer: external docs -> `/gsd-ingest-docs` -> `.planning/` + `INGEST-CONFLICTS.md`; roadmap/issues/plans/code map -> `/gsd-graphify` -> `.planning/graphs/` -> critical path/blocked work. Статус: кандидат на Handbook-схему для подготовки материала до phase loop.
- Worktree safety diagram: configured base path -> milestone branch/worktree -> protected branches -> executor cwd check -> checkpoint rhythm. Статус: кандидат на Fieldbook-схему по безопасной параллельности.

## Открытые вопросы

- Насколько в будущем тексте нужно использовать старое название `Get Shit Done`, если текущая Open GSD-поверхность переупакована как `Git. Ship. Done.`? Возможно, лучше один раз объяснить lineage и дальше писать `GSD / Open GSD`.
- Нужно ли разделять досье на два отдельных файла: `GSD Core` и `GSD Pi`? Сейчас они связаны общим loop, но фактическая механика state/runtime отличается сильно.
- Нужно ли включать в основной теоретический корпус историю trust/migration? Для теории AI SDLC это важно как пример supply-chain/governance риска, но нужно избежать пересказа community drama.
- Какие low-level reference files из `get-shit-done/references/` реально нужны для будущего Handbook, а какие лучше не тащить в теорию? Pass 07 прочитал `checkpoints.md`, `gates.md` и `context-budget.md`; pass 08 добавил `verification-patterns.md`, `artifact-types.md` и `model-profiles.md`; pass 09 частично закрыл `planning-config`/`git-integration` через текущие web docs configuration/commands, но не прочитал отдельные raw reference-файлы `continuation-format.md`, `git-integration.md`, `planning-config.md` как самостоятельные источники.
- Нужно ли отдельно проверять current npm package names and latest versions перед финальным текстом? На 2026-06-09 product page показывает `@opengsd/gsd-core`, troubleshooting/getting-started — `@opengsd/gsd-pi`; старый unscoped `gsd-pi` упомянут как legacy package. Версии всё равно стоит перепроверить перед публикацией.
- Для audit/privacy в финальном тексте нужно решить, считать ли `.planning/.gsd-trace.jsonl` пользовательским evidence artifact или только operator diagnostic artifact. Configuration docs говорят, что файл gitignored, append-only и требует ручной ротации, поэтому сейчас безопаснее относить его к Handbook/Fieldbook, а не к теоретическому core loop.
- Как точно соотнести `gsd-core` command spellings для Codex (`$gsd-*`) с локальной Codex skill model после CLI 0.130.0? Pass 09 подтвердил web-docs examples `$gsd-start`, `$gsd-progress --next`, `$gsd-plan-phase 1`, но для Handbook может понадобиться отдельная проверка на текущей установленной версии Codex.
- Нужно ли читать GitHub issues/discussions по package legitimacy, context rot, stuck detection и migration, чтобы добавить фактуру failure modes? После pass 02 базовая документационная фактура есть; issues нужны только если будущий текст должен показывать реальные пользовательские сбои, а не только design intent.
- Контракты `gsd-planner`, `gsd-plan-checker` и `gsd-executor` в pass 04 сверены как текущие файлы `open-gsd/gsd-core/main/agents/*`. Открытым остаётся только более узкий вопрос: нужно ли перед финальным текстом сверять конкретную tagged release версию, а не `main`, потому что контракты агентских ролей могут меняться быстрее, чем продуктовые страницы.
- Нужно ли перед финальным текстом отдельно нормализовать release/version facts по `gsd-core` и `gsd-pi`? Pass 09 увидел на GitHub releases `gsd-core v1.4.0-rc.2` как pre-release от 2026-06-08, поэтому досье должно различать pre-release и stable/latest; для `gsd-pi` остаётся прежняя нестыковка между `v1.1.1` на latest page и старой заметкой про `v1.2.0`.
- Нужно ли читать сами workflow/reference files, связанные с Nyquist, Plan Drift Guard, workstreams and security hardening, или для методологического досье достаточно `User Guide` + configuration docs? Pass 07 закрыл общий слой gates/checkpoints/context budget, но не читал специализированные raw workflow files по Nyquist/workstreams/security hardening.
- Нужно ли перед финальным текстом сверить `artifact-types.md` и `verification-patterns.md` именно в текущем `open-gsd/gsd-core`, а не только в `open-gsd/get-shit-done-redux` lineage? Pass 08 использовал GitHub-файлы Open GSD lineage как primary reference layer, но для публикации лучше проверить current package/repo path.
- Нужно ли в финальном тексте вообще включать `gsd-browser`, если он companion product, а не GSD surface? Сейчас безопасная позиция: использовать его только как пример browser evidence в verification loop и не смешивать с основным GSD workflow.
