# P03 — начальный source register главы VII

Статус: это рабочий реестр источников перед написанием главы. Он не означает, что все перечисленные источники должны попасть в основной текст. Для публичной главы ссылка ставится только там, где конкретный материал действительно введён в аргумент. Внутренние файлы пакета используются как рабочая навигация; если из них берётся фактическое утверждение о внешней системе, ссылка должна вести на первичный внешний источник.

## 1. Внутренние рабочие источники

| Источник | Функция в главе | Статус использования |
| --- | --- | --- |
| `work/theory-writing/chapters/VII_persistent_work_graph_passes/01_01_context_and_boundary.md` | Рабочий контракт главы: предмет, границы, центральный сбой, сквозной пример, критерии готовности. | Использовать как локальное ограничение, не цитировать и не переносить фразы в основной текст без переписи. |
| `work/theory-writing/chapters/VII_persistent_work_graph_passes/02_02_input_corpus_map.md` | Карта входного корпуса: какие материалы питают главу, где риски дублирования, где нужен внешний добор. | Использовать для композиции и source triage. |
| `work/theory-writing/fragments/A4_persistent_work_graph_boundary.md` | Главная граница PWG: summary/лог/issue/runtime не равны состоянию продолжения работы. | Основной донор отрицательной рамки; переписывать естественным русским языком. |
| `work/theory-writing/fragments/A4_source_usage.md` | Уже собранные внешние ссылки по Beads, issue trackers, durable execution, CRDT/STORM, Intermediate Artifacts, Anthropic multi-agent и Gas Town. | Использовать как provenance map; проверять первоисточник перед включением в основной текст, если факт важен. |
| `work/theory-writing/fragments/A4_story_anchor_map.md` | Story anchors для Jökull, HumanLayer, Matt/Shopify и соседних кейсов. | Использовать только точечно; глава не должна пересказывать истории. |
| `work/theory-writing/fragments/B2_pwg_contribution.md` | Глубокая механика PWG: work item, dependencies, readiness, owner/claim, gates, evidence, prime, recovery, cleanup. | Главный донор механизма; риск — перегрузить текст словарём. |
| `work/theory-writing/fragments/B2_source_usage.md` | Источники по Beads, Taskmaster, `bd ready`, `bd gate`, `bd prime`, recovery, CodeCRDT/STORM, LangGraph. | Использовать для ссылок и проверки фактов. |
| `work/theory-writing/fragments/C2_pwg_to_process_profiles.md` | Граница PWG с GSD/BMAD/Gas Town: граф показывает состояние, process profile задаёт способ продолжения. | Использовать в финальном мосте к главе VIII. |
| `work/theory-writing/fragments/C3_pwg_to_evidence.md` | Связь PWG с gate/done/evidence/acceptance. | Использовать только в границах VII; полный evidence-layer оставить для XI–XII. |
| `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` | Граница runtime/durable execution/worktree/trace и PWG. | Использовать для раздела «граф выполнения и граф работы — разные слои». |
| `work/atlas/articles/persistent_work_graph.md` | Concept-first baseline по PWG. | Использовать как понятийную опору; не пересказывать структуру статьи. |
| `work/atlas/articles/persistent_work_graph_source_usage.md` | Source provenance для атласной статьи. | Использовать как дополнительную проверку ссылок. |
| `work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md` | Фактический quarry: Beads, Taskmaster, durable execution, issue trackers, negative cases, sandbox/recovery. | Использовать для добора деталей; не ссылаться на досье в публичной главе. |
| `work/atlas/articles/gas_town.md` | Соседняя concept-first статья: Gas Town как организация сверх PWG. | Boundary-only, не структура главы. |
| `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | Факты по Gas Town/Beads, changelog, troubleshooting, release risks, roles, backpressure. | Использовать узко для границы и негативной фактуры; не импортировать glossary Gas Town в VII. |
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md` | Место главы VII в общей теории. | Использовать для композиции и границ с VI/VIII/IX/X/XI–XIII. |
| `work/theory-writing/fragments/00_spine_map.md` | Сквозная ось жизненного цикла изменения. | Использовать для первого и последнего раздела главы. |
| `work/theory-writing/reports/POST_ATLAS_*` | Маршрутизация фрагментов, источников, визуальных кандидатов и story anchors. | Использовать как рабочую карту, не как публичный источник. |
| `protocols/rules/conceptual-translation-glossary.md` | Термины `evidence`, `trace`, `transcript`, `handoff`, нежелательные кальки. | Обязательный словарь для языковой переписи. |
| `protocols/rules/visual-assets-and-figures.md` | Правила обращения с локальными и внешними изображениями. | Обязателен для visual decision. |

