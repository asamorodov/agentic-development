# Chapter VI — source register

Статус: обновлён после P30. Для каждого внешнего источника зафиксировано, как он реально использован в финальном тексте или почему оставлен за границей главы.

## Внутренние рабочие источники

| Источник | Роль в главе | Статус |
| --- | --- | --- |
| `P01.md` | Рамка главы и границы с V, VII, IX | использован |
| `P02.md` | Составной пример сбоя проектного интерфейса | использован |
| `P03.md` | Модель правил, состояния и маршрутов действия | использован |
| `P04.md` | Выбор внутренних материалов, story-якорей и Atlas donors | использован |
| `P05.md` | Gap-analysis и план внешнего поиска | использован |
| `P06.md` | Проверка первичных источников | использован |
| `P07.md` | Решение по каждому источнику | использован |
| `VI_context_working_state_interface_fragment_usage.md` | Решение о функциях A4/A6/C4 | использован |
| `VI_context_working_state_interface_story_anchors.md` | Решение о story-якорях | использован |
| `VI_context_working_state_interface_atlas_usage.md` | Решение о донорах Атласа | использован |
| `A6_execution_environment_distinctions.md` | Граница с IX, обвязка, инструменты, hooks/MCP/subagents как поверхность действия | использован |
| `A4_persistent_work_graph_boundary.md` | Граница с VII, состояние работы и PWG-мост | использован |
| `C4_execution_runtime_to_pwg.md` | Состояние запуска против состояния работы | использован |
| Статьи Атласа Kiro / Spec Kit / BMAD / GSD / PWG | Понятийные доноры по слоям интерфейса | использованы |
| Досье Kiro / Spec Kit / BMAD / GSD / PWG | Gap-check и резерв фактуры | использованы выборочно |

## Источники для обязательного встраивания

| Источник | URL | Что взять | Где использовать |
| --- | --- | --- | --- |
| Codex `AGENTS.md` | `https://developers.openai.com/codex/guides/agents-md` | instruction chain, scopes, override order, default size limit | rules layer |
| Claude Code memory / `CLAUDE.md` | `https://code.claude.com/docs/en/memory` | fresh session context; context not enforcement; `PreToolUse` as enforcement boundary | rules layer + boundary |
| Kiro Specs | `https://kiro.dev/docs/specs/` | `requirements.md` / `bugfix.md`, `design.md`, `tasks.md`, task status | working state |
| BMAD Getting Started | `https://docs.bmad-method.org/tutorials/getting-started/` | fresh chats per workflow, PRD/architecture/epics/stories, `sprint-status.yaml` | working state |
| BMAD Project Context | `https://docs.bmad-method.org/how-to/project-context/` | `project-context.md` as implementation guide | rule/state bridge |
| GSD Core | `https://github.com/open-gsd/gsd-core` | phase loop, fresh-context subagents, `STATE.md` / `CONTEXT.md`, verification | working state + bridge to VII |
| Codex Agent Skills | `https://developers.openai.com/codex/skills` | skills as reusable instructions/resources/scripts; platform-specific packaging not transferred into prose | action routes / skills subsection |
| Claude Code skills | `https://docs.anthropic.com/en/docs/claude-code/skills` | skills as reusable task procedures; platform-specific packaging not transferred into prose | action routes / skills subsection |
| Kiro Powers | `https://kiro.dev/docs/powers/` | dynamic capability loading, `POWER.md`, MCP config, context overload warning | action routes + MCP noise |
| Kiro Hooks | `https://kiro.dev/docs/hooks/` | event-triggered agent prompts / shell commands; pre/post tool/spec task events | boundary with execution |
| Claude Code Hooks | `https://code.claude.com/docs/en/hooks` | session/turn/tool lifecycle; `PreToolUse` / `PostToolUse` | boundary with execution |
| MCP intro | `https://modelcontextprotocol.io/docs/getting-started/intro` | MCP as connection to external systems/tools/workflows | instrumental surface |
| MCP tools specification | `https://modelcontextprotocol.io/specification/2025-06-18/server/tools` | validation, access control, confirmations, audit, sanitization | trust boundary, without IX deep dive |
| Claude Code subagents | `https://code.claude.com/docs/en/sub-agents` | custom subagents, separate instructions/tools/permissions/skills | action routes |
| Kiro subagents | `https://kiro.dev/docs/chat/subagents/` | separate context windows, result return, limits: no Specs/hooks in subagents | action routes + context isolation |

