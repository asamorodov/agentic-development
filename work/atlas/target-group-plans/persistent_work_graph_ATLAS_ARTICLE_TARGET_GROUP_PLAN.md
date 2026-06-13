# Target-group plan: статья атласа `persistent_work_graph` — Persistent Work Graph / Beads

Статус: `ready_for_package_manufacture_after_manual_review`.  
Article id: `persistent_work_graph`  
Readiness status: `ready_for_package_manufacture_after_manual_review`.  
Рабочее название: `Persistent Work Graph / Beads`  
Уровень статьи: `core concept article`  
Режим будущего пакета: самодостаточный writing package.  
Внутренних ограничений объёма нет.

## 1. Назначение статьи

Статья должна объяснить Persistent Work Graph как форму устойчивого состояния работы, а не как обзор Beads, Gas Town или task trackers. Главный вопрос читателя: **какое состояние работы должно жить вне чата, вне отдельного запуска агента и вне простого списка задач, чтобы работу можно было продолжать, блокировать, передавать, проверять и восстанавливать?**

Persistent Work Graph нужен там, где работа уже не помещается в один промпт, один чат, один запуск агента или один список задач. Он хранит не просто “что надо сделать”, а состояние работы: что существует как отдельная единица, от чего зависит, кто отвечает, почему работа заблокирована, что готово к следующему шагу, какое контрольное условие должно быть снято, какие свидетельства уже есть и как восстановить контекст без повторного чтения всего прошлого.

## 2. Article contract

Главное досье:

```text
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
```

Статья должна раскрыть:

- почему `prompt`, transcript, Markdown TODO и обычный issue list недостаточны для длинной multi-session / multi-agent работы;
- минимальные свойства устойчивой единицы работы: identity, dependencies, ready queue, owner/claim, comments/history, control conditions, handoff, prime, recovery, evidence links;
- Beads как anchor и проверку механизма: Dolt storage, CLI/MCP, hash ids, dependency-aware execution, `bd ready`, `bd blocked`, `bd graph`, `bd prime`, routing, synchronization и operational caveats;
- границы с issue tracker, Taskmaster, Gas Town, BMAD/GSD, specification methods, ADR, durable execution, CRDT/STORM/MAST и Anthropic multi-agent research;
- перенос на многопроходный документный процесс: job/pass/gate/prime/recovery, source state, intermediate artifacts, source claims, citation audit, synthesis pass и safe parallel source protocol;
- failure modes: stale graph, преждевременное снятие dependency без свидетельства, owner/claim как ложное чувство контроля, `ready` без безопасности следующего действия, `prime` как неполное восстановление смысла, bureaucratic gate, agent gaming status, storage too early.

Отрицательная граница: статья не должна быть product review Beads, повтором Gas Town, общим эссе про issue trackers, survey of papers, or implementation proposal for the user's TypeScript orchestrator. Beads — главный наблюдаемый anchor, но центр тяжести статьи — устойчивое состояние работы.

## 3. Соседние слои и границы

| Слой | Что он хранит или организует | Почему не заменяет PWG |
|---|---|---|
| Issue tracker | Запись о задаче, обсуждение, иногда статус | Обычно не хранит достаточно machine-visible state: ready queue, compact recovery, control conditions, evidence links. |
| PWG | Состояние работы, зависимости, готовность, блокировки, владельца, историю, восстановление | Это не полный operating model и не граф выполнения конкретного запуска. |
| Durable execution | Состояние запуска, checkpoint, thread, pending writes, replay/time travel | Может восстановить run, но не объясняет, какая работа существует и почему она готова/заблокирована. |
| Gas Town | Организационную среду вокруг многих агентов, рабочих пространств, hooks, очередей и watchdog | Использует рабочие единицы, но шире PWG: это operating model. |
| CRDT/STORM/MAST | Конфликты совместного изменения, write-time mediation, parallel agent limits | Помогают при параллельности, но не заменяют смысловое состояние работы. |

## 4. Фактура без coverage-бюрократии

PWG-статья опирается на досье и первоисточники, но package не должен снова превращать перенос фактуры в coverage/disposition-бюрократию. Жёсткий режим `dossier-backed completeness / relevant but untransferred` считается откатанным: не нужно строить тотальную matrix по всему досье и доказывать статус каждого релевантного фрагмента.