## 2. Истории корпуса

| История | Функция в главе VII | Ограничение |
| --- | --- | --- |
| `content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md` | Главный story anchor: PR как объект сопровождения через CI, Greptile, Codex review, Fix/Dismiss/Escalate and readiness to merge. | Не пересказывать всю историю `/babysit-pr`; использовать как короткую сцену ожиданий, проверок и выхода к готовности. |
| `content/stories/10_mark_erikson_maximum_deep_reconstruction_connected.md` | Внешнее состояние и смысл за пределами локального контекста; полезен для линии compact prime / source state. | Вторичный якорь; не уводить в Replay/MCP/runtime-главу. |
| `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md` | Context budget, harness expectations, gates, separation of research/plan/implement. | Использовать как соседний принцип контролируемого контекста, не как обзор harness. |
| `content/stories/11_mae_capozzi_maximum_deep_reconstruction_connected.md` | Platform wrapper, traces, `InstructionsLoaded`, `TRACEPARENT`, observability and human review. | Использовать для различия «видимость процесса» и «закрытие работы», не уходить в evidence/observability-главу. |

## 3. Внешние первичные источники: ядро Beads/PWG

| Источник | Ссылка | Возможная функция в главе | Решение на старте |
| --- | --- | --- | --- |
| Beads documentation | https://gastownhall.github.io/beads/ | Общий якорь: Beads как task tracker / persistent structured memory for coding agents. | Primary candidate; перечитать перед использованием конкретных claims. |
| Beads GitHub repository | https://github.com/gastownhall/beads | Source-of-record рядом с docs; useful for release/issues/troubleshooting if needed. | Secondary primary source. |
| Beads architecture | https://gastownhall.github.io/beads/architecture | Dolt-backed storage, source of truth, recovery / sync / storage boundary. | Primary candidate для persistent state. |
| Beads core concepts | https://gastownhall.github.io/beads/core-concepts | `work item`, `status`, `priority`, dependencies, blocking relationships, ready queue. | Primary candidate для узла и готовности. |
| Beads CLI reference | https://gastownhall.github.io/beads/cli-reference | Общая навигация по командам. | Использовать только для точных команд. |
| `bd ready` | https://gastownhall.github.io/beads/cli-reference/ready | Конкретная опора для readiness as computed queue. | Primary candidate. |
| `bd gate` | https://gastownhall.github.io/beads/cli-reference/gate | Durable gate: human, timer, GitHub PR/CI or bead wait. | Primary candidate для gate-section. |
| `bd prime` | https://gastownhall.github.io/beads/cli-reference/prime | Compact markdown context for AI after compaction/new session. | Primary candidate для restoration/prime. |
| Beads workflows / gates | https://gastownhall.github.io/beads/workflows/gates | Gate как workflow primitive, если CLI page недостаточна. | Использовать при необходимости. |
| Beads multi-agent coordination | https://gastownhall.github.io/beads/multi-agent/coordination | `claim`/assignment/pin/multi-agent coordination. | Primary candidate для ownership/claim. |
| Beads multi-agent overview | https://gastownhall.github.io/beads/multi-agent | Более широкий вход по multi-agent behavior. | Secondary; не раздувать. |
| Beads routing | https://gastownhall.github.io/beads/multi-agent/routing | Cross-repo routing/hydration; полезно только если глава говорит о связанных узлах. | Optional, скорее companion. |
| Beads recovery overview | https://gastownhall.github.io/beads/recovery | Диагностика, recovery, `bd status`, `bd doctor`, `bd blocked`. | Primary candidate для recovery/cleanup. |
| Beads Claude Code integration | https://gastownhall.github.io/beads/integrations/claude-code | `SessionStart`, context injection, compact refresh. | Candidate для prime/compaction, если не хватает Codex-specific source. |
| Beads Codex integration | https://gastownhall.github.io/beads/integrations/codex | `AGENTS.md`, hooks, `SessionStart`, `PreCompact`, `PostCompact`, `UserPromptSubmit`. | Strong candidate для restoration packet / compact prime. |
| Beads Troubleshooting | https://github.com/gastownhall/beads/blob/main/docs/TROUBLESHOOTING.md | Sandboxed environments, Dolt server signal issues, stuck states. | Candidate для честной негативной фактуры. |
| Beads releases | https://github.com/gastownhall/beads/releases | Release gates, migration risk, operational burden of persistent state. | Optional, использовать только если нужен negative pressure. |
| Beads issue #3313 | https://github.com/gastownhall/beads/issues/3313 | Admin cleanup/compact failure, heartbeat-bloat, audit-trail bypass risk. | Optional negative case; не делать центральным. |

