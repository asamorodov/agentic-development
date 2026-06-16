# VIII — source register

Статус: заполнено по текущему тексту `10_10_full_draft.md` после P14. Реестр отражает фактически использованные источники, а не исходный план добора.

## Внутренние фрагменты и карты

| Источник | Как использован в главе | Статус |
|---|---|---|
| `work/theory-writing/fragments/00_spine_map.md` | Позиционирование главы между долговечным состоянием работы, средой исполнения и организационной средой. | used_in_structure |
| `work/theory-writing/fragments/C2_pwg_to_process_profiles.md` | Центральное различение: PWG показывает, где находится работа, но не выбирает следующий режим. | used_in_main_argument |
| `work/theory-writing/fragments/A5_process_methodologies_synthesis.md` | Материал для GSD/BMAD как процессных методик, которые задают фазы, роли, входы и выходы. | used_in_method_sections |
| `work/theory-writing/fragments/B3_gas_town_beyond_pwg.md` | Верхняя граница главы: Gas Town/Beads относятся к организации множества линий работы, а не к выбору режима одного узла. | used_in_boundary_section |
| `work/theory-writing/reports/POST_ATLAS_*` | Использовались как routing-карта: какие досье, атласные статьи и stories должны питать главу VIII. | used_for_routing |

## Atlas / dossiers

| Источник | Как использован | Статус |
|---|---|---|
| `work/atlas/articles/gsd_open_gsd.md` and `work/dossiers/GSD_METHOD_DOSSIER.md` | GSD как способ восстановления длинной агентской работы: route selection, phase loop, `.planning/`, fresh contexts, specialist agents, Verify/Ship boundary, `gsd-pi` bridge to execution environment. | used_in_GSD_section |
| `work/atlas/articles/bmad_method.md` and `work/dossiers/BMAD_METHOD_DOSSIER.md` | BMAD как фазовая передача контекста: Workflow Map, `bmad-help`, `bmad-create-story`, `bmad-correct-course`, `project-context.md`, `bmad-investigate`. | used_in_BMAD_section |
| `work/atlas/articles/gas_town.md` and `work/dossiers/GAS_TOWN_METHOD_DOSSIER.md` | Gas Town/Beads как верхняя граница: организационная среда для множества рабочих линий. | used_in_boundary_section |

## Внешние источники, использованные в основном тексте

