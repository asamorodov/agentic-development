# Skill: stage-0-5-coverage-audit

## Когда применять

Применяйте этот skill перед написанием глав новой теоретической части, чтобы проверить два поздно обнаруженных слоя риска: SDLC artifact coverage и agentic frameworks coverage.

## Что прочитать

```text
AGENTS.md
work/discourse.md
work/source-precedence.md
work/approved-ai-sdlc-plan.md
work/theory-source-map-ai-driven-sdlc.md
work/baseline-restore-rule.md
work/anchor-case-baseline-restore-rule.md
work/anchor-seed-spdd-old-site.md
work/anchor-seed-gas-town-old-site.md
work/workflow-stages.md
work/case-dossier-protocol.md
work/anti-catalog-audit.md
work/source-depth-audit.md
work/anti-degradation-audit.md
```

## Что создать

Создайте или подготовьте к созданию:

```text
work/SDLC_ARTIFACT_COVERAGE_AUDIT.md
work/AGENTIC_FRAMEWORKS_COVERAGE_AUDIT.md
work/PLAN_PATCH_RECOMMENDATIONS.md
```

Если audit требует устойчивого архитектурного решения, предложите ADR-like decision file, но остановитесь на human gate перед изменением утверждённого плана.

## Как работать

SDLC artifact coverage audit проверяет не источники вообще, а артефакты lifecycle: prompt, spec, PRD, requirements, plan.md, ADR, RFC, handoff, research.md, task graph, acceptance criteria, test plan, benchmark, CI evidence, PR description, review comments, release plan, migration plan, rollback plan, runbook, incident report, postmortem, threat model, security review, audit log, ownership/dependency/deprecation/changelog artifacts.

Agentic frameworks coverage audit проверяет operational methodologies и frameworks: Spec Kit, GSD, BMAD, OpenSpec, Spec Kitty, Reversa и другие релевантные кандидаты. Их нужно оценивать по роли в lifecycle, а не добавлять как каталог.

## Завершение

После audit обновите `work/discourse.md`: впишите, какие audit-файлы созданы, какие gaps найдены, какие plan patches предложены и где остановились у human gate.