## 4. Внешние первичные источники: issue trackers and lightweight task graphs

| Источник | Ссылка | Возможная функция в главе | Решение на старте |
| --- | --- | --- | --- |
| GitHub issue dependencies | https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies | Baseline blocked/blocking relations. | Primary contrast source. |
| GitHub sub-issues | https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues | Parent/subtask hierarchy and progress. | Primary contrast source, если нужен пример иерархии. |
| Linear issue relations | https://linear.app/docs/issue-relations | `related`, `blocked`, `blocking`, `duplicate`. | Primary contrast source. |
| Linear issue relations changelog | https://linear.app/changelog/2020-03-11-issue-relations | История issue relations and reopening/closing signals. | Optional; не нужен, если docs достаточно. |
| Taskmaster task structure | https://tryhamster.com/docs/taskmaster/capabilities/task-structure | `tasks.json`, dependencies, details, testStrategy. | Candidate для лёгкой альтернативы Beads. |
| Taskmaster dependencies | https://tryhamster.com/docs/taskmaster/task-workflow/dependencies | Dependency graph and blocked tasks. | Candidate if lightweight graph section exists. |
| Taskmaster tags | https://tryhamster.com/docs/taskmaster/task-workflow/tags | Parallel work streams. | Optional. |
| Taskmaster loop | https://tryhamster.com/docs/taskmaster/automation/loop | Automated loop/resume around tasks. | Optional; may pull toward runtime, use carefully. |
| Task Master task structure | https://docs.task-master.dev/capabilities/task-structure | Alternative/current docs path inherited from A4/B2. | Verify which Taskmaster docs variant is current before public use. |
| Task Master clusters | https://docs.task-master.dev/capabilities/clusters | Clusters by dependency graph, parallel execution planning. | Optional; high duplication risk. |

## 5. Внешние источники для runtime / durable execution boundary

| Источник | Ссылка | Возможная функция в главе | Решение на старте |
| --- | --- | --- | --- |
| LangGraph persistence | https://docs.langchain.com/oss/python/langgraph/persistence | Threads, checkpoints, persistence, state of execution. | Boundary-only. |
| LangGraph interrupts | https://docs.langchain.com/oss/python/langgraph/interrupts | Interrupt/resume/human-in-loop execution state. | Boundary-only. |
| Temporal human-in-the-loop AI agent | https://docs.temporal.io/ai-cookbook/human-in-the-loop-python | Workflow waits/signals and human approval. | Boundary-only; useful contrast with `gate`. |
| Pydantic AI durable execution | https://pydantic.dev/docs/ai/integrations/durable_execution/overview/ | Durable agents, long-running workflows, Temporal/DBOS/Prefect/Restate integrations. | Boundary-only. |
| DBOS durable execution / Transact TS | https://github.com/dbos-inc/dbos-transact-ts | Durable workflows and checkpoints around Postgres-backed execution. | Optional boundary. |
| DBOS why | https://docs.dbos.dev/why-dbos | Resume from last completed step / Postgres-backed execution. | Optional boundary. |
| Restate durable execution | https://docs.restate.dev/concepts/durable_execution | Journal/replay/skip completed steps. | Boundary-only. |
| Restate key concepts | https://docs.restate.dev/foundations/key-concepts | Durable service execution concepts. | Optional. |
| Git worktree documentation | https://git-scm.com/docs/git-worktree | Worktree as technical isolation and cleanup/prune/repair. | Boundary-only; likely more IX than VII. |
| Claude Code worktrees | https://code.claude.com/docs/en/worktrees | Parallel session isolation. | Boundary-only. |
| OpenAI Codex Worktrees | https://developers.openai.com/codex/app/worktrees | Codex worktree handoff / isolated tasks. | Boundary-only; current OpenAI docs should be checked if used. |

