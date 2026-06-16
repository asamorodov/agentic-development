# Инструкция по применению overlay

Базовый snapshot репозитория: полный `git.zip`, загруженный в текущем чате.

Этот overlay собран относительно последнего пользовательского snapshot, а не относительно предыдущего assistant-generated overlay. Поэтому он кумулятивно включает уже выполненные в этой цепочке изменения: лёгкое правило финального closeout, перестройку структуры главы VI вокруг `Маршруты действия`, расширение MCP-секции как внешнего интерфейса, расширение hooks-секции внешними источниками, правку раздела выбора маршрута и русскую перепись всей главы VI.

Текущий overlay дополнительно добавляет отчёт по внешним источникам и кандидатам на иллюстрации для главы VI. Сам текст главы VI в этом проходе не изменялся.

Применение: распаковать архив в корень репозитория. Архив собран в repository-root форме: внутри сразу лежат пути `protocols/...`, `work/...` и другие файлы без дополнительной папки-обёртки.

## Заменить или добавить файлы

Заменить:

```text
START.md
protocols/rules/chat-github-repo-work-protocol.md
protocols/skills/chat-github-repo-work.md
work/theory-writing/chapters/VI_context_working_state_interface.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

Добавить:

```text
work/reports/CHAT_REPO_LIGHTWEIGHT_CLOSEOUT_PROTOCOL_UPDATE.md
work/theory-writing/reports/CHAPTER_VI_ROUTES_AND_MCP_INTERFACE_PATCH_REPORT.md
work/theory-writing/reports/CHAPTER_VI_HOOKS_SOURCE_EXPANSION_PATCH_REPORT.md
work/theory-writing/reports/CHAPTER_VI_ROUTE_SELECTION_AND_NATURAL_RU_PASS_REPORT.md
work/theory-writing/reports/CHAPTER_VI_EXTERNAL_IMAGE_CANDIDATES_REPORT.md
```

## Что добавлено в текущей правке

1. Собран список внешних источников, уже используемых в главе VI и отчётах по её последним правкам.
2. Прочитаны и проверены источники на наличие пригодных визуальных кандидатов: официальные MCP docs/spec, Claude Code hooks, Codex/Kiro/Gemini hooks, Anthropic Agent Skills, Claude Code Agent Teams, Anthropic multi-agent research, LangChain multi-agent patterns, Cognition anti-multi-agent article, Mark Erikson / Mae Capozzi practice reports, MCP examples and related arXiv papers.
3. Добавлен отчёт `work/theory-writing/reports/CHAPTER_VI_EXTERNAL_IMAGE_CANDIDATES_REPORT.md` с приоритизацией кандидатов и proposed local paths.
4. Текст главы VI не изменялся: это asset/source discovery, а не chapter patch.

## Что сохранено из предыдущих изменений этой цепочки

1. Раздел `Маршруты действия` остаётся вводным разделом, а `Skills`, `MCP-сервер`, `Subagents` и `Где инструкция становится вмешательством` остаются разделами уровня `##`.
2. MCP-секция сохраняет техническую фактуру из официальной спецификации: host/client/server, JSON-RPC, initialization handshake, capability negotiation, `stdio`, Streamable HTTP, `resources`, `prompts`, `tools`, discovery и tool/resource/prompt methods.
3. Hooks-секция сохраняет внешние ссылки на Claude Code, OpenAI Codex, Kiro и Gemini CLI и раскрывает hooks как слой жизненного цикла: добавление контекста, барьер политики, обратная связь после действия, финальный барьер, аудит и наблюдаемость.
4. Сохранена синтетическая фигура `fig-vi-mcp-server-interface`.
5. Сохранено лёгкое правило финального закрытия ChatGPT repo/archive задач без отдельного `STATE_CLOSEOUT.md`.

## Проверки

