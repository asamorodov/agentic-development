# Target-group plan: статья атласа `gas_town` — Gas Town

Статус: `ready_for_package_manufacture_after_manual_review`.  
Article id: `gas_town`  
Readiness status: `ready_for_package_manufacture_after_manual_review`.  
Рабочее название: `Gas Town`  
Уровень статьи: `core concept / organizational article`  
Режим будущего пакета: самодостаточный writing package.  
Внутренних ограничений объёма нет.

## 1. Назначение статьи

Статья должна объяснить Gas Town как попытку превратить множество агентных запусков в наблюдаемую, ограниченную, восстанавливаемую и управляемую рабочую среду. Главный вопрос читателя: **какие организационные механизмы становятся необходимы, когда агентная работа перестаёт помещаться в один чат, один worktree, одного исполнителя и ручное наблюдение?**

Gas Town важен не потому, что позволяет запустить много агентов. Флот агентов создаёт не только больше параллельности, но и новые проблемы: видимость, очередь, право запуска, насыщение, столкновения, восстановление, проверка, стоимость координации и человеческая ответственность. Статья должна показывать, как рост этого давления порождает механизмы: Beads/state, роли, очереди, диспетчеризацию, recovery, observability, backpressure and human decision surfaces.

## 2. Article contract

Главное досье:

```text
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
```

Статья должна раскрыть:

- почему один агент, один чат, один worktree и ручная координация перестают удерживать long-running parallel agentic development;
- как Beads даёт рабочую память и граф задач, но не исчерпывает Gas Town;
- как Gas Town строит организационную среду вокруг состояния работы: Town/Rig, Mayor, Crew, Polecats, Refinery, Witness, Deacon, Dogs, scheduler, queue, hooks, service agents, recovery, observability, backpressure, human surfaces;
- как MEOW, GUPP, molecules, formulas, gates and wisps работают как грамматика управления работой, а не как декоративные названия;
- как execution/backpressure/recovery/observability/costs доказывают, что fleet-based work требует собственной среды;
- какие ограничения и failure modes возникают: стоимость наблюдения, sync/merge friction, operation-log gap, local-first limits, responsibility bottleneck, роли как имитация процесса, recovery без восстановления смысла;
- что можно осторожно перенести в многопроходный документный процесс: очередь, heartbeat, watchdog, service pass, recovery, state, human responsibility surface — без попытки скопировать Gas Town как implementation plan.

Границы:

- Beads — рабочая память и task graph внутри Gas Town;
- PWG — переносимый механизм устойчивого состояния работы;
- Gas Town — operating environment вокруг многих агентов и рабочих единиц;
- BMAD/GSD — process profiles, а не fleet workspace;
- generic multi-agent research — полезный фон, но не замена конкретной developer workspace с costs, sync-risk and human bottlenecks.

Статья не должна стать Gas Town glossary, Beads/PWG duplicate, multi-agent hype piece, product tutorial или implementation plan for the user's loop framework.

## 3. Фактура без coverage-бюрократии

Gas Town-статья опирается на досье и первоисточники, но package не должен снова превращать перенос фактуры в coverage/disposition-бюрократию. Жёсткий режим `dossier-backed completeness / relevant but untransferred` считается откатанным: не нужно строить тотальную matrix по всему досье и доказывать статус каждого релевантного фрагмента.

Мягкий ориентир остаётся: ключевые тезисы статьи должны иметь технические опоры. Если раздел объясняет роль Beads, scheduler, queue, Mayor/Crew/Polecats/Witness, service loops, recovery, observability, backpressure, cost или human decision surface, читателю обычно нужны конкретные детали: команда, статус, файл, пример, UI/diagram-кандидат, ограничение или source-specific наблюдение. Если без такой опоры раздел звучит общей прозой, деталь лучше встроить в основной текст. Если деталь не помогает reader question, относится к соседней статье или ломает ход объяснения, её не нужно вставлять ради отчётности.

`source_transfer_ledger`, `image_plan` и `open_questions` остаются журналами реальных решений, долгов и source gaps. Они не заменяют статью и не должны становиться главным результатом прохода.

