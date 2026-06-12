# A4. Использование источников

Внутренние планы, досье и скелет использованы как карта материала и как ограничение композиции. В основном фрагменте они не цитируются: ссылки поставлены только на первичные или публичные документы, из которых взяты фактические якоря.

| Источник | Как использован в A4 | Статус |
|---|---|---|
| [Beads documentation](https://gastownhall.github.io/beads/) | Якорь для тезиса о переносимой памяти работы для AI-supervised coding workflows: Dolt-backed storage, dependency-aware execution, `bd ready`, multi-agent coordination. | Использован в основном тексте. |
| [Beads architecture](https://gastownhall.github.io/beads/architecture) | Подтверждение, что Dolt является sole storage backend/source of truth, записи auto-commit’ятся, recovery строится через pull/backup. | Использован в основном тексте. |
| [Beads core concepts](https://gastownhall.github.io/beads/core-concepts) | Якорь для work item/status/dependencies/ready queue и вычисляемой готовности. | Использован в основном тексте. |
| [Beads gates](https://gastownhall.github.io/beads/workflows/gates) | Якорь для gates как durable async waits: human approval, timer, GitHub PR/CI. | Использован в основном тексте. |
| [Beads multi-agent coordination](https://gastownhall.github.io/beads/multi-agent) | Якорь для pin/hook, work assignment, handoff/cross-repo coordination как частичной формы ownership. | Использован в основном тексте. |
| [Beads Claude Code integration](https://gastownhall.github.io/beads/integrations/claude-code) | Source-depth anchor для compact prime: `SessionStart` hook, compact refresh, `bd prime`, примерно 1–2k tokens of context при старте сессии и обновление workflow context перед compaction. | Использован в основном тексте после прохода 0f1f024c5a. |
| [GitHub issue dependencies](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies) | Базовый contrast: обычные issue trackers уже фиксируют blocked/blocking, но не содержат агентный source/handoff/recovery слой. | Использован в основном тексте. |
| [Linear issue relations](https://linear.app/docs/issue-relations) | Базовый contrast: blocked, blocking, related, duplicate как human project surface. | Использован в основном тексте. |
| [Task Master task structure](https://docs.task-master.dev/capabilities/task-structure) | Граница с lightweight task graph: `tasks.json`, dependencies, details, testStrategy, subtasks, metadata. | Использован в основном тексте. |
| [Task Master clusters](https://docs.task-master.dev/capabilities/clusters) | Граница с execution planning: clusters by dependency graph, Claude Code sessions, parallel task execution. | Использован в основном тексте. |
| [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence) | Граница с durable graph execution: checkpoints, threads, HITL, memory, time travel, fault tolerance. | Использован в основном тексте. |
| [Temporal human-in-the-loop](https://docs.temporal.io/ai-cookbook/human-in-the-loop-python) | Граница с workflow signal/waiting workflow. | Использован в основном тексте. |
| [DBOS why](https://docs.dbos.dev/why-dbos) | Граница с Postgres checkpointing and resume from last completed step. | Использован в основном тексте. |
| [Restate key concepts](https://docs.restate.dev/foundations/key-concepts) | Граница с durable execution через journal/replay/skip completed steps. | Использован в основном тексте. |
| [CodeCRDT](https://arxiv.org/abs/2510.18893) | Граница с CRDT-convergence и observation-driven coordination: speedup/slowdown trade-off, semantic conflicts. | Использован в основном тексте. |
| [STORM](https://arxiv.org/html/2605.20563v1) | Граница с file-level state consistency, read snapshot, stale dependency rejection and retry. | Использован в основном тексте. |
| [Intermediate Artifacts as First-Class Citizens](https://arxiv.org/abs/2605.12087) | Теоретический якорь для durable intermediate artifacts как maintained work products, не chain-of-thought. | Использован в основном тексте. |
| [Anthropic multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) | Якорь для parallel research/subagents, high token cost, ограничения задач с сильными зависимостями, need for citation/evidence pass. | Использован в основном тексте. |
| [Gas Town glossary](https://github.com/gastownhall/gastown/blob/main/docs/glossary.md) | Публичный первоисточник для boundary-утверждения, что Gas Town расположен выше PWG как среде агентной разработки с Town/Rig уровнями и ролями Mayor, Deacon, Polecat, Refinery, Witness. | Использован в основном тексте после прохода eec2b912df. |
| GSD dossier, BMAD dossier, Gas Town dossier | Использованы как соседние рамки и boundary checks: не смешивать PWG с full SDLC process, story context или organizational environment. | Не цитировались как источники фактов в основном тексте. |
| Jökull, HumanLayer, Matt Pocock, Shopify Roast story files | Использованы только для карты story anchors ниже; основной фрагмент не пересказывает истории. | Не цитировались в основном тексте. |
| PERSISTENT_WORK_GRAPH cycle 05 | Не использовался. Материал помечен как rollback/rejected и не положен в основу A4. | Исключён. |

Оставленные без ссылки тезисы в основном фрагменте являются теоретическими выводами из синтеза, а не отдельными утверждения с источниковой опорой. Там, где речь идёт о конкретной системе, поставлена ссылка на публичный первоисточник.

## Обновление после прохода 717a83185f

Новых внешних источников не добавлялось. Второй проход усилил объектную линию самого фрагмента: work item → dependencies/readiness → owner/claim → gates → evidence → handoff/prime → recovery → cleanup. Это теоретическое уточнение опирается на уже открытые источники Beads, Task Master, LangGraph/Temporal/DBOS/Restate, CodeCRDT/STORM, Intermediate Artifacts и Anthropic multi-agent research system. В основном тексте новые ссылки не потребовались, потому что добавленные абзацы развивают механизм, а не вводят новые утверждения с источниковой опорой.

## Обновление после прохода a60c9d9cce

Новых внешних источников не добавлялось. Проход развёл PWG с соседними системами через критерий authority: issue/project authority для GitHub/Linear; task breakdown/execution prompt для Task Master; run replay/resume для durable execution; state convergence/write-time consistency для CRDT/STORM; organizational environment для Gas Town. Добавленные формулировки используют уже внесённые источники: GitHub/Linear, Task Master, LangGraph/Temporal/DBOS/Restate, CodeCRDT/STORM. Для Gas Town на момент этого прохода ссылка не ставилась: доступный материал находился во внутренних досье, а первоисточник тогда не восстанавливался. Позже этот gap закрыт проходом eec2b912df через публичный Gas Town glossary.

## Обновление после прохода 8f35cba720

Новых внешних источников не добавлялось. Failure-pressure pass усилил уже заявленные сбои: false completion, lost state, duplicated reading/work, stale graph, read-snapshot staleness, wrong authority, unclosed gates, unsynthesized утверждения с источниковой опорой. Эти формулировки являются внутренним теоретическим давлением на аргумент и опираются на уже введённые boundary anchors: Beads gates/recovery, STORM read-snapshot consistency, CodeCRDT semantic conflicts, Anthropic parallel research and citation discipline, Intermediate Artifacts. Rejected cycle 05 не использовался как основание.

## Обновление после прохода 0f1f024c5a

Добавлен один внешний источник, открытый в этом проходе: Beads Claude Code integration. Он использован узко, только для уточнения compact prime как регулярно пересобираемого входа в сессию: `bd prime` запускается на `SessionStart` и после context compaction, а документация описывает небольшой context injection и refresh перед compaction. Другие найденные соседние источники не добавлялись, чтобы не превращать A4 в каталог инструментов.

## Обновление после прохода eec2b912df

План починки выявил один реальный provenance gap: Gas Town в основном тексте описывался как верхняя организационная среда, но прежняя source usage карта признавала, что публичный первоисточник не был восстановлен. В этом проходе открыт и добавлен `gastown/docs/glossary.md` из публичного репозитория. Он использован узко: только для поддержки boundary-тезиса о Gas Town как среде управления несколькими экземплярами Claude Code с Town/Rig уровнями и ролями. Внутренние Gas Town досье остаются рабочими картами, но не citation target.

## Остаточная починка после прохода 6e7b58388e

Уточнена хронология Gas Town source gap: ранняя заметка про отсутствие публичного источника сохранена как историческая, но явно помечена как закрытая проходом eec2b912df. Новых внешних источников не добавлялось.

## Repair 2026-06-11 — source usage unchanged

В ходе A4 composition/visual/style repair новые внешние источники не добавлялись. Все прежние утверждения с источниковой опорой сохранены: GitHub/Linear для issue dependencies, Beads для work graph/gates/multi-agent/prime, Intermediate Artifacts для долговечных промежуточных артефактов, Anthropic для параллельного research, LangGraph/Temporal/DBOS/Restate для durable execution, CodeCRDT/STORM для shared-state consistency, Task Master для task structure/clusters и Gas Town glossary для верхнего organizational layer. Изменения касались композиции, визуального слоя и языка; линия происхождения не менялась.
