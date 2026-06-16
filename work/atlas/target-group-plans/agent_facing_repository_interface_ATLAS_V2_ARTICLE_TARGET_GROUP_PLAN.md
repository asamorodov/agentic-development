# Target-group plan: A1. Репозиторий как интерфейс для агента

Статус: план для будущего исполнительного пакета.  
Статья: `A1. Репозиторий как интерфейс для агента`.  
Article id: `agent_facing_repository_interface`.  
Основание: Skeleton V6.3, Atlas V2, `ATLAS_V2_LARGE_SYNTHETIC_ARTICLE_BLUEPRINT.md`, обсуждение больших статей Атласа V2 и опыт плана A2.

## 1. Назначение статьи

Статья должна объяснить, как репозиторий становится интерфейсом для агента. Речь не о том, что в проект добавляют ещё один файл с подсказками. Речь о более широком слое: проект начинает сообщать агенту правила работы, область действия, доступные процедуры, допустимые инструменты, точки остановки, способы делегирования и порядок исправления самих инструкций.

Главный вопрос статьи: где должно жить рабочее знание проекта, чтобы агент мог использовать его как устойчивую часть процесса, а не как случайный фрагмент prompt-а. Одни знания лучше хранить в репозитории, другие — в настройках конкретного инструмента, третьи — в пакете задачи, skill, hook, MCP-конфигурации или отдельной роли subagent. Статья должна показать, что эти формы не равнозначны и не всегда конкурируют напрямую.

Статья пишется как самостоятельный публичный материал Атласа. Она должна быть полезна читателю, который пытается понять современную агентскую разработку и не знает внутренней истории проекта. Теория позже возьмёт из неё свой срез для главы VI, а также для глав IX и XIII.

## 2. Рабочая гипотеза статьи

Репозиторий в агентской разработке перестаёт быть только хранилищем кода и документации. Он становится средой, которая готовит агента к работе: объясняет устройство проекта, задаёт правила изменения, показывает повторяемые процедуры, подключает инструменты и фиксирует, когда агент должен остановиться или передать решение человеку.

Но это не значит, что нужно положить в репозиторий как можно больше инструкций. Избыточные, устаревшие или конфликтующие правила могут ухудшить результат. Поэтому статья должна держать двойной тезис: инструкции и процедуры нужны агенту, но они становятся инженерным артефактом только тогда, когда у них есть область действия, владелец, проверка, возможность удаления и порядок исправления после сбоя.

## 3. Главные риски

1. Статья может стать справочником по файлам: `AGENTS.md`, `CLAUDE.md`, Cursor Rules, GitHub custom instructions, Kiro steering и так далее. Это недопустимо. Файлы и форматы нужны как фактура для объяснения слоя.
2. Статья может стать практическим шаблоном «как написать хороший AGENTS.md». Это полезно для Handbook, но не для Атласа. Атласная статья должна объяснять, какую роль такие файлы играют в жизненном цикле изменения.
3. Статья может смешать разные формы: постоянные инструкции, локальные правила, skills, hooks, subagents, MCP и пакет задачи. Нужно показать, где они дополняют друг друга, а где действительно конкурируют за место рабочего знания.
4. Статья может слишком оптимистично описать инструкции как очевидное улучшение. Нужно явно раскрыть обратную сторону: лишние правила, конфликт областей действия, старение контекста, скрытая зависимость от инструмента и увеличение стоимости работы.
5. Статья может забрать материал будущей A4 о полномочиях и безопасности. В A1 нужно говорить о доступе и интерфейсе, но глубокая тема identity, authorization, secrets, prompt injection и tool poisoning относится к A4.
6. Статья может забрать материал A2 о среде выполнения. В A1 нужно держать проектный интерфейс агента; runtime, cloud execution, open harnesses и наблюдаемость остаются фоном, а не центром.
7. Текст может уйти во внутреннюю проектную записку. Этого делать нельзя: статья должна оставаться самостоятельным публичным материалом сайта.

## 4. Обрабатываемые файлы