- Глава VI в текущем проходе не изменялась.
- Отчёт по image candidates добавлен в `work/theory-writing/reports/`.
- `work/discourse.md` обновлён, потому что изменилась рабочая позиция по визуальному pass-кандидату главы VI.
- `work/theory-writing/WORKING_DOCUMENTS_MAP.md` обновлён, потому что добавлен новый отчёт, относящийся к главе VI.
- `work/APPLY_NOTES.md` обновлён под новый кумулятивный overlay.
- Overlay собран в repository-root форме.

- 2026-06-15 — CHAPTER VI FIGURE INTEGRATION: В `work/theory-writing/chapters/VI_context_working_state_interface.md` встроены шесть локальных иллюстраций. Добавлены asset-файлы в `content/assets/theory-images/`: `vi-project-interface-agent.png`, `vi-route-selection.png`, `vi-skills-procedure.png`, `vi-mcp-server-interface.png`, `vi-subagents-orchestration.png`, `vi-hooks-lifecycle.png`.

- 2026-06-15 — VISUAL LAYER BLUEPRINT AND PLANS UPDATE: обновлены `protocols/rules/visual-assets-and-figures.md`, `POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md` и target plans глав VII–XIII. Новый visual pass различает real source images, source-backed redraw, source-backed synthetic figure, synthetic figure, defer/reject; добавлено правило нейтрального prompt wording для генерации изображений.

- 2026-06-15 — CHAPTERS I–V VISUAL DISCOVERY: Добавлен отчёт `work/theory-writing/reports/CHAPTERS_I_V_EXTERNAL_IMAGE_CANDIDATES_REPORT.md`. Основной текст глав I–V не менялся; иллюстрации не вставлялись. Отчёт фиксирует кандидаты, типы visual assets, placement и рекомендации для будущего visual integration pass.

- 2026-06-15: интегрированы иллюстрации в главы I–V; добавлены 7 новых локальных theory image assets и обновлены главы I–V.


- 2026-06-15 — CHAPTERS_I_V_VISUAL_LAYER_COMPLETION: Completed the visual layer for Chapters I–V. Added six new local SVG figures, restored missing Chapter III/IV figure placements, kept existing useful figures, updated manifest and completion report. No figure was removed.

- 2026-06-15: обновлён `work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md` по ретроспективе ручных правок глав III–VI. Добавлены условные плановые модули; reconstruction-by-traces не добавлялся.

- 2026-06-15 — CHAPTERS VII–X TARGET PLAN REGENERATION: обновлены планы глав VII–X по новому blueprint; тексты глав не менялись.

- 2026-06-15 — CHAPTER VII PLAN INDIVIDUALITY UPDATE: усилен target-group plan главы VII; добавлены направляющие про line-to-graph transition, false done, continuation contract, restoration packet, cleanup and bridge to Chapter VIII.

- 2026-06-15 — CHAPTER VIII PLAN INDIVIDUALITY UPDATE: обновлён target-group plan главы VIII. Усилены ось “PWG показывает где, процессный подход показывает как”, wrong-mode continuation, роль как ответственность, двойной мост к IX/X и терминологическая замена “профиля” на более естественные русские формулировки.

- 2026-06-15 — CHAPTER IX TARGET PLAN INDIVIDUALITY UPDATE: обновлён план `CHAPTER_IX_EXECUTION_ENVIRONMENT_RUNTIME_RIGHTS_TARGET_GROUP_PLAN.md`; тексты глав и общий blueprint не менялись.

- 2026-06-15 — CHAPTER X TARGET PLAN INDIVIDUALITY UPDATE: обновлён `work/theory-writing/target-group-plans/CHAPTER_X_GAS_TOWN_BEADS_TARGET_GROUP_PLAN.md`; Gas Town/Beads раскрываются через функции организации многоагентной рабочей среды, без превращения главы в экскурсию по внутренней метафоре.

- 2026-06-15 — CHAPTERS VII–X SIZE / MATERIAL INTAKE UPDATE: Усилены target plans VII–X. Добавлены явные anti-size-cap формулировки и активный source-backed добор слабых мест после черновика, чтобы главы не стабилизировались на условном размере вроде 40К знаков.