## Источники для выборочного использования

| Источник | URL | Что взять | Ограничение |
| --- | --- | --- | --- |
| AGENTS.md standard | `https://agents.md/` | `README` for agents as cross-tool convention | одна фраза, без отдельного разбора |
| `awesome-claude-skills` | `https://github.com/ComposioHQ/awesome-claude-skills` | signal that skills are collected and categorized as libraries | one sentence in skills subsection; no marketplace overview |
| Agent Skills Library | `https://mcpservers.org/agent-skills` | signal that reusable skills are distributed across agent ecosystems | one sentence in skills subsection; no catalog dump |
| Kiro Steering | `https://kiro.dev/docs/steering/` | steering files and `AGENTS.md` support | не повторять Kiro Atlas |
| Kiro MCP | `https://kiro.dev/docs/mcp/` | specialized tools/prompts/resources, `#` mention system, elicitation | кратко, если нужен пример MCP в IDE |
| Claude MCP | `https://code.claude.com/docs/en/mcp` | access to tools/databases/APIs, trust risks | не углублять security |
| Spec Kit GitHub | `https://github.com/github/spec-kit` | constitution/spec/plan/tasks/implement, `tasks.md` roadmap | не повторять главу V |
| Open GSD product site | `https://opengsd.net/` | explicit plans, clean execution contexts, verification | только как supporting link, primary лучше GitHub/docs |
| BMAD GitHub project-context explanation | `https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/explanation/project-context.md` | project rules/patterns/preferences; workflows loading context | использовать вместо docs-page только если нужна более точная формулировка |

## Источники, которые не использовать без дополнительного добора

| Источник | Решение |
| --- | --- |
| Mark Erikson / OpenCode exact config details | Не использовать как публичную продуктовую деталь без отдельного source pass. Внутренний story-anchor можно оставить общим примером сбоя интерфейса. |
| Mae Capozzi / InstructionsLoaded exact details | Не использовать как публичную деталь без отдельного source pass. Идею context-as-API можно передать через проверенные источники. |
| HumanLayer / Ronacher / Quix MCP-risk materials | Не нужны для VI, если текст не делает отдельный MCP-risk блок. Вероятнее оставить IX. |
| Secondary explainers по BMAD/GSD/Spec Kit | Не использовать как citation targets в финальной главе. |

## Правило использования в финальной главе

1. Каждая ссылка должна отвечать за конкретный механизм, а не за общий фон.
2. Внутренние досье не становятся публичными ссылками.
3. Если факт из story-реконструкции не подтверждён первичным источником, точную продуктовую деталь убрать или добрать источник.
4. Ссылки ставить рядом с первым введением механизма.
5. Не строить каталог инструментов: источник остаётся только если работает на rules, working state, action routes или boundary with execution.

## P11 usage note

После первой русской переписи публичные источники сохранены в основном тексте рядом с механизмами. Новых внешних источников P11 не добавлял. Основное изменение — язык и композиция: рабочие ярлыки `rules layer`, `working state`, `action routes`, `boundary with execution` переведены в естественные русские формулировки без потери функций источников.

## P12 usage note

Раздел о skills усилен на основе `https://code.claude.com/docs/en/skills`. Новых источников не добавлено. В тексте skill теперь трактуется как повторяемый проектный способ действия, а не как справочный файл. Зафиксированы риски: устаревание skill, неправильный выбор по похожему description и применение одной процедуры к разным фазам работы.

