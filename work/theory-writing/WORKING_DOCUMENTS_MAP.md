
# Post-Atlas active source routing

Статус на 2026-06-13: concept-first Атлас завершён как baseline из 10 статей. Активный скелетон для следующих глав:

```text
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
```

`THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` остаётся историческим baseline и источником сравнения, но новые chapter packages должны стартовать от V5.

Статус после языко-стилевого прохода: активный Skeleton V5 вычитан локально по последним правилам Атласа; структура и источник решений не менялись.

Главная иерархия источников для глав:

```text
00_spine_map / Skeleton V5 / CORE plan — композиция и термины
A/B/C-фрагменты — уже проделанный синтез
Atlas articles — concept-first baseline
Dossiers — gap-check, source restoration, failure modes и visual/source queues
External sources — content discovery там, где внутреннего материала недостаточно, плюс provenance/assets
Stories — адресные практические якоря
```

Сопутствующие post-atlas карты:

```text
work/theory-writing/reports/POST_ATLAS_SOURCE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_DISCOVERY_NEEDS.md
work/theory-writing/reports/POST_ATLAS_HEAVY_CHAPTER_PACKAGE_BLUEPRINT.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_TARGET_PLAN_BLUEPRINT_PROPOSAL.md
work/theory-writing/reports/POST_ATLAS_SKELETON_ANTI_DEGRADATION_AUDIT.md
```

Правило: главы не пишутся напрямую из досье и не пересказывают Атлас. Сначала section contract, затем A/B/C и Атлас, затем dossier gap-check, затем external discovery только там, где этого требуют content gaps.

---


## Post-Atlas global routing layer

Создан repo-level target-group plan:

```text
work/theory-writing/target-group-plans/POST_ATLAS_GLOBAL_CORPUS_ROUTING_TARGET_GROUP_PLAN.md
```

Этот план не self-contained: он рассчитан на запуск в корне развёрнутого репозитория. Его задача — подготовить общие карты для будущих chapter target plans: scope глав, маршрутизацию Атласа, A/B/C-фрагментов, досье, историй, внешнего discovery и visual candidates. Он не пишет главы и не заменяет per-chapter blueprint.


# Карта рабочих документов проекта AI-driven SDLC

Статус: рабочая карта документов для подготовки теоретического раздела, технического атласа, Handbook и Fieldbook.  
Дата: 2026-06-13.  
Основание: текущий репозиторий, `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md`, завершённый concept-first Атлас, A/B/C-фрагменты, методологические досье, story-dossiers, отчёты, протоколы и принятые решения.

## Назначение

Этот документ объясняет, какие рабочие документы существуют в репозитории, как они соотносятся между собой и как именно ими пользоваться при дальнейшей разработке сайта.

Карта не заменяет `project/source-precedence.md` и не меняет правила источников. Она даёт практическую навигацию для writing-pass: что читать прежде всего, что использовать как quarry, что считать управляющим решением, а что не использовать как первичный материал для теории.

## Главное правило использования

```text
Публичные истории дают фактический корпус.
Досье дают source-backed quarry и gap-check после чтения Атласа.
Скелетон V5, `00_spine_map` и CORE plan задают композицию.
ADRs фиксируют решения.
Reports и audits помогают не потерять материал и не повторить старые ошибки.
Automation logs не являются источником теории, если только не анализируется сам процесс автоматизации.
```

## Правило базовой линии и формы рабочих delta/overlay

Все рабочие дельты по этой ветке должны собираться относительно последнего полного архива репозитория, который пользователь загрузил в чат, или относительно состояния после явного сообщения пользователя, что изменения применены/закоммичены. Assistant-generated overlay archives не являются новой базой сами по себе.

Если следующий архив должен заменить предыдущие результаты текущей цепочки, он может быть кумулятивным, но кумулятивность считается от той же пользовательской базовой линии. Нельзя молча строить новую дельту поверх предыдущего assistant-generated overlay и выдавать это за состояние репозитория.

Если дельта намеренно узкая и не включает предыдущие незакоммиченные overlay, это нужно прямо написать в `work/APPLY_NOTES.md` и финальном ответе.

Форма архива такая же важная, как baseline: delta/overlay archive должен быть root-shaped. Внутри zip должны лежать repository-relative paths (`START.md`, `AGENTS.md`, `work/...`, `protocols/...`), а не дополнительная папка-обёртка с именем overlay или задачи.

---

---

# 1. Публичный слой сайта

## 1.1. Orientation and section entry points

Файлы:

```text
content/Orientation.md
content/Story_introduction.md
content/Cross_story_synthesis.md
content/Theoretical_synthesis.md
content/Handbook.md
content/Fieldbook.md
```

Использование:

- `Orientation.md` задаёт пользовательский вход в сайт и границу между историями, теорией и практическими разделами.
- `Story_introduction.md` вводит корпус историй.
- `Cross_story_synthesis.md` используется как один из главных входов для ранних теоретических фрагментов, особенно для Частей I–II и заключения.
- `Theoretical_synthesis.md`, `Handbook.md`, `Fieldbook.md` являются текущими публичными заготовками / placeholder-слоем. Их нельзя считать финальным теоретическим текстом, но надо учитывать при интеграции, чтобы не ломать site structure.

## 1.2. Опубликованные истории

Файлы:

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

Использование:

- Это первый раздел сайта и фактический корпус.
- Теория может ссылаться на истории как на короткие фактические якоря.
- Теория не должна пересказывать истории внутри себя.
- При writing-pass каждый пакет должен иметь `story_anchor_map.md`: какие истории использованы, где и зачем.

Приоритетные маршруты:

- Boris Tane: research / plan / annotations / implementation boundary.
- Peter Steinberger: малый радиус, быстрый conversational mode, CLI, diff and taste.
- Simon Willison: agentic research, transcripts, Showboat, evidence.
- Arvid Kahl: browser/log observation, safety loop, UI reality.
- Jökull Sólberg: PR как managed object, skills, CI, review triage.
- Jesse Vincent: workflow, gates, skills, failure under formal pressure.
- HumanLayer: harness, research-plan-implement, context budget, BAML.
- Mike McQuaid: sandbox, worktrees, maintainer policy.
- Calvin French-Owen: human time, context and verification.
- Mark Erikson: mental model, context, external memory.
- Mae Capozzi: team/platform wrapper and organization.
- Matt Pocock: skills as procedural memory.
- Armin Ronacher: minimal harness, logs, simple code, maintainer boundary.
- Stripe Minions: internal developer platform, devbox, PR review.
- Shopify Roast: workflow engine, replay, structured workflows.

---

# 2. Главные управляющие документы

## 2.1. План, скелетон и текущий writing control

Файлы:

```text
START.md
work/approved-ai-sdlc-plan.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/discourse.md
```

Использование:

- `START.md` является корневым входным файлом для восстановления контекста нового чата или среза репозитория: он указывает, какие документы читать первыми. Он не заменяет `work/discourse.md` и не отменяет протокольное сопровождение после нетривиальной сессии.
- `approved-ai-sdlc-plan.md` задаёт утверждённую общую рамку AI-driven SDLC и текущий scope.
- `THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md` является основной структурой будущей теоретической главы.
- `CORE_NODES_WRITING_PLAN.md` задаёт порядок написания несущих узлов и глав.
- `WORKING_DOCUMENTS_MAP.md` объясняет, какие документы использовать и как.
- `work/discourse.md` хранит смысловую непрерывность текущей ветки работы. Перед крупными writing-pass его нужно читать, но не использовать как первичный источник фактов вместо досье и историй. Если сессия меняет рабочую траекторию, процесс или роль документов, дискурс нужно обновлять в том же overlay.

## 2.2. Решения и ADR

Файлы:

```text
work/approved-decisions.md
work/decisions/ADR-0007-sdlc-artifact-and-framework-coverage.md
work/decisions/ADR-0008-protected-methodology-profiles.md
work/decisions/ADR-0009-skeleton-v4-2-story-boundary-and-technical-atlas.md
work/decisions/ADR-0010-persistent-work-graph-deep-mechanism-anchor.md
work/decisions/ADR-0011-чтение от конкретной концепции-technical-atlas.md
work/decisions/PROPOSED_ADR-0007-sdlc-artifact-and-framework-coverage.md
```

Использование:

- Принятые ADR задают рамки, которые нельзя silently переоткрывать в writing-pass.
- `ADR-0007` важен для coverage SDLC artifacts/frameworks.
- `ADR-0008` защищает глубину методологических профилей.
- `ADR-0009` фиксирует границу: истории / теория / технический атлас.
- `ADR-0010` фиксирует PWG как отдельный глубокий механизм.
- `ADR-0011` уточняет границу theory / atlas: технический атлас теперь концептуально-технический слой самостоятельных концептуально-технических статей, а не узкое техническое приложение.
- `PROPOSED_*` использовать только как исторический след, не как принятое решение.

---

# 3. Активные методологические досье

Файлы:

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

Использование:

- Это главный source-backed quarry для теоретической главы и технического атласа.
- Досье нельзя пересказывать целиком в теории.
- Writing-pass должен переносить из досье только материал, нужный функции конкретной главы.
- При нехватке фактуры не придумывать гладкую теорию, а запускать отдельный source-pass по соответствующему досье.

Роли:

- `SPDD_METHOD_DOSSIER.md`: deep case specification lifecycle.
- `PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md`: deep mechanism work-state lifecycle.
- `GAS_TOWN_METHOD_DOSSIER.md`: deep case organizational-operational lifecycle.
- `ADR_METHOD_DOSSIER.md`: protected decision profile.
- `SPEC_KIT_METHOD_DOSSIER.md`, `KIRO_SPECS_DOSSIER.md`, `TDAD_COMPARATIVE_DOSSIER.md`, `CONSTITUTIONAL_SDD_DOSSIER.md`: specification methodology profiles.
- `GSD_METHOD_DOSSIER.md`, `BMAD_METHOD_DOSSIER.md`: process methodology profiles.

---

# 4. Story-dossiers

Файлы:

```text
work/story_dossiers/ARMIN_RONACHER_STORY_DOSSIER.md
work/story_dossiers/PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md
work/story_dossiers/QUIX_KLAUS_KODE_STORY_DOSSIER.md
work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md
work/story_dossiers/STRIPE_MINIONS_STORY_DOSSIER.md
work/story_dossiers/ZIG_NO_AI_POLICY_STORY_DOSSIER.md
```

Использование:

- Story-dossiers дают фактуру для новых историй и story anchors в теории.
- В теории story-dossiers использовать для точности, но не превращать их в embedded mini-stories.
- Особенно важны для частей IX–XIII: execution environment, workflow engine, platform agent, evidence, governance and lifecycle repair.

Роли:

- `ARMIN_RONACHER_STORY_DOSSIER.md`: minimal harness, logs, tool restraint.
- `STRIPE_MINIONS_STORY_DOSSIER.md`: enterprise platform agent, devbox, PR/human review.
- `SHOPIFY_ROAST_STORY_DOSSIER.md`: executable AI workflow, replay, workflow engine.
- `QUIX_KLAUS_KODE_STORY_DOSSIER.md`: deterministic wrapper around coding agent.
- `PRODUCT_MIGRATION_CLAUDE_CODE_STORY_DOSSIER.md`: migration evidence, business-rule oracle, lifecycle tail.
- `ZIG_NO_AI_POLICY_STORY_DOSSIER.md`: governance boundary, AI-generated contributions, maintainer trust.

---

# 5. Сравнительные отчёты и source maps

## 5.1. Главные сравнительные отчёты

Файлы:

```text
work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md
work/reports/COMPARATIVE_DEEP_CASES_AUDIT.md
work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md
work/theory-source-map-ai-driven-sdlc.md
work/expanded-quarry-theoretical-synthesis.md
```

Использование:

- Использовать прежде всего при написании несущих узлов A3, A5, A10.
- `SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md` помогает не потерять source-to-plan links.
- `expanded-quarry-theoretical-synthesis.md` — quarry, не финальный текст.

## 5.2. Coverage and readiness reports

Файлы:

```text
work/reports/SDLC_ARTIFACT_COVERAGE_AUDIT.md
work/reports/AGENTIC_FRAMEWORKS_COVERAGE_AUDIT.md
work/reports/METHODOLOGY_DOSSIERS_QUALITY_AUDIT.md
work/reports/SELECTED_DOSSIERS_QUALITY_AUDIT.md
work/reports/SELECTED_DOSSIERS_CREATED.md
work/reports/SKELETON_V4_QUALITY_AUDIT.md
work/reports/SKELETON_V4_3_PWG_CONSOLIDATION_REPORT.md
work/reports/SKELETON_V4_3_PWG_MATERIAL_READINESS_SOURCES_UPDATE.md
```

Использование:

- Проверять перед writing-pass, если возникает сомнение, достаточно ли фактуры.
- Не использовать как primary source вместо досье.
- Использовать для anti-gap and anti-degradation checks.

## 5.3. Dossier-specific quality audits

Файлы:

```text
work/reports/BMAD_METHOD_DOSSIER_QUALITY_AUDIT.md
work/reports/CONSTITUTIONAL_SDD_DOSSIER_QUALITY_AUDIT.md
work/reports/GSD_OPEN_GSD_DOSSIER_QUALITY_AUDIT.md
work/reports/KIRO_SPECS_DOSSIER_QUALITY_AUDIT.md
work/reports/SPEC_KIT_DOSSIER_QUALITY_AUDIT.md
work/reports/TDAD_COMPARATIVE_DOSSIER_QUALITY_AUDIT.md
```

Использование:

- Читать перед написанием соответствующих methodology profiles.
- Использовать как список рисков и слабых мест, а не как замену досье.

---

# 6. Досье-проходы и накопленные source artifacts

Папки:

```text
work/dossier-passes/adr-method/
work/dossier-passes/bmad-method/
work/dossier-passes/constitutional-sdd/
work/dossier-passes/gsd-open-gsd/
work/dossier-passes/kiro-specs/
work/dossier-passes/persistent-work-graph/
work/dossier-passes/spec-kit/
work/dossier-passes/tdad-comparative/
```

Использование:

- Это следы source accumulation, source opening, transfer, language repair and deltas.
- Для writing-pass обычный вход — итоговое досье из `work/dossiers/`, а не все pass-файлы.
- Pass-файлы читать при сомнении: откуда взялось утверждение, почему источник rejected, что осталось untransferred, где есть should_stop/no or caveat.
- Для PWG не использовать rejected `cycle_05` как основание теории; ориентироваться на `PERSISTENT_WORK_GRAPH_CYCLE_05_ROLLBACK_NOTICE.md`.

---

# 7. Языковые и терминологические документы

Файлы:

```text
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/terminology-and-translation.md
protocols/rules/conceptual-translation-glossary.md
protocols/rules/human-technical-style.md
work/reports/RUSSIAN_LANGUAGE_NORMALIZATION_RUN_REPORT.md
work/reports/LANGUAGE_TERMINOLOGY_REPAIR_QUEUE.md
work/reports/LANGUAGE_TERMINOLOGY_REPAIR_PASS_REPORT.md
work/reports/CONCEPTUAL_TRANSLATION_RETROFIT_AND_PROTOCOL_LANGUAGE_NOTE.md
work/reports/SPDD_LANGUAGE_SANITY_PASS_REPORT.md
work/reports/STORIES_13_15_LANGUAGE_EDITORIAL_PASS_REPORT.md
```

Использование:

- `russian-language.md` обязателен для языкового прохода.
- `human-technical-style.md` и `language-style-rules.md` использовать только в отдельных языково-стилевых проходах, не смешивать с writing-pass. Протоколы не являются образцом финальной прозы; их командный язык не должен переноситься в главы. Для больших atlas article packages после content/source/visual/concept reinforcement идут два языковых прохода, затем общие repair/editorial проходы, затем `style defect audit`, `selective natural rewrite` и отдельный guarded final style pass. Стилевой протокол должен калибровать вкус, а не работать как исполняемый чек-лист тотального переписывания.
- `LANGUAGE_TERMINOLOGY_REPAIR_QUEUE.md` использовать как словарь анти-калек для досье и историй.
- `conceptual-translation-glossary.md` использовать для терминов, где прямой перевод ломает смысл агентской разработки: `evidence`, `transcript`, `trace`, `acceptance`, `handoff`, `state`. Он не является источником теории; это словарь выбора русской формы и границ употребления. При правке уже написанного текста он применяется ретроспективно к словам вроде `свидетельство`, `наблюдение`, `стенограмма` и `доказательный`.
- Отчёты языковой нормализации не являются источниками теории; они нужны для контроля качества текста.

---

# 8. Протоколы, skills and prompts

## 8.1. Repository and task protocols

Файлы:

```text
protocols/rules/chat-github-repo-work-protocol.md
protocols/rules/chat-codex-transfer-protocol.md
protocols/rules/codex-task-work-protocol.md
protocols/rules/discourse-maintenance-rules.md
protocols/skills/maintain-work-discourse.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
protocols/rules/fragment-defect-analysis-and-repair.md
protocols/rules/visual-assets-and-figures.md
protocols/rules/theory-rebuild-rules.md
protocols/rules/english-source-handling.md
protocols/rules/prompt-construction-rules.md
```

Использование:

