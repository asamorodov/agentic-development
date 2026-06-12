# Codex document visibility inventory

Дата: 2026-06-08  
Задача: `work/prompts/FIRST_CODEX_READINESS_CHECK_TASK.md`

## Обязательные core-документы

| Документ | Статус | Роль в проверке |
|---|---:|---|
| `AGENTS.md` | found | Корневые правила для Codex и других агентов. |
| `project/repository-structure.md` | found | Карта репозитория и роль `/work`. |
| `project/source-precedence.md` | found | Приоритет источников и статус `work/discourse.md`. |
| `project/branching-and-task-model.md` | found | Модель веток, worktree и рабочей зоны. |
| `protocols/rules/codex-task-work-protocol.md` | found | Операционный протокол Codex-задачи. |
| `protocols/rules/theory-rebuild-rules.md` | found | Guardrails перестройки теории. |
| `protocols/rules/language-style-rules.md` | found | Вход в языковые правила. |
| `protocols/rules/russian-language.md` | found | Обязательное русскоязычное письмо. |
| `protocols/rules/english-source-handling.md` | found | Перенос англоязычных источников в русский текст. |
| `work/discourse.md` | found | Главная смысловая память текущей задачи. |
| `work/approved-ai-sdlc-plan.md` | found | Утверждённая архитектура v4/v4.1. |
| `work/decisions/ADR-0007-sdlc-artifact-and-framework-coverage.md` | found | Решение о слое артефактов и process/framework coverage. |
| `work/decisions/ADR-0008-protected-methodology-profiles.md` | found | Решение о protected methodology profiles. |
| `work/reports/METHODOLOGY_DEPTH_CONTRACT.md` | found | Рабочий контракт глубины методологий. |
| `work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md` | found | Протокол Stage 0.19 для dossiers. |
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` | found | Рабочий skeleton v4.1 перед writing. |
| `work/reports/SKELETON_V4_QUALITY_AUDIT.md` | found | Аудит skeleton с зависимостями от dossiers. |

## Видимость рабочей директории

| Объект | Статус | Наблюдение |
|---|---:|---|
| `work/` | found | Рабочая зона текущей ветки видна. |
| `work/discourse.md` | found | Прочитан как основной источник непрерывности. |
| `work/approved-ai-sdlc-plan.md` | found | Прочитан; менять запрещено текущей задачей. |
| `work/decisions/ADR-0007-sdlc-artifact-and-framework-coverage.md` | found | Прочитан. |
| `work/decisions/ADR-0008-protected-methodology-profiles.md` | found | Прочитан. |
| `work/reports/METHODOLOGY_DEPTH_CONTRACT.md` | found | Прочитан. |
| `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md` | found | Прочитан. |
| `work/dossiers/` | found | Видны selected dossiers/notes. |
| `work/source-expansion/` | found | Видны материалы Stage 0.6, 0.7, 0.8, 0.9 и 0.12. |
| `work/prompts/` | found | Видны readiness prompt и Stage 0.19 prompt. |
| `work/reports/` | found | Видны отчёты Stage 0.5-0.12, skeleton, handoff и audits. |

## Видимые selected dossiers

В `work/dossiers/` видны:

- `ADR_DECISION_PROVENANCE_DOSSIER.md`
- `API_DATA_CONTRACTS_AND_TRACEABILITY_NOTE.md`
- `ARCHITECTURE_QUALITY_AND_FITNESS_FUNCTIONS_NOTE.md`
- `CODEBASE_READINESS_AND_CONTEXT_FILES_NOTE.md`
- `EVIDENCE_PACKAGE_TAXONOMY_NOTE.md`
- `EXECUTION_CONTROL_SURFACES_NOTE.md`
- `GSD_BMAD_PROCESS_FRAMEWORKS_DOSSIER.md`
- `LIFECYCLE_TAIL_ARTIFACTS_NOTE.md`
- `OWNERSHIP_AND_COMPLETION_ARTIFACTS_NOTE.md`
- `TEST_DATA_ENVIRONMENTS_AND_ORACLES_NOTE.md`

Эти dossiers достаточны для понимания skeleton v4, но сами по себе не заменяют protected methodology dossiers, которые должны быть созданы на Stage 0.19.

## Source-expansion materials visible

В `work/source-expansion/` видны:

- `stage_0_6/`: decision provenance, agentic frameworks, lifecycle tail, security/provenance, ownership/completion right.
- `stage_0_7/`: codebase readiness, contracts/interfaces, workflow specification, delivery safety, decision enforcement.
- `stage_0_8/`: requirements traceability, SBOM/supply chain, secrets/sensitive data, observability/agent traces, human review/DevEx.
- `stage_0_9/`: flow/platform, reproducible environment, policy-as-code, prompt/context lifecycle, artifact graph.
- `stage_0_12/`: architecture quality и test data/test environments.

## Отсутствующие документы

Среди обязательных core-документов пропусков нет.

Известные ещё не созданные выходные файлы Stage 0.19 отсутствуют ожидаемо:

- `work/dossiers/SPEC_KIT_METHOD_DOSSIER.md`
- `work/dossiers/KIRO_SPECS_DOSSIER.md`
- `work/dossiers/CONSTITUTIONAL_SDD_DOSSIER.md`
- `work/dossiers/TDAD_COMPARATIVE_DOSSIER.md`
- `work/dossiers/GSD_METHOD_DOSSIER.md`
- `work/dossiers/BMAD_METHOD_DOSSIER.md`
- `work/reports/SPECIFICATION_METHODS_COMPARATIVE_SYNTHESIS.md`
- `work/reports/PROCESS_METHODS_COMPARATIVE_SYNTHESIS.md`

Их отсутствие является причиной Stage 0.19, а не провалом readiness check.
