# Target-group plan: A2. Стек агентского исполнения

Статус: план для будущего исполнительного пакета.  
Статья: `A2. Стек агентского исполнения: рабочие поверхности, среды выполнения и выбор между ними`.  
Article id: `agent_execution_stack`.  
Основание: Skeleton V6.3, Atlas V2, `ATLAS_V2_LARGE_SYNTHETIC_ARTICLE_BLUEPRINT.md`.

## 1. Назначение статьи

Статья должна объяснить современный стек агентского исполнения как набор разных рабочих форм, а не как список продуктов. Читателю нужно увидеть, что агентская работа может жить в чате, терминале, IDE, облачной среде, среде вокруг спецификации, открытой рабочей обвязке, графовой среде выполнения, многоагентной системе, слое наблюдаемости или возобновляемом процессе с участием человека.

Главный вопрос статьи: где живёт агентская работа и какие последствия имеет выбранная среда. Разные формы по-разному распределяют действие, состояние, права, видимость хода работы, проверку, переносимость, стоимость и роль человека.

Статья пишется как самостоятельная публичная статья Атласа. Она должна держать общую рамку agentic development и быть понятной читателю, который не знает внутренней истории проекта. Теория позже возьмёт из статьи свой срез для вступительной карты поля, глав VII–XI и заключения.

## 2. Главные риски

1. Статья может стать каталогом инструментов: Claude Code, Codex, Cursor, Kiro, OpenHands, LangGraph и так далее. Это недопустимо. Инструменты нужны как фактура для объяснения рабочих форм.
2. Статья может натянуть все технологии на одну сравнительную таблицу. Это тоже плохо: технологии находятся на разных уровнях стека и не всегда конкурируют напрямую.
3. Статья может смешать рабочую поверхность, среду выполнения, интерфейс между агентом и компьютером, многоагентную оркестрацию, наблюдаемость и проверку. Эти различения нужно удержать явно.
4. Статья может уйти во внутренний проектный контекст вместо публичной карты современного стека. Этого нельзя делать: текст должен оставаться самостоятельным материалом сайта.
5. Статья может оказаться слишком гладкой и без фактуры. Для каждого важного блока нужны первичные источники, технические детали, ограничения, UI/diagram candidates или research anchors.

## 3. Обрабатываемые файлы

```yaml
group_mode: linked-target-edit
files:
  - path: work/atlas/articles/agent_execution_stack.md
    status: future
    role: primary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Основная публичная статья Атласа V2."
  - path: work/atlas/articles/agent_execution_stack_source_usage.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Реестр внешних и внутренних источников, реально использованных в статье и мини-досье."
  - path: work/atlas/articles/agent_execution_stack_source_transfer_ledger.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Журнал решений о переносе фактуры: что вошло в статью, что осталось в мини-досье, что отложено."
  - path: work/atlas/articles/agent_execution_stack_image_plan.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "План изображений и решений по визуальным кандидатам."
  - path: work/atlas/articles/agent_execution_stack_external_image_queue.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Очередь внешних реальных изображений для будущего asset-pass."
  - path: work/atlas/articles/agent_execution_stack_open_questions.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Открытые вопросы, слабые места источников и решения, сознательно отложенные из статьи."
  - path: work/atlas/articles/agent_execution_stack_theory_links.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Связи статьи с Skeleton V6.3, главами теории и существующими статьями Атласа."
  - path: work/atlas/articles/agent_execution_stack_degradation_and_duplication_audit.md
    status: future
    role: diagnostic-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Проверка, что статья не стала каталогом, повтором теории или механическим обзором продуктов."
  - path: work/atlas/articles/agent_execution_stack_readiness_report.md
    status: future
    role: diagnostic-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Итоговая готовность статьи и companion-файлов."
  - path: work/atlas/articles/agent_execution_stack_synthesis_design.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Проект сшивки мини-досье в статью: главный ход, порядок разделов, переходы, что переносится и что остаётся за пределами статьи."
  - path: work/atlas/articles/agent_execution_stack_MANIFEST.md
    status: future
    role: diagnostic-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Список выходных файлов и краткое назначение каждого."
  - path: work/atlas/articles/agent_execution_stack_VERIFY.md
    status: future
    role: diagnostic-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Проверка выполнения очереди и готовности результата."
  - path: work/atlas/articles/agent_execution_stack_RESUME.md
    status: future
    role: diagnostic-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Короткая записка для возобновления работы, если пакет остановлен или результат требует repair."
  - path: work/atlas/articles/agent_execution_stack_mini_dossiers/01_terminal_and_local_agents.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о терминальных и локальных агентах."
  - path: work/atlas/articles/agent_execution_stack_mini_dossiers/02_ide_agents.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье об IDE-агентах и средах вокруг редактора."
  - path: work/atlas/articles/agent_execution_stack_mini_dossiers/03_cloud_issue_to_pr_agents.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье об облачных агентских режимах, которые берут задачу и возвращают PR."
  - path: work/atlas/articles/agent_execution_stack_mini_dossiers/04_app_builder_surfaces.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о средах сборки приложения и end-to-end app-builder формах."
  - path: work/atlas/articles/agent_execution_stack_mini_dossiers/05_spec_driven_surfaces.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о средах, построенных вокруг спецификаций."
  - path: work/atlas/articles/agent_execution_stack_mini_dossiers/06_open_harnesses_and_aci.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье об открытых рабочих обвязках и agent-computer interface."
  - path: work/atlas/articles/agent_execution_stack_mini_dossiers/07_graph_and_agent_runtimes.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о LangGraph, OpenAI Agents SDK, Google ADK и близких средах выполнения."
  - path: work/atlas/articles/agent_execution_stack_mini_dossiers/08_multi_agent_orchestration.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о многоагентной оркестрации."
  - path: work/atlas/articles/agent_execution_stack_mini_dossiers/09_observability_and_evaluation.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о наблюдаемости, трассировке и автоматических оценках."
  - path: work/atlas/articles/agent_execution_stack_mini_dossiers/10_durable_workflow_and_human_in_loop.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о возобновляемых рабочих процессах и участии человека."
```

