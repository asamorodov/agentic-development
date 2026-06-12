# CORE_NODES_WRITING_PACKAGES_BUILD_TARGET_GROUP_PLAN

Статус: план целевой группы для сборки writing-пакетов по уже подготовленным планам целевых групп. Этот документ не является исполнительным пакетом. По нему затем собирается отдельный Python-gated package.

Принцип: это механическая сборочная задача. Не строить сложный реестр источников, не реконструировать смысл каждого writing-пакета заново и не превращать сборку в новый research-pass. Все источники, которые нужны будущим writing-пакетам, должны быть заранее сложены в self-contained source bundle внутри исполнительного сборочного пакета. Первый рабочий лист материализует этот bundle в файловую систему, следующие рабочие листы по одному собирают zip-пакеты из готовых target-group plans. При сборке пакетов нельзя переписывать или упрощать уже подготовленные правила фигур: asset-classification gate (`synthetic_figure`, `local_image_asset`, `external_real_image_candidate`, `editorial_visual_idea`) должен попасть в executor prompts. Сборщик не имеет права заменять реальную иллюстрацию текстовой схемой, удалять `<img>`/asset-reference или превращать внешний screenshot/source diagram в синтетическую figure без явного решения в исходном target-group plan; даже для авторских схем такое решение допустимо только после usefulness/nontriviality gate — при явной нетривиальной пользе, а не ради визуального заполнения.

## 1. Обрабатываемые файлы

Создать папку:

```text
work/theory-writing/packages/
```

Создать writing-пакеты:

```text
work/theory-writing/packages/00_SPINE_MAP.zip
work/theory-writing/packages/A2_SPECIFICATION_ADR_CONTRACT.zip
work/theory-writing/packages/A3_SPECIFICATION_METHODOLOGIES_SYNTHESIS.zip
work/theory-writing/packages/A4_PERSISTENT_WORK_GRAPH_BOUNDARY.zip
work/theory-writing/packages/A5_PROCESS_METHODOLOGIES_SYNTHESIS.zip
work/theory-writing/packages/A6_EXECUTION_ENVIRONMENT_DISTINCTIONS.zip
work/theory-writing/packages/A7_OBSERVATION_VS_EVIDENCE.zip
work/theory-writing/packages/A8_AUTHORITY_TO_ACT_VS_COMPLETE.zip
work/theory-writing/packages/A9_LIFECYCLE_REPAIR.zip
work/theory-writing/packages/B1_SPDD_CONTRIBUTION_AND_LIMITS.zip
work/theory-writing/packages/B2_PWG_CONTRIBUTION.zip
work/theory-writing/packages/B3_GAS_TOWN_BEYOND_PWG.zip
work/theory-writing/packages/C1_SPECIFICATION_TO_PWG.zip
work/theory-writing/packages/C2_PWG_TO_PROCESS_PROFILES.zip
work/theory-writing/packages/C3_PWG_TO_EVIDENCE.zip
work/theory-writing/packages/C4_EXECUTION_RUNTIME_TO_PWG.zip
work/theory-writing/packages/C5_THEORY_TO_TECHNICAL_ATLAS.zip
```

Создать служебный результат сборки:

```text
work/theory-writing/packages/PACKAGES_BUILD_MANIFEST.md
work/theory-writing/packages/PACKAGES_BUILD_VERIFY.md
work/theory-writing/packages/PACKAGES_BUILD_RESUME.md
```

Не создавать пакет для `A1_CHANGE_NOT_PROMPT`: он уже был собран отдельно.

Не создавать пакет для `A10_MODE_SELECTION_MAP`: он должен собираться позднее, когда будут написаны ключевые узлы.

### Правило анализа дефектов и repair-pass для этой целевой группы

Repair-pass начинается не с переписывания, а с короткой диагностики по `protocols/rules/fragment-defect-analysis-and-repair.md`. Перед правкой исполнитель должен проверить функцию фрагмента против этого target-group plan, скелетона и карты документов: какую работу фрагмент должен выполнять в общей теории и не выполняет ли он чужую работу.

В диагностике различай как минимум композиционные, фактологические, источниковые/provenance, структурные, визуальные, языковые/стилевые, мета- и интеграционные/regression-дефекты. Для каждого существенного дефекта укажи место, почему это проблема и действие. Исправляй минимально достаточно: не переписывай фрагмент целиком, если дефект локальный; сохраняй фактуру, ссылки, source-specific детали, корректные `<figure>` и уже удачные переходы.