Мягкий ориентир остаётся: ключевые тезисы статьи должны иметь технические опоры. Если раздел объясняет identity, dependencies, ready queue, owner/claim, control condition, comments/history, prime, recovery, evidence links, Beads/Dolt/CLI/MCP, `bd ready`, `bd blocked`, `bd graph`, `bd prime`, routing, synchronization или перенос на многопроходный документный процесс, читателю обычно нужны конкретные детали: команда, статус, файл, пример, ограничение, tradeoff или визуальный кандидат. Если без такой опоры раздел звучит общей прозой, деталь лучше встроить в основной текст. Если деталь не помогает reader question, относится к соседней статье или ломает ход объяснения, её не нужно вставлять ради отчётности.

`source_transfer_ledger`, `image_plan` и `open_questions` остаются журналами реальных решений, долгов и source gaps. Они не заменяют статью и не должны становиться главным результатом прохода.

## 5. Предполагаемая форма будущей статьи

1. Зачем нужно устойчивое состояние работы: почему чат, transcript, TODO и issue list не удерживают agentic work.
2. Минимальная модель PWG: work item, dependencies, ready queue, owner/claim, control condition, history, prime, recovery, evidence links.
3. Beads как anchor: какие свойства PWG становятся наблюдаемыми через Dolt/CLI/MCP/commands.
4. Почему PWG — не просто issue tracker и не просто Beads.
5. Границы: durable execution, Gas Town, process profiles, CRDT/STORM/MAST, source-state protocols.
6. Перенос на многопроходный документный процесс как второе доказательство понятия.
7. Failure modes и overuse: когда граф устаревает, когда `ready` вводит в заблуждение, когда gate становится бюрократией, когда хранилище введено слишком рано.
8. Практический payoff: что PWG меняет в package execution, pass recovery, source-state, merge gates и agent handoff.

## 6. Обрабатываемые файлы будущего article package

```yaml
- path: work/atlas/articles/persistent_work_graph.md
  status: future
  role: primary
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/persistent_work_graph_source_usage.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/persistent_work_graph_source_transfer_ledger.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/persistent_work_graph_image_plan.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/persistent_work_graph_external_image_queue.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/persistent_work_graph_open_questions.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/persistent_work_graph_theory_links.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/persistent_work_graph_degradation_and_duplication_audit.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/persistent_work_graph_readiness_report.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
```

Group mode: `linked-target-edit`.

## 7. Exact read-only inputs to bundle

```text
START.md
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/decisions/ADR-0011-concept-first-technical-atlas.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_ORIENTATION.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_LEDGER.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PATHS.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
protocols/rules/visual-assets-and-figures.md
protocols/rules/human-technical-style.md
protocols/rules/language-style-rules.md
protocols/rules/content-preservation.md
protocols/rules/source-and-provenance.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/ADR_METHOD_DOSSIER.md
work/theory-writing/fragments/00_spine_map.md
work/theory-writing/fragments/A1_change_not_prompt.md
work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
work/theory-writing/fragments/A5_process_methodologies_synthesis.md
work/theory-writing/fragments/A6_execution_environment_distinctions.md
work/theory-writing/fragments/A7_observation_vs_evidence.md
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
work/theory-writing/fragments/A9_lifecycle_repair.md
work/theory-writing/fragments/B2_pwg_contribution.md
work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
work/theory-writing/fragments/C1_specification_to_pwg.md
work/theory-writing/fragments/C2_pwg_to_process_profiles.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
work/theory-writing/fragments/C5_theory_to_technical_atlas.md
work/theory-writing/fragments/C5_concept_atlas_article_map.md
work/theory-writing/fragments/C5_source_usage.md
work/theory-writing/fragments/A10_mode_selection_map.md
work/theory-writing/fragments/A10_mode_selection_matrix.md
work/theory-writing/fragments/A10_decision_stress_tests.md
work/theory-writing/fragments/A10_source_usage.md
content/Theoretical_synthesis.md
content/Cross_story_synthesis.md
content/Handbook.md
content/Fieldbook.md
work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
content/assets/theory-images/MANIFEST.md
content/assets/theory-images/beads-task-graph-memory.svg
content/assets/theory-images/gastown-architecture.svg
content/assets/theory-images/gastown-basic-workflow.svg
content/assets/theory-images/anthropic-multi-agent-process-diagram.webp
content/assets/theory-images/anthropic-multi-agent-research-architecture.webp
work/atlas/target-group-plans/persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

Эти входы должны быть упакованы в future self-contained package. План не должен полагаться на неявный доступ к репозиторию, vague `relevant files` или отсутствие тяжёлых assets в текущем чате. Если путь не существует при сборке пакета, package-builder должен остановиться или зафиксировать конкретный blocker.

## 8. Очередь будущего article-writing package

Выбран полный atlas-queue shape: `P01`–`P25` + `Final`. Для PWG это оправдано: это core concept article, связывающая Beads, issue graphs, Taskmaster, durable execution, source-state protocol, parallel-agent limits и проектный дизайн многопроходного процесса. Сокращение очереди почти наверняка смешает уровни или превратит статью в обзор Beads/Gas Town.

### P01 — первичный концептуальный черновик статьи

```text
Создай первый полный черновик статьи `work/atlas/articles/persistent_work_graph.md` и skeleton/status для всех companion-файлов.

