# P03 — начальный source register для главы X

Этот register фиксирует источники, которые уже входят в пакет и могут питать главу X. Он не заменяет будущий source-restoration pass. Внешние ссылки ниже перенесены из уже собранных source maps, статей Атласа и досье; новые внешние источники на этом проходе не открывались.

## 1. Управляющие внутренние источники

| Источник | Функция в главе | Как использовать | Риск |
| --- | --- | --- | --- |
| `PUBLIC_CONTRACT.md` | Открытый контракт пакета: глава X о переходе от отдельных агентских потоков к многоагентной рабочей среде на Gas Town/Beads. | Удерживать границы пакета и отсутствие скрытого лимита объёма. | Не цитировать и не переносить служебные формулировки в публичный текст. |
| `SELECTED_INPUTS_MANIFEST.md` | Полный список включённых входов и локальных assets. | Проверять, что глава использует только реально доступные материалы; сверять visual candidates. | Манифест не говорит, что все inputs равноценны. |
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md` | Верхний тезис главы X и мост к XI. | Писать X как организационно-операционный жизненный цикл, не как интерфейсный обзор Gas Town. | Может быть слишком сжатым; фактуру брать из Атласа/досье. |
| `work/theory-writing/fragments/00_spine_map.md` | Сквозная ось lifecycle-of-change. | Держать переход от рабочего состояния и исполнения к потоку многих работ. | Не вставлять таблицу оси повторно без нужды. |
| `work/theory-writing/CORE_NODES_WRITING_PLAN.md` | Порядок post-atlas writing: skeleton/fragments/Atlas/dossiers/external discovery. | Использовать как контрольный рабочий протокол. | Не превращать в публичную аргументацию. |
| `work/theory-writing/WORKING_DOCUMENTS_MAP.md` | Карта актуальных документов, правила overlay/delta, визуальные и терминологические статусы. | Проверять source precedence, assets, companion-файлы, статус канонических материалов. | Файл длинный; читать целевые секции, не весь подряд ради симметрии. |
| `REPOSITORY_START_SNAPSHOT.md` / `REPOSITORY_AGENTS_SNAPSHOT.md` | Восстановление рабочего контекста и общие правила работы с репозиторием. | Использовать как служебный контекст. | Не цитировать в главе. |

## 2. Основные синтетические фрагменты

| Источник | Функция в главе | Что переносить | Что не переносить |
| --- | --- | --- | --- |
| `work/theory-writing/fragments/B3_gas_town_beyond_pwg.md` | Главный донор аргумента: Gas Town как слой организации сверх PWG. | Граница «PWG продолжает работу; Gas Town продолжает организацию многих работ»; роли как lifecycle-функции; проблема видимости, обслуживания, backpressure and service agents. | Не копировать структуру B3 целиком; не переносить готовые фразы без переписи. |
| `work/theory-writing/fragments/B3_source_usage.md` | Provenance map для B3. | Первичные ссылки Gas Town/Beads, уже отобранные для фактуры. | Не считать, что все ссылки актуальны без source-restoration. |
| `work/theory-writing/fragments/B3_story_anchor_map.md` | Карта story anchors для Gas Town. | Ограниченно использовать Jökull/HumanLayer и старый baseline как anti-degradation. | Не расширять X в обзор harness or PR evidence. |
| `work/theory-writing/fragments/B3_figure_candidates.md` | Visual candidates для B3. | Проверить, какие Gas Town / Beads visuals уже локализованы и какие остаются external candidates. | Не превращать внешние картинки в synthetic text diagrams. |
| `work/theory-writing/fragments/B3_open_questions.md` | Открытые вопросы B3. | Использовать для проверки, где глава может быть слишком tool-specific или слишком восторженной. | Не тащить все старые рабочие сомнения в публичный текст. |
| `work/theory-writing/fragments/B3_degradation_and_duplication_audit.md` | Audit against duplication/degradation. | Проверять, что глава не повторяет PWG, Gas Town article or process profile catalog. | Не использовать как публичный источник. |
| `work/theory-writing/fragments/C2_pwg_to_process_profiles.md` | Граница PWG / process profiles / Gas Town. | Процесс становится рабочим только через последствия в состоянии; roles/phases without state transitions are theater. | Не уходить в GSD/BMAD comparison. |
| `work/theory-writing/fragments/C2_source_usage.md` / companion files | Provenance and story anchors for C2. | Уточнить process-profile boundary and duplication risks. | Не расширять главу VIII внутри X. |
| `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` | Граница runtime / PWG / operational flow. | Запуск и след не равны рабочему состоянию; durable execution differs from durable work and organizational flow. | Не превращать X в главу IX about runtime/tools. |
| `work/theory-writing/fragments/C4_source_usage.md` / companion files | Provenance and story anchors for C4. | Проверить durable-execution boundary and visual risks. | Не открывать полный landscape runtime tools в X. |

## 3. Атласные статьи

| Источник | Функция в главе | Использование |
| --- | --- | --- |
| `work/atlas/articles/gas_town.md` | Главный concept-first baseline по Gas Town/Beads. | Брать точные различения: one chat is insufficient; two-level Beads; roles as lifecycle functions; delivery loop; queue/backpressure; observability; recovery; service work; limits. |
| `work/atlas/articles/gas_town_source_usage.md` | Карта внешних источников, реально использованных в статье. | Использовать как seed для source restoration и inline provenance в будущей главе. |
| `work/atlas/articles/gas_town_theory_links.md` | Связь Gas Town со сквозной теорией. | Проверить мосты: state, process, runtime, visibility/evidence, authority, repair. |
| `work/atlas/articles/gas_town_image_plan.md` | Visual dispositions for Gas Town article. | Решить, какие локальные assets могут войти в X. |
| `work/atlas/articles/gas_town_external_image_queue.md` | Очередь внешних изображений. | Сохранять для asset-pass, не вставлять как готовое. |
| `work/atlas/articles/gas_town_open_questions.md` | Нерешённые вопросы статьи. | Проверить, где у X риск устаревшей фактуры или чрезмерной детализации. |
| `work/atlas/articles/persistent_work_graph.md` | Нижний слой: PWG and Beads as durable work state. | Использовать только для границы с VII and Beads/PWG reminder. |
| `work/atlas/articles/persistent_work_graph_source_usage.md` | PWG source map. | Проверить Beads facts and boundary with Gas Town. |
| `work/atlas/articles/persistent_work_graph_theory_links.md` | Теоретическая связь PWG with lifecycle. | Использовать для формулы перехода from durable work to organizational flow. |
| `work/atlas/articles/persistent_work_graph_image_plan.md` / external queue | Visual candidates for PWG. | Использовать `beads-task-graph-memory.svg` only if needed as lower-layer reminder. |

## 4. Досье

| Источник | Функция в главе | Особые материалы |
| --- | --- | --- |
| `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | Полный quarry по Gas Town/Beads. | Beads as Dolt-backed work state; `bd prime`; `bd gate`; `bd mail`; `bd hook`; `bd pin`; molecules/formulas/wisps; two-level Beads; roles; `Mayor`; service agents; queue/backpressure; polecat lifecycle; risks and operation-log gap; visual candidates. |
| `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Проверка нижней границы PWG. | Durable identity; dependencies; ready queue; owner/claim; gate; prime/recovery; source/intermediate artifact state; parallelism boundary; failure modes. |
| `work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md` | Дополнительная фактура по Stripe Minions. | Platform-level routing, devbox, analyzer, Toolshed/MCP, blueprint, coding/check/judge loop, PR flow. |
| `work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md` | Дополнительная фактура по Roast. | Executable workflow, YAML/Ruby DSL, `cmd`/`chat`/`agent`, `map`, `repeat`, continue/resume. |

## 5. Истории корпуса

| Источник | Функция в главе | Использовать как | Ограничение |
| --- | --- | --- | --- |
| `content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md` | Малый практический пример операционной петли после PR. | `/babysit-pr`, CI waiting, Greptile/Codex review signals, `Fix / Dismiss / Escalate`, iteration limit, ready-to-merge criteria. | Не уходить в XI: review/evidence are operating signals in X. |
| `content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md` | Платформенный масштаб агентской работы. | Slack → emoji/repository routing → isolated devbox → blueprint/analyzer/tools → checks/judge → PR/review. | Не строить аргумент на PR/week figures без fresh check. |
| `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md` | Агент как шаг исполняемого рабочего процесса. | Workflow as file/versioned artifact; deterministic-agent sandwich; `agent` cog beside `cmd`/`chat`; resume/continue; workflow outputs. | Roast is not many-work organizational city; keep it as adjacent workflow anchor. |
| `content/stories/11_mae_capozzi_maximum_deep_reconstruction_connected.md` | Близкий non-Gas-Town пример orchestration/observability. | `hub-team` phases, process spawn, timeouts, worktrees, checkpoints, `TRACEPARENT`, Honeycomb trace and team observability. | Не уводить X в pure telemetry or Chapter IX runtime. |

## 6. Внешние источники — seed register

### 6.1. Gas Town

| Внешний источник | Ссылка | Функция в главе | Проверка нужна? |
| --- | --- | --- | --- |
| Gas Town README | https://github.com/gastownhall/gastown | Gas Town as system for multiple coding agents; basic loop; Problems View / `gt feed --problems`; You → Mayor → Convoy → Agent → Hook. | Да, source-restoration for current wording. |
| Welcome to Gas Town — Steve Yegge | https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 | Conceptual and authorial framing: chaotic/frontier nature, intended audience, role culture, agent-not-session, GUPP/hook. | Да, особенно не использовать as current implementation source. |
| Gas Town Docs | https://docs.gastownhall.ai/ | Role/reference surface, Mayor/Hub, routing and operational overview. | Да. |
| Gas Town Reference | https://docs.gastownhall.ai/reference/ | Reference-level details. | Да. |
| Gas Town architecture docs | https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md | `Town`/`Rig`, two-level state and architecture. | Да. |
| Mayor role template | https://github.com/gastownhall/gastown/blob/main/internal/templates/roles/mayor.md.tmpl | `bd create`, `gt sling`, filed/slung discipline, role accountability. | Да; internal template, cite carefully. |
| Gas Town mail protocol | https://github.com/gastownhall/gastown/blob/main/docs/MAIL_PROTOCOL.md | `POLECAT_DONE`, `MERGE_READY`, `MERGED` and typed feedback. | Да; B3 notes possible replacement by polecat lifecycle source. |
| Polecat lifecycle patrol | https://github.com/gastownhall/gastown/blob/main/docs/design/polecat-lifecycle-patrol.md | Mail-based per-rig channel, `MERGE_FAILED`, `GUPP_VIOLATION`, `ORPHANED_WORK`, patrol/recovery. | Да, likely stronger current source than old mail protocol. |
| Escalation protocol | https://github.com/gastownhall/gastown/blob/main/docs/design/escalation.md | Agent → Deacon → Mayor → Overseer escalation, stale detection, severity routing. | Да. |
| Gas Town CHANGELOG | https://github.com/gastownhall/gastown/blob/main/CHANGELOG.md | Queue/backpressure, heartbeat, merge queue, Dashboard, `FIX_NEEDED`, `awaiting_verdict`, pressure checks. | Да; version-sensitive. |
| Gas Town Glossary | https://github.com/gastownhall/gastown/blob/main/docs/glossary.md | MEOW, Hook, Convoy, Wisp, Seance/Patrol vocabulary. | Да; glossary may move/change. |
| Gas Town Scheduler design | https://github.com/gastownhall/gastown/blob/main/docs/design/scheduler.md | Ready work vs safe dispatch, `gt sling --queue`, `max_polecats`, `batch_size`, `spawn_delay`, circuit breaker. | Да; design doc. |
| Gas Town discussion #363 | https://github.com/gastownhall/gastown/discussions/363 | Operation-log gap / possible append-only operation log. | Да; discussion only, not implemented fact. |
| HN discussion on Welcome to Gas Town | https://news.ycombinator.com/item?id=46458936 | External perception: conceptual overload, merge/review bottleneck, skepticism. | Optional; weak source, likely not public chapter. |

### 6.2. Beads

| Внешний источник | Ссылка | Функция в главе | Проверка нужна? |
| --- | --- | --- | --- |
| Beads Documentation | https://gastownhall.github.io/beads/ | Base docs for Beads as task/work state layer. | Да. |
| Beads Architecture | https://gastownhall.github.io/beads/architecture | Dolt-backed source of truth, JSONL as export, boundaries of use. | Да. |
| Beads Quick Start | https://gastownhall.github.io/beads/getting-started/quickstart | Minimal command surface and onboarding. | Optional, only if command examples used. |
| Beads CLI Reference | https://gastownhall.github.io/beads/cli-reference | Command surface. | Optional. |
| `bd prime` | https://gastownhall.github.io/beads/cli-reference/prime | Compact agent-oriented rehydration. | Да. |
| `bd gate` | https://gastownhall.github.io/beads/cli-reference/gate | Durable gate conditions. | Да if gates mentioned. |
| Beads Routing | https://gastownhall.github.io/beads/multi-agent/routing | Prefix routing and route maps. | Да if routing explained. |
| Beads multi-agent coordination | https://gastownhall.github.io/beads/multi-agent/coordination | `bd pin`, `bd hook`, handoff, fan-out/fan-in, file reservations. | Да. |
| Beads Workflows | https://gastownhall.github.io/beads/workflows | Formula/Molecule/Wisp family. | Optional; avoid workflow-engine detour. |
| Beads Molecules | https://gastownhall.github.io/beads/workflows/molecules | Durable workflow instances. | Optional. |
| Beads Wisps | https://gastownhall.github.io/beads/workflows/wisps | Lightweight episodic steps. | Optional. |
| Beads Codex Integration | https://gastownhall.github.io/beads/integrations/codex | SessionStart/PreCompact/PostCompact/UserPromptSubmit and recovery through lifecycle hooks. | Да if compaction/recovery described. |
| Beads Troubleshooting | https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md | Infrastructure risk: doctor, debug flags, sync/hash mismatch, sandbox. | Optional, for cost/limits paragraph. |
| Beads Releases | https://github.com/gastownhall/beads/releases | Version-sensitive release/sync risks. | Optional, only if release-gating discussed. |
| DoltHub: Common Beads Classic Workflows | https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/ | Dolt-backed workflows, multi-clone visibility, sync tradeoffs. | Optional, not central. |

### 6.3. Story-source anchors already embedded in stories

These sources are already represented inside the story reconstructions. Use the story files as the immediate internal source; reopen external pages only if the chapter uses a precise public claim.

| Story | External anchors in story | Likely X use |
| --- | --- | --- |
| Jökull Sólberg | “How I Use Claude Code”, “Babysitting PRs With Claude Code”, Greptile/Codex review/CI examples as embedded in `content/stories/05...` | PR babysitting as small operating loop. |
| Stripe Minions | AI Engineer Singapore talk, ChatPRD “How Stripe's AI Minions Ship 1,300 PRs Weekly from a Slack Emoji”, related workflow page, Stripe internal platform details as embedded in `content/stories/14...` | Platform-level routing and workflow, not headline PR numbers. |
| Shopify Roast | Shopify Engineering “Introducing Roast”, Shopify/roast README, GitHub releases, RubyDoc snapshot, Doubrovkine external run as embedded in `content/stories/15...` | Agent step inside executable workflow. |
| Mae Capozzi | Mae blog on multi-agent orchestrator, Honeycomb posts, LinkedIn notes as embedded in `content/stories/11...` | Multi-agent process phases, trace, worktrees, timeouts, team observability. |

## 7. Local visual sources

| Asset | Function in X | Initial disposition |
| --- | --- | --- |
| `content/assets/theory-images/gastown-architecture.svg` | Architecture boundary: Gas Town as upper operational environment around PWG/Beads. | Strong candidate for inline figure. |
| `content/assets/theory-images/gastown-basic-workflow.svg` | Basic path from human request to Mayor/Convoy/Agent/Hook/completion. | Candidate if chapter needs delivery-loop visual. |
| `content/assets/theory-images/gastown-mayor-hub.webp` | Human visibility / problem surface. | Candidate, but avoid UI tour. |
| `content/assets/theory-images/beads-task-graph-memory.svg` | Lower-layer Beads/PWG reminder. | Use only if not duplicating chapter VII. |
| `content/assets/atlas-images/gas-town/gastown-pressure-to-mechanism-stack.svg` | Pressure-to-mechanism stack from Gas Town atlas. | Candidate for concise chapter-specific visual. |
| `content/assets/atlas-images/gas-town/gastown-two-tier-beads-flow.svg` | Two-tier Beads flow. | Candidate if Town/Rig split becomes central. |
| `content/assets/atlas-images/gas-town/gastown-worker-roles.svg` | Roles as functions. | Candidate if role section needs a visual. |
| `content/assets/story-images/11-mae-honeycomb-trace.png` | Mae trace as real observability image. | Probably not for X unless discussing trace; more natural in IX/XI or story page. |
| `content/assets/theory-images/openai-codex-dashboard-workflow.webp` and HumanLayer/Anthropic assets | Adjacent platform/harness/multi-agent visuals. | Likely not for X unless needed as contrast; avoid visual sprawl. |

## 8. Provenance rules for next passes

1. Public factual claims about current Gas Town/Beads behavior should cite primary external sources at the point where the detail enters the chapter.
2. Internal fragments, Атлас and dossiers can guide composition but should not be presented as public evidence.
3. If a detail is inherited from B3/gas_town source maps, preserve its external link immediately when it is first transferred into the chapter.
4. If a detail is only in an internal story reconstruction, use it as a story anchor; reopen external source only when the chapter makes a precise claim beyond the story’s internal summary.
5. Visual candidates require explicit disposition: inserted, deferred, queued, rejected or superseded. No replacement of real images by synthetic diagrams unless the chapter’s own argument needs a new synthetic figure.

## 9. Current gaps before drafting

- Source-restoration pass still needed for the small D1 set of current Gas Town/Beads docs.
- Need decide whether `MAIL_PROTOCOL.md` or `polecat-lifecycle-patrol.md` is the current better source for mail/status terms.
- Need decide whether `Gas Town Scheduler design` matters enough for the chapter or whether queue/backpressure can be supported by README/CHANGELOG/source maps.
- Need choose a small visual set; chapter likely needs one strong operational figure, not every local asset.
- Need keep Stripe/Jökull/Mae/Roast as supporting anchors rather than parallel subchapters.