## 4. Предполагаемая форма будущей статьи

1. Давление масштаба: почему один агент/чат/worktree/наблюдатель перестают работать.
2. Beads как первая форма устойчивого состояния работы, но не весь Gas Town.
3. Work grammar: MEOW, GUPP, molecules, formulas, gates, wisps как операционные функции.
4. Spaces and roles: Town/Rig/Mayor/Crew/Polecats/Refinery/Witness/Deacon/Dogs как распределение видимости, исполнения, проверки, recovery and service loops.
5. Execution and backpressure: queue, scheduler, dispatch, pressure checks, FIX_NEEDED, awaiting_verdict, convoys.
6. Recovery and observability: hooks, `bd prime`, compaction recovery, dashboard, telemetry, shadow DB, locks, diagnostics, operation-log gap.
7. Costs and failures: fleet cost, sync/merge friction, local-first limits, responsibility bottleneck, role theater, recovery without full meaning.
8. Boundaries: Gas Town vs PWG, Beads, BMAD, GSD, generic multi-agent research and ordinary task management.
9. Transferable lessons for multi-pass document process: borrow primitives under pressure, not copy Gas Town.
10. Visual synthesis: architecture/workflow/Mayor/Beads images show system shape and human surface.

## 5. Обрабатываемые файлы будущего article package

```yaml
- path: work/atlas/articles/gas_town.md
  status: future
  role: primary
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/gas_town_source_usage.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/gas_town_source_transfer_ledger.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/gas_town_image_plan.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/gas_town_external_image_queue.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/gas_town_open_questions.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/gas_town_theory_links.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/gas_town_degradation_and_duplication_audit.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
- path: work/atlas/articles/gas_town_readiness_report.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
```

Group mode: `linked-target-edit`.

## 6. Exact read-only inputs to bundle

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
protocols/rules/russian-language.md
protocols/rules/terminology-and-translation.md
protocols/rules/english-source-handling.md
protocols/rules/content-preservation.md
protocols/rules/source-and-provenance.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
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
content/assets/theory-images/gastown-mayor-hub.webp
content/assets/theory-images/anthropic-multi-agent-process-diagram.webp
content/assets/theory-images/anthropic-multi-agent-research-architecture.webp
work/atlas/target-group-plans/gas_town_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

Эти входы должны быть упакованы в future self-contained package. План не должен полагаться на неявный доступ к репозиторию, vague `relevant files` или отсутствие тяжёлых assets в текущем чате. Если путь не существует при сборке пакета, package-builder должен остановиться или зафиксировать конкретный blocker.

## 7. Очередь будущего article-writing package

Выбран полный atlas-queue shape: `P01`–`P26` + `Final`. Для Gas Town это оправдано: это core organizational article с большим досье, локальными assets, внешними image candidates, специфическим языком ролей и высоким риском деградации в role glossary / Beads duplicate / multi-agent hype.

### P01 — первичный концептуальный черновик статьи

```text
Создай первый полный черновик статьи `work/atlas/articles/gas_town.md` и skeleton/status для всех companion-файлов.

Прочитай сначала:
- work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
- work/theory-writing/fragments/B2_pwg_contribution.md
- work/theory-writing/fragments/C2_pwg_to_process_profiles.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/A10_mode_selection_map.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Статья должна начинаться с вопроса: какие организационные механизмы становятся необходимы, когда агентная работа перестаёт помещаться в один чат, один worktree, одного исполнителя и ручное наблюдение? Не пиши глоссарий ролей и не повторяй PWG/Beads. Пиши core organizational article о рабочей среде для supervised fleets of coding agents. Не ограничивай объём искусственно и не закрывай нехватку фактуры гладкой общей прозой.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P02 — article contract and boundaries

```text
Укрепи article contract внутри статьи и companion-файлов.

Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/theory-writing/fragments/B2_pwg_contribution.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
- work/theory-writing/fragments/C2_pwg_to_process_profiles.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md