## 4. Файлы для чтения

### Управляющие документы

```text
START.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V6_3_ACCEPTED.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md
work/theory-writing/reports/ATLAS_V2_STRUCTURE_AND_ARTICLE_STATUS.md
work/theory-writing/reports/FIELD_MAP_COMPETITIVE_TECHNOLOGY_CHOICE_UPDATE_2026_06_16.md
work/theory-writing/reports/AGENTIC_AI_COVERAGE_AUDIT_2026_06_16.md
work/theory-writing/reports/practical_agentic_dev_field_map_2026_06_16/PRACTICAL_AGENTIC_DEV_FIELD_MAP_REPORT.md
work/theory-writing/reports/practical_agentic_dev_field_map_2026_06_16/SOURCE_BIBLIOGRAPHY.md
work/theory-writing/reports/practical_agentic_dev_field_map_2026_06_16/SOURCE_COVERAGE_MATRIX.md
work/theory-writing/reports/practical_agentic_dev_field_map_2026_06_16/ATLAS_ARTICLE_QUEUE.md
work/atlas/plans/ATLAS_V2_LARGE_SYNTHETIC_ARTICLE_BLUEPRINT.md
work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
```

### Протоколы языка, источников и изображений

```text
protocols/rules/russian-language.md
protocols/rules/language-style-rules.md
protocols/rules/terminology-and-translation.md
protocols/rules/conceptual-translation-glossary.md
protocols/rules/human-technical-style.md
protocols/rules/english-source-handling.md
protocols/rules/source-and-provenance.md
protocols/rules/content-preservation.md
protocols/rules/fragment-defect-analysis-and-repair.md
protocols/rules/visual-assets-and-figures.md
```

### Существующие статьи Атласа и связанные материалы

```text
work/atlas/articles/kiro_specs.md
work/atlas/articles/kiro_specs_source_usage.md
work/atlas/articles/kiro_specs_image_plan.md
work/atlas/articles/spec_kit_method.md
work/atlas/articles/spec_kit_method_source_usage.md
work/atlas/articles/spdd_method.md
work/atlas/articles/spdd_method_source_usage.md
work/atlas/articles/persistent_work_graph.md
work/atlas/articles/persistent_work_graph_source_usage.md
work/atlas/articles/gas_town.md
work/atlas/articles/gas_town_source_usage.md
work/atlas/articles/gsd_open_gsd.md
work/atlas/articles/bmad_method.md
work/atlas/articles/adr_method.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
```

### Теория, карты и визуальные материалы