- 2026-06-15 — CHAPTERS VII–X NATURAL PLAN REWRITE: переписаны target-group plans VII–X естественным русским языком без изменения текстов глав и общего blueprint.
- 2026-06-15 — SESSION BASELINE DELTA: built cumulative root-shaped delta relative to the initial `git.zip`; includes Chapter VI updates, Chapters I–V visual layer, visual/blueprint protocol changes, Chapter VII–X natural target plans and executor packages. Apply as the next baseline before building later deltas.
- 2026-06-15: Updated `POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md` with an individual chapter tuning section. This is intended to prevent future plans from needing manual individuality passes like VII–X. No existing chapter text or target plan was regenerated.

- 2026-06-15 — Chapters VIII-X result integration: incorporated uploaded result packages for Chapters VIII, IX and X into `work/theory-writing/chapters/`, stored original result archives under `work/theory-writing/results/`, and added `work/theory-writing/reports/CHAPTERS_VIII_X_RESULT_FS_INTEGRATION_AND_EVALUATION_REPORT.md`. Chapter VII was not integrated because no result package was provided in this turn.

- 2026-06-15 — CHAPTER VIII GSD SOURCE DEEPENING: усилен GSD-раздел в `work/theory-writing/chapters/VIII_protected_process_profiles.md`; добавлен отчёт `work/theory-writing/reports/CHAPTER_VIII_GSD_SOURCE_DEEPENING_REPORT.md`.

## CHAPTER VII RESULT FS INTEGRATION — 2026-06-15

Integrated uploaded result package for Chapter VII into the repository file-system state:

```text
work/theory-writing/chapters/VII_persistent_work_graph.md
work/theory-writing/results/CHAPTER_VII_PERSISTENT_WORK_GRAPH_RESULT.zip
```

Evaluation summary: Chapter VII has a strong individual axis around PWG as the durable state of work beyond summary/transcript and local `done`. It holds boundaries with VI, VIII, IX and X well. However the actual chapter text is about 40.7K characters while the package readiness report claims about 57K characters; this mismatch suggests the result may still have compressed source material around the old hidden size zone. The text also needs a natural-Russian pass to remove remaining English connective prose and meta phrasing before canonical acceptance.

Report:

```text
work/theory-writing/reports/CHAPTER_VII_RESULT_FS_INTEGRATION_AND_EVALUATION_REPORT.md
```

## 2026-06-15 — Chapter VIII GSD integration repair overlay

База: состояние после применения `delta_after_session_baseline_2026-06-15.zip`.

Изменены:

```text
work/theory-writing/chapters/VIII_protected_process_profiles.md
work/theory-writing/chapters/VIII_protected_process_profiles_source_register.md
work/theory-writing/chapters/VIII_protected_process_profiles_atlas_usage.md
work/theory-writing/chapters/VIII_protected_process_profiles_dossier_gap_notes.md
work/theory-writing/reports/CHAPTER_VIII_GSD_INTEGRATION_REPAIR_REPORT.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

Смысл правки: устранить дефект предыдущего GSD-добора, где фактура из Атласа и досье была добавлена отдельным слоем поверх раздела. Теперь GSD User Guide, phase loop, Verify/Ship, `.planning/`, specialist agents, `billing/API` и `gsd-pi` встроены в единый аргумент GSD-раздела.


## 2026-06-15 — Chapters VII–X natural-Russian rewrite

Переписаны интегрированные главы VII–X естественным русским языком без изменения фактической основы и структуры. Проход убирает английский связочный текст, полуанглийские объяснительные фразы, самокомментарии и часть тяжёлых кальк; технические термины и имена источников сохранены там, где они являются рабочими именами механизмов.

Изменены:

```text
work/theory-writing/chapters/VII_persistent_work_graph.md
work/theory-writing/chapters/VIII_protected_process_profiles.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights.md
work/theory-writing/chapters/X_gas_town_beads.md
work/theory-writing/reports/CHAPTERS_VII_X_NATURAL_RU_REWRITE_REPORT.md
```

Отчёт: `work/theory-writing/reports/CHAPTERS_VII_X_NATURAL_RU_REWRITE_REPORT.md`.

## 2026-06-15 — Chapters VII–X `сбой` terminology repair

В главах VII–X устранено неудачное повторение слова `сбой` как универсального объяснительного термина. Замены выполнены по смыслу: проблема, ошибка в работе графа, причина падения, неудачная попытка, нарушение рабочего процесса и т. п.

Изменены:

```text
work/theory-writing/chapters/VII_persistent_work_graph.md
work/theory-writing/chapters/VIII_protected_process_profiles.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights.md
work/theory-writing/chapters/X_gas_town_beads.md
work/theory-writing/reports/CHAPTERS_VII_X_FAILURE_TERM_REPAIR_REPORT.md
```

Отчёт: `work/theory-writing/reports/CHAPTERS_VII_X_FAILURE_TERM_REPAIR_REPORT.md`.


## 2026-06-15 — Chapter VII natural-Russian repair

Переписана глава VII более естественным русским языком. Проход не добирал новые источники и не менял структуру главы; задача — убрать массовую неестественность объяснительной прозы, включая формулу `Когда «почти готово» перестаёт быть состоянием работы`.

Изменены:

```text
work/theory-writing/chapters/VII_persistent_work_graph.md
work/theory-writing/chapters/VIII_protected_process_profiles.md
work/theory-writing/chapters/IX_execution_environment_runtime_rights.md
work/theory-writing/reports/CHAPTER_VII_NATURAL_RU_REPAIR_REPORT.md
```

Также проверены основные тексты глав VII–X на `профайл/профиль/profile`; в основных главах таких вхождений больше нет.


## 2026-06-15 — Chapter VIII natural-Russian repair

Переписана глава VIII более естественным русским языком. Проход не добавлял новые источники и не менял структуру главы; задача — убрать массовую искусственность объяснительной прозы, включая формулы `защищённые способы продолжения работы` и `способ действия`.

Изменены:

```text
work/theory-writing/chapters/VIII_protected_process_profiles.md
work/theory-writing/reports/CHAPTER_VIII_NATURAL_RU_REPAIR_REPORT.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

Основные тексты глав VII–X дополнительно проверены: `профайл/профиль/profile` в них не возвращались.


## 2026-06-15 — Chapter IX natural-Russian repair

Переписана глава IX более естественным русским языком. Проход не добавлял новые источники и не менял структуру главы; задача — убрать массовую искусственность объяснительной прозы, включая формулы `работа перестаёт быть только языковой` и `Поручение само по себе ещё не говорит, где агент действует`.

Изменены:

```text
work/theory-writing/chapters/IX_execution_environment_runtime_rights.md
work/theory-writing/reports/CHAPTER_IX_NATURAL_RU_REPAIR_REPORT.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

Ссылки, источники и структура сохранены. Основной текст главы IX проверен на возвращение `профайл/профиль/profile`, `сбой`, `работа перестаёт`, `Поручение само`, `способ действия`; таких вхождений не осталось.

## 2026-06-15 — Chapter X natural-Russian repair

Переписана глава X более естественным русским языком. Проход не добавлял новые источники и не менял структуру главы; задача — убрать массовую искусственность объяснительной прозы, включая формулы `от рабочих узлов к обслуживаемому потоку`, `среда для многих агентских действий`, `обслуживание потока` и `Beads сам по себе ещё не город`.

Изменены:

```text
work/theory-writing/chapters/X_gas_town_beads.md
work/theory-writing/reports/CHAPTER_X_NATURAL_RU_REPAIR_REPORT.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

Ссылки, фигуры, Gas Town/Beads фактура и сквозной пример сохранены. Оставшийся английский в главе относится к именам инструментов, команд, source-side терминам, статусам событий или техническим именам механизмов.

## 2026-06-15 — Chapter VII second natural-Russian repair overlay

Base for this narrow overlay: repository state after `chapter_x_natural_ru_repair_overlay.zip` was applied.

Changed files:

```text
work/theory-writing/chapters/VII_persistent_work_graph.md
work/theory-writing/reports/CHAPTER_VII_NATURAL_RU_SECOND_REPAIR_REPORT.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/CHECKS.json
```

