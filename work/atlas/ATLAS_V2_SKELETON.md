# Скелетон Атласа V2

Статус: рабочий скелет Атласа V2.  
Дата: 2026-06-17.  
Основание: ADR-0012–ADR-0019, карта статей `ATLAS_V2_LAYER_ARTICLE_MAP.md`, заметки о старых статьях Атласа и внешний срез по AgenticOps / Harness Engineering.

## 0. Зачем нужен этот документ

Этот документ задаёт композицию Атласа. Он нужен не для сборки конкретного пакета, а для удержания формы всей части: какие статьи считаются основными, какие — дополнительными профилями, где проходят границы между Атласом, Теорией, Рабочими сценариями и Каталогом проблем.

Рядом с ним есть более операционный документ:

```text
work/atlas/ATLAS_V2_SKELETON.md
→ композиция Атласа: уровни статей, роли, границы, порядок и проверки качества.

work/atlas/plans/ATLAS_V2_LAYER_ARTICLE_MAP.md
→ рабочая карта для планы целевых групп и пакетов: что собирать по каждой статье, какие артефакты искать, где ставить проверки.
```

Атлас — самостоятельная крупная часть корпуса, а не приложение к Теории. Теория смотрит на ту же область через жизненный цикл изменения. Атлас смотрит через технические слои: какие слои существуют, какие инструменты и форматы их строят, как их выбирать и где они ломаются.

## 1. Главная задача Атласа

Агентская разработка — это не один инструмент и не одна способность модели. На практике она складывается из многих технических слоёв вокруг программного изменения: проектный контекст, рабочая поверхность, оркестрация, инструменты и права, среда выполнения, поиск по кодовой базе, Git/PR-контур, проверки, ревью, память, безопасность, обратная связь от приложения, маршрутизация моделей, организационный каталог, диагностика, тесты и контур эксплуатации.

Атлас должен помочь читателю увидеть это пространство как карту. После хорошей статьи Атласа читатель должен понимать:

```text
какой технический слой перед ним;
какие классы решений в этом слое конкурируют;
какие конкретные технологии, протоколы, форматы и рабочие поверхности там используются;
какие артефакты слой создаёт или меняет;
по каким признакам выбирать подход;
какие сбои характерны для слоя;
как этот слой связан с соседними слоями.
```

Атлас не должен превращаться в Теорию, рейтинг продуктов, список ссылок, Рабочие сценарии или Каталог проблем. В нём может быть сильная концептуальная рамка, но она служит технической карте, а не заменяет её.

## 2. Уровни статей

### Уровень 1 — статьи о технических слоях

A1–A19 образуют основной хребет Атласа. Каждая такая статья описывает один технический слой агентской разработки.

### Уровень 2 — профили продуктов, методов и платформенных сборок

Эти статьи не второстепенны по качеству. У них другая роль: они показывают, как один продукт, метод или платформенный подход собирает несколько слоёв сразу.

К этому уровню относятся Kiro / Kiro Specs, Spec Kit, SPDD, Persistent Work Graph, ADR/MADR, TDAD, Constitutional SDD, BMAD / GSD / Open GSD, Gas Town / Beads, AgenticOps и другие плотные профили. Такая статья должна прямо назвать, какие статьи A-слоя она пересекает, и не должна притворяться заменой этим статьям.

### Уровень 3 — узлы источников и профилей

Это более короткие узлы: источник, инструмент, частный кейс, старая статья или материал, который сохраняет важную фактуру. Они могут питать статьи уровня 1 и 2 и оставаться видимыми из Атласа.

## 3. Общая рамка статьи уровня 1

Каждая крупная статья Атласа должна проходить одну и ту же проверку:

```text
какую задачу решает слой;
какие классы решений существуют;
какие реальные технологии, форматы, протоколы и рабочие поверхности здесь важны;
какие артефакты они создают или меняют;
как слой работает технически;
как отличаются конкурирующие подходы;
как выбирать между ними;
где слой обычно ломается;
что относится к соседним слоям;
что нужно оставить Теории, Рабочим сценариям или Каталогу проблем.
```