```text
work/theory-writing/fragments/00_spine_map.md
work/theory-writing/fragments/A6_execution_environment_distinctions.md
work/theory-writing/fragments/A7_observation_vs_evidence.md
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
work/theory-writing/fragments/A10_mode_selection_map.md
work/theory-writing/fragments/A10_mode_selection_matrix.md
work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
content/Cross_story_synthesis.md
content/Theoretical_synthesis.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

## 5. Стартовые внешние источники

Исполнитель должен открывать первичные источники по мере работы над соответствующим мини-досье, а не читать весь список сразу. Внешний поиск разрешён и обязателен там, где источник устарел, недостаточен или ведёт к более точной первичной странице.

### Терминальные и локальные агенты

```text
https://claude.com/product/claude-code
https://docs.anthropic.com/en/docs/claude-code
https://developers.openai.com/codex/cli
https://github.com/openai/codex
https://aider.chat/docs/
https://github.com/aider-ai/aider
https://ampcode.com/manual
```

### IDE-агенты и редакторные среды

```text
https://cursor.com/docs
https://junie.jetbrains.com/docs/
https://www.jetbrains.com/junie/
https://github.com/JetBrains/junie
https://docs.github.com/copilot
```

### Облачные агенты до PR

```text
https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent
https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions
https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/
https://jules.google/
https://jules.google/docs/
https://developers.openai.com/codex/integrations/github
```

### Среды сборки приложения

```text
https://docs.replit.com/references/agent/overview
https://docs.replit.com/build/welcome
```

### Среды вокруг спецификаций

```text
https://kiro.dev/
https://kiro.dev/docs/specs/
https://kiro.dev/docs/specs/feature-specs/
https://kiro.dev/docs/specs/best-practices/
https://kiro.dev/docs/steering/
https://kiro.dev/docs/hooks/
https://kiro.dev/docs/mcp/
```

### Open harnesses и agent-computer interface

```text
https://swe-agent.com/latest/
https://github.com/swe-agent/swe-agent
https://github.com/SWE-agent/SWE-agent/blob/main/docs/background/aci.md
https://arxiv.org/abs/2405.15793
https://github.com/OpenHands/OpenHands
https://docs.openhands.dev/sdk
https://github.com/OpenHands/software-agent-sdk/
```

### Graph/runtime frameworks

```text
https://docs.langchain.com/oss/python/langgraph/overview
https://docs.langchain.com/oss/python/langgraph/interrupts
https://docs.langchain.com/oss/python/langchain/human-in-the-loop
https://openai.github.io/openai-agents-python/agents/
https://openai.github.io/openai-agents-python/tracing/
https://openai.github.io/openai-agents-python/handoffs/
https://adk.dev/
https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/adk
```

### Многоагентная оркестрация

```text
https://microsoft.github.io/autogen/stable//index.html
https://github.com/microsoft/autogen
https://www.microsoft.com/en-us/research/project/autogen/
https://docs.crewai.com/
https://docs.crewai.com/en/introduction
https://www.llamaindex.ai/workflows
https://developers.llamaindex.ai/typescript/framework/modules/agents/agent_workflow/
```

### Наблюдаемость, оценки и участие человека

```text
https://docs.langchain.com/langsmith/observability
https://openai.github.io/openai-agents-python/tracing/
https://docs.temporal.io/ai-cookbook/human-in-the-loop-python
https://www.humanlayer.dev/
```

### Эмпирический фон и близкие исследования

```text
https://arxiv.org/abs/2602.09185
https://arxiv.org/abs/2601.15195
https://arxiv.org/abs/2606.13468
https://arxiv.org/abs/2606.05548
https://arxiv.org/abs/2511.03690
```

## 6. Очередь рабочих prompt-ов

### P01 — контракт статьи, границы и карта мини-досье

```text
Прочитай сначала:
- START.md
- work/discourse.md
- work/theory-writing/WORKING_DOCUMENTS_MAP.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V6_3_ACCEPTED.md
- work/theory-writing/reports/ATLAS_V2_STRUCTURE_AND_ARTICLE_STATUS.md
- work/atlas/plans/ATLAS_V2_LARGE_SYNTHETIC_ARTICLE_BLUEPRINT.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Создай стартовые файлы целевой группы и зафиксируй контракт статьи `agent_execution_stack`.

Нужно записать:
- какую задачу выполняет статья в Атласе V2;
- почему она не является каталогом инструментов;
- какие мини-досье будут собраны;
- какие мини-досье должны быть крупными, а какие могут быть короче;
- какие локальные углы усиления заданы для каждого мини-досье;
- какие источники входят в стартовый source seed.