```yaml
group_mode: linked-target-edit
files:
  - path: work/atlas/articles/agent_facing_repository_interface.md
    status: future
    role: primary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Основная публичная статья Атласа V2."
  - path: work/atlas/articles/agent_facing_repository_interface_source_usage.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Реестр внешних и внутренних источников, реально использованных в статье и мини-досье."
  - path: work/atlas/articles/agent_facing_repository_interface_source_transfer_ledger.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Журнал решений о переносе фактуры: что вошло в статью, что осталось в мини-досье, что отложено в другие узлы Атласа."
  - path: work/atlas/articles/agent_facing_repository_interface_image_plan.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "План изображений и решений по визуальным кандидатам."
  - path: work/atlas/articles/agent_facing_repository_interface_external_image_queue.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Очередь внешних реальных изображений для будущего asset-pass."
  - path: work/atlas/articles/agent_facing_repository_interface_open_questions.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Открытые вопросы, слабые места источников и решения, сознательно отложенные из статьи."
  - path: work/atlas/articles/agent_facing_repository_interface_theory_links.md
    status: future
    role: supporting-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Связи статьи с Skeleton V6.3, главами теории и существующими статьями Атласа."
  - path: work/atlas/articles/agent_facing_repository_interface_degradation_and_duplication_audit.md
    status: future
    role: diagnostic-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Проверка, что статья не стала каталогом файлов, повтором главы VI или практическим шаблоном вместо Атласа."
  - path: work/atlas/articles/agent_facing_repository_interface_readiness_report.md
    status: future
    role: diagnostic-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Итоговая готовность статьи и сопроводительных файлов."
  - path: work/atlas/articles/agent_facing_repository_interface_relationship_map.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Карта отношений между инструкциями, правилами, procedures, skills, hooks, subagents, MCP и task package."
  - path: work/atlas/articles/agent_facing_repository_interface_synthesis_design.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Проект сшивки мини-досье в статью: главный ход, порядок разделов, переходы, что переносится и что остаётся за пределами статьи."
  - path: work/atlas/articles/agent_facing_repository_interface_MANIFEST.md
    status: future
    role: diagnostic-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Список выходных файлов и краткое назначение каждого."
  - path: work/atlas/articles/agent_facing_repository_interface_VERIFY.md
    status: future
    role: diagnostic-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Проверка выполнения очереди и готовности результата."
  - path: work/atlas/articles/agent_facing_repository_interface_RESUME.md
    status: future
    role: diagnostic-output
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Короткая записка для возобновления работы, если пакет остановлен или результат требует repair."
  - path: work/atlas/articles/agent_facing_repository_interface_mini_dossiers/01_repository_level_context_files.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о repository-level context files: AGENTS.md, agent manifests и близкие формы."
  - path: work/atlas/articles/agent_facing_repository_interface_mini_dossiers/02_tool_specific_instructions.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о CLAUDE.md, Cursor Rules, GitHub Copilot instructions, Codex/Amp instructions и других tool-specific слоях."
  - path: work/atlas/articles/agent_facing_repository_interface_mini_dossiers/03_scope_hierarchy_and_conflicts.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье об области действия инструкций, иерархии, discovery, конфликтах и старении правил."
  - path: work/atlas/articles/agent_facing_repository_interface_mini_dossiers/04_steering_and_spec_context.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о Kiro steering, spec-linked context и проектном контексте, связанном со спецификацией."
  - path: work/atlas/articles/agent_facing_repository_interface_mini_dossiers/05_skills_and_procedural_modules.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о skills, SKILL.md, reusable procedures и процедурной памяти агента."
  - path: work/atlas/articles/agent_facing_repository_interface_mini_dossiers/06_hooks_and_automatic_interventions.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о hooks и автоматических вмешательствах в ход агентской работы."
  - path: work/atlas/articles/agent_facing_repository_interface_mini_dossiers/07_subagents_and_delegation.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о subagents, специализированных ролях и делегировании части работы."
  - path: work/atlas/articles/agent_facing_repository_interface_mini_dossiers/08_mcp_and_tool_access.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о MCP, tool access, resources and prompts как части интерфейса проекта для агента."
  - path: work/atlas/articles/agent_facing_repository_interface_mini_dossiers/09_task_package_as_work_interface.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о task package как переносимом интерфейсе конкретной работы."
  - path: work/atlas/articles/agent_facing_repository_interface_mini_dossiers/10_instruction_quality_and_repair.md
    status: future
    role: secondary
    write_policy: replace-full-file
    result_policy: overlay-path
    notes: "Мини-досье о качестве инструкций, минимальности, устаревании, конфликте правил и ремонте после неудачных прогонов."
```

## 5. Файлы для чтения

