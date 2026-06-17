# Атлас V2 — подробная карта статей технического слоя

Статус: рабочая карта для пересборки target-group plans.  
Дата: 2026-06-17.  
Основание: ADR-0012, ADR-0013, ADR-0014 и жанровая диагностика ex-A3.

## Назначение

Этот документ — не статья Атласа и не финальная навигация сайта. Это рабочая карта, из которой должны строиться новые планы статей Атласа. Она фиксирует, что именно нужно собрать в досье и какие разделы должна закрыть каждая статья.

Главное правило: статья Атласа строится по техническому слою, а не по жизненному циклу изменения. Она должна показывать реальные технологии, форматы, протоколы, рабочие поверхности, артефакты, ограничения и критерии выбора. Хорошая концептуальная статья без этого payload не считается принятой статьёй Атласа.

## Общая форма статьи

Каждая крупная статья уровня A должна пройти одну и ту же рамку:

```text
слой и его задача
→ классы решений
→ конкретные технологии, протоколы, форматы и рабочие поверхности
→ артефакты, которые они создают или меняют
→ техническая логика работы
→ отличия конкурирующих подходов
→ критерии выбора
→ типовые сбои
→ связи с соседними слоями
```

Перед финальной сшивкой нужен technological payload gate. Мини-досье должны предъявить достаточно фактуры, чтобы читатель после статьи понимал не только смысл слоя, но и то, чем люди реально пользуются.

## Быстрая карта A1–A16

| ID | Рабочее название | Слой | Главный риск подмены |
| --- | --- | --- | --- |
| A1 | Контекстный интерфейс проекта для агента | Где живут явные правила, знания и процедуры проекта для агента | Свести к списку файлов инструкций |
| A2 | Рабочие поверхности coding agents | Где агент действует над кодом и проектом | Смешать чат, IDE, CLI, облако и PR-agent в один обзор продуктов |
| A3 | Оркестрация и фреймворки агентского исполнения | Как строится управляемый агентский процесс | Написать историю ReAct или каталог фреймворков |
| A4 | Инструменты, протоколы, доступы и полномочия | Как агент получает возможность и право действовать | Уйти в общую философию ответственности или security-обзор |
| A5 | Наблюдаемость, traces и evals | Как видеть, воспроизводить и измерять агентскую работу | Свести к фразе «нужны логи и бенчмарки» |
| A6 | Git, worktree и PR/MR как субстрат агентского изменения | Как результат получает форму change candidate | Спрятать Git внутри CI/review |
| A7 | CI, status checks, review и acceptance gates | Как candidate проходит проверки и решение о статусе | Повторить ex-A3 как теорию принятия |
| A8 | Спецификации, планы и исполняемые процессные артефакты | Как намерение превращается в управляемую работу | Смешать методологии без технического сравнения |
| A9 | Воспроизводимые среды исполнения и песочницы | Где агент безопасно запускает команды, тесты, сборку и приложение | Растворить среду в A2/A4/A7 |
| A10 | Индексация, поиск и извлечение контекста из кодовой базы | Как агент находит нужный код и проектные закономерности | Смешать с инструкциями A1 или с памятью A12 |
| A11 | Issue-to-agent: задачи, очереди, assignment и progress surfaces | Как задача становится агентской рабочей единицей | Свести к issue templates из A8 или к PR из A6 |
| A12 | Долгая память проекта и повторное использование опыта | Как опыт прошлых сессий и решений становится доступен будущей работе | Превратить в рекламу Нoveia или в общую философию памяти |
| A13 | Безопасность агентской разработки и supply-chain controls | Как защищать агентский контур от инъекций, секретов, вредных зависимостей и небезопасного кода | Смешать с A4 или общей AI security |
| A14 | Browser/GUI/app feedback surfaces | Как агент видит и проверяет работающее приложение через UI, браузер и визуальные следы | Растворить в средах исполнения или E2E-тестах |
| A15 | Model/provider layer, routing, cost and inference constraints | Как выбор модели, провайдера, gateway и routing влияет на процесс | Сделать быстро устаревающий рейтинг моделей |
| A16 | Организационный контекст, software catalog и developer portal | Как агент узнаёт сервисы, ownership, environments, runbooks, зависимости и платформенные правила | Растворить в A1/A11 или сделать обзор Backstage/Port без agentic-development угла |

## A1. Контекстный интерфейс проекта для агента

