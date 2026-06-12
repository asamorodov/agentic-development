# Target group plan: A10 — mode selection map

Статус: рабочий план целевой группы. По этому документу можно будет собрать исполнительный пакет для несущего фрагмента A10 **только после появления и первичного ремонта C1–C4**. План не является опубликованным текстом теории.

## 0. Dependency gate

`A10_mode_selection_map.md` — поздний синтетический узел. Его нельзя писать и пакетировать до готовности `C1_specification_to_pwg.md`, `C2_pwg_to_process_profiles.md`, `C3_pwg_to_evidence.md` и `C4_execution_runtime_to_pwg.md`, потому что финальная карта выбора режима должна учитывать не только A1–A9 and B1–B3, но и переходные мосты между specification, PWG, process, evidence and execution runtime.

Если при сборке или запуске пакета отсутствует хотя бы один из C1–C4, исполнитель должен остановиться, записать blocker в `A10_open_questions.md` и не создавать преждевременный A10-фрагмент. Ранее собранный `A10_MODE_SELECTION_MAP.zip` считать `premature/superseded`; новый пакет A10 можно собирать только после результатов C1–C4. Финальная проверка A10 не может заменить фактическое чтение upstream-файлов ссылкой на план их функций: если A1–A9, B1–B3 или C1–C4 должны быть входом, они должны быть реально открыты и отражены в source/open/audit files.

Главная функция A10: это не итоговое резюме теории и не maturity model. Это карта выбора минимально достаточного режима работы с агентом: когда добавить внешний артефакт, когда добавить продолжимое состояние работы, когда добавить процессный профиль, когда требовать свидетельства, когда ограничить действие агента или человека, когда чинить последствия изменения после merge, и когда всего этого не делать.

## 1. Обрабатываемые файлы

```yaml
- path: work/theory-writing/fragments/A10_mode_selection_map.md
  status: future
  role: primary
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Основной фрагмент: карта выбора минимально достаточного режима работы с агентом, не пересказ A1–A9 и не maturity model."

- path: work/theory-writing/fragments/A10_mode_selection_matrix.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Рабочая матрица признаков выбора: риск, обратимость, длительность, неопределённость, участники/агенты, фиксация намерения, ADR, PWG, process, runtime, evidence, authority boundary, repair. Не обязана целиком становиться публичной таблицей."

- path: work/theory-writing/fragments/A10_decision_stress_tests.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Сценарная проверка карты: 6-8 реальных задач, выбранный режим/комбинация режимов, что лишнее, что недостаточно и почему."

- path: work/theory-writing/fragments/A10_source_usage.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Which upstream fragments, reports and story anchors were used for each mode-selection branch."

- path: work/theory-writing/fragments/A10_story_anchor_map.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Story anchors for each selection branch; all stories as check corpus, only minimal anchors in prose."

- path: work/theory-writing/fragments/A10_figure_candidates.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Кандидаты на иллюстрации для карты выбора режима, branching axes, escalation/de-escalation, combinations and decision-map form."

- path: work/theory-writing/fragments/A10_open_questions.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Missing upstream fragments, unresolved selection criteria and mode-combination ambiguities."

- path: work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Audit that A10 is a practical mode-selection map, not a repeated table of contents, not a maturity ladder and not a generic classification."
```

Целевая группа не является `linked-target-edit`: A10 is dependent final synthesis. Если A/B/C upstream fragments are missing, do not invent their content and do not write A10 prematurely.

### Правило фигур и визуальных ассетов для этой целевой группы

Любое действие с визуальным материалом начинается не с inline-вставки, а с классификации. `*_figure_candidates.md` — это реестр возможностей и решений, а не автоматическая инструкция «вставить всё в основной текст».

Для каждого кандидата, упоминания картинки, screenshot, диаграммы, графика или уже существующего `<figure>` сначала зафиксируй один из статусов:

1. **`synthetic_figure`** — схема, таблица или диаграмма, которую мы действительно создаём сами для объяснения собственного аргумента. Этот статус допустим только если схема проходит usefulness/nontriviality gate: она проясняет нетривиальную связь, процесс, границу, lifecycle-переход или сравнение, которые плохо удерживаются прозой; добавляет самостоятельную объяснительную ценность; не повторяет соседний абзац декоративной таблицей; и не подменяет готовый или ещё не локализованный image asset. Только после этого её можно вставлять в основной фрагмент через `<figure class="synthetic-figure" id="...">...</figure>` рядом с тем абзацем или сравнительным блоком, который она проясняет. Внутри не должно быть служебных заметок вроде `Тип`, `Идея`, `Статус`, `лучше поставить`, `asset-pass` или «кандидат поддерживает абзац»: только публичная подпись и сама схема/таблица.
2. **`local_image_asset`** — готовая локальная иллюстрация, screenshot, source diagram, график или другой image asset, который уже лежит в репозитории и может использоваться. Его нельзя пересказывать, перерисовывать или «нормализовать» в текстовую схему. Он вставляется по месту применения как `<figure class="image-asset" id="..."><img src="..." alt="..." /><figcaption>...</figcaption></figure>` с проверенным локальным путём, нормальной публичной подписью и без потери исходной визуальной формы.
3. **`external_real_image_candidate`** — реальная картинка из внешнего источника: screenshot интерфейса, диаграмма из статьи или документации, график, таблица-изображение, source figure, ещё не скачанная или не проверенная. Такой кандидат нельзя подменять текстовой схемой. Он остаётся в `*_figure_candidates.md` и, если каталог уже используется в этом workflow, в `work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md` со статусом `asset-pass-required`, `rights-check`, `download-needed`, `quality-check`, `deferred` или `rejected` и с точной причиной. В основной текст он попадает только после отдельного asset-pass как локальный image asset. Авторская синтетическая схема вместо него допустима лишь как отдельное редакторское решение после usefulness/nontriviality gate и не должна маскировать потерю или неподготовленность исходной иллюстрации.
4. **`editorial_visual_idea`** — редакторская идея будущей визуализации, которой ещё нет как готовой картинки и которая пока не сделана как синтетическая схема. Она остаётся в `*_figure_candidates.md` с назначением, источниковой опорой и следующим действием.

Правило inline-placement применяется только после этой классификации и usefulness/nontriviality gate для собственных схем. Немногие выбранные `synthetic_figure`, которые действительно добавляют объяснительную ценность, и уже готовые/разрешённые `local_image_asset` не должны жить только в companion-файле и не должны складываться в финальный служебный appendix вроде `Дополнительные встроенные figure-кандидаты`. Но это правило **не** требует вставлять каждый внешний image candidate в основной текст и **никогда** не разрешает превращать готовую иллюстрацию или source screenshot в текстовый суррогат ради закрытия пункта «вставить figure».

При любом изменении визуального слоя обнови соответствующий `*_figure_candidates.md`: статус, тип, решение, локальный путь или причина отсрочки. Если используется общий каталог ассетов, синхронизируй решение с `work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md`, `LOCAL_ASSET_INDEX.md` и `EXTERNAL_REAL_IMAGE_CANDIDATES.md`.

### Правило анализа дефектов и repair-pass для этой целевой группы

Repair-pass начинается не с переписывания, а с короткой диагностики по `protocols/rules/fragment-defect-analysis-and-repair.md`. Перед правкой исполнитель должен проверить функцию фрагмента против этого target-group plan, скелетона и карты документов: какую работу фрагмент должен выполнять в общей теории и не выполняет ли он чужую работу.

В диагностике различай как минимум композиционные, фактологические, источниковые/provenance, структурные, визуальные, языковые/стилевые, мета- и интеграционные/regression-дефекты. Для каждого существенного дефекта укажи место, почему это проблема и действие. Исправляй минимально достаточно: не переписывай фрагмент целиком, если дефект локальный; сохраняй фактуру, ссылки, source-specific детали, корректные `<figure>` и уже удачные переходы.

Для figure-кандидатов это означает не автоматическую inline-вставку, а корректное asset-решение: оставить в companion-файле, вставить как разрешённый local asset, отложить до asset-pass, отклонить или в редком случае оформить как нетривиальную synthetic figure после usefulness/nontriviality gate.