### Управляющие документы

```text
START.md
work/discourse.md
work/theory-writing/WORKING_DOCUMENTS_MAP.md
work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V6_3_ACCEPTED.md
work/theory-writing/reports/ATLAS_V2_STRUCTURE_AND_ARTICLE_STATUS.md
work/theory-writing/reports/FIELD_MAP_COMPETITIVE_TECHNOLOGY_CHOICE_UPDATE_2026_06_16.md
work/theory-writing/reports/AGENTIC_AI_COVERAGE_AUDIT_2026_06_16.md
work/theory-writing/reports/practical_agentic_dev_field_map_2026_06_16/PRACTICAL_AGENTIC_DEV_FIELD_MAP_REPORT.md
work/theory-writing/reports/practical_agentic_dev_field_map_2026_06_16/SOURCE_BIBLIOGRAPHY.md
work/theory-writing/reports/practical_agentic_dev_field_map_2026_06_16/SOURCE_COVERAGE_MATRIX.md
work/theory-writing/reports/practical_agentic_dev_field_map_2026_06_16/ATLAS_ARTICLE_QUEUE.md
work/atlas/plans/ATLAS_V2_LARGE_SYNTHETIC_ARTICLE_BLUEPRINT.md
work/atlas/target-group-plans/agent_execution_stack_ATLAS_V2_ARTICLE_TARGET_GROUP_PLAN.md
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
work/atlas/articles/spec_kit_method.md
work/atlas/articles/spdd_method.md
work/atlas/articles/persistent_work_graph.md
work/atlas/articles/adr_method.md
work/atlas/articles/gas_town.md
work/atlas/articles/gsd_open_gsd.md
work/atlas/articles/bmad_method.md
work/dossiers/KIRO_SPECS_DOSSIER.md
work/dossiers/SPEC_KIT_METHOD_DOSSIER.md
work/dossiers/SPDD_METHOD_DOSSIER.md
work/dossiers/PERSISTENT_WORK_GRAPH_MECHANISM_DOSSIER.md
work/dossiers/ADR_METHOD_DOSSIER.md
work/dossiers/GAS_TOWN_METHOD_DOSSIER.md
```

### Теория, карты и истории

```text
work/theory-writing/fragments/00_spine_map.md
work/theory-writing/fragments/A6_execution_environment_distinctions.md
work/theory-writing/fragments/A7_observation_vs_evidence.md
work/theory-writing/fragments/A8_authority_to_act_vs_complete.md
work/theory-writing/fragments/A10_mode_selection_map.md
work/theory-writing/fragments/A10_mode_selection_matrix.md
content/Cross_story_synthesis.md
content/Theoretical_synthesis.md
content/stories/07_human_layer_agentic_harness_reconstruction_connected.md
content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md
content/stories/13_armin_ronacher_pi_minimal_agent_harness_reconstruction_connected.md
content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md
```

## 6. Стартовые внешние источники

Исполнитель открывает первичные источники по мере работы над соответствующим мини-досье. Список ниже — не предел поиска. Если официальный документ ведёт к более точной странице, changelog, репозиторию, paper или связанному guide, нужно открыть и оценить этот источник тоже.

### Repository-level context files и agent manifests

```text
https://agents.md/
https://developers.openai.com/codex/guides/agents-md
https://arxiv.org/abs/2602.11988
https://arxiv.org/abs/2602.14690
https://arxiv.org/abs/2509.14744
https://arxiv.org/html/2606.13449v1
```

### CLAUDE.md, Cursor Rules, GitHub Copilot instructions, Codex/Amp instructions

```text
https://code.claude.com/docs/en/memory
https://cursor.com/docs
https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/your-first-custom-instructions
https://developers.openai.com/codex/guides/agents-md
https://ampcode.com/manual
```

### Scope, hierarchy, discovery and conflicts

```text
https://developers.openai.com/codex/guides/agents-md
https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions/your-first-custom-instructions
https://code.claude.com/docs/en/memory
https://kiro.dev/docs/steering/
https://arxiv.org/abs/2602.11988
```

### Kiro steering and spec-linked context

```text
https://kiro.dev/docs/steering/
https://kiro.dev/docs/specs/
https://kiro.dev/docs/specs/feature-specs/
https://kiro.dev/docs/hooks/
https://kiro.dev/docs/mcp/
https://kiro.dev/docs/powers/
```

