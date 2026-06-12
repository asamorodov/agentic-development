# Target group plan: C5 — theory → концептуально-технический атлас

Статус: рабочий план целевой группы. По этому документу можно собрать исполнительный пакет для переходного моста C5. План не является опубликованным текстом теории и не является самим техническим атласом.

## 1. Обрабатываемые файлы

```yaml
- path: work/theory-writing/fragments/C5_theory_to_technical_atlas.md
  status: future
  role: primary
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Основной мост: теория остаётся поперечным SDLC-синтезом; технический атлас становится концептуально-техническим слоем самостоятельных статей по конкретным концепциям, источниковой механике, ассетам и оговоркам."

- path: work/theory-writing/fragments/C5_source_usage.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Какие досье, карты, аудиты и списки источников использованы для границы между теорией и концептуально-техническим атласом."

- path: work/theory-writing/fragments/C5_story_anchor_map.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Минимальные якоря для границы теория / истории / атлас: обычно Orientation, Story introduction and Cross-story synthesis."

- path: work/theory-writing/fragments/C5_concept_atlas_article_map.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Карта будущих статей концептуально-технического атласа: какие concept-first articles нужны, на какие досье/источники они опираются, что допустимо повторять из теории, какие механические детали, изображения, команды и оговорки им понадобятся."

- path: work/theory-writing/fragments/C5_figure_candidates.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Кандидаты на иллюстрации для теоретических фрагментов, статей концептуально-технического атласа, досье и будущих asset-pass."

- path: work/theory-writing/fragments/C5_open_questions.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Пробелы, если upstream-фрагменты, source registers или реестры атласа отсутствуют."

- path: work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Audit that C5 сохраняет две траектории: чтение от теории как поперечный синтез и чтение от конкретной концепции через статьи атласа; без механического дублирования и без складирования деталей."
```

Целевая группа не является ``linked-target-edit``: мостовой фрагмент один. C5 должен объяснить новую границу: теория остаётся поперечным SDLC-синтезом, а технический атлас становится концептуально-техническим слоем самостоятельных статей по конкретным концепциям. Атлас не сводится к техническим деталям; контролируемые повторы с теорией допустимы, если они нужны для самостоятельного чтения статьи атласа.
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

Для ещё не построенного фрагмента этот repair-слой реализуется не одним поздним проходом после стиля, а 2–3 общими редакторскими проходами сразу после системного выравнивания и до языковых/стилевых проходов. Каждый такой проход сохраняет общность: оценивает, насколько текст выполняет поставленную задачу, сначала формулирует проблемы, затем исправляет их; не получает заранее специальной повестки вроде visual/source/style.

## 2. Файлы для чтения

### Управляющие документы

```text
work/discourse.md
work/approved-ai-sdlc-plan.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/decisions/ADR-0011-concept-first-technical-atlas.md
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

### Expected upstream theory fragments если available

```text
work/theory-writing/fragments/00_spine_map.md
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

Если many fragments are missing, C5 must fall back to skeleton, writing plan, document map and dossiers; record the limitation in `C5_open_questions.md`.

### Optional later-sync input

```text
work/theory-writing/fragments/A10_mode_selection_map.md
```

Если A10 уже существует в момент выполнения C5, используй его как read-only input для semantic back-links и проверки согласования с mode-selection map. Если A10 отсутствует, не блокируй C5: зафиксируй `A10 sync pending` в `C5_open_questions.md` и `C5_degradation_and_duplication_audit.md`.

### Главные methodological dossiers for atlas boundary

```text
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
work/dossiers/GSD_METHOD_DOSSIER.md
work/dossiers/BMAD_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
work/dossiers/ADR_METHOD_DOSSIER.md
```

### Comparative reports and source maps

```text
work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md
work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md
work/reports/PERSISTENT_WORK_GRAPH_DOSSIER_EXPANSION_REPORT.md
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
work/theory-source-map-ai-driven-sdlc.md
```

### Истории and synthesis materials

```text
content/Orientation.md
content/Story_introduction.md
content/Cross_story_synthesis.md
```

Прочитай individual stories only если a neighboring fragment already uses them and the C5 bridge needs a boundary example.

### Story-dossiers

```text
work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
work/story_dossiers/QUIX_KLAUS_KODE_STORY_DOSSIER.md
work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
work/story_dossiers/ZIG_NO_AI_POLICY_STORY_DOSSIER.md
```