В конце repair-pass сделай regression audit: не потерялись ли источники и детали, не появились ли внутренние ссылки вместо первоисточников, служебный мета-текст, деградация реальных изображений в текстовые схемы, сломанные `<figure>`/`img src`, лишние повторы или конфликт с соседними A/B/C-узлами. Заверши проход readiness status: `ready_for_next_fragment`, `ready_with_known_debts`, `blocked_by_source_gap`, `blocked_by_asset_pass` или `needs_human_review`, с коротким объяснением оставшихся долгов.

Для ещё не построенного фрагмента этот repair-слой реализуется не одним поздним проходом после стиля, а 2–3 общими редакторскими проходами сразу после адресных усилений основной функции и до языковых/стилевых проходов. Каждый такой проход сохраняет общность: оценивает, насколько текст выполняет поставленную задачу, сначала формулирует проблемы, затем исправляет их; не получает заранее специальной повестки вроде visual/source/style.

## 2. Файлы для чтения

### Управляющие документы

```text
work/discourse.md
work/approved-ai-sdlc-plan.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
```

### Протоколы языка, стиля и источников

```text
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/human-technical-style.md
protocols/rules/english-source-handling.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
protocols/rules/fragment-defect-analysis-and-repair.md
protocols/rules/visual-assets-and-figures.md
protocols/rules/terminology-and-translation.md
```

### Mandatory upstream fragments

```text
work/theory-writing/fragments/A1_change_not_prompt.md
work/theory-writing/fragments/A2_specification_adr_contract.md
work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
work/theory-writing/fragments/A5_process_methodologies_synthesis.md
work/theory-writing/fragments/A6_execution_environment_distinctions.md
work/theory-writing/fragments/A7_observation_vs_evidence.md
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
work/theory-writing/fragments/A9_lifecycle_repair.md
work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
work/theory-writing/fragments/B2_pwg_contribution.md
work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
work/theory-writing/fragments/C1_specification_to_pwg.md
work/theory-writing/fragments/C2_pwg_to_process_profiles.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
```

### Mandatory upstream companion files

```text
work/theory-writing/fragments/B1_source_usage.md
work/theory-writing/fragments/B2_source_usage.md
work/theory-writing/fragments/B3_source_usage.md
work/theory-writing/fragments/C1_source_usage.md
work/theory-writing/fragments/C2_source_usage.md
work/theory-writing/fragments/C3_source_usage.md
work/theory-writing/fragments/C4_source_usage.md
work/theory-writing/fragments/C1_degradation_and_duplication_audit.md
work/theory-writing/fragments/C2_degradation_and_duplication_audit.md
work/theory-writing/fragments/C3_degradation_and_duplication_audit.md
work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

### Main synthesis and source controls

```text
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
work/approved-ai-sdlc-plan.md
content/Cross_story_synthesis.md
work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md
work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md
work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
work/theory-source-map-ai-driven-sdlc.md
content/Orientation.md
content/Story_introduction.md
```

### Проверочный корпус историй

```text
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

Primary-pass anchors should normally be limited to Boris, Simon, HumanLayer, Mike, Stripe and Roast unless a branch requires another story.

### Story-dossiers

```text
work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md
work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
work/story_dossiers/QUIX_KLAUS_KODE_STORY_DOSSIER.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
work/story_dossiers/ZIG_NO_AI_POLICY_STORY_DOSSIER.md
```

Story-dossiers нужны только для проверки ветвей. Не пересказывай их.

### Внешние источники

Открывать внешние источники нужно только под конкретные утверждения будущего текста; не проходить весь список ради широты.

Явно известные источники: normally none new for A10. Используй already revealed sources from A1–A9, B1–B3, C1–C4, comparative reports, dossiers, story-dossiers and source registers. Если an exact external support is missing for a branch, write the gap rather than doing a new broad source pass.

Выводимые источники: upstream `*_source_usage.md` files, inline links, source registers, figure candidates, story anchor maps, comparative-report source lists, dossier source notes and all source-map references from A1–A9, B1–B3, C1–C4, `SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md` and `theory-source-map-ai-driven-sdlc.md`.

