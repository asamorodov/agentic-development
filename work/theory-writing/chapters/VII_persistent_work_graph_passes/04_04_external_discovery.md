# P04 — внешний поиск и source discovery для главы VII

## Статус

Веб-доступ есть. Поиск выполнялся 15 июня 2026 года. Этот проход не пишет основной текст главы, а собирает внешний материал для механизма главы VII: что можно уверенно использовать, что нужно держать как границу и что лучше не переносить.

Задача поиска была не в том, чтобы собрать «рынок инструментов управления задачами», а в том, чтобы найти фактуру для главы о постоянном графе работы: как работа становится переносимой между сессиями, агентами и людьми; как выражаются зависимости, готовность, блокировки, ожидания, claims, gates, восстановление контекста и отличие рабочего графа от runtime-чекпойнта.

## Главный вывод внешнего поиска

Для главы VII можно опереться на три внешних слоя.

Первый слой — Beads как самый прямой current-practice пример: локальный, Dolt-backed, dependency-aware граф issue/work-item состояния, специально ориентированный на агентов и на продолжение работы после потери/сжатия контекста. Его нужно использовать не как «единственную реализацию PWG», а как наиболее насыщенный пример того, какой формы требует работа, если её должен подхватить другой агент или следующая сессия.

Второй слой — обычные issue-трекеры и task-менеджеры: GitHub Issues, Linear, Task Master. Они показывают, что подзадачи, dependencies, blocked/blocking, status, assignee/responsibility, test strategy и programmatic issue structure уже являются нормальной практикой. Но их обычно недостаточно для главы в нашем смысле: они хорошо фиксируют work tracking, но не всегда несут `prime`, gates, durable wait, source state, claims и переносимый snapshot того, почему работа действительно готова или не готова.

Третий слой — durable execution / agent runtime: LangGraph, Temporal, Pydantic AI integrations, DBOS, Restate. Эти источники нужны в главе прежде всего как граница. Они сохраняют или восстанавливают ход исполнения, graph state, thread state, workflow replay, journaled steps, long-running waits and human-in-the-loop. Но это не то же самое, что постоянный граф работы: runtime может знать, где остановилась программа, но не обязан знать, какая работа открыта, что блокирует следующий шаг, кто claim-нул задачу, какая проверка ещё не превращена в acceptance, какая ветка/источник stale, и что нужно показать следующему агенту перед продолжением.

## Использованные внешние источники

### 1. Beads: прямой якорь для PWG

#### 1.1. Beads GitHub repository

URL: https://github.com/gastownhall/beads

Что прочитано: README / landing material репозитория.

Полезная фактура:

- Beads описывает себя как `Distributed graph issue tracker for AI agents, powered by Dolt`.
- В README прямо говорится о `persistent structured memory for coding agents` и о dependency-aware graph for long-horizon tasks.
- `bd init` добавляет в `AGENTS.md` минимальный рабочий протокол: `bd prime`, `bd ready`, `bd show`, `bd update --claim`, `bd close`, `bd remember`; отдельно подчёркнуто, что не надо использовать Markdown TODO lists.
- В базовом наборе команд есть `bd ready`, `bd update --claim`, `bd dep add`, `bd show`, `bd prime`, `bd remember`.
- Среди features названы Dolt backend, JSON output, dependency tracking, auto-ready detection, hash IDs, compaction, graph links.

Как использовать в главе:

- Как сильный пример того, что для агентской работы простой список задач быстро оказывается слабой формой. Нужны структурные поля и команды, которые агент может читать и менять без человеческой догадки.
- Ввести `prime` не как «summary», а как отдельный механизм подготовки агента к продолжению работы.
- Ввести `ready` как производное состояние графа, а не как ручную пометку «можно делать».
- Ввести `claim` как защиту от параллельного захвата одной и той же работы.

Ограничение:

- Не превращать главу VII в статью про Beads. Beads должен быть примером плотного внешнего якоря, а не предметом главы.

#### 1.2. Beads architecture

URL: https://gastownhall.github.io/beads/architecture