Story-dossiers are not primary for C5. Используй them only to explain why a concrete practice or image belongs in a статья концептуально-технического атласа, источниковые заметки, Handbook/Fieldbook or theory fragment.

### Quality audits

```text
work/reports/SPEC_KIT_DOSSIER_QUALITY_AUDIT.md
work/reports/KIRO_SPECS_DOSSIER_QUALITY_AUDIT.md
work/reports/TDAD_COMPARATIVE_DOSSIER_QUALITY_AUDIT.md
work/reports/CONSTITUTIONAL_SDD_DOSSIER_QUALITY_AUDIT.md
work/reports/GSD_OPEN_GSD_DOSSIER_QUALITY_AUDIT.md
work/reports/BMAD_METHOD_DOSSIER_QUALITY_AUDIT.md
work/reports/PERSISTENT_WORK_GRAPH_DOSSIER_EXPANSION_REPORT.md
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
```

### Внешние источники

Открывать внешние источники нужно только под конкретные утверждения будущего текста; не проходить весь список ради широты.

Явно известные источники: внешние корпуса для SPDD/OpenSPDD, Spec Kit, Kiro, Constitutional SDD, TDAD, GSD/Open GSD, BMAD, PWG/Beads, Gas Town/Beads и ADR; URL источников и репозитории, названные в соответствующих досье; документация инструментов, справочники команд, шаблоны, release notes, issue threads и screenshot/figure candidates там, где будущей статье атласа нужны механика, визуальный материал или оговорки с опорой на источники.

Выводимые источники: все inline-ссылки, source registers, таблицы внешних источников, названия методологий, команды, шаблоны, имена файлов, репозитории, названия статей, авторы, кандидаты на фигуры/скриншоты и source-usage outputs из методологических досье, story-dossiers, `SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md`, `WORKING_DOCUMENTS_MAP.md` и upstream `*_source_usage.md`, если они существуют.

### Решение о концептуально-техническом атласе

Действующее решение: технический атлас — это концептуально-технический слой, а не только хранилище технической детализации. Каждый будущий раздел атласа должен читаться самостоятельно для человека, который интересуется конкретной концепцией, а не всей общей теорией. Контролируемое повторение тезисов из теории допустимо, если оно нужно для такого самостоятельного чтения; механический копипаст и несвязное складирование технической фактуры считаются дефектами.

## 3. Очередь рабочих prompt-ов

Эта целевая группа должна содержать **17 рабочих проходов плюс финальную проверку**. Не сокращать очередь при сборке пакета. C5 поздний относительно основного набора A/B/C, но для package-manufactury ему достаточно готовности `00` и `C1–C4` вместе с A/B/B/C read-only inputs и ADR-0011. `A10` полезен как later-sync input для будущей сверки с картой выбора режимов, но не является hard gate для сборки C5-пакета. Если `A10_mode_selection_map.md` ещё отсутствует, зафиксируй `A10 sync pending` в `C5_open_questions.md` и audit, не блокируя работу C5.

### P01 — первичный фрагмент: две траектории чтения

```text
Прочитай сначала:
- work/decisions/ADR-0011-concept-first-technical-atlas.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Создай первый черновик `work/theory-writing/fragments/C5_theory_to_technical_atlas.md`. Композиционная функция фрагмента: объяснить не просто переход «теория → атлас», а две траектории чтения материала.

Первая траектория — theory-first: читатель идёт через поперечный SDLC-синтез и понимает связи specification, ADR, PWG, process, runtime, evidence, authority and lifecycle repair.

Вторая траектория — concept-first: читатель открывает статью атласа про SPDD, PWG, Gas Town / Beads, TDAD, Spec Kit, Kiro, BMAD, GSD, ADR или другую конкретную концепцию и получает самостоятельное, связное, source-grounded объяснение этой концепции, её механики, ограничений, изображений, команд, файлов и связи с общей теорией.

Не формулируй атлас как склад технических деталей и не делай его второй копией всей теории. Контролируемое повторение тезисов из теории допустимо, если оно нужно для самостоятельного понимания конкретной статьи атласа. Механический копипаст и несвязное складирование фактуры считаются дефектами.

Подзаголовки добавляй только там, где они помогают удержать смену смыслового хода. Внешние источники открывай только под конкретные утверждения. Если факт взят через внутреннее досье или план, не ссылайся на досье: найди первоисточник, указанный внутри него, а если источник нельзя уверенно восстановить — не ставь ссылку.

Для визуального материала сначала применяй asset-classification gate. Немногие синтетические схемы допустимы только после usefulness/nontriviality gate; готовые изображения вставляются только как image assets, а не как текстовые суррогаты.

Запиши:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
```