**Назначение слоя.** Показать, как проект становится читаемой и исполнимой средой для агента. Агент должен получать не только текст задачи, но и правила проекта, ограничения, процедуры, стиль, источники правды, точки остановки и способы восстановления.

**Обязательные темы.** `AGENTS.md`; `CLAUDE.md`; Cursor Rules; GitHub Copilot custom instructions; Codex/Amp instructions; Kiro steering; skills; hooks; subagents; project docs; specs; ADR; task package / local working sheet; source manifest; старение и ремонт инструкций после неудачного прогона.

**Мини-досье для пакета.**

1. Инструкционные файлы и область действия: корневые, вложенные, tool-specific и task-specific правила.
2. Steering / project knowledge: постоянные проектные правила, документы как рабочее знание, конфликт и устаревание.
3. Skills/hooks/subagents: что является инструкцией, что процедурой, что автоматическим датчиком, что делегированием.
4. Task-local interface: START.md, рабочий лист, acceptance criteria, source manifest, package contract.
5. Failure and repair: устаревшие правила, over-instruction, missing context, conflict of instructions, recovery update.

**Артефакты слоя.** `AGENTS.md`, nested rules, instruction file, skill file, hook config, subagent profile, steering file, task package, source manifest, local acceptance criteria, rule update note.

**Критерии выбора.** Одноразовая задача или повторяемый процесс; один инструмент или несколько агентов; насколько важно наследование правил; сколько контекста держать в инструкции, а что вынести в документы; где будет repair после ошибки.

**Граница.** Не превращать статью в учебник по каждому инструменту. A1 говорит, где агент получает правила и знания; A2 говорит, где он действует; A9 — в какой воспроизводимой среде это происходит; A14 — как он видит и проверяет приложение через UI.

## A2. Рабочие поверхности coding agents

**Назначение слоя.** Показать, где агент реально работает: в чате, IDE, CLI, облачной задаче, песочнице, локальном open-source окружении или PR-контуре. Это выбор прав, видимости, воспроизводимости, проверки и стоимости контроля.

**Обязательные темы.** Chat-based coding; IDE agents; CLI agents; cloud coding agents; PR-agent / issue-to-PR mode; sandbox/worktree/devbox; Aider; OpenHands; SWE-agent-подобные среды; Computer Use / browser-use forms упоминаются здесь как рабочие поверхности, но подробно разбираются в A14 как отдельный слой UI/app feedback.

**Мини-досье для пакета.**

1. Chat-based coding: какие артефакты остаются и где границы.
2. IDE agents: локальная навигация, diff, review, редакторская поверхность.
3. CLI agents: shell, commands, repo-wide edits, local checks, approvals.
4. Cloud coding agents and PR agents: remote branch, issue-to-PR, agent-created PR.
5. Open-source execution environments: OpenHands, SWE-agent, Aider-like surfaces.
6. Sandbox/worktree/devbox: изоляция, запуск проверок, воспроизводимость.

**Артефакты слоя.** Chat transcript, local diff, patch, command log, terminal output, worktree, sandbox snapshot, cloud branch, agent-created PR, task run log.

**Критерии выбора.** Нужен ли агенту полный репозиторий; можно ли запускать проверки; кто видит diff и когда; как ограничивается радиус ущерба; можно ли воспроизвести run; насколько удобно передавать результат в review.

**Граница.** Не сравнивать продукты напрямую как `лучший/хуже`. Сравнивать классы рабочих поверхностей. Оркестрационные фреймворки относятся к A3, Git/PR substrate — к A6.

## A3. Оркестрация и фреймворки агентского исполнения

**Назначение слоя.** Показать, как строится управляемый агентский процесс, когда одного агента в одной рабочей поверхности недостаточно: графы, маршрутизация, состояние, роли, повторные попытки, human gates и возобновление процесса.

**Обязательные темы.** ReAct / tool-use loop как базовая форма; LangGraph; OpenAI Agents SDK; Google ADK; AutoGen; CrewAI; LlamaIndex Workflows; самописные workflow runners; state machines; multi-agent orchestration; human-in-the-loop stops; resumable workflows.

**Мини-досье для пакета.**

1. Базовый цикл: reason/act/observe, tool calling, observation, repair.
2. Graph/state frameworks: LangGraph и state-machine подход.
3. Agents SDK / ADK class: agents, tools, handoffs, guardrails, traces.
4. Multi-agent frameworks: AutoGen, CrewAI and role/task orchestration.
5. Workflow/data frameworks: LlamaIndex Workflows and event/workflow models.
6. Self-built orchestration: runner, queue, state file, explicit gates.
7. Human gates and resumability: interrupts, checkpoints, approvals, retries.