## 6. Внешние источники для shared state / intermediate artifacts

| Источник | Ссылка | Возможная функция в главе | Решение на старте |
| --- | --- | --- | --- |
| Intermediate Artifacts as First-Class Citizens | https://arxiv.org/abs/2605.12087 | Durable intermediate artifacts as maintained work products, not hidden chain-of-thought. | Strong theory support if chapter needs academic anchor. |
| Anthropic multi-agent research system | https://www.anthropic.com/engineering/multi-agent-research-system | Parallel research, high token cost, strong dependency limits, need for citation/evidence pass. | Candidate for multi-agent state pressure, not central. |
| CodeCRDT | https://arxiv.org/abs/2510.18893 | Coordination/convergence and semantic conflicts. | Boundary-only; avoid research survey. |
| STORM paper | https://arxiv.org/html/2605.20563v1 | Read snapshots, stale dependency rejection and retry, state consistency. | Boundary-only if writing about stale graph/source state. |
| STORM paper variant in dossier | https://arxiv.org/html/2604.09003v1 | Dossier uses this URL; verify version before citing. | Needs verification before public use. |
| STORM GitHub repository | https://github.com/haipham2306/STORM-CodeAgent | Implementation reference. | Optional; likely not needed. |
| Why Do Multi-Agent LLM Systems Fail? | https://arxiv.org/abs/2503.13657 | Failure taxonomy for multi-agent systems. | Optional; likely too broad for VII. |
| AEGIS | https://arxiv.org/abs/2603.12621 | Neighbor source from dossier. | Deferred; too broad unless specific gap appears. |
| SKILL.nb | https://arxiv.org/abs/2606.08049 | Neighbor source from dossier. | Deferred; likely not VII. |

## 7. Gas Town and Beads-as-organization sources

| Источник | Ссылка | Возможная функция в главе | Решение на старте |
| --- | --- | --- | --- |
| Gas Town GitHub | https://github.com/gastownhall/gastown | Primary repo for Gas Town concepts. | Boundary-only. |
| Gas Town glossary | https://github.com/gastownhall/gastown/blob/main/docs/glossary.md | Town/Rig/roles boundary; Gas Town as higher organizational environment. | Use only for one contrast if needed. |
| Gas Town docs | https://docs.gastownhall.ai/ | Public docs surface. | Boundary-only; verify if used. |
| Welcome to Gas Town | https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 | High-level public framing of Gas Town. | More relevant to X; avoid relying on VII except context. |
| Introducing Beads | https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a | Public framing of Beads as coding-agent memory. | Candidate only if official docs lack narrative framing. |
| Beads Best Practices | https://steve-yegge.medium.com/beads-best-practices-2db636b9760c | Practical guidance; likely more atlas/Gas Town. | Optional. |
| Gas Town changelog | https://github.com/gastownhall/gastown/blob/main/CHANGELOG.md | Pressure mechanics, repair, queues, quality gates. | Optional negative/operational pressure; more X than VII. |
| Gas Town architecture docs | https://github.com/gastownhall/gastown/blob/main/docs/ARCHITECTURE.md | Organization above Beads. | Boundary-only. |
| Gas Town mail protocol | https://github.com/gastownhall/gastown/blob/main/docs/MAIL_PROTOCOL.md | Inter-agent communication. | Defer to X. |
| Gas Town scheduler design | https://github.com/gastownhall/gastown/blob/main/docs/design/scheduler.md | Scheduling/backpressure. | Defer to X. |
| Witness AT Team Lead design | https://github.com/gastownhall/gastown/blob/main/docs/design/witness-at-team-lead.md | Future architecture limits and costs. | Defer to X/IX unless negative boundary needed. |
| DoltHub: A Day in Gas Town | https://www.dolthub.com/blog/2026-01-15-a-day-in-gas-town/ | Beads as continuity after PR review and new sessions. | Candidate for narrative support, but use sparingly. |
| DoltHub: Restoring Beads Classic | https://www.dolthub.com/blog/2026-04-02-restoring-beads-classic/ | Solo Beads vs Gas Town scale. | Useful boundary Beads ≠ Gas Town. |
| DoltHub: Common Beads Classic Workflows | https://www.dolthub.com/blog/2026-04-15-common-beads-workflows/ | Practical Beads workflows. | Optional. |
| DoltHub: Two Weeks in Gas Town | https://www.dolthub.com/blog/2026-04-16-two-weeks-in-gastown/ | Beads as institutional memory and Gas Town workspace manager. | Candidate for boundary, not central. |
| Multi-Agent Coordination with Dolt and Beads | https://www.dolthub.com/blog/2026-04-22-multi-agent-dolt-beads/ | Dolt-backed multi-agent coordination. | Optional. |
| HN: Welcome to Gas Town discussion | https://news.ycombinator.com/item?id=46458936 | Weak signal: accountability/review bottleneck, merge conflicts, conceptual overload. | Only as weak perception signal; not factual authority. |
| Gas Town discussion #363 | https://github.com/gastownhall/gastown/discussions/363 | Community/design discussion. | Optional, weak/secondary. |

