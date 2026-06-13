# Experimental variant: SPDD article target-plan with dossier-completeness rollback

Статус: `experimental_package_variant`; canonical SPDD target-plan не заменяется.

Назначение: контрольный вариант для сравнения результатов SPDD-статьи после наблюдения по ADR: последнее жёсткое dossier-backed completeness / coverage-matrix / `relevant but untransferred` правило могло улучшить ledger, но ухудшить последовательность и человекочитаемость статьи. Этот вариант сохраняет SPDD-specific source-depth, visual rules, local/external image candidates, свободные доборные проходы и отсутствие лимитов объёма, но откатывает hard gate полного coverage/disposition по всему досье.

---

# Target-group plan: статья атласа `spdd_method` — SPDD / OpenSPDD

Статус: `ready_for_package_manufacture_after_manual_review`.  
Article id: `spdd_method`  
Рабочее название: `SPDD / OpenSPDD`  
Уровень статьи: `core concept / method article`  
Режим будущего пакета: self-contained writing package.  
Внутренних ограничений объёма нет: размер будущей статьи определяется полнотой источниковой фактуры, техническими деталями, визуальными материалами, границами концепции и вопросом читателя.


## 1. Мини-ориентация по досье для планирования

Это ориентация для планирования будущего writing package, не черновик статьи.

Главное досье:

```text
work/dossiers/SPDD_METHOD_DOSSIER.md
```

SPDD в досье трактуется не как техника «лучшего промпта», а как способ превратить намерение изменения в сопровождаемый артефакт: его можно ревьюировать, проверять, исправлять, синхронизировать с кодом и пересматривать, когда он устаревает. Центральный объект — REASONS Canvas. Главная напряжённость статьи: Canvas может выглядеть связным и убедительным, но всё равно быть неверным, устаревшим или слишком дорогим для масштаба изменения. Поэтому статья должна показывать не только силу SPDD, но и цену превращения промпта в артефакт.

Связанные фрагменты теории для будущего пакета:

```text
work/theory-writing/fragments/00_spine_map.md
work/theory-writing/fragments/A1_change_not_prompt.md
work/theory-writing/fragments/A2_specification_adr_contract.md
work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
work/theory-writing/fragments/A7_observation_vs_evidence.md
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
work/theory-writing/fragments/A9_lifecycle_repair.md
work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
work/theory-writing/fragments/C1_specification_to_pwg.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
```

A3 и B1 — главные локальные теоретические якоря. C1 и C3 защищают переход от спецификационного артефакта к состоянию работы и свидетельствам. A7/A8/A9 не дают свести проверки, ревью и синхронизацию к декоративным шагам процесса.

Соседние досье для проверки границ:

```text
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
```

Соседние будущие статьи: `spec_kit_method`, `kiro_specs`, `constitutional_sdd`, `tdad_comparative`, `adr_method`, `persistent_work_graph`.

Главные риски дублирования:

- SPDD / Spec Kit / Kiro / Constitutional SDD: общий кластер specification methodology;
- SPDD / TDAD: API-тесты и ревью SPDD не должны стать общей статьёй о evidence/testing;
- SPDD / ADR: REASONS Canvas может фиксировать решения, но не является архитектурной памятью ADR;
- SPDD / PWG: prompt/Canvas может стать частью долговечного состояния работы, но не заменяет весь Persistent Work Graph;
- SPDD / A3/B1/C1: статья не должна механически повторить уже написанные фрагменты теории.

## 2. Контракт статьи

Вопрос читателя: как SPDD / OpenSPDD превращает намерение уровня фичи в сопровождаемый артефакт — REASONS Canvas, шаблоны, проверки, ревью и синхронизацию — и где этот подход помогает, а где создаёт ложную уверенность, устаревание или лишнюю церемонию?

Центральное объяснение статьи: SPDD нужен не просто потому, что промпт надо структурировать. Он нужен там, где намерение изменения должно пережить несколько шагов работы: анализ, ревью, генерацию, проверку поведения, исправление намерения и синхронизацию с кодом. Главный риск SPDD — убедительный, но ошибочный или устаревший Canvas.

Статья должна:

- объяснить SPDD как самостоятельную concept-first статью, а не как конспект Fowler или OpenSPDD;
- развести Fowler SPDD и OpenSPDD: Fowler SPDD задаёт концептуальную рамку промпта/Canvas как сопровождаемого артефакта намерения, OpenSPDD показывает операционализацию через команды, шаблоны, адаптерный слой, `prompt-update`, `sync` и optional checks;
- показать REASONS Canvas как центральный артефакт намерения: секции, жизненный цикл, проверки, синхронизацию и сбои;
- раскрыть рабочую цепочку: история/анализ → Canvas → генерация → API-свидетельства → ревью → `prompt-update` / `sync`;
- показать повторяющиеся риски: убедительный, но неверный Canvas; устаревший Canvas после изменения кода; локальный патч вместо обновления намерения; церемония дороже изменения; тесты подтверждают поведение, но не доказывают правильность исходного намерения;
- сохранить конкретные технические детали OpenSPDD commands/templates, примеров Fowler и локальных визуальных материалов;
- показать место SPDD в AI-driven SDLC: specification layer, evidence, authority и lifecycle repair, но без превращения статьи в общую теорию;
- провести границы с Spec Kit, Kiro, Constitutional SDD, TDAD, ADR и PWG;
- использовать визуальные материалы как реальные assets/placeholders, а не как текстовые суррогаты картинок.

Статья не должна быть:

- общей статьёй обо всём specification-driven development;
- руководством по «лучшим промптам»;
- заменой будущих статей Spec Kit, Kiro, Constitutional SDD, TDAD, ADR или PWG;
- справочником команд OpenSPDD;
- рекламой SPDD без цены метода и failure modes;
- пересказом B1/A3/C1;
- галереей Fowler-изображений без достаточного объяснения.

Контролируемое повторение с теорией разрешено, если оно нужно для самостоятельного чтения статьи. Механический copy-paste из A3/B1/C1 запрещён.

## 3. Обрабатываемые файлы будущего article package

```yaml
- path: work/atlas/articles/spdd_method.md
  status: future
  role: primary
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Основная concept-first статья атласа."
- path: work/atlas/articles/spdd_method_source_usage.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Фактически открытые и использованные источники."
- path: work/atlas/articles/spdd_method_source_transfer_ledger.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Что перенесено из досье/источников, что сохранено, отложено или отклонено."
- path: work/atlas/articles/spdd_method_image_plan.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Локальные assets, внешние real-image candidates, synthetic figure decisions and placement."
- path: work/atlas/articles/spdd_method_external_image_queue.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Внешние визуальные кандидаты для будущего asset-pass."
- path: work/atlas/articles/spdd_method_open_questions.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Source gaps, конкретные C5/A10-долги и human decisions."
- path: work/atlas/articles/spdd_method_theory_links.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Смысловые связи с фрагментами теории и соседними статьями атласа."
- path: work/atlas/articles/spdd_method_degradation_and_duplication_audit.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Проверка на копирование теории, drift в technical appendix и пересечения с соседями."
- path: work/atlas/articles/spdd_method_readiness_report.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Финальный статус готовности и оставшиеся долги."
```

Режим группы: `linked-target-edit`. Большинство проходов обновляют статью и как минимум один companion-файл.

## 4. Exact read-only inputs to bundle