**Артефакты слоя.** Graph node, edge, state object, tool call, handoff, run id, checkpoint, interrupt, retry record, workflow event, agent role, route decision, trace link.

**Критерии выбора.** Нужен ли persistent state; есть ли ветвление и параллельные ветки; нужны ли разные роли/агенты; сколько human gates; нужна ли наблюдаемость и replay; сколько стоит поддержка фреймворка; проще ли явный runner, чем общий framework.

**Граница.** Не делать историческую статью про papers. Не делать каталог LangGraph/AutoGen/CrewAI. Главное — какие orchestration patterns они воплощают и когда слой нужен.

## A4. Инструменты, протоколы, доступы и полномочия

**Назначение слоя.** Показать разницу между техническим вызовом инструмента, доступом к данным, полномочием действовать и правом признать результат завершённым.

**Обязательные темы.** Tool/function calling; MCP; A2A; connectors; sandbox permissions; approvals; secret handling; scoped access; audit logs; prompt injection; tool poisoning; data boundaries; organizational policy.

**Мини-досье для пакета.**

1. Tool/function calling: схема вызова, результат, ошибки.
2. MCP connectors and resources: что даёт протокол и какие риски вводит.
3. A2A / agent-to-agent boundaries: где начинается межагентское действие.
4. Approval and permission profiles: allow/ask/deny, scoped actions, human confirmation.
5. Secrets and data boundaries: токены, redaction, минимизация доступа.
6. Prompt injection / tool poisoning: типовые атаки и защитные patterns.
7. Audit and organizational control: logs, policy, revocation, accountability.

**Артефакты слоя.** Tool schema, connector config, MCP server/resource/tool, approval prompt, permission profile, audit log, secret reference, redaction rule, policy file, deny/allow list.

**Критерии выбора.** Насколько опасно действие; какие данные видит агент; можно ли действие отменить; нужен ли человек до вызова или после; как отозвать доступ; что должно логироваться; как ограничить prompt injection через tools.

**Граница.** Не писать общую статью о безопасности ИИ. A4 говорит о праве вызвать действие и границах доступа; A13 отдельно раскрывает безопасность агентского контура и supply-chain controls; A7 говорит о праве признать изменение завершённым.

## A5. Наблюдаемость, traces и evals

**Назначение слоя.** Показать, как агентскую работу можно видеть, воспроизводить, сравнивать и измерять.

**Обязательные темы.** Trace; span; tool-call log; run tree; replay/debug surfaces; LangSmith-подобные системы; Langfuse/Phoenix-подобный класс; OpenTelemetry-like vocabulary там, где полезно; eval harnesses; regression evals; golden tasks; automated graders; SWE-bench и близкие coding-agent benchmarks; run comparison.

**Мини-досье для пакета.**

1. Trace model: run, span, tool call, observation, error.
2. Observability platforms: LangSmith/Langfuse/Phoenix classes and what they store.
3. Eval harnesses: local tasks, golden tasks, regression evals, graders.
4. Coding-agent benchmarks: SWE-bench and benchmark-based trust limits.
5. Debug and replay: how traces are used to repair agents/workflows.
6. Metrics and comparison: model/toolchain/prompt/orchestration comparisons.

**Артефакты слоя.** Trace, span, run id, tool-call record, eval dataset, golden task, grader output, benchmark score, regression report, prompt/version comparison, replay link.

**Критерии выбора.** Нужен debug или usage logging; есть ли repeated workflow; нужно ли сравнивать версии; можно ли определить success criteria; кто читает trace; что не покрывает eval.

**Граница.** A5 показывает, как увидеть и измерить run; A7 показывает, как candidate проходит gates; Теория XI объясняет достаточность проверочного материала.

## A6. Git, worktree и PR/MR как субстрат агентского изменения

**Назначение слоя.** Показать, почему version control в агентской разработке становится не фоном, а несущей поверхностью изменения. Агент должен оставлять не только текстовый отчёт, но и изолируемый, сравнимый, ревьюируемый и откатываемый материал.