### Skills and reusable procedures

```text
https://code.claude.com/docs/en/skills
https://developers.openai.com/codex/skills
https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
https://github.com/anthropics/skills
https://arxiv.org/abs/2602.08004
```

### Hooks and automatic interventions

```text
https://code.claude.com/docs/en/hooks
https://code.claude.com/docs/en/hooks-guide
https://kiro.dev/docs/hooks/
https://kiro.dev/docs/powers/
https://arxiv.org/abs/2604.14228
```

### Subagents and delegation

```text
https://code.claude.com/docs/en/agent-sdk/overview
https://arxiv.org/abs/2604.14228
https://arxiv.org/abs/2602.14690
```

Дополнительно нужно искать официальные страницы Claude Code о subagents. Если найден только вторичный источник, его можно использовать как вспомогательный, но в статье не заменять им первичный источник.

### MCP and tool access

```text
https://modelcontextprotocol.io/specification/2025-06-18
https://modelcontextprotocol.io/docs/getting-started/intro
https://modelcontextprotocol.io/specification/2025-06-18/server/resources
https://kiro.dev/docs/mcp/
https://code.claude.com/docs/en/agent-sdk/overview
```

### Task package и instruction repair

```text
work/atlas/plans/ATLAS_V2_LARGE_SYNTHETIC_ARTICLE_BLUEPRINT.md
work/atlas/target-group-plans/agent_execution_stack_ATLAS_V2_ARTICLE_TARGET_GROUP_PLAN.md
work/protocols/TASK_PACKAGE_CREATION_PROTOCOL.md
work/protocols/THEORY_WRITING_PROMPT_QUEUE_PROTOCOL.md
work/prompts/TARGET_GROUP_PLAN_TEMPLATE.md
https://arxiv.org/abs/2602.11988
https://arxiv.org/abs/2602.14690
https://arxiv.org/html/2606.13449v1
```

## 7. Очередь рабочих инструкций

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

Создай стартовые файлы целевой группы и зафиксируй контракт статьи `agent_facing_repository_interface`.

Нужно записать:
- какую задачу выполняет статья в Атласе V2;
- почему она не является справочником по instruction files;
- какую рабочую гипотезу статья проверяет;
- какие мини-досье будут собраны;
- какие группы мини-досье уже заданы;
- какие локальные углы усиления есть у каждого мини-досье;
- какие источники входят в стартовый source seed.

Группы мини-досье уже заданы в этом плане. Не дели их заново и не объясняй в публичном тексте техническое разбиение работы.

Пиши создаваемый текст естественным русским языком и используй словарь. Запиши результат в `agent_facing_repository_interface_open_questions.md`, `agent_facing_repository_interface_source_usage.md` и начальные разделы остальных сопроводительных файлов.
```

### P02 — мини-досье: repository-level context files

```text
Прочитай сначала:
- work/atlas/articles/agent_facing_repository_interface_source_usage.md
- protocols/rules/russian-language.md
- protocols/rules/language-style-rules.md
- protocols/rules/terminology-and-translation.md
- protocols/rules/conceptual-translation-glossary.md
- protocols/rules/source-and-provenance.md
- protocols/rules/visual-assets-and-figures.md

Открой первичные источники по `AGENTS.md`, Codex `AGENTS.md`, agent manifests и empirical work по context files. Собери мини-досье о repository-level context files как первом слое интерфейса репозитория для агента.

Локальные углы усиления:
- `AGENTS.md` и похожие файлы работают как устойчивое место проектных инструкций, а не как разовый prompt;
- context files могут быть межинструментальным стандартом, но эмпирические исследования показывают, что лишние требования могут ухудшать результат;
- важно различить self-description источника и реальную роль файла в жизненном цикле изменения.

Внутри этого пункта нельзя ограничиваться одним проходом. Нужно открыть первичные источники, собрать фактический черновик, переписать его естественным русским языком с использованием словаря, сделать альтернативный поиск, добрать материал, усилить досье по локальным углам, снова переписать затронутый текст естественным русским языком, зафиксировать ограничения, визуальные кандидаты и маршрутизацию материала в другие узлы Атласа.