## 3. Очередь рабочих prompt-ов

### P01 — первичный фрагмент

```text
Прочитай сначала:
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A2_specification_adr_contract.md
- work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
- work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
- work/theory-writing/fragments/A5_process_methodologies_synthesis.md
- work/theory-writing/fragments/A6_execution_environment_distinctions.md
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
- work/theory-writing/fragments/A9_lifecycle_repair.md
- work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
- work/theory-writing/fragments/B2_pwg_contribution.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
- work/theory-writing/fragments/C1_specification_to_pwg.md
- work/theory-writing/fragments/C2_pwg_to_process_profiles.md
- work/theory-writing/fragments/C3_pwg_to_evidence.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Перед написанием проверь dependency gate: C1–C4 должны существовать. Если хотя бы одного C-фрагмента нет, остановись, запиши blocker в `work/theory-writing/fragments/A10_open_questions.md` и не создавай преждевременный A10.

Создай первый черновик `work/theory-writing/fragments/A10_mode_selection_map.md`. Композиционная функция: карта выбора минимально достаточного режима работы с агентом, а не summary A1–A9 and not a maturity model. Текст должен дать признаки: когда достаточно разговора, когда нужен план, когда спецификация, когда ADR, когда PWG, когда process profile, когда execution/runtime discipline, когда нужны свидетельства, когда нужен authority boundary and когда нужна последующая поддержка артефактов после merge.

Не пиши обзор источников и не пересказывай истории. Строй аргумент как часть общей теории: один ход мысли, несколько точных фактических якорей, ссылки сразу в тексте. Подзаголовки добавляй только там, где они помогают удержать смену смыслового хода; не дроби текст декоративно.

Запиши также первые версии `A10_source_usage.md`, `A10_story_anchor_map.md`, `A10_figure_candidates.md`, `A10_open_questions.md` and `A10_degradation_and_duplication_audit.md`.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P02 — upstream synthesis from A/B/C and dependency validation

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A2_specification_adr_contract.md
- work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
- work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
- work/theory-writing/fragments/A5_process_methodologies_synthesis.md
- work/theory-writing/fragments/A6_execution_environment_distinctions.md
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
- work/theory-writing/fragments/A9_lifecycle_repair.md
- work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
- work/theory-writing/fragments/B2_pwg_contribution.md
- work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
- work/theory-writing/fragments/C1_specification_to_pwg.md
- work/theory-writing/fragments/C2_pwg_to_process_profiles.md
- work/theory-writing/fragments/C3_pwg_to_evidence.md
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md

Проверь, что A10 реально опирается на A/B/C-фрагменты, а не заново изобретает их. Для каждого крупного режима выбора зафиксируй в `A10_source_usage.md`, какие A/B/C узлы он использует и какую границу выбора берёт из C1–C4.

Особенно проверь, что C1–C4 не просто упомянуты: C1 должен влиять на границу specification→PWG; C2 — на границу PWG→process profile; C3 — на связку PWG→свидетельство; C4 — на runtime→PWG. Если какая-то C-связка отсутствует, добавь её в основной текст или запиши явный долг.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P03 — рабочая матрица выбора и минимально достаточная структура

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Построй `work/theory-writing/fragments/A10_mode_selection_matrix.md` как рабочую матрицу признаков выбора режима. Это не обязательно публичная таблица целиком; это опорный материал для A10.

Матрица должна различать как минимум: риск, обратимость, длительность, число участников/агентов, неопределённость, необходимость фиксации намерения, необходимость ADR, необходимость продолжимого состояния работы, необходимость process profile, необходимость контролируемой среды исполнения, необходимость свидетельств, authority boundary, необходимость последующей поддержки артефактов после merge.

После создания матрицы проверь основной A10: он должен использовать матрицу как источник критериев, но не превращаться в таблицу всех понятий. Главный принцип: хороший режим — не самый структурированный, а минимально достаточный для риска, неопределённости, обратимости, числа участников, длительности работы и требований к подтверждению результата.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P04 — edge cases from stories and source-depth pass

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md
- content/Cross_story_synthesis.md
- content/stories/01_boris_tane_research_plan_implement_reconstruction_connected.md
- content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
- content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
- content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md

Добери edge cases and source-depth only where they sharpen selection criteria. Минимально проверь: маленькая обратимая правка, неизвестная зона кода / исследование, изменение поведения продукта, архитектурное решение, миграция / массовое изменение, несколько агентов или сессий, внешний PR / policy-bound contribution, post-merge repair.

Открывай внешние источники только под конкретные утверждения. Если добавляешь новый внешний источник, занеси его в `A10_source_usage.md`. Не превращай A10 в каталог историй; story anchors нужны только как проверки ветвей выбора.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P05 — системное выравнивание

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md

Выравняй `work/theory-writing/fragments/A10_mode_selection_map.md` как поздний несущий фрагмент общей теории. Проверь, ведёт ли он один продолжающийся смысл, не спорит ли со скелетоном, не пересказывает ли истории, не стал ли он summary A1–A9, скрытой maturity ladder или красивой классификацией без решения.

Сохрани фактуру и ссылки. Убери повторы, слишком локальные рамки и места, где текст выглядит как список тем. Если часть материала лучше оформить как самостоятельный материал концептуально-технического атласа, отметь это в `A10_open_questions.md` или `A10_degradation_and_duplication_audit.md`, но не удаляй важную мысль без замены и не своди материал атласа к несвязному technical appendix.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P06 — адресное усиление: критерии выбора режима

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Проведи адресный проход по `A10_mode_selection_map.md`: усили критерии выбора режима. A10 не должен пересказывать A1–A9. Он должен дать признаки, по которым опытный разработчик понимает, когда достаточно разговора, когда нужен план, когда спецификация, когда ADR, когда PWG, когда process profile, когда execution/runtime discipline, когда нужны свидетельства, когда нужен authority boundary and когда нужна последующая поддержка артефактов после merge.

Это адресное усиление основной функции фрагмента. Не превращай его в общий редакторский проход и не закрывай им последующую общую редакторскую тройку.

Перед правкой коротко запиши в `A10_degradation_and_duplication_audit.md`, какой конкретный риск проверен и что изменено. Если существенной проблемы нет, не переписывай текст ради активности. При любых изменениях визуального слоя сначала применяй asset-classification gate.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P07 — адресное усиление: переходы, эскалация и деэскалация

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Проведи адресный проход по `A10_mode_selection_map.md`: проверь переходы между режимами. Недостаточно перечислить режимы; нужно показать условия перехода: что должно случиться, чтобы подняться на следующий слой структуры, и когда нужно не усложнять работу преждевременно.

Отдельно проверь деэскалацию: A10 должен показывать не только когда добавить структуру, но и когда снять лишний слой, когда остановиться на более лёгком режиме и когда не превращать полезный процесс в шум. Если карта подталкивает к тому, что более тяжёлый режим всегда лучше, исправь это.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P08 — адресное усиление: сочетания режимов и минимально достаточная структура

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Проведи адресный проход по `A10_mode_selection_map.md`: проверь, что карта показывает не только выбор одного режима, но и допустимые сочетания. В реальной работе часто нужна комбинация: разговор + локальная проверка; ADR + ограниченный implementation plan; PWG + свидетельства + последующая поддержка артефактов; policy boundary + evidence + human acceptance; PWG + runtime discipline + передача работы; process profile + PWG + evidence + authority boundary.

Проверь и обратное: A10 должен показывать лишние сочетания, которые создают шум. Если карта стала скрытой лестницей `conversation → plan → spec → PWG → process → platform`, перепиши её вокруг минимально достаточной структуры.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P09 — сценарный stress-test практической применимости

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Создай или обнови `work/theory-writing/fragments/A10_decision_stress_tests.md`. Проверь A10 на 6–8 коротких сценариях:

- маленькая обратимая правка;
- неизвестная зона кода / исследование;
- изменение поведения продукта;
- архитектурное решение;
- миграция / массовое изменение;
- несколько агентов или сессий;
- внешний PR / policy-bound contribution;
- post-merge repair, когда устарели правила, документы или проверки.

Для каждого сценария укажи: какой режим или комбинация режимов нужна; какой режим был бы лишним; какой режим был бы недостаточным; что именно в A10 помогает принять это решение. Затем поправь основной текст, если stress-test показывает, что карта красива, но не даёт решения.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P10 — общий редакторский проход 1: оценка выполнения задачи и repair

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Оцени текущий текст `A10_mode_selection_map.md` как готовящийся фрагмент теории: насколько хорошо он выполняет задачу, заданную этим target-group plan, скелетоном и картой документов? Сначала сформулируй проблемы, затем исправь их.

Сохрани общность прохода. Не назначай себе заранее специальную задачу вроде «починить визуальный слой», «починить источники» или «переписать стиль». Смотри на весь фрагмент целиком: его функцию, композицию, границы с соседними узлами, источниковую опору, структуру, публичный слой, фигуры, companion-файлы и оставшиеся долги. Используй карту дефектов из `fragment-defect-analysis-and-repair.md`, но не превращай её в механический чек-лист.

Перед правкой запиши короткую диагностику: рабочая ценность, публикационная готовность, readiness status, 3–7 главных проблем и что именно будет исправлено сейчас. После диагностики внеси минимально достаточную правку. После правки обнови companion-файлы, выполни regression audit и readiness status.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P11 — общий редакторский проход 2: повторная оценка после repair

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Заново оцени уже исправленный `A10_mode_selection_map.md`. Не считай первый общий редакторский проход достаточным и не повторяй его механически. Прочитай фрагмент как свежий редактор: насколько он теперь выполняет свою задачу в общей теории? Сначала сформулируй проблемы, затем исправь их.

Сохрани общность прохода. Не ищи только один заранее заданный тип ошибки. Проверь, какие дефекты стали видны после предыдущей правки: перекос функции, обзорность вместо теории, слабые переходы, лишние или недостающие подзаголовки, потеря фактуры, дублирование соседних фрагментов, неудачные figure-решения, служебный мета-текст, плохие формулы, неясные источники или устаревшие companion-записи.

Исправляй только реальные проблемы. Если текст уже выполняет задачу, не переписывай его ради активности: зафиксируй это в audit/open questions и сделай только точечные изменения. После правки обнови companion-файлы, выполни regression audit и запиши readiness status.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P12 — общий редакторский проход 3: контрольная оценка без специальной повестки

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Проведи третий общий редакторский проход по `A10_mode_selection_map.md`. Это не языковая и не стилевая полировка. Задача та же: оценить, насколько фрагмент выполняет поставленную задачу, сначала сформулировать оставшиеся проблемы, затем исправить их.

Сохрани проход общим. Не превращай его в отдельный visual-pass, source-pass, style-pass или atlas-pass. Проверь, не остались ли после двух предыдущих ремонтов более глубокие дефекты: фрагмент выглядит убедительно, но делает чужую работу; стал гладким, но потерял source-specific детали; сохранил лишний обзорный материал; оставил неочевидный конфликт с A/B/C-соседями; держит фигуру или термин только по инерции; companion-файлы расходятся с основным текстом.

Если существенных проблем нет, не делай косметическое переписывание. Зафиксируй `ready_for_next_fragment` или `ready_with_known_debts` с ясным объяснением. Если проблемы есть, исправь их минимально достаточно, затем обнови companion-файлы and regression audit.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P13 — public decision-map / visual-artifact pass

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md
- work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
- work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
- work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md

Проверь A10 как публичную карту решения, а не только как хороший текст. Читатель должен уметь использовать фрагмент для выбора режима работы с агентом.

Проверь:

- есть ли понятные признаки выбора;
- есть ли условия перехода к более структурированному и к более лёгкому режиму;
- нет ли режима, который выглядит всегда лучшим;
- не стала ли главная фигура декоративной;
- не слишком ли много таблиц;
- не ушли ли важные условия выбора в companion-файлы;
- нет ли противоречия между прозой и figure/table.

Для визуального слоя применяй asset-classification gate. Не делай синтетическую схему, если она тривиальна, и не превращай реальные изображения в текстовые схемы. Если нужна публичная decision-map figure, она должна быть нетривиальной и стоять рядом с тем местом текста, где читатель реально принимает решение.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P14 — языковой проход 1

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/visual-assets-and-figures.md

Приведи `A10_mode_selection_map.md` к русскому техническому языку по языковому протоколу. Не делай стилевую полировку и не меняй аргумент без необходимости.

Убери английский связующий слой и механические кальки. Сохрани имена источников, инструментов, команд, файлов, URL, `<figure>` и точные технические имена. Проверь, что URL, raw links and anchors не русифицированы и не содержат кириллицы.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P15 — языковой проход 2

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/visual-assets-and-figures.md

Повторно проверь русский текст `A10_mode_selection_map.md`. Ищи гибриды, остаточные английские объяснения, плохие кальки, ошибочно переведённые технические термины и места, где русификация стерла различие между близкими понятиями.

Не улучшай стиль ради красоты. Это ещё языковой проход: исправляй язык и техническую точность формулировок.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P16 — стилевой проход 1

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/visual-assets-and-figures.md

Сделай первый стилевой проход по `A10_mode_selection_map.md`. Текст должен звучать как человеческий технический аргумент: без summary-интонации, без бюрократических списков, без декоративного пафоса и без размазывания сильных различений.

Не выбрасывай фактуру ради гладкости и не ослабляй конфликтные ограничения. Сохрани ссылки, `<figure>` and source-specific details.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### P17 — стилевой проход 2

```text
Прочитай сначала:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/visual-assets-and-figures.md

