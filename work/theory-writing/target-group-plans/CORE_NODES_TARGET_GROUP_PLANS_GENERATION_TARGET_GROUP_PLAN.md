# Target group plan: CORE_NODES_TARGET_GROUP_PLANS_GENERATION

Статус: build-time план целевой группы.  
Назначение: создать планы целевых групп для оставшихся узловых фрагментов теоретического раздела. A1 уже имеет отдельный план и используется только как образец формы.

## 1. Обрабатываемые файлы

Пакет должен создать или обновить следующие планы целевых групп:

```text
work/theory-writing/target-group-plans/00_SPINE_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A2_SPECIFICATION_ADR_CONTRACT_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A3_SPECIFICATION_METHODOLOGIES_SYNTHESIS_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A4_PERSISTENT_WORK_GRAPH_BOUNDARY_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A5_PROCESS_METHODOLOGIES_SYNTHESIS_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A6_EXECUTION_ENVIRONMENT_DISTINCTIONS_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A7_OBSERVATION_VS_EVIDENCE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A8_AUTHORITY_TO_ACT_VS_COMPLETE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A9_LIFECYCLE_REPAIR_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/B1_SPDD_CONTRIBUTION_AND_LIMITS_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/B2_PWG_CONTRIBUTION_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/B3_GAS_TOWN_BEYOND_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C1_SPECIFICATION_TO_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C3_PWG_TO_EVIDENCE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
```

Все перечисленные файлы имеют статус `future` или `existing` в зависимости от текущего состояния репозитория. Роль каждого файла — `primary target`: это собственно планы, которые затем будут использоваться для сборки writing-пакетов.

Служебные результаты исполнительного пакета:

```text
aa_source_matrix.md
aa_source_matrix_report.txt
target_group_plans_consistency_audit.md
target_group_plans_source_coverage_matrix.md
core_nodes_target_group_plans_result.zip
result/COMPLETE.txt
MANIFEST.md
VERIFY.md
RESUME.md
```

Эти служебные файлы не являются частью канонического каталога `target-group-plans/`, но должны попасть в result archive исполнителя.

### Правило анализа дефектов и repair-pass для этой целевой группы

Repair-pass начинается не с переписывания, а с короткой диагностики по `protocols/rules/fragment-defect-analysis-and-repair.md`. Перед правкой исполнитель должен проверить функцию фрагмента против этого target-group plan, скелетона и карты документов: какую работу фрагмент должен выполнять в общей теории и не выполняет ли он чужую работу.

В диагностике различай как минимум композиционные, фактологические, источниковые/provenance, структурные, визуальные, языковые/стилевые, мета- и интеграционные/regression-дефекты. Для каждого существенного дефекта укажи место, почему это проблема и действие. Исправляй минимально достаточно: не переписывай фрагмент целиком, если дефект локальный; сохраняй фактуру, ссылки, source-specific детали, корректные `<figure>` и уже удачные переходы.

Для figure-кандидатов это означает не автоматическую inline-вставку, а корректное asset-решение: оставить в companion-файле, вставить как разрешённый local asset, отложить до asset-pass, отклонить или в редком случае оформить как нетривиальную synthetic figure после usefulness/nontriviality gate.

В конце repair-pass сделай regression audit: не потерялись ли источники и детали, не появились ли внутренние ссылки вместо первоисточников, служебный мета-текст, деградация реальных изображений в текстовые схемы, сломанные `<figure>`/`img src`, лишние повторы или конфликт с соседними A/B/C-узлами. Заверши проход readiness status: `ready_for_next_fragment`, `ready_with_known_debts`, `blocked_by_source_gap`, `blocked_by_asset_pass` или `needs_human_review`, с коротким объяснением оставшихся долгов.

## 2. Файлы для чтения

Пакет self-contained: все перечисленные ниже источники должны быть упакованы внутрь payload. Repo snapshot при запуске не требуется.

Управляющие документы и планы:

