# Target group plan: A7 — observation vs evidence

Статус: рабочий план целевой группы. По этому документу можно собрать исполнительный пакет для несущего фрагмента A7. План не является опубликованным текстом теории.

## 1. Обрабатываемые файлы

```yaml
- path: work/theory-writing/fragments/A7_observation_vs_evidence.md
  status: future
  role: primary
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Основной фрагмент: observation helps work continue; evidence lets a human accept or reject a change."

- path: work/theory-writing/fragments/A7_source_usage.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Источники, фактически использованные for TDAD, ADR confirmation, Roast, Willison, Arvid, Stripe and Product Migration evidence claims."

- path: work/theory-writing/fragments/A7_story_anchor_map.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Короткие якоря for transcripts, browser observations, governance gates, harness, validation loop and replay/observability."

- path: work/theory-writing/fragments/A7_figure_candidates.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Кандидаты на иллюстрации for observation -> evidence -> human acceptance and false-completion boundary."

- path: work/theory-writing/fragments/A7_open_questions.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Пробелы в источниках around TDAD, ADR confirmation, product migration or replay/observability evidence."

- path: work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Audit that summaries, traces, logs, replays and PWG completed statuses are not mistaken for evidence packages."
```

Целевая группа не является ``linked-target-edit``: основной текст один. A7 must explain acceptance evidence, not simply list observability mechanisms.

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

### Главные досье and reports

```text
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md
```

### Главные истории

```text
content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

### Дополнительные источники

```text
content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
work/reports/PRODUCT_MIGRATION_CLAUDE_CODE_ANTI_DEGRADATION_REPORT.md
work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
work/theory-source-map-ai-driven-sdlc.md
```

### Story-dossiers

```text
work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
```

### Сравнительные отчёты и аудиты

```text
work/reports/PRODUCT_MIGRATION_CLAUDE_CODE_ANTI_DEGRADATION_REPORT.md
work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md
work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md
work/reports/TDAD_COMPARATIVE_DOSSIER_QUALITY_AUDIT.md
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
```

### Внешние источники

Открывать внешние источники нужно только под конкретные утверждения будущего текста; не проходить весь список ради широты.

Явно известные источники: TDAD papers and repositories, contract tests, API compatibility sources, architecture fitness functions, test data / oracle independence, k6, SLO / error budget sources, `oasdiff`, Pact, `can-i-deploy`, Argo Rollouts, Flagger, OpenFeature, ADR confirmation/status sources, Roast replay/observability, Simon Willison transcripts / Showboat / benchmark materials, Arvid browser/runtime-observation materials, Stripe Minions validation loop/devbox sources, Product Migration sources and source registers.

Выводимые источники: inline-ссылки, source registers, source notes, tool names, article titles, repositories, figure candidates, replay/observability details and oracle/acceptance vocabulary from `TDAD_COMPARATIVE_DOSSIER.md`, `ADR_METHOD_DOSSIER.md`, `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`, Product Migration dossier/report, Stripe and Shopify story-dossiers, Simon/Arvid/Stripe/Roast stories and `SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md`.

## 3. Очередь рабочих prompt-ов

### P01 — первичный фрагмент

```text
Прочитай сначала:
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
- content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
- content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Создай первый черновик `work/theory-writing/fragments/A7_observation_vs_evidence.md`. Композиционная функция фрагмента: узел различения между тем, что помогает агенту действовать, и тем, что даёт человеку право принять изменение. Он должен сделать раздел о проверке не списком тестов, а теорией evidence quality.

Покажи не только различие observation/evidence, но и условия превращения наблюдения в свидетельство: scope, oracle, сохранённая трасса, воспроизводимость, связь с требованием, приемлемый владелец проверки и понятный критерий отказа. Без этой цепочки фрагмент станет красивым лозунгом, а не инженерным различением.

Не пиши обзор источников и не пересказывай истории. Строй аргумент как часть общей теории: один ход мысли, несколько точных фактических якорей, ссылки сразу в тексте. Если факт взят через внутреннее досье или план, не ссылайся на досье: найди первоисточник, указанный внутри него, а если источник нельзя уверенно восстановить — не ставь ссылку.

TDAD, ADR confirmation, Product Migration, Roast replay, Simon Willison transcripts, Stripe validation and Arvid browser sources открывать только для text claims.

Запиши:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
```

### P02 — добавление фактуры по заданной оси

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
- content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
- content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Перечитай `work/theory-writing/fragments/A7_observation_vs_evidence.md` и усили его фактурой по направлению: усилить observation line через browser/logs/transcripts/replay and agent working traces.

Открывай внешние источники только под конкретные утверждения текста. Если добавляешь новый внешний источник, занеси его в `work/theory-writing/fragments/A7_source_usage.md`: источник, почему добавлен, какое утверждение поддерживает, где использован. Ссылки на внутренние досье, планы и отчёты не являются валидными ссылками в основном тексте.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
```

### P03 — добавление фактуры по соседней оси

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
- content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
- content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Снова перечитай `work/theory-writing/fragments/A7_observation_vs_evidence.md` и добавь недостающую фактуру по направлению: усилить evidence line через tests, contract tests, architecture fitness, API compatibility, SLO, rollout, owner review.

