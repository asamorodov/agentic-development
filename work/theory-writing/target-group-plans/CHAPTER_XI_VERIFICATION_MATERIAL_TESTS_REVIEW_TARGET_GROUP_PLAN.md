# Рабочий план главы XI — проверочный материал, тесты и ревью

Это план для пакета, который должен написать главу XI. Он задаёт направление работы, входные материалы и критерии готовности, но не даёт готовые абзацы для переноса в главу.

В этой главе особенно важен внешний добор (`D3`). Нужны не только внутренние различения из корпуса, но и реальные практики проверки: контрактное тестирование, архитектурные проверки, ревью, staged rollout, наблюдаемость, SLO, безопасность и проверка поведения в рабочей среде.

## 1. Зачем нужна эта глава

К этому месту теория уже показала, как агентская работа получает рабочее состояние, как её продолжать после паузы, как ограничивать действия агента в среде исполнения и как координировать много параллельных задач. Но даже после этого остаётся отдельный вопрос: **чем подтверждён результат**.

Глава XI не должна быть главой “про тесты”. Её задача шире и точнее: показать, как связать обещание изменения с материалом, который это обещание действительно подтверждает. Изменение может обещать исправить локальное поведение, сохранить внешний контракт, не нарушить архитектурную границу, не раскрыть секреты, выдержать нагрузку, не испортить пользовательский путь или безопасно пройти выкатку. Для каждого такого обещания нужны свои основания.

Главная индивидуальность главы в том, что проверочный материал никогда не бывает универсальным. У любого материала есть область силы и граница применимости. Юнит-тест может хорошо подтверждать локальное поведение, но ничего не говорить о внешнем API. Contract test может защищать совместимость интерфейса, но не доказывать удобство пользовательского пути. Ревью может увидеть архитектурный риск, но само по себе не заменяет проверки поведения в рабочей среде. Staging может поймать часть интеграционных проблем, но не даёт полной картины production-нагрузки. Наблюдаемость после выката показывает реальное поведение, но появляется уже после того, как изменение попало к пользователям.

Поэтому внутренний ход главы такой: **что изменение обещает; какой риск стоит за этим обещанием; какой материал может это подтвердить; где граница этого материала; что остаётся непроверенным и должно быть явно передано дальше**.

## 2. Границы главы

Не писать каталог тестов. Тесты, ревью, линтеры, CI, staging, наблюдаемость и ручная проверка нужны только как материалы, которые что-то подтверждают или, наоборот, оставляют часть вопроса открытой.

Не смешивать проверку с принятием результата. Глава XI собирает и оценивает основания: что проверено, чем проверено, насколько это относится к обещанию изменения и что осталось непокрытым. Глава XII начинается там, где на основе этих оснований кто-то должен принять решение и взять ответственность.

Не повторять главу IX. Среда исполнения оставляет следы: команды, логи, browser/devtools, tool calls, approvals. Но сам след работы ещё не говорит, что именно было проверено. В главе XI нужно интерпретировать этот след: к какому обещанию он относится, чего не покрывает и почему его можно или нельзя считать достаточным.

Не повторять главу X. Gas Town и Beads помогают организовать много параллельных работ и вернуть результаты в общую картину проекта. Но хорошо организованная работа ещё не означает, что результат достаточно подтверждён.

## 3. Куда записывать результат

Основной выход:

```text
work/theory-writing/chapters/XI_verification_material_tests_review.md
```

Сопутствующие файлы:

```text
work/theory-writing/chapters/XI_verification_material_tests_review_source_register.md
work/theory-writing/chapters/XI_verification_material_tests_review_fragment_usage.md
work/theory-writing/chapters/XI_verification_material_tests_review_atlas_usage.md
work/theory-writing/chapters/XI_verification_material_tests_review_dossier_gap_notes.md
work/theory-writing/chapters/XI_verification_material_tests_review_external_discovery_log.md
work/theory-writing/chapters/XI_verification_material_tests_review_story_anchors.md
work/theory-writing/chapters/XI_verification_material_tests_review_figure_candidates.md
work/theory-writing/chapters/XI_verification_material_tests_review_open_questions.md
work/theory-writing/chapters/XI_verification_material_tests_review_degradation_and_duplication_audit.md
work/theory-writing/chapters/XI_verification_material_tests_review_readiness_report.md
```

Проходы пакета пишутся в:

```text
work/theory-writing/chapters/XI_verification_material_tests_review_passes/
```

Пиши создаваемый текст естественным русским языком. Это относится к главе, рабочим заметкам, журналам поиска, реестрам, отчётам, сопутствующим файлам и записям в проходах.

Формулировки этого плана не являются текстом главы. План задаёт работу и критерии, но не даёт готовые фразы для переноса в основной текст.

## 4. Что читать перед работой

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
work/theory-writing/fragments/A7_observation_vs_evidence.md
work/theory-writing/fragments/A7_source_usage.md
work/theory-writing/fragments/A7_story_anchor_map.md
work/theory-writing/fragments/A7_figure_candidates.md
work/theory-writing/fragments/A7_open_questions.md
work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
work/theory-writing/fragments/C3_source_usage.md
work/theory-writing/fragments/C3_story_anchor_map.md
work/theory-writing/fragments/C3_figure_candidates.md
work/theory-writing/fragments/C3_open_questions.md
work/theory-writing/fragments/C3_degradation_and_duplication_audit.md
work/theory-writing/fragments/A2_specification_adr_contract.md
work/theory-writing/fragments/A2_source_usage.md
work/theory-writing/fragments/A2_story_anchor_map.md
work/theory-writing/fragments/A2_figure_candidates.md
work/theory-writing/fragments/A2_open_questions.md
work/theory-writing/fragments/A2_degradation_and_duplication_audit.md
```

Статьи Атласа и связанные файлы:

```text
work/atlas/articles/spdd_method.md
work/atlas/articles/spdd_method_theory_links.md
work/atlas/articles/spdd_method_source_usage.md
work/atlas/articles/spdd_method_image_plan.md
work/atlas/articles/spdd_method_external_image_queue.md
work/atlas/articles/spdd_method_open_questions.md
work/atlas/articles/adr_method.md
work/atlas/articles/adr_method_theory_links.md
work/atlas/articles/adr_method_source_usage.md
work/atlas/articles/adr_method_image_plan.md
work/atlas/articles/adr_method_external_image_queue.md
work/atlas/articles/adr_method_open_questions.md
work/atlas/articles/tdad_comparative.md
work/atlas/articles/tdad_comparative_theory_links.md
work/atlas/articles/tdad_comparative_source_usage.md
work/atlas/articles/tdad_comparative_image_plan.md
work/atlas/articles/tdad_comparative_external_image_queue.md
work/atlas/articles/tdad_comparative_open_questions.md
work/atlas/articles/constitutional_sdd.md
work/atlas/articles/constitutional_sdd_theory_links.md
work/atlas/articles/constitutional_sdd_source_usage.md
work/atlas/articles/constitutional_sdd_image_plan.md
work/atlas/articles/constitutional_sdd_external_image_queue.md
work/atlas/articles/constitutional_sdd_open_questions.md
work/atlas/articles/kiro_specs.md
work/atlas/articles/kiro_specs_theory_links.md
work/atlas/articles/kiro_specs_source_usage.md
work/atlas/articles/kiro_specs_image_plan.md
work/atlas/articles/kiro_specs_external_image_queue.md
work/atlas/articles/kiro_specs_open_questions.md
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
```

Досье:

```text
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
```

Истории и досье историй:

```text
content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md
content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
```

Начальные темы внешнего поиска:

```text
contract testing
Pact can-i-deploy
architecture fitness functions
OpenAPI diff
SLO rollout error budget
software review evidence
AI code review studies
traceability in safety cases
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

## 5. Какой ход нужен тексту

Глава должна идти от обещания изменения к проверочному материалу и дальше к границам этого материала. Не начинать с вопроса “какие тесты бывают”. Начинать с вопроса: что именно изменение должно было обеспечить.

Сквозная сцена может продолжить billing/API или UI-задачу. Агент изменил код, тесты зелёные, ревью выглядит нормально. Но внутри этой одной задачи может быть несколько разных обещаний:

- API возвращает правильный billing status;
- внешний контракт не сломан для существующих клиентов;
- миграция данных не портит старые записи;
- права доступа не стали шире, чем нужно;
- UI показывает новый статус понятно и в правильных состояниях;
- интеграция с платёжным провайдером корректно обрабатывает ошибки;
- после выката есть метрики, по которым можно заметить деградацию.