Зафиксируй границы: Beads — рабочая память и граф задач; PWG — переносимый механизм устойчивого состояния работы; Gas Town — среда, где вокруг этого состояния появляются роли, очереди, диспетчеризация, recovery, service agents, observability, resource limits и human decision points. Статья не должна стать PWG duplicate, Beads product tutorial, BMAD/GSD process-profile essay или multi-agent hype.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P03 — dossier inventory

```text
Сделай inventory досье без тотальной coverage matrix.

Прочитай сначала:
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/atlas/articles/gas_town.md
- work/atlas/articles/gas_town_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Отметь, что уже перенесено, что осталось неперенесённым, что требует открытия первоисточников, где будущей статье могут не хватать технические опоры. Обнови основной текст только при явном пропуске article-critical материала. Запиши результат в `gas_town_source_transfer_ledger.md` and `gas_town_source_usage.md`.

Не строй тотальную coverage matrix по всему досье. Ledger должен помогать статье, а не заменять её.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P04 — source-depth 1: почему один агент и ручная координация перестают работать

```text
Раскрой исходное давление: один агент, один чат, один worktree, один человек-наблюдатель и ручная координация перестают удерживать долгую параллельную agentic development работу.

Прочитай сначала:
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/theory-writing/fragments/A6_execution_environment_distinctions.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md

Покажи конкретно: потеря видимости, насыщение внимания, конфликтующие worktrees/branches, ожидание verdict, stalled agents, sync/merge friction, need for service loops. Если ключевой тезис остаётся общей прозой, добавь техническую опору в основной текст, а не в отдельную отчётность.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P05 — source-depth 2: Beads как первый ответ на потерю состояния

```text
Раскрой Beads как первый ответ на потерю состояния и координации, но не как весь Gas Town.

Прочитай сначала:
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/theory-writing/fragments/B2_pwg_contribution.md
- content/assets/theory-images/beads-task-graph-memory.svg

Покажи, что Beads даёт graph/state/ready/gates/dependencies/prime/recovery, но Gas Town появляется, когда вокруг графа нужны роли, очередь, dispatch, monitoring, service agents and human surfaces. Не превращай это в Beads tutorial.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P06 — source-depth 3: work grammar как операционные функции

```text
Раскрой MEOW, GUPP, molecules, formulas, gates, wisps не как забавные слова, а как рабочую грамматику: что они делают с единицами работы, зависимостями, долговечностью, проверкой, восстановлением или масштабом.

Прочитай сначала:
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/atlas/articles/gas_town.md

Для каждого яркого термина объясняй операционную функцию. Если термин не помогает понять работу, не раздувай глоссарий. Технические детали должны работать на линию статьи, а не на демонстрацию охвата досье.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P07 — source-depth 4: пространства и роли как распределение функций

```text
Раскрой Town/Rig/Mayor/Crew/Polecats/Refinery/Witness/Deacon/Dogs как распределение функций: видимость, запуск, исполнение, review, recovery, сервисные циклы, проверка, человеческое решение.

Прочитай сначала:
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- content/assets/theory-images/gastown-mayor-hub.webp
- work/theory-writing/fragments/A8_authority_to_act_vs_complete.md

Не подавай роли как персонажей. Каждая роль должна отвечать на вопрос: какую проблему масштаба она снимает и какую новую цену создаёт?
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P08 — source-depth 5: execution, backpressure, recovery, observability, cost

```text
Раскрой scheduler, queue, dispatch, pressure checks, FIX_NEEDED, awaiting_verdict, convoys, hooks, `bd prime`, compaction recovery, dashboard, telemetry, shadow DB, locks, diagnostics, operation-log gap, local-first limits, merge/sync friction, fleet cost and responsibility bottleneck.

Прочитай сначала:
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- content/assets/theory-images/gastown-architecture.svg
- content/assets/theory-images/gastown-basic-workflow.svg

Покажи, что scheduler/backpressure/recovery/observability — не appendix, а доказательство сложности fleet-based work. Здесь особенно важно не потерять команды, статусы, ограничения, UI/diagram details и failure modes, которые дают статье технические опоры.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P09 — свободный добор материала 1

