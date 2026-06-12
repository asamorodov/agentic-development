# Report: atlas article target-plan manufactury plan

Статус: создан отдельный план для будущего meta-package, который будет создавать и улучшать target-group plans статей концептуально-технического атласа.

## Что зафиксировано

- Meta-package запускается на машине с развёрнутым репозиторием; входные архивы и досье от пользователя не требуются.
- Объект работы — target-group plans статей, а не сами статьи.
- Список статей берётся из known dossier-backed set, зафиксированного в плане; внешние источники не создают новые article topics.
- Для каждой статьи применяется короткий цикл S01–S05: создать план, свободно отремонтировать, усилить основную мысль и границы, проверить встроенные требования и исправить найденное, поставить readiness stamp.
- S04 обязан исправлять найденные дефекты в plan file, а не только записывать их в report.
- После всех статей выполняются cross-plan consistency repair, readiness matrix and boundary matrix.

## Созданный документ

```text
work/theory-writing/ATLAS_ARTICLE_TARGET_PLAN_MANUFACTORY_PLAN.md
```

## Обновлённые документы

- `START.md`
- `work/theory-writing/ATLAS_ARTICLE_PACKAGE_BLUEPRINT.md`
- `work/theory-writing/WORKING_DOCUMENTS_MAP.md`
- `work/discourse.md`
- `work/APPLY_NOTES.md`
- `work/COMMIT_MESSAGE.txt`
- `work/checks.json`

## Проверка

- План не создаёт сами статьи атласа.
- План не собирает executor packages для статей.
- План указывает, что запуск происходит в развёрнутом репозитории без входных файлов от пользователя.
- План содержит known dossier-backed article set.
- План содержит S01–S05 для каждой статьи, включая S04 как check-and-fix pass.