- Читать перед созданием repo overlays, task packages and writing prompts.
- `protocols/skills/maintain-work-discourse.md` применять, когда сессия меняет ход работы, уточняет решение, создаёт или переоценивает важные файлы, меняет рамку, обнаруживает конфликт или завершает нетривиальную сессию.
- Не использовать как источники теоретического материала, кроме случаев, где теория прямо обсуждает наши собственные process experiments.

## 8.2. Work protocols and prompts

Файлы:

```text
work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md
work/protocols/SOURCE_ACCUMULATION_DOCUMENT_PROTOCOL.md
work/prompts/METHODOLOGY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
work/prompts/STORY_DOSSIER_SOURCE_ACCUMULATION_PROMPT.md
work/prompts/RUN_METHODOLOGY_DOSSIERS_SOURCE_ACCUMULATION.md
work/prompts/RUN_STORY_DOSSIERS_SOURCE_ACCUMULATION.md
work/prompts/RUSSIAN_LANGUAGE_NORMALIZATION_PROMPT.md
work/prompts/RUN_RUSSIAN_LANGUAGE_NORMALIZATION.md
```

Использование:

- Эти файлы нужны для новых source/language passes.
- Writing-packages могут читать их только если задача — создание нового пакета или запуск source/language process.
- Они не являются content sources для теории.

---

# 9. Automation and logs

Папки и файлы:

```text
work/automation/
work/automation/runs/
work/tools/
work/reports/CODEX_SDK_PROBE_RESULT.md
work/reports/RUN_SDK_SUBAGENTS_TEST_RESULT*.md
work/reports/SOURCE_ACCUMULATION_AUTOMATION_MODULES.md
```

Использование:

- Использовать для инфраструктуры, диагностики и оптимизации процесса.
- Не использовать как источники теоретической главы, кроме специальной темы про собственные пакетные/gated-task experiments.
- Старые SDK logs могут быть очень велики; для writing-pass использовать агрегированные отчёты, а не raw logs.
- При создании нового baseline лучше не тащить automation logs в prompt context без необходимости.

---

# 10. Старые baseline, quarry and historical drafts

Файлы:

```text
work/old-site-theoretical-synthesis-baseline.md
work/anchor-seed-spdd-old-site.md
work/anchor-seed-gas-town-old-site.md
work/legacy-current-theoretical-synthesis-draft.md
work/legacy-current-draft-headings.md
work/legacy-current-headings-after-part-vi.md
work/legacy-part-vi-final.md
work/expanded-quarry-headings.md
work/old-site-headings.md
work/anti-catalog-audit.md
work/anti-degradation-audit.md
```

Использование:

- Использовать как baseline/anti-degradation material.
- Не переносить старую структуру автоматически.
- Особенно важны для SPDD and Gas Town: старые seed-фрагменты нельзя ухудшать при новом письме.

---

# 11. Project-level documents

Файлы:

```text
project/repository-structure.md
project/source-precedence.md
project/decisions.md
project/branching-and-task-model.md
project/codex-transition.md
project/roadmap.md
project/open-questions.md
project/scaffold-audit-2026-06-06.md
work/source-precedence.md
work/open-questions.md
```

Использование:

- Определяют структуру репозитория, порядок источников and project process.
- Читать при repo-pass, task package creation and major writing-stage transition.
- Не использовать как factual material for AI-driven SDLC theory, если речь не о собственном process reflection.

---

# 12. Служебные файлы overlay-pass

Файлы:

```text
work/APPLY_NOTES.md
work/COMMIT_MESSAGE.txt
work/checks.json
work/checks.source-handoff.json
```

Использование:

- Служебный слой последнего overlay.
- Читать при применении или проверке delta.
- Не использовать как theory material.
- При новом overlay обновлять `APPLY_NOTES.md`, `COMMIT_MESSAGE.txt`, `checks.json`.

---

# 13. Материалы, которые нельзя использовать без осторожности

## 13.1. Исторические proposed/old plans

Примеры:

```text
work/decision-*.md
work/plan-changelog-baseline-restore.md
work/next-execution-plan-baseline-restore.md
work/reports/PLAN_PATCH_RECOMMENDATIONS*.md
work/reports/TARGETED_SOURCE_EXPANSION*.md
work/reports/STRUCTURAL_*.md
work/reports/CONSOLIDATED_*.md
```

Использование:

- Исторический контекст принятия решений.
- Не считать текущей инструкцией, если она противоречит `approved-ai-sdlc-plan`, `v4.3-PWG` skeleton or accepted ADRs.

## 13.2. Raw automation artifacts

Примеры:

```text
work/automation/runs/**/logs/*.sdk-result.txt
work/automation/runs/**/prompts/*.prompt.md
work/automation/runs/**/status.json
```

Использование:

- Только диагностика процесса.
- Не включать в обычные writing prompts.
- Не использовать для теории без явной причины.

---

# 14. Как пользоваться картой при пакетном написании

Для каждого несущего фрагмента или главы пакет должен:

1. прочитать скелетон;
2. прочитать этот документ;
3. прочитать relevant dossiers;
4. прочитать relevant stories and story-dossiers;
5. прочитать relevant comparative reports;
6. прочитать already written fragments;
7. записать `source_usage.md`;
8. записать `story_anchor_map.md`;
9. записать `omitted_material.md`;
10. записать `open_questions.md`;
11. записать `degradation_audit.md`.

Если материал недостаточен, пакет не должен закрывать дыру гладкой теоретической прозой. Он должен зафиксировать missing material и рекомендовать отдельный source-pass.

---

# 15. Минимальный стартовый набор для ближайшей работы

Перед написанием первых несущих узлов читать:

```text
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/approved-ai-sdlc-plan.md
work/reports/METHODOLOGY_DEPTH_CONTRACT.md
work/reports/SOURCE_TO_PLAN_MAPPING_AFTER_FULL_REREAD.md
work/theory-source-map-ai-driven-sdlc.md
content/Orientation.md
content/Cross_story_synthesis.md
```

Затем подключать только релевантные досье, истории and story-dossiers for the selected fragment.

---

# 16. Протоколы пакетного написания теории

## 16.1. Протокол создания пакетов-заданий

```text
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
```

Использование:

- Описывает двухфазную подготовку пакетов: планы целевых групп и сборка opaque record chain.
- Используется при создании исполнительных архивов для writing, repair, language, style и linked-target-edit задач.

## 16.2. Протокол очередей промптов для глав и подглав

```text
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
```

Использование:

- Задаёт, как строить очередь prompt-ов для написания несущих фрагментов, подглав и глав.
- Требует первичный черновик, 2–4 прохода добавления фактуры, системное выравнивание, repair-pass, отдельные языковые и стилевые проходы.
- Фиксирует обязательное чтение релевантных внутренних материалов, языковых, стилевых и источниковых протоколов, а также явных и выводимых внешних источников.
- Уточняет работу со ссылками, `<figure>`-кандидатами и связанной правкой нескольких целевых документов.

## 16.3. Шаблон плана целевой группы

```text
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
```

Использование:

- Задаёт форму build-time плана целевой группы: обрабатываемые файлы, файлы для чтения, готовые тексты prompt-ов.
- Требует, чтобы каждый prompt начинался с блока `Прочитай сначала:` и содержал точный список источников для данного прохода.
- Используется при подготовке пакетов для несущих фрагментов, глав, repair-pass-ов, language/style-проходов и связанных правок нескольких документов.

## 16.4. Планы целевых групп для несущих фрагментов

```text
work/theory-writing/target-group-plans/*.md
```

Использование:

- Build-time планы для будущих исполнительных пакетов.
- Не являются опубликованным текстом теории.
- Каждый план задаёт целевые файлы, read-only материалы и готовую очередь prompt-ов для конкретной целевой группы.
- Первый созданный план: `work/theory-writing/target-group-plans/A1_CHANGE_NOT_PROMPT_TARGET_GROUP_PLAN.md`.
- План создания планов несущих узлов теперь тоже хранится здесь: `work/theory-writing/target-group-plans/CORE_NODES_TARGET_GROUP_PLANS_GENERATION_TARGET_GROUP_PLAN.md`.
- Все plan-файлы этой категории заканчиваются на `_TARGET_GROUP_PLAN.md`.


## 16.5. Собранные исполнительные пакеты

```text
work/theory-writing/packages/*.zip
```

Использование:

- Cache собранных task packages, чтобы пакет можно было повторно скачать, проверить или пересобрать без поиска по chat artifacts.
- Если пакет собран из одного target-group plan, имя архива совпадает с именем плана без суффикса `_TARGET_GROUP_PLAN` и с расширением `.zip`.
- Если пакет собран из нескольких планов, имя архива отражает объединённую группу, а manifest должен перечислять входящие target-group plans.
- Текущие writing-пакеты несущих узлов A: `work/theory-writing/packages/A1_CHANGE_NOT_PROMPT.zip`, `work/theory-writing/packages/A2_SPECIFICATION_ADR_CONTRACT.zip`, `work/theory-writing/packages/A3_SPECIFICATION_METHODOLOGIES_SYNTHESIS.zip`, `work/theory-writing/packages/A4_PERSISTENT_WORK_GRAPH_BOUNDARY.zip`, `work/theory-writing/packages/A5_PROCESS_METHODOLOGIES_SYNTHESIS.zip`, `work/theory-writing/packages/A6_EXECUTION_ENVIRONMENT_DISTINCTIONS.zip`, `work/theory-writing/packages/A7_OBSERVATION_VS_EVIDENCE.zip`, `work/theory-writing/packages/A8_AUTHORITY_TO_ACT_VS_COMPLETE.zip`, `work/theory-writing/packages/A9_LIFECYCLE_REPAIR.zip`.
- Текущие writing-пакеты B: `work/theory-writing/packages/B1_SPDD_CONTRIBUTION_AND_LIMITS.zip`, `work/theory-writing/packages/B2_PWG_CONTRIBUTION.zip`, `work/theory-writing/packages/B3_GAS_TOWN_BEYOND_PWG.zip`.
- Отчёт о сборке B-пакетов: `work/theory-writing/reports/B_PACKAGES_MANUFACTORY_REPORT.md`.
- Сборочные пакеты: `work/theory-writing/packages/CORE_NODES_TARGET_GROUP_PLANS_GENERATION.zip`, `work/theory-writing/packages/CORE_NODES_WRITING_PACKAGES_BUILD.zip`.


### 16.6. Протокол пакетной мануфактуры

```text
work/protocols/TASK_PACKAGE_MANUFACTORY_PROTOCOL.md
```

- Используется, когда планы целевых групп уже приняты, а задача состоит в механической сборке исполнительных пакетов.
- Не выбирает источники заново и не правит prompt-очереди.
- Собирает пакеты по одному плану за шаг, кладёт их в `work/theory-writing/packages/` и проверяет smoke-test-ом.
- Текущий сборочный пакет: `work/theory-writing/packages/CORE_NODES_WRITING_PACKAGES_BUILD.zip`.


### 16.7. Написанные фрагменты несущих узлов

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
```

Использование:

- Это рабочие фрагменты будущей теоретической главы, а не финальная публикационная сборка.
- Каждый основной фрагмент сопровождается `*_source_usage.md`, `*_story_anchor_map.md`, `*_figure_candidates.md`, `*_open_questions.md` и `*_degradation_and_duplication_audit.md`.
- После asset/style repair A-фрагменты больше не считаются простым результатом массовой inline-вставки. Визуальный слой должен читаться через `*_figure_candidates.md` и asset catalog: реальные image/source assets сохраняются как assets или asset-candidates, а синтетические фигуры допустимы только после usefulness/nontriviality gate. Текущие количества фигур в основных фрагментах после weak-fragment repair: A1 — 6, A2 — 4, A3 — 5, A4 — 4, A5 — 4, A6 — 6, A7 — 5, A8 — 5, A9 — 4. Подзаголовки добавлены умеренно и остаются рабочей структурой до composition-pass.
- При последующей композиции глав сначала читать уже написанные соседние фрагменты, чтобы не дублировать A3/A4/A6/A7/A8/A9 и не ломать границы между слоем спецификации, состоянием работы, средой исполнения, свидетельствами, полномочиями и восстановлением жизненного цикла.

- A4 после composition/visual/style repair и повторного weak-fragment pass содержит 4 фигуры, очищен от inline `figure-candidate`, служебной подписи к Beads asset, формул про «хвост» и остаточного “ложного завершения”. Lifecycle-цепочка теперь дана по-русски; подробные lifecycle/gate/prime/cleanup схемы перенесены в `A4_figure_candidates.md` как deferred/atlas material. Отчёты: `work/theory-writing/reports/A4_COMPOSITION_VISUAL_STYLE_REPAIR_REPORT.md`, `work/theory-writing/reports/WEAKEST_A2_A4_SECOND_REPAIR_REPORT.md`.
- B1/B2/B3 импортированы из completed result archives 2026-06-11. Это рабочие deep-anchor вклад-фрагменты, не финальная публикационная сборка: каждый сопровождается `*_source_usage.md`, `*_story_anchor_map.md`, `*_figure_candidates.md`, `*_open_questions.md`, `*_degradation_and_duplication_audit.md`.
- Оценка B-фрагментов: `work/theory-writing/reports/B_RESULTS_INTEGRATION_AND_EVALUATION_REPORT.md`. После повторного repair B1 имеет умеренную H2-структуру, снятый структурный blocker и более чистый язык: `prompt` как обычное слово в прозе в основном заменён на `промпт`/`спецификация`, Beads-контраст сокращён, граница с B2 точнее. B2 — самый готовый вход для C1–C4; B3 после style/boundary repair чище держит Gas Town/PWG boundary, но перед публикацией всё ещё нужны freshness check, composition/asset-pass и возможный перенос командного уровня в technical atlas. Детали ремонта: `work/theory-writing/reports/B1_COMPOSITION_REPAIR_REPORT.md`, `work/theory-writing/reports/B1_LANGUAGE_BOUNDARY_REPAIR_REPORT.md`, `work/theory-writing/reports/B3_STYLE_BOUNDARY_REPAIR_REPORT.md`.


### 16.8. Навигация по синтезным фрагментам и готовности B/C

```text
work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
work/theory-writing/fragments/A5_process_methodologies_synthesis.md
work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
work/theory-writing/fragments/B2_pwg_contribution.md
work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
work/theory-writing/fragments/C1_specification_to_pwg.md
work/theory-writing/fragments/C2_pwg_to_process_profiles.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
work/theory-writing/fragments/C5_theory_to_technical_atlas.md
```

Использование:

- Узкий смысл слова “синтез” для уже написанных A-фрагментов: `A3_specification_methodologies_synthesis.md` and `A5_process_methodologies_synthesis.md`. A3 синтезирует specification-methodologies; A5 синтезирует process-methodologies / PWG / Gas Town / Beads boundary.
- Широкий композиционный смысл: `00_spine_map.md`, `A10_mode_selection_map.md`, B1–B3 and C1–C5 тоже являются синтетической зоной, но выполняют другие функции: spine, mode-selection, итоговые вклады deep anchors and мосты между уже сформулированными узлами.
- B1, B2 and B3 writing-пакеты уже были собраны и выполнены. Результаты импортированы как рабочие фрагменты: `B1_spdd_contribution_and_limits.md`, `B2_pwg_contribution.md`, `B3_gas_town_beyond_pwg.md` и companion-файлы.
- `B_RESULTS_INTEGRATION_AND_EVALUATION_REPORT.md` фиксирует оценку: все три B-фрагмента имеют статус `ready_with_known_debts`. B1 прошёл структурный repair и повторный language/boundary repair: больше не блокируется отсутствием подзаголовков, очищен от части переводных формул и точнее отделён от B2. B3 прошёл style/boundary repair: лишний английский клей и неверный asset debt исправлены. B2 и B3 перед публикацией всё ещё требуют freshness/asset/composition-pass.
- C1–C4 теперь можно считать нормальными кандидатами на сборку writing-пакетов: прежний блокер `B2_pwg_contribution.md` снят, потому что B2 существует и формулирует вклад PWG.
- C5 остаётся поздним concept-atlas мостом, но его нормальная сборка требует `00_spine_map.md`, B1–B3 and C1–C4; `A10_mode_selection_map.md` полезен для later-sync, но не является hard package gate. Если A10 отсутствует, C5 фиксирует `A10 sync pending`.
- Последний кумулятивный overlay должен включать A3/A6/A7/A8/A9 fragments with all inline figures; baseline-rule-only overlay был узкой промежуточной ошибкой и не заменяет содержательный cumulative overlay.

- Это навигационное правило не отменяет локальные readiness-заметки внутри target-group plans; наоборот, делает их видимыми на уровне общей карты рабочих документов.

### 16.9. Правила inline-фигур и подзаголовков для следующих несущих фрагментов

```text
work/theory-writing/target-group-plans/00_SPINE_MAP_TARGET_GROUP_PLAN.md
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

Использование:

- В этих target-group plans добавлены явные правила для будущих writing-пакетов: выбранные синтетические фигуры и уже готовые/разрешённые image assets должны входить inline в основной фрагмент рядом с соответствующим аргументом.
- `*_figure_candidates.md` остаётся реестром, местом source/asset/status notes, правовых/качественных статусов и причин отказа/переноса. Он может временно быть единственным местом для внешнего image candidate, если asset-pass, rights-check или локальный путь ещё не сделаны.
- Готовые иллюстрации, локальные assets, source screenshots, source diagrams и графики нельзя переписывать или перерисовывать текстовой схемой по умолчанию. Если asset разрешён, он вставляется как `<figure><img src="...">...</figure>`; если не разрешён, остаётся candidate/status note до отдельного asset-pass.
- В этих же планах добавлено правило умеренных подзаголовков: H2/H3 нужны для реальных смысловых переходов, сравнительных блоков и границ механизма; декоративное дробление перед каждым абзацем, примером или фигурой запрещено.
- Уже написанные A-фрагменты проверены по этому правилу: A1/A2/A3/A6/A7/A8/A9 признаны достаточно структурированными для текущего рабочего слоя; A5 получил дополнительные H2-подзаголовки без переписывания текста и источников; A4 позднее прошёл отдельный composition/visual/style repair с сокращением фигур и очищением языка.
- Это рабочее состояние до будущего composition-pass. Подзаголовки A-фрагментов можно позднее переименовать, слить или превратить в anchors, если финальная глава потребует другой композиции.

### 2026-06-11 inline-figure placement and heading rule repair

- `work/theory-writing/fragments/A3_specification_methodologies_synthesis.md`: repaired figure placement; removed final bulk figure appendix; cleaned self-addressing candidate notes from inline figures.
- `work/theory-writing/fragments/A6_execution_environment_distinctions.md`: repaired figure placement; figures now sit in execution-boundary, tool-surface, workflow-engine, platform-agent and PWG-boundary sections.
- `work/theory-writing/fragments/A7_observation_vs_evidence.md`: repaired figure placement; figures now sit in observation/evidence, promise/oracle, trace, migration and PWG-state sections.
- `work/theory-writing/fragments/A8_authority_to_act_vs_complete.md`: repaired figure placement; figures now sit next to CODEOWNERS/ADR, PR, `/babysit-pr`, sandbox, policy and PWG acceptance sections.
- `work/theory-writing/fragments/A9_lifecycle_repair.md`: after composition/visual/style repair, figures reduced from 7 to 4; the real Fowler/Thoughtworks feedback image is preserved as an image asset with public caption; stale-context, memory/guardrail and migration-oracle remain as nontrivial synthetic figures; router/matrix/checklist-like figures moved back to candidates/atlas material.
- `work/theory-writing/target-group-plans/00_SPINE_MAP_TARGET_GROUP_PLAN.md`, `A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md`, `B1-B3`, `C1-C5`: strengthened future execution rule — real figure candidates must be inline at the point of use, not appended in a terminal figure bucket; add headings only where they clarify real argument boundaries.

### 16.10. Anti-meta repair rule для всех планов фрагментов