```text
work/discourse.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
work/approved-ai-sdlc-plan.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
work/theory-writing/target-group-plans/A1_CHANGE_NOT_PROMPT_TARGET_GROUP_PLAN.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Обязательные протоколы:

```text
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
protocols/rules/fragment-defect-analysis-and-repair.md
protocols/rules/visual-assets-and-figures.md
protocols/rules/english-source-handling.md
```

Активные методологические досье:

```text
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
```

Опубликованные истории:

```text
content/Orientation.md
content/Story_introduction.md
content/Cross_story_synthesis.md
content/stories/01_boris_tane_research_plan_implement_reconstruction_connected.md
content/stories/02_peter_steinberger_maximum_deep_dive_reconstruction_connected.md
content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md
content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md
content/stories/06_jesse_vincent_agentic_workflow_reconstruction_connected.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
content/stories/09_calvin_french_owen_maximum_deep_reconstruction_connected.md
content/stories/10_mark_erikson_maximum_deep_reconstruction_connected.md
content/stories/11_mae_capozzi_maximum_deep_reconstruction_connected.md
content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

Story-dossiers:

```text
work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md
work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
work/story_dossiers/QUIX_KLAUS_KODE_STORY_DOSSIER.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
work/story_dossiers/ZIG_NO_AI_POLICY_STORY_DOSSIER.md
```

Сравнительные отчёты, карты и quality audits:

```text
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/METHODOLOGY_DOSSIERS_QUALITY_AUDIT.md
work/reports/SELECTED_DOSSIERS_QUALITY_AUDIT.md
work/reports/BMAD_METHOD_DOSSIER_QUALITY_AUDIT.md
work/reports/CONSTITUTIONAL_SDD_DOSSIER_QUALITY_AUDIT.md
work/reports/GSD_OPEN_GSD_DOSSIER_QUALITY_AUDIT.md
work/reports/KIRO_SPECS_DOSSIER_QUALITY_AUDIT.md
work/reports/PERSISTENT_WORK_GRAPH_DOSSIER_EXPANSION_REPORT.md
work/reports/PERSISTENT_WORK_GRAPH_CYCLE_05_ROLLBACK_NOTICE.md
work/theory-source-map-ai-driven-sdlc.md
work/old-site-theoretical-synthesis-baseline.md
work/expanded-quarry-theoretical-synthesis.md
```

Внешние источники не задаются исчерпывающим списком. Исполнитель обязан учитывать источники, уже присутствующие во внутренних материалах: inline-ссылки, source registers, названия авторов, инструментов, статей, репозиториев, методологий и figure-кандидатов. Главная задача пакета — не открыть новые источники для широты, а корректно выбрать и распределить уже накопленную источниковую базу по планам целевых групп.

## 3. Очередь рабочих prompt-ов

### P01. Матрица выбора источников

```text
Прочитай сначала:
- common planning sources
- methodology dossier sources
- published story sources
- story dossier sources
- comparative reports and quality audits

Создай рабочую матрицу выбора источников для всех оставшихся узловых фрагментов: 00 spine-map, A2–A10, B1–B3, C1–C5. A1 уже имеет отдельный план; используй его только как образец формы, не переписывай и не генерируй заново.

Для каждого узла сопоставь задачу с текущим скелетоном, планом несущих узлов, картой документов, досье, историями, story-dossiers, сравнительными отчётами и quality audits. Не копируй список источников из соседнего узла. Источники выбирай по роли в будущем тексте.

Запиши:
- aa_source_matrix.md
- aa_source_matrix_report.txt
```

### P02. Планы 00, A2, A3