Purpose: second natural-Russian repair of Chapter VII after user feedback that the prior version still sounded unnatural in bulk. The pass removes failed translation traces such as `стенограмма`, rewrites awkward phrases around closing the work, and reduces English connective prose while preserving facts, links, figures and source-specific technical labels.

## 2026-06-15 — Remaining chapter target plans rewrite

Rewrote target-group plans for the remaining unwritten parts of the theoretical synthesis according to the current blueprint:

```text
work/theory-writing/target-group-plans/INTRO_NOT_CODE_GENERATION_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_XI_VERIFICATION_MATERIAL_TESTS_REVIEW_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_XII_AUTHORITY_RESPONSIBILITY_OUTER_CONTOUR_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_XIII_POST_MERGE_MAINTENANCE_LEARNING_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CONCLUSION_MODE_SELECTION_TARGET_GROUP_PLAN.md
work/theory-writing/reports/REMAINING_CHAPTER_TARGET_PLANS_REWRITE_REPORT.md
```

No chapter text was changed. The rewrite preserves concrete input lists but replaces the framing and work directions with current blueprint logic: individual setup, active intake, no hidden size ceiling, visual layer, source discipline, and natural Russian.


## 2026-06-15 — Remaining chapter executor packages

This overlay adds no-stage executor packages for the remaining theory parts. Apply by unpacking into the repository root. It assumes the current working state after the latest natural-Russian repairs and rewritten remaining target plans.

Added package files:

```text
work/theory-writing/packages/INTRO_NOT_CODE_GENERATION_NOSTAGE.zip
work/theory-writing/packages/CHAPTER_XI_VERIFICATION_MATERIAL_TESTS_REVIEW_NOSTAGE.zip
work/theory-writing/packages/CHAPTER_XII_AUTHORITY_RESPONSIBILITY_OUTER_CONTOUR_NOSTAGE.zip
work/theory-writing/packages/CHAPTER_XIII_POST_MERGE_MAINTENANCE_LEARNING_NOSTAGE.zip
work/theory-writing/packages/CONCLUSION_MODE_SELECTION_NOSTAGE.zip
work/theory-writing/packages/remaining_chapter_executor_packages.zip
work/theory-writing/reports/REMAINING_CHAPTER_EXECUTOR_PACKAGES_BUILD_REPORT.md
```


Package mapping manifest: `work/theory-writing/packages/remaining_chapter_executor_packages_manifest.json`.


## 2026-06-15 — Remaining target plans natural-Russian repair

Apply by unpacking the overlay into the repository root. It updates the remaining target plans and rebuilds their executor packages so package payloads match the new plan wording.


## 2026-06-15 — Remaining target plans natural-Russian repair

Apply by unpacking the overlay into the repository root. It updates the remaining target plans and rebuilds their executor packages so package payloads match the new plan wording.


## 2026-06-15 — Natural-Russian repair of remaining plans and packages

Apply by unpacking the overlay into the repository root. It updates the remaining target plans and rebuilds the corresponding executor packages. The chapter texts are unchanged.

Updated files include:

```text
work/theory-writing/target-group-plans/INTRO_NOT_CODE_GENERATION_TARGET_GROUP_PLAN.md
work/theory-writing/packages/INTRO_NOT_CODE_GENERATION_NOSTAGE.zip
work/theory-writing/target-group-plans/CHAPTER_XI_VERIFICATION_MATERIAL_TESTS_REVIEW_TARGET_GROUP_PLAN.md
work/theory-writing/packages/CHAPTER_XI_VERIFICATION_MATERIAL_TESTS_REVIEW_NOSTAGE.zip
work/theory-writing/target-group-plans/CHAPTER_XII_AUTHORITY_RESPONSIBILITY_OUTER_CONTOUR_TARGET_GROUP_PLAN.md
work/theory-writing/packages/CHAPTER_XII_AUTHORITY_RESPONSIBILITY_OUTER_CONTOUR_NOSTAGE.zip
work/theory-writing/target-group-plans/CHAPTER_XIII_POST_MERGE_MAINTENANCE_LEARNING_TARGET_GROUP_PLAN.md
work/theory-writing/packages/CHAPTER_XIII_POST_MERGE_MAINTENANCE_LEARNING_NOSTAGE.zip
work/theory-writing/target-group-plans/CONCLUSION_MODE_SELECTION_TARGET_GROUP_PLAN.md
work/theory-writing/packages/CONCLUSION_MODE_SELECTION_NOSTAGE.zip
work/theory-writing/packages/remaining_chapter_executor_packages.zip
work/theory-writing/packages/remaining_chapter_executor_packages_manifest.json
work/theory-writing/reports/REMAINING_CHAPTER_TARGET_PLANS_NATURAL_RU_REPAIR_REPORT.md
work/theory-writing/reports/REMAINING_CHAPTER_EXECUTOR_PACKAGES_NATURAL_PLAN_REBUILD_REPORT.md
```

## 2026-06-15 — Chapter XI target plan individuality repair

Apply by unpacking the overlay into the repository root. It updates only the Chapter XI target plan and the packages that depend on it. Chapter texts are unchanged.

Updated files include:

```text
work/theory-writing/target-group-plans/CHAPTER_XI_VERIFICATION_MATERIAL_TESTS_REVIEW_TARGET_GROUP_PLAN.md
work/theory-writing/packages/CHAPTER_XI_VERIFICATION_MATERIAL_TESTS_REVIEW_NOSTAGE.zip
work/theory-writing/packages/remaining_chapter_executor_packages.zip
work/theory-writing/packages/remaining_chapter_executor_packages_manifest.json
work/theory-writing/reports/CHAPTER_XI_TARGET_PLAN_INDIVIDUALITY_REPAIR_REPORT.md
```

- 2026-06-16 — AGENTIC AI COVERAGE AUDIT: добавлен отчёт `work/theory-writing/reports/AGENTIC_AI_COVERAGE_AUDIT_2026_06_16.md`. Главы и планы не менялись. Отчёт фиксирует недостающие семейства источников вокруг ReAct/MRKL/Toolformer, LangChain/LangGraph/LangSmith, OpenAI Agents SDK, Google ADK, AutoGen/CrewAI, A2A, observability/evaluation/provenance, security/authorization и coding-agent research. Рабочий вывод: ось software-change lifecycle остаётся правильной, но перед финальной сборкой нужны компактные вставки, чтобы показать место этой теории в общей LLM-agent экосистеме.

## 2026-06-16 — A1 Atlas V2 target plan overlay

Apply by unpacking the overlay into the repository root. It adds the target-group plan and package split meta for `A1. Репозиторий как интерфейс для агента`.

Updated / added files:

```text
work/atlas/target-group-plans/agent_facing_repository_interface_ATLAS_V2_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/plans/agent_facing_repository_interface_ATLAS_V2_ARTICLE_PACKAGE_SPLIT_META.md
work/atlas/plans/reports/agent_facing_repository_interface_A1_TARGET_PLAN_REPORT_2026_06_16.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/APPLY_NOTES.md
work/CHECKS.json
work/COMMIT_MESSAGE.txt
```

No theory chapters, existing Atlas articles, or executor packages were changed.

## 2026-06-16 — protocol update: full dry-run validation for executor packages

Updated the general task-package protocols to require a full dry run of runner chains before releasing long, staged, or reordered executor packages. The rule is generic: every required file for a record must either be bundled initially or produced by an earlier record during the dry run. A record must not require a file that belongs to a future record.

Updated files:

```text
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/TASK_PACKAGE_MANUFACTORY_PROTOCOL.md
work/reports/TASK_PACKAGE_PROTOCOL_DRY_RUN_VALIDATION_UPDATE_2026_06_16.md
work/atlas/packages/agent_execution_stack_ATLAS_V2_ARTICLE.zip
```

The protocol update intentionally avoids article-specific or mini-dossier-specific rules. It only changes the packaging validation gate. The cached A2 package has been replaced with the repaired package version.