Если статья хорошо объясняет идею, но не показывает технический слой, это не статья Атласа. Именно так была диагностирована ex-A3: текст оказался сильным теоретическим фрагментом, но не прошёл как статья Атласа.

## 4. Главные статьи уровня A

### A1. Контекстный интерфейс проекта для агента

**Что показывает статья.** Показать, где в проекте живут явные правила, процедуры и рабочие знания, по которым агент должен действовать. Агент не должен каждый раз начинать из пустого чата: у него должна быть поддерживаемая проектная среда, из которой он узнаёт стиль, ограничения, источники правды, точки остановки и способы восстановления после ошибки.

**Что обязательно раскрыть.** AGENTS.md, CLAUDE.md, Cursor Rules, GitHub Copilot custom instructions, Codex/Amp instructions, Kiro steering, skills, hooks, subagents, project docs, specs, ADR, локальные task packages, манифесты источников, acceptance criteria, заметки о ремонте.

**Какие артефакты показать.** инструкционные файлы, вложенные правила, steering-документы, skill-файлы, hook-конфигурации, профили subagents, рабочие пакеты, манифесты источников, критерии принятия, заметки о ремонте правил.

**Как выбирать.** одноразовая задача или повторяемый процесс; один инструмент или несколько агентов; важность наследования правил; что держать в инструкции, а что вынести в документы; где будет фиксироваться урок после сбоя.

**Граница.** A1 говорит о явных проектных правилах. Поиск по кодовой базе относится к A10, память прошлых сессий — к A12, организационная карта сервисов — к A16.

### A2. Рабочие поверхности coding agents

**Что показывает статья.** Сравнить места, где агент реально действует над кодом и проектом: чат, IDE, CLI, облачная задача, PR-контур, локальная песочница, worktree или open-source agent environment. Это выбор видимости, прав, воспроизводимости, удобства ревью и цены контроля.

**Что обязательно раскрыть.** chat-based coding, IDE agents, CLI agents, cloud coding agents, PR/issue-to-PR agents, Aider, OpenHands, SWE-agent-подобные среды, sandbox/worktree/devbox режимы.

**Какие артефакты показать.** переписка, локальный diff, patch, terminal log, worktree, sandbox snapshot, cloud branch, agent-created PR, command output, отчёт о прогоне.

**Как выбирать.** нужен ли полный репозиторий; можно ли запускать проверки; когда человек увидит diff; как ограничить радиус ущерба; можно ли воспроизвести прогон; насколько удобно довести результат до review.

**Граница.** A2 описывает рабочую поверхность. Оркестрация процесса — A3, воспроизводимая среда выполнения — A9, browser/обратная связь от UI — A14.

### A3. Оркестрация и фреймворки агентского исполнения

**Что показывает статья.** Показать, как агентская работа становится управляемым процессом, когда одного агента в одной поверхности уже недостаточно. Здесь важны графы, состояние, роли, маршрутизация, повторные попытки, остановки, человеческие остановки и возобновление работы.

**Что обязательно раскрыть.** ReAct/tool-use loop как фон, LangGraph, OpenAI Agents SDK, Google ADK, AutoGen, CrewAI, LlamaIndex Workflows, самописные runners, state machines, multi-agent orchestration, resumable workflows.

**Какие артефакты показать.** workflow graph, node/edge, state object, решение о маршруте, tool call, handoff, checkpoint, interrupt, retry record, agent role, маркер возобновления, trace link.

**Как выбирать.** нужно ли persistent state; есть ли ветвление; нужны ли роли; сколько человеческие остановки; важна ли replay/observability; не проще ли явный runner вместо универсального framework.

**Граница.** Не писать историю ReAct и не делать рейтинг фреймворков. Статья сравнивает orchestration patterns и причины, по которым слой становится нужен.

### A4. Инструменты, протоколы, доступы и полномочия