### P02 — модель самостоятельной статьи атласа

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/decisions/ADR-0011-concept-first-technical-atlas.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Перечитай `work/theory-writing/fragments/C5_theory_to_technical_atlas.md` и добавь в него ясную модель самостоятельной статьи концептуально-технического атласа.

Статья атласа должна объяснять: что это за концепция; какую проблему она решает; какой механизм делает её рабочей; какие артефакты, команды, файлы, UI, screenshots, source-specific caveats and limitations важны; где концепция участвует в общей теории; какие у неё границы и типичные ошибки; что читатель должен понять, даже не читая всю теорию.

Создай supporting-output `work/theory-writing/fragments/C5_concept_atlas_article_map.md`. На этом проходе он может быть черновым, но уже должен задать форму будущего article registry: article, назначение, источниковая база, допустимый повтор из теории, технические детали/ассеты, связи обратно к теории.

Не превращай модель статьи в жёсткий шаблон для всех случаев. Это ориентир, который должен помогать писать связные concept-first articles, а не механическая форма.

После описания модели сделай короткий stress-test на разных типах будущих статей, не пиша сами статьи. Минимально проверь SPDD, PWG / Beads, Gas Town and ADR: для каждого случая 5–7 строками покажи, как модель статьи применится к этой концепции, что она должна объяснить самостоятельно и где проходит граница с общей теорией. Если модель не выдерживает хотя бы один из этих случаев, уточни её до обновления article map.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
```

### P03 — карта будущих статей атласа

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/decisions/ADR-0011-concept-first-technical-atlas.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/dossiers/KIRO_SPECS_DOSSIER.md
- work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/GSD_METHOD_DOSSIER.md
- work/dossiers/BMAD_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Разверни `work/theory-writing/fragments/C5_concept_atlas_article_map.md` как карту будущих статей атласа. C5 не должен писать сами статьи атласа, но должен показать, какие concept-first articles нужны и зачем.

Минимально проверь кандидатов: SPDD / OpenSPDD, Spec Kit, Kiro Specs, TDAD, Constitutional SDD, ADR / MADR / Nygard, GSD / Open GSD, BMAD, PWG / Beads, Gas Town, Sandvault, HumanLayer harness, Roast. Добавляй другие статьи только если они действительно нужны из досье/карты документов.

Сначала задай типологию статей атласа, чтобы карта не стала плоским списком равноправных тем. Используй минимум такие tiers:

- `core concept article` — большая самостоятельная статья для центральной концепции или механизма: например SPDD, PWG / Beads, Gas Town.
- `method article` — статья о методике, практической форме или профиле работы: например BMAD, GSD, TDAD, ADR.
- `tool/form article` — статья об инструментальной форме или среде: например Spec Kit, Kiro, Sandvault, HumanLayer harness.
- `source note / case note` — не полноценная статья, а источниковая или кейсовая заметка: например Roast, Stripe minions, Quix or отдельные migration cases, если материала недостаточно для concept article.
- `deferred / not enough material` — кандидат есть, но его пока нельзя честно поднимать до самостоятельной статьи.

Для каждой статьи укажи: article tier; reader question — зачем человек откроет именно эту статью; на какие досье/источники она опирается; article boundary — что статья объясняет сама, а что оставляет соседней статье или общей теории; что может повторять из теории ради самостоятельного понимания; какие команды, файлы, images/assets, external real image candidates, synthetic figure needs, caveats, UI details or source notes вероятны; asset/source readiness; semantic back-links — к каким теоретическим фрагментам она подключается и какой вопрос теории помогает понять.

Отдельно проверь опасные пары на дублирование границ: SPDD / OpenSPDD / Spec Kit / Kiro; PWG / Beads / Gas Town; GSD / BMAD / process profiles; TDAD / evidence / testing; ADR / lifecycle repair / specification. Для каждой пары не нужно писать длинный анализ, но в article map должно быть видно, где проходит граница.

`C5_concept_atlas_article_map.md` не должен становиться первым черновиком атласа. Он фиксирует состав, назначение, границы, reader questions, asset/source readiness and semantic links будущих статей, но не пишет сами статьи.

В основной C5-фрагмент добавь только те выводы из карты, которые нужны самому аргументу. Не превращай C5 в список всех будущих статей.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
```