**Обязательные темы.** Git as baseline; working tree; index; commit; history; diff; patch; branch per task; worktree per agent; commit as checkpoint; PR/MR as change candidate; linked issue; review state; audit trail; merge; squash; rebase; cherry-pick; revert; rollback; bisect; file restore; conflict surface; Git-compatible варианты вроде Jujutsu/Sapling через вопрос совместимости с Git/PR/CI/review контуром.

**Мини-досье для пакета.**

1. Git objects and working states for agentic change.
2. Branch/worktree strategies for agents and parallel tasks.
3. Diff/patch/commit as reviewable and recoverable material.
4. PR/MR as candidate container and provenance surface.
5. Merge/rebase/squash/cherry-pick/revert/bisect as lifecycle operations.
6. Multi-agent conflict patterns: mixed tasks, hidden conflicts, semantic conflicts.
7. Git-compatible alternatives: what they change and what remains Git/PR-compatible.

**Артефакты слоя.** Working tree, index, branch, worktree, commit, diff, patch, PR/MR, linked issue, review state, merge commit, squash commit, rebase history, revert commit, conflict marker, bisect result.

**Критерии выбора.** Одна задача или параллельные agent tasks; нужен ли отдельный worktree; как часто делать commit checkpoints; когда branch должен стать PR; как сохранять readable history; когда squash/rebase/merge commit; как не потерять материал разбора при force push или rebase; как Git слой связан с CI/review gates.

**Граница.** Не превращать статью в учебник Git. Git/PR/MR оформляют candidate; CI/status checks/review/merge rules применяют gates.

## A7. CI, status checks, review и acceptance gates

**Назначение слоя.** Показать, как уже оформленный change candidate проходит проверочные и человеческие контуры перед принятием, отклонением, доработкой или отложенным статусом. Эта статья должна заново пересобрать тему ex-A3, но в техническом разрезе.

**Обязательные темы.** CI systems as class: GitHub Actions, GitLab CI, Azure Pipelines, Buildkite, CircleCI как примеры; required status checks; branch protection; rulesets; test reports; coverage; lint; typecheck; security scans; contract/API compatibility checks; OpenAPI diff; schema compatibility; protobuf breaking checks; consumer-driven contract tests; snapshot/API checks; CODEOWNERS; review comments; approvals; requested changes; AI review tools and bots; merge queue; deployment gates; feature flags; canary; monitoring after merge; accepted/rejected/needs changes/superseded/stale/unknown status vocabulary.

**Мини-досье для пакета.**

1. CI/status check layer: systems, check suites, required checks.
2. Test/report layer: unit/integration/e2e/coverage/lint/type/security scan.
3. Contract/API compatibility layer: OpenAPI/schema/protobuf/consumer contracts/snapshot checks.
4. PR review mechanics: comments, approvals, requested changes, CODEOWNERS.
5. Review automation and AI review: bots, AI review tools, false positives, triage.
6. Merge queue and protected integration: branch protection/rulesets/merge queue.
7. Deployment/rollout signals: feature flags, canary, monitoring, incident/revert feedback.
8. Agent-authored PR statuses: why merged/closed/stale/superseded cannot be read naively.

**Артефакты слоя.** CI run, check suite, status check, test report, coverage report, scan result, contract diff, review comment, approval, requested changes, CODEOWNERS match, merge queue entry, deployment status, rollback/revert signal.

**Критерии выбора.** Какой риск несёт изменение; какие проверки покрывают этот риск; что должно быть required check; где нужен CODEOWNERS/human review; когда AI review помогает, а когда создаёт шум; как защищать главную ветку; когда нужна merge queue; что делать с зелёным CI, который не проверяет главный риск.

**Граница.** Не повторять ex-A3 как теорию статуса. Центральная идея `agent run не равен accepted change` остаётся skeleton, но статья должна быть технической картой gates.

## A8. Спецификации, планы и исполняемые процессные артефакты

**Назначение слоя.** Показать, как намерение становится управляемой работой до кода, вокруг кода и после кода. Этот слой связывает методологический Атлас с новыми техническими статьями: спецификация, ADR, task package, acceptance criteria и handoff становятся не prose, а рабочими артефактами процесса.

**Обязательные темы.** Spec Kit; Kiro specs; SPDD; ADR; BMAD/GSD/TDAD/Constitutional SDD-подобные режимы; issue templates; task packages; START.md; local working sheet; source manifest; acceptance criteria; definition of done; handoff docs; process artifacts as versioned, reviewable, repairable material.

**Мини-досье для пакета.**