Каждое обещание требует своего материала. Зелёные unit tests могут быть важны, но они не закрывают весь список. Contract tests помогают с совместимостью, но не говорят о UX. OpenAPI diff показывает изменение публичного интерфейса, но не доказывает, что бизнес-путь стал правильным. SLO и staged rollout помогают увидеть эксплуатационный риск, но не заменяют проверки до выката. Security review смотрит на права, секреты и опасные пути, но не отвечает за все поведенческие обещания. AI review может подсветить подозрительные места, но не должно выглядеть как самостоятельное основание для принятия результата.

В тексте важно постоянно задавать один и тот же инженерный вопрос: **что этот материал подтверждает, в каких границах и что он не подтверждает**. Именно это отличает проверочный материал от декоративного зелёного сигнала.

## 6. Как работать над главой

Сначала прочитать готовые главы IX и X. Они дают контекст исполнения и координации, но не решают вопрос подтверждения результата. После них нужно показать следующий слой: проект должен понять, какие обещания изменения действительно проверены.

Затем поднять внутренние фрагменты и Атлас: tests, review loops, CI, benchmarks, Showboat, Sandvault, HumanLayer, hooks, MCP, worktrees, browser/devtools и практики из историй. Не пересказывать эти материалы подряд. Каждую фактуру встраивать в ответ на конкретный вопрос: какое обещание она помогает проверить и где её границы.

После внутреннего чтения провести внешний добор. Он нужен не для общего списка современных практик, а для конкретных различений:

- Pact и `can-i-deploy` — совместимость контрактов;
- OpenAPI diff — изменения публичного API;
- architecture fitness functions — архитектурные инварианты;
- SLO, error budget, canary или staged rollout — эксплуатационный риск;
- security review — права, секреты и небезопасные пути;
- AI code review studies — возможности и ограничения автоматического ревью;
- safety-case traceability — связь между утверждениями о системе и материалом, который их поддерживает.

Первый черновик строить вокруг цепочки “обещание → риск → проверочный материал → граница проверки → что остаётся неизвестным”. Если текст превращается в список видов тестов, его нужно переписать.

После первого черновика найти слабые места: где проверка названа, но не объяснено, что именно она подтверждает; где не показано, что остаётся непроверенным; где внешний источник упомянут как отдельная тема, а не встроен в ход главы; где CI или ревью звучат как магическая гарантия; где глава начинает решать будущий вопрос принятия результата.

## 7. Когда глава готова

Глава готова, если читатель после неё умеет отличать “какая-то проверка была” от “это действительно подтверждает нужное обещание”. Она должна показать, почему один и тот же набор зелёных индикаторов может быть достаточным для простой правки и слабым для изменения контракта, данных, безопасности или выкатки.

Сопутствующие файлы должны честно показывать, какие фрагменты, статьи Атласа, досье, истории и внешние источники использованы. В readiness report отдельно объяснить, почему объём главы задан материалом, а не привычной длиной.

## 8. Общие правила для всех проходов

Работа пишется по-русски. Английским остаются только имена инструментов, моделей, проектов, команд, файлов, полей конфигурации, исходные метки источников и короткие фрагменты, где важна точная форма. Нельзя переносить английский связочный язык в русскую прозу.

Формулировки этого плана не являются заготовками для текста. Исполнитель может брать отсюда направление, границы, источники и критерии, но каждую мысль в главе нужно заново написать нормальным русским языком.

У текста нет целевой длины и скрытого потолка. Не нужно стремиться к привычному размеру главы. Если после первого черновика остаются важные источники, недоразобранные различения, слабые переходы или неперенесённая фактура, нужно снова открыть материалы и переписать нужные места.

После первого полного черновика нужен активный добор материала. Это не косметическая правка: нужно проверить, какие фрагменты, статьи Атласа, досье, истории и внешние источники ещё не работают в тексте так, как должны. Новую фактуру нужно встраивать в уже существующие разделы, а не добавлять отдельным блоком сверху.

Visual layer решается после того, как понятен ход текста. Изображение нужно вставлять только тогда, когда оно помогает увидеть различение, порядок действий, границу ответственности, проверочный материал или переход между слоями. Источники изображений и локальные перерисовки фиксируются в `figure_candidates` и связанных заметках.

В конце обязательно проверить естественность языка. Особое внимание — спорным рабочим ярлыкам из словаря смыслового перевода, англоязычным связкам и искусственным формулам, где русские слова соединены не по-русски.