Прочитай сначала:
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
- work/theory-writing/fragments/B2_pwg_contribution.md
- work/theory-writing/fragments/C1_specification_to_pwg.md
- work/theory-writing/fragments/C3_pwg_to_evidence.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/A10_mode_selection_map.md

Статья должна начинаться с рабочего вопроса: какое состояние работы должно жить вне чата, вне отдельного запуска агента и вне простого списка задач, чтобы работу можно было продолжать, блокировать, передавать, проверять и восстанавливать? Не пиши обзор Beads и не повторяй Gas Town. Пиши core concept article про устойчивое состояние работы.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P02 — article contract and boundaries

```text
Укрепи article contract внутри статьи и companion-файлов.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/theory-writing/fragments/B2_pwg_contribution.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
- work/theory-writing/fragments/C2_pwg_to_process_profiles.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md

Зафиксируй границы: PWG ≠ Beads product review, ≠ Gas Town operating model, ≠ BMAD/GSD process profile, ≠ issue tracker alone, ≠ durable execution, ≠ CRDT/shared editor, ≠ implementation plan for a TypeScript orchestrator. Укажи, что Beads нужен как проверка механизма: какие свойства PWG становятся видимыми, когда состояние работы получает хранилище, команды, зависимости, очередь готовности, историю, prime и восстановление.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P03 — dossier inventory

```text
Сделай inventory досье без тотальной coverage matrix.

Прочитай сначала:
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/atlas/articles/persistent_work_graph.md
- work/atlas/articles/persistent_work_graph_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Отметь, что уже перенесено, что осталось неперенесённым, что требует открытия первоисточников, где будущей статье могут не хватать технические опоры. Обнови основной текст только при явном пропуске article-critical материала. Запиши результат в `persistent_work_graph_source_transfer_ledger.md` and `persistent_work_graph_source_usage.md`.

Не строй тотальную coverage matrix по всему досье. Ledger должен помогать статье, а не заменять её.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P04 — source-depth 1: почему task/TODO/transcript недостаточны

```text
Усиль статью вокруг исходной проблемы: почему чат, transcript, Markdown TODO, обычный issue и локальный план не удерживают работу в длинном агентном процессе.

Прочитай сначала:
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
- work/theory-writing/fragments/B2_pwg_contribution.md

Покажи конкретно: потеря identity, dependency, ready-state, owner/claim, gate, evidence, compact recovery и history. Если раздел звучит общей прозой, добавь технические опоры, которые помогают понять механизм.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P05 — source-depth 2: минимальные свойства устойчивой единицы работы

```text
Раскрой минимальные свойства PWG как состояния работы: stable work item identity, dependencies, ready queue, owner/claim, comment/history, control condition, handoff, compact prime, recovery и связь со свидетельствами.

Прочитай сначала:
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/theory-writing/fragments/C1_specification_to_pwg.md
- work/theory-writing/fragments/C3_pwg_to_evidence.md

Сделай это как механизм, а не как список терминов. Не вставляй детали ради отчётности; добавляй их там, где без них PWG выглядит как общая метафора.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P06 — source-depth 3: Beads как anchor и проверка механизма