Пиши создаваемый текст естественным русским языком. Не делай выводов о личном процессе автора или о Новой. Запиши результат в `agent_execution_stack_open_questions.md`, `agent_execution_stack_source_usage.md` и начальные разделы companion-файлов.
```

### P02 — мини-досье: терминальные и локальные агенты

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack_source_usage.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по Claude Code, Codex CLI, Aider и Amp. Собери мини-досье о терминальных и локальных агентах.

Локальные углы усиления:
- агент работает рядом с локальным деревом проекта, командной строкой, файлами и тестами;
- быстрый цикл действия может давать силу, но переносит на пользователя вопросы прав, окружения и проверки;


Внутри прохода сделай основной поиск, первый сбор, русскую перепись, альтернативный поиск по найденным ссылкам, добор материала, локальное усиление, ещё одну русскую перепись и фиксацию кандидатов для изображений. Не превращай досье в таблицу сравнения. В конце коротко ответь на три вопроса: что эта форма добавляет, какой участок жизненного цикла меняет, с чем пересекается или конкурирует.

Запиши результат в `agent_execution_stack_mini_dossiers/01_terminal_and_local_agents.md`, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue` и `open_questions`.
```

### P03 — мини-досье: IDE-агенты

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack_mini_dossiers/01_terminal_and_local_agents.md
- work/atlas/articles/agent_execution_stack_source_usage.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по Cursor, JetBrains Junie, GitHub Copilot в IDE и близким редакторным формам. Собери мини-досье об IDE-агентах.

Локальные углы усиления:
- IDE-агент работает внутри среды понимания кода и навигации по проекту;
- человек часто остаётся рядом с правкой, но часть анализа, запуска и проверки переходит агенту;


Собери материал полным циклом: основной поиск, черновик, русская перепись, альтернативный поиск, добор, локальное усиление, русская перепись, visual candidates. В конце зафиксируй, как IDE-агенты отличаются от терминальных и облачных режимов.

Запиши результат в `agent_execution_stack_mini_dossiers/02_ide_agents.md` и обнови companion-файлы.
```

### P04 — мини-досье: облачные агенты от задачи к PR

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack_mini_dossiers/01_terminal_and_local_agents.md
- work/atlas/articles/agent_execution_stack_mini_dossiers/02_ide_agents.md
- work/atlas/articles/agent_execution_stack_source_usage.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по GitHub Copilot cloud agent, Jules, Codex/GitHub integration и близким issue-to-PR режимам. Собери мини-досье об облачных агентах, которые берут задачу, работают в отдельной среде и возвращают PR или review.

Локальные углы усиления:
- работа переносится из локального цикла в фоновую или облачную среду;
- результат возвращается через PR, review, CI и журнал сессии;
- автономия увеличивается, но возрастает цена постановки задачи, видимости и review.

Собери материал полным циклом, включая alternative search и visual candidates. Обрати внимание на то, какие детали среды видит пользователь и где проходит граница между выполнением и принятием.

Запиши результат в `agent_execution_stack_mini_dossiers/03_cloud_issue_to_pr_agents.md` и обнови companion-файлы.
```

### P05 — мини-досье: среды сборки приложения

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack_source_usage.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по Replit Agent и близким app-builder формам. Собери короткое, но фактурное мини-досье о средах, где агентская работа подаётся как путь от идеи к работающему приложению.

Локальные углы усиления:
- такая среда объединяет постановку, генерацию, запуск, публикацию и часть отладки;
- она может быть удобна для нового приложения, но плохо совпадает с работой над зрелым репозиторием;


Собери материал полным циклом, но не раздувай досье, если источники дают только продуктовый уровень. В конце явно укажи, почему этот блок нужен статье и почему он не должен стать её центром.

Запиши результат в `agent_execution_stack_mini_dossiers/04_app_builder_surfaces.md` и обнови companion-файлы.
```

### P06 — мини-досье: среды вокруг спецификаций

```text
Прочитай сначала:
- work/atlas/articles/kiro_specs.md
- work/atlas/articles/kiro_specs_source_usage.md
- work/atlas/articles/spec_kit_method.md
- work/atlas/articles/spdd_method.md
- work/dossiers/KIRO_SPECS_DOSSIER.md
- work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
- work/atlas/articles/agent_execution_stack_source_usage.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по Kiro specs, Spec Kit и близким spec-driven поверхностям. Собери мини-досье о средах, где агентская работа строится вокруг requirements, design, tasks, steering и approval points.

Локальные углы усиления:
- спецификация становится рабочей поверхностью, а не предварительным документом;
- среда ведёт пользователя через требования, дизайн и задачи;


Не переписывай уже существующую статью Kiro. Используй её как опору и покажи, какую роль spec-driven поверхности играют именно в статье о стеке исполнения.

Запиши результат в `agent_execution_stack_mini_dossiers/05_spec_driven_surfaces.md` и обнови companion-файлы.
```