Запиши результат в `agent_facing_repository_interface_mini_dossiers/01_repository_level_context_files.md`, обнови `source_usage`, `source_transfer_ledger`, `image_plan`, `external_image_queue` и `open_questions`.
```

### P03 — мини-досье: tool-specific instructions

```text
Открой первичные источники по `CLAUDE.md`, Cursor Rules, GitHub Copilot custom instructions, Codex instructions, Amp instructions и близким tool-specific слоям. Собери мини-досье о том, как разные инструменты размещают проектные правила и память.

Локальные углы усиления:
- tool-specific instructions усиливают конкретный инструмент, но могут снижать переносимость рабочего знания между агентами;
- разные инструменты по-разному разводят user-level, repository-level, workspace-level и path-specific инструкции;
- natural language instructions, rules, memory и configuration files нельзя механически считать одним и тем же.

Работай полным циклом мини-досье: первичные источники, первый черновик, переписывание естественным русским языком с использованием словаря, альтернативный поиск, общий добор, локальное усиление, повторное переписывание затронутого текста, ограничения, визуальные кандидаты и маршрутизация лишнего материала.

Запиши результат в `agent_facing_repository_interface_mini_dossiers/02_tool_specific_instructions.md` и обнови сопроводительные файлы.
```

### P04 — мини-досье: область действия, иерархия и конфликты

```text
Открой источники о discovery, hierarchy, nested instructions, global/project/path-specific rules, fallback filenames и конфликтах инструкций. Собери мини-досье об области действия и поддержке инструкций.

Локальные углы усиления:
- инструкция без области действия быстро превращается в шум;
- иерархия правил может помогать, но создаёт конфликты, старение и скрытые переопределения;
- правило должно иметь владельца, срок актуальности или хотя бы понятный повод для удаления.

Не делай досье юридической схемой приоритетов. Нужно показать инженерную проблему: агент может следовать правилу, но само правило может быть плохим, устаревшим или относящимся не к этой задаче.

Работай полным циклом мини-досье. После добора материала перепиши затронутый текст естественным русским языком, используя словарь.

Запиши результат в `agent_facing_repository_interface_mini_dossiers/03_scope_hierarchy_and_conflicts.md` и обнови сопроводительные файлы.
```

### P05 — мини-досье: steering и контекст, связанный со спецификацией

```text
Открой источники по Kiro steering, specs, hooks, MCP и powers. Используй существующие статьи Kiro / Spec Kit / SPDD как внутреннюю опору, но не переписывай их заново. Собери мини-досье о steering и проектном контексте, связанном со спецификацией.

Локальные углы усиления:
- steering связывает постоянный проектный контекст с конкретным способом вести работу;
- spec-driven surface меняет не только исполнение, но и место, где агент получает требования, дизайн и задачи;
- steering-файлы находятся между инструкцией репозитория, спецификацией и рабочей поверхностью агента.

Собери досье полным циклом. В конце явно укажи, что относится к A1, а что лучше оставить статье Kiro, SPDD или A2.

Запиши результат в `agent_facing_repository_interface_mini_dossiers/04_steering_and_spec_context.md` и обнови сопроводительные файлы.
```

### P06 — мини-досье: skills и повторяемые процедуры

```text
Открой первичные источники по Claude Skills, Codex Skills, `SKILL.md`, Anthropic Agent Skills и анализам skill-экосистемы. Собери мини-досье о skills как форме повторяемой процедуры для агента.

Локальные углы усиления:
- skill отличается от постоянной инструкции: он должен включаться тогда, когда задача требует конкретной процедуры;
- skill может содержать не только текст, но и ресурсы, scripts, examples или tool usage patterns;
- большое число skills создаёт проблему выбора, длины описаний, безопасности и повторов.

Не превращай досье в список skill-платформ. Нужно показать, как procedural memory отличается от context file и почему skill требует своего порядка поддержки.

Работай полным циклом мини-досье и переписывай затронутый текст естественным русским языком, используя словарь.

Запиши результат в `agent_facing_repository_interface_mini_dossiers/05_skills_and_procedural_modules.md` и обнови сопроводительные файлы.
```

### P07 — мини-досье: hooks и автоматические вмешательства

```text
Открой источники по Claude Code hooks, Kiro hooks, powers and hooks-related automation. Собери мини-досье о hooks как точках автоматического вмешательства в ход агентской работы.

