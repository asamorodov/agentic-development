# Target group plan: A1 — единица анализа

Статус: build-time план целевой группы. По этому документу можно собрать исполнительный пакет для написания несущего фрагмента A1. План не является опубликованным текстом теории.

## 1. Обрабатываемые файлы

```yaml
- path: work/theory-writing/fragments/A1_change_not_prompt.md
  status: future
  role: primary
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Основной фрагмент: почему единица анализа — программное изменение, а не prompt."

- path: work/theory-writing/fragments/A1_source_usage.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Какие внутренние и внешние источники реально использованы и для каких утверждений."

- path: work/theory-writing/fragments/A1_story_anchor_map.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Какие истории использованы как фактические якоря и где не надо превращать их в пересказ."

- path: work/theory-writing/fragments/A1_figure_candidates.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Кандидаты на схемы и иллюстрации; ассеты на этом этапе не скачиваются."

- path: work/theory-writing/fragments/A1_open_questions.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Открытые вопросы, source gaps и места, которые нельзя закрывать гладкой прозой."

- path: work/theory-writing/fragments/A1_degradation_and_duplication_audit.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Аудит потерь, повторов, чрезмерного пересказа историй и смешения theory / atlas."
```

Целевая группа не является `linked-target-edit`: основной текст один. Служебные файлы создаются и обновляются как артефакты проходов.

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
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
```

### Языковые, стилевые и источниковые протоколы

```text
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/human-technical-style.md
protocols/rules/english-source-handling.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
protocols/rules/fragment-defect-analysis-and-repair.md
protocols/rules/visual-assets-and-figures.md
```

### Главные внутренние материалы для A1

```text
content/Orientation.md
content/Story_introduction.md
content/Cross_story_synthesis.md
content/Theoretical_synthesis.md
work/old-site-theoretical-synthesis-baseline.md
work/expanded-quarry-theoretical-synthesis.md
work/theory-source-map-ai-driven-sdlc.md
work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md
```

### Досье

```text
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
```

### Истории-якоря

```text
content/stories/01_boris_tane_research_plan_implement_reconstruction_connected.md
content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
content/stories/09_calvin_french_owen_maximum_deep_reconstruction_connected.md
content/stories/10_mark_erikson_maximum_deep_reconstruction_connected.md
content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

### Дополнительные истории для точечных якорей

```text
content/stories/02_peter_steinberger_maximum_deep_dive_reconstruction_connected.md
content/stories/04_arvid_kahl_maximum_deep_dive_reconstruction_connected.md
content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md
content/stories/06_jesse_vincent_agentic_workflow_reconstruction_connected.md
content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
```

### Story-dossiers

```text
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md
work/story_dossiers/QUIX_KLAUS_KODE_STORY_DOSSIER.md
work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
work/story_dossiers/ZIG_NO_AI_POLICY_STORY_DOSSIER.md
```

### Сравнительные отчёты и аудиты

```text
work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
work/reports/PERSISTENT_WORK_GRAPH_DOSSIER_EXPANSION_REPORT.md
work/reports/PERSISTENT_WORK_GRAPH_CYCLE_05_ROLLBACK_NOTICE.md
work/reports/LANGUAGE_TERMINOLOGY_REPAIR_QUEUE.md
work/reports/LANGUAGE_TERMINOLOGY_REPAIR_PASS_REPORT.md
```

### Внешние источники

Явно заданные группы источников: SPDD/Fowler/OpenSPDD, Beads/Gas Town, Nygard/MADR/Fowler ADR, Spec Kit, Kiro, TDAD papers, GSD/Open GSD, BMAD, Boris Tane, Simon Willison, HumanLayer, Calvin French-Owen, Mark Erikson, Matt Pocock, Stripe Minions, Shopify Roast.

Исполнитель обязан открывать не только эти явно видимые ссылки, но и источники, выводимые из перечисленных материалов: inline-ссылки, source registers, названия инструментов, авторов, репозиториев, статей, методологий и figure-кандидатов. Источник используется только если он помогает тезису A1; ссылка ставится сразу в основной текст рядом с утверждением.

## 3. Очередь рабочих prompt-ов

### P01 — первичный черновик

```text
Прочитай сначала:
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- content/Orientation.md
- content/Cross_story_synthesis.md
- work/theory-source-map-ai-driven-sdlc.md
- content/stories/01_boris_tane_research_plan_implement_reconstruction_connected.md
- content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
- content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Открой внешние источники, которые прямо поддерживают исходный тезис A1 и уже присутствуют в прочитанных материалах. Не расширяй поиск ради широты.

Напиши первый черновик work/theory-writing/fragments/A1_change_not_prompt.md. Главная мысль: единица анализа в AI-driven SDLC — программное изменение, а не prompt, агентская сессия или сгенерированный код. Текст должен ввести lifecycle изменения и рабочие субстраты: specification, decision memory, persistent work graph, execution environment, evidence, authority, lifecycle repair.

Истории используй как короткие фактические якоря, не пересказывай их. Внутренние и внешние ссылки ставь сразу в текст. Добавь <figure>-кандидаты там, где они помогают структуре аргумента; ассеты не скачивай.

Запиши:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_source_usage.md
- work/theory-writing/fragments/A1_story_anchor_map.md
- work/theory-writing/fragments/A1_figure_candidates.md
```