### P04 — пограничные случаи маршрутизации материала

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Добавь в C5 несколько точных пограничных примеров маршрутизации материала. Нужна не старая граница «смысл в теории, детали в атласе», а более практичная граница между theory fragment, concept-atlas article, source note, story note, Handbook and Fieldbook.

Примеры должны показывать: ADR нужен общей теории как способ памяти решений, но ADR-статья атласа может связно объяснить Nygard/MADR, шаблоны, статусы и инструменты; SPDD нужен теории как lifecycle specification, но SPDD-статья атласа может включать OpenSPDD commands/templates; PWG нужен теории как механизм долговечного состояния работы, но PWG/Beads-статья раскрывает команды, объекты, gates and recovery details; Roast может быть якорем workflow-engine reasoning, но API/code/screenshots должны поддерживать concept article, story note or source note.

Не делай из примеров таблицу ради таблицы. Они должны укреплять границу и выбор маршрута, а не заменять аргумент.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
```

### P05 — проверка пяти перекосов атласа

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_open_questions.md
- work/decisions/ADR-0011-concept-first-technical-atlas.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Проверь пять рисков и исправь C5, если он разрешает любой из них.

1. Сложная мысль выбрасывается из теории в атлас. Теория должна оставлять у себя поперечные концепты, механизм, аргумент и значение для SDLC.
2. Атлас снова сводится к техническому приложению: командам, файлам, screenshots and implementation details без связной концепции.
3. Атлас превращается во вторую теорию: каждая статья заново строит весь общий SDLC-синтез вместо локального объяснения своей концепции.
4. Атлас превращается в набор source dossiers: много фактуры, команд и скриншотов, но нет связной concept article.
5. Атлас превращается в плоский список равноправных статей без tiers, reader questions, границ и приоритетов. Если карта не различает core concept articles, method articles, tool/form articles, source notes and deferred candidates, она не выполняет задачу.

Правь именно композиционную границу, модель атласа и article map. Не добавляй новые источники без необходимости.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_open_questions.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P06 — свободное раскрытие источников

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
- work/dossiers/SPDD_METHOD_DOSSIER.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/dossiers/KIRO_SPECS_DOSSIER.md
- work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md
- work/dossiers/TDAD_COMPARATIVE_DOSSIER.md
- work/dossiers/GSD_METHOD_DOSSIER.md
- work/dossiers/BMAD_METHOD_DOSSIER.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
- work/dossiers/ADR_METHOD_DOSSIER.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Сделай один свободный проход по источникам и глубине. Раскрой источники, которые выводятся из текущего текста, inline-ссылок, source usage, article map, figure-кандидатов, названий инструментов, авторов, статей, репозиториев и методологий. Проверь, не остался ли рядом с уже написанным текстом полезный материал, который нужно добавить.

Для визуального материала сначала выполняй asset-классификацию: не считай figure-candidate доказательством, что нужно сделать текстовую схему; проверь, не является ли это реальным внешним изображением или уже существующим локальным asset. Выбранные синтетические схемы должны быть редкими и проходить usefulness/nontriviality gate. Внешние image candidates без asset-pass/rights-check не превращай в текстовые схемы.

Обязательно открой новые внешние источники до использования. Каждый новый источник занеси в `C5_source_usage.md`. Не добавляй источники ради широты и не превращай текст в каталог фактов.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
```

### P07 — системное выравнивание

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/decisions/ADR-0011-concept-first-technical-atlas.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Выравняй `work/theory-writing/fragments/C5_theory_to_technical_atlas.md` с общей архитектурой теории. Проверь, что C5 не начинает писать сам технический атлас, не пытается выполнить работу будущей или уже готовой A10-карты выбора режимов, не пересказывает C1–C4 и не отменяет самостоятельность concept-first articles.

Сделай переходы к C5 понятными: после A/B/C-фрагментов читателю должно быть ясно, почему нужен второй маршрут чтения через конкретные концепции. Если `A10` уже существует, сверь C5 с картой выбора режимов; если A10 ещё отсутствует, явно оставь `A10 sync pending` в `C5_open_questions.md` / audit, не превращая отсутствие A10 в блокер. При необходимости уточни `C5_concept_atlas_article_map.md`, чтобы он отражал реальную роль атласа, а не только список будущих тем.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P08 — адресный проход 1: самостоятельная ценность atlas article

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/decisions/ADR-0011-concept-first-technical-atlas.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md

Адресно усили C5 по главной новой задаче: каждая будущая статья атласа должна иметь самостоятельную ценность. Читатель, пришедший за SPDD, PWG, Gas Town, BMAD, TDAD, Spec Kit, Kiro или ADR, не должен мысленно собирать концепцию из всех глав теории.