```text
Свободно перечитай статью и сам найди самый слабый участок фактуры.

Прочитай сначала:
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/atlas/articles/gas_town.md
- work/atlas/articles/gas_town_source_transfer_ledger.md

Добери commands, roles, states, changelog evidence, UI/dashboard material, operation logs, queue/scheduler details, cost/failure details or critique. Не превращай проход в стилистику. Расширь основной текст и companion-файлы.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P10 — свободный добор материала 2

```text
Свободно перечитай статью и сам найди самый слабый участок концептуальной связности.

Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
- work/theory-writing/fragments/C2_pwg_to_process_profiles.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md

Усиль линию «рост давления → механизм»: ручное управление → Beads/state → roles → queue/dispatch → recovery/observability → backpressure/cost → human responsibility. Не сокращай; добавляй недостающую фактуру и объяснение.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

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
- content/assets/theory-images/gastown-mayor-hub.webp
- content/assets/theory-images/anthropic-multi-agent-process-diagram.webp
- content/assets/theory-images/anthropic-multi-agent-research-architecture.webp
- work/atlas/articles/gas_town.md

Приоритеты: architecture/town shape, workflow/queue, Mayor hub / human surface, Beads task graph as work memory, cautious analogy with multi-agent diagrams only if it helps the argument. Подпись объясняет смысл изображения для статьи, не историю восстановления файла.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P12 — visual asset pass 2: внешние реальные изображения-кандидаты

```text
Обработай внешние реальные картинки и картинки из досье.

Прочитай сначала:
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
- work/atlas/articles/gas_town.md

Начни с раздела досье `## Кандидаты на иллюстрации` и похожих списков. Для каждого кандидата запиши disposition в `gas_town_image_plan.md`: `inserted_inline_external_placeholder`, `external_queue_only`, `deferred`, `rejected`, `superseded_by_local_asset`, `not_found_in_source`. Если кандидат нужен в статье, поставь inline `<figure data-asset-status="external-real-candidate">` по месту применения и продублируй его в нижнем разделе `Внешние изображения для asset-pass` и в `gas_town_external_image_queue.md`. Внешние источники можно искать и открывать для проверки/картинок; предпочтение первоисточникам.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P13 — visual asset pass 3: редкие синтетические схемы

```text
Создай только те собственные схемы, которые действительно нетривиальны и не подменяют готовые изображения.

Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/atlas/articles/gas_town_image_plan.md

Допустимые сильные кандидаты: pressure-to-mechanism stack; Beads vs Gas Town; role-function map; dispatch/backpressure lifecycle; recovery/observability loop; human responsibility surface. Не делай схемы ради визуального разнообразия.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P14 — concept reinforcement 1: самостоятельность статьи

```text
Сделай статью полностью самостоятельной для читателя, который пришёл за Gas Town без чтения всей теории.

Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md

Разрешён контролируемый повтор с теорией, если он нужен для понимания. Нельзя превращать статью во вторую теорию, роль-глоссарий или technical appendix.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P15 — concept reinforcement 2: механизм, границы, ошибки

```text
Усиль механизм, границы и Gas Town-specific failure modes.

Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/atlas/articles/gas_town_degradation_and_duplication_audit.md

Проверь риски: fleet увеличивает не только скорость, но и стоимость наблюдения; очередь скрывает ответственность; scheduler/backpressure выглядят как автоматическое управление, но решения остаются за человеком; roles становятся театром, если не меняют работу; recovery восстанавливает процесс, но не весь смысл ситуации; local-first/worktree/merge friction ограничивают масштаб; operation-log gap делает систему менее наблюдаемой, чем кажется; Gas Town слишком тяжёл для малой работы.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P16 — concept reinforcement 3: связь с общей теорией

```text
Свяжи статью с общей теорией, не переписывая её.

Прочитай сначала:
- work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
- work/theory-writing/fragments/A5_process_methodologies_synthesis.md
- work/theory-writing/fragments/A6_execution_environment_distinctions.md
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
- work/theory-writing/fragments/A9_lifecycle_repair.md
- work/theory-writing/fragments/B2_pwg_contribution.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
- work/theory-writing/fragments/C2_pwg_to_process_profiles.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md