Что прочитано: architecture page, version line, storage model, sync/recovery sections, operational cautions.

Полезная фактура:

- Документация говорит о Dolt как о sole storage backend и source of truth.
- Every write auto-commits; recovery предлагается через `bd dolt pull` или `bd backup restore`.
- Есть embedded mode by default и server mode for multiple agents / orchestrator.
- В списке причин выбора Dolt: version-controlled SQL, cell-level merge, multi-writer server, offline work, JSONL export.
- Multi-machine sync требует дисциплины: push before switching, pull before creating issues, avoid parallel edits to the same issue unless using server mode.
- Recovery model содержит универсальные последовательности восстановления и предупреждение, что `bd doctor --fix` может удалять зависимости, которые выглядят циклическими, включая валидные parent-child отношения. Это важный пример: автоматический repair графа может повредить семантику работы, если не различать типы связей.
- В разделе when not to use Beads перечислены ограничения: large teams 10+, non-developers, real-time collaboration, cross-repo tracking, rich media.

Как использовать в главе:

- Для тезиса о том, что PWG — это не просто «сохранили файл с задачами». Нужен backend/source-of-truth, история изменений, стратегия merge/sync, recovery и ограничения по масштабу.
- Для границы: постоянный граф работы не магически решает real-time collaboration, large-team coordination или rich media tracking.
- Для раздела о деградации: self-repair графа может быть опасен, если он работает только на топологии и не понимает смысла разных связей.

Текущая осторожность:

- На странице architecture указана версия 1.0.5, но GitHub Releases показывает, что v1.0.5 помечена как gated pre-release с предупреждением “do not upgrade”, а v1.0.4 отмечена как latest. В основном тексте главы лучше не делать утверждений вида «текущая стабильная версия Beads — 1.0.5». Достаточно говорить «в текущей документации Beads» и ссылаться на конкретные механизмы.

#### 1.3. Beads core concepts

URL: https://gastownhall.github.io/beads/core-concepts

Что прочитано: core concepts, design philosophy, issue model, dependency types, formulas.

Полезная фактура:

- Design philosophy включает Dolt as source of truth, AI-native workflows, hash-based IDs, JSON output, dependency-aware execution, local-first, declarative workflows.
- Issue = work item with ID, type, priority, status, labels and dependencies.
- Status vocabulary включает `open`, `in_progress`, `closed`; в других командах встречаются также `blocked`, `deferred`, `hooked` как исключения для ready queue.
- Dependency types: `blocks` влияет на ready queue; `parent-child`, `discovered-from`, `related` не блокируют готовность как hard blocker.
- Formulas задают steps with dependencies, variable substitution, gates, aspect-oriented transformations.

Как использовать в главе:

- Сформулировать различие между жёсткой блокировкой и мягкой связью. Не всякая связь в графе означает «нельзя продолжать».
- Поддержать мысль, что PWG должен хранить не только узлы работы, но и типы отношений между ними.
- Аккуратно ввести `discovered-from` как форму «работа возникла во время другой работы», не смешивая её с иерархией и блокировкой.

#### 1.4. `bd ready`

URL: https://gastownhall.github.io/beads/cli-reference/ready

Что прочитано: command page for ready queue.

Полезная фактура:

- `bd ready` показывает open issues with no active blockers.
- Команда исключает `in_progress`, `blocked`, `deferred`, `hooked`.
- Документация подчёркивает blocker-aware semantics и “truly claimable work”.
- `--claim` atomically claims first ready issue.
- `--explain` может объяснить, почему issue появляется или не появляется в ready set.

Как использовать в главе:

- Это один из центральных механизмов главы: готовность — не поле «ready = true», а вычисляемое состояние графа, зависящее от blockers, status, claims and gates.
- Хороший контраст с обычным handoff: summary может сказать «почти готово», а graph-ready система должна показать, что именно ещё мешает claim-able work.

#### 1.5. `bd gate`

URL: https://gastownhall.github.io/beads/cli-reference/gate

Что прочитано: command page for gates.

Полезная фактура:

- Gates are asynchronous wait conditions blocking workflow steps.
- Gates создаются через formula step with gate field or ad hoc gate issue.
- Gate types включают `human`, `timer`, `gh:run`, `gh:pr`, `bead`.
- `bd gate check` закрывает resolved gates; GitHub gates используют `gh`.
- Gate resolution: GitHub Actions run completed/success, PR merged, timer timeout, target bead closed.
- Failed/canceled GitHub run or closed PR can escalate.
- Gate issue blocks another issue; blocked issue will not appear in `bd ready` until gate resolved.

Как использовать в главе:

- Это ключ к разделу про durable wait. PWG хранит не только «что осталось сделать», но и ожидания, которые нельзя превратить в следующий шаг прямо сейчас: human approval, timer, CI run, PR merge, another bead.
- На примере billing/API change можно показать: реализация может быть готова локально, но gate на CI, PR или архитектурный review всё ещё делает работу не-ready.

#### 1.6. `bd prime`

URL: https://gastownhall.github.io/beads/cli-reference/prime

Что прочитано: command page for prime.

Полезная фактура:

- `bd prime` outputs essential Beads workflow context in AI-optimized markdown.
- Вывод адаптируется под MCP mode или CLI mode; CLI может давать full reference примерно на 1–2k tokens.
- Цель — чтобы Claude Code, Gemini CLI, Codex SessionStart hooks не забывали Beads workflow after context compaction.
- Есть `.beads/PRIME.md`, `--export`, `--memories-only`.

Как использовать в главе:

- `prime` нужно отделить от «сводки проекта». Это не пересказ всей истории, а компактная и воспроизводимая подготовка среды/агента к правильной работе с графом.
- Хорошая связь с главой VI: hooks/skills/MCP могут доставить `prime`, но сам work state лежит в PWG.

#### 1.7. Beads Codex integration

URL: https://gastownhall.github.io/beads/integrations/codex

Что прочитано: integration page for Codex.

Полезная фактура:

- Документация описывает Beads integration with Codex through skill, managed `AGENTS.md`, native hooks.
- `bd setup codex`.
- Codex 0.129.0+ supports hooks/compact lifecycle/hook-provided developer context.
- Beads uses lifecycle to inject `bd prime` on SessionStart and recover context after compaction.
- PreCompact checks memories-only but does not inject full context because Codex ignores plain stdout from compact hooks; PostCompact records need refresh; UserPromptSubmit injects full prime once after compaction.

Как использовать в главе:

- Очень хороший мост между VI и VII: route/interface layer может доставлять context refresh, но причина, по которой это имеет смысл, лежит в persistent work graph.
- Можно аккуратно показать, что compaction — не только UX-проблема чата; для agentic development она ломает знание о рабочем протоколе, и поэтому `prime` становится техническим механизмом восстановления рабочей формы.

#### 1.8. Beads troubleshooting

URL: https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md

Что прочитано: troubleshooting sections for ready work, dependencies, agent issues, sandboxed environments.

Полезная фактура:

- Если `bd ready` показывает nothing but open issues, likely open blockers; рекомендованы `bd blocked`, `bd dep tree`, `bd dep remove`.
- Документация подчёркивает: only `blocks` dependencies affect ready work.
- Different dependency types have different meanings: `blocks`, `related`, `parent-child`, `discovered-from`.
- Для complex dependencies рекомендуется упрощать дерево и использовать labels instead of dependencies for loose relationships.
- Agent can't find ready work: check `bd blocked`, `bd ready --json`, `bd show`, `bd dep tree`.
- Sandboxed environments can cause “database out of sync”, failed `bd dolt stop`, hash mismatch warnings, because sandbox cannot signal/kill existing Dolt server process.

Как использовать в главе:

- Это хороший материал для раздела «граф работы не освобождает от дисциплины». Чем сложнее dependency graph, тем больше риск ложных blockers, пустого ready queue, повреждённого repair и confused agent.
- Для границы с IX: sandbox/runtime restrictions влияют на Beads operation, но это не делает PWG runtime layer.

#### 1.9. Beads releases / issue-state caution

URLs:

- https://github.com/gastownhall/beads/releases
- https://github.com/gastownhall/beads/issues/3313

Что прочитано: release page and selected issue.

Полезная фактура:

- Releases page показывает v1.0.5 as gated pre-release with “do not upgrade”; v1.0.4 marked latest.
- Предупреждение по v1.0.5 связано с migration `0043`, которая может break multi-machine `bd dolt` sync after both clones upgrade; fixed v1.0.6 in progress.
- Issue #3313 показывает практический класс проблемы: `bd admin cleanup` / `bd admin compact` failing in embedded mode, routine maintenance forced users toward direct SQL workaround bypassing audit trail.

Как использовать в главе:

- Не использовать в основной линии слишком подробно, чтобы не превратить главу в changelog. Но можно держать как материал для трезвой оговорки: PWG — это инфраструктура состояния; её собственное состояние, миграции, maintenance paths and audit trail становятся частью надёжности рабочего процесса.
- В chapter prose лучше не фиксировать конкретную текущую версию, чтобы текст не устарел моментально.

### 2. GitHub Issues: mainstream issue graph features

#### 2.1. GitHub About issues

URL: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues

Что прочитано: GitHub docs about issues, sub-issues, issue dependencies, assignees and PR integration.

Полезная фактура:

- Issues are for planning, discussing and tracking work.
- Sub-issues break down larger issues and allow browsing hierarchy.
- Issue dependencies define blocked-by / blocking relationships.
- Pull request keywords can close issues; assignees communicate responsibility.

Как использовать в главе:

- Как baseline: часть PWG vocabulary уже встроена в mainstream issue trackers.
- Это полезно для объяснения, что PWG не начинается с нуля. Он радикализирует уже существующую практику dependency/ownership/closure, потому что агентская работа делает слабые места заметнее.

#### 2.2. GitHub sub-issues

URL: https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues

Полезная фактура:

- Sub-issues establish parent-child relationship.
- Parent issue can show progress of sub-issues in projects.
- GitHub supports multiple levels; up to 100 sub-issues per parent and up to eight nested levels.

Как использовать в главе:

- Как пример hierarchy, но с осторожностью: hierarchy ≠ blocker graph. В PWG важно не смешать decomposition with readiness.

#### 2.3. GitHub CLI changelog: issue relationships for agents

URL: https://github.blog/changelog/2026-06-10-github-cli-projects-issue-types-sub-issues-and-issue-dependencies/

Полезная фактура:

- 10 июня 2026 GitHub CLI exposed issue types, parent/sub-issue relationships and issue dependencies from terminal.
- Commands support `--parent`, `--blocked-by`, `--blocking`, and JSON fields for automation.
- Changelog explicitly notes that scripts and coding agents relying on `gh` can use this structure.

Как использовать в главе:

- Это свежий и сильный current-practice сигнал: issue graph is becoming agent-readable through CLI/JSON, not only UI-visible.
- Можно использовать как аккуратную внешнюю опору для тезиса: agentic development требует, чтобы work graph был доступен инструментально, а не только как человеческая карточка в браузере.

### 3. Linear: issue relations and blocked/blocking semantics

URL: https://linear.app/docs/issue-relations

Что прочитано: Linear docs about issue relations.

Полезная фактура:

- Linear supports relationships: blocking, related, duplicate.
- Issues can be marked blocked, blocking, related, duplicate.
- `blocked by` shows an orange flag; `blocking` shows a red flag.
- When a blocking issue is resolved, the blocked flag turns green and moves under Related.
- Duplicate issues move to reserved Duplicate status.

Как использовать в главе:

- Как mainstream contrast: modern issue tools already give visual/semantic blocked/blocking state.
- Но в главе стоит показать, что UI flag is not enough for PWG unless it participates in a machine-readable ready/claim/prime workflow.

### 4. Task Master: AI-oriented task decomposition and dependency clusters

#### 4.1. Task structure

URL: https://docs.task-master.dev/capabilities/task-structure

Что прочитано: task structure page.

Полезная фактура:

- Tasks in `tasks.json` are designed to provide comprehensive information for humans and AI assistants.
- Fields include `id`, `title`, `description`, `status`, `dependencies`, `priority`, `details`, `testStrategy`, `subtasks`, `metadata`.
- Individual task file format preserves fields including dependency list and test strategy.

Как использовать в главе:

- Хороший пример того, что agent-oriented task state часто требует не только title/status, но also implementation details and test strategy.
- Можно использовать для сравнения с PWG: Task Master помогает превратить PRD/tasks into executable plan, но глава VII должна говорить шире — о долговечном рабочем состоянии, gates, source state, claims, recovery.

#### 4.2. Clusters & Execution

URL: https://docs.task-master.dev/capabilities/clusters

Что прочитано: clusters page.

Полезная фактура:

- Task Master detects execution clusters: groups of tasks that can run in parallel, sequenced by dependency graph.
- `tm clusters` visualizes execution topology.
- `tm clusters start` launches an autonomous Claude Code session to execute the plan.
- Tags at same level can run in parallel; higher levels depend on lower levels.
- Task-level clusters group tasks that share the same topological level and have no dependencies on each other.
- Output formats include table, ASCII tree, Mermaid, raw Mermaid, JSON.
- `tm clusters start` can dry-run, limit parallelism, resume from checkpoint, continue on failure.
- It enables agent teams mode through `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`.

Как использовать в главе:

- Как дополнительный пример перехода от list of tasks to executable topology.
- Сильная формулировка для главы: dependency graph is not just a planning diagram; it can become a scheduler-facing / agent-facing execution topology.
- Но параллельная execution topology ближе к VIII/IX, поэтому в VII использовать только для showing why state must contain dependencies and readiness.

#### 4.3. Loop page

URL: https://docs.task-master.dev/capabilities/loop

Статус: ссылка из навигации открылась как 404 Page Not Found. Не использовать как источник фактов. Можно отметить только как navigation/documentation inconsistency, но в главе это не нужно.

### 5. Durable execution and runtime state: boundary sources

#### 5.1. LangGraph persistence

URL: https://docs.langchain.com/oss/python/langgraph/persistence

Что прочитано: persistence overview.

Полезная фактура:

- LangGraph persistence gives agents short-term memory through checkpointers and long-term memory through stores.
- Checkpointers persist a thread’s graph state as checkpoints for conversation continuity, human-in-the-loop workflows, time travel, and fault tolerance.
- Stores persist application-defined data outside graph state for long-term, cross-thread memory: user preferences, facts, shared knowledge.
- The table distinguishes checkpointer vs store by scope: single thread vs across threads.

Как использовать в главе:

- Для границы с IX: runtime graph state and checkpointers are not the same as a work graph.
- Но LangGraph полезен как external vocabulary: checkpoint, thread-scoped memory, store, human-in-the-loop, fault tolerance.

#### 5.2. LangGraph interrupts

URL: https://docs.langchain.com/oss/python/langgraph/interrupts

Что прочитано: interrupts page.

Полезная фактура:

- Interrupts pause graph execution and wait for external input.
- When interrupt is triggered, LangGraph saves graph state using persistence and waits indefinitely until resume.
- Resume happens by re-invoking graph with `Command`.
- Rules: do not wrap interrupt calls in try/except; do not reorder interrupt calls within a node; do not return complex values; side effects before interrupt must be idempotent.

Как использовать в главе:

- Важный boundary contrast: runtime interrupt can safely pause execution, but PWG must still represent the work question: why are we waiting, what decision is needed, what issue is blocked, what evidence will make it ready.
- Good source for explaining why durable wait exists, but not enough to define work-state semantics.

#### 5.3. Temporal human-in-the-loop AI agent

URL: https://docs.temporal.io/ai-cookbook/human-in-the-loop-python

Что прочитано: Temporal AI cookbook example.

Полезная фактура:

- Workflow flow: LLM proposes action, risky action pauses for human approval via Temporal Signal, executes if approved, cancels if rejected or timed out.
- Key features: resource-efficient waiting, signal-based approval, durable timers, complete audit trail.
- Example can wait for hours, days or indefinitely without consuming compute resources while waiting.