Проверь, что основной C5-фрагмент объясняет это не лозунгом, а рабочей моделью: что именно делает article self-contained, почему controlled repetition допустим и где проходит граница с общей теорией.

Не делай общий редакторский проход; это специальное усиление одной функции перед общей редакторской тройкой.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_open_questions.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P09 — адресный проход 2: контролируемое повторение с теорией

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/decisions/ADR-0011-concept-first-technical-atlas.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Адресно усили правило controlled repetition. C5 должен объяснить, что повтор с теорией допустим, когда нужен для самостоятельного понимания конкретной концепции, но недопустим как механический копипаст или пересборка всего SDLC-синтеза внутри каждой статьи.

Проверь `C5_concept_atlas_article_map.md`: для ключевых articles должно быть понятно, какие тезисы можно повторять из теории и зачем. Если карта не различает полезный повтор и дублирование, исправь.

Не делай общий редакторский repair; это специальное усиление перед общей редакторской тройкой.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P10 — адресный проход 3: двусторонняя навигация theory-first / concept-first

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/decisions/ADR-0011-concept-first-technical-atlas.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md

Адресно усили навигационную функцию C5. Фрагмент должен показывать не только путь из теории в атлас, но и обратный путь: из статьи атласа читатель должен понимать, к каким теоретическим фрагментам, историям, source notes, Handbook or Fieldbook она подключена.

Проверь, что `C5_concept_atlas_article_map.md` содержит не просто навигационные ссылки назад, а semantic back-links: для каждой ключевой статьи должно быть понятно, какой теоретический вопрос она помогает понять и почему ссылка ведёт именно к этому фрагменту. Например, SPDD может ссылаться на A3 как lifecycle specification, на A7 как вопрос свидетельств и на A9 как вопрос обновления спецификационного контекста; PWG / Beads — на A4/B2/C1–C4 как состояние работы, продолжение, evidence and runtime boundary.

Основной C5-фрагмент должен объяснять принцип этой двусторонней навигации без превращения в навигационный справочник.

Не делай общий редакторский repair; это специальное усиление перед общей редакторской тройкой.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_open_questions.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P11 — общий редакторский проход 1: оценка выполнения задачи и repair

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
- work/decisions/ADR-0011-concept-first-technical-atlas.md
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

Оцени текущий текст `work/theory-writing/fragments/C5_theory_to_technical_atlas.md` как готовящийся фрагмент теории: насколько хорошо он выполняет задачу, заданную этим target-group plan, скелетоном и картой документов? Сначала сформулируй проблемы, затем исправь их.

Сохрани общность прохода. Не назначай себе заранее специальную задачу вроде «починить визуальный слой», «починить источники», «починить controlled repetition» или «переписать стиль». Смотри на весь фрагмент целиком: функцию, композицию, границы с соседними узлами, source grounding, article map, структуру, публичный слой, фигуры, companion-файлы и оставшиеся долги.

Перед правкой запиши короткую диагностику: рабочая ценность, публикационная готовность, readiness status, 3–7 главных проблем и что именно будет исправлено сейчас. После диагностики внеси минимально достаточную правку. Если обнаружены визуальные проблемы, сначала применяй asset-classification gate.

После правки обнови companion-файлы. Заверши коротким regression audit и readiness status.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P12 — общий редакторский проход 2: повторная оценка после repair

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
- work/decisions/ADR-0011-concept-first-technical-atlas.md
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

Заново оцени уже исправленный C5. Не считай первый общий редакторский проход достаточным и не повторяй его механически. Прочитай фрагмент как свежий редактор: насколько он теперь выполняет свою задачу? Сначала сформулируй проблемы, затем исправь их.

Сохрани общность прохода. Проверь, какие дефекты стали видны после предыдущей правки: перекос функции, обзорность вместо теории, слабые переходы, слишком жёсткая или слишком рыхлая граница theory/concept-atlas, потеря фактуры, дублирование соседних фрагментов, неудачные figure-решения, служебный мета-текст, плохие формулы, неясные источники или устаревшие companion-записи.

Если текст уже выполняет задачу, не переписывай его ради активности: зафиксируй это в audit/open questions и сделай только точечные изменения. После правки обнови companion-файлы, выполни regression audit и запиши readiness status.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P13 — общий редакторский проход 3: контрольная оценка без специальной повестки

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
- work/decisions/ADR-0011-concept-first-technical-atlas.md
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