| Источник | Где использован | Что поддерживает |
|---|---|---|
| [Open GSD](https://docs.opengsd.net/) | GSD-раздел | Общая рамка Open GSD как рабочего цикла с планами, свежими контекстами, проверкой и историей изменений. |
| [GSD Core — The Phase Loop](https://github.com/firescrawl/gsd-core/blob/main/docs/explanation/the-phase-loop.md) | GSD-раздел | Discuss → UI design when needed → Plan → Execute → Verify → Ship как фазовая защита работы. |
| [GSD Core — Quickstart](https://docs.opengsd.net/gsd-core/tutorials/quickstart) | GSD-раздел | Инициализация `.planning/`, утверждение roadmap, сохранение состояния между сессиями. |
| [GSD Core — Planning Artifacts](https://docs.opengsd.net/gsd-core/explanation/planning-artifacts) | GSD-раздел | `PROJECT.md`, `REQUIREMENTS.md`, `STATE.md`, `CONTEXT.md`, `PLAN-*.md`, `VERIFICATION-*.md`, `UAT-*.md` как рабочие артефакты. |
| [GSD Core — Specialist Agents](https://docs.opengsd.net/gsd-core/explanation/specialist-agents) | GSD-раздел | Fresh contexts, scoped tasks, limited tool permissions, роли planner/plan-checker/executor/verifier. |
| [GSD User Guide](https://www.opengsd.net/docs/v1/user-guide) | GSD-раздел | Маршрутизация рабочих потоков: не каждый случай требует полного фазового цикла; GSD выбирает режим продолжения. |
| [gsd-pi Configuration](https://www.opengsd.net/docs/v2/configuration) | GSD-раздел | GSD на границе со средой исполнения: сессии, конфигурация, политика инструментов и локальное состояние. |
| [GSD Auto Mode](https://raw.githubusercontent.com/open-gsd/gsd-pi/main/docs/user-docs/auto-mode.md) | GSD-раздел | Автоматический режим как управляемое продолжение с состояниями, остановками, надзором и проверкой. |
| [BMAD Workflow Map](https://docs.bmad-method.org/reference/workflow-map/) | BMAD-раздел | BMM как четыре фазы; Phase 3/Phase 4; implementation workflows; `bmad-investigate`; context management. |
| [BMAD Getting Started](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/tutorials/getting-started.md) | BMAD-раздел | `bmad-help`, последовательность workflows, `sprint-status.yaml`, story cycle. |
| [BMAD Core Tools](https://docs.bmad-method.org/reference/core-tools/) | BMAD-раздел | `bmad-spec`, `SPEC.md`, `.decision-log`. |
| [BMAD `bmad-create-story` SKILL.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/4-implementation/bmad-create-story/SKILL.md) | BMAD-раздел | Story file как контейнер контекста для dev agent; список предотвращаемых ошибок; чтение sprint status and planning artifacts. |
| [BMAD `bmad-correct-course` SKILL.md](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/src/bmm-skills/4-implementation/bmad-correct-course/SKILL.md) | BMAD-раздел | Change trigger, impact analysis, Sprint Change Proposal, affected artifacts. |
| [BMAD Established Projects FAQ](https://docs.bmad-method.org/explanation/established-projects-faq/) | BMAD brownfield-раздел | document-project for established projects; Quick Flow detects stack/patterns/conventions; choice between existing conventions and modernization. |
| [BMAD Project Context](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/docs/explanation/project-context.md) | BMAD brownfield-раздел | `project-context.md` as implementation guide / constraint file; automatic loading by workflows; existing project generation. |
| [BMAD Forensic Investigation](https://docs.bmad-method.org/explanation/forensic-investigation/) | BMAD investigation-раздел | `bmad-investigate` opens case file instead of fixing; narrative lock-in; evidence amnesia; confirmed/deduced/hypothesized; stronghold; hypothesis status; output file. |
| [Jesse Vincent — Rules and Gates](https://blog.fsck.com/2026/04/07/rules-and-gates/) | Малые профили | Rules/gates, reviewer context boundary, failure mode with removed tests. |
| [HumanLayer — 12 Factor Agents](https://github.com/humanlayer/12-factor-agents) | Малые профили | research → plan → implement, context firewall, hooks/feedback as signals. |
| [Matt Pocock Skills](https://github.com/mattpocock/skills) | Малые профили | `/grill-me`, `/to-prd`, `/to-issues`, `/triage`, `/tdd`, `/handoff`, `/diagnose` as small process profiles. |
| [Beads Documentation](https://gastownhall.github.io/beads/) | Верхняя граница | Work as durable task object: statuses, labels, dependencies, gates, prime. |
| [Gas Town README](https://github.com/gastownhall/gastown) | Верхняя граница | Town/rig/worker environment, queues, handoffs, cleanup as organizational layer beyond one profile. |

## Источники, проверенные, но не перенесённые напрямую

| Источник / группа | Статус | Почему не вошло напрямую |
|---|---|---|
| BMAD official Workflow Map diagram | external-real-candidate only | Слишком BMAD-specific для центральной теоретической главы; остаётся кандидатом для asset-pass. |
| GSD synthetic figures from atlas article | not_reused | Объясняют GSD как метод, а не общий механизм protected process profiles. |
| HumanLayer local story images | not_reused | Полезны для context/harness chapters, но в главе VIII были бы косвенными. |
| Mae Capozzi and Shopify Roast story materials | not_used_in_final_text | Были в исходном routing, но после написания глава удержала ось через Jesse/HumanLayer/Matt; добавление Mae/Shopify расширило бы раздел малых профилей без нового механизма. |