Back-links должны быть смысловыми: какой вопрос общей теории помогает понять Gas Town и какой вопрос Gas Town помогает прояснить в теории.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P17 — языковой проход 1

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/english-source-handling.md

Сделай языковой проход по основному тексту: русский пользовательский текст, английский только для допустимых имён, команд, файлов, статусов и source terms вроде Mayor, Polecat, Witness, MEOW, GUPP, FIX_NEEDED, awaiting_verdict. Не меняй аргумент и не выбрасывай фактуру.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P18 — языковой проход 2

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/terminology-and-translation.md

Второй языковой проход: найди остаточный английский клей, кальки, неровные русские формулы и mixed-language labels в prose/captions. Особое внимание: operational pressure, work grammar, human surfaces, data/control plane, durable substrate, backpressure, recovery as ordinary prose. Точные source labels не переводить, но объяснять их функцию по-русски.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P19 — общий редакторский проход 1

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/atlas/articles/gas_town_source_transfer_ledger.md
- work/atlas/articles/gas_town_image_plan.md
- work/atlas/articles/gas_town_degradation_and_duplication_audit.md
- protocols/rules/human-technical-style.md
- protocols/rules/russian-language.md
- protocols/rules/content-preservation.md

Оцени, насколько статья выполняет поставленную задачу уже после языковой нормализации. Сначала сформулируй проблемы, затем исправь их. Не проводи визуальный pass под видом редакторского. Новый и переписанный текст должен сразу соблюдать языковые правила и не возвращать английский клей. Заверши regression audit и readiness status в `gas_town_degradation_and_duplication_audit.md`.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P20 — общий редакторский проход 2

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/atlas/articles/gas_town_degradation_and_duplication_audit.md
- protocols/rules/human-technical-style.md
- protocols/rules/russian-language.md
- protocols/rules/content-preservation.md

Повтори общий editorial repair после предыдущих правок. Проверь структуру, причинность, границы, source loss, duplicated work and publication readiness. Исправь реальные дефекты; не сокращай фактуру ради гладкости и не превращай статью в ledger-summary.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P21 — общий редакторский проход 3

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/atlas/articles/gas_town_source_usage.md
- work/atlas/articles/gas_town_image_plan.md
- work/atlas/articles/gas_town_degradation_and_duplication_audit.md
- protocols/rules/human-technical-style.md
- protocols/rules/russian-language.md

Проверь, не стала ли статья Beads/PWG duplicate, role glossary, generic multi-agent hype, implementation plan или кратким конспектом. Дополнительно проверь, хватает ли ключевым тезисам технических опор в основном тексте. Исправь только реальные дефекты и зафиксируй readiness.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P22 — public/article structure and entry-sequence pass

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- protocols/rules/human-technical-style.md
- protocols/rules/russian-language.md

Проверь структуру публичной статьи: H1 должен называть Gas Town, первые абзацы должны сначала объяснять проблему масштаба и рабочий механизм Gas Town, а taxonomy/role glossary/atlas-boundary не должны перегружать вход раньше, чем читатель получил опору. Проверь подзаголовки, путь читателя, placement фигур, подписи и отсутствие executor meta-text. Добавляй или убирай подзаголовки только если это помогает видеть смысловые границы. Не превращай текст в список ролей.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P23 — companion sync

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/atlas/articles/gas_town_source_usage.md
- work/atlas/articles/gas_town_source_transfer_ledger.md
- work/atlas/articles/gas_town_image_plan.md
- work/atlas/articles/gas_town_external_image_queue.md
- work/atlas/articles/gas_town_open_questions.md
- work/atlas/articles/gas_town_theory_links.md
- work/atlas/articles/gas_town_degradation_and_duplication_audit.md