Локальные углы усиления:
- hook отличается от инструкции: он не просто говорит агенту, что делать, а запускает действие или проверку в определённой точке жизненного цикла инструмента;
- hooks могут форматировать файлы, блокировать рискованные команды, добавлять контекст, уведомлять человека или вызывать внешнюю проверку;
- hooks полезны только при ясной границе ответственности: что проверяет hook, что остаётся за человеком, что не должно выполняться автоматически.

Не забирай всю тему безопасности из A4. В A1 важно объяснить hook как часть интерфейса проекта для агента и как точку вмешательства, а не как полный контур authorisation.

Работай полным циклом мини-досье. После добора перепиши затронутый текст естественным русским языком, используя словарь.

Запиши результат в `agent_facing_repository_interface_mini_dossiers/06_hooks_and_automatic_interventions.md` и обнови сопроводительные файлы.
```

### P08 — мини-досье: subagents и делегирование

```text
Открой первичные источники по subagents, Claude Code Agent SDK, Claude Code architecture papers и empirical configuration studies. Собери мини-досье о subagents как форме делегирования части работы внутри агентского процесса.

Локальные углы усиления:
- subagent не равен skill: это не только процедура, а отдельная роль, контекст или исполнитель;
- subagents могут уменьшать смешение задач, но создают вопросы передачи контекста, проверки результата и возврата работы в общую картину;
- важно показать связь subagents с интерфейсом репозитория, не превращая досье в статью о многоагентной оркестрации.

Если официальный источник по subagents недостаточен, найди дополнительные первичные или исследовательские источники. Вторичные материалы можно использовать только как вспомогательные.

Работай полным циклом мини-досье и перепиши затронутый текст естественным русским языком, используя словарь.

Запиши результат в `agent_facing_repository_interface_mini_dossiers/07_subagents_and_delegation.md` и обнови сопроводительные файлы.
```

### P09 — мини-досье: MCP и доступ к инструментам

```text
Открой MCP specification, intro, resources/tools/prompts materials, а также источники по MCP в Kiro и Claude/agent SDK context. Собери мини-досье о MCP как части интерфейса между агентом, проектом и внешними ресурсами.

Локальные углы усиления:
- MCP не является инструкцией, но может сделать ресурсы и инструменты частью рабочей среды агента;
- resources, tools и prompts имеют разные функции и не должны смешиваться;
- подключённость не равна праву действовать: глубокая тема полномочий относится к A4, но в A1 нужно показать границу.

Не превращай досье в технический tutorial по MCP. Нужно объяснить, почему MCP важен для репозитория как интерфейса агента: он показывает, что проект может давать агенту не только текстовые правила, но и структурированный доступ к данным и действиям.

Работай полным циклом мини-досье. После добора перепиши затронутый текст естественным русским языком, используя словарь.

Запиши результат в `agent_facing_repository_interface_mini_dossiers/08_mcp_and_tool_access.md` и обнови сопроводительные файлы.
```

### P10 — мини-досье: пакет задачи как переносимый интерфейс работы

```text
Прочитай внутренние протоколы task package, hidden runner, theory writing prompt queue и A2 package plan. Собери мини-досье о пакете задачи как переносимом интерфейсе конкретной работы для агента.

Локальные углы усиления:
- пакет задачи отличается от постоянных инструкций репозитория: он задаёт контекст, границы и материалы для одной конкретной работы;
- пакет может переносить не только prompt, но и источники, рабочие листы, проверочные требования, визуальные кандидаты и правила остановки;
- пакет задачи может быть мостом между публичным project interface и конкретным проходом исполнения.

Не делай досье внутренней историей этого проекта. Нужно описать task package как общую форму agent-facing work interface, пригодную для публичной статьи.

Работай полным циклом мини-досье. После добора перепиши затронутый текст естественным русским языком, используя словарь.

Запиши результат в `agent_facing_repository_interface_mini_dossiers/09_task_package_as_work_interface.md` и обнови сопроводительные файлы.
```

### P11 — мини-досье: качество инструкций и ремонт после сбоя

```text
Открой исследования по AGENTS.md, agentic coding manifests, configuring agentic coding tools, Toward Instructions-as-Code и близким работам. Собери мини-досье о том, почему инструкции нужно не только писать, но и проверять, сокращать, исправлять и удалять.

Локальные углы усиления:
- больше инструкций не значит лучше;
- лишние требования могут снижать успешность, увеличивать стоимость и уводить агента в ненужное исследование;
- после сбоя нужно чинить не только код, но и правило, пакет задачи, skill, hook или область действия инструкции, если именно они стали причиной ошибки;
- ремонт инструкций должен быть отдельной практикой, а не случайной правкой после раздражения.