```text
Раскрой Beads как anchor: Dolt storage, CLI/MCP, hash ids, dependency-aware execution, `bd ready`, `bd blocked`, `bd graph`, `bd prime`, routing, synchronization, operational caveats.

Прочитай сначала:
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- content/assets/theory-images/beads-task-graph-memory.svg
- work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md

Не делай обзор продукта Beads. Покажи, какие свойства PWG Beads делает наблюдаемыми, и дай достаточно конкретных команд/состояний/ограничений, чтобы это не стало общей прозой.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P07 — source-depth 4: границы с issue tracker, durable execution, CRDT/STORM, Gas Town

```text
Разведи соседние слои так, чтобы они не конкурировали с PWG как равноправные темы.

Прочитай сначала:
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md

Объясни: issue tracker хранит задачу/обсуждение; PWG хранит состояние работы; durable execution восстанавливает запуск; Gas Town организует среду вокруг многих агентов и рабочих единиц; CRDT/STORM/MAST работают с конфликтами совместного изменения и параллельной работы, но не заменяют смысловое состояние работы. Границы должны быть подкреплены конкретными различиями, а не taxonomy ради taxonomy.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P08 — source-depth 5: перенос на многопроходный документный процесс

```text
Покажи перенос PWG на наш document-process workflow как второе доказательство понятия, а не приложение.

Прочитай сначала:
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md
- work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
- work/theory-writing/fragments/C2_pwg_to_process_profiles.md

Раскрой job/pass/gate/prime/recovery, source states, intermediate artifacts, worker returns, citation audit, synthesis pass, safe parallel source protocol. Покажи, что если это можно представить как состояние работы, PWG шире product-specific issue graph. Добавляй technical anchors там, где они помогают читателю увидеть перенос на документный процесс.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P09 — свободный добор материала 1

```text
Свободно перечитай статью и сам найди самый слабый участок фактуры.

Прочитай сначала:
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/atlas/articles/persistent_work_graph.md
- work/atlas/articles/persistent_work_graph_source_transfer_ledger.md

Добери команды, state schemas, dependency semantics, failure modes, image candidates, caveats, operational limitations или конкретные primitives. Не превращай проход в стилистику. Расширь основной текст и companion-файлы.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P10 — свободный добор материала 2

```text
Свободно перечитай статью и сам найди самый слабый участок концептуальной связности.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/theory-writing/fragments/B2_pwg_contribution.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C3_pwg_to_evidence.md

Усиль разделение work graph / execution graph / evidence layer / source state / shared-editing coordination. Не сокращай; добавляй недостающую фактуру и объяснение.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P11 — visual asset pass 1: локальные готовые изображения

```text
Поставь релевантные локальные изображения как настоящие `<figure><img ...></figure>` или явно объясни отказ.

Прочитай сначала:
- work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
- work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
- content/assets/theory-images/MANIFEST.md
- content/assets/theory-images/beads-task-graph-memory.svg
- content/assets/theory-images/gastown-architecture.svg
- content/assets/theory-images/gastown-basic-workflow.svg
- content/assets/theory-images/anthropic-multi-agent-process-diagram.webp
- content/assets/theory-images/anthropic-multi-agent-research-architecture.webp
- work/atlas/articles/persistent_work_graph.md

Для каждого релевантного local asset действует insert-or-explain. Подпись должна объяснять смысл изображения для статьи, а не историю восстановления файла.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P12 — visual asset pass 2: внешние реальные изображения-кандидаты

```text
Обработай внешние реальные картинки и картинки из досье.

Прочитай сначала:
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
- work/atlas/articles/persistent_work_graph.md

Начни с раздела досье `## Кандидаты на иллюстрации` и похожих списков. Для каждого кандидата запиши disposition в `persistent_work_graph_image_plan.md`: `inserted_inline_external_placeholder`, `external_queue_only`, `deferred`, `rejected`, `superseded_by_local_asset`, `not_found_in_source`. Если кандидат нужен в статье, поставь inline `<figure data-asset-status="external-real-candidate">` по месту применения и продублируй его в нижнем разделе `Внешние изображения для asset-pass` и в `persistent_work_graph_external_image_queue.md`. Внешние источники можно искать и открывать для проверки/картинок; предпочтение первоисточникам.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P13 — visual asset pass 3: редкие синтетические схемы