Синхронизируй companion-файлы со статьёй. Удали устаревшие долги, сохрани настоящие blockers, не оставляй стандартных `C5/A10 sync pending`: C5 и A10 доступны как read-only context, а любые проблемы должны быть конкретными долгами статьи. Проверь, что source usage, image plan, external image queue и theory links соответствуют фактической статье. Ledger не должен раздуваться как coverage-бюрократия вместо переноса фактуры в основной текст.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P24 — style defect audit

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Сделай стилевой аудит без тотального переписывания. Найди реальные дефекты: смысловые свёртки, псевдотермины, кальки, тяжёлые цепочки родительного падежа, неестественные заголовки, канцелярит и обратный дефект — механическое разворачивание нормальной мысли в протокольную конструкцию. Отметь места, где правка действительно нужна, и не трогай компактные фразы, если они звучат нормально по-русски и не прячут смысл.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P25 — selective natural rewrite

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Исправь только выбранные стилевые дефекты. Не переписывай всю статью ради красоты, не заменяй конкретику гладким summary и не превращай сильные технические места в таблицы без необходимости. Если фраза плоха, скажи её нормальным русским техническим текстом: иногда раскрыть, иногда сократить, иногда перестроить предложение или заголовок. Сохрани факты, команды, числа, source labels, границы и техническую плотность.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### P26 — guarded final human technical style pass

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- protocols/rules/human-technical-style.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/content-preservation.md

Финально выровняй тон, ритм, переходы, подзаголовки и человеческую техническую фразу. Можно сильно менять форму, если сохраняются смысл, источниковая фактура, команды, числа, ограничения и границы. Нельзя возвращать псевдотермины, нельзя выбрасывать конкретику ради гладкости и нельзя превращать прозу в протокольные конструкции вида «кто действует / что проверяется / чем подтверждается» там, где можно сказать проще.
```

Required companion update: если проход добавляет, переносит или удаляет фактуру, источник, границу, изображение, схему, роль или тезис, синхронизируй `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue`, `open_questions`, `theory_links` и audit-файлы.

### Final — финальная проверка и package-readiness

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/atlas/articles/gas_town_source_usage.md
- work/atlas/articles/gas_town_source_transfer_ledger.md
- work/atlas/articles/gas_town_image_plan.md
- work/atlas/articles/gas_town_external_image_queue.md
- work/atlas/articles/gas_town_open_questions.md
- work/atlas/articles/gas_town_theory_links.md
- work/atlas/articles/gas_town_degradation_and_duplication_audit.md
- work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
- protocols/rules/visual-assets-and-figures.md

Проверь реальные файлы будущего результата: основной article file создан и не пуст; все companion-файлы из секции обрабатываемых файлов существуют и синхронизированы; source usage и source transfer ledger заполнены; внешние факты имеют provenance; локальные assets вставлены как `<figure><img ...></figure>`; external real candidates имеют inline placeholders, нижний раздел `Внешние изображения для asset-pass` и запись в external image queue; synthetic figures редки и проходят usefulness/nontriviality gate; controlled repetition с теорией оправдан; статья не является role glossary, Beads/PWG duplicate, generic multi-agent hype, implementation plan или складом технических деталей. Запиши `gas_town_readiness_report.md`, MANIFEST/VERIFY/RESUME для package output и финальный readiness status.

Technical anchoring final check:
- ключевые тезисы не закрыты одной общей прозой там, где для понимания нужны технические опоры;
- source transfer ledger не заменяет основной текст и не заполнен общими словами;
- image plan / external queue фиксируют реальные visual decisions, а не скрывают полезные candidates от статьи;
- source-depth and free-expansion проходы действительно перенесли фактуру, которая помогает понять механизм, границы, техническую конкретику и ограничения Gas Town.

Style final check:
- после style defect audit / selective rewrite не остались заметные псевдотермины и неестественные заголовки;
- текст не ушёл в обратный дефект: механическое разворачивание, тяжёлые именные группы и протокольные конструкции вместо нормальной русской технической фразы.
```

## Visual candidate disposition guarantee

Будущий article-writing package должен начинать работу с изображениями из трёх источников одновременно:

1. local asset catalogs and manifests;
2. repository-level external image candidate catalogs;
3. основное досье статьи, особенно разделы `## Кандидаты на иллюстрации`, `Кандидаты на изображения`, `image candidates` или похожие списки.