Не раздувай текст ради полноты. Добавляй только то, что усиливает функцию фрагмента. Если полезный материал найден во внутреннем документе, открой его внешний источник; если первоисточник не восстанавливается, лучше оставить утверждение без ссылки, чем ссылаться на рабочее досье.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
```

### P04 — evidence-chain pass

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
- work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Сделай evidence-chain pass. Проверь, есть ли в тексте не просто список проверок, а цепочка: что агент наблюдает → что сохраняется как артефакт → какой oracle делает это проверкой → кто имеет право принять вывод → как это связано с PWG, ADR, review or rollout.

Если цепочка распадается, перестрой соответствующие абзацы. Не превращай фрагмент в каталог тестов. Новые внешние источники открывай только под конкретные утверждения и заноси в `work/theory-writing/fragments/A7_source_usage.md`.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
```

### P05 — свободное раскрытие источников

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
- content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
- content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Сделай один свободный source/depth pass. Раскрой источники, которые выводятся из текущего текста, inline-ссылок, source usage, figure-кандидатов, названий инструментов, авторов, статей, репозиториев и методологий. Проверь, не остался ли рядом с уже написанным текстом полезный материал, который нужно добавить. Для визуального материала в этом проходе сначала выполняй asset-классификацию: не считай figure-candidate доказательством, что нужно сделать текстовую схему; проверь, не является ли это реальным внешним изображением или уже существующим локальным asset.

Обязательно открой все новые внешние источники, которые находишь в этом проходе, до того как использовать их. Каждый новый источник занеси в `work/theory-writing/fragments/A7_source_usage.md`. Не добавляй источники для широты и не превращай текст в каталог фактов.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
```

### P06 — системное выравнивание

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Выравняй `work/theory-writing/fragments/A7_observation_vs_evidence.md` как несущий фрагмент общей теории. Проверь, ведёт ли он один продолжающийся смысл, не спорит ли со скелетоном, не пересказывает ли истории и не стал ли он оглавлением будущих глав вместо самостоятельного аргумента.

Сохрани фактуру и ссылки. Убери повторы, слишком локальные рамки и места, где текст выглядит как список тем. Отдельно проверь, не стал ли фрагмент лозунгом про observation/evidence без инженерной цепочки принятия: артефакт, oracle, owner, отказ and completion boundary должны быть видны. Если часть материала лучше вынести в технический атлас, отметь это в `work/theory-writing/fragments/A7_open_questions.md` или `work/theory-writing/fragments/A7_degradation_and_duplication_audit.md`, но не удаляй важную мысль без замены.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_open_questions.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
```

### P07 — языковой проход 1

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Приведи `work/theory-writing/fragments/A7_observation_vs_evidence.md` к русскому техническому языку по языковому протоколу. Не делай стилевую полировку и не меняй аргумент без необходимости.

Убери английский связующий слой и механические кальки. Сохрани имена источников, инструментов, команд, файлов, URL, `<figure>` и точные технические имена. Проверь, что URL, raw links and anchors не русифицированы и не содержат кириллицы.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
```

### P08 — языковой проход 2

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Повторно проверь русский текст `work/theory-writing/fragments/A7_observation_vs_evidence.md`. Ищи гибриды, остаточные английские объяснения, плохие кальки, ошибочно переведённые технические термины и места, где русификация стерла различие между близкими понятиями.

Не улучшай стиль ради красоты. Это ещё языковой проход: исправляй язык и техническую точность формулировок.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
```

### P09 — стилевой проход 1

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Сделай первый стилевой проход по `work/theory-writing/fragments/A7_observation_vs_evidence.md`. Текст должен звучать как человеческий технический аргумент: без summary-интонации, без бюрократических списков, без декоративного пафоса и без размазывания сильных различений.

Не выбрасывай фактуру ради гладкости и не ослабляй конфликтные ограничения. Сохрани ссылки, `<figure>` and source-specific details.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
```

### P10 — стилевой проход 2

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Сделай второй стилевой проход. Проверь, читается ли `work/theory-writing/fragments/A7_observation_vs_evidence.md` как самостоятельный узел теории, а не как досье, оглавление или пересказ материалов. Усиль переходы, если они нужны, но не добавляй новые факты без источников.

Если история используется слишком широко, оставь её как якорь и перенеси ограничение в `work/theory-writing/fragments/A7_story_anchor_map.md`. Если figure-кандидат не поддержан текстом, уточни его в `work/theory-writing/fragments/A7_figure_candidates.md`.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
```

### P11 — repair-pass: содержательная починка

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Прочитай текущий результат как готовящийся фрагмент теории, а не как черновой конспект. Сначала составь короткий план содержательной починки: где утверждение слабое, неверно опирается на источник, выглядит как пересказ истории, превращается в оглавление, теряет композиционную функцию узла или ссылается на внутреннее досье вместо первоисточника. Особо проверь ссылки: внутренние досье, планы и отчёты не являются валидными публичными источниками; если факт пришёл из них, найди первоисточник, указанный или выводимый из внутреннего материала. Если первоисточник нельзя уверенно восстановить, ссылку не ставь.