Это одно из ключевых мини-досье статьи. Оно должно помочь финальному тексту избежать наивного вывода «надо просто написать больше правил для агента».

Работай полным циклом мини-досье. После добора перепиши затронутый текст естественным русским языком, используя словарь.

Запиши результат в `agent_facing_repository_interface_mini_dossiers/10_instruction_quality_and_repair.md` и обнови сопроводительные файлы.
```

### P12 — проверка мини-досье и карта отношений

```text
Прочитай все мини-досье и сопроводительные файлы. Проверь, не было ли мини-досье сделано одним поверхностным проходом. Если где-то не хватает первичных источников, альтернативного поиска, локального добора или переписывания естественным русским языком, зафиксируй это в open questions и, если возможно, исправь до сшивки.

Создай `agent_facing_repository_interface_relationship_map.md`.

В карте отношений нужно развести:
- постоянные инструкции репозитория;
- tool-specific instructions;
- область действия и иерархию правил;
- steering и spec-linked context;
- skills как повторяемые процедуры;
- hooks как точки автоматического вмешательства;
- subagents как роли и делегирование;
- MCP как доступ к ресурсам и инструментам;
- task package как переносимый интерфейс конкретной работы;
- instruction repair как сопровождение самого интерфейса.

Отдельно зафиксируй:
- какие формы реально конкурируют;
- какие лежат на разных уровнях и не должны сравниваться напрямую;
- где один инструмент совмещает несколько форм;
- что лучше перенести в A2, A3, A4, A5 или старые статьи Атласа.

Пиши естественным русским языком и используй словарь.
```

### P13 — проект сшивки статьи

```text
На основе мини-досье и карты отношений создай `agent_facing_repository_interface_synthesis_design.md`.

Не пересказывай мини-досье. Реши, какой текст должен получиться.

В проекте сшивки нужно указать:
- главный тезис статьи;
- порядок разделов;
- какие мини-досье становятся крупными разделами, а какие работают как примеры;
- где нужны переходы между разделами;
- какие источники обязательны для основной статьи;
- какие визуальные кандидаты действительно полезны;
- какие материалы не переносить в публичную статью;
- какие различения статья обязана донести читателю.

Перед переходом к черновику проверь, можно ли пересказать будущую статью одним тезисом, который не сводится к «существуют разные instruction files для агентов».
```

### P14 — первый цельный черновик статьи

```text
Напиши первый цельный черновик `agent_facing_repository_interface.md` по проекту сшивки.

Пиши статью с нуля. Мини-досье являются источником фактуры, а не готовыми кусками статьи. Не склеивай их подряд.

Статья должна объяснить слой целиком: как репозиторий и связанные с ним артефакты начинают задавать агенту правила, процедуры, доступы, роли, точки вмешательства и порядок ремонта. При этом статья должна удержать предупреждение: instruction layer полезен только как поддерживаемый инженерный артефакт, а не как накопление всё большего числа правил.

Ставь ссылки на первичные источники там, где вводится фактический материал.
```

### P15 — переписать черновик естественным русским языком

```text
Перепиши первый черновик естественным русским языком, используя словарь. Не ограничивайся точечной заменой слов.

Особенно проверь:
- не появился ли англоязычный связующий слой;
- не звучит ли текст как документация продукта;
- не стало ли слишком много выражений вроде context files, workflow, setup, instruction layer без русского объяснения;
- не превратились ли `интерфейс`, `процедура`, `доступ`, `полномочие`, `проверка` и `состояние` в расплывчатые слова без функции.
```

### P16 — anti-catalog / anti-template pass

```text
Проверь статью против двух рисков.

Первый риск: статья стала каталогом instruction files и возможностей инструментов. Если да, перестрой текст вокруг главного слоя: репозиторий как интерфейс для агента.

Второй риск: статья стала практическим шаблоном настройки AGENTS.md / CLAUDE.md / Cursor Rules. Если да, верни её в жанр Атласа: объяснить форму и её место в жизненном цикле изменения, а не дать готовый checklist для проекта.

