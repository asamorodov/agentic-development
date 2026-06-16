# P03 — первичный source register для главы VIII

Статус: начальный реестр. Он фиксирует, какие источники уже входят в пакет, какую функцию они могут выполнить в главе, какие внешние ссылки нужно раскрыть или перепроверить перед основным письмом. Это не финальный `source_usage` и не полный список ссылок.

## 1. Управляющие внутренние документы

| Источник | Функция в главе | Статус использования |
|---|---|---|
| `PUBLIC_CONTRACT.md` | Открытый контракт пакета: глава VIII пишет про переход от состояния работы к правильному способу продолжения. | Использовать как рамку, не цитировать в публичном тексте. |
| `SELECTED_INPUTS_MANIFEST.md` | Проверяет состав self-contained корпуса и отсутствие missing named inputs. | Использовать для completeness check. |
| `REPOSITORY_START_SNAPSHOT.md` | Восстановление режима работы с репозиторием, источниками и baseline. | Использовать как рабочую дисциплину, не как источник главы. |
| `work/theory-writing/WORKING_DOCUMENTS_MAP.md` | Карта документов, роли Атласа/досье/историй/скелетона, правило root-shaped overlay. | Использовать для навигации и closeout. |
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V5_POST_ATLAS.md` | Непосредственная рамка главы VIII: GSD/Open GSD, BMAD, границы с PWG/Gas Town/IX. | Главная композиционная опора. |
| `work/theory-writing/fragments/00_spine_map.md` | Поперечная карта lifecycle carriers: specification, decision memory, PWG, execution environment, evidence, repair. | Использовать для связи главы с общей теорией. |
| `work/theory-writing/reports/POST_ATLAS_CHAPTER_LIST_AND_SCOPE_MAP.md` | Scope главы: «Когда процесс становится артефактом, а не церемонией?», discovery `D2`. | Использовать для защиты границ. |
| `work/theory-writing/reports/POST_ATLAS_CHAPTER_PACKAGE_INPUT_MATRIX.md` | Обязательные входы: A5/B3/C2, GSD/BMAD/Gas Town, story anchors. | Использовать как coverage checklist. |
| `work/theory-writing/reports/POST_ATLAS_ATLAS_TO_CHAPTER_ROUTING_MAP.md` | Разводит primary/boundary-only/secondary статьи Атласа. | Использовать против дублирования. |
| `work/theory-writing/reports/POST_ATLAS_FRAGMENT_TO_CHAPTER_ROUTING_MAP.md` | Уточняет роли A5/B3/C2. | Использовать как карту доноров. |
| `work/theory-writing/reports/POST_ATLAS_DOSSIER_TO_CHAPTER_GAP_MAP.md` | Указывает обязательные досье и их gaps. | Использовать для добора деталей. |
| `work/theory-writing/reports/POST_ATLAS_STORY_ANCHOR_ROUTING_MAP.md` | Story anchors для VIII: Jesse, HumanLayer, Mae, Shopify, Matt. | Использовать для коротких фактических якорей. |
| `work/theory-writing/reports/POST_ATLAS_EXTERNAL_SOURCE_DISCOVERY_MAP.md` | Для VIII: GSD/BMAD mostly Atlas, но нужны current docs and adjacent profiles. | Использовать как search brief. |
| `work/theory-writing/reports/POST_ATLAS_VISUAL_CANDIDATE_ROUTING_MAP.md` | Визуальные кандидаты для VIII. | Использовать позже только при наличии смысловой функции. |
| `work/theory-writing/reports/POST_ATLAS_PER_CHAPTER_TARGET_PLAN_BLUEPRINT.md` | Общие правила для chapter packages: source register, image plan, audits, no fake empty reports. | Использовать как процедурную рамку. |

## 2. Внутренние фрагменты теории

| Источник | Функция в главе | Риск |
|---|---|---|
| `work/theory-writing/fragments/A5_process_methodologies_synthesis.md` | Главный предтекст: процесс становится артефактом, если удерживает состояние работы и переживает разрывы. Даёт базовые различения GSD/BMAD/PWG/Gas Town. | Не переписать A5 механически; глава должна стать самостоятельным развитием. |
| `work/theory-writing/fragments/A5_source_usage.md` | Проверка, какие внешние источники уже были использованы в A5. | Использовать для provenance, но не как замену чтения источников. |
| `work/theory-writing/fragments/A5_story_anchor_map.md` | Какие истории уже привязаны к теме процессных методологий. | Не перегружать историю внутри главы. |
| `work/theory-writing/fragments/A5_figure_candidates.md` | Потенциальные фигуры process profile / GSD / BMAD. | Нужен отдельный image decision later. |
| `work/theory-writing/fragments/A5_open_questions.md` | Открытые вопросы по процессам. | Использовать для gap-check. |
| `work/theory-writing/fragments/A5_degradation_and_duplication_audit.md` | Риски деградации и повторов. | Использовать в редакторском проходе. |
| `work/theory-writing/fragments/C2_pwg_to_process_profiles.md` | Ключевая граница: PWG vs process profiles vs Gas Town. | Не превращать VIII обратно в главу о PWG. |
| `work/theory-writing/fragments/C2_source_usage.md` | Локальная provenance по C2. | Проверить ссылки при переносе фактов. |
| `work/theory-writing/fragments/C2_story_anchor_map.md` | Истории для границы PWG/process. | Использовать выборочно. |
| `work/theory-writing/fragments/C2_degradation_and_duplication_audit.md` | Предупреждения по повтору и смешению понятий. | Использовать при редактуре. |
| `work/theory-writing/fragments/B3_gas_town_beyond_pwg.md` | Верхняя граница: Gas Town как организация многих агентов, а не просто процесс. | Не увести VIII в X. |
| `work/theory-writing/fragments/B3_source_usage.md` | Provenance по Gas Town / Beads. | Использовать для точных ссылок. |
| `work/theory-writing/fragments/B3_degradation_and_duplication_audit.md` | Риски словарного шума Gas Town. | Использовать при language pass. |

## 3. Статьи Атласа

| Источник | Функция в главе | Внешние ссылки, которые могут понадобиться в тексте |
|---|---|---|
| `work/atlas/articles/gsd_open_gsd.md` | Основной концептуальный источник по GSD/Open GSD: фазовая петля, `.planning/`, роли агентов, политика выполнения, verification/ship, граница с PWG. | [Open GSD](https://www.opengsd.net/), [the-phase-loop.md](https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md), [artifact-types.md](https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md), [gsd-planner.md](https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md), [gsd-plan-checker.md](https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md), [gsd-executor.md](https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md), [GSD User Guide](https://www.opengsd.net/docs/v1/user-guide), [GSD Configuration](https://opengsd.net/docs/v1/configuration), [Auto Mode](https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md), [gsd-pi Configuration](https://www.opengsd.net/docs/v2/configuration). |
| `work/atlas/articles/bmad_method.md` | Основной концептуальный источник по BMAD: role/process profile, документы и статусы, story lifecycle, human checkpoints, correct-course, brownfield, retrospective. | [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD), [Workflow Map](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md), [Official Modules](https://docs.bmad-method.org/reference/modules/), [Core Tools](https://docs.bmad-method.org/reference/core-tools/), [bmad-sprint-status SKILL](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-status/SKILL.md), [bmad-dev-story SKILL](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md), [Workflow Map Diagram](https://docs.bmad-method.org/workflow-map-diagram.html). |
| `work/atlas/articles/gas_town.md` | Boundary source: Gas Town/Beads как организационно-операционный слой над PWG и process profiles. | [Gas Town README](https://github.com/gastownhall/gastown), [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04), [Beads Documentation](https://gastownhall.github.io/beads/), [Gas Town architecture docs](https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md), [Beads Routing](https://gastownhall.github.io/beads/multi-agent/routing), [`bd prime`](https://gastownhall.github.io/beads/cli-reference/prime), [`bd gate`](https://gastownhall.github.io/beads/cli-reference/gate). |
| `work/atlas/articles/gsd_open_gsd_theory_links.md` | Already extracted theory links for GSD. | Использовать для source-to-claim alignment. |
| `work/atlas/articles/bmad_method_theory_links.md` | Already extracted theory links for BMAD. | Использовать для source-to-claim alignment. |
| `work/atlas/articles/gas_town_theory_links.md` | Already extracted theory links for Gas Town. | Использовать для границ с X. |
| `work/atlas/articles/*_source_usage.md` | Existing source usage records. | Проверить перед финальным source usage. |
| `work/atlas/articles/*_image_plan.md`, `*_external_image_queue.md` | Потенциальные изображения. | Использовать только если конкретная фигура улучшает главу. |
| `work/atlas/articles/*_open_questions.md` | Открытые вопросы по GSD/BMAD/Gas Town. | Использовать для gap log. |

## 4. Методологические досье

| Источник | Функция в главе | Что брать |
|---|---|---|
| `work/dossiers/GSD_METHOD_DOSSIER.md` | Фактический резерв по GSD. | `context rot`, потеря состояния, фазы, `.planning/`, `gsd-pi`, forced verification, recovery, риски церемониальности и inert artifacts. |
| `work/dossiers/BMAD_METHOD_DOSSIER.md` | Фактический резерв по BMAD. | Фазы, roles, artifacts-as-inputs, `sprint-status`, story lifecycle, human approvals, correct-course, brownfield, investigate, retrospective, risks. |
| `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | Boundary/gap-check по Gas Town/Beads. | Beads as durable work state, gates, prime, routing, two-tier state, service roles. Только для границы, не для разворачивания X. |
| `work/story_dossiers/SHOPIFY_ROAST_STORY_DOSSIER.md` | Дополнительный фактический резерв для executable workflow. | Использовать точечно, если нужен контраст between process profile and workflow engine. |

## 5. Истории

| История | Функция в главе | Ссылки / provenance |
|---|---|---|
| `content/stories/06_jesse_vincent_agentic_workflow_reconstruction_connected.md` | Главный фактический якорь: ручной процесс становится exoskeleton, skills, hard gates, hooks, real-scenario tests. | [My agentic coding methodology of June 2025](https://blog.fsck.com/2025/06/24/my-agentic-coding-methodology-of-june-2025/), [How I'm using coding agents in September, 2025](https://blog.fsck.com/2025/10/05/how-im-using-coding-agents-in-september-2025/), [Superpowers](https://blog.fsck.com/2025/10/09/superpowers/), [Using GraphViz for CLAUDE.md](https://blog.fsck.com/2025/09/29/using-graphviz-for-claudemd/), [Superpowers v4.3.0](https://blog.fsck.com/agent-blog/2026/02/12/superpowers-v4-3-0/), [Superpowers v5.0.1](https://blog.fsck.com/agent-blog/2026/03/10/superpowers-v5-0-1/), [Rules and Gates](https://blog.fsck.com/2026/04/07/rules-and-gates/). |
| `content/stories/07_human_layer_agentic_harness_reconstruction_connected.md` | Harness around research/plan/implement; context budget and durable process expectations. | Использовать локальную историю как fact base; внешние ссылки раскрывать only if needed in source pass. |
| `content/stories/11_mae_capozzi_maximum_deep_reconstruction_connected.md` | Team/platform wrapper and social-technical state. | Использовать как вторичный anchor. |
| `content/stories/15_shopify_roast_executable_ai_workflow_reconstruction_connected.md` | Executable workflow steps and replay as adjacent runtime example. | Использовать только для короткого контраста. |
| `content/stories/12_matt_pocock_skills_maximum_deep_reconstruction_connected.md` | Skills as process memory and artifact-producing procedures. | [mattpocock/skills](https://github.com/mattpocock/skills), [5 Agent Skills I Use Every Day](https://www.aihero.dev/5-agent-skills), [`grill-with-docs/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/engineering/grill-with-docs/SKILL.md), [`to-prd/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-prd/SKILL.md), [`to-issues/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-issues/SKILL.md), [`triage/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/engineering/triage/SKILL.md), [`handoff/SKILL.md`](https://github.com/mattpocock/skills/blob/main/skills/productivity/handoff/SKILL.md). |

## 6. Внешние источники для раскрытия в discovery-pass

### GSD / Open GSD

| Источник | Предполагаемая функция |
|---|---|
| [Open GSD](https://www.opengsd.net/) | Общая рамка проекта и продуктовая поверхность. |
| [GSD User Guide](https://www.opengsd.net/docs/v1/user-guide) | Фазы, команды, human checkpoints, verify/ship. |
| [the-phase-loop.md](https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/the-phase-loop.md) | Первичная формулировка фазовой петли. |
| [context-engineering.md](https://raw.githubusercontent.com/open-gsd/gsd-core/main/docs/explanation/context-engineering.md) | Проблема context rot and external state. |
| [artifact-types.md](https://github.com/open-gsd/get-shit-done-redux/blob/main/get-shit-done/references/artifact-types.md) | Какие файлы состояния существуют и кто их должен читать. |
| [gsd-planner.md](https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-planner.md) | Роль planner как producer executable plan. |
| [gsd-plan-checker.md](https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-plan-checker.md) | Проверка плана и статусы `PASS` / revision / blocked. |
| [gsd-executor.md](https://raw.githubusercontent.com/open-gsd/gsd-core/main/agents/gsd-executor.md) | Executor, atomic task, stopping conditions, output. |
| [GSD Configuration](https://opengsd.net/docs/v1/configuration) | Models, tools, safety, stop policy. |
| [Auto Mode](https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md) | Recovery/autonomy boundary; likely bridge to IX. |

### BMAD

| Источник | Предполагаемая функция |
|---|---|
| [BMAD Method GitHub](https://github.com/bmad-code-org/BMAD-METHOD) | Основной репозиторий и current docs entry. |
| [Official Modules](https://docs.bmad-method.org/reference/modules/) | Установка/модули, чтобы не выдумывать структуру. |
| [Workflow Map](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/docs/reference/workflow-map.md) | Фазы и цепочка артефактов. |
| [Workflow Map Diagram](https://docs.bmad-method.org/workflow-map-diagram.html) | Возможный визуальный источник. |
| [Core Tools](https://docs.bmad-method.org/reference/core-tools/) | `bmad-spec`, core tool surface. |
| [bmad-sprint-status SKILL](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-sprint-status/SKILL.md) | State machine for stories/epics. |
| [bmad-dev-story SKILL](https://raw.githubusercontent.com/bmad-code-org/BMAD-METHOD/main/src/bmm-skills/4-implementation/bmad-dev-story/SKILL.md) | Implementation story workflow and allowed state updates. |
| `bmad-create-story`, `bmad-correct-course`, `bmad-investigate`, brownfield docs | Нужно раскрыть в discovery-pass; ссылки частично есть в Атласе/досье, но нужно проверить exact paths. |

### Boundary / соседние sources

| Источник | Предполагаемая функция |
|---|---|
| [Beads docs](https://gastownhall.github.io/beads/) | Критерий durable work state. |
| [bd prime](https://gastownhall.github.io/beads/cli-reference/prime) | Восстановление контекста. |
| [bd gate](https://gastownhall.github.io/beads/cli-reference/gate) | Durable gate as boundary with PWG. |
| [Welcome to Gas Town](https://steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04) | Верхняя граница: organization beyond profile. |
| [Gas Town architecture docs](https://github.com/gastownhall/gastown/blob/main/docs/design/architecture.md) | Town/rig and routing boundary. |
| Reversa / OpenSpec / AgentSPEX | Использовать только если later discovery покажет, что они дают missing distinction. Пока не primary. |

## 7. Правила переноса ссылок

- В основном тексте ссылка ставится в месте первого переноса факта, а не в финальном списке.
- Если факт уже есть в статье Атласа, но происходит из внешнего источника, публичный текст должен ссылаться на внешний источник, а не на рабочую статью.
- Досье и routing reports можно использовать как quarry и контроль, но не как публичные источники факта.
- Если внешний source не удалось раскрыть или он устарел/не подтверждает тезис, это нужно фиксировать в external discovery log, а не заменять собственной уверенной формулировкой.