```text
Создай только те собственные схемы, которые действительно нетривиальны и не подменяют готовые изображения.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/atlas/articles/persistent_work_graph_image_plan.md

Допустимые сильные кандидаты: состояние работы против состояния запуска; задача как узел графа с зависимостями, блокировками и свидетельствами; перенос PWG на job/pass/gate/source-state; граница PWG/Gas Town/durable execution. Не делай схемы ради визуального разнообразия.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P14 — concept reinforcement 1: самостоятельность статьи

```text
Сделай статью полностью самостоятельной для читателя, который пришёл за PWG/Beads без чтения всей теории.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/theory-writing/fragments/00_spine_map.md
- work/theory-writing/fragments/B2_pwg_contribution.md

Разрешён контролируемый повтор с теорией, если он нужен для понимания. Нельзя превращать статью во вторую теорию или в техническое приложение.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P15 — concept reinforcement 2: механизм, границы, ошибки

```text
Усиль механизм, границы и PWG-specific failure modes.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/atlas/articles/persistent_work_graph_degradation_and_duplication_audit.md

Проверь и раскрой риски: stale graph, dependency снята без свидетельства, owner/claim создаёт ложное чувство контроля, `ready` не значит “безопасно делать”, `prime` не восстанавливает весь смысл, gate превращается в бюрократический флаг, агент учится удовлетворять граф вместо решения задачи, хранилище вводится раньше, чем нужно.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P16 — concept reinforcement 3: связь с общей теорией

```text
Свяжи статью с общей теорией, не переписывая её.

Прочитай сначала:
- work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
- work/theory-writing/fragments/A5_process_methodologies_synthesis.md
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
- work/theory-writing/fragments/A9_lifecycle_repair.md
- work/theory-writing/fragments/C1_specification_to_pwg.md
- work/theory-writing/fragments/C2_pwg_to_process_profiles.md
- work/theory-writing/fragments/C3_pwg_to_evidence.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md

Back-links должны быть смысловыми: какой вопрос общей теории помогает понять эта статья.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P17 — языковой проход 1

```text
Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/english-source-handling.md

Сделай первый языковой проход по основному тексту: русский пользовательский текст, английский только для допустимых имён, команд, файлов, статусов and source-specific названий. Не меняй аргумент и не выбрасывай фактуру.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P18 — языковой проход 2

```text
Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/english-source-handling.md

Второй языковой проход: убери английский клей, кальки и случайное смешение языков. Точные команды и названия не переводить: `bd ready`, `bd blocked`, `bd graph`, `bd prime`, Dolt, Beads, MCP, CLI. Repair-проходы дальше должны работать уже с русским текстом.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P19 — общий редакторский проход 1

```text
Оцени, насколько статья выполняет поставленную задачу. Сначала сформулируй проблемы, затем исправь их.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/atlas/articles/persistent_work_graph_readiness_report.md
- work/atlas/articles/persistent_work_graph_degradation_and_duplication_audit.md

Не ограничивайся стилем. Исправляй крупные нарушения функции статьи, структуры, фактуры, границ и визуального слоя. Проверь, что статья объясняет устойчивое состояние работы, а не Beads product overview.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P20 — общий редакторский проход 2

```text
Перечитай после первого ремонта. Сначала сформулируй проблемы, затем исправь их.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/atlas/articles/persistent_work_graph_source_transfer_ledger.md
- work/atlas/articles/persistent_work_graph_image_plan.md

Проверь последствия P19: не потерялась ли фактура, не стало ли слишком много инструментального обзора, не распался ли главный вопрос, не остались ли ключевые тезисы без технических опор.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P21 — общий редакторский проход 3

```text
Проведи адверсариальное чтение. Сначала сформулируй проблемы, затем исправь их.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/atlas/articles/persistent_work_graph_degradation_and_duplication_audit.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md

Проверь: не стала ли статья обзором Beads, повтором Gas Town, generic task-tracker essay, survey papers, или предложением конкретной реализации вместо concept-first статьи.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P22 — public/article structure and entry-sequence pass

```text
Доведи публичную структуру статьи.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/atlas/articles/persistent_work_graph_image_plan.md
- protocols/rules/human-technical-style.md
- protocols/rules/russian-language.md

Проверь headings, first screen, transitions, order of figures, captions, controlled repetition with theory, bottom section `Внешние изображения для asset-pass`. Читатель должен быстро понять, зачем нужно устойчивое состояние работы и почему transcript/TODO/ordinary issue list недостаточны. Текст должен читаться как большая самостоятельная статья, а не как ledger source transfer.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P23 — companion sync / source ledger / image queue pass