Как использовать в главе:

- Strong boundary case for gates/human approval. Temporal can implement durable wait and approval, but it doesn’t by itself solve project work graph semantics.
- Use sparingly: if the chapter mentions human gates, Temporal provides a credible runtime implementation layer, while PWG remains the state layer that makes wait visible to the next worker.

#### 5.4. Pydantic AI durable execution overview and integrations

URLs:

- https://pydantic.dev/docs/ai/integrations/durable_execution/overview/
- https://pydantic.dev/docs/ai/integrations/durable_execution/temporal/
- https://pydantic.dev/docs/ai/integrations/durable_execution/restate/
- https://docs.dbos.dev/integrations/pydantic-ai

Что прочитано: overview + Temporal, Restate and DBOS integration pages.

Полезная фактура:

- Pydantic AI says durable agents can preserve progress across transient API failures, application errors or restarts and handle long-running, asynchronous and human-in-the-loop workflows.
- Officially supported durable execution solutions: Temporal, DBOS, Prefect, Restate.
- Temporal integration relies on replay; saves key inputs and decisions; separates deterministic workflows and non-deterministic activities; workflow can run for extended periods and resume after interruption, but workflow code generally cannot include network/disk I/O.
- Restate records every step in a journal; after process crash it replays journal, skips completed steps, resumes exactly where it left off; LLM calls can be persisted to avoid re-fetching responses; tool executions wrapped in durable steps to avoid duplicated side effects.
- DBOS integration wraps agent run loop as workflows and model/MCP requests as steps; custom tools and event stream handlers may need explicit decoration or may be skipped if durability is not needed.

Как использовать в главе:

- This is boundary/source-state material. It shows that durable execution is an active, current layer in AI agent infrastructure.
- The chapter should avoid the false equivalence “PWG = durable execution.” Durable execution preserves process progress; PWG preserves work semantics and readiness between possible processes.
- Good formulation for chapter: a durable runtime can resume a run; a PWG lets a different run, different agent or human understand what is worth resuming and why.

### 6. Academic / broader support: issue dependency as graph

URL: https://arxiv.org/abs/2004.06830 (Issue Dependency Network for Improved Project Management)

Что прочитано: abstract-level material from search result.

Полезная фактура:

- Issue trackers are prevalent but focus on lifecycle of single issues, while issues can also express dependency networks.
- Proposed approach treats issues and dependencies as separate objects and constructs an issue graph.
- Adds dependency detection/checks for conflicts and incomplete matters.

Как использовать в главе:

- Optional support only. It can help show that issue-dependency graphs are not a brand-new AI-era invention.
- Probably not necessary in main prose unless we need one short sentence distinguishing conventional issue graph research from PWG as an agentic-development work-state layer.

## Источники, которые стоит держать за границей главы

### Gas Town materials

Known source family:

- https://github.com/gas-town/gas-town
- https://docs.gas.town/overview
- https://docs.gas.town/glossary
- https://docs.gas.town/gas-stations
- https://docs.gas.town/beads
- https://dolthub.com/blog/2024-11-07-gas-town/
- https://steve-yegge.medium.com/welcome-to-gas-town

Статус для главы VII:

- Не поднимать как основной внешний корпус в этой главе.
- Использовать только для короткой границы с главой X: Gas Town — это более широкий организационный город/среда, роли и газовые станции; VII — минимальная переносимая форма рабочей картины.
- Beads можно использовать независимо от полного Gas Town narrative, чтобы глава VII не распухла в материал будущей главы X.

### GSD / BMAD / TDAD / Pact / MADR / CODEOWNERS / Argo / SRE / Shopify / Stripe / Mike McQuaid

Статус для главы VII:

- Эти источники полезны для других глав: process, gates, ownership, evidence, acceptance, release discipline, ADR.
- Для VII они могут создавать соблазн расширить текст в стороны. Сейчас их лучше не читать заново и не переносить, кроме точечных внутренних связок уже в корпусе фрагментов.

### Third-party Beads blog snippets and tool-list pages