### Управляющие документы и blueprint

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
```

### Синхронизация с C5/A10 и provenance manufactury-процесса

```text
work/theory-writing/fragments/C5_theory_to_technical_atlas.md
work/theory-writing/fragments/C5_concept_atlas_article_map.md
work/theory-writing/fragments/C5_source_usage.md
work/theory-writing/fragments/A10_mode_selection_map.md
work/theory-writing/fragments/A10_mode_selection_matrix.md
work/theory-writing/fragments/A10_decision_stress_tests.md
work/theory-writing/fragments/A10_source_usage.md
work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md
```

Эти файлы существуют в текущем репозиторном состоянии и должны входить в future self-contained bundle как read-only inputs. C5 задаёт concept-first atlas architecture и article map; A10 задаёт mode-selection / reader-routing context. Они не являются hard blockers для каждой статьи, но больше не считаются отсутствующим контекстом. Если будущий article-writing run обнаружит реальное несогласование, оно фиксируется как конкретный долг, а не как стандартная пометка `C5/A10 sync pending`.

### Правила

```text
protocols/rules/visual-assets-and-figures.md
protocols/rules/language-style-rules.md
protocols/rules/russian-language.md
protocols/rules/terminology-and-translation.md
protocols/rules/human-technical-style.md
protocols/rules/english-source-handling.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
```

### Основное и соседние досье

```text
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
```

### Теоретические фрагменты и companion-файлы

```text
work/theory-writing/fragments/00_spine_map.md
work/theory-writing/fragments/00_spine_map_source_usage.md
work/theory-writing/fragments/A1_change_not_prompt.md
work/theory-writing/fragments/A1_source_usage.md
work/theory-writing/fragments/A2_specification_adr_contract.md
work/theory-writing/fragments/A2_source_usage.md
work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
work/theory-writing/fragments/A3_source_usage.md
work/theory-writing/fragments/A3_figure_candidates.md
work/theory-writing/fragments/A7_observation_vs_evidence.md
work/theory-writing/fragments/A7_source_usage.md
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
work/theory-writing/fragments/A8_source_usage.md
work/theory-writing/fragments/A9_lifecycle_repair.md
work/theory-writing/fragments/A9_source_usage.md
work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
work/theory-writing/fragments/B1_source_usage.md
work/theory-writing/fragments/B1_figure_candidates.md
work/theory-writing/fragments/C1_specification_to_pwg.md
work/theory-writing/fragments/C1_source_usage.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
work/theory-writing/fragments/C3_source_usage.md
```

### Публичный контекст сайта

```text
content/Theoretical_synthesis.md
content/Cross_story_synthesis.md
```

### Asset catalog и локальные изображения

```text
work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
content/assets/theory-images/MANIFEST.md
content/assets/theory-images/fowler-spdd-overview.svg
content/assets/theory-images/fowler-spdd-reasons-canvas.svg
content/assets/theory-images/fowler-spdd-workflow.svg
content/assets/theory-images/fowler-spdd-code-review.svg
content/assets/theory-images/fowler-spdd-analysis-review.png
content/assets/theory-images/fowler-spdd-api-test-script.png
content/assets/theory-images/fowler-spdd-api-test-results.png
content/assets/theory-images/fowler-spdd-prompt-update.png
```

## 5. Внешние источники для будущего writing package

Явно известные первоисточники:

```text
https://martinfowler.com/articles/structured-prompt-driven/
https://martinfowler.com/articles/structured-prompt-driven/abstraction-first.html
https://martinfowler.com/articles/structured-prompt-driven/alignment.html
https://martinfowler.com/articles/structured-prompt-driven/iterative-review.html
https://github.com/gszhangwei/open-spdd
https://github.com/gszhangwei/open-spdd/blob/main/README.md
https://github.com/gszhangwei/open-spdd/blob/main/docs/design-philosophy.md
https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-analysis.md
https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-reasons-canvas.md
https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-generate.md
https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-prompt-update.md
https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/core/spdd-sync.md
https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-story.md
https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-api-test.md
https://github.com/gszhangwei/open-spdd/blob/v0.4.9/internal/templates/data/optional/spdd-code-review.md
https://raw.githubusercontent.com/gszhangwei/open-spdd/main/internal/templates/data/optional/spdd-reverse.md
https://github.com/gszhangwei/token-billing/blob/after-enhancement/spdd/template/TEST-SCENARIOS-TEMPLATE.md
https://github.com/github/gh-aw/blob/main/.github/workflows/daily-spdd-spec-planner.md
https://github.com/codemie-ai/codemie-code/issues/274
https://mgks.dev/blog/2026-04-29-treating-prompts-like-code-what-spdd-gets-right-about-ai-assisted-development/
https://www.webreactiva.com/blog/spdd
https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
https://arxiv.org/abs/2605.11027
https://arxiv.org/html/2602.00180
```

Дополнительно будущий пакет может открывать первичные ссылки, найденные внутри `work/dossiers/SPDD_METHOD_DOSSIER.md` и перечисленных source-usage файлов. Внешний поиск разрешён для проверки, насыщения источников и поиска реальных визуальных кандидатов, но не для добавления новых тем статей.

## 6. Почему выбранная очередь подходит именно этой статье

Полная очередь article-writing package подходит SPDD / OpenSPDD, потому что это не короткая source note. У статьи есть несколько разных слоёв, которые нельзя раскрыть одним обзорным проходом: концептуальная рамка Fowler, конкретная операционализация OpenSPDD, локальные изображения, внешние визуальные кандидаты, пример биллинга, API-свидетельства, code review, `prompt-update`, `sync` и опасные пересечения с соседними specification/evidence/ADR/PWG статьями. Более короткая очередь почти наверняка дала бы либо пересказ Fowler/OpenSPDD, либо справочник команд.

Главные зоны источниковой глубины:

1. Fowler SPDD: промпт как сопровождаемый артефакт, REASONS Canvas, workflow, review, API-test evidence и `prompt-update`.
2. OpenSPDD: команды и шаблоны как машина поддержания Canvas, а не простой каталог CLI-команд.
3. Цена метода: неверный Canvas, устаревший Canvas, дрейф, чрезмерная церемония, стоимость синхронизации и граница окупаемости.
4. Свидетельства и ревью: API tests, code review и token billing example как разные формы подтверждения поведения и человеческой проверки, но не как доказательство правильности исходного намерения.
5. Границы: Spec Kit/Kiro/Constitutional SDD, TDAD, ADR и PWG используются ровно настолько, чтобы SPDD не присваивал их функции.


## 7. Очередь будущих prompt-ов

Каждый prompt ниже должен быть помещён в будущий self-contained writing package. Он задаёт направление и критерии качества, а не мелочную инструкцию по каждой фразе. Все проходы сохраняют правило: не ограничивать объём статьи заранее и не закрывать нехватку фактуры гладкой общей прозой.

### P01 — первичный концептуальный черновик

```text
Прочитай сначала:
- work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Создай первичный черновик `work/atlas/articles/spdd_method.md` как самостоятельную статью атласа по SPDD / OpenSPDD. Не ограничивай объём искусственно. Не пересказывай досье подряд: выстрой объяснение вокруг вопроса читателя, REASONS Canvas, workflow, свидетельств поведения, ревью, `prompt-update`, `sync` и цены поддержания Canvas. Создай первые версии `spdd_method_source_usage.md`, `spdd_method_source_transfer_ledger.md`, `spdd_method_open_questions.md`, `spdd_method_theory_links.md`.
```

### P02 — article contract and boundaries

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/dossiers/KIRO_SPECS_DOSSIER.md
- work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
- work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md

Уточни article contract в companion-файлах: вопрос читателя, уровень статьи, границы с соседними статьями, допустимый повтор с теорией, использование C5/A10 как доступного read-only context. Исправь основной текст, если он выходит за границы SPDD или недодаёт самостоятельное объяснение.
```