**Что показывает статья.** Развести техническую возможность вызвать инструмент, доступ к данным, полномочие действовать и право считать действие допустимым. Для агента важно не только “может ли он вызвать API”, но и от чьего имени, с какими правами и с каким следом.

**Что обязательно раскрыть.** tool/function calling, MCP, A2A, connectors, sandbox permissions, approvals, scoped access, secret handling, audit logs, prompt injection surfaces, tool poisoning, команды с ограничением по роли, дизайн CLI/API, удобный для агента, SKILL.md-подобные инструкции, discovery команд.

**Какие артефакты показать.** tool schema, MCP server/tool/resource, connector config, approval prompt, deny/allow decision, scoped credential, audit event, CLI command spec, skill/tool guide, discovery output.

**Как выбирать.** опасность действия; какие данные видит агент; можно ли действие отменить; нужен ли подтверждение человека; как отозвать доступ; что логировать; как ограничить prompt injection через tools.

**Граница.** A4 — про полномочия и интерфейсы действия. A13 раскрывает безопасность и риски supply chain шире, A9 — среду выполнения, A16 — организационные действия через platform/catalog.

### A5. Наблюдаемость, traces и evals

**Что показывает статья.** Показать, как агентскую работу можно увидеть, воспроизвести, отладить, измерить и сравнить между версиями модели, промпта, toolchain или orchestration setup.

**Что обязательно раскрыть.** traces, spans, tool-call logs, replay/debug surfaces, LangSmith/Langfuse/Phoenix-подобные системы, eval harnesses, SWE-bench-like benchmarks, golden tasks, regression evals, automated graders, сравнение прогонов.

**Какие артефакты показать.** trace, span, run id, tool-call record, представление для повтора, eval dataset, golden task, grader output, benchmark score, regression report, след стоимости и задержки, comparison report.

**Как выбирать.** нужен debug или production monitoring; есть ли повторяемый workflow; что считать успехом; кто читает trace; нужно ли сравнивать версии; какие ошибки eval всё равно не увидит.

**Граница.** A5 измеряет agent runs и agent systems. CI/контуры ревью — A7, программные диагностика во время работы — A17, тестовые артефакты — A18.

### A6. Git, worktree и PR/MR как субстрат агентского изменения

**Что показывает статья.** Показать, как результат агента становится изолируемым, сравнимым, ревьюируемым, сливаемым и откатываемым change candidate. Git здесь не фон, а несущая поверхность агентского изменения.

**Что обязательно раскрыть.** branch, worktree, index, commit, history, diff, patch, merge, squash, rebase, cherry-pick, conflicts, PR/MR, linked issue, review state, audit trail, revert, rollback, bisect, multi-agent branches/worktrees, Git-compatible варианты вроде Jujutsu/Sapling.

**Какие артефакты показать.** branch, worktree, commit, diff, patch, PR/MR, linked issue, review state, merge commit, revert commit, conflict markers, bisect result, provenance trail.

**Как выбирать.** branch per task или общий поток; нужен ли отдельный worktree; как часто делать commit checkpoints; когда branch превращать в PR; как сохранять readable history; как переживать semantic conflicts.

**Граница.** A6 оформляет candidate. A7 применяет gates. A19 отвечает за release и runtime последствия.

### A7. CI, status checks, review и контуры принятия

**Что показывает статья.** Показать, как оформленный change candidate проходит технические и человеческие проверки перед принятием, отклонением или возвратом на доработку.

**Что обязательно раскрыть.** CI, required status checks, protected branches, rulesets, merge queue, test reports, coverage, lint/typecheck/security scans, CODEOWNERS, review comments, approvals, requested changes, AI review tools, contract/API compatibility checks, deployment gates as handoff to A19.

**Какие артефакты показать.** CI run, check suite, test report, coverage report, review comment, approval, requested-changes state, merge-queue item, compatibility report, acceptance/rejection decision.

**Как выбирать.** какие проверки обязательны; кто имеет право approve; какие checks блокируют merge; где нужен AI review; как читать зелёный CI без ложного спокойствия; что должно уйти в A19 после merge.