### P07 — проверка первой рабочей группы мини-досье

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack_mini_dossiers/01_terminal_and_local_agents.md
- work/atlas/articles/agent_execution_stack_mini_dossiers/02_ide_agents.md
- work/atlas/articles/agent_execution_stack_mini_dossiers/03_cloud_issue_to_pr_agents.md
- work/atlas/articles/agent_execution_stack_mini_dossiers/04_app_builder_surfaces.md
- work/atlas/articles/agent_execution_stack_mini_dossiers/05_spec_driven_surfaces.md
- work/atlas/articles/agent_execution_stack_source_usage.md
- work/atlas/articles/agent_execution_stack_open_questions.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md

Проверь первую рабочую группу мини-досье. Не пиши статью. Оцени, не стала ли работа каталогом продуктов, достаточно ли фактуры, какие различения уже видны, какие досье нужно поправить или усилить и какие вопросы надо сохранить для следующих групп.

Пиши создаваемый текст естественным русским языком. Запиши результат в `agent_execution_stack_open_questions.md`, `source_transfer_ledger` и `RESUME.md`. Если нужен короткий ремонт одного из мини-досье, внеси его сразу и зафиксируй причину.
```

### P08 — мини-досье: open harnesses и agent-computer interface

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack_source_usage.md
- work/atlas/articles/agent_execution_stack_open_questions.md
- content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по SWE-agent, OpenHands, OpenHands Software Agent SDK и Aider там, где он выступает как открытая рабочая обвязка. Собери мини-досье об open harnesses и agent-computer interface.

Локальные углы усиления:
- агент является пользователем компьютерной среды и нуждается в подходящем интерфейсе;
- shell, файлы, тесты, навигация по репозиторию, журнал действий и sandbox становятся частью качества агентской работы;


Собери материал полным циклом. Особое внимание удели paper / docs по SWE-agent ACI и документации OpenHands SDK. В конце укажи, чем open harness отличается от IDE, терминального агента и runtime framework.

Запиши результат в `agent_execution_stack_mini_dossiers/06_open_harnesses_and_aci.md` и обнови companion-файлы.
```

### P09 — мини-досье: графовые и агентские среды выполнения

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack_source_usage.md
- work/atlas/articles/agent_execution_stack_open_questions.md
- work/atlas/articles/persistent_work_graph.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по LangGraph, OpenAI Agents SDK и Google ADK. Собери мини-досье о графовых и агентских средах выполнения.

Локальные углы усиления:
- среда выполнения управляет ходом агентского процесса, состоянием выполнения, sessions, handoffs, interrupts, tools и human-in-the-loop;
- состояние выполнения не равно рабочему состоянию проекта;


Собери материал полным циклом. Не превращай досье в tutorial по API. В конце явно разведи runtime state, trace, work state и accepted change.

Запиши результат в `agent_execution_stack_mini_dossiers/07_graph_and_agent_runtimes.md` и обнови companion-файлы.
```

### P10 — мини-досье: многоагентная оркестрация

```text
Прочитай сначала:
- work/atlas/articles/gas_town.md
- work/atlas/articles/gas_town_source_usage.md
- work/atlas/articles/agent_execution_stack_source_usage.md
- work/atlas/articles/agent_execution_stack_open_questions.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по AutoGen, CrewAI и LlamaIndex Workflows. Собери мини-досье о многоагентной оркестрации.

Локальные углы усиления:
- несколько агентов могут делить работу, роли и сообщения, но это не автоматически даёт управляемую разработку;
- оркестрация решает часть проблемы координации, но создаёт новые проблемы видимости, ответственности и проверки;


Собери материал полным циклом. Отдельно отметь, где AutoGen/CrewAI/LlamaIndex действительно относятся к разработке программных изменений, а где являются общими agent frameworks.