## 8. Sources from process/evidence chapters that should remain mostly out of VII

| Источник | Ссылка | Почему не основной для VII |
| --- | --- | --- |
| GSD context engineering | https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/context-engineering.md | VIII/process profile, not PWG mechanics. |
| GSD phase loop | https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md | VIII. |
| Open GSD architecture | https://www.opengsd.net/docs/v1/architecture | VIII. |
| BMAD workflow map | https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md | VIII; use only as boundary if needed. |
| BMAD agents | https://docs.bmad-method.org/reference/agents/ | VIII. |
| BMAD correct course | https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md | XIII/repair or VIII, not central here. |
| Test-Driven Agentic Development | https://arxiv.org/abs/2603.17973 | XI/evidence, not central to PWG. |
| Pact consumer docs | https://docs.pact.io/consumer | XI/evidence. |
| MADR | https://adr.github.io/madr/ | III/XII/ADR, not VII. |
| GitHub CODEOWNERS docs | https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners | XII/authority. |
| Argo Rollouts Analysis | https://argo-rollouts.readthedocs.io/en/stable/features/analysis/ | XI/release evidence. |
| Google SRE Workbook Canarying Releases | https://sre.google/workbook/canarying-releases/ | XI/release evidence. |
| Shopify Roast sources | https://shopify.engineering/introducing-roast | C4/IX runtime boundary, not VII except contrast. |
| Stripe Minions sources | https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | C4/IX runtime boundary, not VII except contrast. |
| Mike McQuaid / Sandboxes and Worktrees | https://mikemcquaid.com/sandboxed-agent-worktrees-my-coding-and-ai-setup-in-2026/ | IX/runtime/worktree boundary, not core VII. |

## 9. Visual source register

| Кандидат | Путь / источник | Статус | Функция |
| --- | --- | --- | --- |
| Beads task graph memory | `content/assets/theory-images/beads-task-graph-memory.svg` | `local_image_asset` | Центральный visual anchor: graph of tasks, dependencies, claims/memory. |
| PWG vs runtime boundary | авторская схема, пока не создана | `editorial_visual_idea` | Возможна, если тексту нужна отдельная опора различения work graph / execution run. |
| Gate anatomy | авторская схема, пока не создана | `editorial_visual_idea` | Возможна, если `gate` в тексте тяжело удерживается прозой. |
| Restoration packet | авторская схема, пока не создана | `editorial_visual_idea` | Возможна, если сквозной пример требует визуальной проверки идеи PWG. |
| GitHub/Linear boundary screenshots | внешние продукты | `external_real_image_candidate`, пока не использовать | Вероятно не нужны: могут превратить главу в UI-tour. |
| Gas Town visuals | `content/assets/atlas-images/gas-town/*.svg` | `local_image_asset`, but boundary-only | Скорее для X; в VII не вставлять без отдельной причины. |

## 10. Source discovery log

На этом проходе внешний поиск не выполнялся: инструкция требовала собрать первичный source register из выбранных фрагментов, Атласа, досье, историй, route maps and plans. Для следующих source/depth проходов нужно точечно перечитать первичные источники, которые реально войдут в главный текст, особенно Beads CLI/docs, GitHub/Linear docs and negative Beads/recovery sources if used.
