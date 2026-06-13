# kiro_specs — source usage

Статус: `P26_guarded_final_style_current`. Файл синхронизирован с текущей статьёй `kiro_specs.md` после problem-first перестройки P22, стилевого аудита P24, выборочной правки P25 и guarded final style P26. В P26 новые внешние страницы не открывались и новые фактические утверждения не добавлялись; таблица ниже фиксирует фактические публичные источники, на которые сейчас опирается статья.

## Принцип использования источников

Публичная статья ссылается на первичные страницы Kiro/Fowler, а не на рабочие досье. Внутренние C5/A10 и соседние материалы используются только как read-only редакционная карта: они помогают держать границы, но не являются публичными citation targets и не создают отдельного общего долга синхронизации C5/A10.

## Текущая карта публичных источников

| Группа источников | URL / страницы | Что поддерживает в статье | Где используется |
| --- | --- | --- | --- |
| Общий SDD-контекст | `https://martinfowler.com/articles/exploring-gen-ai.html`; локальный файл `content/assets/theory-images/fowler-sdd-overview.png` | Широкий фон SDD: агент, долговременная память, specs. Не является доказательством Kiro UI. | `Где Kiro находится...`, figure `fig-general-sdd-context`. |
| Specs / Feature Specs | `https://kiro.dev/docs/specs/`; `https://kiro.dev/docs/specs/feature-specs/` | Specs как рабочий режим; `.kiro/specs/{spec-name}/requirements.md`, `design.md`, `tasks.md`; approvals; task execution. | Вступление; Feature Specs; задачи; практический критерий. |
| Requirements-First / Design-First | `https://kiro.dev/docs/specs/feature-specs/requirements-first/`; `https://kiro.dev/docs/specs/feature-specs/tech-design-first/` | Два входа в Feature Spec; EARS; discrete trackable tasks; design-first порядок. | Feature Specs; таблица четырёх входов. |
| Specs Best Practices / First Project | `https://kiro.dev/docs/specs/best-practices/`; `https://kiro.dev/docs/getting-started/first-project/` | Sync Files; несколько specs; импорт существующих требований через MCP/репозиторный файл; генерация steering из проекта; ограничение на смену workflow. | Feature Specs; контекст; end-to-end путь; границы применения. |
| Vibe vs Spec sessions | `https://kiro.dev/docs/chat/vibe/` | Различение Vibe session и Spec session; выбор режима для сложной работы. | Методологическое позиционирование; практический критерий. |
| Bugfix Specs | `https://kiro.dev/docs/specs/bugfix-specs/` | `bugfix.md`; current/expected behavior; reproduction steps; unchanged behavior; convergence to `design.md`/`tasks.md`. | Раздел Bugfix Specs; таблица входов. |
| Quick Plan | `https://kiro.dev/docs/specs/quick-plan/`; `https://kiro.dev/blog/faster-smarter-specs/` | Укороченный режим; предварительные вопросы; создание `requirements.md`, `design.md`, `tasks.md` без отдельных phase approvals; partial regeneration; parallel task execution waves. | Quick Plan; задачи; external figures `fig-kiro-quick-plan-candidate`, `fig-kiro-parallel-task-waves-candidate`. |
| Analyze Requirements / Deep Spec Analysis | `https://kiro.dev/docs/specs/analyze-requirements/`; `https://kiro.dev/blog/deep-spec-analysis/` | Анализ существующих требований/документов/кода; gaps/ambiguities/contradictions; refinement → autoformalization → logical analysis; человеческое решение по вопросам. | Analyze Requirements; end-to-end путь; границы применения; figure `fig-kiro-deep-spec-analysis-candidate`. |
| Task execution / Run all Tasks / home demo | `https://kiro.dev/`; `https://kiro.dev/blog/run-all-tasks/`; `https://kiro.dev/blog/faster-smarter-specs/`; `https://kiro.dev/docs/specs/best-practices/` | Task status surface; `Start task`, `Task in progress`, `Task completed`, `View changes`, `View execution`; Run all Tasks; dependency waves; обязательные/необязательные задачи. | Feature lifecycle; задачи как единица исполнения; figures `fig-kiro-task-status-ui-candidate`, `fig-kiro-parallel-task-waves-candidate`. |
| Hooks / Autopilot / Checkpoints | `https://kiro.dev/docs/hooks/`; `https://kiro.dev/docs/hooks/types/`; `https://kiro.dev/docs/chat/autopilot/`; `https://kiro.dev/docs/chat/checkpoints/` | Pre/Post Task Execution; Pre/Post Tool Use; категории `spec`, `@mcp`, `@powers`, `write`, `shell`; Autopilot/Supervised; restore/revert and limitations. | Hooks/Supervised/checkpoints; границы применения. |
| Steering / chat context | `https://kiro.dev/docs/steering/`; `https://kiro.dev/docs/chat/`; `https://kiro.dev/docs/chat/context/` | `.kiro/steering/`; `product.md`, `tech.md`, `structure.md`; `always/fileMatch/manual/auto`; workspace/global priority; `AGENTS.md`; `#spec:user-authentication`. | Контекст; Feature lifecycle; end-to-end путь. |
| MCP / Powers | `https://kiro.dev/docs/mcp/`; `https://kiro.dev/docs/mcp/configuration/`; `https://kiro.dev/docs/mcp/usage/`; `https://kiro.dev/docs/powers/`; `https://kiro.dev/docs/powers/create/` | MCP tools/prompts/resources; workspace/user `mcp.json`; `autoApprove`, `disabledTools`, confirmations, elicitation; Powers as package of `POWER.md`, MCP config, steering/hooks. | MCP и Powers; контекст; governance boundary. |
| Correctness / PBT | `https://kiro.dev/docs/specs/correctness/`; `https://kiro.dev/changelog/ide/0-6` | Natural-language spec/EARS → executable properties; generated cases; failure scenarios; limits of PBT evidence. | PBT section; evidence boundary; figure `fig-kiro-pbt-candidate`. |
| CLI | `https://kiro.dev/blog/introducing-kiro-cli/`; `https://kiro.dev/docs/cli/steering/`; `https://kiro.dev/docs/cli/custom-agents/`; `https://kiro.dev/docs/cli/custom-agents/configuration-reference/`; `https://kiro.dev/docs/cli/headless/`; `https://kiro.dev/docs/cli/chat/subagents/`; `https://kiro.dev/docs/cli/mcp/registry/` | Shared `.kiro` config; steering/MCP in CLI; custom agents/tools/resources; `--no-interactive`, `--trust-tools`, `--require-mcp-startup`; CLI subagents; registry constraints. | CLI section; governance/MCP boundaries. |
| IDE subagents | `https://kiro.dev/docs/chat/subagents/` | IDE subagents as neighboring executors; important limit: no Specs access and Hooks do not trigger. | Subagents section; границы применения; figure `fig-kiro-subagents-boundary-candidate`. |
| Kiro Web | `https://kiro.dev/docs/web/`; `https://kiro.dev/docs/web/autonomous-mode/`; `https://kiro.dev/docs/web/using-the-agent/creating-tasks/`; `https://kiro.dev/blog/introducing-kiro-web/`; `https://kiro.dev/docs/web/identity-center/`; `https://kiro.dev/docs/web/sandbox/mcp/` | Web Preview autonomous PR cycle; tasks/PRs/review; steering; planned Web Specs; identity-center constraints; Web MCP sandbox/stdin boundary. | Web Preview section; governance boundary; figure `fig-kiro-web-boundary-candidate`. |
| Enterprise governance / monitoring | `https://kiro.dev/docs/enterprise/governance/`; `https://kiro.dev/docs/enterprise/governance/model/`; `https://kiro.dev/docs/enterprise/governance/mcp/`; `https://kiro.dev/docs/enterprise/governance/api-keys/`; `https://kiro.dev/docs/enterprise/governance/web-tools/`; `https://kiro.dev/docs/enterprise/monitor-and-track/`; `https://kiro.dev/docs/enterprise/monitor-and-track/user-activity/`; `https://kiro.dev/docs/enterprise/monitor-and-track/prompt-logging/` | Модели, MCP registry, API keys, web tools; monitoring dashboard, user activity, prompt logging, CloudTrail/CloudWatch. | Enterprise governance/monitoring; policy-vs-evidence table. |