## P13 usage note

Раздел о hooks усилен на основе `https://kiro.dev/docs/hooks/` и `https://code.claude.com/docs/en/hooks`. Новых источников не добавлено. В тексте hooks теперь трактуются как точки автоматического вмешательства до закрепления ошибки в результате. Зафиксированы риски: чрезмерная жёсткость, ложная уверенность, устаревание и конфликт с человеческим решением.

## P14 usage note

Раздел о MCP усилен на основе `https://modelcontextprotocol.io/docs/getting-started/intro`, `https://code.claude.com/docs/en/mcp`, `https://kiro.dev/docs/mcp/`, `https://modelcontextprotocol.io/specification/2025-06-18/server/tools` и `https://kiro.dev/docs/powers/`. Новых источников не добавлено. MCP теперь описан как управляемый канал чтения, проверки и действия, который должен быть связан с процедурой и текущей задачей.

## P15 usage note

Раздел о subagents усилен на основе `https://kiro.dev/docs/chat/subagents/` и `https://code.claude.com/docs/en/sub-agents`. Новых источников не добавлено. В тексте subagent теперь раскрыт как отдельный рабочий контекст с входом, границей задания, инструментами и результатом, который должен быть связан с общим состоянием работы.

## P21 usage note

После P21 в основной текст добавлены точные внешние ссылки для story-материала, который был встроен в P19/P20.

Дополнительно использованы:

- Mark Erikson: `https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/`, `https://github.com/markerikson/opencode-config-example`, а также прямые ссылки на `config/AGENTS.md`, `devplans.ts`, `/context`, `/progress`, `orchestrator`, `reviewer`, `/subtask-complete`, `/subtask-resume`.
- Mae Capozzi: `https://maecapozzi.com/blog/building-a-multi-agent-orchestrator` для `InstructionsLoaded` и наблюдаемой загрузки инструкций.
- Matt Pocock: `https://github.com/mattpocock/skills`, `https://www.aihero.dev/5-agent-skills`, `handoff/SKILL.md`, `diagnose/SKILL.md`, `tdd/SKILL.md`.
- Armin Ronacher: `https://lucumr.pocoo.org/2025/6/12/agentic-coding/` и `https://lucumr.pocoo.org/2025/8/18/code-mcps/`.
- Stripe Minions: `https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents` и `https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2`.

Это отменяет раннее ограничение P07 для этих story-деталей: теперь точные детали, оставшиеся в главе, имеют рядом публичные ссылки. Ограничение сохраняется для неиспользованных деталей вроде DiffLoupe, Replay MCP, telemetry boilerplate, devbox-метрик и расширенного runtime/security-разбора.

## P22 usage note

После добавления ссылок P21 затронутые абзацы переписаны на более естественный русский язык. Источники сохранены рядом с фактами, но текст не превращён в обзор инструментов. Основные правки: меньше английского клея (`productive session`, `fresh chats`, `tool definitions`, `read-only lookup`), больше русских объяснений вокруг официальных терминов.

## P23 link-placement check

Проверено размещение ссылок в основной главе после P21/P22.

Результат:

- ссылки для новых story-источников стоят рядом с первым содержательным вводом материала;
- проверены Mark Erikson, Mae Capozzi, Matt Pocock, Armin Ronacher, Stripe Minions;
- исправлена техническая ошибка после русской переписи: URL Mark Erikson был повреждён заменой слова `workflow` в ссылке; восстановлен правильный адрес `https://blog.isquaredsoftware.com/2026/05/ai-thoughts-part-2-agent-workflow-tools/`;
- не найдено markdown-ссылок с пробелами или кириллицей в URL после исправления.

## P27 visual decision note

В главу вставлена собственная synthetic figure `fig-vi-project-interface-layers`. Внешний источник не нужен: фигура не заимствует чужую диаграмму и не изображает конкретный инструмент. Она визуально фиксирует композицию главы: человек/команда → проектный интерфейс агента → агентская сессия → проектные артефакты и внешние каналы.