### P03 — dossier inventory

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/atlas/articles/spdd_method_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Сделай inventory досье: что уже перенесено, что осталось неперенесённым, что требует открытия первоисточников. Обнови основной текст только при явном пропуске article-critical материала. Запиши результат в `spdd_method_source_transfer_ledger.md` and `spdd_method_source_usage.md`.
```

### P04 — source-depth 1: ключевая фактура

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/atlas/articles/spdd_method_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md

Открой первичные источники Fowler SPDD и OpenSPDD README/design philosophy. Раскрой анатомию REASONS Canvas: какие части Canvas удерживают намерение изменения, почему Canvas становится сопровождаемым артефактом и где он может ввести в заблуждение. Ссылки ставь сразу в месте ввода факта. Обнови source usage и transfer ledger.
```

### P05 — source-depth 2: техническая механика

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/atlas/articles/spdd_method_source_usage.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md

Открой шаблоны OpenSPDD commands: `spdd-analysis`, `spdd-reasons-canvas`, `spdd-generate`, `spdd-prompt-update`, `spdd-sync`, optional `spdd-story`, `spdd-api-test`, `spdd-code-review`, `spdd-reverse`. Раскрой OpenSPDD как машину поддержания Canvas: какие команды создают, используют, проверяют, обновляют и синхронизируют артефакт намерения. Не превращай статью в справочник команд; каждая команда должна объяснять функцию метода.
```

### P06 — source-depth 3: ограничения и сбои

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/atlas/articles/spdd_method_open_questions.md
- protocols/rules/source-and-provenance.md

Сделай failure modes несущей частью статьи: убедительный, но неверный Canvas; устаревший Canvas после изменения кода; локальный патч вместо обновления намерения; чрезмерная церемония; стоимость синхронизации; граница окупаемости; необходимость человеческого суждения. Используй первоисточники и разделы досье. Не сглаживай конфликтные места. Обнови open questions и degradation audit.
```