После правки перепиши затронутые фрагменты естественным русским языком, используя словарь.
```

### P17 — проход на различения

```text
Проверь, что статья не смешивает:
- постоянную инструкцию и task package;
- context file и skill;
- skill и subagent;
- hook и проверку человеком;
- MCP и право действовать;
- repository-level instruction и tool-specific memory;
- состояние выполнения и состояние работы проекта;
- инструкцию как текст и инструкцию как поддерживаемый инженерный артефакт.

Если различение не видно в тексте, исправь статью. После правки перепиши затронутые фрагменты естественным русским языком.
```

### P18 — проход по источникам и фактической плотности

```text
Проверь все фактические утверждения и ссылки.

Нужно убедиться, что:
- сильные утверждения о продуктах и форматах опираются на первичные источники;
- исследования используются там, где они действительно поддерживают тезис;
- внутренние досье не подменяют первоисточники в публичной статье;
- source_usage содержит дату просмотра, устойчивость источника, самоописание источника и роль материала в статье;
- source_transfer_ledger фиксирует материал, который лучше перенести в A2, A3, A4, A5 или старые статьи Атласа.
```

### P19 — визуальный проход

```text
Прочитай image_plan и external_image_queue. Выбери, какие визуальные кандидаты действительно помогают статье.

Для A1 возможны:
- screenshot или diagram `AGENTS.md` / Codex discovery;
- screenshot или diagram Claude memory / hooks / skills / subagents;
- screenshot Cursor Rules или GitHub custom instructions;
- Kiro steering / specs / hooks diagram или UI;
- MCP architecture diagram;
- собственная схема только если она действительно проясняет отношения между инструкциями, skills, hooks, subagents, MCP и task package.

Не подменяй готовые реальные изображения текстовыми схемами. Если asset-pass не выполнен, ставь внешний кандидат в очередь, а не вставляй сомнительный материал inline.
```

### P20 — синхронизация сопроводительных файлов

```text
Синхронизируй основную статью и сопроводительные файлы:
- source_usage;
- source_transfer_ledger;
- image_plan;
- external_image_queue;
- open_questions;
- theory_links;
- relationship_map;
- synthesis_design.

Каждый материал, который был найден, но не вошёл в статью, должен иметь понятное решение: оставить в мини-досье, перенести в другой узел Атласа, вернуть при future repair или отклонить.
```

### P21 — общие редакторские repair-проходы

```text
Проведи три общих редакторских repair-прохода:

1. Диагностика структуры: статья держит один ход или распадается на куски?
2. Диагностика полноты: нет ли важного слоя интерфейса репозитория, который потерялся после сжатия мини-досье?
3. Адверсариальная проверка: где статья преувеличивает силу инструкций, скрывает риск старения правил или смешивает разные формы agent-facing interface?

После каждого содержательного исправления переписывай затронутые фрагменты естественным русским языком, используя словарь.
```

### P22 — style defect audit и selective natural rewrite

```text
Проведи style defect audit. Найди фрагменты, где текст звучит как:
- машинная инструкция;
- маркетинговый обзор продукта;
- калька с английской документации;
- слишком абстрактная классификация;
- повтор главы VI вместо самостоятельной статьи Атласа.

Затем перепиши найденные фрагменты естественным русским языком, используя словарь. Переписывай фрагменты заново, а не заменяй отдельные слова.
```

### P23 — guarded final human technical style pass

```text
Проведи финальный технический стилевой проход.

Сохрани точность, ссылки, названия инструментов, имена файлов и важные различения. Убери остаточную тяжесть языка, повторяющиеся формулы и искусственные обороты.

Не делай текст проще за счёт потери различений. Не превращай статью в набор советов. Она должна остаться самостоятельной статьёй Атласа.
```

### Final — готовность, manifest, verify, resume

```text
Создай:
- `agent_facing_repository_interface_degradation_and_duplication_audit.md`
- `agent_facing_repository_interface_readiness_report.md`
- `agent_facing_repository_interface_MANIFEST.md`
- `agent_facing_repository_interface_VERIFY.md`
- `agent_facing_repository_interface_RESUME.md`

Проверь, что:
- все заявленные выходные файлы существуют;
- мини-досье включены в результат;
- статья не является каталогом файлов и инструментов;
- статья не является практическим шаблоном настройки;
- источники стоят по месту фактических утверждений;
- словарь был использован;
- визуальные кандидаты обработаны честно;
- открытые вопросы записаны явно;
- теория сможет взять из статьи срез для главы VI, не копируя Атлас механически.
```
