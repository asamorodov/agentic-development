# Target group plan: C4 — execution runtime → PWG

Статус: рабочий план целевой группы. По этому документу можно собрать исполнительный пакет для переходного моста C4. План не является опубликованным текстом теории.

## 1. Обрабатываемые файлы

```yaml
- path: work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
  status: future
  role: primary
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Основной мост: runtime can execute/resume a step, but does not store full work meaning, authority to continue and cleanup."

- path: work/theory-writing/fragments/C4_source_usage.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Источники, фактически использованные for runtime, workflow engine, platform agent, worktree/sandbox and PWG boundary claims."

- path: work/theory-writing/fragments/C4_story_anchor_map.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Короткие якоря for Sandvault/Homebrew, Pi harness, Stripe Minions platform, Shopify Roast workflow and Quix deterministic wrapper."

- path: work/theory-writing/fragments/C4_figure_candidates.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Кандидаты на иллюстрации for runtime step/replay vs PWG work-item lifecycle."

- path: work/theory-writing/fragments/C4_open_questions.md
  status: future
  role: supporting-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Gaps если A6/A4/B2 are missing or если runtime/tool primary docs need later verification."

- path: work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
  status: future
  role: diagnostic-output
  write_policy: replace-full-file
  result_policy: overlay-path
  notes: "Audit that C4 does not identify durable execution, sandbox, worktree or workflow engine with PWG."
```

Целевая группа не является ``linked-target-edit``: мост один. It must distinguish execution runtime from work graph rather than using a generic PWG source bundle.
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

### Уже написанные / ожидаемые несущие фрагменты

```text
work/theory-writing/fragments/A6_execution_environment_distinctions.md
work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
work/theory-writing/fragments/B2_pwg_contribution.md
```

Если these fragments are absent, read the corresponding story-dossiers/PWG dossier and write the gap to `C4_open_questions.md`.

### Главные досье and story-dossiers

```text
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
work/story_dossiers/QUIX_KLAUS_KODE_STORY_DOSSIER.md
```

### Дополнительные материалы

```text
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
work/reports/PERSISTENT_WORK_GRAPH_DOSSIER_EXPANSION_REPORT.md
work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md
work/theory-source-map-ai-driven-sdlc.md
content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

### Истории-якоря

```text
content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

### Story-dossiers

```text
work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
work/story_dossiers/QUIX_KLAUS_KODE_STORY_DOSSIER.md
```

### Сравнительные отчёты и аудиты

```text
work/reports/PERSISTENT_WORK_GRAPH_DOSSIER_EXPANSION_REPORT.md
work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md
work/reports/STORIES_13_15_LANGUAGE_EDITORIAL_PASS_REPORT.md
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
```

### Внешние источники

Открывать внешние источники нужно только под конкретные утверждения будущего текста; не проходить весь список ради широты.

Явно известные источники: LangGraph persistence/interrupts, Temporal human-in-the-loop / durable execution, Pydantic AI durable execution, DBOS, Restate, Shopify Roast workflow/replay/observability, Git worktree, Codex worktrees, Claude Code worktrees/subagents, Sandvault, Pi, Stripe Minions devbox and validation loop, Quix/Klaus Kode deterministic wrapper, Gas Town / Beads docs for the upper-boundary contrast.

Выводимые источники: inline-ссылки, source registers, source notes, repository/tool names, architecture diagrams, figure candidates and runtime vocabulary from `ARMIN_RONACHER_STORY_DOSSIER.md`, `STRIPE_MINIONS_STORY_DOSSIER.md`, `SHOPIFY_ROAST_STORY_DOSSIER.md`, `QUIX_KLAUS_KODE_STORY_DOSSIER.md`, `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`, `PERSISTENT_WORK_GRAPH_DOSSIER_EXPANSION_REPORT.md`, `SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md` and upstream `A6_source_usage.md`, `A4_source_usage.md`, `B2_source_usage.md` если they exist.

## 3. Очередь рабочих prompt-ов

### P01 — первичный фрагмент