## Внутренний контекст

| Внутренний вход | Текущая роль после P23 |
| --- | --- |
| C5 technical atlas / concept-atlas map | Read-only рамка standalone concept-first статьи и границ с соседними методами. Не требует отдельного sync-долга. |
| A10 mode-selection map | Read-only рамка для практического критерия выбора Vibe / Quick Plan / Feature Spec / Bugfix Spec. Не требует отдельного sync-долга. |
| Соседние досье Spec Kit, SPDD, Constitutional SDD, TDAD, ADR, PWG | Использованы только для отрицательных границ; публичные ссылки на них не добавляются в статью Kiro Specs. |

## P23 sync note

- Source usage теперь отражает фактические URL и фигуры текущей статьи, включая Fowler/SDD local asset.
- Первичный P01-статус снят; pass-by-pass log не используется как coverage matrix.
- Реальные долги перенесены в `kiro_specs_open_questions.md`: свежесть Web/CLI/enterprise docs, task status persistence, PBT UI/defaults, prompt logging/data protection и asset rights/freshness.
## P24 style-audit note

No source facts or citation targets changed in P24. The article removed remaining public style defects such as internal C5 wording in the theory paragraph, heavy headings and pseudo-terms, while preserving all URLs, source titles, file paths and product labels.
## P25 selective rewrite note

No source facts, URL targets or citation groupings changed in P25. Edits were style-only: they removed meta phrasing and over-compressed formulations while preserving all Kiro/Fowler source links and product labels.

## P26 guarded final style note

No source facts, URL targets, citation groupings, commands, paths, limits or product labels changed in P26. The pass only made final human-style adjustments in the intro, scope, Feature Specs, Analyze Requirements, hooks, MCP, CLI/Web, theory and boundary sections.