### P07 — source-depth 4: свидетельства, ревью и примеры

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/C3_pwg_to_evidence.md
- protocols/rules/source-and-provenance.md

Раскрой API-test evidence, code review, token billing example, expected/actual/result evidence и review triage как разделение поведения, ревью и исправления намерения. Покажи, что свидетельства помогают human review, но не доказывают корректность всего исходного намерения. Обнови source usage и theory links.
```

### P08 — source-depth 5: анти-конспектная проверка

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/atlas/articles/spdd_method_source_transfer_ledger.md
- protocols/rules/content-preservation.md
- protocols/rules/human-technical-style.md

Проверь, не осталась ли статья конспектом. Особенно ищи места, где текст говорит «SPDD синхронизирует намерение и код», «Canvas обновляется», «ревью обнаруживает проблему» или «OpenSPDD поддерживает workflow», но не показывает, как это происходит в источнике. Разверни такие места прямым описанием. Сохрани фактуру, команды, версии, ограничения и источниковую конкретику.
```

### P09 — свободный добор материала 1

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/atlas/articles/spdd_method_source_transfer_ledger.md
- work/atlas/articles/spdd_method_open_questions.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- protocols/rules/source-and-provenance.md

Сам определи главный недобор фактуры в статье, добавь материал в текст и companion-файлы. В `spdd_method_source_transfer_ledger.md` запиши: что счёл главным недобором, что добавил, откуда взял материал, что осталось долгом.
```

### P10 — свободный добор материала 2

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/atlas/articles/spdd_method_theory_links.md
- work/atlas/articles/spdd_method_degradation_and_duplication_audit.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- protocols/rules/human-technical-style.md

Найди слабое место в объяснении механизма, границ или сравнения с соседними статьями. Исправь статью и companion-файлы. Не добавляй новые темы статей; работай внутри SPDD / OpenSPDD.
```

### P11 — visual asset pass 1: локальные assets

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
- work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
- content/assets/theory-images/MANIFEST.md
- content/assets/theory-images/fowler-spdd-overview.svg
- content/assets/theory-images/fowler-spdd-reasons-canvas.svg
- content/assets/theory-images/fowler-spdd-workflow.svg
- content/assets/theory-images/fowler-spdd-code-review.svg
- content/assets/theory-images/fowler-spdd-analysis-review.png
- content/assets/theory-images/fowler-spdd-api-test-script.png
- content/assets/theory-images/fowler-spdd-api-test-results.png
- content/assets/theory-images/fowler-spdd-prompt-update.png
- protocols/rules/visual-assets-and-figures.md

Классифицируй локальные SPDD assets как `local_image_asset`. Вставляй релевантные изображения как настоящие `<figure><img ...></figure>` с публичными подписями. Не переписывай изображения текстовыми схемами. Особое внимание: `reasons-canvas`, `workflow`, `api-test-script/results`, `code-review`, `prompt-update` должны поддерживать основные узлы статьи, а не висеть как галерея. Запиши решения в `spdd_method_image_plan.md`.
```

### P12 — visual asset pass 2: внешние реальные изображения

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
- protocols/rules/visual-assets-and-figures.md
- protocols/rules/source-and-provenance.md

Начни с разделов досье о кандидатах на иллюстрации. Затем открой первоисточники и найди реальные screenshots, diagrams, tables или UI images, которые должны стать `external_real_image_candidate`: OpenSPDD Plan vs REASONS Canvas, OpenSPDD code-review report, risk traceability, Canvas ↔ sync и другие кандидаты, если они реально помогают статье. Не скачивай изображения. Если кандидат нужен в статье, поставь inline placeholder в месте будущего использования и добавь нижний раздел `Внешние изображения для asset-pass` с источником, что взять, зачем нужно, предлагаемым локальным путём, местом в тексте и статусом `external-real-candidate; download/rights/quality check required`. Синхронизируй `spdd_method_external_image_queue.md` и `spdd_method_image_plan.md`.
```