```text
Прочитай сначала:
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md
- work/theory-writing/CORE_NODES_WRITING_PLAN.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
- work/theory-writing/fragments/A6_execution_environment_distinctions.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Создай первый черновик `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md`. Композиционная функция фрагмента: мост от execution runtime к PWG. Runtime может запустить команду, удержать thread, восстановить workflow или изолировать worktree, но он не знает сам по себе, почему эта работа существует, кто её владелец, какие gates должны блокировать следующий шаг и какое evidence нужно для завершения.

Не пиши обзор источников и не пересказывай истории. Строй аргумент как часть общей теории: один ход мысли, несколько точных фактических якорей, ссылки сразу в тексте. Подзаголовки добавляй только там, где они помогают удержать смену смыслового хода; не дроби текст декоративно. Если факт взят через внутреннее досье или план, не ссылайся на досье: найди первоисточник, указанный внутри него, а если источник нельзя уверенно восстановить — не ставь ссылку.

LangGraph/Temporal/DBOS/Restate, Roast, Stripe, Claude/Codex worktrees sources открывать only under concrete claims.

Проверь, что немногие выбранные синтетические фигуры, прошедшие usefulness/nontriviality gate, и уже готовые/разрешённые image assets стоят inline рядом с соответствующим ходом аргумента, а `*_figure_candidates.md` хранит внешний image-candidate registry, варианты, asset-pass notes, rights/status notes и причины отказа/переноса в атлас. Не заменяй настоящие изображения текстовыми схемами.

Запиши:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
```

### P02 — добавление фактуры по заданной оси

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
- work/theory-writing/fragments/A6_execution_environment_distinctions.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Перечитай `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` и усили его фактурой по направлению: добрать material on worktrees, devboxes, workflow runners, replay and durable execution.

Открывай внешние источники только под конкретные утверждения текста. Если добавляешь новый внешний источник, занеси его в `work/theory-writing/fragments/C4_source_usage.md`: источник, почему добавлен, какое утверждение поддерживает, где использован. Ссылки на внутренние досье, планы и отчёты не являются валидными ссылками в основном тексте.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
```

### P03 — добавление фактуры по соседней оси

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
- work/theory-writing/fragments/A6_execution_environment_distinctions.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Снова перечитай `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` и добавь недостающую фактуру по направлению: показать why runtime success still needs work item, gate, evidence and cleanup in PWG.

Не раздувай текст ради полноты. Добавляй только то, что усиливает функцию фрагмента. Если полезный материал найден во внутреннем документе, открой его внешний источник; если первоисточник не восстанавливается, лучше оставить утверждение без ссылки, чем ссылаться на рабочее досье.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
```

### P04 — проверка состояния запуска и состояния работы

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/A6_execution_environment_distinctions.md
- work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Проверь, разведены ли run state и work state. Execution state говорит, что сейчас запущено, где и с какими правами. Work state говорит, зачем это делается, что считается готовым, кто принимает и что делать после обрыва. Если workflow runner смог возобновить выполнение, но не знает, должен ли он продолжать именно эту работу, это runtime recovery без work recovery.

Не повторяй A6 и не превращай фрагмент в каталог runtime-инструментов. Открывай внешние источники только под конкретные утверждения; новые источники заноси в `C4_source_usage.md`.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

### P05 — свободное раскрытие источников

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
- content/stories/14_stripe_minions_enterprise_agentic_platform_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- content/stories/08_mike_mcquaid_maximum_deep_dive_reconstruction_v_2_connected.md
- work/theory-writing/fragments/A6_execution_environment_distinctions.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Сделай один свободный проход по источникам и глубине. Раскрой источники, которые выводятся из текущего текста, inline-ссылок, source usage, figure-кандидатов, названий инструментов, авторов, статей, репозиториев и методологий. Проверь, не остался ли рядом с уже написанным текстом полезный материал, который нужно добавить. Для визуального материала в этом проходе сначала выполняй asset-классификацию: не считай figure-candidate доказательством, что нужно сделать текстовую схему; проверь, не является ли это реальным внешним изображением или уже существующим локальным asset. Отдельно проверь фигуры: выбранные синтетические схемы должны быть редкими и проходить usefulness/nontriviality gate перед inline-вставкой; готовые/разрешённые image assets должны быть вставлены как `<figure><img ...></figure>`; внешние image candidates без asset-pass/rights-check не превращай в текстовые схемы, а оставь в `*_figure_candidates.md` с ясным статусом и причиной.