Скриншоты Kiro, Claude, Stripe, Mark Erikson, Mae Capozzi и PWG/Beads отклонены как неподходящие для VI: они либо тянут главу в обзор инструментов, либо преждевременно раскрывают VII/IX.

## P30 final source audit

Финальная проверка потерь не выявила источников, которые должны были войти в главу и остались без места. Основные группы закрыты:

- правила и проектные инструкции: Codex `AGENTS.md`, `AGENTS.md` standard, Claude memory / `CLAUDE.md`, Kiro Steering;
- рабочее состояние: Kiro Specs, Erikson `dev-plans`, BMAD `project-context` / `sprint-status.yaml`, GSD Core, Spec Kit;
- маршруты действия: Claude Skills, Matt Pocock skills, MCP, Kiro Powers, Ronacher, Stripe Minions, Kiro / Claude subagents;
- граница с исполнением: Kiro Hooks, Claude Hooks, MCP tools specification;
- мост к VII: Persistent Work Graph назван только как следующий слой рабочего состояния.

Раннее ограничение P07 по Mark Erikson, Mae Capozzi, Matt Pocock, Armin Ronacher и Stripe изменено после P21: в итоговой главе оставлены только те детали, рядом с которыми добавлены публичные ссылки. Неиспользованные детали story-досье по-прежнему не перенесены.


## Skills lifecycle patch note

Раздел о skills усилен после ручной правки. Добавлены Codex Agent Skills и обновлённая документация Claude Code Skills как официальные источники общего понятия: skill рассматривается не через конкретный путь к файлу, а как переносимая процедура с назначением, условиями применения, шагами, входами, выходами и ограничениями.

Matt Pocock и открытые каталоги skills использованы для тезиса о библиотеке skills как новом слое практики: skills выбирают, устанавливают, адаптируют, обновляют и выводят из использования. Текст не превращён в обзор рынка и не переносит платформенную техническую раскладку Claude/Codex в главу.


## Skills expansion source pass note

Раздел `Skills: повторяемые процедуры как часть проекта` расширен после дополнительного внешнего поиска. Новые источники используются не для обзора рынка, а для четырёх функций: устройство skill как повторяемой процедуры, практические сценарии использования, библиотеки skills и риски выбора/доверия.

Дополнительно использованы:

- OpenAI Codex Agent Skills: `https://developers.openai.com/codex/skills` — skill как reusable workflow с инструкциями, ресурсами, optional scripts, progressive disclosure, explicit/implicit invocation, роль description.
- OpenAI Codex Best Practices: `https://developers.openai.com/codex/learn/best-practices` — когда повторяемую работу стоит превращать в skill, scoped-to-one-job, concrete use cases, inputs/outputs, examples of recurring jobs.
- OpenAI Codex reusable skills use case: `https://developers.openai.com/codex/use-cases/reusable-codex-skills` — примеры Buildkite, PR review comments, release notes, merge conflicts, frontend skill.
- OpenAI Codex customization: `https://developers.openai.com/codex/concepts/customization` — metadata, progressive disclosure, repo/user skills, skills plus MCP.
- OpenAI skills catalog: `https://github.com/openai/skills` — публичный каталог skills для Codex.
- Anthropic Agent Skills engineering post: `https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills` — procedural knowledge, organizational context, progressive disclosure, security considerations.
- Anthropic skills repository: `https://github.com/anthropics/skills` — примеры официальных skill sets и демонстрационных skills.
- Matt Pocock skills: `https://github.com/mattpocock/skills`, `https://www.aihero.dev/5-agent-skills-i-use-every-day` — практический набор skills для уточнения задачи, PRD, issues, TDD, архитектурного улучшения, handoff и диагностики.
- `awesome-claude-skills`: `https://github.com/ComposioHQ/awesome-claude-skills` — каталогизация skills по категориям.
- Agent Skills Library: `https://mcpservers.org/agent-skills` — примеры библиотечного слоя и публичных skills по провайдерам.
- `Agent Skills: A Data-Driven Analysis`: `https://arxiv.org/abs/2602.08004` — количественная картина публичных skills, концентрация сценариев, повторяемость намерений и риски действий с побочными эффектами.
- `How Well Do Agentic Skills Work in the Wild`: `https://arxiv.org/abs/2604.04323` — хрупкость пользы skills в реалистичных условиях поиска и выбора из большой коллекции.
- `Under the Hood of SKILL.md`: `https://arxiv.org/abs/2605.11418` — `SKILL.md` как operational text, влияющий на обнаружение, выбор, загрузку и доверие к skill.

