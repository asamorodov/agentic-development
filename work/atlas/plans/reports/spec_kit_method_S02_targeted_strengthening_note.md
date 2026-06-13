# S02 note: `spec_kit_method`

## Problems found

- Первичный S01-план уже имел правильную форму, но местами был слишком близок к generic blueprint: Spec Kit мог превратиться в общий обзор specification-driven development или в справочник команд.
- Article contract недостаточно явно показывал основной путь читателя: от намерения о фиче к спецификации, плану, задачам, реализации, evidence and repair.
- Визуальный слой был отмечен, но нужно было сильнее зафиксировать, что локальный Fowler SDD asset — контекстный, а Spec Kit-specific screenshots/diagrams должны идти как real image candidates, а не как текстовая реконструкция.
- Full 25-pass queue требовала отдельного ответа на вопрос: подходит ли она именно этой статье, а не просто наследуется из blueprint.

## Decisions

- Сохранить полную 25-pass очередь и финальную проверку, потому что Spec Kit одновременно является методом, инструментом, repo workflow, набором command templates/scripts/integrations and пограничным случаем specification cluster.
- Усилить article contract вокруг feature intent → specification → plan/tasks → implementation/evidence.
- Сделать source-depth priorities article-specific: official docs, repository surface, command templates, scripts, integrations, constitution/checklists, human confirmation, verification, caveats and boundaries.
- Зафиксировать две главные деградации для final gate: generic SDD overview and command dump without lifecycle explanation.

## Changes made

- Обновлён статус target-group plan до S02-усиленного.
- Переписан `Article contract`.
- Полностью усилен раздел `Почему очередь подходит статье`.
- Усилены P04–P08, P09–P10, P11–P13, P14–P16 and Final verification.
- Добавлен раздел `S02 integrated strengthening`.
- Статья не писалась, article-writing package не собирался.

## Remaining known debts

- `work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md` отсутствует в snapshot; это сохраняется как provenance debt.
- C5/A10 sync pending остаётся optional later sync, не blocker для текущего target-group plan.