Обязательно открой все новые внешние источники, которые находишь в этом проходе, до того как использовать их. Каждый новый источник занеси в `work/theory-writing/fragments/C4_source_usage.md`. Не добавляй источники для широты и не превращай текст в каталог фактов.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
```

### P06 — системное выравнивание

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
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

Выравняй `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` как несущий фрагмент общей теории. Проверь, ведёт ли он один продолжающийся смысл, не спорит ли со скелетоном, не пересказывает ли истории и не стал ли он оглавлением будущих глав вместо самостоятельного аргумента.

Сохрани фактуру и ссылки. Убери повторы, слишком локальные рамки и места, где текст выглядит как список тем. Если часть материала лучше оформить как самостоятельный материал или раздел концептуально-технического атласа, отметь это в `work/theory-writing/fragments/C4_open_questions.md` или `work/theory-writing/fragments/C4_degradation_and_duplication_audit.md`, но не удаляй важную мысль без замены и не своди материал атласа к несвязному техническому приложению.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

### P07 — адресное усиление: состояние запуска и состояние работы

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
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

Проведи адресный проход по `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md`: усили границу между состоянием запуска и состоянием работы. Runtime может знать команду, thread, worktree, log, browser, sandbox и workflow. Но он сам по себе не знает, почему работа существует, кто отвечает за продолжение, какой барьер должен остановить следующий шаг и какое свидетельство нужно для принятия изменения. Если текст смешивает runtime traces и PWG-state, разведи их.

Это адресное усиление основной функции фрагмента. Не превращай его в общий редакторский проход и не закрывай им последующую общую редакторскую тройку: после этого шага всё равно будут независимые чтения “оцени задачу → сформулируй проблемы → исправь”.

Перед правкой коротко запиши в `work/theory-writing/fragments/C4_degradation_and_duplication_audit.md`, какой конкретный риск проверен и что изменено. Если существенной проблемы нет, не переписывай текст ради активности: зафиксируй, что целевая проверка пройдена. При любых изменениях визуального слоя сначала применяй asset-classification gate.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

### P08 — адресное усиление: сценарий продолжения и восстановления

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
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

Проведи адресный проход по `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md`: добавь или усили один сквозной сценарий продолжения/восстановления. Агент остановлен, другая сессия продолжает работу, runtime-следов недостаточно, а PWG делает продолжение осмысленным: показывает цель, владельца, блокировки, контрольные условия, уже собранные свидетельства и следующий безопасный шаг. Сценарий должен служить аргументу, а не превращаться в техническую инструкцию.

Это адресное усиление основной функции фрагмента. Не превращай его в общий редакторский проход и не закрывай им последующую общую редакторскую тройку: после этого шага всё равно будут независимые чтения “оцени задачу → сформулируй проблемы → исправь”.

Перед правкой коротко запиши в `work/theory-writing/fragments/C4_degradation_and_duplication_audit.md`, какой конкретный риск проверен и что изменено. Если существенной проблемы нет, не переписывай текст ради активности: зафиксируй, что целевая проверка пройдена. При любых изменениях визуального слоя сначала применяй asset-classification gate.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```


### P09 — общий редакторский проход 1: оценка выполнения задачи и repair

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
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

Оцени текущий текст `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` как готовящийся фрагмент теории: насколько хорошо он выполняет задачу, заданную этим target-group plan, скелетоном и картой документов? Сначала сформулируй проблемы, затем исправь их.

Сохрани общность прохода. Не назначай себе заранее специальную задачу вроде «починить визуальный слой», «починить источники» или «переписать стиль». Смотри на весь фрагмент целиком: его функцию, композицию, границы с соседними узлами, источниковую опору, структуру, публичный слой, фигуры, companion-файлы и оставшиеся долги. Используй карту дефектов из `protocols/rules/fragment-defect-analysis-and-repair.md`, но не превращай её в механический чек-лист.

Перед правкой запиши короткую диагностику: рабочая ценность, публикационная готовность, readiness status, 3–7 главных проблем и что именно будет исправлено сейчас. После диагностики внеси минимально достаточную правку: не переписывай весь фрагмент заново, если дефекты локальны, и не сглаживай фактуру ради красивого текста. Если обнаружены визуальные проблемы, сначала применяй asset-classification gate из `protocols/rules/visual-assets-and-figures.md`.

После правки обнови companion-файлы: source usage, story anchors, figure candidates, open questions и degradation/duplication audit. Заверши коротким regression audit и readiness status.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

### P10 — общий редакторский проход 2: повторная оценка после repair

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
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

Заново оцени уже исправленный `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md`. Не считай первый общий редакторский проход достаточным и не повторяй его механически. Прочитай фрагмент как свежий редактор: насколько он теперь выполняет свою задачу в общей теории? Сначала сформулируй проблемы, затем исправь их.