1. Specs as process artifacts: Spec Kit, Kiro specs, SPDD.
2. Decision artifacts: ADR, status, supersession, operational projection.
3. Task packages and local execution sheets: START.md, source manifests, acceptance criteria.
4. Methodology profiles: BMAD, GSD/Open GSD, TDAD, Constitutional SDD as protected process forms.
5. Handoff and continuation artifacts: resume files, state notes, checkpoint records.
6. Executable/checkable criteria: tests, confirmation, contract, validation scripts as linked boundaries.
7. Repair loop: how process artifacts are updated after failures or accepted changes.

**Артефакты слоя.** Spec, feature spec, steering file, ADR, task package, START.md, working sheet, source manifest, acceptance criteria, confirmation note, handoff/resume note, supersession record, process profile.

**Критерии выбора.** Насколько изменение дорогое или опасное; нужно ли ревью намерения до кода; нужна ли память решения; должен ли процесс пережить одну сессию; какие критерии можно проверить автоматически; когда достаточно issue template, а когда нужен полноценный package; когда артефакт становится долгом и требует cleanup.

**Граница.** Не повторять старые статьи SPDD/ADR/Spec Kit целиком. Эта статья сравнивает классы process artifacts как технический слой.


## A9. Воспроизводимые среды исполнения и песочницы

**Назначение слоя.** Показать, где агент может безопасно и воспроизводимо выполнять работу: запускать команды, тесты, сборку, браузер, приложение, миграции и вспомогательные проверки. Для агентской разработки среда исполнения — это не фон, а техническое условие доверия к результату.

**Обязательные темы.** Dev containers; Docker / Docker Compose; Codespaces-подобные облачные среды; sandboxed execution; isolated working directories; disposable vs persistent environments; Nix/reproducible environment class where relevant; CI-like local pipelines; dependency setup; environment snapshots; secret handling inside runtime; browser/VNC/Computer Use environments; relation to A2 surfaces, A4 permissions and A7 checks.

**Мини-досье для пакета.**

1. Local runtime and shell surface: commands, dependencies, OS assumptions, local contamination.
2. Dev containers / Docker / Compose: reproducible project environment and limits.
3. Cloud dev environments and remote sandboxes: Codespaces/devbox-like class, ephemeral compute, permissions.
4. Browser/VNC/desktop runtime: when UI work requires a rendered app rather than file edits.
5. Environment snapshots and reset: how to make failed runs recoverable.
6. Secrets and network boundaries inside runtime: what must not leak into agent context.
7. CI-like local validation: what can be run before PR gates and what remains platform-only.

**Артефакты слоя.** Dev container config, Dockerfile, compose file, sandbox profile, environment snapshot, dependency lockfile, terminal session, command log, browser session, environment variable reference, local validation report.

**Критерии выбора.** Нужно ли запускать проект; насколько сложно окружение; есть ли опасные команды; можно ли изолировать зависимости; нужен ли браузер; сколько стоит disposable runtime; нужны ли секреты; можно ли воспроизвести run на другой машине или в CI.

**Граница.** Не делать учебник Docker/Nix/Codespaces. Статья объясняет слой исполнения для агента. A2 говорит о рабочей поверхности, A4 — о правах, A7 — о формальных gates.

## A10. Индексация, поиск и извлечение контекста из кодовой базы

**Назначение слоя.** Показать, как агент находит нужный код, связи, символы, зависимости, похожие места и проектные закономерности в большой кодовой базе. Это не то же самое, что явные инструкции A1: здесь контекст извлекается из самого проекта.

**Обязательные темы.** Code search; symbol search; language server / LSP class; IDE index; semantic code search; embeddings/RAG over codebase; call graph and dependency graph; code maps; repo indexing; large-repo context selection; multi-repo context; Sourcegraph/Cody-like systems; Shotgun and `shotgun_code`; limits of context blast; stale indexes; relevance errors.

**Мини-досье для пакета.**

1. Text/search baseline: grep/ripgrep, file search, exact symbol lookup.
2. IDE/LSP index: symbol graph, references, definitions, type-aware navigation.
3. Semantic retrieval and embeddings over code: when approximate search helps and where it lies.
4. Codebase maps and dependency/call graphs: structural context beyond snippets.
5. Sourcegraph/Cody-like layer: large codebase search and agent context.
6. Shotgun family: codebase-aware spec/planning and context blast variants.
7. Context selection failures: wrong files, stale indexes, overlarge payload, missing negative evidence.