```text
Синхронизируй companion-файлы.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/atlas/articles/persistent_work_graph_source_usage.md
- work/atlas/articles/persistent_work_graph_source_transfer_ledger.md
- work/atlas/articles/persistent_work_graph_image_plan.md
- work/atlas/articles/persistent_work_graph_external_image_queue.md
- work/atlas/articles/persistent_work_graph_open_questions.md
- work/atlas/articles/persistent_work_graph_theory_links.md
- work/atlas/articles/persistent_work_graph_degradation_and_duplication_audit.md

Каждый важный источник, факт, visual candidate и theory link должен быть отражён в правильном companion-файле. Убери устаревшие долги. Ledger не должен раздуваться как coverage-бюрократия вместо переноса фактуры в основной текст.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P24 — style defect audit

```text
Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Сделай стилевой аудит без тотального переписывания. Найди реальные дефекты: смысловые свёртки, псевдотермины, кальки, тяжёлые цепочки родительного падежа, неестественные заголовки, канцелярит и обратный дефект — механическое разворачивание нормальной мысли в протокольную конструкцию. Отметь места, где правка действительно нужна, и не трогай компактные фразы, если они звучат нормально по-русски и не прячут смысл.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P25 — selective natural rewrite

```text
Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Выборочно перепиши только реально плохие места из style defect audit. Цель — нормальный русский технический текст, а не тотальное разжатие, не канцелярит и не новая компактная псевдотерминология. Можно менять заголовки, порядок слов и синтаксис; нельзя выбрасывать источниковую фактуру, команды, числа, ограничения, границы или technical anchors.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P26 — guarded final human technical style pass

```text
Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- protocols/rules/human-technical-style.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/content-preservation.md

Финально выровняй тон, ритм, переходы, подзаголовки и человеческую техническую фразу. Можно сильно менять форму, если сохраняются смысл, источниковая фактура, команды, числа, ограничения и границы. Нельзя возвращать псевдотермины, нельзя выбрасывать конкретику ради гладкости и нельзя превращать прозу в протокольные конструкции вида «кто действует / что проверяется / чем подтверждается» там, где можно сказать проще.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### Final — финальная проверка и package-readiness

```text
Проведи финальную проверку и собери result package.

Прочитай сначала:
- work/atlas/articles/persistent_work_graph.md
- work/atlas/articles/persistent_work_graph_source_usage.md
- work/atlas/articles/persistent_work_graph_source_transfer_ledger.md
- work/atlas/articles/persistent_work_graph_image_plan.md
- work/atlas/articles/persistent_work_graph_external_image_queue.md
- work/atlas/articles/persistent_work_graph_open_questions.md
- work/atlas/articles/persistent_work_graph_theory_links.md
- work/atlas/articles/persistent_work_graph_degradation_and_duplication_audit.md
- work/atlas/articles/persistent_work_graph_readiness_report.md
- work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
- protocols/rules/visual-assets-and-figures.md

Блокируй readiness, если статья стала product review Beads, повтором Gas Town, survey papers, generic task-tracker essay; если перепутаны work graph / execution graph / evidence layer; если отсутствует document-process transfer; если visual candidates из досье не получили disposition; если локальный asset не вставлен и не объяснён; если companion-файлы не синхронизированы. Упакуй результат как completed только при выполнении всех условий; иначе interrupted/blocked с отчётом.

Technical anchoring final check:
- ключевые тезисы не закрыты общей прозой там, где для понимания нужны технические опоры;
- source transfer ledger не заменяет основной текст и не заполнен общими словами;
- source-state/citation audit/control-condition mechanics раскрыты не только общими формулировками;
- source-depth and free-expansion проходы действительно перенесли фактуру, которая помогает понять механизм, границы, техническую конкретику и ограничения PWG.

Style final check:
- после style defect audit / selective rewrite не остались заметные псевдотермины и неестественные заголовки;
- текст не ушёл в обратный дефект: механическое разворачивание, тяжёлые именные группы и протокольные конструкции вместо нормальной русской технической фразы.
```

## Visual candidate disposition guarantee

Будущий article-writing package должен начинать работу с изображениями из трёх источников одновременно:

1. local asset catalogs and manifests;
2. repository-level external image candidate catalogs;
3. основное досье статьи, особенно разделы `## Кандидаты на иллюстрации`, `Кандидаты на изображения`, `image candidates` или похожие списки.