### P02 — request surfaces и начало изменения

```text
Прочитай сначала:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_source_usage.md
- content/stories/01_boris_tane_research_plan_implement_reconstruction_connected.md
- content/stories/05_jokull_solberg_maximum_deep_dive_reconstruction_connected.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
- work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Открой внешние источники, которые нужны для request surfaces: blog/source links из перечисленных историй, Stripe Minions, Shopify Roast и связанные источники, если они прямо используются.

Усиль A1 фактурой о том, что работа начинается не только с prompt-а. Покажи request surfaces: issue, Slack/thread, PR feedback, browser observation, workflow run, source shard, migration task, architecture decision. Не делай каталог; эти поверхности нужны только чтобы доказать, что prompt — поздняя и малая единица анализа.

Обнови:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_source_usage.md
- work/theory-writing/fragments/A1_story_anchor_map.md
```

### P03 — сессия и долговечное состояние

```text
Прочитай сначала:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- content/stories/03_simon_willison_agentic_research_reconstruction_connected.md
- content/stories/10_mark_erikson_maximum_deep_reconstruction_connected.md
- content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md
- work/reports/PERSISTENT_WORK_GRAPH_DOSSIER_EXPANSION_REPORT.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Открой внешние источники из PWG, Gas Town, Simon Willison, Mark Erikson and Matt Pocock materials, если они нужны для различения session trace and durable work state.

Усиль A1 различением: трасса сессии полезна, но не равна долговечному рабочему состоянию. Введи это как переход к будущей PWG-части, не раскрывая PWG полностью. Отдельно покажи риск false completion и потери нерешённых напряжений после обрыва сессии.

Обнови:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_source_usage.md
- work/theory-writing/fragments/A1_figure_candidates.md
```

### P04 — детализация через specification, decision memory and evidence

```text
Прочитай сначала:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
- content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Открой внешние источники, которые нужны для SPDD, ADR, Spec Kit and TDAD facts already used or clearly required by the text.

Проверь, хватает ли в A1 связки между намерением, specification, decision memory and evidence. Добавь только те детали, которые помогают главному тезису: изменение проходит через несколько субстратов, и ни один prompt не удерживает их все. Не превращай фрагмент в обзор SPDD, ADR or TDAD.

Обнови:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_source_usage.md
- work/theory-writing/fragments/A1_open_questions.md
```

### P05 — системное выравнивание

```text
Прочитай сначала:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Не ищи новые источники без необходимости. Используй этот проход для композиции.

Перепроверь A1 как несущий фрагмент. Он должен вести одну мысль: prompt слишком мал, потому что программное изменение проходит через lifecycle and substrates. Убери локальные рамки, повторы, мини-пересказы историй и преждевременные глубокие объяснения SPDD/PWG/Gas Town/ADR. Сохрани фактуру и ссылки.

Обнови:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_degradation_and_duplication_audit.md
```

### P06 — repair-pass