Проведи третий общий редакторский проход. Это не языковая и не стилевая полировка. Задача та же: оценить, насколько фрагмент выполняет поставленную задачу, сначала сформулировать оставшиеся проблемы, затем исправить их.

Сохрани проход общим. Проверь, не остались ли после двух предыдущих ремонтов более глубокие дефекты: фрагмент выглядит убедительно, но делает чужую работу; стал гладким, но потерял source-specific details; сохранил лишний обзорный материал; оставил конфликт с A/B/C-соседями; держит фигуру или термин по инерции; article map расходится с основным текстом.

Если существенных проблем нет, не делай косметическое переписывание. Зафиксируй `ready_for_next_fragment` или `ready_with_known_debts` с ясным объяснением. Если проблемы есть, исправь их минимально достаточно, затем обнови companion-файлы и regression audit.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_open_questions.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P14 — языковой проход 1

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Приведи `work/theory-writing/fragments/C5_theory_to_technical_atlas.md` и `work/theory-writing/fragments/C5_concept_atlas_article_map.md` к русскому техническому языку по языковому протоколу. Не делай стилевую полировку и не меняй аргумент без необходимости.

Убери английский связующий слой и механические кальки. Сохрани имена источников, инструментов, команд, файлов, URL, `<figure>` и точные технические имена. Проверь, что URL, raw links and anchors не русифицированы и не содержат кириллицы.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P15 — языковой проход 2

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Повторно проверь русский текст C5 и article map. Ищи гибриды, остаточные английские объяснения, плохие кальки, ошибочно переведённые технические термины и места, где русификация стерла различие между близкими понятиями.

Не улучшай стиль ради красоты. Это ещё языковой проход: исправляй язык и техническую точность формулировок.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P16 — стилевой проход 1

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Сделай первый стилевой проход по C5 и article map. Текст должен звучать как человеческий технический аргумент: без summary-интонации, без бюрократических списков, без декоративного пафоса и без размазывания сильных различений.

Не выбрасывай фактуру ради гладкости и не ослабляй ограничения. Сохрани ссылки, `<figure>` and source-specific details. Не используй неудачные псевдотехнические формулы из bad phrase ledger.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

### P17 — стилевой проход 2

```text
Прочитай сначала:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_source_usage.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Сделай второй стилевой проход. Проверь, читается ли C5 как самостоятельный узел теории, а не как досье, оглавление, план сайта или пересказ материалов. Усиль переходы, если они нужны, но не добавляй новые факты без источников.

Проверь, что article map остаётся рабочей картой будущих concept-first articles, а не превращается в слишком подробный атлас до атласа. Если в карте появились длинные разделы, похожие на черновики статей, сожми их до registry-level fields: tier, reader question, boundary, sources, allowed theory repetition, asset/source readiness and semantic back-links. Для визуального материала не используй правило «кандидат поддерживает аргумент — значит вставить inline» без классификации.

После правки выполни короткий regression audit: проверь, не потерялись ли источники, команды, ограничения, source-specific details and provenance; не появились ли внутренние ссылки вместо первоисточников; не попал ли в основной текст служебный мета-текст; не были ли готовые изображения или external real image candidates деградированы в текстовые схемы; не сломались ли `<figure>`, `img src`, `alt`, `figcaption` and figure id; не усилилось ли дублирование с соседними фрагментами.

Обнови:
- work/theory-writing/fragments/C5_theory_to_technical_atlas.md
- work/theory-writing/fragments/C5_story_anchor_map.md
- work/theory-writing/fragments/C5_concept_atlas_article_map.md
- work/theory-writing/fragments/C5_figure_candidates.md
- work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

## 4. Финальная проверка package-run

Финальная проверка не считается рабочим проходом P01–P17. При сборке self-contained package runner должен добавить отдельный final record, который проверяет наличие всех target outputs, source usage, article map, story anchors, figure candidates, open questions, degradation/duplication audit, визуальную классификацию, отсутствие служебного мета-текста в основном фрагменте, regression audit and readiness status.

Для `C5_concept_atlas_article_map.md` финальный record дополнительно проверяет, что карта содержит tiers, reader questions, article boundaries, asset/source readiness and semantic back-links; что она различает core concept articles, method articles, tool/form articles, source/case notes and deferred candidates; что опасные пары статей не оставлены без boundary; и что карта не превратилась в мини-атлас или черновик самих статей. После финальной проверки runner больше не запускается.
