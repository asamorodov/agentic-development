# Bilingual term registry

Date: 2026-06-17.

This registry is for corpus-level terms whose English/Russian mapping must stay stable across Theory, Atlas, Working Scenarios and Problem/Solution Catalog. It is not a full glossary of every technical word.

## Corpus parts and genres

| ID | Russian working/public term | English working term | Do not translate as | Notes |
|---|---|---|---|---|
| corpus.theory | Теория; possible future `Жизненный цикл программного изменения` | Theory; possible `Lifecycle of Software Change` | not fixed as final branding | `Теория` is current short working label. Future public title may foreground lifecycle. |
| corpus.atlas | Атлас | Atlas | technical appendix | Atlas is a peer major part, not an appendix to Theory. |
| corpus.working_scenarios | Рабочие сценарии; possible `Практикум` | Working Scenarios; Practical Scenarios; Practicum if training-like | Handbook as public Russian | Replaces awkward Russianized `Хандбук` for public-facing Russian. |
| corpus.problem_solution_catalog | Каталог проблем и решений | Problem and Solution Catalog; possible `Failure and Recovery Catalog` | Fieldbook as public Russian | Diagnostic/failure-recovery section. Avoid `Фильдбук` in Russian public text. |
| corpus.stories | Истории; Developer Workflow Stories | Stories; Developer Workflow Stories | — | Story corpus remains evidence/texture path, not necessarily site entrypoint. |

## Projection cuts

| ID | Russian term | English term | Notes |
|---|---|---|---|
| cut.lifecycle | разрез по жизненному циклу изменения | lifecycle-of-change cut | Main cut for Theory. |
| cut.technical_layers | разрез по техническим слоям | technical-layer cut | Main cut for Atlas. |
| cut.practitioner_decisions | разрез по решениям практика | practitioner-decision cut | Main cut for Working Scenarios. |
| cut.failure_modes | разрез по типовым сбоям | failure-mode cut | Main cut for Problem/Solution Catalog. |

## Core agentic-development concepts

| ID | Russian term | English term | Notes |
|---|---|---|---|
| concept.agentic_development | агентская разработка | agentic development | Keep broad; not only coding-agent automation. |
| concept.ai_driven_sdlc | AI-driven SDLC | AI-driven SDLC | Usually keep acronym. |
| concept.change_lifecycle | жизненный цикл изменения | lifecycle of change / software change lifecycle | Central theory axis. |
| concept.change_substrate | субстрат изменения | change substrate | Used for Git/worktree/PR/MR layer. |
| concept.agent_run | агентский прогон / прогон агента | agent run | Avoid Russian `ран`. |
| concept.accepted_change | принятое изменение | accepted change | Not just merged commit; includes decision/status context. |
| concept.verification_material | проверочный материал | verification material / evidence for verification | Do not default to `evidence = доказательство`. |
| concept.trace | след выполнения / трассировка | execution trace / trace | Distinguish broad trace of work from technical tracing. |
| concept.translation_ready | готовность к будущему переводу | translation-readiness | Gate for public stabilization, not actual translation. |
| concept.technical_payload | техническая фактура / technical payload | technical payload | For Atlas acceptance gate. |

## Atlas Level 1 article IDs — working English titles

| ID | Russian title | Working English title |
|---|---|---|
| atlas-a01-project-context-interface | Контекстный интерфейс проекта для агента | Project context interface for agents |
| atlas-a02-coding-agent-work-surfaces | Рабочие поверхности coding agents | Coding-agent work surfaces |
| atlas-a03-agent-orchestration-frameworks | Оркестрация и фреймворки агентского исполнения | Agent orchestration and execution frameworks |
| atlas-a04-tools-protocols-access-authority | Инструменты, протоколы, доступы и полномочия | Tools, protocols, access and authority |
| atlas-a05-observability-traces-evals | Наблюдаемость, traces и evals | Observability, traces and evals |
| atlas-a06-git-worktree-pr-change-substrate | Git, worktree и PR/MR как субстрат агентского изменения | Git, worktrees and PR/MR as the change substrate |
| atlas-a07-ci-review-acceptance-gates | CI, status checks, review и acceptance gates | CI, status checks, review and acceptance gates |
| atlas-a08-specs-plans-process-artifacts | Спецификации, планы и исполняемые процессные артефакты | Specs, plans and executable process artifacts |
| atlas-a09-reproducible-environments-sandboxes | Воспроизводимые среды исполнения и песочницы | Reproducible execution environments and sandboxes |
| atlas-a10-codebase-context-retrieval | Индексация, поиск и извлечение контекста из кодовой базы | Codebase context retrieval, indexing and search |
| atlas-a11-issue-to-agent-task-queue | Issue-to-agent: задачи, очереди, assignment и progress surfaces | Issue-to-agent task queues, assignment and progress surfaces |
| atlas-a12-long-term-project-memory | Долгая память проекта и повторное использование опыта | Long-term project memory and experience reuse |
| atlas-a13-agentic-security-supply-chain | Безопасность агентской разработки и supply-chain controls | Agentic-development security and supply-chain controls |
| atlas-a14-browser-gui-app-feedback | Browser/GUI/app feedback surfaces | Browser, GUI and app feedback surfaces |
| atlas-a15-model-provider-routing-cost | Model/provider layer, routing, cost and inference constraints | Model/provider layer, routing, cost and inference constraints |
| atlas-a16-organizational-context-developer-portal | Организационный контекст, software catalog и developer portal | Organizational context, software catalog and developer portal |

## Notes

This file should be treated as a seed registry. Future packages may expand it or migrate it into a structured YAML/JSON glossary, but this markdown version is enough to prevent avoidable drift during the Russian-first writing phase.