```text
Прочитай сначала:
- common planning sources
- methodology dossier sources
- published story sources
- story dossier sources
- comparative reports and quality audits
- aa_source_matrix.md

Создай планы целевых групп для 00 spine-map, A2 specification / ADR / contract и A3 specification methodologies synthesis.

Каждый план должен иметь ровно три секции: обрабатываемые файлы, файлы для чтения, очередь рабочих prompt-ов. В очереди должны быть готовые тексты prompt-ов, не пересказ. Каждый prompt начинается с блока «Прочитай сначала:». Каждый генерируемый fragment plan должен иметь явный asset-classification gate для визуального материала: `synthetic_figure`, `local_image_asset`, `external_real_image_candidate`, `editorial_visual_idea`. Планы не должны заставлять превращать готовые иллюстрации, screenshots, source diagrams или локальные assets в текстовые схемы. Для локальных assets нужен asset-reference/`<img>` с проверенным путём; для внешних реальных изображений без asset-pass — статус `asset-pass-required`/`rights-check` в `*_figure_candidates.md` и asset catalog; для синтетических схем — inline `<figure>` по месту применения только после usefulness/nontriviality gate, то есть проверки явной пользы и нетривиальности. Нельзя использовать формулировку «figure-кандидат поддерживает аргумент — вставь inline» без предварительной классификации.

Для A2 особенно внимательно включи ADR-досье, Nygard/MADR/Fowler-линию и материалы про operational projection. Для A3 тщательно разведи SPDD, Spec Kit, Kiro, TDAD и Constitutional SDD; не делай общий обзор методологий.

Запиши:
- work/theory-writing/target-group-plans/00_SPINE_MAP_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/A2_SPECIFICATION_ADR_CONTRACT_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/A3_SPECIFICATION_METHODOLOGIES_SYNTHESIS_TARGET_GROUP_PLAN.md
- 00_SPINE_MAP_TARGET_GROUP_PLAN_batch_report.txt
```

### P03. Планы A4, B2, C1

```text
Прочитай сначала:
- common planning sources
- methodology dossier sources
- published story sources
- story dossier sources
- comparative reports and quality audits
- aa_source_matrix.md

Создай планы целевых групп для A4 Persistent Work Graph boundary, B2 PWG contribution и C1 specification → PWG.

Эти планы должны максимально аккуратно опираться на PWG-досье, PWG expansion report, Gas Town, GSD/BMAD и rollback notice по отклонённому cycle 05. Не используй отклонённый implementation-sketch как теоретическое основание.

Запиши:
- work/theory-writing/target-group-plans/A4_PERSISTENT_WORK_GRAPH_BOUNDARY_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/B2_PWG_CONTRIBUTION_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/C1_SPECIFICATION_TO_PWG_TARGET_GROUP_PLAN.md
- A4_PERSISTENT_WORK_GRAPH_BOUNDARY_TARGET_GROUP_PLAN_batch_report.txt
```

### P04. Планы C2, C3, C4

```text
Прочитай сначала:
- common planning sources
- methodology dossier sources
- published story sources
- story dossier sources
- comparative reports and quality audits
- aa_source_matrix.md

Создай планы целевых групп для C2 PWG → process profiles, C3 PWG → evidence и C4 execution runtime → PWG.

Главная задача — построить мосты между уже сильными узлами. Не превращай эти планы в сокращённые версии больших глав. У каждого моста должны быть свои источники, свои story anchors и своя очередь prompt-ов.

Запиши:
- work/theory-writing/target-group-plans/C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/C3_PWG_TO_EVIDENCE_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
- C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN_batch_report.txt
```

### P05. Планы A5, B3, C5

```text
Прочитай сначала:
- common planning sources
- methodology dossier sources
- published story sources
- story dossier sources
- comparative reports and quality audits
- aa_source_matrix.md

Создай планы целевых групп для A5 process methodologies synthesis, B3 Gas Town beyond PWG и C5 theory → technical atlas.

A5 должен связывать GSD, BMAD, Reversa / OpenSpec / AgentSPEX, PWG и Gas Town. B3 должен защитить Gas Town от сведения к PWG. C5 должен зафиксировать новую границу: теория остаётся поперечным SDLC-синтезом, а технический атлас становится концептуально-техническим слоем самостоятельных статей по конкретным концепциям, не сводясь к складу технических деталей и не копируя теорию механически.

Запиши:
- work/theory-writing/target-group-plans/A5_PROCESS_METHODOLOGIES_SYNTHESIS_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/B3_GAS_TOWN_BEYOND_PWG_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
- A5_PROCESS_METHODOLOGIES_SYNTHESIS_TARGET_GROUP_PLAN_batch_report.txt
```

### P06. Планы A6, A7