Сделай второй стилевой проход. Проверь, читается ли `A10_mode_selection_map.md` как самостоятельный финальный узел теории, а не как досье, оглавление, maturity model, пересказ материалов или таблица всех понятий. Усиль переходы, если они нужны, но не добавляй новые факты без источников.

Проверь также, что `A10_mode_selection_matrix.md` and `A10_decision_stress_tests.md` поддерживают основной текст, но не заменяют его: matrix не должна быть финальным публичным содержанием сама по себе, а stress-tests не должны превращаться в отдельную главу.

Обнови:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

### Final verification — package/result check

```text
Прочитай сначала все целевые файлы A10:
- work/theory-writing/fragments/A10_mode_selection_map.md
- work/theory-writing/fragments/A10_mode_selection_matrix.md
- work/theory-writing/fragments/A10_decision_stress_tests.md
- work/theory-writing/fragments/A10_source_usage.md
- work/theory-writing/fragments/A10_story_anchor_map.md
- work/theory-writing/fragments/A10_figure_candidates.md
- work/theory-writing/fragments/A10_open_questions.md
- work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md

Проверь финальный результат A10:

1. C1–C4 были прочитаны и реально использованы; если нет — статус `blocked`, не выдавай готовый result.
2. A10 не является summary A1–A9, оглавлением, maturity model или красивой классификацией без решения.
3. В тексте явно есть критерии выбора, переходы, деэскалация, сочетания режимов и минимально достаточная структура.
4. `A10_mode_selection_matrix.md` существует и содержит рабочую матрицу признаков выбора.
5. `A10_decision_stress_tests.md` существует и проверяет карту на 6–8 сценариях.
6. Визуальный слой прошёл asset-classification gate; `<figure>`/`</figure>` сбалансированы; реальные assets не переписаны текстом.
7. Companion-файлы согласованы с основным текстом.
8. В тексте нет служебного мета-текста, плохих псевдотехнических формул, английского связующего слоя и ссылок на внутренние досье как на публичные источники.
9. Readiness status записан честно: `ready_for_next_fragment`, `ready_with_known_debts`, `blocked_by_source_gap`, `blocked_by_asset_pass` или `needs_human_review`.

Если проверка проходит, подготовь result archive. Если есть blocker, не маскируй его стилевой правкой: запиши blocker и выдай частичный результат с честным статусом.
```