Примеры найденных/упомянутых классов источников:

- короткие tool listings;
- пересказы Beads без документационной глубины;
- старые статьи, где Beads описывается ещё через Git/Markdown semantics, а текущая документация говорит о Dolt as source of truth.

Статус:

- Не использовать как source of truth.
- Допустимы только как historical/background if later needed, но глава VII не нуждается в них.

### Task Master Loop page

URL: https://docs.task-master.dev/capabilities/loop

Статус:

- Открывается как 404, несмотря на ссылку из навигации. Не использовать как источник.

## Предлагаемая source usage policy для главы VII

1. Для механизма PWG ссылаться прежде всего на Beads official docs / repo:
   - repo/README;
   - architecture;
   - core concepts;
   - `bd ready`;
   - `bd gate`;
   - `bd prime`;
   - Codex integration;
   - troubleshooting только для operational caveats.

2. Для baseline issue graph ссылаться на GitHub and Linear:
   - GitHub issues/sub-issues/dependencies;
   - GitHub CLI changelog 2026-06-10 as fresh agent-readable evidence;
   - Linear issue relations.

3. Для AI task graph / execution topology использовать Task Master minimally:
   - task structure;
   - clusters/execution;
   - не использовать 404 loop page.

4. Для runtime boundary использовать LangGraph/Temporal/Pydantic/DBOS/Restate:
   - только чтобы объяснить отличие PWG from durable execution;
   - не превращать VII в durable runtime chapter.

5. Версионные утверждения о Beads писать осторожно:
   - не утверждать стабильность v1.0.5;
   - если нужно упомянуть текущую нестабильность, лучше в примечании или boundary paragraph, not main mechanism.

## Кандидаты на перенос в будущий основной текст

### Короткая формула отличия

Постоянный граф работы не является ни summary, ни issue list, ни runtime checkpoint. Summary переносит рассказ; issue list переносит набор карточек; runtime checkpoint переносит точку исполнения. PWG должен переносить состояние работы как систему продолжения: что можно брать, что нельзя брать, почему нельзя, кто уже взял, чего ждём, на каком источнике стоим, какая проверка закрывает вопрос и что нужно показать следующему агенту перед действием.

### Beads как пример ready semantics

`ready` в таком графе лучше понимать не как ручную метку, а как вычисляемый ответ на вопрос: есть ли у work item активные blockers, gates, claims or excluded statuses. Это особенно важно для агентов: без вычисляемой готовности агент либо бросается в заблокированную задачу, либо не видит подхватываемую работу.

### Gates as durable wait

Gate — это не комментарий «подождать CI» и не человеческая память о том, что надо вернуться. Это work-state object, который удерживает blocked work outside the current session and can be resolved by human decision, timer, CI run, PR merge or another work item.

### Prime as workflow restoration

`prime` — это не summary of everything. Это краткий protocol/state refresh, который позволяет агенту снова работать с графом after compaction/session start. Поэтому он принадлежит к пограничной зоне VI/VII: delivery comes through interface/hooks/skills, but the reason and content come from persistent work graph.

### Boundary with durable execution

Durable execution solves “this run can survive interruption.” PWG solves “this work can be understood and continued by another run.” These overlap when a runtime waits for human approval, CI or a timer, but they are not interchangeable.

## Открытые вопросы после discovery

1. Нужно ли в основной главе упоминать release caution по Beads v1.0.5? Скорее нет, если только в небольшой оговорке о том, что work-state infrastructure has its own state and upgrade risks.
2. Нужно ли ссылаться на academic issue-dependency paper? Скорее нет в основном тексте, если GitHub/Linear/Task Master and Beads already give enough practical grounding.
3. Нужно ли подробно вводить Task Master clusters? Возможно один абзац. Более подробная orchestration belongs to VIII/IX.
4. Нужно ли включать Temporal/LangGraph examples в основной текст? Да, но как contrast, не как предмет.
5. Нужно ли повторно поднимать Gas Town sources? Нет для VII; достаточно уже имеющихся atlas/dossier boundaries and one sentence pointing forward to chapter X.