Для figure-кандидатов это означает не автоматическую inline-вставку, а корректное asset-решение: оставить в companion-файле, вставить как разрешённый local asset, отложить до asset-pass, отклонить или в редком случае оформить как нетривиальную synthetic figure после usefulness/nontriviality gate.

В конце repair-pass сделай regression audit: не потерялись ли источники и детали, не появились ли внутренние ссылки вместо первоисточников, служебный мета-текст, деградация реальных изображений в текстовые схемы, сломанные `<figure>`/`img src`, лишние повторы или конфликт с соседними A/B/C-узлами. Заверши проход readiness status: `ready_for_next_fragment`, `ready_with_known_debts`, `blocked_by_source_gap`, `blocked_by_asset_pass` или `needs_human_review`, с коротким объяснением оставшихся долгов.

## 2. Файлы для чтения

Планы целевых групп, по которым собираются пакеты:

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
work/theory-writing/target-group-plans/B1_SPDD_CONTRIBUTION_AND_LIMITS_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/B2_PWG_CONTRIBUTION_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/B3_GAS_TOWN_BEYOND_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C1_SPECIFICATION_TO_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C3_PWG_TO_EVIDENCE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
```

Сборочные правила:

```text
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
protocols/rules/visual-assets-and-figures.md
```

Источник для самих writing-пакетов: self-contained source bundle, упакованный в payload исполнительного сборочного пакета рядом со скриптом. В него должны войти все внутренние материалы, которые перечислены в секции “Файлы для чтения” каждого target-group plan: скелетон, планы, карта документов, протоколы, досье, истории, story-dossiers, source maps, comparative reports, quality audits и нужные рабочие файлы. Сборщик не должен вести отдельный сложный реестр соответствия “источник → пакет”: каждый writing-пакет может получить общий read-only source bundle и использовать из него только то, что требует его собственный plan.

## 3. Очередь рабочих prompt-ов

### P01. Материализовать общий source bundle

Прочитай сначала:

```text
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
```

Материализуй общий read-only source bundle из payload в файловую систему сборочного запуска. Не анализируй источники заново и не делай source selection. Проверь, что все target-group plans из секции 2 доступны, что папка `work/theory-writing/packages/` создана, и что источник для будущих writing-пакетов лежит в одном понятном локальном месте.

Запиши короткий отчёт о материализации source bundle и переходи к следующему рабочему листу.

### P02. Собрать пакет 00_SPINE_MAP

Прочитай сначала:

```text
work/theory-writing/target-group-plans/00_SPINE_MAP_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери self-contained Python-gated writing-пакет по этому target-group plan. Используй общий source bundle, не создавай новый реестр источников и не меняй текст плана. Итоговый пакет должен называться:

```text
work/theory-writing/packages/00_SPINE_MAP.zip
```

Проведи smoke-test первого и второго перехода runner-а: рабочие листы должны получать разные непрозрачные имена, видимый Python не должен раскрывать структуру задания.

### P03. Собрать пакет A2_SPECIFICATION_ADR_CONTRACT

Прочитай сначала:

```text
work/theory-writing/target-group-plans/A2_SPECIFICATION_ADR_CONTRACT_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери self-contained Python-gated writing-пакет по этому target-group plan. Используй общий source bundle и не переписывай prompt-очередь. Итоговый пакет:

```text
work/theory-writing/packages/A2_SPECIFICATION_ADR_CONTRACT.zip
```

Проведи тот же smoke-test.

### P04. Собрать пакет A3_SPECIFICATION_METHODOLOGIES_SYNTHESIS

Прочитай сначала:

```text
work/theory-writing/target-group-plans/A3_SPECIFICATION_METHODOLOGIES_SYNTHESIS_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/A3_SPECIFICATION_METHODOLOGIES_SYNTHESIS.zip
```

Проведи smoke-test.

### P05. Собрать пакет A4_PERSISTENT_WORK_GRAPH_BOUNDARY

Прочитай сначала:

```text
work/theory-writing/target-group-plans/A4_PERSISTENT_WORK_GRAPH_BOUNDARY_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/A4_PERSISTENT_WORK_GRAPH_BOUNDARY.zip
```

Проведи smoke-test.

### P06. Собрать пакет A5_PROCESS_METHODOLOGIES_SYNTHESIS

Прочитай сначала:

```text
work/theory-writing/target-group-plans/A5_PROCESS_METHODOLOGIES_SYNTHESIS_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/A5_PROCESS_METHODOLOGIES_SYNTHESIS.zip
```

Проведи smoke-test.

### P07. Собрать пакет A6_EXECUTION_ENVIRONMENT_DISTINCTIONS

Прочитай сначала:

```text
work/theory-writing/target-group-plans/A6_EXECUTION_ENVIRONMENT_DISTINCTIONS_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/A6_EXECUTION_ENVIRONMENT_DISTINCTIONS.zip
```

Проведи smoke-test.

### P08. Собрать пакет A7_OBSERVATION_VS_EVIDENCE

Прочитай сначала:

```text
work/theory-writing/target-group-plans/A7_OBSERVATION_VS_EVIDENCE_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/A7_OBSERVATION_VS_EVIDENCE.zip
```

Проведи smoke-test.

### P09. Собрать пакет A8_AUTHORITY_TO_ACT_VS_COMPLETE

Прочитай сначала:

```text
work/theory-writing/target-group-plans/A8_AUTHORITY_TO_ACT_VS_COMPLETE_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/A8_AUTHORITY_TO_ACT_VS_COMPLETE.zip
```

Проведи smoke-test.

### P10. Собрать пакет A9_LIFECYCLE_REPAIR

Прочитай сначала:

```text
work/theory-writing/target-group-plans/A9_LIFECYCLE_REPAIR_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/A9_LIFECYCLE_REPAIR.zip
```

Проведи smoke-test.

### P11. Собрать пакет B1_SPDD_CONTRIBUTION_AND_LIMITS

Прочитай сначала:

```text
work/theory-writing/target-group-plans/B1_SPDD_CONTRIBUTION_AND_LIMITS_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/B1_SPDD_CONTRIBUTION_AND_LIMITS.zip
```

Проведи smoke-test.

### P12. Собрать пакет B2_PWG_CONTRIBUTION

Прочитай сначала:

```text
work/theory-writing/target-group-plans/B2_PWG_CONTRIBUTION_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/B2_PWG_CONTRIBUTION.zip
```

Проведи smoke-test.

### P13. Собрать пакет B3_GAS_TOWN_BEYOND_PWG

Прочитай сначала:

```text
work/theory-writing/target-group-plans/B3_GAS_TOWN_BEYOND_PWG_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/B3_GAS_TOWN_BEYOND_PWG.zip
```

Проведи smoke-test.

### P14. Собрать пакет C1_SPECIFICATION_TO_PWG

Прочитай сначала:

```text
work/theory-writing/target-group-plans/C1_SPECIFICATION_TO_PWG_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/C1_SPECIFICATION_TO_PWG.zip
```

Проведи smoke-test.

### P15. Собрать пакет C2_PWG_TO_PROCESS_PROFILES

Прочитай сначала:

```text
work/theory-writing/target-group-plans/C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/C2_PWG_TO_PROCESS_PROFILES.zip
```

Проведи smoke-test.

### P16. Собрать пакет C3_PWG_TO_EVIDENCE

Прочитай сначала:

```text
work/theory-writing/target-group-plans/C3_PWG_TO_EVIDENCE_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/C3_PWG_TO_EVIDENCE.zip
```

Проведи smoke-test.

### P17. Собрать пакет C4_EXECUTION_RUNTIME_TO_PWG

Прочитай сначала:

```text
work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/C4_EXECUTION_RUNTIME_TO_PWG.zip
```

Проведи smoke-test.

### P18. Собрать пакет C5_THEORY_TO_TECHNICAL_ATLAS

Прочитай сначала:

```text
work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Собери пакет:

```text
work/theory-writing/packages/C5_THEORY_TO_TECHNICAL_ATLAS.zip
```

Проведи smoke-test.

### P19. Проверить собранные пакеты и записать manifest

Прочитай сначала:

```text
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Проверь, что все 17 zip-пакетов из секции 1 существуют, проходят `unzip -t`, содержат `START.md`, generic Python-runner и payload, а видимый Python не раскрывает предметную структуру пакета.

Запиши:

```text
work/theory-writing/packages/PACKAGES_BUILD_MANIFEST.md
work/theory-writing/packages/PACKAGES_BUILD_VERIFY.md
work/theory-writing/packages/PACKAGES_BUILD_RESUME.md
```

`PACKAGES_BUILD_VERIFY.md` должен явно перечислить каждый zip и результат проверки. Если какой-то пакет не собран или smoke-test не прошёл, не скрывай это; пометь пакет как failed и укажи, что нужно пересобрать.
```


Правило для будущих writing-пакетов: repair-планы должны включать диагностику дефектов перед правкой, проверку функции фрагмента, минимальную достаточную правку, regression audit и readiness status по `protocols/rules/fragment-defect-analysis-and-repair.md`.