**Граница.** Не повторять ex-A3 как философию принятия. A7 — техническая инфраструктура gates; теоретический вопрос статуса материала остаётся в Теории.

### A8. Спецификации, планы и исполняемые процессные артефакты

**Что показывает статья.** Показать, как намерение становится управляемой работой до кода и вокруг кода: через specs, планы, decision records, acceptance criteria, handoff-документы и process profiles.

**Что обязательно раскрыть.** Spec Kit, Kiro specs, ADR, SPDD, BMAD/GSD/TDAD-like methods, Constitutional SDD, issue templates, task packages, acceptance criteria, executable specs, handoff docs.

**Какие артефакты показать.** spec, ADR, plan, task package, acceptance criteria, handoff, decision record, process profile, package manifest, stop/checkpoint note.

**Как выбирать.** что нужно контролировать: intent, scope, sequence, acceptance, state, recovery; нужен ли doc-first режим; насколько формальным должен быть plan; кто читает handoff.

**Граница.** Не делать каталог методологий. Статья сравнивает, какие стороны работы разные артефакты делают явными для агента и человека.

### A9. Воспроизводимые среды исполнения и песочницы

**Что показывает статья.** Показать, где агент безопасно запускает команды, тесты, сборку, миграции и приложение, чтобы результат был воспроизводимым и ограниченным по риску.

**Что обязательно раскрыть.** Docker/Compose, dev containers, Codespaces-like environments, ephemeral sandboxes, remote devboxes, Nix/reproducible environments where useful, CI-like runners, browser/VNC environments, dependency setup, secret boundaries, snapshots.

**Какие артефакты показать.** devcontainer config, Dockerfile/Compose file, sandbox session, environment snapshot, dependency cache, setup log, isolated filesystem, allowed-command policy.

**Как выбирать.** локально или удалённо; постоянная или одноразовая среда; какие команды разрешены; как изолировать secrets; нужно ли запускать приложение целиком; как воспроизвести сбой.

**Граница.** A9 — место выполнения. A14 — feedback от работающего приложения, A17 — программные диагностика, A7 — formal gates.

### A10. Индексация, поиск и извлечение контекста из кодовой базы

**Что показывает статья.** Показать, как агент находит нужный код, символы, зависимости, call paths и проектные закономерности в большой кодовой базе.

**Что обязательно раскрыть.** grep/ripgrep, IDE/LSP indexes, symbol search, semantic search/embeddings, RAG over code, dependency/call graphs, code maps, Sourcegraph/Cody-like systems, multi-repo context, Shotgun / shotgun_code, context blast, stale index and retrieval errors.

**Какие артефакты показать.** selected file list, search results, symbol references, code map, call graph, dependency graph, retrieval packet, context bundle, relevance note, предупреждение об устаревшем индексе.

**Как выбирать.** точный поиск или semantic retrieval; один repo или multi-repo; нужен ли graph/call context; как проверять полноту retrieval; как не смешать похожие участки; когда делать context blast.

**Граница.** A10 извлекает текущую структуру проекта. A1 даёт явные правила, A12 хранит прошлый опыт и решения.

### A11. Issue-to-agent: задачи, очереди, assignment и progress surfaces

**Что показывает статья.** Показать, как issue/ticket становится агентской рабочей единицей с владельцем, scope, планом, прогрессом, branch/PR связью и handoff.

**Что обязательно раскрыть.** GitHub Issues, Jira/Linear-like trackers, labels, ownership, issue templates, task assignment to agent, background sessions, progress updates, plan comments, queueing, cancellation, retry, branch/PR linking.

**Какие артефакты показать.** issue/ticket, assignment event, plan comment, progress update, queue entry, linked branch, draft PR, status comment, cancellation note.

**Как выбирать.** какие задачи можно отдавать агенту; как задавать scope; нужен ли queue; когда cancel/retry; как сообщать progress; кто принимает результат.

**Граница.** A11 — work-management layer. Issue templates как process artifacts связаны с A8, branch/PR mechanics — с A6.