```text
Прочитай сначала:
- common planning sources
- methodology dossier sources
- published story sources
- story dossier sources
- comparative reports and quality audits
- aa_source_matrix.md

Создай планы целевых групп для A6 execution environment distinctions и A7 observation vs evidence.

A6 должен развести execution envelope, tool/sensor surface, workflow engine и platform agent. A7 должен развести наблюдение, свидетельство, проверку, replay, transcript, rollout evidence и owner review.

Запиши:
- work/theory-writing/target-group-plans/A6_EXECUTION_ENVIRONMENT_DISTINCTIONS_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/A7_OBSERVATION_VS_EVIDENCE_TARGET_GROUP_PLAN.md
- A6_EXECUTION_ENVIRONMENT_DISTINCTIONS_TARGET_GROUP_PLAN_batch_report.txt
```

### P07. Планы A8, A9, A10

```text
Прочитай сначала:
- common planning sources
- methodology dossier sources
- published story sources
- story dossier sources
- comparative reports and quality audits
- aa_source_matrix.md

Создай планы целевых групп для A8 authority to act vs complete, A9 lifecycle repair и A10 mode selection map.

A8 должен держать governance, human authority, CODEOWNERS, open-source policy, Zig policy и право завершения. A9 должен собрать repair tail: stale specification, stale ADR, stale operational projection, stale work graph, stale evidence gate. A10 должен дать карту выбора режима, не повторяя все предыдущие узлы.

Запиши:
- work/theory-writing/target-group-plans/A8_AUTHORITY_TO_ACT_VS_COMPLETE_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/A9_LIFECYCLE_REPAIR_TARGET_GROUP_PLAN.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- A8_AUTHORITY_TO_ACT_VS_COMPLETE_TARGET_GROUP_PLAN_batch_report.txt
```

### P08. План B1

```text
Прочитай сначала:
- common planning sources
- methodology dossier sources
- published story sources
- story dossier sources
- comparative reports and quality audits
- aa_source_matrix.md

Создай план целевой группы для B1 SPDD contribution and limits.

План должен показать вклад SPDD как deep case specification lifecycle и одновременно его границы: SPDD не решает durable work state, ownership, handoff и recovery. Обязательно опирайся на SPDD-досье, old-site seed, Spec Kit/Kiro/TDAD/Constitutional SDD и будущие мосты к PWG.

Запиши:
- work/theory-writing/target-group-plans/B1_SPDD_CONTRIBUTION_AND_LIMITS_TARGET_GROUP_PLAN.md
- B1_SPDD_CONTRIBUTION_AND_LIMITS_TARGET_GROUP_PLAN_batch_report.txt
```

### P09. Консолидационный аудит

```text
Прочитай сначала:
- все созданные target-group plans
- aa_source_matrix.md
- common planning sources
- comparative reports and quality audits

Проверь планы как набор: не дублируют ли они друг друга механически, все ли prompt-очереди содержат готовые тексты prompt-ов, каждый ли prompt начинается с «Прочитай сначала:», достаточно ли аккуратно подобраны источники, учтены ли досье, истории, story-dossiers, comparative reports и внешние источники, выводимые из материалов.

Исправь планы точечно, если видишь пропуски, слабые источниковые привязки или copy-paste между узлами.

Запиши:
- target_group_plans_consistency_audit.md
- target_group_plans_source_coverage_matrix.md
```

### P10. Финальная проверка и упаковка

```text
Прочитай сначала:
- все созданные target-group plans
- target_group_plans_consistency_audit.md
- target_group_plans_source_coverage_matrix.md

Проверь, что все ожидаемые планы существуют, имеют ровно три секции, содержат точные списки файлов, готовые тексты prompt-ов и блоки «Прочитай сначала:». Проверь, что source coverage не выглядит механически скопированным между узлами.

Собери итоговый архив:
- core_nodes_target_group_plans_result.zip

В архив включи все target-group plans, source matrix, consistency audit, source coverage matrix, MANIFEST.md, VERIFY.md, RESUME.md и marker result/COMPLETE.txt.
```


Правило для будущих writing-пакетов: repair-планы должны включать диагностику дефектов перед правкой, проверку функции фрагмента, минимальную достаточную правку, regression audit и readiness status по `protocols/rules/fragment-defect-analysis-and-repair.md`.
