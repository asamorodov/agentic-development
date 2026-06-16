# План целевой группы — Глава IX: исполнение, среда агента, инструменты и права

Статус: рабочий план для пакета главы.  
Режим внешнего поиска: `D3`; тип пакета — `discovery_heavy / asset_heavy`.  
Основание: Skeleton V5, `00_spine_map`, послеатласные карты маршрутизации, обновлённый blueprint и материалы главы IX.

## 1. Зачем нужна эта глава

Глава IX должна показать, что способ продолжения работы из VIII становится реальным только в конкретной среде исполнения. Агент не действует “в проекте вообще”: он читает файлы, меняет `worktree`, запускает команды, открывает браузер, вызывает инструменты, иногда выходит к внешнему сервису или MCP-серверу. У каждого такого шага свой радиус последствий и свой риск.

Главная линия главы: технически возможное действие ещё не означает, что действие допустимо в этой фазе работы. Среда может разрешить команду, человек может подтвердить один запуск, sandbox может ограничить последствия, но из этого не следует, что результат проверен или принят проектом.

Глава должна развести несколько близких вещей: что агент может увидеть; что он может изменить локально; где начинается действие с внешними последствиями; что требует подтверждения; что должно быть полностью недоступно; какой след оставляет среда исполнения; почему этот след ещё не является проверочным основанием и не даёт права принять результат.

Рабочая формула главы: PWG показывает, где находится работа; способ продолжения показывает, как её вести; IX показывает, что агенту реально можно делать в среде исполнения и где это действие нужно ограничить, подтвердить или остановить.

План задаёт работу, а не готовый текст главы. Исполнитель не должен переносить формулировки плана в основной текст без переписывания. Все выходные материалы — сама глава, журналы поиска, реестры, отчёты и проходы — пишутся нормальным русским языком. Технические имена файлов, команд, моделей, методов и полей сохраняются точно там, где это нужно для источника.

У главы нет целевого объёма, нормальной длины и скрытого ориентира вроде 40 тысяч знаков. Текст должен стать таким длинным, каким требует исходный материал: плотность источников, число важных различений, количество нужных сцен, визуальный слой и объём фактуры из Атласа, досье, фрагментов, историй и внешних источников. Если после первого черновика остаются значимые недоразобранные источники или тонкие места, работу нужно продолжать, а не полировать прежний объём.


## 2. Границы главы

Глава не должна стать каталогом sandbox, permissions, approvals, worktrees, browser, MCP и durable workflows. Эти механизмы важны только потому, что они отвечают на общий вопрос: где агент действует, что он может затронуть, где требуется подтверждение и какой след остаётся после действия.

IX также не должна забирать тему XI и XII. Среда исполнения производит материал о том, что агент делал: команды, логи, tool calls, browser snapshots, approvals, изменения в рабочем дереве. Но этот материал становится проверочным основанием только тогда, когда его связывают с обещанием изменения, областью проверки и правом принятия. А право принять результат будет разобрано позже отдельно.

Durable execution нужно держать в границах. LangGraph, Temporal, DBOS, Restate и соседние подходы помогают продолжать выполнение, повторять шаги, переживать сбой процесса или оркестрировать долгую операцию. Но они сами по себе не хранят принятое намерение, достаточность свидетельств и право закрыть изменение.

## 3. Целевые файлы

Основной выход:

```text
work/theory-writing/chapters/IX_execution_environment_runtime_rights.md
```

Сопутствующие файлы:

```text
work/theory-writing/chapters/IX_execution_environment_runtime_rights_source_register.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights_fragment_usage.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights_atlas_usage.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights_dossier_gap_notes.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights_external_discovery_log.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights_story_anchors.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights_figure_candidates.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights_open_questions.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights_degradation_and_duplication_audit.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights_readiness_report.md
```

Проходы пакета пишутся в:

```text
work/theory-writing/chapters/IX_execution_environment_runtime_rights_passes/
```

Пиши создаваемый текст естественным русским языком. Это относится к главе, рабочим заметкам, журналам поиска, реестрам, отчётам, сопутствующим файлам и записям в проходах.

Формулировки этого плана не являются текстом главы. План задаёт работу и критерии, но не даёт готовые фразы для переноса в основной текст.

## 4. Входные файлы только для чтения

Управляющие документы:

```text
START.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/theory-writing/fragments/00_spine_map.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_LIST_AND_SCOPE_MAP.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md
work/theory-writing/reports/POST_ATLAS_ATLAS_TO_CHAPTER_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_FRAGMENT_TO_CHAPTER_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_DOSSIER_TO_CHAPTER_GAP_MAP.md
work/theory-writing/reports/POST_ATLAS_STORY_ANCHOR_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_SOURCE_DISCOVERY_MAP.md
work/theory-writing/reports/POST_ATLAS_VISUAL_CANDIDATE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md
```

Фрагменты:

```text
work/theory-writing/fragments/A6_execution_environment_distinctions.md
work/theory-writing/fragments/A6_source_usage.md
work/theory-writing/fragments/A6_story_anchor_map.md
work/theory-writing/fragments/A6_figure_candidates.md
work/theory-writing/fragments/A6_open_questions.md
work/theory-writing/fragments/A6_degradation_and_duplication_audit.md
work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
work/theory-writing/fragments/C4_source_usage.md
work/theory-writing/fragments/C4_story_anchor_map.md
work/theory-writing/fragments/C4_figure_candidates.md
work/theory-writing/fragments/C4_open_questions.md
work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

Статьи Атласа и связанные файлы:

```text
work/atlas/articles/gsd_open_gsd.md
work/atlas/articles/gsd_open_gsd_theory_links.md
work/atlas/articles/gsd_open_gsd_source_usage.md
work/atlas/articles/gsd_open_gsd_image_plan.md
work/atlas/articles/gsd_open_gsd_external_image_queue.md
work/atlas/articles/gsd_open_gsd_open_questions.md
work/atlas/articles/bmad_method.md
work/atlas/articles/bmad_method_theory_links.md
work/atlas/articles/bmad_method_source_usage.md
work/atlas/articles/bmad_method_image_plan.md
work/atlas/articles/bmad_method_external_image_queue.md
work/atlas/articles/bmad_method_open_questions.md
work/atlas/articles/persistent_work_graph.md
work/atlas/articles/persistent_work_graph_theory_links.md
work/atlas/articles/persistent_work_graph_source_usage.md
work/atlas/articles/persistent_work_graph_image_plan.md
work/atlas/articles/persistent_work_graph_external_image_queue.md
work/atlas/articles/persistent_work_graph_open_questions.md
work/atlas/articles/gas_town.md
work/atlas/articles/gas_town_theory_links.md
work/atlas/articles/gas_town_source_usage.md
work/atlas/articles/gas_town_image_plan.md
work/atlas/articles/gas_town_external_image_queue.md
work/atlas/articles/gas_town_open_questions.md
```

Досье:

```text
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
```

Истории и досье историй:

```text
content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
```

Начальные темы внешнего поиска:

```text
LangGraph durable execution
Temporal workflows
DBOS
Restate
HumanLayer human-in-the-loop
Sandvault worktrees sandbox
Codex AGENTS.md
Claude Code hooks
MCP docs
subagents
devbox agent runtime
```

Правила языка, стиля, источников и изображений:

```text
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/terminology-and-translation.md
protocols/rules/conceptual-translation-glossary.md
protocols/rules/human-technical-style.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
protocols/rules/fragment-defect-analysis-and-repair.md
protocols/rules/visual-assets-and-figures.md
```

Словарь смыслового перевода используется как справочник при выборе русских слов. План не дублирует словарь и не создаёт локальный список спорных терминов.

## 5. Содержательное направление

Сквозной пример должен естественно провести агента через разные границы действия. Например, агент чинит ошибку в billing/UI. Сначала он читает код и тесты. Потом меняет локальный `worktree`. Затем запускает проверки. Потом открывает браузер или devtools и видит, что интерфейс всё ещё показывает старое состояние. Для диагностики ему хочется вызвать внешний API или MCP-инструмент. Но часть данных похожа на production-среду, часть команд может изменить внешнее состояние, а секреты не должны попасть в логи. Среда должна различать, что можно читать без подтверждения, что допустимо только локально, что требует approval, что должно быть недоступно и что обязано оставить след.

Через главу нужно провести простую шкалу: чтение, локальная правка, запуск локальных команд, браузерная проверка, вызов внешнего сервиса, работа около secrets или production-like boundary, изменение состояния внешней системы. Это не список ради списка. Каждый следующий тип действия увеличивает возможные последствия и требует другой среды, другого подтверждения, другого лога и иногда другого человека.

Ключевое различение: `permission`, `approval`, `sandbox` и `authority` — не одно и то же. Permission описывает, что среда технически позволяет. Approval — что человек или политика подтвердили конкретное действие или класс действий. Sandbox ограничивает радиус последствий. Authority отвечает за право признать результат допустимым для проекта. IX раскрывает первые три и доводит читателя до границы с authority, не забирая главу XII.

Sandbox нужно объяснять трезво. Он снижает риск последствий, но не делает действие правильным. Агент может в sandbox исправить не ту проблему, подогнать тест, неверно понять браузерный сигнал или создать убедительный, но неверный результат. Поэтому sandbox — это не гарантия качества, а ограничение среды, в которой агент пробует и оставляет след.

В конце глава должна связать среду исполнения с соседями. Из VIII приходит вопрос: какой способ работы выбран. IX спрашивает: в какой среде и с каким радиусом действия этот способ допустим. К XI уходит вопрос о проверочном материале: среда оставляет след, но достаточность проверки определяется отдельно. К XII уходит вопрос о принятии: разрешённое действие ещё не означает, что проект принял результат.

## 6. Как вести работу над главой

Начать нужно с фрагментов A6 и C4, статей Атласа по GSD, BMAD, PWG и Gas Town, досье и историй Arvid Kahl, HumanLayer, Mike McQuaid, Armin Ronacher, Stripe Minions и Shopify Roast. При чтении нужно собирать не “инструменты вообще”, а фактуру о средах исполнения: рабочие деревья, devbox, containers, permissions, approvals, browser/devtools, hooks, MCP, network, secrets, production boundary, logs и trace.

Внешний поиск должен быть активным. Нужны официальные и текущие источники по LangGraph, Temporal, DBOS, Restate, HumanLayer, Sandvault/worktrees, Codex/Claude/Kiro permissions и hooks, MCP, browser/devtools и devbox/runtime. Но current-practice pass должен собирать не обзор продуктов, а повторяющиеся границы действия: что агент может читать, где он пишет, где запускает команды, где обращается к внешнему миру, где требуется подтверждение и что остаётся в журнале.

Перед черновиком нужно собрать порядок главы вокруг среды действия. Сначала показать, почему выбранный способ работы сам по себе ничего не делает без среды. Потом провести сквозной пример через разные уровни действия. Затем развести permission, approval, sandbox и authority. После этого раскрыть worktree/container/devbox, browser/devtools, MCP/tool calls, durable execution и след исполнения как разные ответы на разные части проблемы.

Первый черновик не должен идти в ритме документации “Codex умеет X, Claude умеет Y, Kiro умеет Z”. Инструменты нужно группировать по функции: где ограничивается файловая система, где появляется подтверждение, где browser даёт наблюдение, где MCP открывает внешний канал, где durable workflow переживает сбой. Главный вопрос: что агент может затронуть и какой след оставляет.

После черновика провести активный добор без потолка объёма. Если тонкими остались approvals, sandbox, worktree, container/devbox, browser/devtools, MCP/tool calls, durable execution, external services, secrets/production boundary или мосты к XI/XII, нужно заново открыть источники и добрать фактуру. Не останавливаться на привычной длине главы, если исходный материал требует большего.

Визуальный слой особенно важен для этой главы. Проверить схемы: уровни действия агента; граница среды исполнения; approval loop; agent session внутри sandbox/worktree/container; связь runtime trace с будущим evidence. Сильные кандидаты довести до локальных assets, если среда позволяет.

После каждого добора переписывать текст нормальным русским языком. Убирать тревожные или искусственные формулы, канцелярит и самокомментарии. Писать прямо: техническая возможность выполнить действие не равна разрешению, проверке и принятию результата; разные действия имеют разный радиус последствий.

## 7. Готовность

Глава готова, если она не выглядит обзором инструментов среды. После чтения должно быть ясно, что агентское действие имеет разные границы: чтение, запись, запуск команд, браузерная проверка, внешний вызов, секреты, production-like среда. Должно быть ясно, почему permission, approval, sandbox и authority нельзя смешивать, и почему след исполнения ещё не является достаточным доказательством или правом принять изменение.

Сопутствующие файлы должны фиксировать источники, визуальные решения, открытые вопросы и границы с XI/XII. Финальная проверка должна отдельно искать механическое перечисление возможностей инструментов, остатки английского клея, самокомментарии и искусственные рабочие ярлыки.