### A12. Долгая память проекта и повторное использование опыта

**Что показывает статья.** Показать, как опыт прошлых сессий, решений, неудачных попыток, хрупких файлов и проектных привычек становится доступным будущей агентской работе.

**Что обязательно раскрыть.** session memory, project memory, episodic/semantic/procedural memory, summaries, event logs, topic documents, decision records, failed attempts, known fragile files, chat-history retrieval, MCP memory servers, graph memory, consolidation, forgetting, contradiction handling, provenance.

**Какие артефакты показать.** memory entry, topic document, event log, decision note, failed-attempt record, retrieval packet, provenance link, contradiction note, предупреждение об устаревшей памяти.

**Как выбирать.** что запоминать; как проверять источник памяти; когда забывать; как разрешать противоречия; как отделять проектную память от текущего контекста; как не превратить память в шум.

**Граница.** Публичная статья нейтральна: не превращать A12 в позиционирование Noveia. A1 — явные правила, A10 — поиск по текущему коду, A16 — организационная карта.

### A13. Безопасность агентской разработки и контроли supply chain

**Что показывает статья.** Показать, как агентская разработка расширяет поверхность риска и какие технические меры уменьшают ущерб.

**Что обязательно раскрыть.** prompt injection in docs/issues/web pages, indirect injection, MCP/tool poisoning, malicious skills/instruction packages, secrets, unsafe dependencies, уязвимости сгенерированного кода, SAST/SCA/CodeQL-like scans, license/security policy gates, least privilege, generator/checker separation, audit logs, incident response.

**Какие артефакты показать.** injection finding, denied tool call, redacted log, scan result, dependency alert, license policy result, security review comment, audit event, incident note.

**Как выбирать.** где может войти вредная инструкция; какие tools опасны; как хранить secrets; кто проверяет зависимости; что должен видеть audit log; где нужен независимый checker.

**Граница.** A4 описывает доступы и полномочия. A13 — безопасность всего агентского контура и риски supply chain.

### A14. Browser/GUI/обратная связь от приложения surfaces

**Что показывает статья.** Показать, как агент видит и проверяет работающее приложение через браузер, GUI, screenshots, accessibility snapshots, devtools logs и обратная связь от приложения.

**Что обязательно раскрыть.** Playwright/browser automation, Playwright MCP, accessibility snapshots, screenshots, Computer Use, desktop/VNC sessions, devtools logs, network/console traces, visual diffs, appshots, UI comments, generated E2E steps, privacy/secrets risks.

**Какие артефакты показать.** browser session, accessibility snapshot, screenshot, UI action, devtools log, console error, network trace, visual diff, appshot, E2E step, UI comment.

**Как выбирать.** нужен ли browser automation; достаточно ли accessibility snapshot или нужен screenshot; как хранить приватные UI traces; когда превращать feedback в E2E test; где нужен человек.

**Граница.** A14 — feedback от работающего приложения. A9 — среда запуска, A18 — тестовые артефакты и их сопровождение.

### A15. Слой моделей, провайдеров, маршрутизации, стоимости и ограничений инференса

**Что показывает статья.** Показать, как выбор модели, провайдера, gateway и маршрутизации, стоимости и задержек меняет весь агентский процесс.

**Что обязательно раскрыть.** model capability axes, provider APIs, tool support, context windows, multimodal support, OpenAI-compatible gateways, LiteLLM/Portkey/OpenRouter-like маршрутизация, retry/fallback, caching, rate limits, cost accounting, latency, data retention/residency, BYOK/BYOC/self-hosted options, model/process fit, local evals, проверки в реальной работе.

**Какие артефакты показать.** model-selection note, маршрутизация config, gateway policy, cost report, latency report, eval comparison, model-change decision, fallback log.

**Как выбирать.** какая модель подходит к процессу; как считать стоимость; где нужен fallback; как разделять dev/eval/production-маршрутизацию; когда benchmark ничего не решает; как часто пересматривать выбор.