Сохрани общность прохода. Не ищи только один заранее заданный тип ошибки. Проверь, какие дефекты стали видны после предыдущей правки: перекос функции, обзорность вместо теории, слабые переходы, лишние или недостающие подзаголовки, потеря фактуры, дублирование соседних фрагментов, неудачные figure-решения, служебный мета-текст, плохие формулы, неясные источники или устаревшие companion-записи.

Исправляй только реальные проблемы. Если текст уже выполняет задачу, не переписывай его ради активности: зафиксируй это в audit/open questions и сделай только точечные изменения. После правки обнови companion-файлы, выполни regression audit и запиши readiness status.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

### P11 — общий редакторский проход 3: контрольная оценка без специальной повестки

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
- work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
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

Проведи третий общий редакторский проход по `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md`. Это не языковая и не стилевая полировка. Задача та же: оценить, насколько фрагмент выполняет поставленную задачу, сначала сформулировать оставшиеся проблемы, затем исправить их.

Сохрани проход общим. Не превращай его в отдельный visual-pass, source-pass, style-pass или technical-atlas pass. Проверь, не остались ли после двух предыдущих ремонтов более глубокие дефекты: фрагмент выглядит убедительно, но делает чужую работу; стал гладким, но потерял source-specific детали; сохранил лишний обзорный материал; оставил неочевидный конфликт с A/B/C-соседями; держит фигуру или термин только по инерции; companion-файлы расходятся с основным текстом.

Если существенных проблем нет, не делай косметическое переписывание. Зафиксируй `ready_for_next_fragment` или `ready_with_known_debts` с ясным объяснением. Если проблемы есть, исправь их минимально достаточно, затем обнови companion-файлы и regression audit.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_open_questions.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

### P12 — языковой проход 1

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Приведи `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` к русскому техническому языку по языковому протоколу. Не делай стилевую полировку и не меняй аргумент без необходимости.

Убери английский связующий слой и механические кальки. Сохрани имена источников, инструментов, команд, файлов, URL, `<figure>` и точные технические имена. Проверь, что URL, raw links and anchors не русифицированы и не содержат кириллицы.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

### P13 — языковой проход 2

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Повторно проверь русский текст `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md`. Ищи гибриды, остаточные английские объяснения, плохие кальки, ошибочно переведённые технические термины и места, где русификация стерла различие между близкими понятиями.

Не улучшай стиль ради красоты. Это ещё языковой проход: исправляй язык и техническую точность формулировок.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

### P14 — стилевой проход 1

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Сделай первый стилевой проход по `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md`. Текст должен звучать как человеческий технический аргумент: без summary-интонации, без бюрократических списков, без декоративного пафоса и без размазывания сильных различений.

Не выбрасывай фактуру ради гладкости и не ослабляй конфликтные ограничения. Сохрани ссылки, `<figure>` and source-specific details.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

### P15 — стилевой проход 2

```text
Прочитай сначала:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_source_usage.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/english-source-handling.md
- protocols/rules/source-and-provenance.md
- protocols/rules/content-preservation.md
- protocols/rules/fragment-defect-analysis-and-repair.md
- protocols/rules/visual-assets-and-figures.md

Сделай второй стилевой проход. Проверь, читается ли `work/theory-writing/fragments/C4_execution_runtime_to_pwg.md` как самостоятельный узел теории, а не как досье, оглавление или пересказ материалов. Усиль переходы, если они нужны, но не добавляй новые факты без источников.

Если история используется слишком широко, оставь её как якорь и перенеси ограничение в `work/theory-writing/fragments/C4_story_anchor_map.md`. Для визуального материала не используй правило «кандидат поддерживает аргумент — значит вставить inline» без классификации. Сначала присвой кандидату статус из asset policy: `synthetic_figure`, `local_image_asset`, `external_real_image_candidate` или `editorial_visual_idea`. Inline-вставка допустима только для уже оформленной синтетической схемы, которая прошла usefulness/nontriviality gate, или для разрешённого локального image asset через `<img src="...">`; внешний screenshot/source diagram без asset-pass остаётся в `work/theory-writing/fragments/C4_figure_candidates.md` с причиной и следующим действием. Если кандидат не поддержан текстом, уточни его статус, перенеси в отложенные/отклонённые или сними в `work/theory-writing/fragments/C4_figure_candidates.md`.

Обнови:
- work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
- work/theory-writing/fragments/C4_story_anchor_map.md
- work/theory-writing/fragments/C4_figure_candidates.md
- work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```