**Артефакты слоя.** Search result, symbol reference list, code map, dependency graph, call graph, embedding index, retrieval packet, context bundle, selected file list, relevance note, stale-index warning.

**Критерии выбора.** Размер репозитория; язык и toolchain; есть ли LSP; нужна точная навигация или semantic recall; сколько контекста можно дать модели; как проверять полноту выбранных файлов; как избежать того, что retrieval выдаёт удобный, но неверный контекст.

**Граница.** Не смешивать с A1: инструкции говорят агенту, как работать; retrieval показывает, где в коде искать материал. Не смешивать с A12: память хранит прошлый опыт и решения; retrieval извлекает текущую структуру кодовой базы.

## A11. Issue-to-agent: задачи, очереди, assignment и progress surfaces

**Назначение слоя.** Показать, как задача становится агентской рабочей единицей: из issue/ticket/задачи в назначение агенту, план, рабочую ветку, прогресс, draft PR и обратную связь в tracker.

**Обязательные темы.** GitHub Issues; Jira/Linear-like trackers; issue templates; labels; priorities; ownership; task assignment to agent; background agent sessions; progress updates; branch/PR linking; task decomposition; queued agent work; status comments; review handoff; cancellation/retry; relation to A6/A7/A8.

**Мини-досье для пакета.**

1. Issue/ticket as agent input: description, comments, labels, acceptance criteria.
2. Assignment and ownership: who can assign an agent, what scope is implied.
3. Task decomposition and plan publication: when the agent must show plan before work.
4. Progress surfaces: comments, status updates, logs, draft PR links.
5. Tracker ↔ branch ↔ PR linkage: preserving provenance and review route.
6. Queue and background work: parallel tasks, cancellation, retries, stale work.
7. Failure modes: underspecified ticket, wrong owner, hidden dependencies, misleading progress.

**Артефакты слоя.** Issue, ticket, label, assignment event, agent plan comment, progress update, linked branch, draft PR, status comment, cancellation note, task queue entry, ownership metadata.

**Критерии выбора.** Когда достаточно prompt; когда нужна issue-first работа; кто владеет задачей; где должны жить acceptance criteria; нужен ли план до исполнения; как часто агент должен обновлять статус; как связать tracker с Git/PR и не потерять решение.

**Граница.** Не сводить к issue templates из A8 и не повторять PR mechanics из A6/A7. A11 отвечает за превращение задачи в управляемую агентскую работу.

## A12. Долгая память проекта и повторное использование опыта

**Назначение слоя.** Показать, как знания, решения, неудачные попытки, проектные привычки и выводы прошлых сессий становятся доступными будущей агентской работе. Это центрально для agentic development, но публичная статья должна быть нейтральной: не рекламировать Нoveia и не раскрывать частные стратегические выводы.

**Обязательные темы.** Session memory; project memory; episodic/semantic/procedural memory; summaries; event logs; topic documents; decision records; failed attempts; known fragile files; chat-history retrieval; MCP memory servers; graph memory; consolidation; forgetting; contradiction handling; provenance; why memory is not just a larger context window.

**Мини-досье для пакета.**

1. Context window vs memory: why long context does not equal project memory.
2. Memory forms: summary, event log, topic document, decision record, graph/link structure.
3. Coding-agent memory: past attempts, fragile files, conventions, known fixes, reviewer preferences.
4. Memory retrieval and injection: when and how memory enters a run.
5. Consolidation and forgetting: avoiding stale or wrong memory.
6. Provenance and auditability: linking memory back to source conversation, commit, issue or decision.
7. Competitive/source landscape: neutral survey, with private Noveia notes kept out of public text.

**Артефакты слоя.** Memory entry, topic document, event log, decision note, failed-attempt record, retrieval packet, provenance link, contradiction note, stale-memory warning, memory update instruction.

**Критерии выбора.** Насколько проект долгий; сколько повторяется ошибок; есть ли cross-session work; нужно ли сохранять точную provenance; кто может изменять memory; как обнаруживать устаревшие выводы; когда memory опаснее отсутствия памяти.

**Граница.** Не писать статью о Нoveia и не делать product positioning. Публичный Атлас описывает long-lived project memory as a technical layer of agentic development.

## A13. Безопасность агентской разработки и supply-chain controls

**Назначение слоя.** Показать, как агентская разработка расширяет поверхность риска: модель читает документы и issue, вызывает tools, может добавлять зависимости, генерировать небезопасный код, утекать секретами и принимать вредные инструкции. A13 собирает security слой, который не помещается полностью в A4 или A7.