Перед применением правки классифицируй найденные проблемы по карте дефектов из `protocols/rules/fragment-defect-analysis-and-repair.md`: композиционные, фактологические, источниковые/provenance, структурные, визуальные, языковые/стилевые, мета- и интеграционные/regression-дефекты. Коротко запиши для каждого существенного дефекта: место, почему это проблема и действие. Отдельно проверь функцию фрагмента против target-group role: фрагмент должен делать именно свою работу в общей теории, а не превращаться в обзор источников, пересказ истории, самостоятельную мини-главу или повтор соседнего узла. Не переписывай текст целиком, если дефект локальный; применяй минимальную достаточную правку.

Перед правкой любого `<figure>` или figure-кандидата сначала проверь его asset-класс по правилу фигур: `synthetic_figure`, `local_image_asset`, `external_real_image_candidate` или `editorial_visual_idea`. Не превращай cleanup служебного текста в пересказ или перерисовку реальной картинки.

Отдельно проверь и убери из основного фрагмента любые следы служебного мета-текста и «разговора с самим собой»: `Тип`, `Идея`, `Зачем нужен`, `Статус`, `лучше поставить`, `если редактор`, заметки о переносе figure-кандидатов, `repair-note`, `executor-note`, плановые комментарии и формулировки вида «это надо сделать позже» или «кандидат поддерживает абзац». Если такой материал относится к синтетической схеме, которую мы сами создаём для объяснения аргумента, перепиши его как нормальную публичную подпись, таблицу или диаграмму только при условии, что сама схема проходит usefulness/nontriviality gate; иначе оставь идею в companion-файле или удали из основного текста. Если он относится к готовому изображению, локальному asset, source screenshot, source diagram, графику или другой внешней иллюстрации, не пересказывай и не перерисовывай её текстом: сохрани как asset-reference/figure-candidate с публичной подписью и статусом в companion-файле либо вставь через `<figure><img ...></figure>`, если asset уже разрешён и лежит по известному локальному пути. Если это просто рабочая заметка, вынеси её в companion-файл (`*_figure_candidates.md`, `*_open_questions.md`, audit/source register) или удали из основного текста. Служебный мета-текст не должен оставаться внутри `<figure>`, кроме короткой публичной подписи, понятной читателю без знания процесса сборки.

После плана примени его к тексту и сопутствующим файлам. Не переписывай всё заново и не расширяй фрагмент ради объёма; исправляй реальные дефекты, открывая внешние источники только под конкретные утверждения. В отчёте явно отдели план починки от применённых изменений и оставшихся вопросов.


После правки выполни короткий regression audit: проверь, не потерялись ли источники, числа, команды, ограничения, source-specific детали и provenance; не появились ли внутренние ссылки вместо первоисточников; не попал ли в основной текст служебный мета-текст; не были ли готовые изображения или external real image candidates деградированы в текстовые схемы; не сломались ли `<figure>`, `img src`, `alt`, `figcaption` и figure id; не усилилось ли дублирование с соседними фрагментами. В `*_degradation_and_duplication_audit.md`, `*_open_questions.md` или соответствующем отчёте зафиксируй readiness status: `ready_for_next_fragment`, `ready_with_known_debts`, `blocked_by_source_gap`, `blocked_by_asset_pass` или `needs_human_review`, с коротким объяснением оставшихся долгов.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
```

### P12 — repair-pass: остаточная починка

```text
Прочитай сначала:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Прочитай уже исправленный результат заново и не считай предыдущий repair-pass достаточным. Сначала составь короткий план остаточной починки: где после предыдущих правок остались повторы, слабые переходы, сухое перечисление, оглавительный тон, плохая композиционная функция, сомнительные ссылки, неразрешённые asset/figure-решения, языковые или стилевые шероховатости, а также прочие проблемы, которые могли быть пропущены раньше.

В остаточном проходе используй ту же карту дефектов, но не дублируй первый repair-pass механически. Ищи оставшиеся композиционные, источниковые, структурные, визуальные, языковые, мета- и интеграционные дефекты. Для figure-кандидатов задача не «вставить всё inline», а принять корректное asset-решение: оставить в companion-файле, вставить как разрешённый local asset, отложить до asset-pass, отклонить или в редком случае оформить как нетривиальную synthetic figure после usefulness/nontriviality gate.

В конце повтори regression audit и readiness status по `protocols/rules/fragment-defect-analysis-and-repair.md`, особенно если результат будет входом для B/C-фрагментов.

После плана примени его к тексту и сопутствующим файлам. Не начинай новую редакцию с нуля, не добавляй материал без необходимости и не сглаживай сильные различения. В отчёте явно отдели план остаточной починки от применённых изменений и того, что оставлено без изменения.

Обнови:
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- work/theory-writing/fragments/A7_source_usage.md
- work/theory-writing/fragments/A7_story_anchor_map.md
- work/theory-writing/fragments/A7_figure_candidates.md
- work/theory-writing/fragments/A7_open_questions.md
- work/theory-writing/fragments/A7_degradation_and_duplication_audit.md
```
