# Codex readiness check

Дата: 2026-06-08  
Задача: `work/prompts/FIRST_CODEX_READINESS_CHECK_TASK.md`

status: READY_WITH_WARNINGS

documents_read:

- `AGENTS.md`
- `project/repository-structure.md`
- `project/source-precedence.md`
- `project/branching-and-task-model.md`
- `protocols/rules/codex-task-work-protocol.md`
- `protocols/rules/theory-rebuild-rules.md`
- `protocols/rules/language-style-rules.md`
- `protocols/rules/russian-language.md`
- `protocols/rules/english-source-handling.md`
- `protocols/rules/discourse-maintenance-rules.md`
- `work/discourse.md`
- `work/approved-ai-sdlc-plan.md`
- `work/decisions/ADR-0007-sdlc-artifact-and-framework-coverage.md`
- `work/decisions/ADR-0008-protected-methodology-profiles.md`
- `work/reports/METHODOLOGY_DEPTH_CONTRACT.md`
- `work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md`
- `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`
- `work/reports/SKELETON_V4_QUALITY_AUDIT.md`
- `work/reports/CODEX_METHODOLOGY_STAGE_HANDOFF.md`
- `work/prompts/STAGE_0_19_METHOD_PROFILES_CODEX_TASK.md`
- `work/reports/SELECTED_DOSSIERS_QUALITY_AUDIT.md`
- `work/dossiers/GSD_BMAD_PROCESS_FRAMEWORKS_DOSSIER.md`
- `work/source-expansion/stage_0_6/INDEX.md`
- `work/source-expansion/stage_0_7/INDEX.md`
- `work/source-expansion/stage_0_8/INDEX.md`
- `work/source-expansion/stage_0_9/INDEX.md`
- `work/source-expansion/stage_0_12/INDEX.md`

missing_documents:

- none among required core documents.

understanding_summary:

Codex видит текущий worktree, `work/`, `work/discourse.md`, approved AI-driven SDLC plan, ADR-0007, ADR-0008, methodology depth contract, skeleton v4.1, selected dossiers и staged source-expansion materials. Текущий проект больше не пытается полировать expanded theory как main draft. Expanded theory является quarry: она полезна для фактуры, источников и наблюдений, но не является финальной композиционной формой. Активная архитектура — AI-driven SDLC как lifecycle программного изменения.

SPDD и Gas Town являются protected deep anchors. Их нужно восстанавливать из old-site baseline seeds перед адаптацией, и их нельзя сжимать без human gate. Spec Kit, Kiro, Constitutional SDD, оба значения TDAD, GSD и BMAD являются protected methodology profiles: не обязательно deep anchors, но и не shallow mentions. Для них нужны dossiers, которые восстанавливают workflow, artifacts, context, roles, human gates, validation, lifecycle tail, strengths, failure modes, contrasts и theory/Handbook split.

Parts VI-XII не должны стать artifact catalogs. Артефакты являются first-class только тогда, когда несут lifecycle function. Поэтому skeleton v4.1 использует lifecycle tensions и comparative syntheses вместо headings по именам источников или артефактов.

Stage 0.19 — это dossier/pass stage. Он должен создать methodology pass files, final protected methodology dossiers и comparative synthesis reports. Он не должен писать final theory chapters, менять `work/approved-ai-sdlc-plan.md`, менять `/content` или redesign architecture без human gate.

risks:

- Stage 0.19 может потребовать более сильный primary/official source access, чем дают существующие локальные notes.
- Protected profiles могут случайно превратиться в отполированные shallow summaries.
- GSD/BMAD могут быть чрезмерно promoted to deep anchors или, наоборот, недоразвёрнуты как mere mentions.
- Comparative sections могут сжать SPDD/Gas Town вопреки baseline rule.
- Parts VI-XII всё ещё могут сползти к catalog form во время later writing.
- Существующий checks-файл называется `work/checks.json`; prompt называет `work/CHECKS.json`. В этом Windows workspace они разрешаются в один путь, но регистр стоит учитывать осознанно, если репозиторий будет перенесён на case-sensitive filesystem.

recommended_next_task:

- Запустить `work/prompts/STAGE_0_19_METHOD_PROFILES_CODEX_TASK.md` по `work/protocols/METHODOLOGY_DOSSIER_PASS_PROTOCOL.md` после принятия этой readiness check человеком.

human_gates:

- Любой broad new source search или source-access decision.
- Любое изменение `work/approved-ai-sdlc-plan.md`.
- Любое изменение `work/skeletons/THEORETICAL_SYNTHESIS_REBUILT_SKELETON_V4.md`.
- Любая demotion protected methodology profiles.
- Любая promotion GSD/BMAD или adjacent process methods to deep anchors.
- Writing Parts V или VII до появления methodology dossiers.
- Любое compression SPDD или Gas Town against baseline restore rule.

## Выполненные проверки

- Проверены required core files через `Test-Path`.
- Просмотрены `work/`, `work/dossiers/`, `work/reports/`, `work/source-expansion/` и `work/prompts/`.
- Прочитаны source-expansion indexes for Stage 0.6, 0.7, 0.8, 0.9 и 0.12.
- Подтверждено, что worktree был чистым перед созданием readiness artifacts.

## Проверки, которые не выполнялись

- Stage 0.19 не запускался.
- Methodology dossiers и pass files не создавались.
- Final theory chapters не писались и не изменялись.
- `work/approved-ai-sdlc-plan.md` не изменялся.
- `/content` не изменялся.
- Каждый отдельный source-expansion result file не валидировался.