**Граница.** Это быстро устаревающая рабочая карта, а не вечнозелёный рейтинг моделей.

### A16. Организационный контекст, software catalog и developer portal

**Что показывает статья.** Показать, как агент узнаёт инженерную топологию организации: сервисы, владельцев, зависимости, environments, runbooks, scorecards, portal actions и operational metadata.

**Что обязательно раскрыть.** Backstage/Port-like catalogs, catalog-info.yaml and service descriptors, ownership, components/systems/APIs/resources, dependency maps, environments, runbooks, scorecards, maturity/security/compliance metadata, self-service actions, workflow automations, машиночитаемый дескрипторы приложений и сервисов, topology, resource bindings, log/trace locations, deployment units and операционные возможности.

**Какие артефакты показать.** catalog entity, service descriptor, ownership record, dependency link, system/domain map, API entity, runbook link, scorecard, environment record, self-service action, platform workflow.

**Как выбирать.** нужен ли software catalog; какие metadata обязательны для агента; как связывать сервис с logs/deploy/runbook; какие actions безопасно отдавать через portal; где проходит ownership.

**Граница.** A16 — текущая организационная и платформенная карта. A12 — память, A11 — управление задачами, A1 — проектные инструкции.

### A17. Структурированная обратная связь от программы

**Что показывает статья.** Показать, как агент получает и использует структурированные сигналы от кода, toolchain и runtime во время работы.

**Что обязательно раскрыть.** compiler errors, typechecker диагностика, language server диагностика, lints, static analysis warnings, debugger sessions, breakpoints, variable inspection, stack traces, runtime logs, profiler output, local reконтур эксплуатацииs, repair loops driven by these signals.

**Какие артефакты показать.** compiler diagnostic, type error, LSP diagnostic, lint/static-analysis warning, stack trace, debugger transcript, breakpoint state, profiler output, runtime log, reproduction note, fix verification output.

**Как выбирать.** какие диагностика доступны локально; можно ли agent-driven debug; когда достаточно static analysis; как связать log/stack trace с правкой; как проверить исчезновение warning.

**Граница.** A17 — feedback от программы и toolchain. A5 — observability/evals агента, A7 — контуры принятия, A18 — tests, A14 — обратная связь от UI.

### A18. Автономное тестирование и QA-артефакты

**Что показывает статья.** Показать, как агенты создают, чинят, запускают, оценивают и сопровождают тесты и QA artifacts.

**Что обязательно раскрыть.** unit/integration/E2E test generation, bug reproduction, regression tests, test repair, flaky-test handling, coverage-guided work, mutation testing, UI test generation, property/fuzz tests where relevant, test-data generation, test review, governance of AI-generated tests, limits of tests written by the same agent that wrote the code.

**Какие артефакты показать.** generated test, reproduction test, regression test, test diff, coverage report, mutation score, flaky-test note, test-review comment, QA checklist, generated fixture, bug reproduction script.

**Как выбирать.** когда агенту можно писать тест; как проверять тест, написанный тем же агентом; как бороться с flaky tests; когда нужен mutation/coverage signal; как тест становится regression guard.

**Граница.** A18 создаёт и сопровождает test/QA artifacts. A7 использует результаты tests как gates, A17 даёт диагностика, A14 может дать UI/E2E steps.

### A19. Выпуск, развёртывание, наблюдение в эксплуатации и агенты восстановления

**Что показывает статья.** Показать слой после merge: release, deployment, runtime observation, rollback, incident response, remediation PRs и возвращение уроков в документы, rules, tests и memory.

**Что обязательно раскрыть.** release pipelines, deployment approvals, feature flags, canaries, progressive delivery, environment promotion, production monitoring, alerts, Sentry/Datadog/Grafana/PagerDuty-like signals, runbook automation, rollback/revert decisions, incident triage, remediation PRs, postmortems, learning back into docs/rules/tests/memory.

**Какие артефакты показать.** release plan, deployment run, environment promotion, feature flag, canary result, alert, incident ticket, runbook action, rollback, remediation PR, postmortem, production metric, monitoring dashboard note.

