# Quix / Klaus Kode

## Черновое назначение

Документ создан режимом fresh для накопления материала из первоисточников. Это досье для будущей истории, а не методологическая глава: здесь важны конкретные артефакты, ограничения, рабочие повороты, странные детали и несколько конкурирующих рамок.

Текущие проходы: `01`, `02`, `03`, `04`, `05`, `06`, `run_id=story-dossiers-source-accumulation-2026-06-09-0855`.

## Рабочая карта

Тема пока не должна сжиматься до одной формулы. По первому набору источников видны как минимум четыре возможные истории.

1. **Workflow engine вокруг Claude Code.** Автор Quix описывает, что Claude Code хорошо решал локальные задачи, но плохо держал многошаговый процесс с картой файлов, pull request, отладкой и интеграционными тестами. Ответом стал не ещё один prompt, а отдельный управляющий слой: OpenAI Agents SDK координирует шаги, вызывает Claude Code SDK для конкретных задач и ведёт состояние между ними ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it), [README](https://github.com/quixio/klaus-kode-agentic-integrator)).
2. **Onramp для новых инженеров в сложной R&D-среде.** Практическая цель не была абстрактной автоматизацией coding tasks. Quix хотел, чтобы новый инженер мог взять типовую интеграцию API и быстрее пройти путь от понимания API до pull request в монорепозиторий `quix-streams`, где нужны source-коннекторы, sink-коннекторы, docs, templates и UI-совместимые metadata ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it), [docs.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs.md)).
3. **История о границах prompt-only управления.** Первые попытки были через подробный prompt и MCP-документацию. По словам автора, агент терял поток на длинных задачах, делал документы в wrong order, забывал тесты, переключался на unrelated refactors и в конечном счёте требовал от человека ручной проверки каждого шага ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).
4. **Узкий эксперимент, который сам нуждается в проверке.** Репозиторий выглядит как рабочий прототип с `docs.md`, `instructions.md`, `example_workflow.md`, `custom_workflow_example.py`, `main.py`, небольшим test/fixture набором и без релизов на GitHub на момент просмотра. Это не доказательство зрелого продукта, а материал о том, как команда упаковывала повторяемую агентскую процедуру в исполняемый scaffold ([GitHub repo](https://github.com/quixio/klaus-kode-agentic-integrator)).
5. **Wizard и Quix Cloud как вторая поверхность истории.** Во втором проходе обнаружилась публичная страница Quix Integration, где Klaus Kode описан уже не только как репозиторий workflow engine, а как путь из браузерного мастера: пользователь вводит API-документацию и Personal Access Token, после чего процесс уходит в sandbox Quix Cloud, создаёт fork/branch/PR и делает auto-debug cycles ([Quix Integration page](https://quix.io/integrations/klaus-kode)). Это меняет ранний угол: история может быть не только про локальный Python orchestrator вокруг Claude Code, но и про попытку превратить его в управляемый self-service onramp.
6. **Текущая публичная поверхность стала более терминальной и менее GitHub-PR-центричной.** В третьем проходе та же страница `quix.io/integrations/klaus-kode` уже описывает Klaus Kode как терминальный мастер workflow, который использует Quix Cloud sandbox и Quix Cloud PAT, а не подтверждает прежнюю формулировку про браузерный wizard, GitHub PAT, fork/branch/PR. README репозитория тоже показывает запуск через `start.sh`/`start.bat`/`start.ps1`, `.env` с `ANTHROPIC_API_KEY`, `QUIX_TOKEN`, `QUIX_BASE_URL` и меню из Source/Sink/Transform/Debug, где Transform и Debug помечены как coming soon ([Quix Integration page](https://quix.io/integrations/klaus-kode), [README](https://github.com/quixio/klaus-kode-agentic-integrator)).
7. **MCP и prompt files как конкретная цена контекста.** В четвёртом проходе блог стал полезнее как источник сцены, а не только общей позиции: автор показывает вывод `/context` в Claude Code и пишет, что MCP tool descriptions занимали 34% контекста ещё до начала работы. Это даёт проверяемую фактуру для поворота от "дать агенту больше tools/docs" к "оставить агенту узкую coding task, а API-вызовы делать детерминированным кодом" ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).
8. **Кодовая версия истории стала менее похожа на PR-generator и больше похожа на runtime wizard.** В пятом проходе через GitHub API раскрыты `workflow_tools/workflow_factory.py`, `workflow_tools/contexts.py`, `workflow_tools/services/claude_code_service.py`, `workflow_tools/services/debug_analyzer.py`, prompt-файлы и `config/models.yaml`. Текущая реализация явно собирает Source/Sink/Diagnose из фаз, хранит состояние в dataclass-контексте, запускает Claude Code из основного каталога с указанием `app_path`, гоняет код в Quix IDE/sandbox и обрабатывает debug-циклы до десяти попыток. Это укрепляет линию "детерминированный коридор вокруг агента", но ослабляет старую линию про реальные PR в `quix-streams` ([workflow_factory.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/workflow_factory.py), [contexts.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/contexts.py), [ClaudeCodeService](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/services/claude_code_service.py), [DebugAnalyzer](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/services/debug_analyzer.py)).
9. **Платформа догоняет тот же класс проблемы.** На 28 мая 2026 Anthropic уже описывает dynamic workflows in Claude Code как встроенную способность разбивать большую задачу на subagents, хранить progress outside the conversation, подтверждать запуск и предупреждать о существенно большем token usage. Это не источник про Quix, но полезный фон: Klaus Kode можно читать как ранний доменный harness вокруг Claude Code для фиксированного integration workflow, а не как изолированную причуду одной команды ([Anthropic dynamic workflows announcement](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)).

Что мешает раннему framing: пока почти все сильные факты идут из собственного поста Quix, собственного репозитория и собственной интеграционной страницы. Нужны внешние реакции, реальные PR в `quix-streams`, проверка issues/commits, а также понимание, использовался ли Klaus Kode после публикации или остался демонстрацией. Текущая страница `quix.io/integrations/klaus-kode` усиливает гипотезу о productized experiment, но одновременно заставляет поправить второй проход: проверенная на третьем проходе версия страницы говорит о терминальном wizard и Quix Cloud PAT, а не о GitHub PAT и создании fork/branch/PR.

## Контекст Quix и задачи интеграций

Quix позиционирует себя вокруг Python stream processing и Apache Kafka. В публичной документации `quixstreams` описан как open source Python stream processing framework, а tutorials показывают работу с `Application`, topics, `StreamingDataFrame` и локальным Kafka через `docker compose` ([Quix Streams docs](https://quix.io/docs/quix-streams/introduction.html), [tutorial](https://quix.io/docs/quix-streams/tutorials/hello-world.html)). Для истории это важно как фон: интеграции здесь не выглядят как одноразовые скрипты. Коннектор должен совпасть с библиотекой, документацией, templates и пользовательским интерфейсом Quix.

В статье задача формулируется через "connector integrations" к API третьих сторон: source-connector должен получать данные из внешнего API в Quix Streams, sink-connector должен отправлять обработанные данные из Quix Streams обратно во внешний API. Автор отдельно говорит о повторяемой структуре такой работы: читать API-документацию, писать код, генерировать metadata, templates, документацию, запускать тесты и открывать pull request ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).

В `docs.md` репозитория эта предметная рамка разложена уже не как блоговая история, а как инженерная схема: интеграция имеет четыре компонента - source, sink, metadata и template. Source-connector должен читать из внешнего API и публиковать в Quix Streams; sink-connector должен читать из Quix Streams и писать во внешний API; metadata задаёт параметры интеграции; template описывает готовый pipeline пример ([docs.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs.md)).

Публичная страница интеграции добавляет к этому облачный контекст, но в третьем проходе она выглядит иначе, чем было записано после второго прохода. Текущая версия описывает Klaus Kode как Python-based Agentic Data Integrator, который запускается в терминале как мастер workflow, генерирует и тестирует connector code, анализирует логи, управляет dependencies/env vars и использует Quix Cloud как sandbox для isolated containers и хранения данных ([Quix Integration page](https://quix.io/integrations/klaus-kode)). На этой же странице предпосылки сформулированы через Git, Python, Claude Code CLI, Anthropic API token и Quix Cloud PAT; GitHub PAT, fork/branch/PR в текущем прочтении страницы не подтверждены ([Quix Integration page](https://quix.io/integrations/klaus-kode)).

В текущем README при запуске показываются четыре пункта: `Source Workflow`, `Sink Workflow`, `Transform Workflow *Coming soon`, `Debug Workflow *Coming soon` ([README](https://github.com/quixio/klaus-kode-agentic-integrator)). При этом `docs/example_workflow.md` в конце всё ещё упоминает `Diagnose and Update` как режим, который позволяет итеративно править уже созданное приложение в Quix Cloud, а `main.py` содержит `run_diagnose_workflow` и маршрутизацию `WorkflowType.DIAGNOSE` ([End-to-end Tutorial](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs/example_workflow.md), [main.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py)). Это стало более точным расхождением: публичное меню и README называют Debug будущим пунктом, но код и tutorial уже содержат diagnose/update след.

## Ход событий и рабочие эпизоды

Раздел переписан как последовательность технических попыток: сначала Claude Code получает всё как prompt/documentation/tool-surface, затем становится видно, где именно ломается контроль, и только после этого появляется Klaus Kode как workflow engine вокруг агента.

### Эпизод 1. Исходная задача: data connectors are not just code files

Quix хотел ускорить создание Python applications for data pipelines in Quix Cloud. Снаружи задача может звучать просто: “прочитай документацию SendGrid или другого источника и напиши connector”. Но фактический lifecycle шире: нужно определить Source/Sink/Transform route, собрать environment variables, update dependency definitions, create Python application, upload code, variables and dependencies into a cloud sandbox, install dependencies, run the app, download logs, check whether it does what it should, then deploy as a containerized app. Для high-fidelity data sources это не cron-job and not a static webhook script: Quix говорит о telemetry streams, blockchain feeds, large static datasets and distributed processing on a platform that hides Kafka/Kubernetes complexity behind APIs ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).

Первые attempts gave Claude Code requirements prompt, documentation and repo access. Claude could write Python. The failure was in the sequence: it would skip steps, call the wrong tool, upload before the files were ready, retry after errors without preserving the intended workflow, or spend too much time deciding which tool to call. The user had to keep checking “where are we in the process, which files have changed, what ran, what failed, what remains?” The problem was therefore not one bad code generation, but the inability to keep a procedural integration workflow reliable over several steps ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).

### Эпизод 2. Nested prompts and MCP server: more instruction surface, still brittle

The next attempt used nested prompt files: a master workflow prompt branching into sub-workflow prompts such as `workflow1.md` and `workflow2.md`, depending on the app type. The author also built an MCP server for the cloud sandbox platform API and included hints telling Claude which tool to use and when. This worked “OK” but remained brittle: Claude occasionally followed the wrong step or called the wrong endpoint. It was also slow: before real work began, tool descriptions and complex prompting consumed context and thinking time ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).

The concrete number matters: the `/context` screenshot in Claude Code showed MCP tool descriptions taking 34% of context before any coding work had started. Even if some MCP servers were added for experimentation, the single custom MCP server for the workflow still used a lot of context. This is the case’s central before/after: before Klaus Kode, control was attempted by putting more instructions and tools into the agent’s input; after the pivot, fixed API calls moved out of the agent and back into deterministic Python ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).

### Эпизод 3. Pivot: Claude Code should write code, deterministic Python should call known APIs

The turning point is explicit in the source: “I really don’t need to tell Claude to call APIs for me.” If the engineer already knows the correct API endpoint and the sequence is fixed, making the model decide tool calls burns time and tokens. So Klaus Kode separates responsibilities. Claude Code handles the agentic part: write or modify Python code, update files, debug code. The workflow engine handles deterministic steps: call Quix APIs, upload files, run the sandbox, fetch logs, decide which phase comes next. Claude Code SDK is used to invoke Claude Code from within the workflow application, then control returns to the orchestrator after the coding step ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it), [Claude Code SDK docs](https://docs.anthropic.com/en/docs/claude-code/sdk)).

The repository makes this split concrete. `main.py` creates a `WorkflowOrchestrator`, registers services through a `ServiceContainer`, builds a `WorkflowContext`, configures the OpenAI Agents SDK with tracing disabled and a dummy key because the tool is using Anthropic, and then runs source/sink/diagnose flows through phase arrays. In source workflow, phase instances are recreated on each run to support back navigation; some phases, such as connection testing and schema, can be skipped if cached schema analysis is available. This is not “Claude decides every next step”; it is a Python state machine with explicit phase index, navigation exceptions and optional monitoring ([repository `main.py`](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py)).

### Эпизод 4. Workflow structure: source, sink, transform, diagnose and phase-level control

Klaus Kode’s CLI is a wizard. The public blog says it guides users step-by-step through workflows centered on coding and deploying Python applications. The repo setup also makes the target use case narrow: users need Python 3.12+, Quix PAT, Anthropic API key, Quix Cloud sandbox/project access and Claude Code CLI installed/authenticated. This matters because Klaus Kode is not a generic agent platform. It is a workflow tool for a specific platform and integration task: building Quix-compatible data pipeline applications ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it), [Klaus Kode repo](https://github.com/quixio/klaus-kode-agentic-integrator)).

Inside the workflow, phases map to concrete operations. A source workflow runs through source selection, connection testing, schema analysis, code generation/debugging, sandbox testing, deployment and optional monitoring. Sink and diagnose workflows have their own sequences. The `NavigationBackRequest` handling is important: when a user goes back, the orchestrator decrements phase index or returns to triage rather than asking Claude to remember a prior step. The workflow engine therefore owns state transitions; Claude is called inside selected phases as an executor or analyzer, not as the keeper of the whole lifecycle ([repository `main.py`](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py), [workflow factory](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/workflow_factory.py)).

### Эпизод 5. Claude prompts become local contracts, not the whole process

The prompt files in the repo show how the agent is bounded. `prompts/tasks/claude_code_system_prompt.md`, source instructions, source connection test prompts and debug prompts define what Claude Code should do in a specific phase. The prompt is not “manage the full workflow”; it is a local contract inside a phase that already has input context, expected output and next step determined by the orchestrator. This is why the repo contains not only prompts, but `WorkflowContext`, service classes, phase classes, debug analyzer and deployment monitoring logic ([Klaus Kode prompts directory](https://github.com/quixio/klaus-kode-agentic-integrator/tree/main/prompts/tasks), [debug analyzer](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/services/debug_analyzer.py)).

The technical before/after is sharp. Before: large prompts and MCP descriptions try to teach Claude the whole cloud workflow. After: Python code calls known APIs and gives Claude bite-sized tasks. If API returns an unexpected error, the engine can hand the logs to an agent for analysis. But the ordinary “upload code, start sandbox, download logs” path is deterministic. This reduces context pressure and makes the workflow auditable: the system knows which phase failed and what artifact came out of it ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).

### Эпизод 6. Sandbox loop: code, upload, run, logs, debug, redeploy

The most concrete working loop is the sandbox loop. Claude writes or modifies the Python application; the orchestrator uploads code, variables and dependency definitions to Quix Cloud; Quix runs the app inside a development container in a Kubernetes cluster; the orchestrator downloads run logs; if the app fails, debug analysis identifies the problem and control returns to a coding/debug phase. Only after sandbox testing does deployment happen, and deployment monitoring is optional: the user can monitor logs manually in the Quix Portal or let the workflow monitor status/logs. This makes the case more precise than “workflow engine”: the engine is effectively a stateful wrapper around code generation, Quix APIs, sandbox execution and log-driven debugging ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it), [repository `main.py`](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py)).

This also explains why Quix/Klaus Kode is not simply anti-agent. The agentic step remains central where code and debugging require language-model flexibility. The point is not to remove Claude, but to stop making Claude perform known procedural API orchestration. The result is a hybrid: agentic coding inside deterministic rails.

### Эпизод 7. Platform catch-up: Claude Code dynamic workflows do not erase the Quix-specific layer

Later Claude Code added dynamic workflows, which partially validate the problem Klaus Kode addressed: complex work needs structured workflow layers, not just prompts. But the Quix-specific part remains: Quix Cloud sandbox APIs, data pipeline deployment, source/sink/transform distinctions, logs, connection testing and platform-specific setup. Dynamic workflow support can reduce the need for custom orchestration in some environments, but it does not remove the case’s core lesson: when workflow steps are fixed and API calls are known, deterministic code should carry them, while the agent should handle the parts that actually require generation, adaptation or debugging ([Claude Code dynamic workflows](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code), [Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).

### Эпизод 8. Repository code turns the story from “workflow idea” into a state machine

The repository-level code should be kept in the story because it makes the Quix case more concrete than a blog post. `main.py` does not delegate the whole run to Claude. It creates services, a `WorkflowContext`, a `RunConfig`, a `ServiceContainer`, a `TriageAgent`, and then calls `WorkflowFactory.create_source_workflow`, `create_sink_workflow` or `create_diagnose_workflow`. Source workflow has eight phases; sink has seven; diagnose maps navigation steps such as application selection, download, analysis, edit, sandbox and deployment sync to phase indices. The code recreates fresh phase instances on each run because navigation/backtracking must not reuse stale phase state. That is a real implementation detail of “workflow engine”: the parent process has to remember where the human/agent is in the workflow, and sometimes it must intentionally go back ([repository `main.py`](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py)).

The debug/deployment branch also matters. Deployment monitoring is optional: after sandbox testing or deployment, the tool asks whether the user wants to monitor status/logs. If the deployment has `BuildFailed` or `RuntimeError`, the workflow can report completion with issues rather than pretend success. This is exactly the type of direct event description the story needs: Claude did not “make a connector”; the workflow guided source/sink/diagnose phases, used deterministic calls for platform actions, asked for monitoring decisions, handled back navigation and returned status-specific messages when deployment failed or required manual inspection ([repository `main.py`](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py)).

## Практика в действии

`example_workflow.md` даёт самый конкретный walkthrough. В примере используется SendGrid API. Запуск описан командой:

```bash
python main.py --api-docs https://docs.sendgrid.com/api-reference --service-name SendGrid --workflow source
```

После запуска CLI выводит заголовок `Klaus Kode Agentic Integrator`, service name, documentation URL и workflow type; затем запускает `APIDocsAnalyzer`, который "fetching and analyzing API documentation", после чего source agent генерирует connector implementation, testing agent запускает tests, documentation agent создаёт docs, PR manager открывает pull request ([example_workflow.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/example_workflow.md)).

Для source workflow пример перечисляет созданные файлы:

- `source_sendgrid.py`;
- `sendgrid_source.json`;
- `template.yml`;
- `README.md`;
- `test_sendgrid_source.py`;
- PR: `https://github.com/quixio/quix-streams/pull/123`.

Эта ссылка на PR теперь проверена через GitHub API: `quixio/quix-streams#123` действительно существует, но это merged PR `Update readme` от 19 мая 2023 года, с одним изменённым файлом и без связи с Klaus Kode, SendGrid или сгенерированным source connector. Поэтому URL из walkthrough нельзя использовать как подтверждение реального PR Klaus Kode ([example_workflow.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/example_workflow.md), [`quix-streams` PR #123](https://github.com/quixio/quix-streams/pull/123)).

Sink workflow запускается похожей командой с `--workflow sink` и генерирует `sink_stripe.py`, `stripe_sink.json`, `template.yml`, `README.md`, `test_stripe_sink.py`, а примерный PR указан как `https://github.com/quixio/quix-streams/pull/124` ([example_workflow.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/example_workflow.md)). Проверка через GitHub API вернула 404 для `quixio/quix-streams#124`, а прямые root-path запросы к `source_sendgrid.py` и `sink_stripe.py` в `quix-streams` тоже вернули 404. Это не доказывает, что подобных файлов нигде нет в дереве, но подтверждает: номера PR в старом walkthrough - демонстрационная фактура, не evidence внедрения.

Full integration workflow запускается с `--workflow full` и должен создать оба коннектора, metadata files, templates, documentation, tests и pull request. В walkthrough отдельно показана "auto-debugging" ветка: при падении теста агент читает failure output, определяет проблему authentication, обновляет connector implementation и повторно запускает тесты ([example_workflow.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/example_workflow.md)). Пока это описание сценария из документации, а не независимый лог реального запуска.

`custom_workflow_example.py` добавляет другой тип конкретики: workflow можно расширять своими агентами. Пример вводит `SecurityReviewAgent`, который проверяет authentication handling, API key exposure, input validation, rate limiting и error handling. В том же файле показан `CustomIntegrationContext`, где добавлены `security_review_passed` и `performance_metrics`, а также `CustomWorkflowRunner`, который запускает security review после базовой интеграции ([custom_workflow_example.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/custom_workflow_example.py)).

Текущий `docs/example_workflow.md` даёт другой уровень walkthrough, ближе к Quix Cloud. Он больше не подтверждает старый Alpha Vantage/GitHub Issues/PR сценарий из второго прохода; вместо этого показывает end-to-end поток Wikipedia Change Event Stream -> Kafka topic -> Clickhouse ([End-to-end Tutorial](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs/example_workflow.md)). Это важная поправка: старые ссылки `e2e_tutorial.md` и root-level examples могли относиться к более ранней структуре репозитория или к неверно прочитанной поверхности, а текущая проверенная страница репозитория ведёт на `docs/example_workflow.md`.

Страница интеграции Quix обещает sandbox, анализ логов, auto-debug for configured cycles и deployment connector as containerized application, но не подтверждает текущим текстом fork/branch/PR и отсутствие локальных зависимостей: Quick Start требует локальные Git/Python/Claude Code CLI и startup script ([Quix Integration page](https://quix.io/integrations/klaus-kode), [README](https://github.com/quixio/klaus-kode-agentic-integrator)). Для будущей истории полезно сравнить три поверхности: блог о рождении идеи, README как пользовательская установка, и docs/example_workflow как длинная сцена работы с Quix Cloud.

В четвёртом проходе integration page добавила ещё одну мини-сцену, не связанную с Wikipedia example. Страница предлагает мысленный пример: пользователь хочет читать sensor data из internal Websocket API и позже писать в S3. "Обычный" путь перечислен как восемь шагов: прочитать Websocket docs, настроить environment/dependencies/S3 env vars, написать чтение из Websocket, написать запись в S3, протестировать локально, вернуться к коду при поломке, упаковать для deployment и развернуть серверный процесс. Klaus Kode оставляет почти то же число шагов, но переносит их в терминальный Source wizard: сохранить Websocket docs в knowledge folder, описать нужные данные, принять сгенерированный код, ответить на вопросы про env vars/secrets, загрузить код в Quix Cloud sandbox, прочитать логи, включить auto-debug на заданное число cycles, затем развернуть контейнер, пишущий в Kafka topic `sensor-data`; для S3 нужно запускать Sink workflow из того же topic ([Quix Integration page](https://quix.io/integrations/klaus-kode)).

## Артефакты и файлы

Публичный репозиторий `quixio/klaus-kode-agentic-integrator` содержит несколько файлов, которые надо раскрыть глубже в следующих проходах:

- `README.md`: позиционирование, архитектура агентов, quick start, workflow types, environment variables, testing commands, license ([README](https://github.com/quixio/klaus-kode-agentic-integrator)).
- `docs.md`: более предметное описание Quix integration structure, source/sink/metadata/template components и требований к docs/tests ([docs.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs.md)).
- `instructions.md`: вероятно, operational instructions для Claude Code или workflow. Найден как файл в репозитории, но в этом проходе не раскрыт достаточно глубоко, чтобы использовать его как подтверждение фактов ([repo listing](https://github.com/quixio/klaus-kode-agentic-integrator)).
- `example_workflow.md`: walkthrough для source, sink и full workflows с sample output и списком generated files ([example_workflow.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/example_workflow.md)).
- `custom_workflow_example.py`: extension story, где workflow дополняется security review и performance metrics ([custom_workflow_example.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/custom_workflow_example.py)).
- `main.py`: текущий composition root, который создаёт `WorkflowOrchestrator`, регистрирует сервисы, запускает source/sink/diagnose workflows, обрабатывает back navigation и reset context для нового workflow ([main.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py)).
- `workflow_tools/workflow_factory.py`: текущий список фаз Source/Sink/Diagnose и регистрация phase factories через `ServiceContainer` ([workflow_factory.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/workflow_factory.py)).
- `workflow_tools/contexts.py`: dataclass-состояние workflow, включая workspace, technology, schema, code generation, deployment и credentials ([contexts.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/contexts.py)).
- `workflow_tools/services/claude_code_service.py`: обнаружение Claude CLI, Windows monkey-patch, prompt size check, запуск `claude_code_sdk.query`, чтение/запись `main.py`, debug через `error_logs.txt`, `schema_analysis.md` и сохранение thought files ([claude_code_service.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/services/claude_code_service.py)).
- `workflow_tools/services/debug_analyzer.py`, `workflow_tools/phases/source/phase_source_connection_testing.py`, `workflow_tools/phases/source/phase_source_sandbox.py`, `workflow_tools/phases/shared/phase_monitoring.py`: auto-debug, connection test, sandbox upload/run/log analysis и deployment monitoring ([debug_analyzer.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/services/debug_analyzer.py), [phase_source_connection_testing.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/phases/source/phase_source_connection_testing.py), [phase_source_sandbox.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/phases/source/phase_source_sandbox.py), [phase_monitoring.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/phases/shared/phase_monitoring.py)).
- `prompts/tasks/*.md`, `config/models.yaml`, `.env.example`: точные prompt contracts, модельная конфигурация и минимальный набор секретов `ANTHROPIC_API_KEY`, `QUIX_TOKEN`, `QUIX_BASE_URL` ([prompts/tasks](https://github.com/quixio/klaus-kode-agentic-integrator/tree/main/prompts/tasks), [models.yaml](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/config/models.yaml), [.env.example](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/.env.example)).
- `tests/`: в README есть команды `pytest tests/`, `pytest tests/ -v`, `pytest tests/test_agents.py::test_api_docs_analyzer -v`; сами тесты ещё не раскрыты ([README](https://github.com/quixio/klaus-kode-agentic-integrator)).

Текущие quick-start/environment источники фиксируют уже не `OPENAI_API_KEY`/GitHub CLI как основной путь, а Claude Code CLI, Anthropic API key, Quix PAT и `.env` с `ANTHROPIC_API_KEY`, `QUIX_TOKEN`, `QUIX_BASE_URL` ([README](https://github.com/quixio/klaus-kode-agentic-integrator), [.env.example](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/.env.example)).

После третьего прохода список артефактов нужно снова уточнить. Текущая repo listing показывает `.claude/`, `config/`, `docs/`, `logging/`, `prompts/`, `resources/`, `workflow_tools/`, `working_files/`, `.env.example`, `README.md`, `main.py`, `requirements.txt`, `start.bat`, `start.ps1`, `start.sh`; в шестом проходе GitHub показывал 109 commits, 67 stars, 13 forks, Issues 0, Pull requests 0, отсутствие published releases и latest commit `588b653` от 29 сентября 2025 ([GitHub repo](https://github.com/quixio/klaus-kode-agentic-integrator)). Это уже не тот root layout, который был записан после второго прохода (`app/`, `services/`, `workflows/`, `DEPLOYMENT.md`, `quix.yaml`); расхождение нужно проверять не по памяти ранних проходов, а через commit history или clone.

`main.py` в текущем виде выглядит как composition root: он импортирует `WorkflowContext`, `ServiceContainer`, `WorkflowFactory`, `WorkflowType`, `TriageAgent`, `PlaceholderWorkflowFactory` из `workflow_tools`, отдельно берёт `ClaudeCodeService`, содержит `run_source_workflow`, `run_sink_workflow`, `run_diagnose_workflow`, проверяет `ANTHROPIC_API_KEY`, `QUIX_TOKEN`, `QUIX_BASE_URL` и работает с Quix workspace ([main.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py)). В пятом проходе это уже не только HTML-страница файла: GitHub API позволил прочитать `main.py` и ключевые модули `workflow_tools`.

## Повороты взгляда

Первый проход даёт полезную цепочку:

- сначала автор пытался решить задачу увеличением prompt и контекста;
- затем добавил MCP как источник знаний;
- затем признал, что проблема находится в управлении процессом, а не только в знаниях агента;
- после этого появился отдельный workflow layer, который разбивает интеграцию на этапы и хранит контекст между ними ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it), [README](https://github.com/quixio/klaus-kode-agentic-integrator)).

Но есть и обратная сторона. Архитектура добавляет ещё один слой сложности: теперь надо поддерживать сам workflow engine, его agents, SDK integration, credentials, Quix Cloud sessions, тесты и шаблоны. История может оказаться не "AI сам сделал интеграции", а "команда заменила постоянное ручное сопровождение агента на сопровождение собственного инструмента".

Четвёртый проход усиливает именно эту обратную сторону. В блоге автор прямо разделяет agentic steps и deterministic steps: Claude Code получает task на генерацию кода и изменение файлов, а workflow engine вызывает нужные API, загружает код, переменные и зависимости в cloud sandbox, запускает приложение и забирает логи. Это не просто "multi-agent orchestration"; это решение забрать у агента часть свободы там, где порядок действий известен заранее ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).

Пятый проход добавляет проверяемую кодовую опору под этот поворот. Source/Sink/Diagnose теперь видны как phase lists в `WorkflowFactory`, context - как dataclasses с сериализацией, а Claude Code - как сервис, которому передают narrow file task и app path. При этом цена обвязки тоже стала видна: Windows monkey-patch, prompt size checks, запись больших логов в файлы, env var collection, Quix IDE session management, retry menus и отдельный AI-анализ логов ([workflow_factory.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/workflow_factory.py), [contexts.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/contexts.py), [claude_code_service.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/services/claude_code_service.py)).

## Ограничения и неудобная фактура

- Основной нарратив пока исходит от Quix. Нужны внешние подтверждения: реальные PR, комментарии ревью, issues, обсуждения команды, follow-up материалы.
- `example_workflow.md` использует PR URLs `/pull/123` и `/pull/124`; они выглядят как демонстрационные placeholders. Их нельзя использовать как свидетельство реального merged contribution без проверки ([example_workflow.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/example_workflow.md)).
- Проверка PR `/pull/123` и `/pull/124` через GitHub API дала более жёсткий результат: `quix-streams#123` - реальный merged PR `Update readme` от 19 мая 2023 года, не связанный с Klaus Kode; `quix-streams#124` возвращает 404. В досье эти URL остаются placeholders из walkthrough, а не evidence фактического использования ([`quix-streams` PR #123](https://github.com/quixio/quix-streams/pull/123), [`quix-streams` PR #124](https://github.com/quixio/quix-streams/pull/124)).
- README говорит о GitHub PR creation, но пока не проверено, действительно ли `PRManager` создаёт PR через `gh` или это scaffold/демонстрационный код ([README](https://github.com/quixio/klaus-kode-agentic-integrator)).
- Репозиторий на момент шестого прохода показывал `Issues 0`, `Pull requests 0`, отсутствие published releases, 109 commits, 67 stars, 13 forks и latest commit `588b653` от 29 сентября 2025. Это может означать ранний прототип с некоторым вниманием сообщества, но не доказывает реальное использование в Quix Streams или у внешних команд ([GitHub repo](https://github.com/quixio/klaus-kode-agentic-integrator)).
- Запись второго прохода о GitHub Personal Access Token, fork/branch/PR и удалении temporary token после работы на третьем проходе не подтвердилась текущей версией страницы. Сейчас страница и README говорят о Quix Cloud PAT, Anthropic API token и локальном `.env`; это всё ещё security/trust деталь, но другая: пользователь выдаёт инструменту доступ к Quix Cloud sandbox/deployments и оплачиваемому Anthropic API, а не обязательно к GitHub PR workflow ([Quix Integration page](https://quix.io/integrations/klaus-kode), [README](https://github.com/quixio/klaus-kode-agentic-integrator)).
- На разных публичных поверхностях не полностью совпадает набор workflow: README показывает Source/Sink и coming soon для Transform/Debug; текущий `docs/example_workflow.md` всё ещё упоминает Diagnose and Update; `main.py` имеет `run_diagnose_workflow` и `WorkflowType.DIAGNOSE` ([README](https://github.com/quixio/klaus-kode-agentic-integrator), [End-to-end Tutorial](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs/example_workflow.md), [main.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py)). Это может быть следом быстрого развития или рассинхронизации документации.
- В `WorkflowInfo` Diagnose уже помечен как `IMPLEMENTED`, Transform - как `TBD`, тогда как часть пользовательской поверхности всё ещё говорит о Debug как coming soon. Это уточняет расхождение: кодовая enum-карта и README/menu могут быть рассинхронизированы ([workflow_types.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/workflow_types.py)).
- История привязана к домену Quix: коннекторы к API, Quix Streams, templates, metadata, docs. Переносимость на другие проекты требует проверки. Возможно, ценность Klaus Kode именно в узкой повторяемой форме задач, а не в универсальности.
- Нужно осторожно обращаться с термином "multi-agent". В текущих источниках агенты выглядят как роли в workflow. Пока нет свидетельства, что они автономно спорят, планируют или конкурируют.
- Auto-debug в текущем tutorial имеет явную цену: до десяти попыток Claude, расход API tokens и риск, что базовые connection problems вроде wrong password/hostname не будут распознаны агентом ([End-to-end Tutorial](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs/example_workflow.md)).
- Текущая integration page прямо говорит, что Klaus Kode не free-form chat interface, а wizard, и в disclaimer сохраняет early prototype warning: tool может содержать bugs, выдавать incorrect results, unstable/incomplete features; generated code/configurations нужно review/test перед production ([Quix Integration page](https://quix.io/integrations/klaus-kode)).
- В блоге есть признание, что автор добавил несколько MCP-серверов "попробовать, полезны ли они"; поэтому цифра 34% по `/context` не должна автоматически переноситься на минимальную конфигурацию Klaus Kode. При этом автор отдельно оговаривает, что даже один MCP-сервер для его workflow всё равно съедал заметный контекст ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).
- Слабый внешний сигнал из LinkedIn выглядит скорее как перепубликация/популяризация, чем как независимый опыт использования: Santiago Valdarrama называет Klaus Kode open-source console-based workflow для data integrations через Claude Code SDK, говорит о "10x faster" по сравнению с просьбой к chatbot написать всё целиком и оставляет ссылку на GitHub repo; поисковая выдача показывает 3 реакции. Это полезно как след распространения, но не как подтверждение production adoption ([LinkedIn search result](https://www.linkedin.com/posts/svpino_this-open-source-agent-is-sick-klaus-kode-activity-7376997668344033280-MfX9)).
- Dynamic workflows in Claude Code - это фон, а не источник о Quix. Его нельзя использовать как доказательство, что Klaus Kode был принят, заменён или технически устарел. Он показывает только, что проблема сохранения workflow/progress outside a single conversation стала достаточно общей, чтобы Anthropic вынес её в продуктовую функцию Claude Code; доменная часть Quix Cloud/Kafka/connectors остаётся отдельной ([Anthropic dynamic workflows announcement](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)).

## Неровная фактура

- Название `Klaus Kode` само по себе работает как деталь истории: автор статьи объясняет его как "parent" над Claude Code и немецкую игру с заменой `C` на `K` в словах вроде `Class`, `Culture`, `Camera` ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).
- В статье автор описывает сбои агента через бытовые, но проверяемые симптомы: wrong order, skipped tests, unrelated refactoring, loss of state. Это лучше сохранять как список наблюдений, а не сглаживать до "агент был нестабилен" ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).
- В `example_workflow.md` workflow не только генерирует код, но и печатает staged output. Это может дать будущей истории сцену терминала: запуск с `--workflow source`, затем "Step 1: Analyzing API Documentation", затем generation, tests, docs, PR ([example_workflow.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/example_workflow.md)).
- `custom_workflow_example.py` показывает, что авторы думали о расширении процесса не только в сторону "больше кода", но и в сторону security review. Однако это может быть пример extensibility, а не реальная практика Quix ([custom_workflow_example.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/custom_workflow_example.py)).
- В текущем `docs/example_workflow.md` будущая сцена выглядит как терминальный wizard и Quix Cloud: выбор Source Workflow, app name `wikipedia-source`, project `MyProject`, topic `input-data`, knowledge folder с Wikipedia docs, загрузка `app.py` в sandbox, логи с event metadata, schema analysis через Haiku, producer test, затем sink в Clickhouse ([End-to-end Tutorial](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs/example_workflow.md)).
- В `main.py` есть странная, но показательная деталь: dummy OpenAI key ставится не как production credential, а чтобы Agents SDK не падал без `OPENAI_API_KEY`, пока tracing отключён. Это может стать маленьким техническим эпизодом о том, как агентские SDK тянут за собой инфраструктурные требования даже там, где главный исполнительный агент - Claude Code ([main.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py)).
- В README есть Windows-specific шероховатость: Claude Code нужно ставить через `irm https://claude.ai/install.ps1 | iex`, потому что установка через `npm` даёт проблемы с `claude.cmd`; Linux/Mac идут через `curl -fsSL https://claude.ai/install.sh | bash` ([README](https://github.com/quixio/klaus-kode-agentic-integrator)). Это маленькая сцена про то, что "workflow wizard" всё равно начинается с локальной инструментальной среды.
- Скриншот `/context` в блоге может стать важнее архитектурной диаграммы: он показывает, что проблема была не только в "агент забыл шаг", но и в цене попытки выдать агенту весь toolbox сразу. 34% контекста под MCP tool descriptions до начала работы - это фактура про перегруженную рабочую среду, а не абстрактная критика prompt engineering ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).
- Integration page аккуратно портит красивую историю "агент делает меньше шагов": пример Websocket -> S3 сохраняет восемь шагов и сам говорит, что их столько же. Разница не в исчезновении процесса, а в том, что пользователь отвечает на вопросы wizard, а fixed steps выполняются за него через Quix Cloud sandbox и deployment path ([Quix Integration page](https://quix.io/integrations/klaus-kode)).
- В `claude_code_service.py` есть отдельная защита от того, что Claude Code отредактирует не тот `main.py`: debug path проверяет, не содержит ли файл `WorkflowOrchestrator`, и тогда печатает предупреждение, что это workflow orchestrator, а не app `main.py`; если в коде есть `quixstreams`, он считает это признаком правильного application file. Это очень конкретный след проблемы working directory/app path, которую проект решал не доверием к агенту, а явными проверками ([claude_code_service.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/services/claude_code_service.py)).
- В prompt-файле `claude_code_source_instructions.md` есть внутреннее противоречие: один блок просит "production-ready" Python-код, а ниже testing documentation note говорит считать приложение prototype/get-started app, а не full fledged production app. Для истории это полезная шероховатость: даже внутри жёсткого prompt-коридора остаётся напряжение между demo, production и onboarding ([claude_code_source_instructions.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/prompts/tasks/claude_code_source_instructions.md)).
- Anthropic dynamic workflows тоже сохраняют трение: перед запуском workflow показывается план and asks for confirmation, а документация/announcement предупреждает начинать с малого, проверять части и ждать ошибок. Это полезная параллель к Klaus Kode: даже когда workflow становится встроенной функцией Claude Code, human gate и operational caution не исчезают ([Anthropic dynamic workflows announcement](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)).

## Детали, восстановленные после сверки с последней загруженной версией

- Репозиторий Klaus Kode нужно сохранить не как абстрактный “workflow engine”, а как набор конкретных компонентов: `WorkflowFactory`, `ClaudeCodeService`, `PRManager`, `APIDocsAnalyzer`, `DocumentationAgent`, `SourceConnectorAgent`, `SinkConnectorAgent`, `TestingAgent`, `DebugAnalyzer`, `CodeGenerationContext`, `CredentialsContext`, `DeploymentContext`, `SchemaContext`, `WorkspaceContext`, `TechnologyContext` ([Klaus Kode repository](https://github.com/quixio/klaus-kode-agentic-integrator)).
- Claude Code boundary должна оставаться технической: в prompts/tasks используются tool names and expectations like `Read`, `Write`, `Edit`, `MultiEdit`, `Bash`, `Glob`, `Grep`, `WebFetch`, `WebSearch`; workflow also depends on `CLAUDE_CLI_PATH`, `PATH`, local project layout and an environment where `OPENAI_AGENTS_DISABLE_TRACING=true` may be relevant for OpenAI Agents SDK usage ([Klaus Kode repository](https://github.com/quixio/klaus-kode-agentic-integrator)).
- Wikipedia/ClickHouse example should remain concrete: source documentation included `Wikipedia Changes Event Stream HTTP Service - Wikitech.md`; the run created `app.py` / `app.yaml`, pushed rows with messages such as `Inserting 48 rows into wikipedia_edits`, `Processed 48 valid rows`, `Successfully inserted 48 rows into wikipedia_edits`, and carried fields like `Time`, `Title`, `User`, `Type`, `Wiki` ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it); [Klaus Kode repository](https://github.com/quixio/klaus-kode-agentic-integrator)).
- `claude_code_source_instructions.md` contained a useful internal tension: one part asks for production-ready Python code, while testing/documentation notes can frame the output as prototype/get-started app rather than full production application. This should be preserved because it shows the mismatch between demo onboarding, production language and generated integration code ([claude_code_source_instructions.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/prompts/tasks/claude_code_source_instructions.md)).
- The wizard/startup details should remain visible: `bash start.sh`, Quix PAT / Anthropic API key / GitHub token setup, Quix Cloud sandbox, branch creation such as `branch_name`, generated project files and `MyProject` style workspace naming are part of the story’s concrete surface, not incidental setup ([README](https://github.com/quixio/klaus-kode-agentic-integrator)).

## Источники

### Первичные раскрытые

- [Quix blog: "Claude Code Wouldn't Behave, So I Built a Workflow Engine to Tame It"](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it). Главный нарративный источник: проблема, неудачные попытки через prompt/MCP, архитектурный поворот к workflow engine. В четвёртом проходе дополнительно раскрыт как источник конкретной сцены: nested prompt files `master_workflows.md`/`workflow1.md`/`workflow2.md`, MCP-сервер для cloud sandbox API, `/context` в Claude Code и 34% контекста под MCP tool descriptions. Ограничение: источник от автора/компании, нужен внешний контроль.
- [GitHub: `quixio/klaus-kode-agentic-integrator`](https://github.com/quixio/klaus-kode-agentic-integrator). Публичный репозиторий инструмента. В первом проходе использован для состава файлов, README, статуса issues/PR/releases; в шестом проходе переоценён по текущему listing: 109 commits, 67 stars, 13 forks, Issues 0, Pull requests 0, no releases, latest commit `588b653` от 29 сентября 2025. Ограничение: GitHub metadata не заменяет анализ commit history и не доказывает real adoption.
- [README](https://github.com/quixio/klaus-kode-agentic-integrator). В третьем проходе перечитан как текущая user-facing точка входа: terminal workflow wizard, quick start через `start.sh`/`start.bat`/`start.ps1`, `.env`, `ANTHROPIC_API_KEY`, `QUIX_TOKEN`, `QUIX_BASE_URL`, Source/Sink/Transform/Debug menu, Claude Code install notes.
- [docs.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs.md). Использован для структуры Quix integrations: source, sink, metadata, template. Ограничение: текущая repo listing выводит docs как папку; root-level `docs.md` нужно перепроверить через raw clone или commit history.
- [example_workflow.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/example_workflow.md). Использован в ранних проходах для команд запуска, SendGrid/Stripe examples, generated files, staged output и auto-debugging branch. Ограничение: walkthrough может быть демонстрационным; текущий репозиторий ведёт к `docs/example_workflow.md`, и старый root-level файл может быть устаревшим или перемещённым.
- [custom_workflow_example.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/custom_workflow_example.py). Использован для факта расширяемости через `SecurityReviewAgent` и `CustomWorkflowRunner`. Ограничение: пример, не доказательство production use.
- [Quix Integration page: Klaus Kode](https://quix.io/integrations/klaus-kode). В третьем проходе перечитана как текущая user-facing поверхность: терминальный wizard, Quix Cloud sandbox, Quix Cloud PAT, Anthropic API token, auto-debug cycles, early prototype warning, disclaimer про bugs/incorrect results/review before production. В четвёртом проходе дополнительно использована для Websocket -> S3 comparison и точного списка prerequisites: Git, Python, Claude Code CLI, Anthropic API token, Quix Cloud PAT, `.env` и startup script. Ограничение: собственная продуктовая страница Quix, не внешнее подтверждение; не подтверждает прежнюю запись про GitHub PAT/fork/PR.
- [End-to-end Tutorial / `docs/example_workflow.md`](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs/example_workflow.md). Раскрыт в третьем проходе как текущий walkthrough: Wikipedia Change Event Stream source, Quix Cloud sandbox, schema analysis through Haiku, producer test, Clickhouse sink, auto-debug options и limit до десяти попыток. Ограничение: tutorial может описывать intended flow, а не лог реального запуска.
- [main.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/main.py). В пятом проходе раскрыт через GitHub API как composition root: `WorkflowOrchestrator`, `ServiceContainer`, `WorkflowFactory`, source/sink/diagnose runners, back navigation, optional deployment monitoring и context reset.
- [workflow_tools/workflow_factory.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/workflow_factory.py). Раскрыт как список фаз и service registration для Source/Sink/Diagnose. Подтверждает, что порядок workflow задан Python-кодом.
- [workflow_tools/contexts.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/contexts.py). Раскрыт как state model: workspace, technology, schema, code generation, deployment, credentials и JSON-сериализация.
- [workflow_tools/services/claude_code_service.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/services/claude_code_service.py). Раскрыт как граница Claude Code SDK: CLI detection, Windows monkey patch, prompt size checks, `ClaudeCodeOptions`, чтение/запись app `main.py`, debug logs через файлы, сохранение thought process.
- [workflow_tools/services/debug_analyzer.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/services/debug_analyzer.py). Раскрыт как auto-debug loop и меню debug-действий. Ограничение: это кодовая intended behavior, не лог успешного production run.
- [workflow_tools/phases/source/phase_source_connection_testing.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/phases/source/phase_source_connection_testing.py), [phase_source_sandbox.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/phases/source/phase_source_sandbox.py), [phase_monitoring.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/phases/shared/phase_monitoring.py). Раскрыты для connection test, Quix IDE/session upload/run, env vars/secrets, timeout, log analysis и deployment monitoring.
- [prompts/tasks/claude_code_system_prompt.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/prompts/tasks/claude_code_system_prompt.md), [claude_code_source_connection_test.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/prompts/tasks/claude_code_source_connection_test.md), [claude_code_source_instructions.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/prompts/tasks/claude_code_source_instructions.md), [claude_code_debug_system_prompt.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/prompts/tasks/claude_code_debug_system_prompt.md). Раскрыты как prompt contracts: `app_path`, запрет mock sample data, 10 real records для connection test, schema file, `app.yaml`, Kafka/Quix Streams правила, обязательный edit при debug.
- [config/models.yaml](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/config/models.yaml), [.env.example](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/.env.example). Раскрыты для моделей, tools, `max_turns`, `permission_mode`, `ANTHROPIC_API_KEY`, `QUIX_TOKEN`, `QUIX_BASE_URL`.
- [`quixio/quix-streams` PR #123](https://github.com/quixio/quix-streams/pull/123). Раскрыт как отрицательное подтверждение: реальный merged README PR от 2023-05-19, не SendGrid/Klaus Kode. Нужен, чтобы не использовать walkthrough URL как evidence.

### Фоновые раскрытые

- [Quix Streams documentation: Introduction](https://quix.io/docs/quix-streams/introduction.html). Фон по Quix Streams как Python stream processing framework. Нужен только для контекста предметной области.
- [Quix Streams tutorial: Hello World](https://quix.io/docs/quix-streams/tutorials/hello-world.html). Фон по локальной работе с Kafka, `Application`, topics и `StreamingDataFrame`.
- [Anthropic docs: Claude Code SDK](https://docs.anthropic.com/en/docs/claude-code/sdk). Нужно раскрыть глубже в следующем проходе, если описывать техническую границу Claude Code SDK.
- [OpenAI Agents SDK docs](https://openai.github.io/openai-agents-python/). Нужно раскрыть глубже в следующем проходе, если описывать техническую границу OpenAI Agents SDK.
- [Anthropic: "Introducing dynamic workflows in Claude Code"](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code). Фоновый источник после Quix: встроенные workflows in Claude Code, subagents, сохранение progress outside the conversation, confirmation before run и предупреждение о token usage/mistakes. Нужен как контраст к Klaus Kode, но не как подтверждение фактов о Quix.

### Непрочитанные или слабые

- `instructions.md`, `workflow.py`, `agents.py`, `tests/` в старой карте репозитория. Найдены в ранних проходах, но не сверены с текущим деревом. `main.py` уже частично раскрыт через GitHub API.
- `.claude/`, `docs/`, `logging/`, `resources/`, `working_files/`, `start.*` и часть `workflow_tools/`. Найдены как текущая структура репозитория; часть ключевых модулей раскрыта в пятом проходе, но commit history, tests, resources и working_files ещё требуют отдельной проверки.
- Реальные PR в `quixio/quix-streams`, которые могли быть созданы или вдохновлены Klaus Kode. PR `#123/#124` из walkthrough проверены и не подтверждают внедрение; остаётся открытым поиск по другим PR/commits/paths.
- [LinkedIn post by Santiago Valdarrama](https://www.linkedin.com/posts/svpino_this-open-source-agent-is-sick-klaus-kode-activity-7376997668344033280-MfX9). В четвёртом проходе раскрыт только через поисковую выдачу, не через полноценное открытие LinkedIn. Поисковая выдача даёт полувнешний сигнал: Klaus Kode назван open-source console-based workflow для data integrations с Claude Code SDK, упомянуто четыре обещанных шага и ссылка на GitHub repo, показаны 3 реакции. Статус: слабый источник / социальная реакция; не использовать как подтверждение реального внедрения.

### Источники, заново раскрытые для переработки эпизодов

- [Quix blog: “Claude Code wouldn’t behave, so I built a workflow engine to tame it”](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it) — главный первичный narrative source: prompt/MCP failures, 34% context used by MCP tool descriptions, Claude Code SDK, deterministic API sequence, upload/run/download logs.
- [quixio/klaus-kode-agentic-integrator README](https://github.com/quixio/klaus-kode-agentic-integrator) — первичный source-level источник по setup: Python 3.12+, Claude Code CLI, Quix project/PAT, Anthropic key, `.env`, `start.sh`, workflow menu, Source/Sink/Transform/Debug structure.

## Поисковые формулировки

Уже использованные формулировки:

- `"Quix" "Klaus Kode"`
- `"Klaus Kode" AI coding`
- `"Quix" "agentic development" "Klaus"`
- `"Klaus Kode" "Claude Code SDK"`
- `"Klaus Kode" "OpenAI Agents SDK"`
- `"Klaus Kode" "auto-debug"`
- `"Klaus Kode" Quix LinkedIn`
- `site:github.com/quixio/klaus-kode-agentic-integrator "Source Workflow" "Sink Workflow"`
- `site:github.com/quixio/klaus-kode-agentic-integrator "End-to-end Tutorial"`

Следующие углы поиска:

- `site:github.com/quixio/quix-streams "Klaus Kode"`
- `site:github.com/quixio/quix-streams "Generated with Klaus"`
- `site:github.com/quixio/quix-streams "SendGrid" "source_sendgrid.py"`
- `site:github.com/quixio/quix-streams "Stripe" "sink_stripe.py"`
- `"Claude Code Wouldn't Behave" reaction`
- `"klaus-kode-agentic-integrator" issues`
- `"quixio/klaus-kode-agentic-integrator" "main.py"`
- `"Klaus Kode" "PRManager"`
- `"Klaus Kode" "SecurityReviewAgent"`

Добавленные во втором проходе:

- `site:github.com/quixio/klaus-kode-agentic-integrator "e2e_tutorial"`
- `site:github.com/quixio/klaus-kode-agentic-integrator "Diagnose and Update"`
- `site:github.com/quixio/klaus-kode-agentic-integrator "dummy-key-for-local-agents-sdk"`
- `site:github.com/quixio/klaus-kode-agentic-integrator "WorkflowDependencies"`
- `site:quix.io/integrations/klaus-kode "Personal Access Token"`
- `site:quix.io/integrations/klaus-kode "auto-debug cycles"`
- `site:github.com/quixio/quix-streams "source_sendgrid.py"`
- `site:github.com/quixio/quix-streams "sink_stripe.py"`
- `site:github.com/quixio/quix-streams "Klaus Kode"`

Добавленные в третьем проходе:

- `site:github.com/quixio/klaus-kode-agentic-integrator "Wikipedia Change Event Stream"`
- `site:github.com/quixio/klaus-kode-agentic-integrator "Clickhouse" "wikipedia_edits"`
- `site:github.com/quixio/klaus-kode-agentic-integrator "Let Claude Code SDK fix the error directly"`
- `site:github.com/quixio/klaus-kode-agentic-integrator "auto-debug" "10"`
- `site:github.com/quixio/klaus-kode-agentic-integrator "ANTHROPIC_API_KEY" "QUIX_TOKEN"`
- `site:github.com/quixio/klaus-kode-agentic-integrator "start.ps1" "claude.cmd"`
- `site:github.com/quixio/quix-streams "Wikipedia Change Event Stream"`
- `site:github.com/quixio/quix-streams "Clickhouse" "wikipedia_edits"`
- `"Claude Code Wouldn't Behave" "Klaus Kode"`
- `"Klaus Kode" "Quix Cloud PAT"`
- `"Klaus Kode" "terminal workflow wizard"`
- `"quixio/klaus-kode-agentic-integrator" "workflow_tools"`

Добавленные в четвёртом проходе:

- `"Klaus Kode" "34%" "context"`
- `"Klaus Kode" "/context" "MCP tool descriptions"`
- `"Klaus Kode" "master_workflows.md"`
- `"Klaus Kode" "workflow1.md" "workflow2.md"`
- `"Klaus Kode" "Websocket" "S3"`
- `"Klaus Kode" "sensor-data" "Kafka topic"`
- `"Klaus Kode" "Santiago Valdarrama" "LinkedIn"`
- `"Claude Code Wouldn't Behave" "MCP tool descriptions"`
- `"quixio/klaus-kode-agentic-integrator" "ServiceContainer"`
- `"quixio/klaus-kode-agentic-integrator" "WorkflowRunner"`

Добавленные в пятом проходе:

- `"quixio/klaus-kode-agentic-integrator" "workflow_factory.py"`
- `"quixio/klaus-kode-agentic-integrator" "phase_source_connection_testing.py"`
- `"quixio/klaus-kode-agentic-integrator" "phase_source_sandbox.py"`
- `"quixio/klaus-kode-agentic-integrator" "claude_code_source_connection_test.md"`
- `"quixio/klaus-kode-agentic-integrator" "forbidden-sample-data"`
- `"quixio/klaus-kode-agentic-integrator" "metadata String DEFAULT"`
- `"quixio/klaus-kode-agentic-integrator" "Argument list too long"`
- `"quixio/klaus-kode-agentic-integrator" "monkey_patch_claude_sdk_for_windows"`
- `"quixio/quix-streams" "Update readme" "pull/123"`
- `site:github.com/quixio/quix-streams/pull "Klaus Kode"`
- `site:github.com/quixio/quix-streams/pull "source_sendgrid.py"`

Добавленные в шестом проходе:

- `"Klaus Kode" "dynamic workflows"`
- `"Claude Code" "dynamic workflows" "Klaus Kode"`
- `"Klaus Kode" "588b653"`
- `"quixio/klaus-kode-agentic-integrator" "588b653"`
- `"quixio/klaus-kode-agentic-integrator" "latest commit"`
- `site:github.com/quixio/klaus-kode-agentic-integrator/commits "workflow_factory.py"`
- `site:github.com/quixio/klaus-kode-agentic-integrator/commits "PRManager"`
- `site:github.com/quixio/klaus-kode-agentic-integrator/commits "Diagnose"`
- `site:github.com/quixio/klaus-kode-agentic-integrator/commits "Quix Cloud"`


### Дополнительные раскрытые источники текущего прохода

- [Quix, “Claude Code wouldn’t behave, so I built a workflow engine to tame it”](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it) — первичный источник: 34% context from MCP descriptions, dev container in Kubernetes, deterministic Python API calls, OpenAI Agents SDK + Claude Code SDK split.
- [Stack Overflow: “Any way to load only some tools from an MCP server?”](https://stackoverflow.com/questions/79751034/any-way-to-load-only-some-tools-from-an-mcp-server) — фоновый технический источник по MCP context overhead and filtering/proxy approaches; использовать как внешний contrast, не как источник по Quix.

### Дополнительные раскрытые источники pass 3

- [GitHub `quixio/klaus-kode-agentic-integrator`](https://github.com/quixio/klaus-kode-agentic-integrator) — первичный repo source: terminal workflow wizard, install path, `.env`, Quix PAT, Anthropic API key, prerequisites, Claude Code CLI, Quix Cloud sandbox.
- [Quix integration page: “Klaus Kode — The Agentic Data Integrator”](https://quix.io/integrations/klaus-kode) — продуктовая страница: Python-based agentic data integrator, OpenAI Agents SDK for log/schema analysis, Claude Code SDK for code/debug/env/deps, Quix Cloud isolated containers.

## Кандидаты на иллюстрации

- Источник: [GitHub `quixio/klaus-kode-agentic-integrator`](https://github.com/quixio/klaus-kode-agentic-integrator). Что искать: README Quick Start with `git clone`, `.env`, Python 3.12+, Quix PAT and Anthropic API key. Зачем: показать, что история держится на конкретном terminal setup, а не на идее “приручить Claude Code”. Статус: high.
- Источник: [Quix integration page](https://quix.io/integrations/klaus-kode). Что искать: images around Klaus Kode / Quix Cloud / integration flow. Зачем: дать визуальный слой для wizard/cloud-sandbox. Статус: medium; проверить права.

- Из статьи Quix: image `KK2.png` / `https://cdn.prod.website-files.com/65cceb8c2a3ffed636247957/68d5c172c49663957a4c85e4_KK2.png`, если права позволяют. Нужен как визуальный вход в историю о workflow engine поверх Claude Code или startup CLI scene; точную роль нужно проверить по изображению перед публикацией ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).
- Из статьи Quix: image `KK3.png` / `https://cdn.prod.website-files.com/65cceb8c2a3ffed636247957/68d5c17161bdd527b2ab6ffa_KK3.png`. Нужен для сцены `/context` или workflow output; точное содержание нужно визуально сверить, права проверить отдельно ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).
- Из `README`: Mermaid-диаграмма architecture, где `Workflow Orchestrator` соединён с `APIDocsAnalyzer`, `SourceAgent`, `SinkAgent`, `TestingAgent`, `DocsAgent`, `PRManager`, а ниже показаны Claude Code SDK, OpenAI Agents SDK и GitHub API. Нужна как техническая схема. Статус: кандидат, можно реконструировать по README, но для публикации лучше проверить лицензию репозитория ([README](https://github.com/quixio/klaus-kode-agentic-integrator)).
- Из `example_workflow.md`: terminal output запуска `python main.py --api-docs ... --workflow source`. Нужен как "сцена" запуска. Статус: кандидат, можно цитировать коротко или пересобрать как собственную схему, не вставляя длинный фрагмент вывода ([example_workflow.md](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/example_workflow.md)).
- Из `quix.io/integrations/klaus-kode`: текущая страница с описанием терминального wizard, Quix Cloud sandbox, auto-debug и warning/disclaimer. Нужна для перехода от developer scaffold к productized onramp. Статус: кандидат, права и фактический UI нужно проверить; старая запись про GitHub PAT screen не подтверждена текущим прочтением ([Quix Integration page](https://quix.io/integrations/klaus-kode)).
- Из старой записи `e2e_tutorial.md`: pipeline/status screen с шагами cloning, analysis, implementation, testing, PR creation. Статус: исторический кандидат из второго прохода, не использовать без повторной проверки, потому что текущий repo путь ведёт на `docs/example_workflow.md`, а PR-сценарий не подтвердился ([End-to-end Tutorial](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/e2e_tutorial.md)).
- Из текущего `docs/example_workflow.md`: терминальный wizard с выбором `Source Workflow`, app name `wikipedia-source`, topic `input-data`, Quix Cloud project `MyProject` и последующими sandbox logs. Нужен как сцена перехода от prompt к управляемому запуску в Quix Cloud. Статус: кандидат, лучше реконструировать как собственную схему или использовать короткие допустимые excerpts ([End-to-end Tutorial](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs/example_workflow.md)).
- Из текущего `docs/example_workflow.md`: auto-debug option list и предупреждение про token usage / wrong password / hostname. Нужен как визуальное подтверждение трения: отладка есть, но она не магическая и ограничена стоимостью и диагностическими слепыми зонами. Статус: кандидат, не вставлять длинный terminal output без проверки прав и объёма цитирования ([End-to-end Tutorial](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/docs/example_workflow.md)).
- Из текущего README: Quick Start block с `ANTHROPIC_API_KEY`, `QUIX_TOKEN`, `QUIX_BASE_URL`, `start.sh`/`start.bat`/`start.ps1` и Windows install caveat для Claude Code. Нужен как иллюстрация того, что пользовательский wizard начинается с локальной настройки и credentials. Статус: кандидат, можно пересобрать как собственный callout, не как screenshot ([README](https://github.com/quixio/klaus-kode-agentic-integrator)).
- Из статьи Quix: screenshot вывода `/context` в Claude Code, где MCP tool descriptions занимают 34% контекста до начала работы. Нужен как иллюстрация цены prompt/MCP-heavy подхода. Статус: сильный кандидат; вероятный прямой URL `KK3.png`, но перед публикацией нужно визуально сверить, что это именно `/context` screenshot, и проверить права ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).
- Из статьи Quix: startup screen Klaus Kode CLI. Нужен как сцена перехода от Claude Code chat к отдельному terminal wizard. Статус: кандидат; вероятный прямой URL `KK2.png`, но перед публикацией нужно визуально сверить содержимое и проверить права ([Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it)).
- Из integration page: Websocket -> S3 comparison, где "обычный" путь и Klaus Kode path оба состоят из восьми шагов. Нужен как иллюстрация того, что Klaus Kode не отменяет процесс, а переносит фиксированные шаги в wizard/sandbox. Статус: кандидат для собственной схемы, не обязательно screenshot ([Quix Integration page](https://quix.io/integrations/klaus-kode)).
- Из `workflow_factory.py`: собственная схема фаз Source/Sink/Diagnose на основе текущего кода. Нужна, чтобы показать реальный deterministic skeleton вместо старой README-диаграммы с `PRManager`. Статус: кандидат для собственной схемы, не screenshot ([workflow_factory.py](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/workflow_factory.py)).
- Из `claude_code_source_connection_test.md` и `claude_code_source_instructions.md`: два prompt-фрагмента как иллюстрация staged narrowing: сначала 10 real sample records без Kafka/mock, потом Quix Streams/Kafka/app.yaml/schema. Статус: кандидат для короткого цитирования или собственной таблицы, не вставлять длинные prompt-блоки ([connection test prompt](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/prompts/tasks/claude_code_source_connection_test.md), [source instructions prompt](https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/prompts/tasks/claude_code_source_instructions.md)).
- Из Anthropic dynamic workflows announcement: схема/экран встроенного workflow in Claude Code, если будущая история будет сравнивать hand-built Klaus Kode harness и platform-native workflow. Статус: только как фоновый контраст, не как иллюстрация Quix; права нужно проверять отдельно ([Anthropic dynamic workflows announcement](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)).


- Источник: [Quix blog](https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it). Что искать: screenshot of Claude Code `/context` output showing 34% MCP tool-description overhead. Зачем: это сильнейший визуальный артефакт before-state. Статус: high.
- Источник: [Stack Overflow MCP question](https://stackoverflow.com/questions/79751034/any-way-to-load-only-some-tools-from-an-mcp-server). Что искать: question screenshot around `~46k tokens` and selective MCP loading. Зачем: показать, что Quix решает более широкий class of MCP context-overhead problems. Статус: low/medium; лучше ссылаться текстом.

### Дополнительные кандидаты после переработки эпизодов

- Скриншот Klaus Kode terminal menu с `Source Workflow`, `Sink Workflow`, `Transform Workflow`, `Debug Workflow` — high: показывает, как свобода агента ограничивается wizard-структурой.
- Изображение Source Workflow Steps из README / repo assets — high: лучший визуальный материал для последовательности deterministic/agentic steps.
- Скриншоты KK2/KK3 из Quix-assets — medium/high: если качество хорошее, могут показать реальный UI/terminal flow.
- Схема “Claude Code SDK → workflow engine → Quix Cloud sandbox → logs → next step” — high, если делать локально как поясняющую диаграмму.

## Открытые вопросы

- Были ли реальные PR в `quix-streams`, созданные Klaus Kode или явно использующие его шаблоны? PR `#123/#124` из walkthrough проверены и не подходят; нужно искать другие PR/commits/paths по SendGrid, Stripe, generated metadata и commit messages.
- Что именно делает `PRManager`: вызывает `gh`, формирует branch/commit/PR body или только описывает expected behavior?
- Как именно используется JSON-сериализация `WorkflowContext`: это реальный resume/state persistence path или вспомогательная возможность, которая почти не вызывается?
- Где проходит граница между OpenAI Agents SDK и Claude Code SDK в реализации? В пятом проходе видно, что `main.py` создаёт `RunConfig`, отключает tracing и использует dummy OpenAI key, а Claude Code работает через `ClaudeCodeService`; но нужно проверить все `Agent`-классы, `run_agent_with_retry` и Quix tools.
- Как соотносятся старые `APIDocsAnalyzer`/`SourceConnectorAgent`/`PRManager` из README первого прохода с текущими `workflow_tools/`, `workflows/`, `services/` и browser/cloud workflow? Это переименование, рефакторинг или две разные поверхности одного проекта?
- Почему README/menu говорит, что Debug workflow coming soon, а `WorkflowInfo` помечает `Diagnose and Update` как implemented? Нужно проверить commit history и текущий runtime.
- Что именно произошло между вторым и третьим проходом с публичной страницей: это изменение сайта, неверно прочитанная старая поверхность, A/B/динамический контент или рассинхронизация источников? Текущая версия не подтверждает GitHub PAT/fork/PR.
- Что именно происходит с Quix Cloud PAT в sandbox: где хранится, как долго живёт, какие scopes требуются, можно ли ограничить доступ workspace-only? Текущая страница и README требуют Quix token, но не раскрывают lifecycle credentials.
- Есть ли негативные реакции или ограничения: стоимость, latency, flaky tests, API credentials, hallucinated API docs, security concerns?
- Был ли проект внутренним экспериментом, public demo или инструментом, который реально поддерживается? Название теперь объяснено в статье, но статус использования всё ещё не проверен.
- Как изменилась позиция автора после публикации? Есть ли follow-up posts, comments, conference talks или commits после blog post?
- Почему текущая GitHub repo listing сильно отличается от файлов, зафиксированных в ранних проходах? Нужна commit history или полноценный clone.
- Что именно изменилось в commit `588b653` от 29 сентября 2025 и в соседних commits: это доработка после blog post, подготовка к публичной странице или обычный cleanup?
- Dynamic workflows in Claude Code появились уже после Klaus Kode. Есть ли у Quix follow-up, где они сравнивают свой external workflow engine with Claude Code native workflows, или проект остался на прежней архитектуре?
- Прямые URL изображений `KK2.png` и `KK3.png` найдены; остаётся проверить права, точное соответствие `KK2`/`KK3` сценам и пригодность для публикации.
- Можно ли открыть LinkedIn-пост Santiago Valdarrama полностью или найти его кросс-пост без login wall? Сейчас это только слабый поисковый сигнал.
- Почему integration page в одном месте говорит "Klaude Kode" с `d`? Это простая опечатка на продуктовой странице или след переименования/быстрой публикации?

## Синтез

Quix / Klaus Kode is a compact but very useful story because it refuses the obvious next step. When Claude Code did not reliably manage a multi-step integration workflow, Quix did not simply add a larger prompt or a larger MCP surface. The decisive move was to remove repeatable orchestration from the model and encode it as Python workflow state, phases, prompts, sandbox calls and deterministic API operations.

The technical lesson is sharp: Claude Code remains valuable for code generation, debugging and editing, but not every surrounding procedure should live in the context window. `WorkflowFactory`, `WorkflowContext`, prompt contracts, CLI path handling, file-backed logs, Quix Cloud sandbox and auto-debug menu make Klaus Kode a workflow system with an agent inside it, not an agent loosely told to remember the workflow. This makes it a strong story for the theme “sometimes the right answer to agent failure is more ordinary software”.