```text
work/theory-writing/target-group-plans/00_SPINE_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A1_CHANGE_NOT_PROMPT_TARGET_GROUP_PLAN.md
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

Использование:

- Во всех планах фрагментов первый repair-pass теперь явно требует убрать из основного фрагмента служебный мета-текст и «разговор с самим собой»: `Тип`, `Идея`, `Зачем нужен`, `Статус`, `лучше поставить`, `если редактор`, `repair-note`, `executor-note`, plan/editor notes и другие следы процесса сборки.
- Если такой материал относится к синтетической схеме, которую мы сами создаём для объяснения аргумента, он должен быть переписан как нормальная публичная подпись, таблица или диаграмма. Если он относится к готовому изображению, локальному asset, source screenshot/source diagram, графику или другой внешней иллюстрации, его нельзя пересказывать или перерисовывать текстом: нужно сохранить asset-reference/candidate status либо вставить `<img>` после asset-pass.
- Это правило особенно важно для inline `<figure>`: фигура в основном фрагменте должна быть либо синтетической схемой, либо нормальной публичной подписью/обёрткой к реальному asset, но не набором внутренних статусов и инструкций executor-у.
- Теперь это жёсткое правило планов: настоящий локальный image/source screenshot/source diagram нельзя заменять текстовой схемой без отдельного решения о правах, качестве и назначении.


### 2026-06-11 figure asset preservation rule repair

- Переписаны правила фигур во всех fragment target-group plans (`00`, `A1`–`A10`, `B1`–`B3`, `C1`–`C5`) и в `work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md`.
- Убрана двусмысленность, будто каждый visual candidate обязан стать текстовой схемой. Теперь планы различают синтетические схемы, готовые/локальные image assets, external source screenshots/diagrams и редакторские идеи будущей визуализации.
- Inline-placement остаётся обязательным для выбранных синтетических схем и уже разрешённых/готовых assets, но не требует вставлять все внешние candidates без asset-pass и не разрешает ухудшать готовые иллюстрации текстовым пересказом.
- Первый repair-pass во всех fragment plans теперь формулирует anti-meta правило с тем же различением: служебная заметка о синтетической схеме превращается в публичную схему/таблицу, а заметка о готовом изображении превращается в asset-reference/status note or `<img>` после проверки, но не в текстовый суррогат картинки.


## Figure asset catalog / recovery

- `work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md` — рабочее различение local assets, external real candidates and synthetic figures.
- `work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md` — индекс локальных изображений из `content/assets/**`.
- `work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md` — очередь реальных внешних иллюстраций/скриншотов/таблиц из досье, которые ещё не локализованы.
- `work/theory-writing/reports/A_FRAGMENTS_ASSET_RECOVERY_PASS.md` — отчёт о восстановлении локальных source assets в A-фрагментах.

Правило: готовые локальные или внешние изображения не переписываются в текстовые схемы по умолчанию; synthetic figure допустима только когда это действительно авторская схема/таблица, а не замена настоящей картинки.


### 2026-06-11 asset-classification gate in all fragment plans

После asset-recovery pass пользователь уточнил, что сами планы должны предотвращать повторение ошибки с иллюстрациями. Исправлен не только общий комментарий про `<figure>`, но и рабочие prompt-инструкции внутри target-group plans.

Изменение:

- во всех fragment target-group plans (`00`, `A1`–`A10`, `B1`–`B3`, `C1`–`C5`) правило фигур переписано как обязательный asset-classification gate до inline-вставки;
- введены четыре статуса: `synthetic_figure`, `local_image_asset`, `external_real_image_candidate`, `editorial_visual_idea`;
- инструкция вида «если figure-кандидат поддерживает аргумент — вставь inline» заменена на правило: сначала классифицировать, затем inline допускается только для synthetic figure или разрешённого local image asset;
- внешний screenshot/source diagram без asset-pass, rights-check, download/localization and quality-check остаётся в `*_figure_candidates.md` и asset catalog, а не превращается в текстовый суррогат;
- во все prompt-блоки с правкой/переносом фактуры добавлен `protocols/rules/visual-assets-and-figures.md`, чтобы это правило не потерялось при сборке writing-пакетов;
- `work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md`, `CORE_NODES_TARGET_GROUP_PLANS_GENERATION_TARGET_GROUP_PLAN.md`, `CORE_NODES_WRITING_PACKAGES_BUILD_TARGET_GROUP_PLAN.md` and `START.md` теперь требуют сохранять это различение в будущих планах и executor prompts.

Практическое правило для следующих чатов: `*_figure_candidates.md` — это реестр возможностей и статусов, а не команда вставить всё в основной текст. Готовая картинка сохраняется как картинка или как внешний asset-candidate до отдельного asset-pass; synthetic figure допустима только как авторская схема, а не как деградация исходного изображения.

### 2026-06-11 — Synthetic figure usefulness gate

Дополнено правило визуальных ассетов: собственные синтетические схемы допустимы не как обычный способ «добавить figure», а только после usefulness/nontriviality gate. Схема должна прояснять нетривиальную связь, процесс, boundary, lifecycle-переход или сравнительную структуру, которую трудно удержать прозой. Банализация соседнего абзаца в таблицу, декоративная картинка или компенсация несделанного asset-pass теперь считаются деградацией визуального слоя. Правило внесено в `protocols/rules/visual-assets-and-figures.md`, `START.md`, `work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md` и все target-group plans.


### 2026-06-11 — Fragment defect analysis and repair guardrails

Добавлен `protocols/rules/fragment-defect-analysis-and-repair.md` и усилены все target-group plans. Repair-pass теперь должен начинаться с диагностики функции фрагмента и карты дефектов: композиционный, фактологический, источниковый/provenance, структурный, визуальный, языковой/стилевой, мета- и интеграционный/regression. Опасная формулировка про «figure-кандидаты, не вставленные inline» заменена на правило корректного asset-решения. Каждый repair-pass должен завершаться regression audit и readiness status (`ready_for_next_fragment`, `ready_with_known_debts`, `blocked_by_source_gap`, `blocked_by_asset_pass`, `needs_human_review`).

### 2026-06-11 — A3 visual/style repair and anti-metaphor rule

Обновлены:

```text
protocols/rules/human-technical-style.md
protocols/rules/fragment-defect-analysis-and-repair.md
work/theory-writing/fragments/A3_specification_methodologies_synthesis.md
work/theory-writing/fragments/A3_figure_candidates.md
work/theory-writing/fragments/A3_open_questions.md
work/theory-writing/fragments/A3_degradation_and_duplication_audit.md
work/theory-writing/fragments/A3_source_usage.md
work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
work/theory-writing/reports/A3_VISUAL_STYLE_REPAIR_REPORT.md
```

Использование:

- В стилевых правилах усилен запрет на нечеловеческие псевдотехнические словосочетания. Антипримеры: «хвост сопровождения» и «ложный авторитет». В публичном тексте использовать прямые формулировки: «последующая поддержка артефакта», «порядок обновления артефакта», «границы доверия», «артефакт выглядит убедительнее, чем заслуживает», «пределы доказательной силы».
- A3 после repair больше не является визуально перегруженным фрагментом с 15 inline-фигурами. В основном тексте оставлены 5 фигур: `fig-a3-specification-functions`, `fig-a3-spdd-closed-loop`, `fig-a3-spec-kit-plan-gate`, `fig-a3-tdad-two-meanings`, `fig-a3-artifact-trust-boundaries`.
- `fig-a3-drift-taxonomy` сохранён как локальный source asset candidate для будущего B1/SPDD-focused section и не должен возвращаться в A3 без отдельного решения.
- `A3_figure_candidates.md` теперь является статусным companion-файлом: он фиксирует, какие фигуры оставлены inline, какие отложены, какие объединены или отвергнуты для основного A3.
- A3 имеет статус `ready_with_known_debts`: его можно использовать как вход для B/C-работы, но перед публикацией нужны link/freshness check и возможное сжатие процедурных деталей в technical atlas.
- Поскольку B1-пакет содержит A3 как read-only вход, `work/theory-writing/packages/B1_SPDD_CONTRIBUTION_AND_LIMITS.zip` пересобран после A3 repair. B2/B3 сохранены без смыслового изменения.

### 2026-06-11 — A5 visual/composition repair

- `work/theory-writing/fragments/A5_process_methodologies_synthesis.md` — отремонтирован: inline-фигур стало 4 вместо 7, служебные подписи убраны, ослаблено чтение A5 как линейной шкалы процессов, фрагмент заново собран вокруг разных рабочих разрывов.
- `work/theory-writing/fragments/A5_figure_candidates.md` — обновлён: текущий inline-набор — `fig-a5-gsd-bmad-pwg-questions`, `fig-a5-gsd-bmad-light-state`, `fig-a5-method-pwg-organization-stack`, `fig-a5-process-imitation-boundary`; удалённые/отложенные фигуры записаны явно.
- `work/theory-writing/fragments/A5_degradation_and_duplication_audit.md` — дополнен regression audit и readiness после ремонта A5.
- `work/theory-writing/fragments/A5_open_questions.md`, `work/theory-writing/fragments/A5_source_usage.md`, `work/theory-writing/fragments/A5_story_anchor_map.md` — синхронизированы с новой границей A5.
- `work/theory-writing/reports/A5_VISUAL_COMPOSITION_REPAIR_REPORT.md` — отчёт по этому repair-pass.

Примечание по B-пакетам: после ремонта A5 все три B-пакета пересобраны ради консистентности встроенных карт и read-only support files, хотя полный текст A5 не был напрямую встроен в их payload.

### 2026-06-11 — B3 style/boundary repair

Обновлены:

```text
work/theory-writing/fragments/B3_gas_town_beyond_pwg.md
work/theory-writing/fragments/B3_source_usage.md
work/theory-writing/fragments/B3_story_anchor_map.md
work/theory-writing/fragments/B3_figure_candidates.md
work/theory-writing/fragments/B3_open_questions.md
work/theory-writing/fragments/B3_degradation_and_duplication_audit.md
work/theory-writing/reports/B3_STYLE_BOUNDARY_REPAIR_REPORT.md
work/theory-writing/reports/B_RESULTS_INTEGRATION_AND_EVALUATION_REPORT.md
```

Использование:

- B3 остаётся working deep-anchor фрагментом со статусом `ready_with_known_debts`.
- Смысловая функция сохранена: Gas Town показывает организационно-операционный слой сверх PWG, а не переопределяет PWG.
- Языковой repair снял лишний английский клей (`gates/evidence/handoff/recovery` как обычные слова) и кальки вроде `контрольная плоскость` / `рабочий субстрат`; имена команд, ролей, статусов и проектных primitives сохранены.
- `B3_figure_candidates.md` больше не считает локальные Gas Town assets отсутствующими: `gastown-architecture.svg`, `gastown-basic-workflow.svg`, `gastown-mayor-hub.webp` и `beads-task-graph-memory.svg` классифицированы как `local_image_asset`, но не вставлены автоматически из-за композиционных причин.
- Перед публикацией B3 требует freshness check по Gas Town/Beads, composition/asset-pass по возможному повтору `gastown-architecture.svg` с A5 и technical atlas для командного уровня Gas Town.

### 2026-06-11 — B1 language/boundary repair

Обновлены:

```text
work/theory-writing/fragments/B1_spdd_contribution_and_limits.md
work/theory-writing/fragments/B1_source_usage.md
work/theory-writing/fragments/B1_open_questions.md
work/theory-writing/fragments/B1_degradation_and_duplication_audit.md
work/theory-writing/reports/B1_LANGUAGE_BOUNDARY_REPAIR_REPORT.md
work/theory-writing/reports/B1_COMPOSITION_REPAIR_REPORT.md
work/theory-writing/reports/B_RESULTS_INTEGRATION_AND_EVALUATION_REPORT.md
```

Использование:

- B1 остаётся `ready_with_known_debts`, но после повторного repair лучше годится как вход для C-мостов.
- Повторный repair не менял источниковую базу и не добавлял новые визуальные материалы; он исправил язык и границу с B2.
- В основном тексте `prompt` как обычное объяснительное слово в основном заменён на `промпт` или `спецификация`; source-specific имена команд и терминов сохранены.
- Beads-контраст сокращён до пограничного примера: B1 показывает предел SPDD, но не начинает выполнять работу B2/PWG.
- Перед публикацией остаются поздние долги: финальная терминологическая проверка `промпт`/`prompt`/`REASONS Canvas`, возможный SPDD asset-pass и composition check при сборке всей теории.

### 2026-06-11 — A2 contract/ADR repair

Обновлены:

```text
work/theory-writing/fragments/A2_specification_adr_contract.md
work/theory-writing/fragments/A2_figure_candidates.md
work/theory-writing/fragments/A2_open_questions.md
work/theory-writing/fragments/A2_degradation_and_duplication_audit.md
work/theory-writing/fragments/A2_source_usage.md
work/theory-writing/fragments/A2_story_anchor_map.md
work/theory-writing/reports/A2_CONTRACT_ADR_REPAIR_REPORT.md
```

Использование:

- A2 теперь содержит 4 inline `synthetic_figure` вместо прежних 8, с публичными captions и без служебных notes.
- Основная функция A2 сохранена: спецификация, проверочный контракт/оракул и ADR не смешиваются, а контролируют разные сбои агентского изменения.
- `A2_figure_candidates.md` теперь является реестром visual decisions: снятые inline-схемы не потеряны, но не перегружают основной фрагмент; `fig-a2-operational-projection-card` снята с inline и отложена для technical atlas / fieldbook.
- Статус A2: `ready_with_known_debts`. Прежний терминологический долг “контракт/оракул” снят в основном тексте; остаются поздние долги по глоссарию и possible technical atlas для detailed ADR projection/reconstructed ADR lifecycle.

### A6 composition / visual / style repair

- `work/theory-writing/fragments/A6_execution_environment_distinctions.md` прошёл отдельный composition / visual / style repair после оценки пользователем. Основная функция фрагмента сохранена: различить границу исполнения, инструментальную поверхность, движок рабочего процесса, платформенный агент и границу с Persistent Work Graph.
- Inline-фигуры сокращены с 18 до 6: 2 real local image assets and 4 nontrivial synthetic figures. Подробные worktree/sandbox/Roast/Quix/Stripe схемы перенесены в `A6_figure_candidates.md` как deferred/technical-atlas/merged decisions.
- Новый отчёт: `work/theory-writing/reports/A6_COMPOSITION_VISUAL_STYLE_REPAIR_REPORT.md`.
- Статус A6: `ready_with_known_debts`; годится как рабочий вход для C4, но при финальной сборке главы нужно решить, оставлять ли оба real assets в основном тексте или переносить один в technical atlas/story layer.


### A7 composition / visual / style repair

- `work/theory-writing/fragments/A7_observation_vs_evidence.md` прошёл отдельный repair после пользовательской оценки. Основная функция сохранена: различить наблюдение как сигнал для следующего хода агента и свидетельство как материал для человеческого принятия, отклонения или остановки изменения.
- Inline-фигуры сокращены с 13 до 5: 3 нетривиальные synthetic figures and 2 real local image assets. Подробные TDAD/ADR/Roast/Stripe/migration/status схемы перенесены в `A7_figure_candidates.md` как merged/deferred decisions.
- Оставленные inline-figures: `fig-a7-observation-to-evidence-chain`, `fig-a7-evidence-type-by-promise`, `fig-a7-evidence-chain-pwg`, `fig-a7-browser-observation-evidence`, `fig-a7-showboat-rodney-replay`.
- `content/assets/theory-images/openai-codex-citations-evidence.webp` не потерян: он сохранён в asset catalog / figure candidates как local asset candidate для technical atlas / Codex evidence surface.
- Новый отчёт: `work/theory-writing/reports/A7_COMPOSITION_VISUAL_STYLE_REPAIR_REPORT.md`.
- Статус A7: `ready_with_known_debts`; пригоден как рабочий вход для C3, но перед публикацией нужны link/freshness check, решение по термину `replay` и возможное сокращение одного real asset.

### A8 composition / visual / style repair

Обновлены:

```text
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
work/theory-writing/fragments/A8_figure_candidates.md
work/theory-writing/fragments/A8_open_questions.md
work/theory-writing/fragments/A8_degradation_and_duplication_audit.md
work/theory-writing/fragments/A8_source_usage.md
work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
work/theory-writing/reports/A8_COMPOSITION_VISUAL_STYLE_REPAIR_REPORT.md
```

Использование:

- A8 теперь содержит 5 inline-фигур вместо прежних 11 и лучше выполняет функцию governance-узла о различии между разрешением на действие и правом признать изменение принятым.
- `fig-a8-local-sandbox-action-boundary` остаётся настоящим local image asset через `<img>`; подпись публичная, без recovery-служебности.
- Detailed governance figures (CODEOWNERS, ADR adoption, `/babysit-pr`, Homebrew, Zig, anti-pattern table) сохранены в `A8_figure_candidates.md` как material для technical atlas / прикладного governance-слоя, но не перегружают основной A8.
- Статус A8: `ready_with_known_debts`. Оставшиеся долги — финальное решение по англоязычным model states и стыковка с A7/B2 при сборке главы.


## 2026-06-11 — A9 lifecycle repair visual/style status

- `work/theory-writing/fragments/A9_lifecycle_repair.md` прошёл composition / visual / style repair после пользовательской оценки.
- Основная функция сохранена: показать, что `merge` не завершает изменение, если будущая работа получает устаревшие specification/ADR/rules/skills/hooks/work graph/release evidence/workspace state.
- Inline-фигуры сокращены с 7 до 4: один реальный локальный Fowler/Thoughtworks asset и три нетривиальные synthetic figures.
- `fig-a9-artifact-freshness-matrix`, `fig-a9-feedback-signal-router`, `fig-a9-repair-target-selected-by-signal` перенесены из основного текста в `A9_figure_candidates.md` как deferred/merged/sidebar/technical-atlas material.
- Служебная подпись к image asset очищена: в основном тексте больше нет “восстановленная source-иллюстрация” и “локальный файл”.
- Новый отчёт: `work/theory-writing/reports/A9_COMPOSITION_VISUAL_STYLE_REPAIR_REPORT.md`.
- Статус A9: `ready_with_known_debts`; перед публикацией нужны финальный terminology pass и решение, что из ADR/release visual candidates уходит в technical atlas.


### 2026-06-11 — B2 language / boundary repair

Обновлены:

```text
work/theory-writing/fragments/B2_pwg_contribution.md
work/theory-writing/fragments/B2_source_usage.md
work/theory-writing/fragments/B2_story_anchor_map.md
work/theory-writing/fragments/B2_figure_candidates.md
work/theory-writing/fragments/B2_open_questions.md
work/theory-writing/fragments/B2_degradation_and_duplication_audit.md
work/theory-writing/reports/B2_LANGUAGE_BOUNDARY_REPAIR_REPORT.md
work/theory-writing/reports/B_RESULTS_INTEGRATION_AND_EVALUATION_REPORT.md
```

Использование:

- B2 сохраняет функцию deep-mechanism фрагмента: PWG даёт общей теории долговечное состояние работы, а не implementation sketch и не обзор task trackers.
- Основной repair был языково-пограничным: убраны `рабочий субстрат`, `ложное завершение`, `gate-условия` как обычная связка и формулы с “хвостом”.
- Точное `bd gate` оставлено только как команда/source term; в теоретической речи используются `контрольные условия` и `контрольный барьер`.
- Единственная inline-figure `fig-b2-pwg-contribution-matrix` остаётся собственной synthetic figure; внешняя Anthropic-диаграмма остаётся `external_real_image_candidate`, не вставлена без asset-pass.
- Статус B2: `ready_with_known_debts`; годится как вход для C1–C4, но C3/C4 должны раскрывать протокол свидетельств и границу среды исполнения подробнее.


### 2026-06-11 — weakest-fragment second repair: A2 and A4

Обновлены:

```text
work/theory-writing/fragments/A2_specification_adr_contract.md
work/theory-writing/fragments/A2_figure_candidates.md
work/theory-writing/fragments/A2_open_questions.md
work/theory-writing/fragments/A2_degradation_and_duplication_audit.md
work/theory-writing/fragments/A4_persistent_work_graph_boundary.md
work/theory-writing/fragments/A4_open_questions.md
work/theory-writing/fragments/A4_degradation_and_duplication_audit.md
work/theory-writing/reports/A2_CONTRACT_ADR_REPAIR_REPORT.md
work/theory-writing/reports/A4_COMPOSITION_VISUAL_STYLE_REPAIR_REPORT.md
work/theory-writing/reports/WEAKEST_A2_A4_SECOND_REPAIR_REPORT.md
```

Использование:

- A2 и A4 выбраны по repair-отчётам как два фрагмента с самой низкой явной публикационной готовностью после предыдущих ремонтов (~7.4/10).
- A2: `контракт/оракул` больше не используется в основном тексте как неразобранная связка; проверочный контракт и оракул разведены по функции, а `fig-a2-operational-projection-card` снята с inline как technical-atlas / fieldbook material.
- A4: снят остаточный lifecycle/status blocker; “Ложное завершение” заменено на “преждевременное закрытие”, lifecycle-цепочка переведена в русскую прозу, `gates` оставлены только как точный Beads term при объяснении контрольных барьеров.
- Оба фрагмента остаются `ready_with_known_debts`, но их долги теперь поздние: glossary / technical atlas / final composition, а не blocker основного текста.


### 2026-06-11 — future fragment plans: general editorial passes before language/style

Обновлены правила и планы будущих фрагментов, чтобы дефекты, обнаруженные в A/B repair-серии, ловились внутри writing-пакетов, а не отдельными ручными проходами.

Обновлены правила:

```text
protocols/rules/fragment-defect-analysis-and-repair.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
START.md
```

Обновлены target-group plans ещё не построенных фрагментов:

```text
work/theory-writing/target-group-plans/00_SPINE_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C1_SPECIFICATION_TO_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C3_PWG_TO_EVIDENCE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
work/theory-writing/reports/FUTURE_FRAGMENT_EDITORIAL_PASS_PLAN_UPDATE_REPORT.md
```

Использование:

- Для ещё не построенных writing-фрагментов после системного выравнивания и до языковых/стилевых проходов теперь стоят три общих редакторских прохода.
- Эти проходы сохраняют общность: каждый оценивает, насколько текст выполняет поставленную задачу, сначала формулирует проблемы, затем исправляет их; проходы не получают заранее специальной темы вроде visual/source/style.
- Старые поздние prompt-разделы `repair-pass: содержательная починка` / `repair-pass: остаточная починка` сняты из очередей 00/A10/C1–C5 и заменены на общую редакторскую тройку до языковых/стилевых проходов.
- Планы уже построенных A1–A9 и B1–B3 не менялись под новую очередь; их результаты уже существуют и чинятся отдельными repair overlays.


### 2026-06-11 — концептуально-технический атлас decision

Принято и зафиксировано решение: technical atlas / технический атлас больше не трактуется как узкое приложение для технических деталей. Он становится **концептуально-технический атлас**: самостоятельным слоем статей с опорой на источники по конкретным концепциям, методологиям и инструментальным формам.

Обновлены связанные документы:

```text
START.md
protocols/rules/theory-rebuild-rules.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/approved-ai-sdlc-plan.md
work/approved-decisions.md
work/decisions/ADR-0009-skeleton-v4-2-story-boundary-and-technical-atlas.md
work/decisions/ADR-0010-persistent-work-graph-deep-mechanism-anchor.md
work/decisions/ADR-0011-чтение от конкретной концепции-technical-atlas.md
work/theory-writing/CORE_NODES_WRITING_PLAN.md
work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CORE_NODES_TARGET_GROUP_PLANS_GENERATION_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CORE_NODES_WRITING_PACKAGES_BUILD_TARGET_GROUP_PLAN.md
work/theory-writing/reports/CONCEPT_FIRST_ATLAS_DECISION_UPDATE_REPORT.md
```

Использование:

- Теория остаётся поперечным AI-driven SDLC синтезом: она объясняет связи между specification-layer, decision memory, PWG, process profiles, execution runtime, evidence, authority and lifecycle repair.
- Атлас даёт путь чтения от конкретной концепции: читатель может открыть SPDD, PWG, Gas Town / Beads, TDAD, Spec Kit, Kiro, BMAD, GSD, ADR или соседнюю концепцию и получить цельное самостоятельное объяснение на основе досье.
- Контролируемое повторение теоретических тезисов в статья атласа допустимо, если оно нужно для самостоятельного понимания конкретной концепции.
- Нельзя возвращаться к прежней формуле «атлас только хранит техническую фактуру». Также нельзя превращать атлас в механическую копию всей теории или в склад команд, скриншотов и источниковых заметок без связного объяснения.
- C5 должен теперь объяснять две траектории чтения: чтение от теории и чтение от конкретной концепции, а не жёсткое разделение «смысл здесь, детали там».

### 2026-06-11 — future fragment plans: target-specific reinforcement passes before general editorials

После обсуждения целей ещё не построенных фрагментов добавлена прослойка адресных проходов усиления основной функции перед общей редакторской тройкой. Это не отменяет и не сужает общие редакторские проходы: специальные проходы дотягивают заранее известный риск конкретного фрагмента, а затем 2–3 общих прохода заново оценивают весь текст без специальной повестки.

Обновлены target-group plans:

```text
work/theory-writing/target-group-plans/00_SPINE_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C1_SPECIFICATION_TO_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C3_PWG_TO_EVIDENCE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
```

`C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md` намеренно не изменён этим проходом: C5 будет обсуждаться отдельно после решения о concept-first atlas.

Подробности: `work/theory-writing/reports/FUTURE_TARGET_REINFORCEMENT_PASS_UPDATE_REPORT.md`.


### 2026-06-11 — packages for ready future fragments

Обновлены target-group plans перед пакетной мануфактурой:

```text
work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C1_SPECIFICATION_TO_PWG_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C2_PWG_TO_PROCESS_PROFILES_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C3_PWG_TO_EVIDENCE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/C4_EXECUTION_RUNTIME_TO_PWG_TARGET_GROUP_PLAN.md
```

Правка: companion-файлы в адресных и редакторских проходах приведены к тем именам, которые заданы в секции `Обрабатываемые файлы`: `A10_source_usage.md`, `C1_source_usage.md`, `C2_source_usage.md` и т.д. Это предотвращает остановку runner-а из-за ожидания несуществующих длинных companion aliases.

Собраны новые packages:

```text
work/theory-writing/packages/00_SPINE_MAP.zip
work/theory-writing/packages/C1_SPECIFICATION_TO_PWG.zip
work/theory-writing/packages/C2_PWG_TO_PROCESS_PROFILES.zip
work/theory-writing/packages/C3_PWG_TO_EVIDENCE.zip
work/theory-writing/packages/C4_EXECUTION_RUNTIME_TO_PWG.zip
```

Использование:

- `00_SPINE_MAP` можно запускать сейчас: он не ждёт ещё не написанных фрагментов и работает как терминологический контракт.
- `C1–C4` можно запускать сейчас, потому что B2 уже построен и отремонтирован, а нужные A-фрагменты существуют.
- `A10_MODE_SELECTION_MAP` не запускать: ранний package был собран преждевременно и исключён из current cumulative overlay; нормальная сборка A10 должна идти после результатов C1–C4.
- `C5_THEORY_TO_TECHNICAL_ATLAS` собирать после `00` and `C1–C4`; A10 is optional later-sync, not a hard gate.

Отчёт: `work/theory-writing/reports/FUTURE_READY_PACKAGES_MANUFACTORY_REPORT.md`.


### 2026-06-11 — C5 concept-first atlas plan, 17 passes

Updated documents:

```text
work/theory-writing/target-group-plans/C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md
work/theory-writing/fragments/C5_concept_atlas_article_map.md  # future supporting-output
work/theory-writing/reports/C5_CONCEPT_ATLAS_PLAN_17_PASS_UPDATE_REPORT.md
work/decisions/ADR-0011-concept-first-technical-atlas.md
```

C5 now uses 17 working passes plus final package verification. The plan adds a concept-atlas article model, future article map, five-risk atlas check, and three target-reinforcement passes before the three general editorial passes. C5 package manufacturing requires `00` and `C1–C4`; `A10` is optional later-sync for semantic alignment with the mode-selection map, not a hard gate. Previously generated premature A10 package remains superseded; the new A10 package has since been rebuilt after C1–C4.

### 2026-06-11 — C5 concept atlas article map refinement

Уточнён `C5_THEORY_TO_TECHNICAL_ATLAS_TARGET_GROUP_PLAN.md` без увеличения очереди: сохраняются 17 рабочих проходов плюс финальная проверка, но P02/P03/P05/P10/P17 усилены вокруг качества `C5_concept_atlas_article_map.md`.

Новые обязательные элементы карты будущих статей атласа:

- article tiers: `core concept article`, `method article`, `tool/form article`, `source note / case note`, `deferred / not enough material`;
- `reader question` for each article;
- `article boundary`, including checks for dangerous overlap pairs such as SPDD/OpenSPDD/Spec Kit/Kiro, PWG/Beads/Gas Town, GSD/BMAD/process profiles, TDAD/evidence/testing, ADR/lifecycle repair/specification;
- asset/source readiness: local assets, external real image candidates, synthetic figure needs and asset-pass requirements;
- semantic back-links to theory fragments: not just navigation, but the theoretical question each article helps explain.

`C5_concept_atlas_article_map.md` must stay a registry-level map, not a miniature atlas or draft of the atlas articles themselves. Report: `work/theory-writing/reports/C5_CONCEPT_ATLAS_ARTICLE_MAP_REFINEMENT_REPORT.md`.



### 2026-06-11 — A10 mode-selection plan refinement

Уточнён `work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md`. A10 закреплён как поздний узел после `C1`–`C4`, а не как пакет, который можно запускать параллельно с C-мостами.

Ключевые изменения:

- dependency gate: если C1–C4 отсутствуют, A10 не пишется и не пакетируется;
- очередь A10 теперь содержит 17 рабочих проходов плюс отдельную финальную проверку;
- добавлены target outputs `A10_mode_selection_matrix.md` and `A10_decision_stress_tests.md`;
- A10 должен выбирать минимально достаточный режим работы, а не строить maturity model or summary A1–A9;
- добавлены адресные проходы по критериям выбора, переходам/деэскалации, сочетаниям режимов and scenario stress-test;
- после общей редакторской тройки добавлен public decision-map / visual-artifact pass.

Отчёт: `work/theory-writing/reports/A10_MODE_SELECTION_PLAN_REFINEMENT_REPORT.md`.

### 2026-06-11 — integrated 00 and C1–C4 results

Imported result fragments:

```text
work/theory-writing/fragments/00_spine_map.md
work/theory-writing/fragments/00_spine_map_source_usage.md
work/theory-writing/fragments/00_spine_map_story_anchor_map.md
work/theory-writing/fragments/00_spine_map_figure_candidates.md
work/theory-writing/fragments/00_spine_map_open_questions.md
work/theory-writing/fragments/00_spine_map_degradation_and_duplication_audit.md
work/theory-writing/fragments/C1_specification_to_pwg.md
work/theory-writing/fragments/C1_source_usage.md
work/theory-writing/fragments/C1_story_anchor_map.md
work/theory-writing/fragments/C1_figure_candidates.md
work/theory-writing/fragments/C1_open_questions.md
work/theory-writing/fragments/C1_degradation_and_duplication_audit.md
work/theory-writing/fragments/C2_pwg_to_process_profiles.md
work/theory-writing/fragments/C2_source_usage.md
work/theory-writing/fragments/C2_story_anchor_map.md
work/theory-writing/fragments/C2_figure_candidates.md
work/theory-writing/fragments/C2_open_questions.md
work/theory-writing/fragments/C2_degradation_and_duplication_audit.md
work/theory-writing/fragments/C3_pwg_to_evidence.md
work/theory-writing/fragments/C3_source_usage.md
work/theory-writing/fragments/C3_story_anchor_map.md
work/theory-writing/fragments/C3_figure_candidates.md
work/theory-writing/fragments/C3_open_questions.md
work/theory-writing/fragments/C3_degradation_and_duplication_audit.md
work/theory-writing/fragments/C4_execution_runtime_to_pwg.md
work/theory-writing/fragments/C4_source_usage.md
work/theory-writing/fragments/C4_story_anchor_map.md
work/theory-writing/fragments/C4_figure_candidates.md
work/theory-writing/fragments/C4_open_questions.md
work/theory-writing/fragments/C4_degradation_and_duplication_audit.md
```

Result-archive root service files are preserved under:

```text
work/theory-writing/reports/c-results-import/
```

Evaluation and repair report:

```text
work/theory-writing/reports/C_AND_00_RESULTS_INTEGRATION_EVALUATION_REPAIR_REPORT.md
```

Post-import status:

- `00`, `C1`, `C2`, `C3`, `C4`: `ready_with_known_debts`.
- Main repairs were language/public-layer repairs, not full rewrites: removed weak formulas such as `артефакт поставки`, `субстрат`, `театр процесса`, `ложное завершение`, and machine-like labels in C3/C4 figures.
- `C1–C4` can now be used as read-only inputs for a rebuilt A10 package.
- Previously generated `A10_MODE_SELECTION_MAP.zip` remains premature/superseded because it was built before C1–C4 existed.
- `C5` remains later than C1–C4, but it may be packaged before A10 is completed; record `A10 sync pending` if needed.

### 2026-06-12 — A10 package built; C5 blocker corrected

New package:

```text
work/theory-writing/packages/A10_MODE_SELECTION_MAP.zip
```

This package supersedes the earlier premature A10 package. It was rebuilt after importing `00` and `C1`–`C4`, so the C-bridge fragments are now valid read-only inputs for the 17-pass A10 queue. The package contains 17 working prompt records plus a final packaging record and passed unzip/runner smoke tests.

Correction: C5 is package-ready after `00` and `C1`–`C4`; `A10_mode_selection_map.md` is useful for later synchronization but no longer blocks package manufactury. `work/theory-writing/packages/C5_THEORY_TO_TECHNICAL_ATLAS.zip` has been built from the corrected 17-pass plan; if A10 is absent during execution, C5 must record `A10 sync pending`.

Report:

```text
work/theory-writing/reports/A10_PACKAGE_MANUFACTORY_AND_C5_BLOCKER_REPORT.md
```

### 2026-06-12 — atlas article package blueprint

Добавлен отдельный документ:

```text
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
```

Роль: blueprint для будущих target-group plans больших concept-first статей технического атласа. Он фиксирует, что статьи атласа не должны строиться по короткой очереди обычных A/B/C-фрагментов: текущая базовая форма — 26 рабочих проходов плюс финальная проверка, без внутренних ограничений объёма, с пятью source-depth pass-ами, двумя свободными проходами добора материала, visual asset passes, concept reinforcement, двумя языковыми проходами, тремя общими редакторскими проходами, public/article structure / entry-sequence pass, companion sync, `style defect audit`, `selective natural rewrite` и guarded final human technical style pass.

Ключевые решения:

- источник должен разворачиваться в основной текст, а не заменяться конспектом или ledger-отчётностью;
- внешние источники разрешены, особенно для поиска реальных изображений, screenshots, diagrams and source-specific details;
- локальные релевантные assets вставляются в статью как `<img>` даже если тяжёлые файлы не включены в package context;
- внешние реальные изображения ставятся inline как candidates и выносятся в нижний раздел `Внешние изображения для asset-pass` / external image queue;
- синтетические схемы редки и допустимы только при нетривиальной объяснительной пользе;
- C5 полезен для sync article map / tiers / boundaries / semantic back-links, но не является hard gate для blueprint или первых конкретных atlas article plans.

Связанный отчёт: `work/theory-writing/reports/ATLAS_ARTICLE_PACKAGE_BLUEPRINT_REPORT.md`.

### 2026-06-12 — atlas article target-plan manufactury plan

Добавлен отдельный документ:

```text
work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md
```

Роль: план будущего repo-bound meta-package, который создаёт target-group plans для статей концептуально-технического атласа. Важное различение: этот meta-package не пишет сами статьи и не добирает материал для них; он создаёт и улучшает планы будущих article-writing packages. Он запускается в уже развёрнутом репозитории и не требует входных архивов: все досье, фрагменты, asset catalogs and protocols берутся из файловой системы.

Текущий known dossier-backed set фиксируется в самом плане: SPDD / OpenSPDD, Spec Kit, Kiro Specs, Constitutional SDD, TDAD, ADR, GSD / Open GSD, BMAD, Persistent Work Graph / Beads, Gas Town. Новые atlas article topics нельзя создавать из внешнего поиска без отдельного пользовательского решения; если найдено досье вне списка, оно фиксируется как `unplanned_dossier`, а не автоматически превращается в статью.

Цикл для каждой статьи: S01 создаёт initial target-group plan; S02 выполняет свободный редакторский repair плана; S03 усиливает reader question, основную мысль and article boundaries; S04 проверяет встроенные требования будущего article-writing package and сразу исправляет найденные дефекты; S05 ставит readiness stamp. После всех статей идут cross-plan consistency repair and readiness/boundary matrices.

Связанный отчёт: `work/theory-writing/reports/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN_REPORT.md`.

### 2026-06-12 — Atlas article target-plan manufactury package

Built package:

```text
work/theory-writing/packages/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY.zip
```

Source plan:

```text
work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md
```

Report:

```text
work/theory-writing/reports/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PACKAGE_REPORT.md
```

The package runs inside a deployed repository and creates target-group plans for the known dossier-backed atlas article set. It should not be treated as an article-writing package.

### 2026-06-12 — refined atlas article target-plan manufactury plan

Updated:

```text
work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md
work/theory-writing/packages/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY.zip
work/theory-writing/reports/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_REFINEMENT_REPORT.md
```

The refined process keeps S02 as targeted strengthening of the generated plan and S03 as a free editorial strengthening pass. Boundary debts no longer block package manufacture when the article goal and dossier-backed basis are clear.

### 2026-06-12 — atlas article target-plan manufactury self-contained refinement

Updated:

```text
work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
work/theory-writing/packages/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY.zip
work/theory-writing/reports/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_SELFCONTAINED_REFINEMENT_REPORT.md
```

Key rule: generated atlas article target-group plans must list exact read-only inputs and be buildable into independent/self-contained article-writing packages with bundled inputs.

### 2026-06-12 — A10 result integration and repair

Imported completed A10 result into:

```text
work/theory-writing/fragments/A10_mode_selection_map.md
work/theory-writing/fragments/A10_source_usage.md
work/theory-writing/fragments/A10_story_anchor_map.md
work/theory-writing/fragments/A10_figure_candidates.md
work/theory-writing/fragments/A10_open_questions.md
work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

Post-import repair added the missing target outputs from the updated A10 plan:

```text
work/theory-writing/fragments/A10_mode_selection_matrix.md
work/theory-writing/fragments/A10_decision_stress_tests.md
```

Service files from the result archive are stored at:

```text
work/theory-writing/reports/a10-result-import/
```

Evaluation/repair report:

```text
work/theory-writing/reports/A10_RESULT_INTEGRATION_EVALUATION_REPAIR_REPORT.md
```

A10 is now a ready input for later synchronization and final assembly checks.


### 2026-06-12 — A10 second repair and post-import validation rule

Updated A10 files:

```text
work/theory-writing/fragments/A10_mode_selection_map.md
work/theory-writing/fragments/A10_mode_selection_matrix.md
work/theory-writing/fragments/A10_decision_stress_tests.md
work/theory-writing/fragments/A10_source_usage.md
work/theory-writing/fragments/A10_open_questions.md
work/theory-writing/fragments/A10_degradation_and_duplication_audit.md
```

Process/protocol updates:

```text
protocols/rules/fragment-defect-analysis-and-repair.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/theory-writing/target-group-plans/A10_MODE_SELECTION_MAP_TARGET_GROUP_PLAN.md
work/theory-writing/reports/A10_SECOND_REPAIR_AND_FREE_PASS_DIAGNOSIS_REPORT.md
```

Key rule: for late synthetic fragments and linked-target groups, in-package free editorial passes must be followed by independent post-import validation in the deployed repo. Missing target outputs and stale companion debts are mechanical defects, not ordinary known debts.

### 2026-06-12 — C5 result integration and A10 sync

Imported completed C5 result into:

```text
work/theory-writing/fragments/C5_theory_to_technical_atlas.md
work/theory-writing/fragments/C5_source_usage.md
work/theory-writing/fragments/C5_story_anchor_map.md
work/theory-writing/fragments/C5_concept_atlas_article_map.md
work/theory-writing/fragments/C5_figure_candidates.md
work/theory-writing/fragments/C5_open_questions.md
work/theory-writing/fragments/C5_degradation_and_duplication_audit.md
```

Service files from the result archive are stored at:

```text
work/theory-writing/reports/c5-result-import/
```

Evaluation/repair report:

```text
work/theory-writing/reports/C5_RESULT_INTEGRATION_EVALUATION_REPAIR_REPORT.md
```

Post-import repair synced C5 with the now-present A10 outputs:

```text
work/theory-writing/fragments/A10_mode_selection_map.md
work/theory-writing/fragments/A10_mode_selection_matrix.md
work/theory-writing/fragments/A10_decision_stress_tests.md
```

Current C5 status: `ready_with_known_debts / A10 synced`.

### 2026-06-12 — Atlas article target-plan manufactury results

Imported completed manufactury result from `ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_RESULT.zip`.

Created/updated atlas article target plans:

```text
work/atlas/target-group-plans/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/spec_kit_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/kiro_specs_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/constitutional_sdd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/tdad_comparative_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/gsd_open_gsd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/bmad_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/target-group-plans/gas_town_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

Control matrices and reports:

```text
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_READINESS_MATRIX.md
work/atlas/plans/ATLAS_ARTICLE_BOUNDARY_MATRIX.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLANS_MANUFACTORY_REPORT.md
work/atlas/plans/reports/ATLAS_ARTICLE_TARGET_PLANS_IMPORT_EVALUATION_REPAIR_REPORT.md
work/atlas/plans/reports/manufactury-result-import/
```

Post-import repair closed stale default C5/A10 sync debts and added `Prompt-record manifest for package builder` to each target plan. The plans are not article texts and not executor packages; they are article-writing package specifications ready for manual review before package manufacture.


### 2026-06-12 — ADR atlas article plan repair and package

Repaired ADR article target plan:

```text
work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

Built self-contained article-writing executor package:

```text
work/atlas/packages/adr_method_ATLAS_ARTICLE.zip
```

Repair/package report:

```text
work/atlas/plans/reports/adr_method_PLAN_REPAIR_AND_PACKAGE_REPORT.md
```

Package status: ready for execution after manual review. The package bundles exact read-only inputs from the target plan and expands P01–P25 + Final into separate gated records.

## 2026-06-12 visual image-candidate rule update

- `work/atlas/target-group-plans/*_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` — все планы статей атласа обновлены: visual passes должны читать основной dossier image-candidate section, ставить inline external-real placeholders и вести disposition для каждого кандидата из досье.
- `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md` — общий blueprint статей атласа теперь включает dossier image-candidate disposition rule; после SPDD/Gas Town сравнений откатывает hard dossier-completeness and section-local enrichment logic к мягкому `Фактура без coverage-бюрократии`; после Gas Town style regression использует `style defect audit`, `selective natural rewrite` и guarded final style.
- `protocols/rules/visual-assets-and-figures.md` — правило для `Кандидаты на иллюстрации` / `image candidates` в досье.
- `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` — future plan-manufactury runs должны создавать планы, которые сохраняют это visual rule.
- `work/atlas/packages/adr_method_ATLAS_ARTICLE.zip` — пересобранный self-contained ADR article package с обновлённым visual block.
- `work/atlas/plans/reports/ATLAS_ARTICLE_IMAGE_CANDIDATE_RULE_REPAIR_REPORT.md` — отчёт о правке и проверке.

### 2026-06-12 — SPDD atlas article target-plan second repair

Updated target plan:

```text
work/atlas/target-group-plans/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
```

Updated SPDD plan reports/control files:

```text
work/atlas/plans/reports/spdd_method_PLAN_SECOND_REPAIR_REPORT.md
work/atlas/plans/reports/spdd_method_target_plan_manufacture_report.md
work/atlas/plans/reports/spdd_method_S05_readiness_stamp.md
work/atlas/plans/ATLAS_ARTICLE_BOUNDARY_MATRIX.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_LEDGER.md
work/atlas/plans/ATLAS_ARTICLE_TARGET_PLANS_MANUFACTORY_REPORT.md
```

No SPDD article-writing package was built in this step. The current SPDD plan is `ready_for_package_manufacture_after_manual_review` and should be reviewed before package manufacture.


- `work/atlas/plans/reports/DOSSIER_BACKED_COMPLETENESS_RULE_UPDATE_REPORT.md` — отчёт о системном усилении atlas article plans: досье как основная база статьи, coverage/disposition, transfer-audit, final dossier completeness check.


### 2026-06-12 — SPDD atlas article package

`work/atlas/packages/spdd_method_ATLAS_ARTICLE.zip` — self-contained package для написания concept-first статьи атласа `spdd_method` (`SPDD / OpenSPDD`). Пересобран после style-protocol softening и technical-anchoring softening. Содержит 27 gated records (`P01`–`P26` + `Final`) и точные bundled read-only inputs. Текст статьи ещё не выполнен.

`work/atlas/plans/reports/spdd_method_PACKAGE_MANUFACTORY_REPORT.md` — отчёт о сборке и smoke-test.


### 2026-06-12 — Persistent Work Graph atlas plan/package

`work/atlas/target-group-plans/persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` — repaired target plan for the PWG/Beads core concept atlas article. The plan now centers durable work state, Beads as mechanism anchor, boundaries with Gas Town/durable execution/issue trackers, and transfer to the multi-pass document workflow.

`work/atlas/packages/persistent_work_graph_ATLAS_ARTICLE.zip` — self-contained article-writing package built from the repaired plan.

`work/atlas/plans/reports/persistent_work_graph_PLAN_REPAIR_AND_PACKAGE_REPORT.md` and `persistent_work_graph_PACKAGE_MANUFACTORY_REPORT.md` — repair and package reports.


### Gas Town atlas package update — 2026-06-13

- `work/atlas/target-group-plans/gas_town_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` — Gas Town-specific atlas article plan aligned with the current softened blueprint. It now uses P01–P26 + Final: rollback-like `dossier inventory` instead of hard coverage matrix, no repeated `transfer-audit` checks in P04–P08, soft technical anchoring for key Gas Town claims, language passes before general repair/editorial, entry-sequence pass, companion sync, `style defect audit`, `selective natural rewrite`, and guarded final human technical style.
- `work/atlas/packages/gas_town_ATLAS_ARTICLE.zip` — self-contained executor package rebuilt from that plan; contains 27 gated records (`P01`–`P26` + `Final`) and exact bundled read-only inputs. The article itself has not been executed.
- `work/atlas/plans/reports/gas_town_PLAN_REPAIR_AND_PACKAGE_REPORT.md` — earlier repair/package report.
- `work/atlas/plans/reports/gas_town_PACKAGE_MANUFACTORY_REPORT.md` — earlier package manufactury checks.
- `work/atlas/plans/reports/gas_town_TECHNICAL_ANCHORING_ALIGNMENT_AND_PACKAGE_REPORT.md` — current alignment/rebuild report.


### 2026-06-12 — remaining atlas article packages

`work/atlas/target-group-plans/spec_kit_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`, `kiro_specs_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`, `constitutional_sdd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`, `tdad_comparative_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`, `gsd_open_gsd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`, `bmad_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` — repaired article-specific plans for concept-first atlas articles.

`work/atlas/packages/spec_kit_method_ATLAS_ARTICLE.zip`, `kiro_specs_ATLAS_ARTICLE.zip`, `constitutional_sdd_ATLAS_ARTICLE.zip`, `tdad_comparative_ATLAS_ARTICLE.zip`, `gsd_open_gsd_ATLAS_ARTICLE.zip`, `bmad_method_ATLAS_ARTICLE.zip` — self-contained packages for writing these atlas articles.

`work/atlas/plans/reports/REMAINING_ATLAS_PLANS_REPAIR_AND_PACKAGE_REPORT.md` — summary report and smoke-test evidence.


## Экспериментальный SPDD package без dossier-completeness hard gate

- `work/atlas/target-group-plans/experiments/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN_rollback_dossier_completeness.md` — variant target-plan для контрольного SPDD-запуска. Не заменяет canonical SPDD target-plan.
- `work/atlas/packages/spdd_method_ATLAS_ARTICLE_rollback_dossier_completeness.zip` — self-contained экспериментальный package для сравнения с canonical SPDD article package.
- `work/atlas/plans/reports/spdd_method_ROLLBACK_DOSSIER_COMPLETENESS_EXPERIMENT_PACKAGE_REPORT.md` — отчёт о создании и проверке экспериментального пакета.


### 2026-06-12 — style decompression rule and Gas Town package rebuild

Обновлены рабочие правила для atlas article packages после сравнения SPDD-вариантов до/после отката dossier-completeness hard gate. Действующее решение: не возвращать жёсткую `coverage matrix / relevant but untransferred` бюрократию как центральный gate. Вместо неё blueprint использует main-text-first перенос фактуры, section-local enrichment checks и мягкий entry-sequence pass.

Стилевой протокол `protocols/rules/human-technical-style.md` расширен правилом о смысловых свёртках и псевдотерминах: искусственные двух-/трёхсловные формулы нужно разворачивать в нормальное русское объяснение, а не заменять новым псевдотермином. Для больших atlas article packages хвост теперь: два языковых прохода → три общих repair/editorial прохода → entry-sequence/public structure → companion sync → два style-decompression прохода → guarded final human technical style pass. Финальный стиль сохраняет право улучшать тон и ритм, но не сжимает раскрытый смысл обратно.

Пересобран только Gas Town package: `work/atlas/packages/gas_town_ATLAS_ARTICLE.zip`. Остальные atlas target plans и packages в этой дельте не менялись. Отчёт: `work/atlas/plans/reports/gas_town_STYLE_DECOMPRESSION_BLUEPRINT_REPAIR_AND_PACKAGE_REPORT.md`.

## 2026-06-12 — Gas Town atlas package language-before-repair correction

- `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md` теперь задаёт для больших atlas article packages порядок: content/source/visual/concept reinforcement → два языковых прохода → три общих repair/editorial прохода → entry-sequence/public structure → companion sync → style defect audit → selective natural rewrite → guarded final human technical style pass → Final.
- `work/atlas/target-group-plans/gas_town_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` приведён к этому порядку. В Gas Town plan `P17`–`P18` — language passes, `P19`–`P21` — general repair/editorial, `P22` — entry-sequence, `P23` — companion sync, `P24`–`P25` — semantic decompression, `P26` — guarded final style.
- `work/atlas/packages/gas_town_ATLAS_ARTICLE.zip` пересобран после коррекции. Package содержит `P01`–`P26 + Final`, 27 records; payload order and first/second runner transitions checked.
- Другие atlas target plans/packages этой правкой не изменялись.
- Отчёт: `work/atlas/plans/reports/gas_town_LANGUAGE_BEFORE_REPAIR_BLUEPRINT_CORRECTION_REPORT.md`.

## 2026-06-12 — Gas Town latest result comparison

`work/atlas/plans/reports/gas_town_LATEST_RESULT_COMPARISON_REPORT.md` — сравнительный отчёт по двум выполненным Gas Town packages:

- `gas_town_ATLAS_ARTICLE_completed_package` — предыдущий результат до отката/смягчения hard dossier-completeness direction;
- `gas_town_result_package_completed` — результат после последних blueprint/plan corrections: language-before-repair, soft main-text-first enrichment, two semantic-decompression passes, guarded final style.

Главный вывод: последние изменения улучшили problem-first вход и локальную стилистическую декомпрессию, но финальный текст стал короче и более table-driven. Для самой Gas Town статьи предыдущий результат лучше как structural/factual base; последний результат лучше как donor для вступления, стиля, диагностических деталей и отдельных limits fragments. Для blueprint/plan нужен дополнительный мягкий guardrail: title/object preservation, no silent article compression, mechanism-anchor preservation and checkpoint snapshots around style/decompression tail.


### 2026-06-13 — SPDD plan and atlas style tail softened after Gas Town regression

После сравнения Gas Town результатов пользователь указал, что два decompression-pass-а сняли часть явных псевдотерминов, но местами ухудшили русский синтаксис: вместо нечеловеческих словосочетаний появились тяжёлые протокольные конструкции. Рабочий вывод: проблема не решается усилением запретов. Стилевой протокол должен быть калибровкой вкуса, а не исполняемым чек-листом тотального разворачивания.

Изменены:

```text
protocols/rules/human-technical-style.md
protocols/rules/language-style-rules.md
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
START.md
work/atlas/target-group-plans/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md
work/atlas/plans/reports/spdd_method_STYLE_PROTOCOL_BLUEPRINT_AND_PLAN_SOFTENING_REPORT.md
```

Новая базовая схема atlas style tail: `P24 — style defect audit`, `P25 — selective natural rewrite`, `P26 — guarded final human technical style pass`. `human-technical-style.md` теперь фиксирует не только смысловые свёртки и псевдотермины, но и обратный дефект — механическое разворачивание нормальной мысли в длинную протокольную конструкцию.

SPDD target plan позже обновлён повторно: hard coverage/disposition gate and main-text-first / section-local enrichment checks заменены на rollback-like dossier inventory и мягкий technical anchoring. `P17`–`P18` — языковые проходы; `P19`–`P21` — общие редакторские проходы; `P22` — entry-sequence/public structure; `P23` — companion sync; `P24`–`P26` — новый стилевой хвост. SPDD executor package пересобран после этой правки.


### 2026-06-13 — SPDD technical-anchoring softening and package rebuild

- `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md` — после последней правки откатывает hard dossier-completeness / section-local enrichment logic к `Фактура без coverage-бюрократии`: ключевые тезисы должны иметь технические опоры, если без них раздел становится общей прозой; ledger/image/open questions не заменяют основной текст.
- `work/atlas/target-group-plans/spdd_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` — обновлённый SPDD target plan: rollback-like dossier inventory, no coverage matrix, no repeated section-local enrichment checks in P04–P08, мягкий technical anchoring in P03/P08/P09/Final, current language-before-repair order and style audit/selective rewrite tail.
- `work/atlas/packages/spdd_method_ATLAS_ARTICLE.zip` — пересобранный self-contained package для `spdd_method`, 27 gated records (`P01`–`P26` + `Final`).
- `work/atlas/plans/reports/spdd_method_TECHNICAL_ANCHORING_SOFTENING_AND_PACKAGE_REPORT.md` — отчёт о правке blueprint/SPDD plan и проверках package.

### 2026-06-13 — ADR and PWG packages aligned with current technical-anchoring blueprint

- `work/atlas/target-group-plans/adr_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` — aligned with the current softened atlas blueprint: no hard coverage matrix, rollback-like dossier inventory, soft technical anchoring for ADR decision status / confirmation / replacement / AI-ADR research / executable projections, language passes before repair, style defect audit → selective natural rewrite → guarded final style.
- `work/atlas/target-group-plans/persistent_work_graph_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md` — aligned with the same blueprint: no hard coverage matrix, no repeated transfer-audit in P04–P08, soft technical anchoring for durable work state, Beads command/state anchors and document-process transfer, current language-before-repair and style-tail order.
- `work/atlas/packages/adr_method_ATLAS_ARTICLE.zip` — rebuilt self-contained executor package; 27 gated records (`P01`–`P26` + `Final`).
- `work/atlas/packages/persistent_work_graph_ATLAS_ARTICLE.zip` — rebuilt self-contained executor package; 27 gated records (`P01`–`P26` + `Final`).
- `work/atlas/plans/reports/adr_pwg_TECHNICAL_ANCHORING_ALIGNMENT_AND_PACKAGES_REPORT.md` — report for the plan alignment, package rebuild and checks.

These package rebuilds do not execute the article-writing packages and do not create final article files under `work/atlas/articles/`. The remaining six atlas packages may still predate the current technical-anchoring/style-tail blueprint unless rebuilt separately.


### 2026-06-13 — all canonical atlas article plans aligned with accepted blueprint

All ten canonical atlas article target plans under `work/atlas/target-group-plans/` now follow the accepted technical-anchoring/style-tail blueprint. The last aligned set was:

- `work/atlas/target-group-plans/spec_kit_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
- `work/atlas/target-group-plans/kiro_specs_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
- `work/atlas/target-group-plans/constitutional_sdd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
- `work/atlas/target-group-plans/tdad_comparative_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
- `work/atlas/target-group-plans/gsd_open_gsd_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`
- `work/atlas/target-group-plans/bmad_method_ATLAS_ARTICLE_TARGET_GROUP_PLAN.md`

Their rebuilt executor packages are:

- `work/atlas/packages/spec_kit_method_ATLAS_ARTICLE.zip`
- `work/atlas/packages/kiro_specs_ATLAS_ARTICLE.zip`
- `work/atlas/packages/constitutional_sdd_ATLAS_ARTICLE.zip`
- `work/atlas/packages/tdad_comparative_ATLAS_ARTICLE.zip`
- `work/atlas/packages/gsd_open_gsd_ATLAS_ARTICLE.zip`
- `work/atlas/packages/bmad_method_ATLAS_ARTICLE.zip`

The current canonical atlas package shape is `P01`–`P26 + Final`: source/content passes, visual passes, concept reinforcement, two language passes, three general repair/editorial passes, entry-sequence, companion sync, style defect audit, selective natural rewrite, guarded final human technical style, and final verification. Do not reintroduce hard dossier coverage / `relevant but untransferred` gates unless the user explicitly reopens that decision.

Report: `work/atlas/plans/reports/remaining_atlas_TECHNICAL_ANCHORING_ALIGNMENT_AND_PACKAGES_REPORT.md`.


### 2026-06-13 — patched anchor atlas articles included in filesystem

Accepted patched atlas article results now present under `work/atlas/articles/`:

- `work/atlas/articles/spdd_method.md` — SPDD v4 article with user-edited patch: three SPDD human skills, `/spdd-reverse`, numeric billing anchors, and localized OpenSPDD source-excerpt assets.
- `work/atlas/articles/persistent_work_graph.md` — PWG v4 article with local patch: `bd ready` / `bd blocked`, durable gate fields, `bd prime` as compact restart context, and source-state transitions.
- `work/atlas/articles/gas_town.md` — Gas Town v4 article with user-edited patch: problem-state vocabulary and local source-excerpt SVG assets for Yegge Figure 5 / Figure 6.
- `work/atlas/articles/adr_method.md` — ADR v4 article with local patch: localized source-excerpt SVG assets for Nygard, MADR, AWS lifecycle and Design Decision Gate; generated/reconstructed ADR remains candidate evidence until human acceptance.

Companion files live next to each article using the same article prefix: `_source_usage.md`, `_source_transfer_ledger.md`, `_image_plan.md`, `_external_image_queue.md`, `_open_questions.md`, `_theory_links.md`, readiness/report files and patch reports where applicable. These articles are accepted local patch results, not new blueprint/plan changes.

Filesystem inclusion report for the latest ADR inclusion: `work/atlas/plans/reports/adr_method_PATCHED_ARTICLE_FILESYSTEM_INCLUSION_REPORT.md`.

---

# 6. Atlas article outputs

Текущие включённые результаты atlas articles находятся в:

```text
work/atlas/articles/spdd_method.md
work/atlas/articles/persistent_work_graph.md
work/atlas/articles/gas_town.md
work/atlas/articles/adr_method.md
work/atlas/articles/spec_kit_method.md
work/atlas/articles/kiro_specs.md
work/atlas/articles/constitutional_sdd.md
work/atlas/articles/tdad_comparative.md
work/atlas/articles/gsd_open_gsd.md
work/atlas/articles/bmad_method.md
```

Статус: десять canonical atlas article outputs включены в файловую систему. SPDD, PWG, Gas Town и ADR включены как patched anchor articles; оставшиеся шесть включены из latest completed packages. Для всех статей сохраняются companion-файлы рядом с основным `.md`: source usage, source transfer ledger, image plan, external image queue, open questions, theory links, degradation/duplication audit and readiness reports where provided by the package.

Заголовок `Вопрос читателя` больше не используется в article headings; текущая формула — `О чём эта статья`.



## Post-atlas chapter-plan blueprint proposal

`work/theory-writing/reports/POST_ATLAS_CHAPTER_TARGET_PLAN_BLUEPRINT_PROPOSAL.md` — предложенный blueprint для будущих chapter target-group plans. Документ пока proposal, не active protocol: использовать его для обсуждения и пилотного plan-manufacturing, но не считать автоматически утверждённым, пока пользователь явно не примет.


## Post-Atlas chapter blueprint correction — 2026-06-13

The previous combined chapter blueprint proposal is superseded because it mixed global preparation with per-chapter writing. Current planning artifacts:

- `work/theory-writing/reports/POST_ATLAS_GLOBAL_CORPUS_ROUTING_PREPARATION_BLUEPRINT.md` — proposed one-time/global preparation package for chapter routing: chapter list, Atlas routing, A/B/C fragment routing, dossier gap map, story anchors, external discovery profiles, visual routing and input matrix.
- `work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md` — рабочий blueprint для плана одной послеатласной главы. Обновлён по результату главы II: вместо отдельного языко-стилевого хвоста использует добор материала и русскую перепись после каждого существенного содержательного изменения; внешний поиск добавляется только при реальной лакуне.
- `work/theory-writing/reports/POST_ATLAS_CHAPTER_TARGET_PLAN_BLUEPRINT_PROPOSAL.md` — superseded historical proposal; kept for provenance only.

Next planning step should normally be a `GLOBAL_CORPUS_ROUTING` target-group plan/package, not a direct chapter-writing package.


## Skeleton V5 — second language/style pass — 2026-06-13

`work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md` прошёл второй, более строгий языко-стилевой проход после замечания пользователя, что первый проход оставил слишком много английских полупредложений. Структура, список глав, источникoвая иерархия и модель тяжёлого пакета главы не менялись.

Отчёт: `work/theory-writing/reports/SKELETON_V5_LANGUAGE_STYLE_PASS_2_REPORT.md`.

## Post-atlas global corpus routing package — 2026-06-13

`work/theory-writing/packages/POST_ATLAS_GLOBAL_CORPUS_ROUTING.zip` — repo-snapshot-bound executor package для общего routing layer перед изготовлением планов глав. Пакет не содержит весь корпус источников и должен запускаться рядом с отдельно развёрнутым репозиторием. Он создаёт карты глав, маршрутизацию Атласа, A/B/C-фрагментов, досье, story anchors, external discovery profiles, visual candidates and chapter package input matrix.

Target plan: `work/theory-writing/target-group-plans/POST_ATLAS_GLOBAL_CORPUS_ROUTING_TARGET_GROUP_PLAN.md`.
Report: `work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_PACKAGE_BUILD_REPORT.md`.

---

## Post-Atlas global corpus routing result — 2026-06-13

Статус: результат repo-level package `POST_ATLAS_GLOBAL_CORPUS_ROUTING` включён в файловую систему как рабочий слой маршрутизации для будущего изготовления планов глав.

Основные выходы результата:

```text
work/theory-writing/reports/POST_ATLAS_CHAPTER_LIST_AND_SCOPE_MAP.md
work/theory-writing/reports/POST_ATLAS_ATLAS_TO_CHAPTER_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_FRAGMENT_TO_CHAPTER_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_DOSSIER_TO_CHAPTER_GAP_MAP.md
work/theory-writing/reports/POST_ATLAS_STORY_ANCHOR_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_EXTERNAL_SOURCE_DISCOVERY_MAP.md
work/theory-writing/reports/POST_ATLAS_VISUAL_CANDIDATE_ROUTING_MAP.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_DECISIONS.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_OPEN_QUESTIONS.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_READINESS_REPORT.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_VERIFY.md
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_RESUME.md
```

Сырой result-архив сохранён как:

```text
work/theory-writing/results/POST_ATLAS_GLOBAL_CORPUS_ROUTING_RESULT.zip
```

Оценка результата:

```text
work/theory-writing/reports/POST_ATLAS_GLOBAL_ROUTING_RESULT_INCLUSION_AND_EVALUATION_REPORT.md
```

Результат пригоден как routing layer: он не пишет главы, не создаёт per-chapter plans, не запускает внешний поиск и не подменяет Skeleton V5. Перед изготовлением конкретных планов глав нужно использовать `POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md` вместе с актуальным `POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md`.

## Chapter I target plan — 2026-06-13

`work/theory-writing/target-group-plans/CHAPTER_I_UNIT_OF_ANALYSIS_TARGET_GROUP_PLAN.md` — рабочий target-group plan для пилотной главы I, `Единица анализа: программное изменение, а не prompt`.

Статус: готов для ручной проверки и последующей сборки chapter-writing package. План не пишет главу и не меняет Skeleton or routing maps. Он использует post-atlas global routing layer and current per-chapter blueprint, но адаптирует их под особенность главы: глава задаёт единицу анализа, поэтому должна отличить prompt, task, diff, session trace and software change, не превращаясь в prompt-philosophy, method catalogue or protocol handbook.

Ключевые входы: `00_spine_map`, Skeleton V5, A1, A10, SPDD/Spec Kit/Kiro/BMAD atlas articles, sparse story anchors Boris/Peter/Calvin/Mark/HumanLayer and D1 source-restoration only if terminology/provenance needs it.


## Chapter I package — unit of analysis

Status: package built, chapter not written.

- Target plan: `work/theory-writing/target-group-plans/CHAPTER_I_UNIT_OF_ANALYSIS_TARGET_GROUP_PLAN.md`.
- Executor package: `work/theory-writing/packages/CHAPTER_I_UNIT_OF_ANALYSIS.zip`.
- Build report: `work/theory-writing/reports/CHAPTER_I_UNIT_OF_ANALYSIS_PACKAGE_BUILD_REPORT.md`.

This package is the pilot per-chapter writing package after the post-atlas routing layer. It uses a self-contained selected-input bundle, not the whole repository, and tests the new per-chapter plan logic on Chapter I: software change as the unit of analysis, not prompt/task/diff/session.


## Package creation protocol hardening — 2026-06-13

Updated protocol files:

```text
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/TASK_PACKAGE_MANUFACTORY_PROTOCOL.md
work/reports/TASK_PACKAGE_CREATION_PROTOCOL_STAGED_RESUME_UPDATE_REPORT.md
```

Purpose: harden executor package construction after the Chapter I pilot exposed a failure mode in which a weaker model, after interruption, could inspect visible future-plan clues and synthesize pass reports/final outputs too quickly.

Operational consequences for future packages:

- regular executor packages must not include open `TARGET_PLAN_SNAPSHOT.md`, full pass queue, final artifact inventory or readiness checklist;
- full target plans remain build-time inputs;
- package builders may receive `stage_count` or `max_passes_per_stage` without changing the target plan;
- heavy chapter packages should use planned stage stops or separate stage packages;
- interruption/resume behavior is now explicit: no reconstruction of missing pass outputs, no bulk creation of future pass reports, no finalization before final worksheet;
- final verification must check chain integrity.

Current status: protocol update only. Existing packages are not automatically rebuilt.


## Chapter II and III target plans

Созданы рабочие планы для следующих глав:

```text
work/theory-writing/target-group-plans/CHAPTER_II_AGENTIC_SESSION_TRACE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_III_INTENT_SPEC_CONTRACT_ADR_TARGET_GROUP_PLAN.md
```

Оба плана используют Skeleton V5, послеатласные карты маршрутизации, A/B/C-фрагменты, Атлас, досье, stories and ordinary language/style tail. Они не являются готовыми главами и не заменяют будущие executor packages.

## Chapter II/III target plans — individuality patch — 2026-06-13

Обновлены рабочие планы глав II и III:

```text
work/theory-writing/target-group-plans/CHAPTER_II_AGENTIC_SESSION_TRACE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_III_INTENT_SPEC_CONTRACT_ADR_TARGET_GROUP_PLAN.md
work/theory-writing/reports/CHAPTER_II_III_TARGET_PLANS_INDIVIDUALITY_PATCH_REPORT.md
```

Изменение не переписывает Skeleton V5 и global routing. Оно усиливает индивидуальность будущих глав: глава II теперь строится вокруг анатомии живой агентской сессии, а глава III — вокруг лестницы полномочий артефактов и границы `candidate vs accepted`.



## Chapter II/III packages

Добавлены no-stage executor packages для глав II и III, построенные из очищенных target plans и текущего post-atlas package protocol.


## Chapter IV–VI target plans — 2026-06-14

Созданы рабочие планы для следующих глав:

```text
work/theory-writing/target-group-plans/CHAPTER_IV_SPDD_SPECIFICATION_LIFECYCLE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_V_PROTECTED_SPECIFICATION_PROFILES_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_VI_CONTEXT_WORKING_STATE_INTERFACE_TARGET_GROUP_PLAN.md
```

Планы используют Skeleton V5, послеатласные карты маршрутизации, готовый Атлас, релевантные A/B/C-фрагменты и обычный языко-стилевой хвост. Они не пишут главы и не заменяют будущие executor packages.

Особенности:

- IV — глубокий SPDD-узел: REASONS Canvas, человеческие навыки, OpenSPDD как переходы жизненного цикла, billing example, `/spdd-reverse`, sync/update, границы метода.
- V — сравнительный узел спецификационных профилей: Spec Kit, Kiro, Constitutional SDD и TDAD по обязанностям, а не по набору возможностей.
- VI — мостовой узел между specification profiles и PWG: проектный контекст как интерфейс агента, происхождение поведения, rules/specs/skills/state files, граница с PWG и runtime.

Для VI в плане явно указано: если A4/C4 отсутствуют в доступном пакете, это нужно зафиксировать, а не восстанавливать по памяти.

## Update — chapter IV–VI target plans individuality/language pass

Обновлены планы глав IV–VI. Глава IV теперь подчёркивает SPDD как путь одного программного изменения; глава V строит спецификационные профили через типы сбоев и усиливает TDAD как самостоятельную тестовую логику; глава VI описывает проектный контекст как интерфейс агента и добавляет проверки устаревших правил и конфликтующих источников. После содержательных правок выполнен отдельный языко-смысловой проход по планам. Пакеты не создавались.

## 2026-06-14 — словарь смыслового перевода

Добавлен устойчивый словарь терминологического перевода:

```text
protocols/rules/conceptual-translation-glossary.md
```

Его роль — не расширять стилевой протокол новыми запретами, а отделить смысловой перевод терминов агентской разработки от обычного словаря анти-калек. В него вынесены различения для `evidence`, `transcript`, `trace`, `observation`, `acceptance`, `handoff`, `artifact` и `state`. После уточнения словарь прямо запрещает переводить `evidence` как `наблюдение`: `наблюдение` оставлено для `observation`, а материал проверки должен называться по функции — `результат проверки`, `артефакт проверки`, `проверочный материал`, `проверочное основание`, `основание для принятия изменения`, `подтверждение` или, в строгих случаях, `доказательство`.

Обновлены связанные правила и будущие package inputs: `language-style-rules.md` теперь прямо указывает на словарь, `terminology-and-translation.md` оставлен для обычных английских слов и отсылает сложные случаи в новый документ, а chapter blueprint / input matrix / chapter target plans I–VI включают словарь как явный read-only input. Это должно предотвращать автоматические переводы вроде `evidence → свидетельство`, `evidence → наблюдение` и `transcript → стенограмма` в новых главах и при ретроспективной правке уже написанного текста.



## 2026-06-14 — ретроспективная терминологическая проверка и риск протокольного языка

Уточнён `protocols/rules/conceptual-translation-glossary.md`: `evidence` больше не предлагается переводить как `наблюдение`. `Наблюдение` оставлено для `observation` и для материала, который помогает вести текущую работу, но сам по себе не даёт права принять изменение.

Добавлено правило ретроспективной правки: при языковом проходе, `selective natural rewrite` или обычной просьбе сделать текст естественнее нужно проверять не только английские исходные термины, но и уже написанные русские слова: `свидетельство`, `наблюдение`, `стенограмма`, `доказательный`, `трасса сессии`. Они могут быть следами прежнего неудачного перевода. Замена не должна быть массовой; нужно заново определить функцию слова в предложении.

Отдельно зафиксирован риск: языковые и рабочие протоколы написаны операционным языком, а не языком финальной главы. Они должны работать как ограничения и критерии, но не как prose sample. Target plans опаснее, потому что становятся seed-текстом для будущей главы; поэтому их нужно вычитывать естественным русским до сборки executor package.

## Chapter II target plan — natural Russian rewrite update — 2026-06-14

Обновлён план главы II:

```text
work/theory-writing/target-group-plans/CHAPTER_II_AGENTIC_SESSION_TRACE_TARGET_GROUP_PLAN.md
work/theory-writing/reports/CHAPTER_II_TARGET_PLAN_NATURAL_REWRITE_UPDATE_REPORT.md
```

Смысл обновления: сохранить добор источников, добор материала, усиление главы и визуально-ссылочные проверки, но заменить отдельные языковые/стилевые проходы на естественную русскую перепись после каждого существенного содержательного изменения. План также явно снимает неявный потолок объёма: будущая глава не должна подгоняться под привычный размер, если тема требует большего раскрытия.

При будущей сборке пакета главы II прежний no-stage package считать устаревшим по очереди проходов: его нужно пересобрать из обновлённого target plan.


## План главы II — сжатие очереди проходов — 2026-06-14

Обновлён план главы II:

```text
work/theory-writing/target-group-plans/CHAPTER_II_AGENTIC_SESSION_TRACE_TARGET_GROUP_PLAN.md
work/theory-writing/reports/CHAPTER_II_TARGET_PLAN_STRUCTURE_SIMPLIFICATION_REPORT.md
```

Правка сжимает очередь проходов с 31 до 22 без удаления содержательного добора. Ранние шаги восстановления рамки, фрагментов, историй, Атласа и досье объединены в три рабочих шага, чтобы подготовка не превращалась в семь отдельных отчётов до первого черновика. Прежние отдельные ремонты логики аргумента и технической плотности убраны: их полезная часть перенесена в добор слабых мест и проверку обзорности.

Решение по фигуре перенесено после появления устойчивого текста главы. Раннее чтение источников может только записывать визуальных кандидатов; вставлять или отклонять фигуру нужно после черновика, интеграции материалов и русской переписи.

Термин `читательский ход` удалён как неестественный рабочий язык. План использует формулировку `логика построения главы`.

## План главы II — русский язык вспомогательных текстов и визуальный баланс — 2026-06-14

Обновлён план главы II:

```text
work/theory-writing/target-group-plans/CHAPTER_II_AGENTIC_SESSION_TRACE_TARGET_GROUP_PLAN.md
work/theory-writing/reports/CHAPTER_II_TARGET_PLAN_RUSSIAN_TEXT_AND_VISUAL_BALANCE_UPDATE_REPORT.md
```

Правка уточняет уже упрощённый план. Во все места, где создаётся текст — основной черновик, рабочие заметки, журналы поиска, решения по источникам, реестры, сопутствующие файлы и финальные отчёты — добавлено требование писать естественным русским техническим языком. Формулировки target plan прямо помечены как рабочие указания, а не как готовые фразы будущей главы.

Порядок объяснения главы теперь не должен становиться скрытым мини-черновиком: P07 собирает только 5–7 пунктов логики. Полная проверка источников сдвинута к финалу, потому что поздний добор может добавить новые ссылки. Шаги про обзорность и фигуру переставлены: сначала глава избавляется от каталога материалов и выбирает сильные сцены/технические опоры, потом принимается решение по изображению.

Визуальный шаг теперь смещён в сторону сохранения полезного кандидата: если изображение действительно помогает главе и его можно использовать, лучше зафиксировать или встроить его в текущем пакете, потому что позже восстановить потерянный визуальный материал из нескольких уровней документов трудно. Отказ от фигуры остаётся допустимым, но должен быть обоснован.

План дополнительно вычитан на естественный русский. Убраны рабочие маркеры вроде `рабочие якоря`, `визуальный долг`, `первый экран`, `карта внутренних опор`, `asset-проход` и `readiness report`.


## План главы II — короткие локальные напоминания о естественном русском языке — 2026-06-14

Обновлён план главы II:

```text
work/theory-writing/target-group-plans/CHAPTER_II_AGENTIC_SESSION_TRACE_TARGET_GROUP_PLAN.md
work/theory-writing/reports/CHAPTER_II_TARGET_PLAN_SHORT_LOCAL_RUSSIAN_PROMPTS_REPORT.md
```

Правка сохраняет очередь из 22 проходов и не меняет содержательную логику плана. Локальные языковые напоминания в шагах, где создаётся или правится текст, сокращены до короткой формулы: `Пиши создаваемый текст естественным русским языком.` Для проходов переписи используется форма `Переписывай текст естественным русским языком.`

Цель правки — дать исполнителю короткий якорь прямо в текущей инструкции, не превращая каждый шаг в мини-стильгайд и не добавляя новый протокольный шум. Подробные правила языка, терминологии и словаря смыслового перевода остаются в общих протоколах.


## Глава II — принят новый результат пакета и внесён в рабочие файлы — 2026-06-14

Последний результат пакета главы II принят как текущая рабочая версия и внесён в репозиторий:

```text
work/theory-writing/chapters/II_agentic_session_trace.md
work/theory-writing/chapters/II_agentic_session_trace_*.md
work/theory-writing/chapters/II_agentic_session_trace_passes/
work/theory-writing/reports/CHAPTER_II_RESULT_INTEGRATION_AND_TERMINOLOGY_PATCH_REPORT.md
work/DELETE_PATHS_CHAPTER_II_RESULT_INTEGRATION.txt
```

Новая версия заметно лучше предыдущей по языку и терминологии: убраны `свидетельство` как неудачный перевод `evidence`, почти полностью снята `трасса` как псевдотермин, а основной ход главы строится вокруг `следа сессии`, вмешательства человека и состояния работы после обрыва.

После применения результата выполнена локальная правка: `стенограмма` заменена там, где речь шла об обычной переписке или сыром логе разговора; `diff` в русской прозе заменён на `дифф`; встроенная текстовая схема русифицирована; термин `выживание результата` убран из заголовка и основного текста. Словарь смыслового перевода получил отдельную запись о нежелательности этой формы.

При применении overlay нужно удалить старый каталог `work/theory-writing/chapters/II_agentic_session_trace_passes/`, иначе старые pass-файлы из baseline останутся рядом с новыми P01–P22. Готовые старые пакеты главы II считать историческими. Если главу II нужно запускать заново, пакет следует пересобрать из текущего target plan; если нужно продолжать редактирование, исходить из `II_agentic_session_trace.md` как текущей рабочей версии.

## Глава II — правка формулировки вместо «повторного расследования» — 2026-06-14

Обновлены:

```text
work/theory-writing/chapters/II_agentic_session_trace.md
protocols/rules/conceptual-translation-glossary.md
work/theory-writing/reports/CHAPTER_II_INVESTIGATION_WORDING_PATCH_REPORT.md
```

Правка уточняет уже принятую замену `выживание результата`. Формулировка `работу можно продолжить без повторного расследования` признана неестественной: слово `расследование` слишком юридическое/детективное для обычной мысли о продолжении агентской работы. В словаре и тексте главы используется более простой вариант: следующий человек или агент может продолжить работу, не выясняя заново, что было сделано, что проверено и где остались риски.

## Post-Atlas per-chapter blueprint обновлён по результату главы II — 2026-06-14

`work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md` переписан как действующий blueprint для будущих планов отдельных глав. Новый blueprint закрепляет форму, проверенную на главе II: короткая подготовка рамки, рабочая модель предмета главы, выбор внутренних материалов, внешний поиск только по лакунам, первый черновик, русская перепись, содержательная интеграция, русская перепись после каждого крупного добора, добор слабых мест без потолка объёма, проверка обзорности, решение по фигуре после устойчивого текста, финальная проверка потерь и синхронизация сопутствующих файлов.

Старый хвост `language pass / style pass / selective natural rewrite / guarded final style` больше не является обычной схемой для послеатласных глав. Он сохранён только как исторический след в старых пакетах и в общих протоколах, где теперь добавлено уточнение: для послеатласных глав использовать обновлённый blueprint.


## Post-Atlas per-chapter blueprint: русская перепись самого плана — 2026-06-14

Обновлены:

```text
work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md
work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_BLUEPRINT_PLAN_RUSSIAN_REWRITE_UPDATE_REPORT.md
```

Blueprint теперь явно требует: после написания плана главы выполнить отдельную русскую перепись самого плана. Эта перепись не меняет очередь проходов и не добавляет новые требования; она убирает протокольный ритм, служебные кальки, искусственные рабочие термины, повторяющиеся страхующие формулы и фразы, похожие на готовые абзацы будущей главы.

Сам blueprint также переписан как естественный русский рабочий документ. Его задача — порождать планы, похожие на обновлённый план главы II: с содержательным добором материала, русской переписью после существенных изменений, решением по изображениям после устойчивого текста и без старого хвоста отдельных языковых и стилевых проходов.

Словарь смыслового перевода уже содержит отдельную запись про `расследование`: слово допустимо для настоящего разбора инцидента, но не должно заменять обычные формулы вроде `выяснить заново, что было сделано` или `восстановить ход работы`.


## Post-Atlas per-chapter blueprint: гибкость очереди и защита от чрезмерной спецификации — 2026-06-14

Обновлены:

```text
work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md
protocols/rules/conceptual-translation-glossary.md
work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_BLUEPRINT_FLEXIBILITY_AND_SPECIFICATION_UPDATE_REPORT.md
```

Blueprint уточнён после обсуждения нового плана главы II. Базовая очередь больше не читается как обязательная форма на 22 прохода: план может быть короче или длиннее, если это отражает сложность главы, количество аспектов для добора, внешний поиск, изображения и риск обзорности. Каждый конкретный план должен явно выбрать профиль внешнего поиска `D0`, `D1`, `D2` или `D3`.

Добавлено определение существенного содержательного изменения: новый источник, сцена, различение, раздел, пример или правка хода аргумента. После такого изменения переписывается затронутый раздел; вся глава переписывается только если изменилась общая логика.

Отдельно закреплено, что план не должен быть механической копией blueprint, мини-главой или чрезмерно подробной заготовкой, где исполнителю остаётся только заполнить фразы. Он задаёт направление, материалы, риски и критерии; конкретный текст рождается в исполнительном пакете.

В словарь смыслового перевода добавлена запись про `долг`: слово допустимо для настоящего technical debt, но не для обычных планировочных форм вроде `визуальный долг` или `долг для другой главы`. В таких случаях писать `открытый вопрос`, `отложенная задача`, `кандидат для последующей работы`, `тема для другой главы` или `запись для последующей работы`.


## 2026-06-14 — планы оставшихся послеатласных глав по новому blueprint

Созданы или переписаны планы всех глав послеатласного ряда, кроме I–II. Новые планы следуют схеме, проверенной на главе II: профиль внешнего поиска выбран явно, добор материала сохранён, русская перепись запускается после существенных содержательных изменений, а сам план не должен становиться мини-главой.

- `work/theory-writing/target-group-plans/INTRO_NOT_CODE_GENERATION_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_III_INTENT_SPEC_CONTRACT_ADR_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_IV_SPDD_SPECIFICATION_LIFECYCLE_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_V_PROTECTED_SPECIFICATION_PROFILES_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_VI_CONTEXT_WORKING_STATE_INTERFACE_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_VII_PERSISTENT_WORK_GRAPH_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_VIII_PROTECTED_PROCESS_PROFILES_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_IX_EXECUTION_ENVIRONMENT_RUNTIME_RIGHTS_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_X_GAS_TOWN_BEADS_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_XI_VERIFICATION_MATERIAL_TESTS_REVIEW_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_XII_AUTHORITY_RESPONSIBILITY_OUTER_CONTOUR_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CHAPTER_XIII_POST_MERGE_MAINTENANCE_LEARNING_TARGET_GROUP_PLAN.md`
- `work/theory-writing/target-group-plans/CONCLUSION_MODE_SELECTION_TARGET_GROUP_PLAN.md`
- `work/theory-writing/reports/POST_ATLAS_REMAINING_CHAPTER_TARGET_PLANS_REWRITE_REPORT.md` — отчёт о переписывании планов.


## Планы глав III–VI: индивидуализация после обновления blueprint — 2026-06-14

Обновлены:

```text
work/theory-writing/target-group-plans/CHAPTER_III_INTENT_SPEC_CONTRACT_ADR_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_IV_SPDD_SPECIFICATION_LIFECYCLE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_V_PROTECTED_SPECIFICATION_PROFILES_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_VI_CONTEXT_WORKING_STATE_INTERFACE_TARGET_GROUP_PLAN.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_III_VI_PLAN_INDIVIDUALIZATION_REPORT.md
```

Планы III–VI больше не являются одинаковой реализацией общей очереди. У каждой главы задан собственный режим письма: III — цепочка носителей намерения и решения; IV — полный цикл SPDD; V — сравнение профилей по общей фиче и осям; VI — проектный интерфейс агента с глубоким раскрытием `skills`, `hooks`, `MCP`, `subagents`.

Глава VI намеренно усилена как большая глава. В плане прямо снят неявный потолок объёма и добавлены отдельные проходы для ключевых понятий, чтобы они не превратились в каталог инструментов.


## Планы III–VI: второе усиление индивидуальности и языка — 2026-06-14

Обновлены:

```text
work/theory-writing/target-group-plans/CHAPTER_III_INTENT_SPEC_CONTRACT_ADR_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_IV_SPDD_SPECIFICATION_LIFECYCLE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_V_PROTECTED_SPECIFICATION_PROFILES_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_VI_CONTEXT_WORKING_STATE_INTERFACE_TARGET_GROUP_PLAN.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_III_VI_SECOND_INDIVIDUALIZATION_AND_LANGUAGE_REVIEW_REPORT.md
```

Правка усиливает индивидуальность будущих глав и одновременно чистит язык планов. III теперь сильнее держит разрыв между сгенерированным текстом и принятым изменением. IV заменяет неудачный `обратный вход` на восстановление намерения по старому коду. V сильнее строится вокруг выбора профиля. VI расширена до 29 проходов и получила отдельную проверку, что `skills`, `hooks`, `MCP`, `subagents` раскрыты как механизмы проектного интерфейса, а не как список инструментов.

Замечание по языку: `лакуна` не считается проблемным словом само по себе. Это нормальное, хотя и редкое, русское слово; его не нужно автоматически заменять при будущих правках.

## План главы VI: уточнение языка и механики `skills` / `hooks` / `MCP` / `subagents` — 2026-06-14

Обновлён:

```text
work/theory-writing/target-group-plans/CHAPTER_VI_CONTEXT_WORKING_STATE_INTERFACE_TARGET_GROUP_PLAN.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_VI_INTERFACE_MECHANISMS_LANGUAGE_PATCH_REPORT.md
```

Правка точечно исправляет язык плана главы VI и убирает слишком симметричную постановку проходов P08–P11. Теперь `skills`, `hooks`, `MCP` и `subagents` раскрываются не по одинаковой анкете, а через разные функции проектного интерфейса: повторяемая способность, автоматическое вмешательство, управляемый доступ и разделение внимания/ответственности между агентами.

Очередь главы VI остаётся на 29 проходах; профиль внешнего поиска остаётся `D3`. Смысл правки — сильнее удержать главу VI как большую главу о проектном интерфейсе агента, а не как каталог возможностей.

## Языковая правка планов глав III–V — 2026-06-14

Обновлены:

```text
work/theory-writing/target-group-plans/CHAPTER_III_INTENT_SPEC_CONTRACT_ADR_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_IV_SPDD_SPECIFICATION_LIFECYCLE_TARGET_GROUP_PLAN.md
work/theory-writing/target-group-plans/CHAPTER_V_PROTECTED_SPECIFICATION_PROFILES_TARGET_GROUP_PLAN.md
work/theory-writing/reports/POST_ATLAS_CHAPTER_III_IV_V_LANGUAGE_PATCH_REPORT.md
```

Правка убирает из планов III–V несколько формул, которые были понятны как внутренние рабочие ярлыки, но звучали неестественно в русском техническом тексте. Глава V теперь не выносит `поверхность` в главное место плана; глава IV говорит о полном рабочем цикле и возвращении принятого результата в документы, решения и текущее состояние проекта; глава III уточняет язык вокруг внешних источников и восстановления истории решения.

## 2026-06-14 — план главы VI: глубокое раскрытие ключевых механизмов перенесено после первого черновика

Пользователь уточнил, что для главы VI небезопасно подробно разбирать `skills`, `hooks`, `MCP` и `subagents` до первого черновика. Даже если эти проходы не должны писать готовые разделы, они всё равно задают симметричный материал и могут подтолкнуть будущую главу к каталогу четырёх возможностей агентской платформы.

План `work/theory-writing/target-group-plans/CHAPTER_VI_CONTEXT_WORKING_STATE_INTERFACE_TARGET_GROUP_PLAN.md` обновлён. До первого черновика теперь остаётся только короткое разведение четырёх понятий: повторяемая способность, автоматическое вмешательство, управляемый доступ и разделение внимания/ответственности. Глубокие проходы по `skills`, `hooks`, `MCP` и `subagents` перенесены после первого черновика и первой русской переписи. Они работают уже с живым текстом: находят место в существующей главе, добавляют объяснение, пример, источник, риск и связь с общей логикой.

После этих четырёх усилений добавлена отдельная русская перепись, чтобы глава снова читалась как цельный текст о проектном интерфейсе агента, а не как черновик с поздно добавленными техническими блоками. Очередь главы VI теперь содержит 30 проходов.
## 2026-06-14 — глава III: принята расширенная ADR-редакция V4; глава IV проверена против SPDD-Атласа

В файловую систему внесена последняя редакция главы III после ADR-расширения и ребаланса: `work/theory-writing/chapters/III_intent_spec_contract_adr.md`. Эта версия сохраняет усиленный ADR-блок, но больше не подаёт ADR как единственный возможный способ записывать архитектурные решения. ADR объясняется как удобная и распространённая форма явной записи решения; рядом явно оставлено место для RFC, дизайн-документа, обсуждения в pull request, задачи или внутреннего журнала решений, если они выполняют ту же функцию в проекте.

Также обновлены сопутствующие файлы главы III и заменён каталог проходов `work/theory-writing/chapters/III_intent_spec_contract_adr_passes/`. Перед применением overlay старый каталог проходов главы III нужно удалить, чтобы старые pass-файлы не остались рядом с текущими `P01.md`…`P23.md` и `FINAL.md`.

По главе IV выполнена отдельная проверка против `work/atlas/articles/spdd_method.md` и `work/dossiers/SPDD_METHOD_DOSSIER.md`. Вывод зафиксирован в `work/theory-writing/reports/CHAPTER_IV_SPDD_ATLAS_ALIGNMENT_REVIEW.md`: глава IV в целом последовательна, но SPDD раскрыт слабее, чем позволяет Атлас. Для будущей ручной правки нужно усилить REASONS Canvas, человеческое ревью намерения, проверку результата по Canvas, `prompt-update` / `sync`, работу со старым кодом без исходной спецификации и визуальный слой.


## Глава IV: интеграция ручной SPDD-редакции V4 — 2026-06-14

Текущая версия главы IV находится здесь:

```text
work/theory-writing/chapters/IV_spdd_specification_lifecycle.md
```

Она заменяет пакетный результат и последующие промежуточные SPDD-патчи. В редакции V4 усилено объяснение SPDD как спецификационного жизненного цикла: зачем он нужен, что он решает и как REASONS Canvas, генерация, проверки, code review, `prompt-update` и `sync` работают в одном цикле.

Ключевая правка V4: пример биллинга введён прямо в главу и теперь достаточно предметен для чтения без внешней реконструкции. В тексте есть API `POST /usage/quote`, клиент, модель, токены, тарифы, квота, валюта, версия тарифа и спорные правила обработки ошибок/округления.

Связанные файлы:

```text
work/theory-writing/chapters/IV_spdd_specification_lifecycle_atlas_usage.md
work/theory-writing/chapters/IV_spdd_specification_lifecycle_degradation_and_duplication_audit.md
work/theory-writing/chapters/IV_spdd_specification_lifecycle_dossier_gap_notes.md
work/theory-writing/chapters/IV_spdd_specification_lifecycle_external_discovery_log.md
work/theory-writing/chapters/IV_spdd_specification_lifecycle_figure_candidates.md
work/theory-writing/chapters/IV_spdd_specification_lifecycle_fragment_usage.md
work/theory-writing/chapters/IV_spdd_specification_lifecycle_open_questions.md
work/theory-writing/chapters/IV_spdd_specification_lifecycle_passes/
work/theory-writing/chapters/IV_spdd_specification_lifecycle_readiness_report.md
work/theory-writing/chapters/IV_spdd_specification_lifecycle_source_register.md
work/theory-writing/chapters/IV_spdd_specification_lifecycle_story_anchors.md
content/assets/theory-images/fowler-spdd-workflow.svg
work/theory-writing/reports/CHAPTER_IV_SPDD_RESULT_V4_INTEGRATION_REPORT.md
work/theory-writing/reports/CHAPTER_IV_SPDD_PATCH_APPLY_REPORT.md
work/theory-writing/reports/CHAPTER_IV_SPDD_CYCLE_LANGUAGE_REBALANCE_REPORT.md
work/theory-writing/reports/CHAPTER_IV_BILLING_EXAMPLE_THREAD_PATCH_REPORT.md
work/theory-writing/reports/CHAPTER_IV_BILLING_EXAMPLE_RECONSTRUCTION_PATCH_REPORT.md
```

Перед применением overlay удалить старый каталог проходов главы IV:

```text
work/theory-writing/chapters/IV_spdd_specification_lifecycle_passes/
```


## Глава I: интеграция принятого nostage-результата — 2026-06-14

В файловую систему добавлена принятая nostage-версия главы I:

```text
work/theory-writing/chapters/I_unit_of_analysis.md
```

Также добавлены сопутствующие файлы и каталог проходов:

```text
work/theory-writing/chapters/I_unit_of_analysis_*.md
work/theory-writing/chapters/I_unit_of_analysis_passes/
```

Источник интеграции — пользовательский архив `CHAPTER_I_UNIT_OF_ANALYSIS_NOSTAGE_RESULT.zip`. По доступным файлам это пакетный результат без отдельной ручной редакции после генерации; глава ранее была принята как canonical nostage prose result, но не была внесена в текущий каталог `work/theory-writing/chapters/`.

Перед применением overlay удалить старый каталог проходов главы I, если он уже есть:

```text
work/theory-writing/chapters/I_unit_of_analysis_passes/
```

Отчёт:

```text
work/theory-writing/reports/CHAPTER_I_RESULT_INTEGRATION_REPORT.md
```


## Update — Chapter IV V6 current version

- `work/theory-writing/chapters/IV_spdd_specification_lifecycle.md` — current integrated Chapter IV text after the V6 natural Russian pass.
- `work/theory-writing/reports/CHAPTER_IV_RESULT_V6_FS_INTEGRATION_REPORT.md` — integration note and workflow correction.
- `work/DELETE_PATHS_CHAPTER_IV_RESULT_V6_INTEGRATION.txt` — path to remove before applying this overlay.


## Update — Chapter IV V7 direct API example patch

- `work/theory-writing/chapters/IV_spdd_specification_lifecycle.md` — current integrated Chapter IV text after direct rewriting of the billing API example.
- `work/theory-writing/reports/CHAPTER_IV_DIRECT_API_EXAMPLE_V7_REPORT.md` — report for the local in-place patch.

The billing example now starts from `POST /usage/quote` as a concrete API method and directly states the input fields, output fields, data sources and error/rounding rules. This replaces the earlier indirect presentation where the reader had to reconstruct the task from the phrase "calculate model usage cost".

## Chapter VI routes / MCP interface patch — 2026-06-15

Current integrated Chapter VI file:

```text
work/theory-writing/chapters/VI_context_working_state_interface.md
```

The `Маршруты действия` part was restructured. The former large nested subsections are now top-level chapter sections:

```text
## Маршруты действия: как проект выбирает способ работы
## Skills: повторяемые процедуры как часть проекта
## MCP-сервер: управляемый внешний интерфейс
## Subagents: разные исполнители для разных частей задачи
```

The MCP section was expanded from a general access/context explanation into a technical external-interface explanation grounded in the official MCP specification: host/client/server, JSON-RPC, initialization, capability negotiation, `stdio`, Streamable HTTP, `resources`, `prompts`, `tools`, and discovery/call methods such as `tools/list`, `tools/call`, `resources/read`, `prompts/get`.

Report:

```text
work/theory-writing/reports/CHAPTER_VI_ROUTES_AND_MCP_INTERFACE_PATCH_REPORT.md
```

## Chapter VI hooks source expansion patch — 2026-06-15

Current integrated Chapter VI file remains:

```text
work/theory-writing/chapters/VI_context_working_state_interface.md
```

The local MCP paragraph that referred to an old wording about “MCP gives context” was rewritten so the chapter no longer comments on its own draft history. The text now directly distinguishes `resources`, `prompts`, and `tools` as different external-interface forms.

The hooks section was expanded with external technical sources and practical usage patterns. The chapter now cites official Claude Code, Codex, Kiro, and Gemini CLI materials and presents hooks as a lifecycle layer: contextual input at session/prompt time, policy checks before action, post-action repair/verification, stop/finalization gates, and audit/observability.

Report:

```text
work/theory-writing/reports/CHAPTER_VI_HOOKS_SOURCE_EXPANSION_PATCH_REPORT.md
```

## Chapter VI route selection and natural Russian pass — 2026-06-15

Current integrated Chapter VI file remains:

```text
work/theory-writing/chapters/VI_context_working_state_interface.md
```

The section `Маршруты действия: как проект выбирает способ работы` has been expanded from a short transition into a functional argument node. It now explains route-selection failure, criteria for choosing between skill, MCP, subagent and hook, route combinations, and the requirement that the chosen route leaves a trace in working state.

The whole Chapter VI text has also passed a natural Russian rewrite. This pass preserved the previously added MCP and hooks technical material and existing inline external links, while reducing protocol-like phrasing, awkward translation residue and avoidable English glue. No new external sources were added in this pass.

Report:

```text
work/theory-writing/reports/CHAPTER_VI_ROUTE_SELECTION_AND_NATURAL_RU_PASS_REPORT.md
```


## Chapter VI external image candidate discovery — 2026-06-15

Current integrated Chapter VI file remains unchanged:

```text
work/theory-writing/chapters/VI_context_working_state_interface.md
```

A source/asset discovery report was added for Chapter VI:

```text
work/theory-writing/reports/CHAPTER_VI_EXTERNAL_IMAGE_CANDIDATES_REPORT.md
```

The report scans the external sources currently referenced by Chapter VI and the recent Chapter VI patch reports. It identifies likely illustration candidates for a future visual pass: route-selection, skills progressive disclosure, MCP external-interface structure, hooks lifecycle / hook resolution, subagents versus agent teams, and optional current-practice screenshots from field reports. The chapter text was not changed in this pass.

- `work/theory-writing/chapters/VI_context_working_state_interface.md` — текущая файловая версия главы VI; теперь включает шесть встроенных локальных иллюстраций из `content/assets/theory-images/` (project interface, route selection, skills, MCP, subagents, hooks).