Запиши результат в `agent_execution_stack_mini_dossiers/08_multi_agent_orchestration.md` и обнови companion-файлы.
```

### P11 — мини-досье: наблюдаемость и оценки

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack_source_usage.md
- work/atlas/articles/agent_execution_stack_open_questions.md
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по LangSmith, OpenAI tracing, ADK evaluation и близким слоям наблюдаемости. Собери мини-досье о трассировке, наблюдаемости и оценках агентских прогонов.

Локальные углы усиления:
- след выполнения помогает увидеть, что делал агент;
- trace, eval и benchmark не равны доказательству корректности изменения;


Собери материал полным циклом. Визуальные кандидаты здесь особенно важны: trace views, run views, dashboard screenshots, diagrams. Не вставляй изображения без asset classification.

Запиши результат в `agent_execution_stack_mini_dossiers/09_observability_and_evaluation.md` и обнови companion-файлы.
```

### P12 — мини-досье: возобновляемый workflow и участие человека

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack_source_usage.md
- work/atlas/articles/agent_execution_stack_open_questions.md
- content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
- content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по HumanLayer-like patterns, Temporal human-in-the-loop examples и workflow engines там, где они помогают понять возобновляемую агентскую работу. Собери мини-досье о долгих процессах, подтверждениях человека и контрольных точках.

Локальные углы усиления:
- участие человека может быть runtime-событием, approval gate, обратной связью или решением о продолжении;
- долгий процесс требует сохранения состояния, возобновления и понятной точки ожидания;


Собери материал полным циклом. В конце разведи human-in-the-loop как runtime pattern, review как проверку результата и acceptance как право принять изменение.

Запиши результат в `agent_execution_stack_mini_dossiers/10_durable_workflow_and_human_in_loop.md` и обнови companion-файлы.
```

### P13 — проверка полноты мини-досье и точечный добор

```text
Прочитай сначала:
- все файлы `work/atlas/articles/agent_execution_stack_mini_dossiers/*.md`
- work/atlas/articles/agent_execution_stack_source_usage.md
- work/atlas/articles/agent_execution_stack_source_transfer_ledger.md
- work/atlas/articles/agent_execution_stack_open_questions.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Проверь все мини-досье как корпус будущей статьи. Определи, достаточно ли материала для synthesis design, не пропущен ли важный класс технологий, не нужно ли сделать точечный добор по одному узкому месту.

Если точечный добор нужен, выполни его сразу: открой первичные источники, добавь материал в соответствующее мини-досье и companion-файлы, затем перепиши затронутый фрагмент естественным русским языком.

Не пиши основную статью. Запиши решение о готовности к сшивке в `agent_execution_stack_open_questions.md`, `source_transfer_ledger` и `RESUME.md`.
```

### P14 — synthesis design

```text
Прочитай сначала:
- все файлы `work/atlas/articles/agent_execution_stack_mini_dossiers/*.md`
- work/atlas/articles/agent_execution_stack_source_usage.md
- work/atlas/articles/agent_execution_stack_source_transfer_ledger.md
- work/atlas/articles/agent_execution_stack_open_questions.md
- work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V6_3_ACCEPTED.md
- work/theory-writing/reports/ATLAS_V2_STRUCTURE_AND_ARTICLE_STATUS.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md

Сделай проект сшивки статьи. Не пиши статью.

Нужно решить:
- что стало видно после мини-досье;
- какие технологии идут последовательно, а какие действительно конкурируют;
- какие уровни стека нужно развести;
- какой главный ход статьи;
- порядок разделов;
- мосты между разделами;
- что из каждого мини-досье берётся в основную линию;
- что остаётся только примером или companion-материалом;
- где нужны изображения;
- какие различения должны быть явно видны в статье.