Решение по границе: конкретные пути, синтаксис и platform-specific packaging не переносились в главу, потому что Codex, Claude Code и другие среды устроены по-разному. В текст перенесены общие свойства: назначение, условия применения, порядок работы, входы, выходы, ограничения, примеры, поддерживающие материалы, progressive loading, жизненный цикл и риски.


## MCP source expansion note

Раздел `MCP: управляемый доступ к внешнему миру` расширен после отдельного внешнего поиска. Новые источники используются для четырёх функций: объяснить внутренний смысл MCP как канала чтения и действия, показать разные классы серверов, объяснить необходимость узкого доступа под задачу и добавить security-границу без превращения VI в главу о sandbox/runtime.

Дополнительно использованы:

- MCP specification: `https://modelcontextprotocol.io/specification/2025-06-18` — базовое различение `resources`, `prompts`, `tools`.
- MCP Resources: `https://modelcontextprotocol.io/specification/2025-06-18/server/resources` — resources как данные и контекст.
- MCP Prompts: `https://modelcontextprotocol.io/specification/2025-06-18/server/prompts` — prompts как шаблоны сообщений и workflows.
- GitHub MCP: `https://github.com/github/github-mcp-server`, `https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp-in-your-ide/use-the-github-mcp-server` — репозитории, issues, pull requests, workflows.
- Figma MCP: `https://developers.figma.com/docs/figma-mcp-server/` — дизайн-контекст для generation from Figma design files.
- Playwright MCP: `https://github.com/microsoft/playwright-mcp` — браузерная автоматизация, snapshots, testing/data extraction.
- Chrome DevTools MCP: `https://github.com/ChromeDevTools/chrome-devtools-mcp` — debugging/performance/network/browser context.
- Stripe MCP: `https://docs.stripe.com/mcp` — Stripe API и knowledge base для платежных интеграций.
- Notion MCP: `https://developers.notion.com/guides/mcp/overview` — secure access to Notion workspace.
- Sentry MCP: `https://github.com/getsentry/sentry-mcp` — human-in-the-loop coding agents, developer workflows, debugging use cases.
- Context7: `https://github.com/upstash/context7` — up-to-date code documentation for prompts.
- MCP reference servers: `https://github.com/modelcontextprotocol/servers` — Filesystem, Git, Fetch, Memory and other reference access types.
- MCP Registry: `https://github.com/mcp` — signal that MCP servers are becoming searchable/discoverable infrastructure.
- MCP Security Best Practices: `https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices` — confused deputy, token passthrough, SSRF, session hijacking, local compromise, scope minimization.
- MCP at First Glance: `https://arxiv.org/abs/2506.13538` — empirical study of MCP server security and maintainability.
- MCPTox: `https://arxiv.org/abs/2508.14925` — tool poisoning in real MCP settings.
- VIPER-MCP: `https://arxiv.org/abs/2605.21392` — privileged operations and taint-style vulnerabilities in MCP servers.
- Prompts Don’t Protect: `https://arxiv.org/abs/2605.18414` — prompt restrictions are weaker than architectural tool access control.