Для каждого dossier image candidate нужен disposition в `gas_town_image_plan.md`: `inserted_inline_external_placeholder`, `external_queue_only`, `deferred`, `rejected`, `superseded_by_local_asset`, `not_found_in_source`, с короткой причиной.

Если кандидат нужен статье, пакет должен поставить inline `<figure data-asset-status="external-real-candidate">` там, где изображение будет использоваться, и отразить тот же пункт в нижнем разделе `Внешние изображения для asset-pass` и в `gas_town_external_image_queue.md`.

Если релевантный local asset уже существует, действует insert-or-explain: вставить как `<figure><img ...></figure>` по месту применения или явно отклонить с причиной. Реальную картинку, screenshot, diagram, template, table или local asset нельзя заменять синтетической текстовой схемой без явного решения пользователя.

## Prompt-record manifest for package builder

Каждый пункт ниже должен стать отдельным gated prompt record. Нельзя оставлять сгруппированные диапазоны вроде `P04–P08` или `P17–P19` одним record.

```text
P01 — primary article draft
P02 — article contract and boundaries
P03 — dossier inventory
P04 — source-depth pass 1
P05 — source-depth pass 2
P06 — source-depth pass 3
P07 — source-depth pass 4
P08 — source-depth pass 5 / anti-summary check
P09 — free material-expansion pass 1
P10 — free material-expansion pass 2
P11 — visual asset pass 1: local assets
P12 — visual asset pass 2: external real image candidates
P13 — visual asset pass 3: rare nontrivial synthetic figures
P14 — concept reinforcement 1: standalone concept explanation
P15 — concept reinforcement 2: mechanism, boundaries, typical mistakes
P16 — concept reinforcement 3: links to broader theory without rewriting it
P17 — language pass 1
P18 — language pass 2
P19 — general editorial pass 1
P20 — general editorial pass 2
P21 — general editorial pass 3
P22 — public/article structure and entry-sequence pass
P23 — companion sync / source ledger / image queue pass
P24 — style defect audit
P25 — selective natural rewrite
P26 — guarded final human technical style pass
Final — final verification, package output, readiness status
```

## Companion/output invariants

Будущий package обязан:

- обновлять source usage и source transfer ledger при первом внесении каждого внешнего факта, команды, роли, статуса, caveat, changelog detail или visual candidate;
- переводить source labels в операционные функции: что термин делает с работой, состоянием, очередью, зависимостью, проверкой, recovery или ответственностью;
- сохранять реальные diagrams/screenshots как local assets или external-real placeholders, а не пересказывать их текстом;
- использовать synthetic figures только для нетривиального объяснения mechanism/boundary;
- поддерживать open questions вокруг Beads/Gas Town boundary, Witness maturity, hooks reliability, operation-log gap, local-first limits, fleet cost, sync/merge friction and document-process transfer;
- поддерживать theory links с B2/B3/C2/C4/C5/A10.

## Final verification future package must block readiness if

- статья стала role glossary;
- статья стала Beads/PWG duplicate;
- статья стала generic multi-agent hype or product tutorial;
- roles представлены как персонажи, а не функции;
- scheduler/backpressure/recovery/observability missing or generic;
- costs, sync-risk, operation-log gap and responsibility bottleneck missing;
- critique/costs appended only at end and do not shape interpretation;
- transfer to the user's document process becomes implementation plan rather than transferable lessons;
- ключевые тезисы закрыты общей прозой там, где для понимания нужны технические опоры;
- source transfer ledger заменяет основной текст или превращается в coverage-бюрократию;
- visual candidates из досье не получили disposition;
- local asset не вставлен и не объяснён;
- companion files out of sync;
- после style defect audit / selective rewrite остались заметные псевдотермины, machine-like English glue, тяжёлое механическое разворачивание или неестественные заголовки.

## Readiness

Статус после ремонта плана: `ready_for_package_manufacture_after_manual_review`.

C5 и A10 доступны как read-only context. Они не являются pending blockers. Если future article-writing package обнаружит конкретное расхождение с concept atlas или mode-selection map, оно фиксируется как конкретный debt в open questions/audit, а не как default sync pending.