Пиши создаваемый текст естественным русским языком. Запиши результат в `agent_execution_stack_synthesis_design.md` и обнови `theory_links`, `image_plan`, `open_questions`.
```

### P15 — первый цельный черновик статьи

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack_synthesis_design.md
- все файлы `work/atlas/articles/agent_execution_stack_mini_dossiers/*.md`
- work/atlas/articles/agent_execution_stack_source_usage.md
- work/atlas/articles/agent_execution_stack_image_plan.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Напиши первый цельный черновик статьи `agent_execution_stack.md` по synthesis design. Мини-досье используй как источник фактуры, а не как готовые блоки для склейки.

Статья должна читаться самостоятельно. Она должна объяснять стек агентского исполнения как слой современной агентской разработки: рабочие поверхности, среды выполнения, open harnesses, runtime frameworks, многоагентность, наблюдаемость и участие человека. Не превращай статью в список продуктов и не делай выводов о личном процессе автора или о Новой.

Ссылки на внешние источники ставь сразу по месту утверждения. Пиши создаваемый текст естественным русским языком. Обнови companion-файлы по мере использования материала.
```

### P16 — русская перепись и anti-catalog pass

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- work/atlas/articles/agent_execution_stack_synthesis_design.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md

Перечитай статью и перепиши её естественным русским языком. Затем проверь, не стала ли она каталогом продуктов.

Если статья перечисляет инструменты без общей линии, перестрой проблемные разделы: покажи, какую рабочую форму они раскрывают, как она устроена и какой участок жизненного цикла изменения меняет. Сохраняй фактуру, источники и технические детали.

Запиши исправленную статью и короткую запись в `degradation_and_duplication_audit.md`.
```

### P17 — проход на различения

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- work/atlas/articles/agent_execution_stack_synthesis_design.md
- work/atlas/articles/persistent_work_graph.md
- work/theory-writing/fragments/A6_execution_environment_distinctions.md
- work/theory-writing/fragments/A7_observation_vs_evidence.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md

Проверь и усили различения: рабочая поверхность, среда выполнения, open harness, runtime state, рабочее состояние проекта, trace, проверка, полномочие, review, принятие. Исправь места, где статья смешивает эти вещи.

Пиши создаваемый и исправляемый текст естественным русским языком. Обнови `theory_links`, `open_questions` и audit-файл.
```

### P18 — проход на источники и фактическую плотность

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- work/atlas/articles/agent_execution_stack_source_usage.md
- work/atlas/articles/agent_execution_stack_source_transfer_ledger.md
- protocols/rules/source-and-provenance.md
- protocols/rules/english-source-handling.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md

Проверь фактическую плотность статьи. Сильные утверждения должны иметь первичные источники. Если раздел остался общей прозой без технической опоры, открой нужные первичные источники, добавь фактуру и поставь ссылки по месту утверждения.

Не добавляй новые темы ради широты. Исправляй только те места, где статья не держит собственный аргумент. Пиши создаваемый текст естественным русским языком. Обнови `source_usage`, `source_transfer_ledger` и `open_questions`.
```

### P19 — визуальный проход

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- work/atlas/articles/agent_execution_stack_image_plan.md
- work/atlas/articles/agent_execution_stack_external_image_queue.md
- work/theory-writing/asset-catalog/FIGURE_ASSET_CATALOG.md
- work/theory-writing/asset-catalog/LOCAL_ASSET_INDEX.md
- work/theory-writing/asset-catalog/EXTERNAL_REAL_IMAGE_CANDIDATES.md
- protocols/rules/visual-assets-and-figures.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md

Проведи визуальный проход. Сначала используй кандидаты, найденные в мини-досье. Выбери только те изображения, которые действительно помогают понять статью: UI рабочей поверхности, workflow, runtime graph, trace view, architecture diagram, issue-to-PR flow или agent-computer interface.

Локальные assets вставляй как настоящие `<figure><img ...></figure>`. Внешние реальные изображения ставь как `external-real-candidate` placeholders и заноси в нижний раздел статьи и external image queue. Собственные схемы создавай только если они нетривиально проясняют связь, которую трудно удержать прозой.

Обнови `agent_execution_stack.md`, `image_plan` и `external_image_queue`.
```

### P20 — public/article structure pass

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- work/theory-writing/reports/ATLAS_V2_STRUCTURE_AND_ARTICLE_STATUS.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/source-and-provenance.md

Проверь статью как публичную статью Атласа. Первый экран должен быстро объяснять, зачем читателю эта статья. Статья должна быть самостоятельной, но не должна заново писать всю теорию агентской разработки.

Убери внутренние формулы, которые выглядят как рабочие заметки. Убедись, что в тексте нет выводов о личном процессе автора или о Новой. Пиши создаваемый текст естественным русским языком.
```

### P21 — companion sync

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- все companion-файлы `work/atlas/articles/agent_execution_stack_*`
- все файлы `work/atlas/articles/agent_execution_stack_mini_dossiers/*.md`
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md
- protocols/rules/russian-language.md

Синхронизируй companion-файлы с текущей статьёй. Проверь, что source usage, source transfer ledger, image plan, external image queue, open questions, theory links и audit-файл не противоречат статье и не содержат устаревших решений.

Создай или обнови `MANIFEST.md`, `VERIFY.md` и `RESUME.md`. Пиши создаваемый текст естественным русским языком.
```

### P22 — общий редакторский repair 1

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- work/atlas/articles/agent_execution_stack_synthesis_design.md
- work/atlas/articles/agent_execution_stack_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/fragment-defect-analysis-and-repair.md

Оцени, насколько статья выполняет поставленную задачу. Сначала сформулируй проблемы, затем исправь их. Не сужай проход заранее до стиля, источников или изображений: смотри на функцию статьи целиком.

После правки сделай короткий regression audit: что изменилось, какие риски сняты, что осталось. Пиши создаваемый текст естественным русским языком.
```

### P23 — общий редакторский repair 2

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- work/atlas/articles/agent_execution_stack_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/human-technical-style.md
- protocols/rules/fragment-defect-analysis-and-repair.md

Перечитай статью после первого repair. Снова оцени, насколько она выполняет задачу: не стала ли она каталогом, не потеряла ли фактуру, не смешала ли уровни стека, не стала ли слишком общей или слишком продуктовой.

Сначала сформулируй проблемы, затем исправь их. Пиши создаваемый текст естественным русским языком. Обнови audit и readiness notes.
```

### P24 — style defect audit

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/human-technical-style.md

Проведи стилевой аудит без массовой переписи. Найди реальные дефекты: кальки, тяжёлые цепочки родительного падежа, псевдотермины, протокольные формулы, неестественные заголовки, англоязычный клей, слишком гладкие места без точного смысла.

Запиши список дефектов и предложи выборочную правку. Не меняй статью целиком на этом проходе.
```

### P25 — selective natural rewrite

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- work/atlas/articles/agent_execution_stack_degradation_and_duplication_audit.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/human-technical-style.md

Исправь только те места, которые style defect audit признал реально плохими. Переписывай текст естественным русским языком, но не выбрасывай фактуру, источники, технические детали, ограничения и различения ради гладкости.

Обнови статью и audit-файл.
```

### P26 — финальная проверка и готовность

```text
Прочитай сначала:
- work/atlas/articles/agent_execution_stack.md
- все companion-файлы `work/atlas/articles/agent_execution_stack_*`
- все файлы `work/atlas/articles/agent_execution_stack_mini_dossiers/*.md`
- work/atlas/plans/ATLAS_V2_LARGE_SYNTHETIC_ARTICLE_BLUEPRINT.md
- work/theory-writing/reports/ATLAS_V2_STRUCTURE_AND_ARTICLE_STATUS.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Проверь финальный результат.

Должно быть верно:
- основной файл статьи существует и читается самостоятельно;
- статья не является каталогом продуктов;
- статья не делает выводов о личном процессе автора или о Новой;
- технологии раскрыты на своих основаниях;
- выбор между режимами появляется там, где режимы действительно конкурируют;
- источники стоят по месту утверждения;
- visual candidates обработаны через image plan и external image queue;
- companion-файлы синхронизированы;
- все целевые файлы созданы или получили явный blocked status.

Запиши `agent_execution_stack_readiness_report.md`, `VERIFY.md`, `MANIFEST.md` и `RESUME.md`. Пиши создаваемый текст естественным русским языком.
```

## 7. Заметки для сборщика пакета

Target-group plan остаётся единой логической очередью. Стадии выполнения задаются не здесь, а в служебной meta-записке пакета.

Для текущего A2-пакета мини-досье нужно выполнить тремя рабочими группами:

1. `06_open_harnesses_and_aci`, `09_observability_and_evaluation`, `10_durable_workflow_and_human_in_loop`.
2. `05_spec_driven_surfaces`, `07_graph_and_agent_runtimes`, `08_multi_agent_orchestration`.
3. `01_terminal_and_local_agents`, `02_ide_agents`, `03_cloud_issue_to_pr_agents`, `04_app_builder_surfaces`.

После трёх групп отдельный завершающий блок строит карту отношений, проект сшивки, статью и ремонтные отчёты. Не нужно возвращать в план объяснения о техническом разбиении работы; это обязанность сборщика пакета.

Внутри каждого мини-досье нужно сохранить полный цикл: первичные источники, первый черновик, переписывание естественным русским языком с использованием словаря, альтернативный поиск, общий добор, локальные доборы, ограничения, визуальные кандидаты, маршрутизация лишнего материала и итоговое переписывание. Нельзя сворачивать это в один рабочий лист.