### P13 — visual asset pass 3: собственные схемы

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/atlas/articles/spdd_method_image_plan.md
- protocols/rules/visual-assets-and-figures.md
- protocols/rules/human-technical-style.md

Рассмотри собственные synthetic figures только там, где они объясняют нетривиальную границу, переход жизненного цикла или сравнение, которое не закрывают проза и уже существующие assets. Для SPDD допустимые кандидаты — например граница Fowler SPDD / OpenSPDD, риск неверного Canvas или отношение Canvas к PWG/evidence. Отклоняй декоративные схемы и любые схемы, которые заменяют готовую source-иллюстрацию. Обновляй статью и image plan только если схема проходит usefulness gate.
```

### P14 — concept reinforcement 1: самостоятельное объяснение концепции

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- protocols/rules/human-technical-style.md

Усиль статью как самостоятельное объяснение. Читатель должен понять, зачем существует SPDD, что делает REASONS Canvas, почему Canvas требует сопровождения и как OpenSPDD превращает эту идею в рабочую систему. Не своди статью к общим лозунгам о промптах.
```

### P15 — concept reinforcement 2: механизм, границы, типичные ошибки

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/dossiers/KIRO_SPECS_DOSSIER.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- protocols/rules/human-technical-style.md

Уточни механизм, границы и типичные ошибки: SPDD как набор prompt templates, SPDD как formal methods, SPDD как замена ADR, SPDD как evidence framework, SPDD как полный PWG, OpenSPDD как просто CLI. Исправь основной текст и degradation/duplication audit так, чтобы статья не присваивала чужие функции.
```

### P16 — concept reinforcement 3: связь с теорией

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/theory-writing/fragments/00_spine_map.md
- work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
- work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
- work/theory-writing/fragments/C1_specification_to_pwg.md
- work/atlas/articles/spdd_method_theory_links.md

Свяжи SPDD с AI-driven SDLC frame, не превращая статью в главу общей теории. Сделай смысловые back-links явными: какой теоретический вопрос помогает объяснить каждая связь, а что остаётся за соседними статьями.
```

### P17 — общий редакторский проход 1

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/atlas/articles/spdd_method_source_transfer_ledger.md
- work/atlas/articles/spdd_method_image_plan.md
- work/atlas/articles/spdd_method_degradation_and_duplication_audit.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Оцени, насколько статья выполняет поставленную задачу. Сначала сформулируй проблемы, затем исправь их. Не проводи языковой или визуальный pass под видом редакторского. Заверши regression audit и readiness status в `spdd_method_degradation_and_duplication_audit.md`.
```

### P18 — общий редакторский проход 2

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/atlas/articles/spdd_method_degradation_and_duplication_audit.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Повтори общий editorial repair после предыдущих правок. Проверь структуру, причинность, границы, source loss, duplicated work and publication readiness. Исправь реальные дефекты; не сокращай фактуру ради гладкости.
```

### P19 — общий редакторский проход 3

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/atlas/articles/spdd_method_source_usage.md
- work/atlas/articles/spdd_method_image_plan.md
- work/atlas/articles/spdd_method_degradation_and_duplication_audit.md
- protocols/rules/human-technical-style.md

Проверь, не стала ли статья второй теорией, справочником команд, пересказом досье, набором картинок или кратким конспектом. Исправь только реальные дефекты и зафиксируй readiness.
```

### P20 — public/article structure pass

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- protocols/rules/human-technical-style.md
- protocols/rules/russian-language.md

Проверь структуру публичной статьи: вход, подзаголовки, путь читателя, placement фигур, подписи, отсутствие executor meta-text. Добавляй или убирай подзаголовки только если это помогает видеть смысловые границы. Не превращай текст в список.
```