Решение по границе: не переносить в главу установку серверов, transports, OAuth flow, JSON-RPC details, server config, platform-specific setup and full threat model. В основной текст перенесены свойства, нужные для главы VI: MCP как внешний канал, servers by task, examples by class, minimum necessary access, human confirmation, tool metadata risks and relationship with skills/working state.


## Дополнительная правка subagents после внешнего поиска

| Источник | URL | Что использовано | Где используется |
| --- | --- | --- | --- |
| Codex Subagents — concepts | `https://developers.openai.com/codex/concepts/subagents` | контекстное загрязнение, параллельные read-heavy задачи, summaries вместо промежуточного шума, осторожность с параллельными write-heavy изменениями, пример PR-review через security/test/maintainability subagents | раздел `Subagents: разные исполнители для разных частей задачи` |
| Codex Subagents — usage | `https://developers.openai.com/codex/subagents` | практическая форма запуска нескольких subagents и сборки результатов | раздел subagents, примеры ревью |
| Claude Code Subagents | `https://code.claude.com/docs/en/sub-agents` | отдельный контекст, собственные инструкции, ограничения инструментов, permissions, best practices и nested subagents | раздел subagents |
| Claude Agent SDK Subagents | `https://code.claude.com/docs/en/agent-sdk/subagents` | context isolation, parallelization, specialized instructions, tool restrictions | раздел subagents |
| Claude Code Agent Teams | `https://code.claude.com/docs/en/agent-teams` | отличие subagents от agent teams: subagents возвращают результат главному агенту, teams имеют общий список задач и прямую коммуникацию | раздел subagents, граница с настоящими командами агентов |
| Anthropic multi-agent research system | `https://www.anthropic.com/engineering/multi-agent-research-system` | orchestrator-worker pattern, parallel exploration, compression, cost/coordination limits, требования к постановке задачи subagent: цель, формат ответа, инструменты/источники, границы | раздел subagents, advanced orchestration |
| LangChain multi-agent patterns | `https://docs.langchain.com/oss/python/langchain/multi-agent` | supervisor pattern и context engineering как центральная задача многоагентного дизайна | раздел subagents |
| LangChain architecture comparison | `https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture` | различение supervisor/router/handoffs и условий, где уместен параллельный dispatch/synthesis | раздел advanced orchestration |
| Cognition — Don’t Build Multi-Agents | `https://cognition.ai/blog/dont-build-multi-agents` | предостережение против наивных multi-agent схем: потеря общего контекста, разные локальные предположения, сложность согласования | раздел рисков subagents |
| Claude Code design-space paper | `https://arxiv.org/abs/2604.14228` | subagent delegation with worktree isolation как часть более широкой архитектуры Claude Code наряду с MCP, skills, hooks, permissions и compaction | связка с проектным интерфейсом |
| Mark Erikson story | `../../../content/stories/10_mark_erikson_maximum_deep_reconstruction_connected.md` | малая обвязка с отдельными agents для ревью/документации/тестов, handoff-команды и защита ментальной модели | story-parallel в разделе subagents |
| Peter Steinberger story | `../../../content/stories/02_peter_steinberger_maximum_deep_dive_reconstruction_connected.md` | параллельные сессии, радиус воздействия, скепсис к театральным role-based subagents | story-parallel в разделе subagents |
| Simon Willison story | `../../../content/stories/03_simon_willison_agentic_research_reconstruction_connected.md` | scout agents, subagents как защита основного контекста и шумных проверок | story-parallel в разделе subagents |
| Jökull Sólberg story | `../../../content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md` | специализированные agents рядом с PR/CI/review loop и worktrees | story-parallel в разделе subagents |
| Jesse Vincent story | `../../../content/stories/06_jesse_vincent_agentic_workflow_reconstruction_connected.md` | Superpowers, subagent-driven execution, session-driver workers, выбор между тяжёлой оркестрацией и inline execution | story-parallel в разделе subagents |
