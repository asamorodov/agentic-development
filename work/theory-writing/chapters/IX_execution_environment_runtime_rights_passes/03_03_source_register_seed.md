# P03 — Первичный source register для главы IX

Статус: начальный реестр. Он фиксирует, какие материалы можно использовать, какую функцию они выполняют и где требуется повторное раскрытие первоисточника. Это не финальный список ссылок главы: после внешнего discovery он должен быть расширен и очищен.

## 1. Внутренние управляющие материалы

| Материал | Функция в главе | Статус использования |
|---|---|---|
| `PUBLIC_CONTRACT.md` | Задаёт режим package: глава IX, no-stage execution, без скрытого потолка объёма, выполнять только текущие рабочие листы | Использовать как рабочее ограничение, не цитировать в основном тексте |
| `SELECTED_INPUTS_MANIFEST.md` | Показывает весь включённый корпус: фрагменты A6/C4, Атлас, досье, истории, карты, ассеты | Использовать как check-list покрытия |
| `REPOSITORY_START_SNAPSHOT.md` | Восстанавливает состояние проекта и post-atlas режим | Использовать для ориентации, не переносить формулировки в главу |
| `work/discourse.md` | Общий контекст текущей теории и последних решений | Использовать для проверки, что глава соответствует принятой оси SDLC/change lifecycle |
| `work/theory-writing/WORKING_DOCUMENTS_MAP.md` | Карта рабочих документов и их ролей | Использовать как навигацию по corpus, не как публичный источник |
| `work/theory-writing/fragments/00_spine_map.md` | Главная ось: программное изменение проходит через намерение, спецификацию, состояние работы, исполнение, проверочный материал, принятие и последующее сопровождение | Использовать как композиционный backbone главы |
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md` | Непосредственный скелет главы IX: среда агента, harness, tools, permissions; четыре слоя | Использовать как структурное ограничение, не копировать стиль |
| `work/theory-writing/CORE_NODES_WRITING_PLAN.md` | Общие решения по writing packages и external discovery | Использовать для режима работы, не цитировать |

## 2. Карты маршрутизации и отчёты

| Материал | Функция в главе | Практическое решение |
|---|---|---|
| `POST_ATLAS_CHAPTER_LIST_AND_SCOPE_MAP.md` | Фиксирует главный вопрос IX: что делает действие агента ограниченным, наблюдаемым, возобновляемым и подотчётным | Держать вопрос главы; не уходить в каталог инструментов |
| `POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md` | Указывает обязательные входы IX: A6, C4, истории; GSD/BMAD/PWG/Gas Town as secondary donors; D3 discovery; asset-heavy | Использовать как coverage checklist |
| `POST_ATLAS_ATLAS_TO_CHAPTER_ROUTING_MAP.md` | Показывает, какие статьи Атласа работают как доноры и границы | Использовать GSD/BMAD/PWG/Gas Town как boundary donors |
| `POST_ATLAS_FRAGMENT_TO_CHAPTER_ROUTING_MAP.md` | Указывает A6/C4 as key inputs and границы с A4/A7/A8/A9 | Держать IX между runtime, evidence and authority |
| `POST_ATLAS_DOSSIER_TO_CHAPTER_GAP_MAP.md` | Подсказывает, какие досье могут добавить gap-check | Использовать только для проверки потерь и поиска первичных ссылок |
| `POST_ATLAS_STORY_ANCHOR_ROUTING_MAP.md` | Для IX перечисляет Arvid, HumanLayer, Mike, Armin, Stripe, Shopify | Использовать как story-anchor selection |
| `POST_ATLAS_EXTERNAL_SOURCE_DISCOVERY_MAP.md` | Профиль IX = D3; seed terms: LangGraph, Temporal, DBOS, Restate, HumanLayer, Sandvault, Codex/Claude docs, MCP/hooks/subagents | Обязательно расширить через внешний discovery/unfolding |
| `POST_ATLAS_VISUAL_CANDIDATE_ROUTING_MAP.md` | Предупреждает: IX asset-heavy, риск UI-tour | Визуальный слой решать отдельно; не вставлять картинки ради полноты |
| `POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md` | Общие правила chapter package: current-practice pass, source discovery, visual pass, style passes | Использовать как методологическое ограничение, не как источник содержания |

## 3. Главные внутренние содержательные фрагменты

| Материал | Что даёт IX | Ограничение |
|---|---|---|
| `A6_execution_environment_distinctions.md` | Четыре обязанности среды: граница исполнения, инструменты/наблюдение, workflow engine, platform agent | Главный донор, но его нельзя переписать как готовую главу |
| `A6_source_usage.md` | Реестр внешних ссылок по Sandvault/worktrees/HumanLayer/Ronacher/Roast/Quix/Stripe | При переносе фактов идти к первоисточникам |
| `A6_story_anchor_map.md` | Защищает от пересказа историй: каждый якорь связан с конкретным различением | Использовать для контроля плотности |
| `A6_figure_candidates.md` | Кандидаты: four-layer figure, Sandvault, HumanLayer harness, sandbox/permission boundary | Перед вставкой нужен visual/rights pass |
| `A6_open_questions.md` | Долги: secret/network threat boundary, observation vs evidence, минимальный стек, Stripe source status | Использовать как agenda for discovery |
| `A6_degradation_and_duplication_audit.md` | Фиксирует, где A6 не должен дублировать A7/C4/PWG/technical atlas | Использовать для anti-duplication check |
| `C4_execution_runtime_to_pwg.md` | Различение состояния запуска и состояния работы; durable execution vs PWG | Использовать как мост, не как повтор A6 |
| `C4_source_usage.md` | Реестр ссылок по durable execution, worktrees, Roast, Stripe, Beads | Использовать для initial external register |
| `C4_story_anchor_map.md` | Показывает, где C4 использует Mike/Stripe/Roast/Beads | Не давать C4 захватить главу IX |
| `C4_figure_candidates.md` | Visual candidates for runtime vs PWG boundary | Возможно использовать только если глава требует схемы runtime/work state |
| `C4_open_questions.md` | Долги: Claude/Codex worktrees source-pass, Stripe transcript status, asset-pass | Внести в discovery plan |
| `C4_degradation_and_duplication_audit.md` | Проверяет, что C4 не стал runtime-catalog | Использовать в финальном audit |

## 4. Атлас и методологические статьи

| Статья / материал | Возможная функция в IX | Уровень использования |
|---|---|---|
| `work/atlas/articles/gsd_open_gsd.md` | Process/runtime boundary, auto mode, browser proof, worktree strategy, gates, recovery | Вторичный donor; конкретные команды не разворачивать |
| `work/atlas/articles/bmad_method.md` | Boundary with process profile: roles, phases, story/sprint status, correct-course | Почти только граница с VIII |
| `work/atlas/articles/persistent_work_graph.md` | Boundary: runtime state vs durable work state; gates/evidence/prime | Важен для финального моста к VII/XI/XII |
| `work/atlas/articles/gas_town.md` | Boundary with organizational-operational lifecycle | Мост к X, не основной материал IX |
| `work/dossiers/GSD_METHOD_DOSSIER.md` | Deep quarry по GSD: `gsd-browser`, auto mode, worktree, MCP budget, gates, runtime health | Использовать для gap-check and primary-source lookup |
| `work/dossiers/BMAD_METHOD_DOSSIER.md` | Deep quarry по BMAD process mechanics | Только если требуется граница process/runtime |
| `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Deep quarry по work graph, gates, state | Использовать для проверки границы runtime/PWG |
| `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | Deep quarry по Beads/Gas Town | Не раскрывать в IX, кроме моста к X |

## 5. Истории и story dossiers

| История | Функция в IX | Публичные источники, которые нужно использовать при переносе фактов |
|---|---|---|
| `content/stories/04_arvid_kahl...` | Browser/log observation and safe loop | Нужны первичные ссылки из истории; внутреннюю историю не цитировать как источник факта |
| `content/stories/07_human_layer...` | Harness engineering, context firewall, MCP/tools pressure | HumanLayer “Skill Issue”; возможно HumanLayer screenshots/assets |
| `content/stories/08_mike_mcquaid...` | Sandvault, worktrees, maintainer policy | Mike McQuaid post; Sandvault repo; Git/Claude/Codex worktree docs; Homebrew policy if used |
| `content/stories/13_armin_ronacher...` and `ARMIN_RONACHER_STORY_DOSSIER.md` | Minimal harness, shell/log/browser, Pi, code over MCP catalog | Ronacher posts; Pi repo/docs |
| `content/stories/14_stripe_minions...` and `STRIPE_MINIONS_STORY_DOSSIER.md` | Platform agent, devbox, context analyzer, checks/judge/diagnose, PR path | Stripe blog Part 1/2; Stripe Sessions; AI Engineer transcript with caution; ChatPRD only if used as secondary practical material |
| `content/stories/15_shopify_roast...` and `SHOPIFY_ROAST_STORY_DOSSIER.md` | Executable workflow, cogs, repeat/replay, Boba, agent as workflow step | Shopify Engineering post; Shopify/roast README/tutorials; Doubrovkine post if used as external run example |

## 6. Внешние источники уже названные во внутренних материалах

### Execution boundary, sandbox and worktrees

| Источник | URL | Функция в главе | Действие |
|---|---|---|---|
| Mike McQuaid, “Sandboxes and Worktrees” | https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/ | Sandvault + worktrees as practical boundary of execution | Повторно открыть before final facts |
| Sandvault repository | https://github.com/webcoyote/sandvault | Отдельный macOS user, `sandbox-exec`, shared workspace, browser/iOS endpoints | Повторно открыть; использовать exact mechanics |
| Git worktree documentation | https://git-scm.com/docs/git-worktree | Canonical semantics of Git worktree | Использовать как stable support |
| Claude Code worktrees | https://code.claude.com/docs/en/worktrees | Claude worktree mechanics, setup and cleanup | Требуется актуальная проверка official docs |
| Codex Worktrees | https://developers.openai.com/codex/app/worktrees | Codex local/remote worktrees, Handoff, managed worktrees | Требуется актуальная проверка official docs |
| Homebrew CONTRIBUTING | https://github.com/Homebrew/brew/blob/main/CONTRIBUTING.md | Maintainer policy around AI-generated changes, if used | Скорее XII/authority; in IX only as boundary with acceptance |

### Harness, tools, MCP and local observation

| Источник | URL | Функция в главе | Действие |
|---|---|---|---|
| HumanLayer, “Skill Issue: Harness Engineering for Coding Agents” | https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents | `model + harness`; context, tools, MCP, skills, subagents, hooks, back-pressure | Основной external anchor; повторно открыть |
| Ronacher, “Agentic Coding Recommendations” | https://lucumr.pocoo.org/2025/6/12/agentic-coding/ | `make dev`, `make tail-log`, browser/logs, local scripts, permissions caveat | Основной anchor local harness |
| Ronacher, “Your MCP Doesn’t Need 30 Tools: It Needs Code” | https://lucumr.pocoo.org/2025/8/18/code-mcps/ | Code as programmable tool interface; critique of large MCP catalogs | Use in tools section |
| Ronacher, “Pi: The Minimal Agent Within OpenClaw” | https://lucumr.pocoo.org/2026/1/31/pi/ | Pi as minimal local harness | Проверить актуальность |
| Pi README | https://github.com/earendil-works/pi | `Read`/`Write`/`Edit`/`Bash`, extensions, local agent mechanics | Use as repo source |
| Pi compaction docs | https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/compaction.md | Session tree/compaction/state | Use only if needed; likely VI/C4 boundary |
| Quix, “Claude Code wouldn’t behave…” | https://quix.io/blog/claude-code-wouldnt-behave-so-i-built-a-workflow-engine-to-tame-it | MCP context cost, workflow engine around coding agent, cloud sandbox/logs | Use as domain runtime example |
| Klaus Kode `workflow_factory.py` | https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/workflow_factory.py | Source/Sink/Diagnose/Deployment/Monitoring phases | Use if code-level source remains needed |
| Klaus Kode `contexts.py` | https://github.com/quixio/klaus-kode-agentic-integrator/blob/main/workflow_tools/contexts.py | Serialized WorkflowContext: workspace, technology, schema, code_generation, deployment, credentials | Use if code-level source remains needed |

### Workflow runtime and durable execution

| Источник | URL | Функция в главе | Действие |
|---|---|---|---|
| Shopify Engineering, “Introducing Roast” | https://shopify.engineering/introducing-roast | Structured AI workflows; Boba; deterministic steps around agent | Основной Roast source |
| Shopify/roast README | https://github.com/Shopify/roast/blob/main/README.md | Ruby DSL/cogs: `cmd`, `agent`, `chat`, `ruby`, `map`, `repeat`, `call` | Current public API; repeat before final |
| Roast iterative workflows tutorial | https://github.com/Shopify/roast/blob/main/tutorial/08_iterative_workflows/README.md | `repeat`, `break!`, `next!`, outputs | Use for runtime control flow |
| Roast session resumption tutorial | https://github.com/Shopify/roast/blob/main/tutorial/02_chaining_cogs/session_resumption.rb | Session resumption | Use if chapter needs replay/resumption details |
| Roast Ruby docs | https://rubydoc.info/github/Shopify/roast | API-level support if needed | Optional |
| Doubrovkine, “Executing Structured A.I. Workflows with Shopify Roast” | https://code.dblock.org/2025/05/10/executing-structured-ai-workflows-with-shopify-roast.html | External hands-on run; configuration/log/report | Optional practical source |
| LangGraph persistence | https://docs.langchain.com/oss/python/langgraph/persistence | Durable graph/thread/checkpoint concepts | External discovery required; use conceptually, not catalogue |
| LangGraph interrupts | https://docs.langchain.com/oss/python/langgraph/interrupts | Human-in-the-loop interruption/resume | Use only if helpful for approval/runtime distinction |
| Temporal AI cookbook: human-in-the-loop Python | https://docs.temporal.io/ai-cookbook/human-in-the-loop-python | Durable workflow + human interruption | Use for durable execution language |
| DBOS Transact TS | https://github.com/dbos-inc/dbos-transact-ts | Durable execution/runtime state in code | Needs current docs/source check |
| Restate durable execution | https://docs.restate.dev/concepts/durable_execution | Durable execution, retries, state | Strong candidate for conceptual runtime passage |
| Pydantic AI durable execution overview | https://pydantic.dev/docs/ai/integrations/durable_execution/overview/ | Durable agent execution integrations | Optional, if it sharpens current practice |

### Platform agent and enterprise workflow

| Источник | URL | Функция в главе | Действие |
|---|---|---|---|
| Stripe Minions Part 1 | https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | One-shot coding agents, PR path, human review | Повторно открыть; cite only visible text |
| Stripe Minions Part 2 | https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2 | Infrastructure/devbox/blueprints/scoped context, if visible | Повторно открыть; watch extraction gaps |
| AI Engineer Singapore Mark Doyle transcript | https://aie-sg-day1.vercel.app/ | Devbox scale, analyzer/checks/judge/diagnose cycle | Use cautiously as curated transcript, not official Stripe spec |
| Stripe Sessions 2026 Developer Keynote | https://stripe.com/sessions/2026/developer-keynote | Current official framing of developer agents and human control | Use only for high-level current Stripe context |
| Stripe integration benchmark | https://stripe.com/blog/can-ai-agents-build-real-stripe-integrations | Evidence package / benchmark context | More XI/C4 than IX; optional |
| Stripe Selective Test Execution | https://stripe.dev/blog/selective-test-execution-at-stripe-fast-ci-for-a-50m-line-ruby-monorepo | CI substrate in large monorepo | Keep as background; likely not needed in IX |
| ChatPRD workflow article | https://www.chatprd.ai/how-i-ai/workflows/how-to-automate-code-generation-from-a-slack-message-into-a-pull-request | Secondary practical view of Slack→PR flow | Use only if clearly marked as secondary |

### PWG / Beads boundary sources

| Источник | URL | Функция в главе | Действие |
|---|---|---|---|
| Beads gate CLI | https://gastownhall.github.io/beads/cli-reference/gate | Gate as work-state/acceptance boundary | Mostly VII/X, only bridge in IX |
| Beads prime CLI | https://gastownhall.github.io/beads/cli-reference/prime | Rehydration/prime as work-state recovery | Mostly VII/X, not runtime |
| Beads dependencies docs | https://github.com/gastownhall/beads/blob/main/docs/DEPENDENCIES.md | Work item dependencies | Boundary source only |

## 7. External discovery targets not yet resolved by internal register

These are not claims yet; they are search targets for later pass:

1. OpenAI/Codex current docs: sandbox, approvals, permissions, tools, browser/DevTools, hooks, MCP, AGENTS/project configuration.
2. Anthropic/Claude Code current docs: permissions, hooks, subagents, MCP, worktrees, browser/devtools support, `dangerously-skip-permissions` boundaries.
3. MCP official/security guidance: tool descriptions, prompt injection, remote server trust, data access and approvals.
4. Current LangGraph/Temporal/DBOS/Restate docs that sharpen durable execution without turning IX into an orchestration overview.
5. Security guidance on secrets/network/production-like environments for coding agents.

## 8. Provenance rule for future draft

In the main chapter, internal files may determine what to say, but public claims about tools, commands, numbers, product behavior, screenshots and repository mechanics must cite the public source at the point of introduction. If a detail is present only in an internal story or dossier and the primary source cannot be reopened, either omit it from the main chapter or mark it as unresolved in source usage.