```text
Прочитай сначала:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_source_usage.md
- work/theory-writing/fragments/A1_story_anchor_map.md
- work/theory-writing/fragments/A1_figure_candidates.md
- work/theory-writing/fragments/A1_open_questions.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Открой только те внешние источники, которых явно не хватает для уже написанного утверждения. Если источник нужен, но его нельзя быстро проверить, зафиксируй gap вместо гладкого закрытия.

Найди дефекты, видимые после появления текста: слабые переходы, неполные различения, ссылки не у того утверждения, потерянные figure-кандидаты, чрезмерное обобщение, смешение теории и технического атласа. Исправляй точечно, не переписывай всё заново.

Перед применением правки классифицируй найденные проблемы по карте дефектов из `protocols/rules/fragment-defect-analysis-and-repair.md`: композиционные, фактологические, источниковые/provenance, структурные, визуальные, языковые/стилевые, мета- и интеграционные/regression-дефекты. Коротко запиши для каждого существенного дефекта: место, почему это проблема и действие. Отдельно проверь функцию фрагмента против target-group role: фрагмент должен делать именно свою работу в общей теории, а не превращаться в обзор источников, пересказ истории, самостоятельную мини-главу или повтор соседнего узла. Не переписывай текст целиком, если дефект локальный; применяй минимальную достаточную правку.

Перед правкой любого `<figure>` или figure-кандидата сначала проверь его asset-класс по правилу фигур: `synthetic_figure`, `local_image_asset`, `external_real_image_candidate` или `editorial_visual_idea`. Не превращай cleanup служебного текста в пересказ или перерисовку реальной картинки.

Отдельно проверь и убери из основного фрагмента любые следы служебного мета-текста и «разговора с самим собой»: `Тип`, `Идея`, `Зачем нужен`, `Статус`, `лучше поставить`, `если редактор`, заметки о переносе figure-кандидатов, `repair-note`, `executor-note`, плановые комментарии и формулировки вида «это надо сделать позже» или «кандидат поддерживает абзац». Если такой материал относится к синтетической схеме, которую мы сами создаём для объяснения аргумента, перепиши его как нормальную публичную подпись, таблицу или диаграмму только при условии, что сама схема проходит usefulness/nontriviality gate; иначе оставь идею в companion-файле или удали из основного текста. Если он относится к готовому изображению, локальному asset, source screenshot, source diagram, графику или другой внешней иллюстрации, не пересказывай и не перерисовывай её текстом: сохрани как asset-reference/figure-candidate с публичной подписью и статусом в companion-файле либо вставь через `<figure><img ...></figure>`, если asset уже разрешён и лежит по известному локальному пути. Если это просто рабочая заметка, вынеси её в companion-файл (`*_figure_candidates.md`, `*_open_questions.md`, audit/source register) или удали из основного текста. Служебный мета-текст не должен оставаться внутри `<figure>`, кроме короткой публичной подписи, понятной читателю без знания процесса сборки.


После правки выполни короткий regression audit: проверь, не потерялись ли источники, числа, команды, ограничения, source-specific детали и provenance; не появились ли внутренние ссылки вместо первоисточников; не попал ли в основной текст служебный мета-текст; не были ли готовые изображения или external real image candidates деградированы в текстовые схемы; не сломались ли `<figure>`, `img src`, `alt`, `figcaption` и figure id; не усилилось ли дублирование с соседними фрагментами. В `*_degradation_and_duplication_audit.md`, `*_open_questions.md` или соответствующем отчёте зафиксируй readiness status: `ready_for_next_fragment`, `ready_with_known_debts`, `blocked_by_source_gap`, `blocked_by_asset_pass` или `needs_human_review`, с коротким объяснением оставшихся долгов.

Обнови:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_open_questions.md
- work/theory-writing/fragments/A1_degradation_and_duplication_audit.md
```

### P07 — языковой проход

```text
Прочитай сначала:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/reports/LANGUAGE_TERMINOLOGY_REPAIR_QUEUE.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Не открывай новые внешние источники. Это языковой проход.

Приведи A1 к русскому языку по протоколу. Убери английский связующий слой, гибриды и кальки. Сохрани точные имена инструментов, файлов, команд, источников, URL, inline-code, figure-кандидаты и технические различия. Не делай стилевую полировку и не меняй аргумент без необходимости.

Обнови:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_degradation_and_duplication_audit.md
```

### P08 — стилевой проход

```text
Прочитай сначала:
- work/theory-writing/fragments/A1_change_not_prompt.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Не открывай новые внешние источники. Это стилевой проход.

Выровняй A1 как человеческий технический текст: точный, плотный, без бюрократического списка, без декоративного пафоса и без summary-языка. Не выбрасывай фактуру ради гладкости. Следи, чтобы текст был самостоятельным несущим узлом, а не quarry-досье и не пересказом историй.

Обнови:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_degradation_and_duplication_audit.md
```

### P09 — финальная проверка и упаковка

```text
Прочитай сначала:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_source_usage.md
- work/theory-writing/fragments/A1_story_anchor_map.md
- work/theory-writing/fragments/A1_figure_candidates.md
- work/theory-writing/fragments/A1_open_questions.md
- work/theory-writing/fragments/A1_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Не открывай новые источники, кроме случая явной сломанной ссылки в уже написанном тексте.

Проверь результат целевой группы: основной файл существует; ссылки стоят в основном тексте; истории используются как якоря, а не пересказ; figure-кандидаты есть и не требуют скачанных ассетов; технический атлас не подменяет теорию; открытые вопросы вынесены отдельно; нет грубых языковых поломок.

Собери result archive для этой целевой группы. В архив включи:
- work/theory-writing/fragments/A1_change_not_prompt.md
- work/theory-writing/fragments/A1_source_usage.md
- work/theory-writing/fragments/A1_story_anchor_map.md
- work/theory-writing/fragments/A1_figure_candidates.md
- work/theory-writing/fragments/A1_open_questions.md
- work/theory-writing/fragments/A1_degradation_and_duplication_audit.md
- MANIFEST.md
- VERIFY.md
- RESUME.md

Если работа оборвана или часть файлов отсутствует, собери emergency archive со всем доступным состоянием и явно пометь его как interrupted, а не completed.
```