Для каждого dossier image candidate нужен disposition в `persistent_work_graph_image_plan.md`: `inserted_inline_external_placeholder`, `external_queue_only`, `deferred`, `rejected`, `superseded_by_local_asset`, `not_found_in_source`, с короткой причиной.

Если кандидат нужен статье, пакет должен поставить inline `<figure data-asset-status="external-real-candidate">` там, где изображение будет использоваться, и отразить тот же пункт в нижнем разделе `Внешние изображения для asset-pass` и в `persistent_work_graph_external_image_queue.md`.

Если релевантный local asset уже существует, действует insert-or-explain: вставить как `<figure><img ...></figure>` по месту применения или явно отклонить с причиной. Реальную картинку, screenshot, diagram, template, table или local asset нельзя заменять синтетической текстовой схемой без явного решения пользователя.

## Prompt-record manifest for package builder

Каждый пункт ниже должен стать отдельным gated prompt record. Нельзя оставлять сгруппированные диапазоны вроде `P04–P08` или `P17–P19` одним record.

```text
P01 — первичный концептуальный черновик статьи
P02 — article contract and boundaries
P03 — dossier inventory
P04 — source-depth 1: почему task/TODO/transcript недостаточны
P05 — source-depth 2: минимальные свойства устойчивой единицы работы
P06 — source-depth 3: Beads как anchor и проверка механизма
P07 — source-depth 4: границы с issue tracker, durable execution, CRDT/STORM, Gas Town
P08 — source-depth 5: перенос на многопроходный документный процесс
P09 — свободный добор материала 1
P10 — свободный добор материала 2
P11 — visual asset pass 1: локальные готовые изображения
P12 — visual asset pass 2: внешние реальные изображения-кандидаты
P13 — visual asset pass 3: редкие синтетические схемы
P14 — concept reinforcement 1: самостоятельность статьи
P15 — concept reinforcement 2: механизм, границы, ошибки
P16 — concept reinforcement 3: связь с общей теорией
P17 — языковой проход 1
P18 — языковой проход 2
P19 — общий редакторский проход 1
P20 — общий редакторский проход 2
P21 — общий редакторский проход 3
P22 — public/article structure and entry-sequence pass
P23 — companion sync / source ledger / image queue pass
P24 — style defect audit
P25 — selective natural rewrite
P26 — guarded final human technical style pass
Final — финальная проверка, упаковка, readiness status
```

## Companion/output invariants

Будущий package обязан:

- обновлять source usage и source transfer ledger при первом внесении каждого внешнего факта, команды, схемы, ограничения, paper result или visual candidate;
- различать source-backed factual transfer и project-design synthesis;
- сохранять реальные diagrams/screenshots как local assets или external-real placeholders, а не пересказывать их текстом;
- использовать synthetic figures только для нетривиального объяснения механизма/границы;
- держать open questions вокруг store choice, JSON/SQLite/Dolt boundary, gate visibility, read snapshot, write validation, source-state storage, branch/merge и agent gaming of state;
- поддерживать theory links с A4/B2/B3/C1–C4/C5/A10.

## Final verification future package must block readiness if

- статья стала Beads product overview;
- статья повторяет Gas Town вместо извлечения PWG mechanism;
- work graph, execution graph, evidence layer и shared-editing coordination смешаны;
- ordinary issue tracking представлен как достаточный без анализа ready queue / owner / control condition / recovery;
- Taskmaster/JSON либо отвергнут слишком рано, либо представлен как эквивалент Dolt/Beads без tradeoffs;
- CRDT/STORM/MAST/Anthropic materials стали survey вместо boundary/supporting evidence;
- перенос на многопроходный документный процесс отсутствует или превратился в coding plan;
- source-state/citation audit/control-condition mechanics отсутствуют;
- - visual candidates из досье не получили disposition;
- локальный asset не вставлен и не объяснён;
- companion files out of sync;
- после style defect audit / selective rewrite остались заметные псевдотермины, machine-like English glue, тяжёлое механическое разворачивание или неестественные заголовки;

## Readiness

Статус после ремонта плана: `ready_for_package_manufacture_after_manual_review`.

C5 и A10 доступны как read-only context. Они не являются pending blockers. Если future article-writing package обнаружит конкретное расхождение с concept atlas или mode-selection map, оно фиксируется как конкретный debt в open questions/audit, а не как default sync pending.