### P21 — companion sync

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/atlas/articles/spdd_method_source_usage.md
- work/atlas/articles/spdd_method_source_transfer_ledger.md
- work/atlas/articles/spdd_method_image_plan.md
- work/atlas/articles/spdd_method_external_image_queue.md
- work/atlas/articles/spdd_method_open_questions.md
- work/atlas/articles/spdd_method_theory_links.md
- work/atlas/articles/spdd_method_degradation_and_duplication_audit.md

Синхронизируй companion-файлы со статьёй. Удали устаревшие долги, сохрани настоящие blockers, не оставляй стандартных `C5/A10 sync pending`: C5 и A10 доступны как read-only context, а любые проблемы должны быть конкретными долгами статьи. Проверь, что source usage, image plan, external image queue и theory links соответствуют фактической статье.
```

### P22 — языковой проход 1

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/english-source-handling.md

Сделай языковой проход по основному тексту: русский пользовательский текст, английский только для допустимых имён, команд, файлов и source terms. Не меняй аргумент и не выбрасывай фактуру.
```

### P23 — языковой проход 2

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- protocols/rules/language-style-rules.md
- protocols/rules/russian-language.md
- protocols/rules/terminology-and-translation.md

Второй языковой проход: найди остаточный английский клей, кальки, неровные русские формулы и mixed-language labels в prose/captions. Исправь без смысловой деградации.
```

### P24 — стилевой проход 1

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Сделай стилевой проход: спокойное техническое объяснение для сильного инженера, без маркетинга, лозунгов, декоративных метафор и bullet-summary там, где нужна причинность. Сохрани источниковую конкретику.
```

### P25 — стилевой проход 2

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- protocols/rules/human-technical-style.md
- protocols/rules/content-preservation.md

Второй стилевой проход: убери механический ритм, повторяющиеся формулы `не X, а Y`, канцелярит и empty abstractions. Не переписывай хорошо работающие технические места ради красоты.
```

### Final — финальная проверка и package-readiness

```text
Прочитай сначала:
- work/atlas/articles/spdd_method.md
- work/atlas/articles/spdd_method_source_usage.md
- work/atlas/articles/spdd_method_source_transfer_ledger.md
- work/atlas/articles/spdd_method_image_plan.md
- work/atlas/articles/spdd_method_external_image_queue.md
- work/atlas/articles/spdd_method_open_questions.md
- work/atlas/articles/spdd_method_theory_links.md
- work/atlas/articles/spdd_method_degradation_and_duplication_audit.md
- work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
- protocols/rules/visual-assets-and-figures.md

Проверь реальные файлы будущего результата: основной article file создан и не пуст; все companion-файлы из секции обрабатываемых файлов существуют и синхронизированы; source usage и source transfer ledger заполнены; внешние факты имеют provenance; локальные assets вставлены как `<figure><img ...></figure>`; external real candidates имеют inline placeholders, нижний раздел `Внешние изображения для asset-pass` и запись в external image queue; synthetic figures редки и проходят usefulness/nontriviality gate; controlled repetition с теорией оправдан; статья не является конспектом, справочником команд, копией всей теории или складом технических деталей. Запиши `spdd_method_readiness_report.md`, MANIFEST/VERIFY/RESUME для package output и финальный readiness status.
```



## Правило решений по визуальным кандидатам

Будущий article-writing package должен начинать работу с изображениями сразу из трёх источников:

1. локальные asset catalogs и manifests;
2. общий каталог внешних image candidates;
3. раздел основного досье с кандидатами на иллюстрации, особенно заголовки вроде `## Кандидаты на иллюстрации`, `Кандидаты на изображения`, `image candidates` или эквивалентные списки.

Для каждого image candidate из досье будущий пакет должен зафиксировать решение в `spdd_method_image_plan.md`: `inserted_inline_external_placeholder`, `external_queue_only`, `deferred`, `rejected`, `superseded_by_local_asset` или `not_found_in_source`, с короткой причиной.

Если кандидат нужен в статье, пакет должен поставить inline `<figure data-asset-status="external-real-candidate">` в месте будущего использования изображения и продублировать тот же item в нижнем разделе `Внешние изображения для asset-pass` и в `spdd_method_external_image_queue.md`.