**Обязательные темы.** Prompt injection in docs/issues/web pages; indirect prompt injection; MCP/tool poisoning; malicious skills/instruction packages; secret exposure; unsafe dependency additions; supply-chain attacks; generated-code vulnerabilities; SAST/SCA/CodeQL/security scans; license/security policy gates; separation of generator and validator; least privilege; audit logs; incident response for agent-caused changes.

**Мини-досье для пакета.**

1. Prompt injection surfaces in development artifacts: issues, docs, comments, web pages.
2. Tool/MCP poisoning: malicious tool descriptions, connector risks, tool-result trust.
3. Skills/instruction supply chain: operational prompts as executable influence.
4. Secrets and sensitive data: env vars, logs, screenshots, accessibility snapshots, redaction.
5. Dependency and generated-code risk: unsafe packages, vulnerable code, license conflicts.
6. Security gates and scanners: SAST, SCA, CodeQL-like scans, policy checks.
7. Separation of roles: generator, checker, reviewer, deployer, incident responder.

**Артефакты слоя.** Security warning, injection finding, redacted log, denied tool call, scan result, dependency alert, license policy result, secret reference, audit entry, incident note, security review comment.

**Критерии выбора.** Что агент читает; какие tools доступны; может ли он добавлять зависимости; где живут секреты; какие сканы обязательны; где нужен человек; как отделить генерацию от проверки; как восстановиться после unsafe change.

**Граница.** Не превращать в общую AI security. A4 раскрывает полномочия и доступы; A13 — безопасность всего agentic-development supply chain; A7 — gates принятия изменения.

## A14. Browser/GUI/app feedback surfaces

**Назначение слоя.** Показать, как агент получает обратную связь от реально работающего приложения: через браузер, GUI, screenshots, accessibility snapshots, devtools, визуальные комментарии, E2E-навигацию и Computer Use. Это закрывает разрыв между `код изменён` и `приложение действительно ведёт себя так, как нужно`.

**Обязательные темы.** Browser automation; Playwright; Playwright MCP; accessibility snapshots vs screenshots; Computer Use; Claude computer use; OpenAI computer use; in-app browser / shared rendered page; VNC/desktop sessions; devtools logs; screenshots; visual diffs; appshots; UI comments; generated E2E tests; risks of page snapshots and secrets; relation to A9 runtime and A7 acceptance gates.

**Мини-досье для пакета.**

1. Browser automation baseline: Playwright/Selenium-like class, rendered application checks.
2. Playwright MCP and accessibility snapshots: structured page context for agents.
3. Screenshot/vision-based Computer Use: when visual state matters more than DOM structure.
4. In-app browser and UI comments: shared rendered page as review and debugging surface.
5. Devtools/log feedback: console, network, browser errors, screenshots, video traces.
6. Visual regression and appshots: when screenshots become acceptance material.
7. Security and privacy risks: passwords in snapshots, screenshots, third-party pages, indirect injection.

**Артефакты слоя.** Browser session, accessibility snapshot, screenshot, UI action, devtools log, console error, network trace, visual diff, appshot, E2E test, UI comment, browser macro, reproduction step.

**Критерии выбора.** Нужно ли видеть rendered app; достаточно ли DOM/accessibility snapshot; нужна ли vision; есть ли секреты на странице; надо ли генерировать E2E; важен ли visual diff; кто проверяет UI-result; можно ли воспроизвести шаги.

**Граница.** Не растворять в A9: среда даёт место запуска, A14 даёт обратную связь от приложения. Не растворять в A7: acceptance gates могут использовать UI feedback, но не объясняют сам слой.

## A15. Model/provider layer, routing, cost and inference constraints

**Назначение слоя.** Дать рабочую карту того, как выбор модели, провайдера, gateway, routing, cost controls, context limits, latency, data controls and tool support меняет агентский процесс. Эта статья полезна прямо сейчас, но должна иметь специальный статус fast-staleness layer: её нужно обновлять чаще остальных и не превращать в рейтинг моделей.

**Обязательные темы.** Model families and capabilities as volatile inputs; reasoning vs fast/cheap models; context window and multimodal/tool support; provider APIs; OpenAI-compatible gateways; LiteLLM/Portkey/OpenRouter-like routing layer; fallback/retry; cost tracking; caching; rate limits; data retention/data residency; regional availability; BYOK/BYOC/self-hosted options; model evaluation and routing policies; separation of dev, eval and production routing.