**Как выбирать.** кто выпускает изменение; где нужны approvals; когда откатывать; что может чинить agent-monitor; когда заводить incident; как урок возвращается в проектную обвязку.

**Граница.** A7 принимает engineering candidate. A19 проверяет, выживает ли изменение в эксплуатации, и замыкает runtime петля обратной связи.

## 5. Дополнительные статьи Атласа

A1–A19 — это хребет технических слоёв, но не весь Атлас.

**Kiro / Kiro Specs** стоит вести как профиль продукта и метода: specs, steering, hooks, IDE work surface и MCP/tooling в одной связке. Связи: A1, A2, A4, A8, A11, A14.

**AgenticOps / platform engineering, рассчитанный на работу агентов** — профиль платформенной сборки, а не A20. Он полезен именно тем, что соединяет несколько слоёв: CLI/API, удобные для агента, обнаруживаемый команды с ограничением по роли, IaC/CaC, self-hosted infrastructure, deployment, monitoring, model gateway, observability, software catalog и петли инцидентов и восстановления. Связи: A4, A6, A7, A9, A15, A16, A19.

**SPDD** — методологический профиль specification-driven work. Связи: A8, A1, A6, A7, A18.

**Persistent Work Graph** — профиль долгого состояния работы, связей, recovery, memory и context carryover. Связи: A8, A12, A1, A6, A5.

**ADR/MADR** — профиль decision records: происхождение решений, review, связь с кодом и повторное использование. Связи: A8, A1, A6, A7, A12.

**Spec Kit / TDAD / Constitutional SDD / BMAD / GSD** — профили способов сделать намерение, ограничения, план, проверки и состояние процесса явными для агента. Связи: A1, A3, A8, A11, A18.

**Gas Town / Beads** — плотный организационно-операционный кейс: роли, очереди, backpressure, continuation, локальные истории и границы ответственности. Связи: A3, A8, A11, A12, A16, A19.

## 6. Связь с другими частями корпуса

`Тёмная материя софта` относится прежде всего к Cross-story synthesis. Это не технический слой, а паттерн: AI делает рентабельными внутренние утилиты, личные инструменты, одноразовые автоматизации, отчёты и workflow scripts, которые могут массово появляться, но не становиться публичными продуктами.

Теория использует материалы Атласа как техническое заземление, но не должна превращаться в мини-Атлас. Рабочие сценарии берут из Атласа критерии выбора. Каталог проблем и решений берёт типовые сбои слоёв и превращает их в диагностические сценарии.

## 7. Проверки для пакетов Атласа

Каждый пакет Атласа должен заранее назвать:

```text
уровень статьи: слой / профиль / source node;
какой технический слой или сборка описывается;
какое техническое наполнение нужно;
какие карточки источников и фактов должны быть собраны;
какая технологическая матрица нужна;
какие артефакты должен увидеть читатель;
какие критерии выбора обязательны;
где граница с Теорией, Рабочими сценариями и Каталогом проблем;
где человек должен проверить жанр до финального синтеза.
```

Для статей уровня 1 длинные мини-досье в виде самостоятельных эссе больше не считаются хорошей формой по умолчанию. Предпочтительны карточки источников и фактов, technology matrices, artifact-level extraction и section-slice drafts, где seed сразу превращается в будущий фрагмент статьи.

## 8. Синхронизация

Если меняется этот Скелетон, нужно сверить и при необходимости обновить:

```text
work/atlas/plans/ATLAS_V2_LAYER_ARTICLE_MAP.md
work/theory-writing/reports/ATLAS_V2_STRUCTURE_AND_ARTICLE_STATUS.md
work/theory-writing/reports/THEORY_CHAPTER_ATTACHMENT_MAP.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/APPLY_NOTES.md
```

Скелетон Атласа отвечает за композицию части. Карта статей отвечает за сборку пакетов. Карта приложений к Теории отвечает за то, как материалы Атласа заземляют главы Теории.