Если релевантный локальный asset уже существует, действует правило insert-or-explain: вставить его как `<figure><img ...></figure>` по месту применения или явно отклонить в image plan. Нельзя заменять реальное изображение, screenshot, diagram, template, table или локальный asset синтетической текстовой схемой, если пользователь прямо не попросил перерисовать/заменить изображение.

Финальная visual/source проверка:

- каждый dossier image candidate имеет disposition в `spdd_method_image_plan.md`;
- каждый inline external-real placeholder также есть в нижнем разделе `Внешние изображения для asset-pass` и в `spdd_method_external_image_queue.md`;
- каждый релевантный local asset либо вставлен как настоящий `<img>` figure, либо явно отклонён с причиной;
- ни одно реальное source image или local asset не заменено текстовой/synthetic diagram.

## Манифест prompt-records для сборщика пакета

Этот manifest разворачивает очередь будущего article-writing package в отдельные prompt records. При сборке executor-пакета нельзя оставлять сгруппированные диапазоны вроде `P04–P08` или `P17–P19` одним record: каждый пункт ниже должен стать отдельным gated prompt.

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
P17 — general editorial pass 1
P18 — general editorial pass 2
P19 — general editorial pass 3
P20 — public/article structure pass
P21 — companion sync / source ledger / image queue pass
P22 — language pass 1
P23 — language pass 2
P24 — style pass 1
P25 — style pass 2
Final — final verification, package output, readiness status
```

Очередь выше может описывать несколько проходов вместе ради читаемости, но package manufacture должен развернуть их по этому манифесту и сохранить article-specific акценты из очереди и контракта статьи.


## 8. Проверки для S04–S05

S04 должен проверить buildability:

- все read-only paths существуют;
- future outputs перечислены точно;
- bundle не зависит от неявного repository context;
- будущие prompt-ы не содержат placeholders вроде «релевантные файлы»;
- все image paths существуют или явно отмечены как external-real candidates;
- idempotency/rerun/emergency packaging покрыты будущим package protocol.

## 8.1. S04 integrated guardrails

S04 проверил план как будущий package contract. Все последующие шаги должны сохранять эти встроенные guardrails:

- source-depth проходы обязаны раскрывать досье и первоисточники, а не писать обзор;
- P09/P10 являются настоящими проходами добора материала и связности, а не декоративным повтором;
- внешний поиск разрешён только для проверки, насыщения источников и визуальных кандидатов, но не для создания новых тем статей;
- локальные SPDD assets нельзя игнорировать из-за тяжёлых файлов: они перечислены точными путями и входят в bundle;
- external-real candidates требуют inline placeholder, нижний раздел `Внешние изображения для asset-pass` и external image queue;
- synthetic figures допустимы только после usefulness/nontriviality gate;
- P21 синхронизирует все companion outputs;
- Final проверяет реальные файлы результата, а не только общее впечатление от статьи.

S05 должен проверить смысловую готовность:

- очередь действительно подходит статье SPDD;
- план не пишет статью заранее;
- план не собирает article-writing package;
- C5/A10 доступны как read-only context; если появится проблема синхронизации, она должна быть конкретной, а не стандартным `sync pending`;
- итоговый status может быть `ready_for_package_manufacture_after_manual_review` только после проверки точных путей, article contract и границ.

## 9. S05 readiness stamp

Readiness status: `ready_for_package_manufacture_after_manual_review`.

План механически пригоден для будущей сборки article-writing package: target outputs перечислены, read-only inputs имеют точные пути, локальные SPDD assets зафиксированы, source-depth/free expansion/visual/concept/editorial/language/style/final verification проходят включены, companion-файлы синхронизируются, внутренних ограничений объёма нет.

Ручной просмотр желателен перед package manufacture по трём причинам:

- статья имеет высокий риск boundary overlap с Spec Kit, Kiro, Constitutional SDD, TDAD, ADR и PWG;
- C5/A10 доступны как read-only context для article tier, semantic back-links и reader routing; конкретные несогласования фиксируются как долги статьи, но стандартного `sync pending` нет.

Сборка executor package разрешена после ручной проверки article contract, уровня статьи, границ и C5/A10 context.