**Мини-досье для пакета.**

1. Model capability axes: reasoning, coding, vision, tool use, context, latency.
2. Provider/API differences: tools, computer use, hosted tools, data controls, regions.
3. Gateway/routing layer: unified API, fallback, retry, model routing, policy.
4. Cost and latency controls: budgets, caching, token accounting, prompt size, batch/retry costs.
5. Context and memory pressure: context window, retrieval, compression, memory vs raw context.
6. Eval-driven model choice: local tasks, regression sets, canary model changes.
7. Staleness and update protocol: how to keep the article useful without chasing every release.

**Артефакты слоя.** Model selection note, routing config, gateway policy, cost report, latency report, rate-limit event, cache hit, provider incident note, data-control note, eval comparison, model-change decision.

**Критерии выбора.** Какая часть workflow требует сильной модели; где нужна дешёвая модель; что можно routed/fallback; где latency убивает процесс; какие данные можно отправлять провайдеру; нужен ли gateway; как считать стоимость; какие evals подтверждают смену модели; когда статья/таблица устарела.

**Граница.** Не делать evergreen рейтинг моделей. Статья объясняет model/provider layer as an engineering layer, а конкретные модели и цены должны иметь дату, источник и короткий срок актуальности.


## A16. Организационный контекст, software catalog и developer portal

**Назначение слоя.** Показать, как агентская разработка опирается не только на код, инструкции, Git и CI, но и на организационную карту инженерной системы: какие сервисы существуют, кто ими владеет, какие у них зависимости, environments, runbooks, maturity/security/compliance metadata, scorecards, self-service actions and platform workflows. Этот слой особенно важен для командной и enterprise-разработки, но полезен и как модель будущей project memory / developer platform integration.

**Обязательные темы.** Backstage-like software catalog; Port-like internal developer portal; `catalog-info.yaml` / service descriptors; components, systems, APIs, resources and ownership; service dependency maps; environments and deployment metadata; runbooks; scorecards; maturity/security/compliance metadata; developer self-service actions; event-driven workflows/automations; links from issue/task to service catalog; agent-facing organizational context; relation to A1/A10/A11/A12/A13.

**Мини-досье для пакета.**

1. Software catalog baseline: components, systems, APIs, resources, ownership and metadata.
2. Internal developer portal: catalog + actions + scorecards + self-service workflows.
3. Agent-facing organizational context: how agents use ownership, service boundaries, runbooks and environments.
4. Catalog ↔ repository ↔ issue ↔ PR links: preserving organizational provenance.
5. Scorecards and maturity gates: how catalog metadata influences acceptance and prioritization.
6. Automation/workflow layer: event-driven portal workflows and self-service actions as agent-accessible surfaces.
7. Failure modes: stale ownership, missing catalog entries, wrong service boundary, hidden dependencies, catalog as false authority.

**Артефакты слоя.** Catalog entity, service descriptor, ownership record, dependency link, system/domain map, API entity, resource entity, runbook link, scorecard, maturity metric, environment record, self-service action, workflow automation, catalog event, service health/status panel, platform policy note.

**Критерии выбора.** Достаточно ли repo-local knowledge или нужен organizational context; сколько сервисов и команд; есть ли владельцы и dependencies; может ли агент безопасно действовать без catalog metadata; нужен ли self-service portal; какие scorecards/gates должны влиять на change acceptance; как синхронизировать catalog с Git/issues/CI/deployments.

**Граница.** Не смешивать с A1: A1 описывает явные инструкции и правила проекта; A16 описывает организационную карту инженерной системы. Не смешивать с A11: A11 отвечает за задачу и очередь работы; A16 — за сервисы, ownership, dependencies and platform context. Не смешивать с A12: memory хранит прошлый опыт и решения; catalog describes current organizational topology and operational metadata.

## Синхронизация с Теорией

Эта карта является источником для `work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md`. Когда меняется состав A1–A16, нужно обновлять attachment map, чтобы будущие главы Теории знали, какие слои Атласа их заземляют.

Правило: Атлас раскрывает слой технически; Теория берёт из слоя только тот срез, который нужен для жизненного цикла изменения. Если chapter package начинает пересказывать статью Атласа, это ошибка. Если chapter package вообще не привязывает теоретический тезис к техническим слоям, это тоже ошибка.
